---
title: "Game State Queries"
wiki_source: "Modding:Game state queries"
permalink: /Modding:Game_state_queries/
category: reference
tags: [game-state-queries, overview, query-format, argument-format, queries-versus-content-patcher-conditions, built-in-queries, meta, date-time]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents **game state queries**, a built-in way to specify
conditions in some of the game's data assets inspired by
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a>'s conditions.

## Overview

### Query format

A query consists of a comma-delimited list of conditions in the form
\<type\> \[arguments\]. The type can be prefixed with `!` to negate it.
The query is true if it's null/blank, or if every listed condition
exists and is true. For example, `!SEASON Spring, WEATHER Here Sun` is
true on sunny
non-<a href="spring" class="wikilink" title="spring">spring</a> days.

**⚠** Game state queries are partly case-sensitive. While some values
are case-insensitive (e.g. both `SEASON Spring` and `SEASON spring` will
work), this isn't consistent. Using the exact capitalization is
recommended to avoid issues.

### Argument format

Game state queries can take space-delimited arguments. For example,
`BUILDINGS_CONSTRUCTED Here Cabins` has two arguments: `Here` and
`Cabins`.

If you have spaces within an argument, you can surround it with quotes
to keep it together. For example,
`BUILDINGS_CONSTRUCTED Here "Junimo Hut"` passes `Junimo Hut` as one
argument. You can escape inner quotes with backslashes, like
`ANY "BUILDINGS_CONSTRUCTED Here \"Junimo Hut\""`.

Remember that quotes and backslashes inside JSON strings need to be
escaped too. For example,
`"Condition": "BUILDINGS_CONSTRUCTED Here \"Junimo Hut\""` will send
`BUILDINGS_CONSTRUCTED Here "Junimo Hut"` to the game code.
Alternatively, you can use single-quotes for the JSON string instead,
like `"Condition": 'BUILDINGS_CONSTRUCTED Here "Junimo Hut"'`.

### Queries versus Content Patcher conditions

When making <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher packs">Content Patcher packs</a>, you may be able
to achieve a certain effect with either `When` conditions or game state
queries (with different formatting in either case, but the same end
result).

Which you use is mainly a performance tradeoff:

- Content Patcher's `When` conditions are highly optimized and cached,
  so thousands of patches can check the same condition without impacting
  performance and the resulting changes are written once to the asset.
  Then there's no performance impact after the asset edit, since it's
  just plain unconditional data. However the asset is reloaded when
  patches are added/removed, which may impact performance if they change
  often in some cases (like reloading a map or indoor/outdoor NPC
  appearance).
- A game state query has no caching, so it can significantly affect
  performance when it's checked often. For example, a thousand game
  state queries checked each update tick means sixty thousand condition
  evaluations per second. On the other hand, game state queries are
  faster in cases where the conditions are checked rarely and doing so
  avoids reloading textures or maps (like `Appearance` in
  `Data/Characters` or `Music` in `Data/Locations`).

## Built-in queries

### Meta

| Condition | effect |
|----|----|
| `ANY <query>+` | Get whether at least one of the listed game state queries match, where each argument is a query. For example, `ANY "SEASON Winter" "SEASON Spring, DAY_OF_WEEK Friday"` is true if (a) it's winter or (b) it's a spring Friday. You can list any number of queries to check. |

You can nest ANY tokens inside of ANY tokens, but you're likely to get
yourself into quote escaping madness if you try. Instead, approach as
Sum of Products.

Here's an example.

     "ANY \"LOCATION_NAME Here BathHouse_Pool\" \"LOCATION_NAME Here BathHouse_MensLocker\" \"LOCATION_NAME Here BathHouse_WomensLocker\" \"LOCATION_NAME Here Beach, WEATHER Here Sun Wind, SEASON Summer\" \"IS_EVENT festival_summer5, \""

Broken down, this means:

- ANY of the following locations: BathHouse_Pool, BathHouse_MensLocker,
  BathHouse_WomensLocker.
- The location Beach but only if it's sunny or windy, and it's summer
- The event (in this case festival) summer5 is active, and
  spacechase0.SurfingFestival is installed, as the `<nowiki>` token will
  either resolve to true or false, which are valid tokens.

Remember: you can token inside GSQ!

### Date & time

