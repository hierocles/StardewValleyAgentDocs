---
title: "Outdated"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, outdated-unimplemented-or-unknown, see-also]
---
### Outdated, unimplemented, or unknown

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
<td><p><samp>break</samp></p></td>
<td><p>| Does absolutely nothing as the method handler has no
body.</p></td>
<td><p>|<a href="#break" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>eventtest</samp></p></td>
<td><p>| <em>Syntax</em>: <code>eventtest</code>
&lt;S:locationName&gt;,&lt;I:eventIndex&gt;</p>
<p>Sets <samp>Game1.eventTest</samp> using the specified arguments.
Defaults are "" and 0 respectively. This field is not accessed
elsewhere.</p></td>
<td><p>|<a href="#eventtest" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>eventtestspecific</samp></p></td>
<td><p>| <em>Syntax</em>: <code>eventtestspecific</code>
&lt;S:whichEvents&gt;,[...]</p>
<p>Sets <samp>Game1.eventTest</samp> with the specified arguments.
Arguments are interpreted as an array of strings. This field is not
accessed elsewhere.</p></td>
<td><p>|<a href="#eventtestspecific" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>lantern</samp></p></td>
<td><p>| Adds a lantern to your inventory which looks like an axe and
will softlock the player when trying to use it; <a href="#canmove"
class="wikilink" title="canmove">canmove</a> can be used to fix the soft
lock.</p></td>
<td><p>|<a href="#lantern" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>refuel</samp></p></td>
<td><p>| Sets lantern fuel to maximum. As the lantern was not fully
implemented, this doesn't do much.</p></td>
<td><p>|<a href="#refuel" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>stoprafting</samp></p></td>
<td><p>| Sets an internal <samp>isRafting</samp> flag to false. As
rafting was not fully implemented, this doesn't do much.</p></td>
<td><p>|<a href="#stoprafting" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## See also

- <a href="Multiplayer#Chat" class="wikilink" title="Chat commands">Chat
  commands</a> for information about commands used in the chat window
  and <a href="Modding_Chat_Commands" class="wikilink"
  title="Modding:Chat Commands">Modding:Chat Commands</a> to add custom
  chat commands.
- <a href="Modding_Modder_Guide_APIs_Console" class="wikilink"
  title="Modding:Modder Guide/APIs/Console">Modding:Modder
  Guide/APIs/Console</a> to add custom commands from a SMAPI mod.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Команды_для_отладки" class="wikilink"
title="ru:Модификации:Команды для отладки">ru:Модификации:Команды для
отладки</a> <a href="zh_模组_控制台命令" class="wikilink"
title="zh:模组:控制台命令">zh:模组:控制台命令</a>
