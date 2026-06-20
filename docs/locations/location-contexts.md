---
title: "Location Contexts"
wiki_source: "Modding:Location contexts"
permalink: /Modding:Location_contexts/
category: locations
tags: [location-contexts, format, player-actions, season, weather, music, advanced, location-context-ids]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains location contexts. This is an advanced guide for
modders.

## Format

Custom contexts can be created by editing the new
`Data/LocationContexts` asset, and setting the context name in the
location's `LocationContext`
<a href="Modding_Maps" class="wikilink" title="map property">map
property</a>.

The data asset consists of a string → model lookup, where the key is the
<a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> of the
location context and the value is a model with these fields:

### Player actions

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AllowRainTotem</samp></p></td>
<td><p><em>(Optional)</em> Whether a <a href="Rain_Totem"
class="wikilink" title="rain totem">rain totem</a> can be used to force
rain in this context tomorrow. If false, using a rain totem here will
show a "<em>this item can't be used here</em>" message instead.</p></td>
</tr>
<tr>
<td><p><samp>RainTotemAffectsContext</samp></p></td>
<td><p><em>(Optional)</em> If set, using a rain totem here will change
the weather in the given context ID. For example, rain totems in the
desert change weather in the valley.</p></td>
</tr>
<tr>
<td><p><samp>MaxPassOutCost</samp></p></td>
<td><p><em>(Optional)</em> When the player passes out (due to <a
href="energy" class="wikilink" title="exhaustion">exhaustion</a> or at
2am) in this context, the maximum amount of <a href="gold"
class="wikilink" title="gold">gold</a> lost. If omitted or set to
<samp>-1</samp>, uses the same value as the <samp>Default</samp> context
( by default).</p></td>
</tr>
<tr>
<td><p><samp>PassOutMail</samp></p></td>
<td><p><em>(Optional)</em> When the player passes out (due to <a
href="energy" class="wikilink" title="exhaustion">exhaustion</a> or at
2am) in this context, the possible <a href="Modding_Mail_data"
class="wikilink" title="letter IDs">letter IDs</a> to add to their
mailbox (if they haven't received it before). If multiple letters are
valid, one will be chosen randomly (unless one specifies
<samp>SkipRandomSelection</samp>).</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry in the list.</p></td>
</tr>
<tr>
<td><p><samp>Mail</samp></p></td>
<td><p>The <a href="Modding_Mail_data" class="wikilink"
title="letter ID">letter ID</a> to add.</p>
<p>The game will look for an existing letter ID in
<samp>Data/mail</samp> in this order (where &lt;billed&gt; is
<samp>Billed</samp> if they lost <a href="gold" class="wikilink"
title="gold">gold</a> or <samp>NotBilled</samp> otherwise, and
&lt;gender&gt; is <samp>Female</samp> or <samp>Male</samp>):</p>
<ul>
<li><samp>&lt;letter id&gt;_&lt;billed&gt;_&lt;gender&gt;</samp></li>
<li><samp>&lt;letter id&gt;_&lt;billed&gt;</samp></li>
<li><samp>&lt;letter id&gt;</samp></li>
</ul>
<p>If no match is found in <samp>Data/mail</samp>, the game will send
<samp>passedOut2</samp> instead.</p>
<p>If the mail ID starts with <samp>passedOut</samp>, <samp>{0}</samp>
in the letter text will be replaced with the gold amount lost, and it
won't appear in the <a href="collections" class="wikilink"
title="collections">collections</a> page.</p></td>
</tr>
<tr>
<td><p><samp>MaxPassOutCost</samp></p></td>
<td><p><em>(Optional)</em> The maximum amount of <a href="gold"
class="wikilink" title="gold">gold</a> lost. This is applied after the
context's <samp>MaxPassOutCost</samp> (i.e. the context's value is used
to calculate the random amount, then this field caps the result).
Defaults to unlimited.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry is active. Defaults to always
true.</p></td>
</tr>
<tr>
<td><p><samp>SkipRandomSelection</samp></p></td>
<td><p><em>(Optional)</em> If true, send this mail if the
<samp>Condition</samp> matches instead of choosing a random valid mail.
Default false.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>PassOutLocations</samp></p></td>
<td><p><em>(Optional)</em> When the player passes out (due to <a
href="energy" class="wikilink" title="exhaustion">exhaustion</a> or at
2am) in this context <em>and</em> they started the day in a different
location context, the locations where they'll wake up. (If the player
started the day in the same context, they'll wake up in the last bed
they slept in instead.)</p>
<p>If the selected location doesn't contain a bed and doesn't have the
<a href="#New_map_properties" class="wikilink"
title="AllowWakeUpWithoutBed map property"><samp>AllowWakeUpWithoutBed</samp>
map property</a>, the player will wake up in the farmhouse instead.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry in the list.</p></td>
</tr>
<tr>
<td><p><samp>Location</samp></p></td>
<td><p>The internal location name.</p></td>
</tr>
<tr>
<td><p><samp>Position</samp></p></td>
<td><p>The <em>default</em> tile position within the location, specified
as an object with <samp>X</samp> and <samp>Y</samp> fields. If the
location has any bed furniture, they'll be placed in the first bed found
instead.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry is active. Defaults to always
applied.</p></td>
</tr>
</tbody>
</table>
<p>If no locations are specified or none match, the player will wake up
in their bed at home.</p></td>
</tr>
<tr>
<td><p><samp>ReviveLocations</samp></p></td>
<td><p><em>(Optional)</em> If the player just got knocked out in combat,
the location names where they'll wake up.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry in the list.</p></td>
</tr>
<tr>
<td><p><samp>Location</samp></p></td>
<td><p>The internal location name.</p></td>
</tr>
<tr>
<td><p><samp>Position</samp></p></td>
<td><p>The tile position within the location, specified as an object
with <samp>X</samp> and <samp>Y</samp> fields.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry is active. Defaults to always
applied.</p></td>
</tr>
</tbody>
</table>
<p>If the selected location has a standard <a href="Modding_Event_data"
class="wikilink" title="event">event</a> with the exact key
<samp>PlayerKilled</samp> (with no <samp>/</samp> or preconditions in
the key), that event will play when the player wakes up and the game
will apply the lost items or <a href="gold" class="wikilink"
title="gold">gold</a> logic. The game won't track this event, so it'll
repeat each time the player is revived. If there's no such event, the
player will wake up without an event, and no items or gold will be
lost.</p>
<p>If no locations are specified or none match, the player will wake up
at <a href="Harvey&#39;s_Clinic" class="wikilink"
title="Harvey&#39;s clinic">Harvey's clinic</a>.</p></td>
</tr>
</tbody>
</table>