<table>
<thead>
<tr>
<th><p>Condition</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DATE_RANGE &lt;min season&gt; &lt;min day&gt; &lt;min
year&gt; [max season] [max day] [max year]</samp></p></td>
<td><p>Whether the calendar date is within the specified range,
inclusively. The max values default to winter (season), 28 (day), and
unlimited (year) if omitted.</p>
<p>For example:</p>
<ul>
<li>Between summer 15 and winter 15 in year one:
<pre><code>DATE_RANGE Summer 15 1 Winter 15 1</code></pre></li>
<li>Or fall 15 or later:</li>
</ul>
<pre><code>DATE_RANGE Fall 15 1</code></pre></td>
</tr>
<tr>
<td><p><samp>DAY_OF_MONTH &lt;day&gt;+</samp></p></td>
<td><p>The day of month. This can be an integer between 1 and 28, or
<samp>even</samp>/<samp>odd</samp> to match on any even/odd day. You can
specify multiple values to match any of them.</p></td>
</tr>
<tr>
<td><p><samp>DAY_OF_WEEK &lt;day&gt;+</samp></p></td>
<td><p>The day of week. This can be an integer between 0 (Sunday) and 6
(Saturday), three-letter English name (like <samp>Fri</samp>), or full
English name (like <samp>Friday</samp>). You can specify multiple values
to match any of them (like <samp>DAY_OF_WEEK Monday Tuesday</samp> for
Monday <em>or</em> Tuesday).</p></td>
</tr>
<tr>
<td><p><samp>DAYS_PLAYED &lt;min&gt; [max]</samp></p></td>
<td><p>Whether &lt;min&gt; to [max] (default unlimited) days have been
played in the current save (including the current one). This always
increments in sync with the date in the base game, but when mods change
the in-game date, they may or may not update this value.</p></td>
</tr>
<tr>
<td><p><samp>IS_FESTIVAL_DAY [location context] [day
offset]</samp></p></td>
<td><p>Whether there's a festival today, with an optional [day offset]
(e.g. 1 for tomorrow).</p>
<p>The [location context] (default <samp>Any</samp>) must be one of
these values:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Any</samp></p></td>
<td><p>Check for a festival anywhere.</p></td>
</tr>
<tr>
<td><p><samp>Here</samp></p></td>
<td><p>Check for a festival in the location context containing the
player.</p></td>
</tr>
<tr>
<td><p><samp>Target</samp></p></td>
<td><p>Check for a festival in the location context containing <a
href="#Target_location" class="wikilink" title="the target location">the
target location</a>.</p></td>
</tr>
<tr>
<td><p><em>any other</em></p></td>
<td><p>Check for a festival in the given location context ID.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>IS_PASSIVE_FESTIVAL_OPEN &lt;id&gt;</samp></p></td>
<td><p>Whether a <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_passive_festivals"
class="wikilink" title="passive festival">passive festival</a> with the
given ID is active today, and the current time is within its opening
hours.</p></td>
</tr>
<tr>
<td><p><samp>IS_PASSIVE_FESTIVAL_TODAY &lt;id&gt;</samp></p></td>
<td><p>Whether a <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_passive_festivals"
class="wikilink" title="passive festival">passive festival</a> with the
given ID is active today.</p></td>
</tr>
<tr>
<td><p><samp>SEASON &lt;season&gt;+</samp></p></td>
<td><p>The season (one of <samp>spring</samp>, <samp>summer</samp>,
<samp>fall</samp>, or <samp>winter</samp>). You can specify multiple
values to match any of them (like <samp>SEASON spring summer</samp> for
spring <em>or</em> summer).</p></td>
</tr>
<tr>
<td><p><samp>SEASON_DAY [&lt;season&gt; &lt;day&gt;]+</samp></p></td>
<td><p>The season (in the same format as <samp>SEASON</samp>) and day
(an integer between 1 and 28). You can specify multiple values to match
any of them (like <samp>SEASON_DAY fall 15 winter 20</samp> for fall 15
<em>or</em> winter 20).</p></td>
</tr>
<tr>
<td><p><samp>TIME &lt;min&gt; [max]</samp></p></td>
<td><p>Whether the current time is between &lt;min&gt; and [max]
(default unlimited) inclusively, specified in <a
href="Modding_Modder_Guide_Game_Fundamentals#Time_format"
class="wikilink" title="26-hour time">26-hour time</a>.</p></td>
</tr>
<tr>
<td><p><samp>YEAR &lt;min&gt; [max]</samp></p></td>
<td><p>Whether the current year is between &lt;min&gt; and [max]
(default unlimited) inclusively.</p></td>
</tr>
</tbody>
</table>

### Events

| Condition | effect |
|----|----|
| `IS_EVENT` | Whether the player is viewing any <a href="Modding_Event_data" class="wikilink" title="event">event</a> or attending any active festival. This doesn't cover passive festivals like the <a href="Night_Market" class="wikilink" title="Night Market">Night
Market</a>. |
| `IS_EVENT <event ID>+` | Whether the player is viewing an <a href="Modding_Event_data" class="wikilink" title="event">event</a> or attending an active festival whose ID matches one of the specified \<event ID\> values. Festivals have IDs in the form `festival_<season><day>` (like `festival_spring13` for the <a href="Egg_Festival" class="wikilink" title="Egg Festival">Egg
Festival</a>). |

### World

