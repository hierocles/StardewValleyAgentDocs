---
title: "Custom Wedding Events"
wiki_source: "Modding:Custom wedding events"
permalink: /Modding:Custom_wedding_events/
category: npcs
tags: [custom-wedding-events, format, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents how the game stores and parses data for
<a href="Marriage#The_Wedding" class="wikilink"
title="wedding">wedding</a> events. This is an advanced guide for mod
developers.

## Format

The <a href="Marriage#The_Wedding" class="wikilink"
title="wedding">wedding</a> event can now be changed by editing the
`Data\Weddings` data asset, which consists of a data model with two
relevant fields (listed below).

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>EventScript</samp></p></td>
<td><p>The <a href="Modding_Event_data" class="wikilink"
title="event scripts">event scripts</a> which play the wedding. The game
will use the script for the spouse NPC/player if it exists, otherwise
it'll use the default script.</p>
<p>This consists of a string → string dictionary, where...</p>
<ul>
<li>The key is an NPC internal name (like <samp>Abigail</samp>), unique
player ID, or <samp>default</samp> for the default script (which handles
marrying either an NPC or player);</li>
<li>The value is a <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the event script to play.</li>
</ul>
<p>The event scripts also have access to three extra tokens:</p>
<table>
<thead>
<tr>
<th><p>token</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>[SetupContextualWeddingAttendees]</samp></p></td>
<td><p>The concatenated <samp>Setup</samp> values for each of the
<samp>Attendees</samp> present in the wedding.</p></td>
</tr>
<tr>
<td><p><samp>[ContextualWeddingCelebrations]</samp></p></td>
<td><p>The concatenated <samp>Celebration</samp> values for each of the
<samp>Attendees</samp> present in the wedding.</p></td>
</tr>
<tr>
<td><p><samp>[SpouseActor]</samp></p></td>
<td><p>The actor ID for the NPC or other player being married (like
<samp>Abigail</samp> for an NPC or <samp>farmer2</samp> for a player).
This can be used in event commands like
<code>faceDirection [SpouseActor] 1</code>.</p>
<p>(You can also use <samp>spouse</samp> as an actor ID, but that will
only work when marrying an NPC.)</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Attendees</samp></p></td>
<td><p>The other NPCs which should attend the wedding (unless they're
the spouse). This consists of a string → model lookup, where the key is
the internal NPC name, and the value is a model with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ID</samp></p></td>
<td><p>The internal NPC name.</p></td>
</tr>
<tr>
<td><p><samp>Setup</samp></p></td>
<td><p>The NPC's tile position and facing direction when they attend.
This is equivalent to field index 2 in the <a
href="Modding_Event_data#Basic_format" class="wikilink"
title="event basic data">event basic data</a>.</p></td>
</tr>
<tr>
<td><p><samp>Celebration</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Event_data"
class="wikilink" title="event script">event script</a> to run during the
celebration, like <samp>faceDirection Pierre 3 true</samp> which makes
Pierre turn to face left. This can contain any number of script
commands.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the NPC should attend. Defaults to true.</p></td>
</tr>
<tr>
<td><p><samp>IgnoreUnlockConditions</samp></p></td>
<td><p><em>(Optional)</em> Whether to add the NPC even if their entry in
<samp>Data/Characters</samp> has an <samp>UnlockConditions</samp> field
which doesn't match. Default false.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

## See also

- See <a href="Modding_Event_data" class="wikilink"
  title="Modding:Event data">Modding:Event data</a> for more information
  about event scripting.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Пользовательские_свадебные_события"
class="wikilink"
title="ru:Модификации:Пользовательские свадебные события">ru:Модификации:Пользовательские
свадебные события</a> <a href="zh_模组_自定义婚礼事件" class="wikilink"
title="zh:模组:自定义婚礼事件">zh:模组:自定义婚礼事件</a>