### Season

| field | effect |
|----|----|
| `SeasonOverride` | *(Optional)* The season which is always active for locations within this context (one of `spring`, `summer`, `fall`, or `winter`). For example, setting `summer` will make it always <a href="summer" class="wikilink" title="summer">summer</a> there regardless of the calendar season. If not set, the calendar season applies. |

### Weather

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>WeatherConditions</samp></p></td>
<td><p><em>(Optional)</em> The weather logic to apply for locations in
this context (ignored if <samp>CopyWeatherFromLocation</samp> is set).
Defaults to always sunny. If multiple are specified, the first matching
weather is applied.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry in the list.</p></td>
</tr>
<tr>
<td><p><samp>Weather</samp></p></td>
<td><p>The <a href="#Custom_weather" class="wikilink"
title="weather ID">weather ID</a> to set.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether to apply the weather. Defaults to always
applied.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>CopyWeatherFromLocation</samp></p></td>
<td><p><em>(Optional)</em> The <samp>Name</samp> (i.e. unique ID) of the
location context from which to inherit weather.</p></td>
</tr>
</tbody>
</table>

If a <a href="#Custom_passive_festivals" class="wikilink"
title="passive festival">passive festival</a> is active in any location
within this context, the weather is sunny for the entire context
regardless of these fields.

### Music

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DefaultMusic</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Audio" class="wikilink"
title="cue ID">cue ID</a> for the music to play when the player is in
the location, unless overridden by a <samp>Music</samp> map property.
Despite the name, this has a higher priority than the seasonal music
fields below. Ignored if omitted.</p></td>
</tr>
<tr>
<td><p><samp>DefaultMusicCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
returns whether the <samp>DefaultMusic</samp> field should be applied
(if more specific music isn't playing). Defaults to always
true.</p></td>
</tr>
<tr>
<td><p><samp>DefaultMusicDelayOneScreen</samp></p></td>
<td><p><em>(Optional)</em> When the player warps and the music changes,
whether to silence the music and play the ambience (if any) until the
next warp (similar to the default valley locations). Default
false.</p></td>
</tr>
<tr>
<td><p><samp>Music</samp></p></td>
<td><p><em>(Optional)</em> A list of <a href="Modding_Audio"
class="wikilink" title="cue IDs">cue IDs</a> to play before noon in this
location unless it's raining, there's a <samp>Music</samp> map property,
or the context has a <samp>DefaultMusic</samp> value. If multiple values
are specified, the game will play one per day in sequence.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p><em>(Optional)</em> A <a
href="Modding_Common_data_field_types#Unique_string_ID" class="wikilink"
title="unique string ID">unique string ID</a> which identifies this
entry within the list. Defaults to the <samp>Track</samp>
value.</p></td>
</tr>
<tr>
<td><p><samp>Track</samp></p></td>
<td><p>The <a href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_audio"
class="wikilink" title="audio track ID">audio track ID</a> to
play.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry applies. Default true.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>DayAmbience</samp><br />
<samp>NightAmbience</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Audio" class="wikilink"
title="cue ID">cue ID</a> for the background ambience to play when
there's no music active, depending on the <a href="Day_Cycle"
class="wikilink" title="time of day">time of day</a>. Both default to
none.</p></td>
</tr>
<tr>
<td><p><samp>PlayRandomAmbientSounds</samp></p></td>
<td><p><em>(Optional)</em> Whether to play random outdoor ambience
sounds depending on factors like the season and time of day (e.g. birds,
crickets, and mysterious groan sounds in the rain). This is unrelated to
the <samp>DayAmbience</samp> and <samp>NightAmbience</samp> fields.
Default true.</p></td>
</tr>
</tbody>
</table>

### Advanced

| field | effect |
|----|----|
| `CustomFields` | The <a href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry. |

## Location context IDs

The base game defines these location context IDs:

| context ID | about |
|----|----|
| `Default` | The Stardew Valley region, including all the main areas like the farm, beach, mountain, town, etc. The constant for C# mods is `LocationContexts.DefaultId`. |
| `Desert` | The <a href="desert" class="wikilink" title="desert">desert</a> region. The constant for C# mods is `LocationContexts.DesertId`. |
| `Island` | The <a href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a> region. The constant for C# mods is `LocationContexts.IslandId`. |

## For C# mods

- `LocationContexts::Require` can be used to require that a specific
  entry in `Data/LocationContexts` exists. It gets a location context by
  ID, throwing if the context does not exist.

## See also

- <a href="Modding_Location_data" class="wikilink"
  title="Modding:Location data">Modding:Location data</a>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Контекст_локаций" class="wikilink"
title="ru:Модификации:Контекст локаций">ru:Модификации:Контекст
локаций</a> <a href="zh_模组_地点上下文" class="wikilink"
title="zh:模组:地点上下文">zh:模组:地点上下文</a>
