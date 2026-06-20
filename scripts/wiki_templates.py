"""Expand MediaWiki templates used in the Stardew Valley modding wiki export."""

from __future__ import annotations

import html
import re
from typing import Callable


def decode_entities(text: str) -> str:
    return html.unescape(text)


def slugify_anchor(text: str) -> str:
    text = decode_entities(text).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")


def expand_param_notation(text: str) -> str:
    """Convert {{t|TYPE:name}} and {{o|TYPE:name}} to readable notation."""

    def repl_t(match: re.Match[str]) -> str:
        return f"<{match.group(1)}>"

    def repl_o(match: re.Match[str]) -> str:
        return f"[{match.group(1)}]"

    for _ in range(5):
        before = text
        text = re.sub(r"\{\{t\|([^}|]+)\}\}", repl_t, text, flags=re.IGNORECASE)
        text = re.sub(r"\{\{o\|([^}|]+)\}\}", repl_o, text, flags=re.IGNORECASE)
        if text == before:
            break
    return text


def find_template_end(text: str, start: int, *, inside_template: bool = False) -> int:
    """Return index after closing }} for the template opened at or before start."""
    depth = 1 if inside_template else 0
    i = start
    while i < len(text) - 1:
        if text[i : i + 2] == "{{":
            depth += 1
            i += 2
            continue
        if text[i : i + 2] == "}}":
            depth -= 1
            i += 2
            if depth == 0:
                return i
            continue
        i += 1
    return len(text)


def parse_template_params(body: str) -> dict[str, str]:
    params: dict[str, str] = {}
    positional = 0
    for line in body.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        line = line.lstrip("|").strip()
        if "=" not in line:
            positional += 1
            params[str(positional)] = line
            continue
        key, _, value = line.partition("=")
        params[key.strip().lower()] = value.strip()
    return params


def parse_named_params(body: str) -> dict[str, str]:
    params: dict[str, str] = {}
    for part in re.split(r"(?<!\|)\|(?!\|)", body):
        part = part.strip()
        if not part or "=" not in part:
            continue
        key, _, value = part.partition("=")
        params[key.strip().lower()] = value.strip()
    return params


def expand_cmd_template(params: dict[str, str]) -> str:
    """Expand /cmd into wikitable rows Pandoc can parse."""
    command = params.get("command", "").strip()
    par = expand_param_notation(params.get("params", "").strip())
    desc = expand_param_notation(params.get("desc", "").strip())
    example = expand_param_notation(params.get("example", "").strip())

    commands = [c.strip() for c in command.split(",") if c.strip()]
    primary = commands[0] if commands else "command"
    cmd_html = "<br />".join(f"<samp>{c}</samp>" for c in commands)

    body_parts: list[str] = []
    if par:
        body_parts.append(f"''Syntax'': <code>{primary}</code> {par}")
    body_parts.append(desc)
    if example:
        examples = [e.strip() for e in example.split(";") if e.strip()]
        if len(examples) == 1:
            body_parts.append(f"''Example:'' {examples[0]}")
        else:
            body_parts.append("''Examples:''")
            for ex in examples:
                body_parts.append(f"* {ex}")

    desc_cell = "\n\n".join(body_parts)
    return (
        f'|- id="{primary}"\n'
        f"|{cmd_html}\n"
        f"||\n"
        f"{desc_cell}\n"
        f"||[[#{primary}|#]]\n"
        "|-\n"
    )


def expand_event_template(params: dict[str, str]) -> str:
    group = params.get("group", "").strip()
    names_raw = params.get("name", "").strip()
    desc = expand_param_notation(params.get("desc", "").strip())
    names = [n.strip() for n in names_raw.split(",") if n.strip()]
    primary = names[0] if names else "Event"

    lines = [f"==== {primary} ====", ""]
    if len(names) > 1:
        lines.append("''Also known as:'' " + ", ".join(f"<code>{n}</code>" for n in names[1:]))
        lines.append("")
    if group:
        lines.append(f"''Group:'' <code>{group}</code>")
        lines.append("")
    lines.append(desc)
    lines.append("")

    args = []
    for i in range(1, 11):
        arg_name = params.get(f"arg name {i}", "").strip()
        if not arg_name:
            break
        args.append(
            (
                arg_name,
                params.get(f"arg type {i}", "").strip(),
                expand_param_notation(params.get(f"arg desc {i}", "").strip()),
            )
        )

    if args:
        lines.append("''Event arguments:''")
        lines.append("")
        lines.append('{| class="wikitable"')
        lines.append("|-")
        lines.append("! Argument !! Type !! Description")
        for name, typ, adesc in args:
            lines.append("|-")
            lines.append(f"| <code>{name}</code> || <code>{typ}</code> || {adesc}")
        lines.append("|}")
        lines.append("")

    return "\n".join(lines).strip() + "\n\n"


def expand_note_box(params: dict[str, str]) -> str:
    note_type = params.get("type", "note").strip().lower()
    text = params.get("text", "").strip()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"'''(.*?)'''", r"'''\1'''", text)
    label = note_type.upper() if note_type != "note" else "NOTE"
    return f"'''{label}:''' {decode_entities(text)}\n\n"


