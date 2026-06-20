---
title: "Input"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, input]
---
### Input

`this.Helper.Events.Input` has events raised when the player uses a
controller, keyboard, or mouse in some way. They can be used with the
<a href="Modding_Modder_Guide_APIs_Input" class="wikilink"
title="input API">input API</a> to access more info or suppress input.

<table>
<thead>
<tr>
<th><p>event</p></th>
<th><p>summary</p>
<h4 id="buttonschanged">ButtonsChanged</h4>
<p><em>Group:</em> <code>Input</code></p>
<p>Raised after the player pressed/released any buttons on the keyboard,
mouse, or controller. This includes mouse clicks. If the player
pressed/released multiple keys at once, this is only raised once.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Pressed</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#SButton"
class="wikilink" title="SButton[]"><samp>SButton[]</samp></a></p></td>
<td><p>The buttons that were pressed since the previous tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Held</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#SButton"
class="wikilink" title="SButton[]"><samp>SButton[]</samp></a></p></td>
<td><p>The buttons that were held since the previous tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Released</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#SButton"
class="wikilink" title="SButton[]"><samp>SButton[]</samp></a></p></td>
<td><p>The buttons that were released since the previous tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Cursor</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#Check_cursor_position"
class="wikilink"
title="ICursorPosition"><samp>ICursorPosition</samp></a></p></td>
<td><p>The cursor position and grab tile.</p></td>
</tr>
</tbody>
</table>
<h4 id="buttonpressed">ButtonPressed</h4>
<p><em>Also known as:</em> <code>ButtonReleased</code></p>
<p><em>Group:</em> <code>Input</code></p>
<p>Raised after the player pressed/released a keyboard, mouse, or
controller button. This includes mouse clicks. If the player
pressed/released multiple keys at once, this is raised for each button
pressed.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Button</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#SButton"
class="wikilink" title="SButton"><samp>SButton</samp></a></p></td>
<td><p>The button pressed or released.</p></td>
</tr>
<tr>
<td><p><samp>e.Cursor</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#Check_cursor_position"
class="wikilink"
title="ICursorPosition"><samp>ICursorPosition</samp></a></p></td>
<td><p>The cursor position and grab tile.</p></td>
</tr>
<tr>
<td><p><samp>e.IsDown</samp></p></td>
<td><p><em><code>method</code></em><code> returns </code><samp>bool</samp></p></td>
<td><p>Indicates whether a given button is currently pressed.</p></td>
</tr>
<tr>
<td><p><samp>e.IsSuppressed</samp></p></td>
<td><p><em><code>method</code></em><code> returns </code><samp>bool</samp></p></td>
<td><p>A method which indicates whether a given button was suppressed by
a mod, so the game itself won't see it.</p></td>
</tr>
</tbody>
</table>
<h4 id="cursormoved">CursorMoved</h4>
<p><em>Group:</em> <code>Input</code></p>
<p>Raised after the player moves the in-game cursor.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.OldPosition</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#Check_cursor_position"
class="wikilink"
title="ICursorPosition"><code>ICursorPosition</code></a></p></td>
<td><p>The previous cursor position and grab tile.</p></td>
</tr>
<tr>
<td><p><samp>e.NewPosition</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#Check_cursor_position"
class="wikilink"
title="ICursorPosition"><code>ICursorPosition</code></a></p></td>
<td><p>The current cursor position and grab tile.</p></td>
</tr>
</tbody>
</table>
<h4 id="mousewheelscrolled">MouseWheelScrolled</h4>
<p><em>Group:</em> <code>Input</code></p>
<p>Raised after the player scrolls the mouse wheel.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Position</samp></p></td>
<td><p><a href="Modding_Modder_Guide_APIs_Input#Check_cursor_position"
class="wikilink"
title="ICursorPosition"><code>ICursorPosition</code></a></p></td>
<td><p>The current cursor position and grab tile.</p></td>
</tr>
<tr>
<td><p><samp>e.Delta</samp></p></td>
<td><p><samp>int</samp></p></td>
<td><p>The amount by which the mouse wheel was scrolled since the last
update.</p></td>
</tr>
<tr>
<td><p><samp>e.OldValue</samp><br />
<samp>e.NewValue</samp></p></td>
<td><p><samp>int</samp></p></td>
<td><p>The previous and current scroll value, cumulative since the game
started. Mods should generally use <samp>e.Delta</samp>
instead.</p></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