<table>
<thead>
<tr>
<th><p>Condition</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>BUILDINGS_CONSTRUCTED &lt;locations&gt; [building type]
[min] [max] [count unbuilt]</samp></p></td>
<td><p>Whether the number of matching buildings is within a range.</p>
<p>For example:</p>
<ul>
<li><code>BUILDINGS_CONSTRUCTED Here</code> checks if any buildings were
constructed in the player's current location.</li>
<li><code>BUILDINGS_CONSTRUCTED Target Cabin</code> checks if there's at
least one cabin in the <a href="#Target_location" class="wikilink"
title="target location">target location</a>.</li>
<li><code>BUILDINGS_CONSTRUCTED All "Junimo Hut" 3 5</code> checks if
there's between 3 and 5 Junimo huts (inclusively) anywhere in the
world.</li>
</ul>
<p>Arguments:</p>
<ul>
<li>&lt;locations&gt;: a <a href="#Target_location" class="wikilink"
title="target location">target location</a>, or <samp>All</samp> to
count buildings in all locations.</li>
<li>[building type]: the building ID in <samp>Data/Buildings</samp> to
count, or <samp>All</samp> to count all building types. Note that
<samp>All</samp> includes default buildings like the farmhouse.</li>
<li>[min]/[max]: the minimum (default 1) and maximum (default unlimited)
count to require.</li>
<li>[count unbuilt]: whether to count buildings that haven't been fully
constructed yet.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>CAN_BUILD_CABIN</samp></p></td>
<td><p>Whether players can build more <a href="cabin" class="wikilink"
title="cabin">cabins</a> (i.e. they haven't reached the maximum number
of player slots yet).</p></td>
</tr>
<tr>
<td><p><samp>CAN_BUILD_FOR_CABINS &lt;building ID&gt;</samp></p></td>
<td><p>Whether there are fewer of the given building constructed than
there are cabins.</p></td>
</tr>
<tr>
<td><p><samp>FARM_CAVE &lt;type&gt;+</samp></p></td>
<td><p>The current <a href="The_Farm#The_Cave" class="wikilink"
title="farm cave">farm cave</a> (one of <samp>Bats</samp>,
<samp>Mushrooms</samp>, or <samp>None</samp>).</p></td>
</tr>
<tr>
<td><p><samp>FARM_NAME &lt;name&gt;</samp></p></td>
<td><p>The name of the farm.</p></td>
</tr>
<tr>
<td><p><samp>FARM_TYPE &lt;type&gt;+</samp></p></td>
<td><p>The <a href="Farm_Maps" class="wikilink" title="farm type">farm
type</a>. The &lt;type&gt; can be one of...</p>
<ul>
<li>a numeric ID for a vanilla farm type: <samp>1</samp> (standard),
<samp>2</samp> (riverland), <samp>3</samp> (forest), <samp>4</samp>
(hilltop), <samp>5</samp> (combat), <samp>6</samp> (four corners), or
<samp>7</samp> (beach);</li>
<li>a readable key for a vanilla farm type: <samp>Standard</samp>,
<samp>Beach</samp>, <samp>Forest</samp>, <samp>FourCorners</samp>,
<samp>Hilltop</samp>, <samp>Riverland</samp>, or
<samp>Wilderness</samp>;</li>
<li>or the ID for a custom farm type.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>FOUND_ALL_LOST_BOOKS</samp></p></td>
<td><p>Whether all the <a href="Lost_Books" class="wikilink"
title="Lost Books">Lost Books</a> for the <a href="museum"
class="wikilink" title="museum">museum</a> have been found.</p></td>
</tr>
<tr>
<td><p><samp>HAS_TARGET_LOCATION</samp></p></td>
<td><p>Whether the <a href="#Target_location" class="wikilink"
title="&#39;Target&#39; location">'<samp>Target</samp>' location</a> is
explicitly set for the current context (ignoring the fallback to the
current player's location).</p></td>
</tr>
<tr>
<td><p><samp>IS_COMMUNITY_CENTER_COMPLETE</samp></p></td>
<td><p>Whether the <a href="Community_Center" class="wikilink"
title="community center">community center</a> has been
repaired.</p></td>
</tr>
<tr>
<td><p><samp>IS_CUSTOM_FARM_TYPE</samp></p></td>
<td><p>Whether the <a href="Farm_Maps" class="wikilink"
title="farm type">farm type</a> is a custom one created by a mod. (This
returns false for mods which edit/replace a vanilla farm type.)</p></td>
</tr>
<tr>
<td><p><samp>IS_GREEN_RAIN_DAY</samp></p></td>
<td><p>Whether the RNG has determined today to be the Green Rain day for
the year.</p></td>
</tr>
<tr>
<td><p><samp>IS_HOST</samp></p></td>
<td><p>Whether the current player is the main/host player.</p></td>
</tr>
<tr>
<td><p><samp>IS_ISLAND_NORTH_BRIDGE_FIXED</samp></p></td>
<td><p>Whether the <a href="Ginger_Island#Island_North" class="wikilink"
title="North Ginger Island">North Ginger Island</a> bridge to the dig
site has been repaired.</p></td>
</tr>
<tr>
<td><p><samp>IS_JOJA_MART_COMPLETE</samp></p></td>
<td><p>Whether the <a href="Joja_Community_Development_Form"
class="wikilink" title="Joja community development form">Joja community
development form</a> has been completed.</p></td>
</tr>
<tr>
<td><p><samp>IS_MULTIPLAYER</samp></p></td>
<td><p>Whether the game is currently in multiplayer mode (regardless of
whether there's multiple players connected).</p></td>
</tr>
<tr>
<td><p><samp>IS_VISITING_ISLAND &lt;name&gt;</samp></p></td>
<td><p>Whether the named NPC is visiting <a href="Ginger_Island"
class="wikilink" title="Ginger Island">Ginger Island</a> today.</p></td>
</tr>
<tr>
<td><p><samp>LOCATION_ACCESSIBLE &lt;name&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_location" class="wikilink"
title="given location">given location</a> is accessible. For vanilla
locations, this is relevant to <samp>CommunityCenter</samp>,
<samp>JojaMart</samp>, <samp>Railroad</samp>, or <samp>Desert</samp>;
any other location will return true unless a mod customizes the
query.</p></td>
</tr>
<tr>
<td><p><samp>LOCATION_CONTEXT &lt;location&gt; &lt;context
ID&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_location" class="wikilink"
title="given location">given location</a> is part of the given <a
href="Modding_Location_contexts" class="wikilink"
title="location context">location context</a>.</p></td>
</tr>
<tr>
<td><p><samp>LOCATION_HAS_CUSTOM_FIELD &lt;location&gt; &lt;key&gt;
[value]</samp></p></td>
<td><p>Checks to see if the location has a given value in its
CustomFields. If the value is omitted, checks to see if the key exists
at all.</p></td>
</tr>
<tr>
<td><p><samp>LOCATION_IS_INDOORS &lt;location&gt;</samp><br />
<samp>LOCATION_IS_OUTDOORS &lt;location&gt;</samp><br />
<samp>LOCATION_IS_MINES &lt;location&gt;</samp><br />
<samp>LOCATION_IS_SKULL_CAVE &lt;location&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_location" class="wikilink"
title="given location">given location</a> is indoors, outdoors, in <a
href="The_Mines" class="wikilink" title="the mines">the mines</a>, or in
the <a href="Skull_Cavern" class="wikilink" title="Skull Cavern">Skull
Cavern</a>.</p></td>
</tr>
<tr>
<td><p><samp>LOCATION_NAME &lt;location&gt; &lt;name&gt;+</samp><br />
<samp>LOCATION_UNIQUE_NAME &lt;location&gt;
&lt;name&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_location" class="wikilink"
title="given location">given location</a> has one of the specified names
or unique instanced names (you can see both names in-game using the
mod).</p></td>
</tr>
<tr>
<td><p><samp>LOCATION_SEASON &lt;location&gt;
[&lt;season&gt;]+</samp></p></td>
<td><p>Whether the <a href="#Target_location" class="wikilink"
title="given location">given location</a> is in one of the given seasons
(which can be <samp>spring</samp>, <samp>summer</samp>,
<samp>fall</samp>, or <samp>winter</samp>). This accounts for the
<samp>SeasonOverride</samp> field in the <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_location_contexts"
class="wikilink" title="location&#39;s context data">location's context
data</a>.</p>
<p>For example, this is valid in spring <em>or</em> summer:
<code>LOCATION_SEASON Here spring summer</code>.</p></td>
</tr>
<tr>
<td><p><samp>MUSEUM_DONATIONS &lt;min count&gt; [max count] [object
type]+</samp></p></td>
<td><p>Whether all players have donated a total of &lt;min count&gt; to
[max count] (default unlimited) inclusively to the <a href="museum"
class="wikilink" title="museum">museum</a>. This can optionally be
filtered by the object type field, like <samp>MUSEUM_DONATIONS 40 Arch
Minerals</samp> to require at least 40 artifacts and minerals combined.
You can omit the max count and still specify a filter. Object type is
case-sensitive.</p></td>
</tr>
<tr>
<td><p><samp>WEATHER &lt;location&gt; &lt;weather&gt;+</samp></p></td>
<td><p>The weather ID in the <a href="#Target_location" class="wikilink"
title="given location">given location</a>. The &lt;weather&gt; can be
one of <samp>Festival</samp>, <samp>GreenRain</samp>, <samp>Rain</samp>,
<samp>Snow</samp>, <samp>Storm</samp>, <samp>Sun</samp>,
<samp>Wind</samp>, or a <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_weather"
class="wikilink" title="custom weather ID">custom weather
ID</a>.</p></td>
</tr>
<tr>
<td><p><samp>WORLD_STATE_FIELD &lt;name&gt;
&lt;value&gt;</samp></p></td>
<td><p>Whether a property on <samp>Game1.netWorldState</samp> has the
given value. If the property is numeric, this is the <em>minimum</em>
value. Some useful values not covered by their own query:</p>
<table>
<thead>
<tr>
<th><p>name</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>GoldenCoconutCracked</samp></p></td>
<td><p>Whether the player has cracked open any <a href="Golden_Coconut"
class="wikilink" title="Golden Coconut">Golden Coconuts</a>
(<samp>true</samp> or <samp>false</samp>).</p></td>
</tr>
<tr>
<td><p><samp>GoldenWalnutsFound</samp><br />
<samp>GoldenWalnuts</samp></p></td>
<td><p>The total number of <a href="Golden_Walnut" class="wikilink"
title="Golden Walnut">Golden Walnuts</a> found or held by any player. To
check how many one player currently holds, see the
<samp>PLAYER_HAS_ITEM</samp> query.</p></td>
</tr>
<tr>
<td><p><samp>IsGoblinRemoved</samp></p></td>
<td><p>Whether the <a href="Henchman" class="wikilink"
title="Henchman">Henchman</a> has been removed, so the player can access
<a href="Witch&#39;s_Hut" class="wikilink"
title="Witch&#39;s Hut">Witch's Hut</a> (<samp>true</samp> or
<samp>false</samp>).</p></td>
</tr>
<tr>
<td><p><samp>IsSubmarineLocked</samp></p></td>
<td><p>Whether the <a href="Night_Market" class="wikilink"
title="Night Market">Night Market</a> submarine is currently in use by a
player (<samp>true</samp> or <samp>false</samp>).</p></td>
</tr>
<tr>
<td><p><samp>LostBooksFound</samp></p></td>
<td><p>The total number of <a href="Lost_Book" class="wikilink"
title="Lost Book">Lost Books</a> found or held by any player.</p></td>
</tr>
<tr>
<td><p><samp>MinesDifficulty</samp><br />
<samp>SkullCavesDifficulty</samp></p></td>
<td><p>The current <a href="The_Mines#Shrine_of_Challenge"
class="wikilink" title="Shrine of Challenge">Shrine of Challenge</a>
difficulty level for the <a href="The_Mines" class="wikilink"
title="mine">mine</a> or <a href="Skull_Cavern" class="wikilink"
title="Skull Cavern">Skull Cavern</a> (a numeric value, where
<samp>0</samp> is the default level when the shrine is
deactivated).</p></td>
</tr>
<tr>
<td><p><samp>MiniShippingBinsObtained</samp></p></td>
<td><p>The number of times the player has obtained a <a
href="Mini-Shipping_Bin" class="wikilink"
title="Mini-Shipping Bin">Mini-Shipping Bin</a>.</p></td>
</tr>
<tr>
<td><p><samp>ParrotPlatformsUnlocked</samp></p></td>
<td><p>Whether the player has unlocked <a href="Ginger_Island"
class="wikilink" title="Ginger Island">Ginger Island</a> parrot
platforms, regardless of whether they've completed them
(<samp>true</samp> or <samp>false</samp>).</p></td>
</tr>
<tr>
<td><p><samp>ServerPrivacy</samp></p></td>
<td><p>The <a href="multiplayer" class="wikilink"
title="multiplayer">multiplayer</a> connection privacy mode
(<samp>InviteOnly</samp> or <samp>FriendsOnly</samp>).</p></td>
</tr>
<tr>
<td><p><samp>ShuffleMineChests</samp></p></td>
<td><p>The value of the 'mine rewards' <a href="Options"
class="wikilink" title="game option">game option</a>
(<samp>Default</samp> or <samp>Remixed</samp>).</p></td>
</tr>
<tr>
<td><p><samp>WeatherForTomorrow</samp></p></td>
<td><p>The weather ID for tomorrow in the main valley area.</p></td>
</tr>
<tr>
<td><p><samp>VisitsUntilY1Guarantee</samp></p></td>
<td><p>The number of times the <a href="Traveling_Cart" class="wikilink"
title="Traveling Cart">Traveling Cart</a> will visit before <a
href="Red_Cabbage" class="wikilink" title="Red Cabbage">Red Cabbage</a>
is guaranteed to drop.</p></td>
</tr>
</tbody>
</table>
<p>For example, the <a href="Traveling_Cart" class="wikilink"
title="Traveling Cart">Traveling Cart</a> shop uses a
<code>WORLD_STATE_FIELD VisitsUntilY1Guarantee 0</code> condition to
check if it should guarantee a <a href="Red_Cabbage" class="wikilink"
title="Red Cabbage">Red Cabbage</a> item.</p></td>
</tr>
<tr>
<td><p><samp>WORLD_STATE_FIELD &lt;name&gt; &lt;min&gt;
[max]</samp></p></td>
<td><p>For numeric properties only, whether a property on
<samp>Game1.netWorldState</samp> has a value between &lt;min&gt; and
[max] (default unlimited). If [max] is omitted or the properties isn't
numeric, the previous form is used. See the previous entry for a list of
useful properties.</p></td>
</tr>
<tr>
<td><p><samp>WORLD_STATE_ID &lt;id&gt;+</samp></p></td>
<td><p>Whether any world state flag matching the given &lt;id&gt; values
is set.</p></td>
</tr>
</tbody>
</table>

### Player info & progress

<table>
<thead>
<tr>
<th><p>Condition</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>MINE_LOWEST_LEVEL_REACHED &lt;min&gt; [max]</samp></p></td>
<td><p>Whether any player has reached a level between &lt;min&gt; and
[max] (default unlimited) inclusively in <a href="The_Mines"
class="wikilink" title="the mines">the mines</a>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_BASE_COMBAT_LEVEL</samp><br />
<samp>PLAYER_BASE_FARMING_LEVEL</samp><br />
<samp>PLAYER_BASE_FISHING_LEVEL</samp><br />
<samp>PLAYER_BASE_FORAGING_LEVEL</samp><br />
<samp>PLAYER_BASE_LUCK_LEVEL</samp><br />
<samp>PLAYER_BASE_MINING_LEVEL</samp></p></td>
<td><p>Same as the non-<samp>BASE</samp> queries, but ignores buffs
which change skill levels.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_COMBAT_LEVEL &lt;player&gt; &lt;min&gt;
[max]</samp><br />
<samp>PLAYER_FARMING_LEVEL &lt;player&gt; &lt;min&gt; [max]</samp><br />
<samp>PLAYER_FISHING_LEVEL &lt;player&gt; &lt;min&gt; [max]</samp><br />
<samp>PLAYER_FORAGING_LEVEL &lt;player&gt; &lt;min&gt;
[max]</samp><br />
<samp>PLAYER_LUCK_LEVEL &lt;player&gt; &lt;min&gt; [max]</samp><br />
<samp>PLAYER_MINING_LEVEL &lt;player&gt; &lt;min&gt;
[max]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have a <a
href="skills" class="wikilink" title="skill level">skill level</a>
between &lt;min&gt; and [max] (default unlimited) inclusively, including
the effects of buffs which raise them.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_CURRENT_MONEY &lt;player&gt; &lt;min&gt;
[max]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have between
&lt;min&gt; and [max] (default unlimited) gold inclusively.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_FARMHOUSE_UPGRADE &lt;player&gt; &lt;min&gt;
[max]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have upgraded their
<a href="farmhouse" class="wikilink" title="farmhouse">farmhouse</a> or
<a href="cabin" class="wikilink" title="cabin">cabin</a> to a level
between &lt;min&gt; and [max] (default unlimited) inclusively. See <a
href="https://github.com/Pathoschild/StardewMods/blob/develop/ContentPatcher/docs/author-guide/tokens.md#FarmhouseUpgrade">possible
levels</a>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_GENDER &lt;player&gt; &lt;gender&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> are
<samp>Male</samp> or <samp>Female</samp>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_ACHIEVEMENT &lt;player&gt; &lt;achievement
id&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have unlocked a
specific achievement ID. The valid IDs are listed in <a
href="Modding_Achievement_data" class="wikilink"
title="Data/Achievements"><samp>Data/Achievements</samp></a>, plus a few
Steam achievement IDs that aren't listed.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_ALL_ACHIEVEMENTS &lt;player&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have unlocked every
achievement listed in <a href="Modding_Achievement_data"
class="wikilink"
title="Data/Achievements"><samp>Data/Achievements</samp></a>. This
doesn't count the extra Steam achievement IDs that aren't listed in that
file.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_BUFF &lt;player&gt; &lt;id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have <em>any</em> of
the specified buff IDs currently applied.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_CAUGHT_FISH &lt;player&gt;
&lt;id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have caught
<em>any</em> of the specified fish qualified IDs.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_CONVERSATION_TOPIC &lt;player&gt;
&lt;id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have <em>any</em> of
the specified <a href="Modding_Dialogue#Conversation_topics"
class="wikilink" title="conversation topics">conversation topics</a>
active.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_COOKING_RECIPE &lt;player&gt; &lt;recipe
name&gt;</samp><br />
<samp>PLAYER_HAS_CRAFTING_RECIPE &lt;player&gt; &lt;recipe
name&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> know the
crafting/cooking recipe identified by its internal name (spaces
allowed). For example,
<code>PLAYER_HAS_CRAFTING_RECIPE Current Field Snack</code>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_DIALOGUE_ANSWER &lt;player&gt;
&lt;id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have chosen
<em>any</em> of the given dialogue answers in a previous
dialogue.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_HEARD_SONG &lt;player&gt;
&lt;id&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have heard
<em>any</em> of the song track's cue names (e.g. for the <a
href="jukebox" class="wikilink" title="jukebox">jukebox</a> track
selection).</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_ITEM &lt;player&gt; &lt;item&gt; [min]
[max]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have between [min]
and [max] (default unlimited) matching items in their inventory,
inclusively. The &lt;item&gt; can be <samp>858</samp> or
<samp>(O)858</samp> (Qi Gems), <samp>73</samp> or <samp>(O)73</samp>
(Walnuts), or the <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_MAIL &lt;player&gt; &lt;mail id&gt;
[type]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have the given <a
href="Modding_Mail_data" class="wikilink" title="mail flag">mail
flag</a> set.</p>
<p>The [type] (default <samp>Any</samp>) can be one of:</p>
<table>
<thead>
<tr>
<th><p>type</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Any</samp></p></td>
<td><p>Mail in <a href="The_Farm#Mailbox" class="wikilink"
title="the mailbox">the mailbox</a>, in the queue for tomorrow's
mailbox, or already received.</p></td>
</tr>
<tr>
<td><p><samp>Mailbox</samp></p></td>
<td><p>Mail in the mailbox.</p></td>
</tr>
<tr>
<td><p><samp>Tomorrow</samp></p></td>
<td><p>Mail in the queue for tomorrow's mailbox.</p></td>
</tr>
<tr>
<td><p><samp>Received</samp></p></td>
<td><p>Mail which either:</p>
<ul>
<li>was in the mailbox and read by the player;</li>
<li>or has no letter in <samp>Data/mail</samp>, so it was added to the
received list directly.</li>
</ul></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_PROFESSION &lt;player&gt; &lt;profession
id&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have the given <a
href="Skills" class="wikilink" title="profession">profession</a> ID. See
<a href="Modding_Console_commands#Skills_and_XP" class="wikilink"
title="Skills and XP debug commands">Skills and XP debug commands</a>
for a list.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_RUN_TRIGGER_ACTION &lt;player&gt;
&lt;id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have applied
<em>any</em> of the specified <a href="Modding_Trigger_actions"
class="wikilink" title="trigger actions">trigger actions</a>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_SECRET_NOTE &lt;player&gt;
&lt;id&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have read a secret
note, where &lt;id&gt; is the secret note's integer ID.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_SEEN_EVENT &lt;player&gt;
&lt;id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have seen the
<em>any</em> of the specified event.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_TOWN_KEY &lt;player&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have the <a
href="Key_To_The_Town" class="wikilink" title="town key">town
key</a>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_TRASH_CAN_LEVEL &lt;player&gt; &lt;min&gt;
[max]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have a <a
href="Trash_Cans" class="wikilink" title="trash can upgrade level">trash
can upgrade level</a> between &lt;min&gt; and [max] (default unlimited)
inclusively. The &lt;level&gt; can be <samp>0</samp> (base),
<samp>1</samp> (copper), <samp>2</samp> (steel), <samp>3</samp> (gold),
or <samp>4</samp> (iridium).</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_TRINKET &lt;player&gt; &lt;trinket
ID&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have one of the
listed <a href="trinkets" class="wikilink" title="trinkets">trinkets</a>
equipped. Each ID can be a qualified or unqualified item ID.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_LOCATION_CONTEXT &lt;player&gt; &lt;location context
ID&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> are in the given <a
href="Modding_Location_contexts" class="wikilink"
title="location context">location context</a>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_LOCATION_NAME &lt;player&gt; &lt;location
name&gt;+</samp><br />
<samp>PLAYER_LOCATION_UNIQUE_NAME &lt;player&gt; &lt;location
name&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> are in the given
location, using the name or unique instanced name (you can see both
names in-game using the mod). The &lt;location name&gt; value doesn't
recognize <a href="#Target_location" class="wikilink"
title="target location keywords">target location keywords</a> like
<samp>Here</samp>.</p>
<p><strong>Note:</strong> The player's current location is updated
slower than the game's current location. This mainly impacts usage in
LocationChanged as PLAYER_LOCATION_NAME will check the player's previous
(not yet updated) location. Instead, use LOCATION_NAME to check the
location they are entering. This GSQ works as expected in other cases
where the player isn't in the middle of changing locations, and it's
likely that this behavior will be fixed in future game updates.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_MOD_DATA &lt;player&gt; &lt;key&gt;
&lt;value&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have a
<samp>player.modData</samp> entry added by a mod with the given
&lt;key&gt; and &lt;value&gt;.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_MONEY_EARNED &lt;player&gt; &lt;min&gt;
[max]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have earned between
&lt;min&gt; and [max] (default unlimited) gold inclusively.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_KILLED_MONSTERS &lt;player&gt; &lt;monster name&gt;+
[min count] [max count]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have killed the
given monster(s) between [min count] (default 1) and [max count]
(default unlimited) times inclusively. If you list multiple monsters,
it'll check the combined count for all of them.</p>
<p>For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">// killed 50+ slimes, skeletons, and bugs combined</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>PLAYER_KILLED_MONSTERS Current <span class="st">&quot;Green Slime&quot;</span> Skeleton Bug <span class="dv">50</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>PLAYER_SHIPPED_BASIC_ITEM &lt;player&gt; &lt;item ID&gt;
[min count] [max count]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have shipped the
given item between [min count] (default 1) and [max count] (default
unlimited) times inclusively. This only works for the items tracked by
the game for shipping stats (shown in the <a href="Shipping#Collection"
class="wikilink" title="shipping collections menu">shipping collections
menu</a>).</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_SPECIAL_ORDER_ACTIVE &lt;player&gt; &lt;order
id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have <em>any</em> of
the given <a href="Special_Orders" class="wikilink"
title="special orders">special orders</a> active.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_SPECIAL_ORDER_COMPLETE &lt;player&gt; &lt;order
id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have completed
<em>any</em> of the given <a href="Special_Orders" class="wikilink"
title="special orders">special orders</a>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_SPECIAL_ORDER_RULE_ACTIVE &lt;player&gt; &lt;rule
id&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have <em>any</em> of
the <a href="Modding_Special_orders#Special_rules" class="wikilink"
title="special rules">special rules</a> active.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_STAT &lt;player&gt; &lt;stat key&gt; &lt;min
value&gt; [max value]</samp></p></td>
<td><p>Whether a <a href="Modding_Stats" class="wikilink"
title="stat counter">stat counter</a> for the <a href="#Target_player"
class="wikilink" title="specified player(s)">specified player(s)</a> has
a value between &lt;min value&gt; and [max value] (default unlimited)
inclusively.</p>
<p><strong>⚠ Careful:</strong> stats are not synced in multiplayer, so
farmhands can't access stats on the host or other farmhands.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_VISITED_LOCATION &lt;player&gt; &lt;location
name&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have visited one of
the given location names. For example,
<code>PLAYER_VISITED_LOCATION Current IslandWest</code> checks whether
the current player has ever visited <a href="Ginger_Island#Island_West"
class="wikilink" title="Ginger Island West">Ginger Island West</a>.</p>
<p>Notes:</p>
<ul>
<li>Some locations have both a common name (like <samp>Barn</samp>) and
unique name (like <samp>Barn{unique ID}</samp>). This tracks the common
name.</li>
<li>Generated mine and volcano dungeon levels aren't tracked.</li>
</ul></td>
</tr>
</tbody>
</table>

### Player relationships

<table>
<thead>
<tr>
<th><p>Condition</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>PLAYER_FRIENDSHIP_POINTS &lt;player&gt; &lt;npc&gt; &lt;min
points&gt; [max points]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have a friend with
<a href="friendship" class="wikilink"
title="friendship points">friendship points</a> between &lt;min
points&gt; and [max points] (default unlimited) inclusively. The
&lt;npc&gt; can be an NPC's internal name, <samp>Any</samp> (check every
NPC), or <samp>AnyDateable</samp> (check every romanceable NPC).</p>
<p>For example, this checks if the current player has 750 or more points
(i.e. 3+ hearts) with Abigail:</p>
<pre><code>PLAYER_FRIENDSHIP_POINTS Current Abigail 750</code></pre></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_CHILDREN &lt;player&gt; [min]
[max]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have a number of
children between [min] (default 1) and [max] (default unlimited)
inclusively.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_PET &lt;player&gt;</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have a <a
href="Animals#Cat_or_Dog" class="wikilink" title="pet">pet</a>.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_HEARTS &lt;player&gt; &lt;npc&gt; &lt;min hearts&gt;
[max hearts]</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have a friend with a
<a href="friendship" class="wikilink" title="heart level">heart
level</a> between &lt;min hearts&gt; and [max hearts] (default
unlimited) inclusively. The &lt;npc&gt; can be an NPC's internal name,
<samp>Any</samp> (check every NPC), or <samp>AnyDateable</samp> (check
every romanceable NPC).</p>
<p>For example, this checks if the current player has 3 or more hearts
with Abigail:</p>
<pre><code>PLAYER_HEARTS Current Abigail 3</code></pre></td>
</tr>
<tr>
<td><p><samp>PLAYER_HAS_MET &lt;player&gt; &lt;npc&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have talked to one
of the given NPCs at least once. The &lt;npc&gt; is an NPC's internal
name.</p></td>
</tr>
<tr>
<td><p><samp>PLAYER_NPC_RELATIONSHIP &lt;player&gt; &lt;npc&gt;
&lt;type&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have one of the
relationship statuses with an NPC. The &lt;npc&gt; can be an NPC's
internal name or <samp>Any</samp> (match any NPC).</p>
<p>&lt;type&gt; can be any combination of these values:</p>
<table>
<thead>
<tr>
<th><p>type</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Friendly</samp></p></td>
<td><p>Met the NPC, but no other status applies.</p></td>
</tr>
<tr>
<td><p><samp>Roommate</samp></p></td>
<td><p>The NPC has moved in with the player as a roommate.</p></td>
</tr>
<tr>
<td><p><samp>Dating</samp></p></td>
<td><p>The player has given a <a href="bouquet" class="wikilink"
title="bouquet">bouquet</a> to the NPC, but haven't yet given them a <a
href="Mermaid&#39;s_Pendant" class="wikilink"
title="mermaid&#39;s pendant">mermaid's pendant</a>.</p></td>
</tr>
<tr>
<td><p><samp>Engaged</samp></p></td>
<td><p>The player has given a <a href="Mermaid&#39;s_Pendant"
class="wikilink" title="mermaid&#39;s pendant">mermaid's pendant</a> to
the NPC, but the marriage hasn't happened yet.</p></td>
</tr>
<tr>
<td><p><samp>Married</samp></p></td>
<td><p>The NPC has moved in with the player as a spouse.</p></td>
</tr>
<tr>
<td><p><samp>Divorced</samp></p></td>
<td><p>The player has dissolved their marriage with the NPC.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>PLAYER_PLAYER_RELATIONSHIP &lt;player&gt; &lt;other
player&gt; &lt;type&gt;+</samp></p></td>
<td><p>Whether the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> have one of the
relationship types with the other specified player(s). The &lt;other
player&gt; can be a <a href="#Target_player" class="wikilink"
title="target player">target player</a> or <samp>Any</samp> (match any
player).</p>
<p>&lt;type&gt; can be any combination of these values:</p>
<table>
<thead>
<tr>
<th><p>type</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Friendly</samp></p></td>
<td><p>No other status applies.</p></td>
</tr>
<tr>
<td><p><samp>Engaged</samp></p></td>
<td><p>One of the players has given a <a href="Wedding_Ring"
class="wikilink" title="wedding ring">wedding ring</a> to the other, but
the marriage hasn't happened yet.</p></td>
</tr>
<tr>
<td><p><samp>Married</samp></p></td>
<td><p>The players are married.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>PLAYER_PREFERRED_PET &lt;player&gt; &lt;pet
type&gt;+</samp></p></td>
<td><p>Whether the preferred pet for the <a href="#Target_player"
class="wikilink" title="specified player(s)">specified player(s)</a> is
one of the given types. The vanilla pet types are <samp>Cat</samp> and
<samp>Dog</samp>.</p></td>
</tr>
</tbody>
</table>

