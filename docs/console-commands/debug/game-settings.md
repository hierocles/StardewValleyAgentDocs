---
title: "Game Settings"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, game-settings-and-meta-info]
---
### Game settings and meta info

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>conventionmode</samp></p></td>
<td><p>| Toggles convention mode on and off. When on, disables the
resolution and window mode options as well as both "Exit to Title" and
"Exit to Desktop" buttons.</p></td>
<td><p>|<a href="#conventionmode" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>filterLoadMenu</samp></p></td>
<td><p>| <em>Syntax</em>: <code>filterLoadMenu</code>
&lt;searchText&gt;</p>
<p>Filter the current list of saves to those whose player name or farm
name contains the given text.</p></td>
<td><p>|<a href="#filterLoadMenu" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>gamemode</samp></p></td>
<td><p>| <em>Syntax</em>: <code>gamemode</code> &lt;I:mode&gt;</p>
<p>Sets the game mode to the specified value. Details unknown.</p></td>
<td><p>|<a href="#gamemode" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>gamepad</samp></p></td>
<td><p>| Toggles gamepad control options and displays a global message
about whether they are being used or not.</p></td>
<td><p>|<a href="#gamepad" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>inputsim</samp><br />
<samp>is</samp></p></td>
<td><p>| <em>Syntax</em>: <code>inputsim</code> &lt;S:type&gt;</p>
<p>Sets input simulator to the specified type. Valid types are
<samp>spamtool</samp> and <samp>spamlr</samp>. Details unknown.</p></td>
<td><p>|<a href="#inputsim" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>language</samp></p></td>
<td><p>| Brings up the language selection menu.</p></td>
<td><p>|<a href="#language" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>musicvolume</samp><br />
<samp>mv</samp><br />
<samp>m</samp></p></td>
<td><p>| <em>Syntax</em>: <code>musicvolume</code> &lt;D:value&gt;</p>
<p>Sets music volume to the specified value. This is a double-precision
float in the range of <samp>0 - 1</samp>.</p></td>
<td><p>|<a href="#musicvolume" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>nosave</samp><br />
<samp>ns</samp></p></td>
<td><p>| Toggles end of day saving on or off. Outputs a message to the
console with the current saving status.</p></td>
<td><p>|<a href="#nosave" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>performTitleAction</samp><br />
<samp>pta</samp></p></td>
<td><p>| <em>Syntax</em>: <code>performTitleAction</code>
&lt;button&gt;</p>
<p>While on the title screen, jump to a given title submenu.</p></td>
<td><p>|<a href="#performTitleAction" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>save</samp></p></td>
<td><p>| Toggles saving on a new day on/off. Plays a select sound if
toggled on and a deselect sound if toggled off.</p></td>
<td><p>|<a href="#save" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>showplurals</samp></p></td>
<td><p>| Prints (to the console) the plural forms of all items listed in
<samp>Data/ObjectInformation</samp> and
<samp>Data/BigCraftablesInformation</samp>.</p></td>
<td><p>|<a href="#showplurals" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>toggleCheats</samp></p></td>
<td><p>| Enable or disable entering debug commands into the in-game chat
(prefixed with <samp>/</samp>).</p></td>
<td><p>|<a href="#toggleCheats" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>toggleNetCompression</samp></p></td>
<td><p>| Disable (or re-enable) multiplayer compression</p></td>
<td><p>|<a href="#toggleNetCompression" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>toggletimingoverlay</samp><br />
<samp>tto</samp></p></td>
<td><p>| Show an on-screen overlay with basic timing info (e.g. draw
loop times) to help with performance profiling.</p></td>
<td><p>|<a href="#toggletimingoverlay" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>steaminfo</samp><br />
<samp>sdkinfo</samp></p></td>
<td><p>| Outputs information about whether Steam is running and if a
user is logged in.</p></td>
<td><p>|<a href="#steaminfo" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>version</samp></p></td>
<td><p>| Outputs the assembly version number to the console. Note this
is different from the more user-friendly version that can be accessed
from the credits screen. For example, running this command on Stardew
Valley 1.4.3 for Windows will output
<samp>1.3.7286.33936</samp></p></td>
<td><p>|<a href="#version" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>worldMapLines</samp></p></td>
<td><p>| Toggles the <a href="Modding_World_map#Debug_view"
class="wikilink" title="world map&#39;s debug view">world map's debug
view</a>.</p></td>
<td><p>|<a href="#worldMapLines" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>worldMapPosition</samp></p></td>
<td><p>| <em>Syntax</em>: <code>worldMapPosition</code> [includeLog]</p>
<p>Show detailed info to help troubleshoot <a href="Modding_World_map"
class="wikilink" title="world map positioning data">world map
positioning data</a>. If [includeLog] is <samp>true</samp>, it will
print a detailed log of how the current position was determined based on
the <samp>Data/WorldMap</samp> entries.</p></td>
<td><p>|<a href="#worldMapPosition" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
