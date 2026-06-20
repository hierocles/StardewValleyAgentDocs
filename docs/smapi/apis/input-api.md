---
title: "Input Api"
wiki_source: "Modding:Modder Guide/APIs/Input"
permalink: /Modding:Modder_Guide/APIs/Input/
category: smapi
tags: [input, apis, check-button-state, check-cursor-position, send-input, suppress-input, data-structures, sbutton]
---
<div style="float: right; border: 2px solid rgb(0, 116, 72); background: #A1DEE2; padding: 0.75em; padding-top: 0.5em; margin: 0 0 2em 2em;">

<span style="font-size: larger;">**Creating SMAPI mods**
<a href="File_SMAPI_mascot.png" class="wikilink" title="25px">25px</a></span>

------------------------------------------------------------------------

- <a href="Modding_Modder_Guide_Get_Started" class="wikilink"
  title="Get started">Get started</a>
- <a href="Modding_Modder_Guide_Game_Fundamentals" class="wikilink"
  title="Game fundamentals">Game fundamentals</a>
- <a href="Modding_Modder_Guide_Test_and_Troubleshoot" class="wikilink"
  title="Test &amp; troubleshoot">Test &amp; troubleshoot</a>
- <a href="Modding_Modder_Guide_Release" class="wikilink"
  title="Release">Release</a>
- <a href="Modding_Modder_Guide_APIs" class="wikilink"
  title="API reference">API reference</a>

  Basic SMAPI APIs:

  - <a href="Modding_Modder_Guide_APIs_Mod_structure" class="wikilink"
    title="Mod structure">Mod structure</a>
  - <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
    title="Manifest">Manifest</a>
  - <a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
    title="Events">Events</a>
  - <a href="Modding_Modder_Guide_APIs_Config" class="wikilink"
    title="Configuration">Configuration</a>
  - <a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
    title="Load &amp; edit content">Load &amp; edit content</a>
  - <a href="Modding_Modder_Guide_APIs_Data" class="wikilink"
    title="Data">Data</a>
  - <a href="Modding_Modder_Guide_APIs_Input" class="wikilink"
    title="Input">Input</a>
  - <a href="Modding_Modder_Guide_APIs_Logging" class="wikilink"
    title="Logging">Logging</a>
  - <a href="Modding_Modder_Guide_APIs_Reflection" class="wikilink"
    title="Reflection">Reflection</a>
  - <a href="Modding_Modder_Guide_APIs_Multiplayer" class="wikilink"
    title="Multiplayer">Multiplayer</a>
  - <a href="Modding_Modder_Guide_APIs_Translation" class="wikilink"
    title="Translation">Translation</a>
  - <a href="Modding_Modder_Guide_APIs_Update_checks" class="wikilink"
    title="Update checks">Update checks</a>
  - <a href="Modding_Modder_Guide_APIs_Utilities" class="wikilink"
    title="Utilities">Utilities</a>

  Advanced SMAPI APIs:

  - <a href="Modding_Modder_Guide_APIs_Content_Packs" class="wikilink"
    title="Content packs">Content packs</a>
  - <a href="Modding_Modder_Guide_APIs_Console" class="wikilink"
    title="Mod console commands">Mod console commands</a>
  - <a href="Modding_Modder_Guide_APIs_Integrations" class="wikilink"
    title="Mod integrations">Mod integrations</a>
  - <a href="Modding_Modder_Guide_APIs_Harmony" class="wikilink"
    title="Harmony patching">Harmony patching</a>
- <a href="Modding_Index#Advanced_topics" class="wikilink"
  title="Specific guides">Specific guides</a>

</div>

←
<span style="font-size: smaller;"><a href="Modding_Index" class="wikilink"
title="Modding:Index">Modding:Index</a></span>
<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

The input API lets you check and suppress controller/keyboard/mouse
state.

## APIs

### Check button state

<dl>

<dt>

`IsDown`

</dt>

<dd>

You can check if any <a href="#SButton" class="wikilink"
title="controller/keyboard/mouse button">controller/keyboard/mouse
button</a> is currently pressed by calling the `IsDown(button)` method.
For example:

``` c#
bool isShiftPressed = this.Helper.Input.IsDown(SButton.LeftShift) || this.Helper.Input.IsDown(SButton.RightShift);
```

</dd>

<dt>

`GetState`

</dt>

<dd>

For more finetuned control, you can check the
<a href="#SButton" class="wikilink" title="button">button</a> state
relative to the previous game tick:

``` c#
SButtonState state = this.Helper.Input.GetState(SButton.LeftShift);
bool isDown = (state == SButtonState.Pressed || state == SButtonState.Held);
```

Available button states:

| previous tick | current tick | resulting state |
|---------------|--------------|-----------------|
| up            | up           | `None`          |
| up            | down         | `Pressed`       |
| down          | down         | `Held`          |
| down          | up           | `Released`      |

</dd>

</dl>

### Check cursor position

The `GetCursorPosition()` method provides the
<a href="#ICursorPosition" class="wikilink"
title="cursor position in three coordinate systems">cursor position in
three coordinate systems</a>.

For example:

``` c#
// draw text at the cursor position
ICursorPosition cursorPos = this.Helper.Input.GetCursorPosition();
Game1.spriteBatch.DrawString(Game1.smallFont, "some text", cursorPos.ScreenPixels, Color.Black);
```

### Send input

You can send <a href="#SButton" class="wikilink"
title="controller/keyboard/mouse button input">controller/keyboard/mouse
button input</a> programmatically, which is equivalent to the player
physically pressing the button.

| method  | effect                    |
|---------|---------------------------|
| `Press` | Mark a button as pressed. |

For example, this will make the player move left once:

``` c#
SButton moveLeft = Game1.options.moveLeftButton[0].ToSButton();
this.Helper.Input.Press(moveLeft);
```

The button will be released on the next input tick by default; it can be
'pressed' again each tick to hold it down.

### Suppress input

You can prevent the game from handling any
<a href="#SButton" class="wikilink"
title="controller/keyboard/mouse button press">controller/keyboard/mouse
button press</a> (including clicks) by *suppressing* it. This
suppression will remain in effect until the player releases the button.
This won't prevent other mods from handling it.

| method | effect |
|----|----|
| `Suppress` | Suppress a specified <a href="#SButton" class="wikilink"
title="SButton"><samp>SButton</samp></a> value. |
| `SuppressActiveKeybinds` | Suppress every button that's part of a specified <a href="#KeybindList" class="wikilink"
title="KeybindList"><samp>KeybindList</samp></a>'s activated keybinds. |
| `SuppressScrollWheel` | Suppress a mouse wheel scroll. |
| `IsSuppressed` | Get whether a specified <a href="#SButton" class="wikilink"
title="SButton"><samp>SButton</samp></a> value is currently suppressed. |

For example:

``` c#
// prevent game from seeing that LeftShift is pressed
this.Helper.Input.Suppress(SButton.LeftShift);

// that works for clicks too:
this.Helper.Input.Suppress(SButton.MouseLeft);

// check if a button is being suppressed:
bool suppressed = this.Helper.Input.IsSuppressed(SButton.LeftShift);
```

Side-effects:

- The <a href="Modding_Modder_Guide_APIs_Events#Input.ButtonReleased"
  class="wikilink"
  title="ButtonReleased event"><samp>ButtonReleased</samp> event</a>
  will be raised on the next tick for the suppressed input.
- Methods like `helper.Input.IsDown(button)` and
  `helper.Input.GetState(button)` will show the button as released for
  the duration of the suppression, even if it's physically still
  pressed. You can use `helper.Input.IsSuppressed(button)` to check if
  that's the case (it will only be true until the button is physically
  released):
  ``` c#
  bool isPhysicallyDown = helper.Input.IsDown(button) || helper.Input.IsSuppressed(button);
  ```

## Data structures

### SButton

SMAPI's `SButton` is a constant which includes every
\[<https://docs.microsoft.com/en-us/previous-versions/windows/xna/bb975202(v%3dxnagamestudio.40>)
controller\],
\[<https://docs.microsoft.com/en-us/previous-versions/windows/xna/bb197781(v%3dxnagamestudio.40>)
keyboard\], and
\[<https://docs.microsoft.com/en-us/previous-versions/windows/xna/bb198097(v%3dxnagamestudio.40>)
mouse\] button. SMAPI events use this to let you handle button presses
without needing separate code for each. See
<a href="Modding_Player_Guide_Key_Bindings" class="wikilink"
title="Modding:Player Guide/Key Bindings">Modding:Player Guide/Key
Bindings</a> for a list of values.

SMAPI provides extensions to convert any of the other constants to
`SButton`:

``` c#
SButton key = Keys.A.ToSButton(); // SButton.A
SButton button = Buttons.A.ToSButton(); // SButton.ControllerA
SButton input = new InputButton(true).ToSButton(); // SButton.MouseLeft
```

You can also convert `SButton` to the other constants. This uses a
`TryGet` approach since `SButton` is a superset of the others (*e.g.,*
you can't convert `SButton.ControllerA` to a keyboard value):

``` c#
SButton value = SButton.A;
if (value.TryGetKeyboard(out Keys key))
   ...;
if (value.TryGetController(out Buttons button))
   ...;
if (value.TryGetStardewInput(out InputButton input))
   ...;
```

Two last extensions let you check how the button is mapped in the game:

``` c#
SButton button = SButton.MouseLeft;
if (button.IsUseToolButton())
   // use tool
else if (button.IsActionButton())
   // perform action
```

You can use `SButton` values directly in your
<a href="Modding_Modder_Guide_APIs_Config" class="wikilink"
title="config model">config model</a>, but
`[[#KeybindList|KeybindList]]` is recommended instead in most cases.

### KeybindList

SMAPI's `KeybindList` utility lets you manage an arbitrary set of
keybindings. A *keybind list* has any number of *keybinds*, each of
which has any number of
<a href="#SButton" class="wikilink" title="button codes">button
codes</a>. For example, the keybind list `"F2, LeftShift + S"` would be
pressed if (a) `F2` is pressed, *or* (b) both `LeftShift` and `S` are
pressed.

You can use a `KeybindList` directly in
<a href="Modding_Modder_Guide_APIs_Config" class="wikilink"
title="your config.json model">your <samp>config.json</samp> model</a>:

<table>
<thead>
<tr>
<th><p>C# model</p></th>
<th><p> </p></th>
<th><p>JSON file</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="kw">class</span> ModConfig</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="op">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>   <span class="kw">public</span> KeybindList ToggleKey <span class="op">{</span> <span class="kw">get</span><span class="op">;</span> <span class="kw">set</span><span class="op">;</span> <span class="op">}</span> <span class="op">=</span> KeybindList<span class="op">.</span><span class="fu">Parse</span><span class="op">(</span><span class="st">&quot;LeftShift + F2&quot;</span><span class="op">);</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="op">}</span></span></code></pre></div></td>
<td><p>→</p></td>
<td><div class="sourceCode" id="cb2"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;ToggleKey&quot;</span><span class="fu">:</span> <span class="st">&quot;LeftShift + F2&quot;</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

And you can then check whether it's pressed directly in your code. For
example, in a
<a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="ButtonsChanged event handler"><samp>ButtonsChanged</samp> event
handler</a>:

``` c#
private void OnButtonsChanged(object sender, ButtonsChangedEventArgs e)
{
   if (this.Config.ToggleKey.JustPressed())
   {
      // perform desired action
   }
}
```

The `KeybindList` provides a number of methods depending on your use
case:

<table>
<thead>
<tr>
<th><p>member</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>KeybindList.Parse(…)</code><br />
<code>KeybindList.TryParse(…)</code></p></td>
<td><p>Parse a keybind string like <code>"F2, LeftShift + S"</code> into
a keybind list.</p></td>
</tr>
<tr>
<td><p><code>IsBound</code></p></td>
<td><p>Whether the keybind list has any keys bound. For example, this
would be false for the strings <code>"None"</code> or
<code>""</code>.</p></td>
</tr>
<tr>
<td><p><code>Keybinds</code></p></td>
<td><p>The individual keybinds. In most cases you shouldn't use these
directly.</p></td>
</tr>
<tr>
<td><p><code>GetState()</code></p></td>
<td><p>Get the overall <a href="#Check_button_state" class="wikilink"
title="keybind state relative to the previous tick">keybind state
relative to the previous tick</a>. This state is transitive across
keybinds; <em>e.g.,</em> if the player releases one keybind and
immediately presses another within the list, the overall state is
<samp>Held</samp>.</p></td>
</tr>
<tr>
<td><p><code>IsDown()</code></p></td>
<td><p>Get whether any keybind in the list is currently down
(<em>i.e.,</em> the player pressed or is holding down the
keys).</p></td>
</tr>
<tr>
<td><p><code>JustPressed()</code></p></td>
<td><p>Get whether the player just activated the keybind during the
current tick (<em>i.e.,</em> <code>GetState()</code> returns
<samp>Pressed</samp> instead of <samp>Held</samp>).</p></td>
</tr>
<tr>
<td><p><code>GetKeybindCurrentlyDown()</code></p></td>
<td><p>Get the individual <samp>Keybind</samp> in the list which is
currently down, if any. If there are multiple keybinds down, the first
one is returned.</p></td>
</tr>
<tr>
<td><p><code>ToString()</code></p></td>
<td><p>Get a string representation of the input binding (<em>e.g.,</em>
<code>"F2, LeftShift + S"</code>).</p></td>
</tr>
</tbody>
</table>

Caveats:

- **Don't use the `ButtonPressed`
  <a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
  title="event">event</a> to check keybinds**, since it's raised once
  for each button pressed. If the player presses two keys at once, your
  keybind would be activated twice. Use `ButtonsChanged` instead.

### ICursorPosition

SMAPI's `ICursorPosition` provides the cursor position in four
coordinate systems:

- `AbsolutePixels` is the pixel position relative to the top-left corner
  of the in-game map, adjusted for
  <a href="Modding_Modder_Guide_Game_Fundamentals#Zoom_level"
  class="wikilink" title="zoom">zoom</a> but not
  <a href="Modding_Modder_Guide_Game_Fundamentals#UI_scaling"
  class="wikilink" title="UI scaling">UI scaling</a>.
- `ScreenPixels` is the pixel position relative to the top-left corner
  of the visible screen, adjusted for
  <a href="Modding_Modder_Guide_Game_Fundamentals#Zoom_level"
  class="wikilink" title="zoom">zoom</a> but not
  <a href="Modding_Modder_Guide_Game_Fundamentals#UI_scaling"
  class="wikilink" title="UI scaling">UI scaling</a>.
- `Tile` is the
  <a href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
  title="tile position">tile position</a> under the cursor.
- `GrabTile` is the tile position that the game considers under the
  cursor for the purposes of clicking actions. This automatically
  accounts for controller mode. This may be different than `Tile` if
  that's too far from the player.

This is returned by the `this.Helper.Input.GetCursorPosition()` method
and in the event args for some input events.

**The pixel positions are *not* adjusted for
<a href="Modding_Modder_Guide_Game_Fundamentals#UI_scaling"
class="wikilink" title="UI scaling">UI scaling</a>** (*i.e.,* they're
non-UI mode). Whether you need UI or non-UI positions depends how you're
using them, so you can use `cursorPos.GetScaledAbsolutePixels()` or
`cursorPos.GetScaledScreenPixels()` to adjust them automatically for the
current mode or `Utility.ModifyCoordinatesForUIScale` to always get UI
mode coordinates.

## See also

- <a href="Modding_Modder_Guide_APIs_Events#Input" class="wikilink"
  title="Input events">Input events</a>
- <a href="Modding_Player_Guide_Key_Bindings" class="wikilink"
  title="Modding:Player Guide/Key Bindings">Modding:Player Guide/Key
  Bindings</a> for a list of valid `SButton` values

<a href="ru_Модификации_Руководство_мододела_API_Ввод" class="wikilink"
title="ru:Модификации:Руководство мододела/API/Ввод">ru:Модификации:Руководство
мододела/API/Ввод</a>
<a href="zh_模组_制作指南_APIs_Input" class="wikilink"
title="zh:模组:制作指南/APIs/Input">zh:模组:制作指南/APIs/Input</a>