### Randomization

<table>
<thead>
<tr>
<th><p>Condition</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>RANDOM &lt;chance&gt; [@addDailyLuck]</samp></p></td>
<td><p>A random probability check which is re-rolled each time it's
called. For example, <code>RANDOM 0.4</code> is true 40% of the
time.</p>
<p>If the exact text <samp>@addDailyLuck</samp> is specified, the
current player's daily <a href="luck" class="wikilink"
title="luck">luck</a> is added to the probability.</p></td>
</tr>
<tr>
<td><p><samp>SYNCED_CHOICE &lt;interval&gt; &lt;key&gt; &lt;min&gt;
&lt;max&gt; &lt;choices&gt;+</samp></p></td>
<td><p>Choose a random integer between &lt;min&gt; and &lt;max&gt;
inclusively, and check whether it matches one of the &lt;choices&gt;.
The result will be identical for all queries with the same &lt;key&gt;
value during the given &lt;interval&gt; (one of <samp>tick</samp>,
<samp>day</samp>, <samp>season</samp>, or <samp>year</samp>), including
between players in multiplayer mode.</p>
<p>For example, <samp>SYNCED_CHOICE day example_key 1 5 1 2</samp>
chooses a random value between 1 and 5, and checks if it's either 1 or
2.</p>
<p>This is mainly useful in cases where you need to pick between a
number of discrete cases. For regular probability checks, see
<samp>SYNCED_RANDOM</samp> instead.</p></td>
</tr>
<tr>
<td><p><samp>SYNCED_RANDOM &lt;interval&gt; &lt;key&gt; &lt;chance&gt;
[@addDailyLuck]</samp></p></td>
<td><p>A random probability check. The result will be identical for all
queries with the same &lt;key&gt; value during the given
&lt;interval&gt; (one of <samp>tick</samp>, <samp>day</samp>,
<samp>season</samp>, or <samp>year</samp>), including between players in
multiplayer mode.</p>
<p>For example, <samp>SYNCED_RANDOM day cart_rare_seed 0.4</samp> has a
40% chance to be true the first time it's called that day, and will
always be the same value if called again with the same key on the same
day.</p>
<p>If the exact text <samp>@addDailyLuck</samp> is specified, the
current player's daily <a href="luck" class="wikilink"
title="luck">luck</a> is added to the probability.</p></td>
</tr>
<tr>
<td><p><samp>SYNCED_SUMMER_RAIN_RANDOM</samp></p></td>
<td><p>A random probability check used to calculate the chance of rain
in summer, which increases with the day number.</p></td>
</tr>
</tbody>
</table>

### For items only

These queries apply in cases where there's an item (e.g. machine
recipes, shops, etc); they'll return false if not applicable. They take
a \<target\> argument which can be `Input` (the machine input item) or
`Target` (the machine output, tree fruit, shop item, etc). These applies
only to vanilla contexts, modded ones can pick what items they want to
pass to `Input` or `Target`.

| Condition | effect |
|----|----|
| `ITEM_CATEGORY <target>` | Whether the item has a non-zero <a href="Modding_Items#Category" class="wikilink"
title="category">category</a>. |
| `ITEM_CATEGORY <target> [category]+` | Whether the item's <a href="Modding_Items#Category" class="wikilink"
title="category">category</a> number matches one of the given values. |
| `ITEM_CONTEXT_TAG <target> <tags>` | Whether the item has all of the given space-delimited tags. For example, `ITEM_CONTEXT_TAG Target bone_item marine_item` will only match items with both tags. |
| `ITEM_EDIBILITY <target> [min] [max]` | Whether the item's edibility is between \[min\] (default -299) and \[max\] (default unlimited) inclusively. A value of -300 is inedible, so `ITEM_EDIBILITY <target>` without min/max values checks if the item is edible. |
| `ITEM_ID <target> <item ID>+` | Whether the item has one of the given <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item IDs">qualified or unqualified item
IDs</a>. |
| `ITEM_ID_PREFIX <target> <prefix>` | Whether the item's <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a> starts with the given prefix. |
| `ITEM_NUMERIC_ID <target> [min] [max]` | Whether the item has a numeric <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="unqualified item ID">unqualified item ID</a> which is between \[min\] and \[max\] (both defaulting to the lowest and highest possible value). |
| `ITEM_OBJECT_TYPE <target> <type>+` | Whether the item has one of the given <a href="Modding_Objects" class="wikilink" title="object types">object
types</a>. |
| `ITEM_PRICE <target> <min> [max]` | Whether the item has a default purchase-from-shop price between \<min\> and \[max\] (default highest possible value). This checks the base sell price (including <a href="Multiplayer#Profit_margins" class="wikilink"
title="profit margins">profit margins</a>, but excluding custom shop data like custom prices, price modifiers, out-of-season pricing, etc). |
| `ITEM_QUALITY <target> <min> [max]` | Whether the item's quality is between \<min\> and \[max\] (default unlimited) inclusively. The possible values are `0` (normal), `1` (silver), `2` (gold), or `4` (iridium). |
| `ITEM_STACK <target> <min> [max]` | Whether the item stack size is between \<min\> and \[max\] (default unlimited) inclusively. Note that this only applies to the target item, it doesn't include other stacks in the inventory. |
| `ITEM_TYPE <target> <type>+` | Whether the <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="item&#39;s type definition ID">item's type definition ID</a> matches one of the given values. For example, `ITEM_TYPE Target (BC)` matches bigcraftables. |
| `ITEM_HAS_EXPLICIT_OBJECT_CATEGORY <target>` | *(Specialized)* Whether the item has an explicit category set in `Data/Objects`, ignoring categories assigned dynamically in code (e.g. for rings). Items without an explicit category are often (but not always) special items like <a href="Secret_Notes" class="wikilink" title="secret notes">secret
notes</a> or unimplemented items. |

### Immutable

| Condition | effect                            |
|-----------|-----------------------------------|
| `TRUE`    | A condition which always matches. |
| `FALSE`   | A condition which never matches.  |

### Content Patcher tokens

Since `TRUE` and `FALSE` are valid game state queries,
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> tokens which return a
true/false value can be used directly as a game state query too.

For example, you can check if a mod is installed:

``` js
// Automate is installed
"Condition": ""
```

``` js
// Automate is not installed
"Condition": "!"
```

## Common values

### Target location

Some conditions have a \<location\> argument. This can be one of...

<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>result</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Here</samp></p></td>
<td><p>The location containing the current player (regardless of the <a
href="#Target_player" class="wikilink" title="target player">target
player</a>).</p></td>
</tr>
<tr>
<td><p><samp>Target</samp></p></td>
<td><p>The location containing the in-game entity being edited (e.g. the
machine for <samp>Data/Machines</samp> or fruit tree for
<samp>Data/FruitTrees</samp>).</p>
<p>If the asset being edited isn't tied to a location, this is the
location of the <a href="#Target_player" class="wikilink"
title="target player">target player</a> (if set), else equivalent to
<samp>Here</samp>.</p></td>
</tr>
<tr>
<td><p><em>any other</em></p></td>
<td><p>The <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_locations"
class="wikilink" title="location ID">location ID</a> (i.e. internal
name) for the location to check.</p></td>
</tr>
</tbody>
</table>

### Target player

Some conditions have a \<player\> argument. This can be one of...

<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>result</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Any</samp></p></td>
<td><p>At least one player must match the condition, regardless of
whether they're online.</p></td>
</tr>
<tr>
<td><p><samp>All</samp></p></td>
<td><p>Every player must match the condition, regardless of whether
they're online.</p></td>
</tr>
<tr>
<td><p><samp>Current</samp></p></td>
<td><p>The local player.</p></td>
</tr>
<tr>
<td><p><samp>Host</samp></p></td>
<td><p>The main player.</p></td>
</tr>
<tr>
<td><p><samp>Target</samp></p></td>
<td><p>This value depends on the context:</p>
<table>
<thead>
<tr>
<th><p>context</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Data/LocationContexts</samp></p></td>
<td><p>For the <samp>PassOutLocations</samp> field only, the player
whose pass-out location to get.</p></td>
</tr>
<tr>
<td><p><samp>Data/Weddings</samp></p></td>
<td><p>For the <samp>Attendees</samp> field only, the attendee player
(if the attendee is a player).</p></td>
</tr>
<tr>
<td><p><samp>Data/WildTrees</samp></p></td>
<td><p>For the <samp>AdditionalChopDrops</samp> field only, the last
player who chopped the tree.</p></td>
</tr>
<tr>
<td><p><em>custom queries</em></p></td>
<td><p>C# mods may specify a <samp>target_farmer</samp> parameter when
calling <samp>GameStateQuery.CheckConditions</samp>.</p></td>
</tr>
<tr>
<td><p><em>any other</em></p></td>
<td><p>Equivalent to <samp>Current</samp>.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><em>any other</em></p></td>
<td><p>The unique multiplayer ID for the player to check.</p></td>
</tr>
</tbody>
</table>

## For C# mod authors

### Using queries elsewhere

C# code can work with queries using the `GameStateQuery` class, which
provides utility methods like `GameStateQuery.CheckConditions(query)` or
`GameStateQuery.IsImmutablyTrue(query)`.

You can also use game state queries in
<a href="Modding_Event_data" class="wikilink"
title="event preconditions">event preconditions</a> using the new
precondition flag, like
`some_event_id/gameStateQuery !SEASON Spring, WEATHER Here Sun`.

### Extensibility

C# mods can...

- check if a query exists using
  `GameStateQuery.Exists("Example.ModId_ConditionName")`;
- define custom queries using
  `GameStateQuery.Register("Example.ModId_ConditionName", handleQueryMethod)`
  (using a <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  query name);
- and add query aliases using
  `GameStateQuery.RegisterAlias("Example.ModId_AliasName", "Example.ModId_ConditionName")`
  (ideally using a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  alias).

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Запросы_состояния_игры" class="wikilink"
title="ru:Модификации:Запросы состояния игры">ru:Модификации:Запросы
состояния игры</a> <a href="zh_模组_游戏状态查询" class="wikilink"
title="zh:模组:游戏状态查询">zh:模组:游戏状态查询</a>