def expand_github(params: dict[str, str]) -> str:
    positional = [params[k] for k in sorted(params, key=lambda x: int(x) if x.isdigit() else 999) if k.isdigit()]
    if len(positional) >= 2:
        return f"[https://github.com/{positional[0]} {positional[1]}]"
    repo = params.get("1", "")
    label = params.get("2", repo)
    return f"[https://github.com/{repo} {label}]" if repo else ""


def expand_nexus_mod(params: dict[str, str]) -> str:
    mod_id = params.get("1", "")
    label = params.get("2", "Nexus mod")
    return (
        f"[https://www.nexusmods.com/stardewvalley/mods/{mod_id} {label}]"
        if mod_id
        else ""
    )


def expand_key_template(params: dict[str, str]) -> str:
    key = params.get("1", params.get("key", "")).strip()
    return f"<code>{key}</code>" if key else ""


def expand_toc(_params: dict[str, str]) -> str:
    return ""


TEMPLATE_HANDLERS: dict[str, Callable[[dict[str, str]], str]] = {
    "note box": expand_note_box,
    "toc": expand_toc,
    "github": expand_github,
    "nexus mod": expand_nexus_mod,
    "key": expand_key_template,
}


def expand_named_template(name: str, body: str) -> str:
    name_lower = name.strip().lower()
    params = parse_template_params(body) if "\n|" in body or body.strip().startswith("|") else parse_named_params(body)

    if name_lower in ("/cmd", "cmd"):
        return expand_cmd_template(params)
    if name_lower in ("/event", "event"):
        return expand_event_template(params)

    handler = TEMPLATE_HANDLERS.get(name_lower)
    if handler:
        return handler(params)
    return ""


def expand_balanced_templates(text: str, names: set[str]) -> str:
    pattern = re.compile(r"\{\{/(" + "|".join(re.escape(n) for n in names) + r")\b", re.IGNORECASE)
    result: list[str] = []
    pos = 0
    while True:
        match = pattern.search(text, pos)
        if not match:
            result.append(text[pos:])
            break
        result.append(text[pos : match.start()])
        end = find_template_end(text, match.start() + 2, inside_template=True)
        full = text[match.start() : end]
        inner = full[2:-2]
        name_end = inner.find("\n")
        if name_end == -1:
            name_end = inner.find("|")
        if name_end == -1:
            name = inner.strip()
            body = ""
        else:
            name = inner[:name_end].strip().lstrip("/")
            body = inner[name_end:]
        expanded = expand_named_template(f"/{name}", body)
        result.append(expanded if expanded else full)
        pos = end
    return "".join(result)


def expand_templates(text: str, pages: dict[str, str] | None = None) -> str:
    pages = pages or {}

    text = re.sub(r"\{\{../header\}\}", pages.get("Modding:Modder Guide/header", ""), text)
    text = re.sub(r"\{\{../../header\}\}", pages.get("Modding:Modder Guide/header", ""), text)
    text = re.sub(
        r"\{\{modding player guide header\}\}",
        pages.get("Modding:Mod compatibility/entry", ""),
        text,
        flags=re.IGNORECASE,
    )

    text = expand_param_notation(text)
    text = expand_balanced_templates(text, {"cmd", "event"})

    for _ in range(20):
        before = text
        pos = 0
        parts: list[str] = []
        pattern = re.compile(r"\{\{([^/#][^|{}]*?)(?:\|([\s\S]*?))?\}\}")
        for match in pattern.finditer(text):
            parts.append(text[pos : match.start()])
            expanded = expand_named_template(match.group(1).strip(), match.group(2) or "")
            parts.append(expanded if expanded else match.group(0))
            pos = match.end()
        parts.append(text[pos:])
        text = "".join(parts)
        if text == before:
            break

    return text


def strip_remaining_templates(text: str) -> str:
    """Remove leftover {{...}} blocks without breaking nested braces."""
    result: list[str] = []
    i = 0
    while i < len(text):
        if text.startswith("{{", i):
            end = find_template_end(text, i + 2, inside_template=True)
            i = end
            continue
        result.append(text[i])
        i += 1
    return "".join(result)


def strip_unexpanded_templates(text: str) -> str:
    """Remove remaining template/parser syntax that breaks Pandoc."""
    text = re.sub(r"\{\{#switch:[\s\S]*?\}\}", "", text)
    text = re.sub(r"\{\{#ifeq:[\s\S]*?\}\}", "", text)
    text = re.sub(r"\{\{#if:[\s\S]*?\}\}", "", text)
    text = re.sub(r"\{\{#arraydefine:[\s\S]*?\}\}", "", text)
    text = re.sub(r"\{\{#arrayprint:[\s\S]*?\}\}", "", text)
    text = re.sub(r"\{\{#arrayindex:[\s\S]*?\}\}", "", text)
    text = re.sub(r"\{\{#arraysize:[\s\S]*?\}\}", "", text)
    text = re.sub(r"\{\{anchorencode:[^}]+\}\}", "", text)
    text = re.sub(r"\{\{FULLPAGENAME\}\}", "", text)
    text = re.sub(r"\{\{NAMESPACE\}\}", "", text)
    text = re.sub(r"<noinclude>[\s\S]*?</noinclude>", "", text)
    text = re.sub(r"<includeonly>|</includeonly>", "", text)
    text = strip_remaining_templates(text)
    text = re.sub(r"</nowiki>\}\}", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def preprocess_wikitext(text: str, pages: dict[str, str] | None = None) -> str:
    text = expand_templates(text, pages)
    return strip_unexpanded_templates(text)
