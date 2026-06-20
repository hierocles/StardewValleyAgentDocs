---
title: "Key Bindings"
wiki_source: "Modding:Player Guide/Key Bindings"
permalink: /Modding:Player_Guide/Key_Bindings/
category: player-guide
tags: [player-guide, key-bindings, how-to, configure-a-mod-s-bindings, disable-a-mod-s-key-binding, find-the-code-for-a-key, use-key-bindings-on-android, button-codes]
---
}\|1}}}} }

` |}`\
`   |unofficial`\
`   |}`\
`     |broken`\
`     |ok`\
`   }}`\
` }}`

}}}} }}} }}} }}} }}} \|- class="mod" style="line-height: 1em;
\|ok\|optional=background: \#9F9; \|workaround\|unofficial=background:
\#CF9; \|broken=background: \#F99; \|obsolete\|abandoned=background:
\#999}}" id="" data-id="" data-name="" data-author=""
}\|data-cf-id="}"}} }\|data-curseforge-id="}"}}
}\|data-curseforge-key="}"}} }\|data-nexus-id="}"}}
}\|data-moddrop-id="}"}} }\|data-github="}"}}
}\|data-custom-source="}"}} data-url="}}}}}}}}}" data-status=""
}\|data-broke-in="}"}} }\|data-unofficial-version="}"}}
}\|data-unofficial-url="}"}} }\|data-pr="}"}}
}\|data-content-pack-for="}"}} }\|data-dev-note="}"}}
}\|data-map-local-versions="}"}} }\|data-map-remote-versions="}"}}
}\|data-change-update-keys="}"}} \| }\|\[}
\]\|}\|\|}\|\[<https://www.curseforge.com/stardewvalley/mods/>}
\]\|}\|\[<https://community.playstarbound.com/resources/>} \]\|}\|\[}
\]\|}}}}}}}}}} \| \| <span class="mod-summary">

`|ok         = ✓ }|}|use latest version.}}`\
`|optional   = ✓ }|}|use optional download.}}`\
`|unofficial = ⚠ broken}|, use [} unofficial update]}| (`<small>`}`</small>`)}}|}}}.`\
`|workaround = ⚠ broken, }`\
`|broken     = ↻ broken, }|}||not updated yet.|not open-source.}}}}`\
`|obsolete   = ✖ }|}|remove this mod (obsolete).}}`\
`|abandoned  = ✖ }|}|remove this mod (no longer maintained).}}`\
`|unknown    = ☐ }|}|not tested yet.}}`

}}</span>\|optional\|[^1]}} }\|\
⚠ }} \| <small>}</small> \| }\|\[<https://github.com/>} source\]\|}\|\[}
source\]\|<span style="color: red; font-size: 0.85em; opacity: 0.5;">closed
source</span>}}}} \| class="no-wrap"\|<small>
<a href="#" class="wikilink" title="#">#</a> }\| \[} PR\]}}
}\|<abbr title="}">\[dev note\]</abbr>}}
}\|1\|0}}\|}\|1\|0}}\|\|<abbr title="The mod data is invalid: can't specify CurseForge key or ID without the other.">\[⚠
invalid data\]</abbr>}}</small>

