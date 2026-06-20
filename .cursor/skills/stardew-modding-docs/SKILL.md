---
name: stardew-modding-docs
description: >-
  Navigate Stardew Valley modding documentation in docs/. Use when answering
  questions about SMAPI, Content Patcher, game data formats, console commands,
  or mod troubleshooting in this repository. Docs are generated via mediawiki-to-gfm.
---

# Stardew Valley Modding Docs

Read files under `docs/` — do not guess formats. Search first:

```bash
python scripts/search_docs.py "schedule npc"
python scripts/search_docs.py --category smapi
```

Concept map: [docs/README.md](../../docs/README.md). Index: [docs/manifest.json](../../docs/manifest.json).

| Intent                         | Folder                |
| ------------------------------ | --------------------- |
| Player install/troubleshooting | `docs/player-guide/`  |
| SMAPI C# mods                  | `docs/smapi/`         |
| Content Patcher                | `docs/content-packs/` |
| NPCs                           | `docs/npcs/`          |
| Items                          | `docs/items/`         |
| Maps/locations                 | `docs/locations/`     |
| Queries/tokens                 | `docs/reference/`     |

Regenerate: `bash scripts/convert.sh`

Related: [stardew-smapi-csharp](../stardew-smapi-csharp/SKILL.md), [stardew-content-patcher](../stardew-content-patcher/SKILL.md)
