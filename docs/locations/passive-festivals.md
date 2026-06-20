---
title: "Passive Festivals"
wiki_source: "Modding:Passive Festival data"
permalink: /Modding:Passive_Festival_data/
category: locations
tags: [passive-festival-data, overview, data-format, npc-schedules, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and uses passive festival data.
This is an advanced guide for mod developers.

## Overview

A *passive festival* is a
<a href="festivals" class="wikilink" title="festival">festival</a> like
the <a href="Night_Market" class="wikilink" title="Night Market">Night
Market</a>. They replace a location for a period of time, the player can
enter/leave them anytime, and time continues passing while at the
festival. Passive festivals have their data stored in the
`Data/PassiveFestivals` asset.

## Data format

The `Data/PassiveFestivals` asset consists of a string → model lookup,
where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  festival.
- The value is a model with the fields listed below.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DisplayName</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the display name
shown on the <a href="calendar" class="wikilink"
title="calendar">calendar</a>.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p>The <a href="season" class="wikilink" title="season">season</a>
when the festival becomes active.</p></td>
</tr>
<tr>
<td><p><samp>StartDay</samp><br />
<samp>EndDay</samp></p></td>
<td><p>The days of month when the festival becomes active.</p></td>
</tr>
<tr>
<td><p><samp>StartTime</samp></p></td>
<td><p>The time of day when the festival opens each day.</p></td>
</tr>
<tr>
<td><p><samp>StartMessage</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the in-game <a
href="wikipedia_Pop-up_notification" class="wikilink"
title="toast notification">toast notification</a> shown when the
festival begins each day.</p></td>
</tr>
<tr>
<td><p><samp>MapReplacements</samp></p></td>
<td><p>The locations to swap for the duration of the festival. Despite
the field name, this swaps <strong>locations</strong> (e.g. as added by
<samp>CustomLocations</samp> using <a href="Modding_Content_Patcher"
class="wikilink" title="Content Patcher">Content Patcher</a>), and not
the location's map asset.</p>
<p>This is specified as a string → string lookup, where the key is the
original location to replace and the value is the new location. Both use
the internal location name, as shown by the mod. For example, this swaps
the <samp>Beach</samp> location with <samp>BeachNightMarket</samp>
during the <a href="Night_Market" class="wikilink"
title="Night Market">Night Market</a>:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;MapReplacements&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Beach&quot;</span><span class="fu">:</span> <span class="st">&quot;BeachNightMarket&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the festival is enabled (subject to the other fields
like <samp>StartDay</samp> and <samp>EndDay</samp>). Defaults to always
enabled.</p></td>
</tr>
<tr>
<td><p><samp>ShowOnCalendar</samp></p></td>
<td><p><em>(Optional)</em> Whether the festival appears on the <a
href="calendar" class="wikilink" title="calendar">calendar</a>, using
the same iridium-star icon as the <a href="Calendar#Winter"
class="wikilink" title="Night Market">Night Market</a>. Default
true.</p></td>
</tr>
<tr>
<td><p><samp>DailySetupMethod</samp><br />
<samp>CleanupMethod</samp></p></td>
<td><p><em>(Optional)</em> A C# method which applies custom logic when
the day starts (<samp>DailySetupMethod</samp>) and/or overnight after
the last day of the festival (<samp>CleanupMethod</samp>).</p>
<p>These must be specified in the form <samp>&lt;full type name&gt;:
&lt;method name&gt;</samp> (like <samp>ExampleMod.Namespace.Type,
ExampleMod: MethodName</samp>). The methods must be static, take zero
arguments, and return void.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

## NPC schedules

When a passive festival is active, NPCs will check for
<a href="Modding_Schedule_data" class="wikilink"
title="a schedule entry">a schedule entry</a> in this order:

<table>
<thead>
<tr>
<th><p>syntax</p></th>
<th><p>summary</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>&lt;festival ID&gt;_&lt;festival day&gt;</samp></p></td>
<td><p>Applies on the given date. The &lt;festival day&gt; is relative,
so <samp>1</samp> matches the festival <samp>StartDay</samp>.<br />
<small>Example: <samp>NightMarket_3</samp> or
<samp>marriage_NightMarket_3</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;festival ID&gt;</samp></p></td>
<td><p>Applies if there's no date-specific entry.<br />
<small>Example: <samp>NightMarket</samp> or
<samp>marriage_NightMarket</samp></small></p></td>
</tr>
</tbody>
</table>

If the NPC is married to a player, they'll add a `marriage_` prefix to
the keys (like `marriage_<festival ID>_<festival day>`) and ignore any
entry without the prefix.

## See also

<a href="Modding_Festival_data" class="wikilink"
title="Modding:Festival data">Modding:Festival data</a> for data about
other types of festivals.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Пассивные_фестивали" class="wikilink"
title="ru:Модификации:Пассивные фестивали">ru:Модификации:Пассивные
фестивали</a> <a href="zh_模组_被动节日" class="wikilink"
title="zh:模组:被动节日">zh:模组:被动节日</a>