Some mods let you edit key bindings, which are controller/keyboard/mouse
buttons which do something in-game. This page explains how to configure
them. (This works for any mod using SMAPI's standard APIs.)

## How to…

### Configure a mod's bindings

1.  Install the mod
    (<a href="Modding_Player_Guide_Getting_Started" class="wikilink"
    title="see player guide">see player guide</a>).
2.  Run SMAPI at least once with the mod to let it generate its config
    file.
3.  Edit `config.json` in the mod's folder with a text editor.
4.  Change the key options using
    <a href="#Button_codes" class="wikilink" title="the values below">the
    values below</a>. (On macOS, make sure it doesn't change to curly
    quotes.)

Note that some mods may not be configurable.

### Disable a mod's key binding

You can use `"None"` to disable a key binding.

### Find the code for a key

<a href="#Button_codes" class="wikilink" title="Button codes"><em>Button
codes</em></a> below shows all available codes, but sometimes it's not
clear which one applies (*e.g.,* for non-English keyboards). Here's how
to check:

1.  Launch the game.
2.  In the SMAPI console window, enter the `log_context` command.
3.  In the game, press the keys you want to test.
4.  The SMAPI console will list the codes for the keys it received.

### Use key bindings on Android

- You can <a href="#Mobile" class="wikilink"
  title="bind physical mobile buttons">bind physical mobile buttons</a>,
  but there aren't many available.
- Otherwise you can use the mod to add on-screen buttons you can tap to
  send them to installed mods. See the mod page for how to use it.
- Additionally, if you use a controller on mobile, controller
  assignments will still work, both with vanilla controls, as well as
  with mods. Just use the normal controller keys.

## Button codes

### Keyboard

common keys
{\| class="wikitable"

\|- ! value ! description \|- \| `A` through `Z` \| The letter keys. \|-
\| `D0` through `D9` \| The number keys. \|- \| `Down`, `Left`,\
`Right`, `Up` \| The arrow keys. \|- \| `F1` through `F24` \| The
function keys. \|- \| `Apps` \| The applications or menu () key,
typically located next to your right key. \|- \| `Back` \| The backspace
( or ) key. \|- \| `CapsLock` \| The or key. \|- \| `Enter` \| The or
key. \|- \| `Escape` \| The key. \|- \| `LeftAlt`, `RightAlt` \| The
keys. \|- \| `LeftControl`, `RightControl` \| The keys. \|- \|
`LeftShift`, `RightShift` \| The or keys. \|- \| `LeftWindows`,
`RightWindows` \| The Windows keys. \|- \| `OemCloseBrackets` \| The
key. \|- \| `OemComma` \| The key. \|- \| `OemMinus` \| The key. \|- \|
`OemOpenBrackets` \| The key. \|- \| `OemPeriod` \| The key. \|- \|
`OemPipe` \| The key. \|- \| `OemPlus` \| The key. \|- \| `OemQuestion`
\| The key on a US standard keyboard. \|- \| `OemQuotes` \| The or key
on a US standard keyboard. \|- \| `OemSemicolon` \| The key on a US
standard keyboard. \|- \| `OemTilde` \| The key on a US standard
keyboard. \|- \| `Space` \| The space bar. \|- \| `Tab` \| The key. \|}

numeric pad
{\| class="wikitable"

\|- ! value ! description \|- \| `Numpad0` through `Numpad9` \| The
numpad number keys. \|- \| `Add` \| The numpad key. \|- \| `Subtract` \|
The numpad key. \|- \| `Divide` \| The numpad key. \|- \| `Multiply` \|
The numpad key. \|- \| `NumLock` \| The numeric lock, , , or key. \|}

control keys (above arrow keys)
{\| class="wikitable"

\|- ! value ! description \|- \| `Delete` \| The key. \|- \| `End` \|
The key. \|- \| `Insert` \| The key. \|- \| `PageDown`, `PageUp` \| The
and keys. \|- \| `Pause` \| The key. \|- \| `PrintScreen` \| The key.
\|- \| `Scroll` \| The key. \|}

uncommon keys
{\| class="mw-collapsible mw-collapsed wikitable"

\|- ! \|- ! value ! description \|- \| `BrowserBack` \| The browser back
key. \|- \| `BrowserFavorites` \| The browser favorites key. \|- \|
`BrowserForward` \| The browser forward key. \|- \| `BrowserHome` \| The
browser start and home key. \|- \| `BrowserRefresh` \| The browser
refresh key. \|- \| `BrowserSearch` \| The browser search key. \|- \|
`BrowserStop` \| The browser stop key. \|- \| `ChatPadGreen` \| The
green ChatPad key. \|- \| `ChatPadOrange` \| The orange ChatPad key. \|-
\| `Crsel` \| The cursor select key. \|- \| `Decimal` \| The decimal
key. \|- \| `EraseEof` \| The erase EOF key. \|- \| `Execute` \| The
execute key. \|- \| `Exsel` \| The execute selection key. \|- \| `Help`
\| The help key. \|- \| `Home` \| The home key. \|- \| `ImeConvert` \|
The IME convert key. \|- \| `ImeNoConvert` \| The IME no-convert key.
\|- \| `Kana` \| The Kana key on Japanese keyboards. \|- \| `Kanji` \|
The Kanji key on Japanese keyboards. \|- \| `LaunchApplication1` \| The
Start Application 1 key. \|- \| `LaunchApplication2` \| The Start
Application 2 key. \|- \| `LaunchMail` \| The Start Mail key. \|- \|
`MediaNextTrack` \| The Next Track key. \|- \| `MediaPlayPause` \| The
Play/Pause Media key. \|- \| `MediaPreviousTrack` \| The Previous Track
key. \|- \| `MediaStop` \| The Stop Media key. \|- \| `Oem8` \| Varies
by keyboard. \|- \| `OemAuto` \| OEM Auto key. \|- \| `OemBackslash` \|
The The OEM angle bracket or backslash key on the RT 102 key keyboard.
\|- \| `OemClear` \| The OEM clear key. \|- \| `OemCopy` \| The OEM copy
key. \|- \| `OemEnlW` \| The OEM Enlarge Window key. \|- \| `PA1` \| The
PA1 key. \|- \| `Play` \| The play key. \|- \| `Print` \| The key. \|-
\| `ProcessKey` \| The IME process key. \|- \| `Select` \| The select
key. \|- \| `SelectMedia` \| The select media key. \|- \| `Separator` \|
The separator key. \|- \| `Sleep` \| The computer sleep key. \|- \|
`VolumeDown`, `VolumeUp` \| The volume down/up keys. \|- \| `VolumeMute`
\| The volume mute keys. \|- \| `Zoom` \| The zoom key. \|}

### Controller

<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ControllerA</samp>, <samp>ControllerB</samp>,<br />
<samp>ControllerX</samp>, <samp>ControllerY</samp></p></td>
<td><p>The main buttons.</p></td>
</tr>
<tr>
<td><p><samp>ControllerBack</samp></p></td>
<td><p>The 'BACK' button on an XBox controller.</p></td>
</tr>
<tr>
<td><p><samp>ControllerStart</samp></p></td>
<td><p>The 'START' button.</p></td>
</tr>
<tr>
<td><p><samp>BigButton</samp></p></td>
<td><p>The 'big button' on the XBox Big Button controller.</p></td>
</tr>
<tr>
<td><p><samp>DPadDown</samp>, <samp>DPadLeft</samp><br />
<samp>DPadRight</samp>, <samp>DPadUp</samp></p></td>
<td><p>The directional pad buttons.</p></td>
</tr>
<tr>
<td><p><samp>LeftShoulder</samp>, <samp>RightShoulder</samp></p></td>
<td><p>The bumper (shoulder) buttons.</p></td>
</tr>
<tr>
<td><p><samp>LeftTrigger</samp>, <samp>RightTrigger</samp></p></td>
<td><p>The trigger buttons.</p></td>
</tr>
<tr>
<td><p><samp>LeftStick</samp>, <samp>RightStick</samp></p></td>
<td><p>The left/right thumbsticks when clicked or pressed as a
button.</p></td>
</tr>
<tr>
<td><p><samp>LeftThumbstickDown</samp>,
<samp>LeftThumbstickLeft</samp>,<br />
<samp>LeftThumbstickRight</samp>, <samp>LeftThumbstickUp</samp></p></td>
<td><p>The left thumbstick when pushed in a direction.</p></td>
</tr>
<tr>
<td><p><samp>RightThumbstickDown</samp>,
<samp>RightThumbstickLeft</samp>,<br />
<samp>RightThumbstickRight</samp>,
<samp>RightThumbstickUp</samp></p></td>
<td><p>The right thumbstick when pushed in a direction.</p></td>
</tr>
</tbody>
</table>

### Mouse

| value                | description                                   |
|----------------------|-----------------------------------------------|
| `MouseLeft`          | The left mouse button.                        |
| `MouseRight`         | The right mouse button.                       |
| `MouseMiddle`        | The middle mouse button.                      |
| `MouseX1`, `MouseX2` | The extended mouse buttons (varies by mouse). |

### Mobile

| value                    | description                 |
|--------------------------|-----------------------------|
| `VolumeUp`, `VolumeDown` | The volume up/down buttons. |

## Device mappings

### Steam Deck

The Steam deck is mapped as a controller (see
<a href="#Controller" class="wikilink"
title="controller codes">controller codes</a>), and you can remap
buttons using Steam Input. Here's how the different Steam Deck buttons
are mapped by default:

<table>
<thead>
<tr>
<th><p>button</p></th>
<th><p>mapped as</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>A, B, X, Y<br />
left/right shoulder<br />
left/right trigger buttons<br />
left/right thumbstick<br />
D-Pad<br />
Start<br />
Select</p></td>
<td><p>Sends the equivalent controller codes.</p></td>
</tr>
<tr>
<td><p>left touchpad</p></td>
<td><p>Sends equivalent D-Pad codes when touching the edges (e.g. left
edge is <samp>DPadLeft</samp>).</p></td>
</tr>
<tr>
<td><p>right touchpad</p></td>
<td><p>Sends right thumbstick codes.</p></td>
</tr>
<tr>
<td><p>'Back grip' buttons (L4, L5, R4, R5)</p></td>
<td><p>Not sent to the game by default, unless mapped to a key in Steam
Input.</p></td>
</tr>
<tr>
<td><p><br />
</p></td>
<td><p>Not sent to the game.</p></td>
</tr>
</tbody>
</table>

You can also rebind physical keys in the Steam Deck settings:

1.  Go to *Controller Settings \> Edit Layout*.
2.  Choose the button to rebind.
3.  Choose *Command Page \> Keyboard*.
4.  Choose the keyboard button to bind it to.
5.  Now when you press that physical button in-game, it'll send the new
    keyboard code instead.

## Multi-key bindings

Mods using SMAPI 3.9+ features can support multi-key bindings. That lets
you combine multiple
<a href="#Button_codes" class="wikilink" title="button codes">button
codes</a> into a combo keybind, and list alternate keybinds. For
example, `"LeftShoulder, LeftControl + S"` will apply if `LeftShoulder`
is pressed, *or* if both `LeftControl` and `S` are pressed.

Some things to keep in mind:

- The order doesn't matter, so `"LeftControl + S"` and
  `"S + LeftControl"` are equivalent.
- SMAPI doesn't prevent mods from using overlapping hotkeys. For
  example, if one mod uses `"S"` and the other mod uses
  `"LeftControl + S"`, pressing `LeftControl` and `S` will activate
  both.

## See also

- <a href="Controls" class="wikilink" title="Controls">Controls</a> for
  the game's default bindings
- <a href="Modding_Modder_Guide_APIs_Input" class="wikilink"
  title="SMAPI input events">SMAPI input events</a> for mod authors

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="de_Modding_Spieleranleitung_Tastenbelegung" class="wikilink"
title="de:Modding:Spieleranleitung/Tastenbelegung">de:Modding:Spieleranleitung/Tastenbelegung</a>
<a href="es_Modding_Guía_del_jugador_Enlaces_de_teclas" class="wikilink"
title="es:Modding:Guía del jugador/Enlaces de teclas">es:Modding:Guía
del jugador/Enlaces de teclas</a> <a
href="ru_Модификации_Руководство_по_использованию_модификаций_Привязка_клавиш"
class="wikilink"
title="ru:Модификации:Руководство по использованию модификаций/Привязка клавиш">ru:Модификации:Руководство
по использованию модификаций/Привязка клавиш</a>
<a href="zh_模组_使用指南_按键绑定" class="wikilink"
title="zh:模组:使用指南/按键绑定">zh:模组:使用指南/按键绑定</a>

[^1]:
