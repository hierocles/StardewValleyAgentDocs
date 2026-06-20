---
title: "Locations"
wiki_source: "Modding:Location data"
permalink: /Modding:Location_data/
category: locations
tags: [location-data, terminology, data-format, basic-info, contents, music, advanced, default-entry]
---
← <a href="Modding_Index" class="wikilink"
title="Modding:Index">Modding:Index</a>

This page explains how to create and edit in-game locations.

## Terminology

A few terms may be used interchangeably or have different meanings
depending on the context. In the context of Stardew Valley:

- A **location** is part of the game code and save data. It manages the
  in-game area and everything inside it (including non-map entities like
  players). The location is read/written to the save file, and is only
  loaded when loading the save file.
- A **<a href="Modding_Maps" class="wikilink" title="map">map</a>** is
  an asset which describes the tile layout, tilesheets, and map/tile
  properties for the in-game area. The map is reloaded each time you
  load a save, and each time a mod changes the map.
- A
  **<a href="Modding_World_map" class="wikilink" title="world map">world
  map</a>** is the image shown for a world region in the in-game menu.

In other words, a *location* (part of the game code) references the
*map* (loaded from the `Content` folder):

    ┌─────────────────────────────────┐
    │ Location                        │
    │   - objects                     │
    │   - furniture                   │
    │   - crops                       │
    │   - bushes and trees            │
    │   - NPCs and players            │
    │   - etc                         │
    │                                 │
    │   ┌─────────────────────────┐   │
    │   │ Map asset               │   │
    │   │   - tile layout         │   │
    │   │   - map/tile properties │   │
    │   │   - tilesheets          │   │
    │   └─────────────────────────┘   │
    └─────────────────────────────────┘

## Data format

You can add or edit locations by editing the `Data/Locations` asset.

This consists of a string → model lookup, where...

- The key is the
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> of the
  location (i.e. "internal name"), which will also be used as the
  location's `Name` (not `DisplayName`) field. (The farm will use
  `Farm_<type key>` for a vanilla farm type, or `Farm_<type ID>` for a
  custom farm type, or `Farm_Standard` if no type-specific entry was
  found.)
- The value is a model with the fields listed below.

### Basic info

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
<td><p><em>(Optional but strongly recommended)</em> A <a
href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the translated
location name. This is used anytime the location name is shown in-game
for base game logic or mods.</p></td>
</tr>
<tr>
<td><p><samp>DefaultArrivalTile</samp></p></td>
<td><p><em>(Optional but strongly recommended)</em> The default tile
position where the player should be placed when they arrive in the
location, if arriving from a warp that didn't specify a tile position.
Default none, which usually places the player at (0, 0).</p></td>
</tr>
<tr>
<td><p><samp>CreateOnLoad</samp></p></td>
<td><p><em>(Optional)</em> If set, the location will be created
automatically when the save is loaded using this data.</p>
<p>This consists of a model with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>MapPath</samp></p></td>
<td><p>The asset name for the map to use for this location.</p></td>
</tr>
<tr>
<td><p><samp>AlwaysActive</samp></p></td>
<td><p><em>(Optional)</em> Whether this location is always synchronized
to farmhands in multiplayer, even if they're not in the location. Any
location which allows building cabins <strong>must</strong> have this
enabled to avoid breaking game logic.</p></td>
</tr>
<tr>
<td><p><samp>Type</samp></p></td>
<td><p><em>(Optional)</em> The full name of the C# location class to
create. This must be one of the vanilla types to avoid a crash when
saving. There are too many to list here, but the most useful types are
likely <samp>StardewValley.GameLocation</samp> (default value) and
<samp>StardewValley.Locations.DecoratableLocation</samp>.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>CanPlantHere</samp></p></td>
<td><p><em>(Optional)</em> Whether crops and trees can be planted and
grown here by default, unless overridden by their plantable rules.
Defaults to true for farms and false for other locations.</p></td>
</tr>
<tr>
<td><p><samp>CanHaveGreenRainSpawns</samp></p></td>
<td><p><em>(Optional)</em> Whether green rain trees and debris can spawn
here by default. Default true.</p></td>
</tr>
<tr>
<td><p><samp>ExcludeFromNpcPathfinding</samp></p></td>
<td><p><em>(Optional)</em> Whether NPCs should ignore this location when
pathfinding between locations. Default false.</p></td>
</tr>
</tbody>
</table>

### Contents

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ArtifactSpots</samp></p></td>
<td><p><em>(Optional)</em> The items that can be found when digging <a
href="Artifact_Spot" class="wikilink" title="artifact spots">artifact
spots</a> in this location.</p>
<p>An artifact spot is selected by combining this field with the
equivalent field on the <samp>Default</samp> entry, sorting by
<samp>Precedence</samp> value, and then choosing the first entry whose
fields match. (Artifact spot drops can also be listed in <a
href="Modding_Objects" class="wikilink"
title="Data/Objects"><samp>Data/Objects</samp></a>'s
<samp>ArtifactSpotChances</samp> field; those are applied by the
<samp>RANDOM_ARTIFACT_FOR_DIG_SPOT</samp> entry in
<samp>DefaultArtifactSpots</samp>.)</p>
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
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported by artifact spot drops.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that the item will be dropped
if the other fields match, as a decimal value between 0 (never) and 1
(always). Default 1.</p></td>
</tr>
<tr>
<td><p><samp>ApplyGenerousEnchantment</samp></p></td>
<td><p><em>(Optional)</em> Whether to apply the 'Generous' <a
href="Forge#Enchantments" class="wikilink"
title="enchantment">enchantment</a>, which adds a 50% chance of the item
dropping twice. If the enchantment is applied, the item's fields are
rerolled for the second drop (e.g. a new random value between
<samp>MinStack</samp> and <samp>MaxStack</samp> is selected). Default
true.</p></td>
</tr>
<tr>
<td><p><samp>OneDebrisPerDrop</samp></p></td>
<td><p><em>(Optional)</em> Whether to split the dropped item stack into
multiple floating debris that each have a stack size of one. For
example, if the dropped item has a stack size of 3, this will spawn
three separate item stacks. Default true.</p></td>
</tr>
<tr>
<td><p><samp>ContinueOnDrop</samp></p></td>
<td><p><em>(Optional)</em> Whether to continue checking for more items
to drop when this item is dropped. Default false.</p></td>
</tr>
<tr>
<td><p><samp>Precedence</samp></p></td>
<td><p><em>(Optional)</em> The order in which this entry should be
checked, where lower values are checked first. This can be a negative
value. Artifact spots with the same precedence are checked in the order
listed. Default 0.</p>
<p>For consistency, vanilla artifact drops mostly use these values:</p>
<ul>
<li><samp>-1000</samp>: location items which should override the global
priority items (e.g. fossils on Ginger Island);</li>
<li><samp>-100</samp>: global priority items (e.g. Qi Beans);</li>
<li><samp>0</samp>: normal items;</li>
<li><samp>100</samp>: global fallback items (e.g. clay).</li>
</ul></td>
</tr>
</tbody>
</table>
<p>For example, a location with this field will drop 2-4 pufferfish with
a 50% chance on summer days:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ArtifactSpots&quot;</span><span class="op">:</span> [</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    {</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Condition&quot;</span><span class="op">:</span> <span class="st">&quot;LOCATION_SEASON Here summer&quot;</span><span class="op">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;ItemId&quot;</span><span class="op">:</span> <span class="st">&quot;(O)128&quot;</span><span class="op">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;MinStack&quot;</span><span class="op">:</span> <span class="dv">2</span><span class="op">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;MaxStack&quot;</span><span class="op">:</span> <span class="dv">4</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>]</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>FishAreas</samp></p></td>
<td><p><em>(Optional)</em> The distinct <a href="fishing"
class="wikilink" title="fishing">fishing</a> areas within the location.
These can be referenced by fish via <samp>FishAreaId</samp>, and
determine which fish are collected by <a href="Crab_Pot"
class="wikilink" title="crab pots">crab pots</a>.</p>
<p>This consists of a string → model lookup, where the key is the fish
area ID and the value consists of a list of models with these
fields:</p>
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
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the translated area name, if any.</p></td>
</tr>
<tr>
<td><p><samp>Position</samp></p></td>
<td><p><em>(Optional)</em> The tile position and size covered by this
fishing area, specified as an object with <samp>X</samp>,
<samp>Y</samp>, <samp>Width</samp>, and <samp>Height</samp> fields. This
area will apply for crab pots placed within it, or when the fishing rod
bobber lands within it. Default null (anywhere).</p>
<p>Areas with a <samp>Position</samp> value have priority over those
without. If two areas with a <samp>Position</samp> overlap, the tiles
that are overlapping will be treated as part of the first FishArea
listed, effectively making the other area smaller than its
<samp>Position</samp> values indicate.</p></td>
</tr>
<tr>
<td><p><samp>CrabPotFishTypes</samp></p></td>
<td><p><em>(Optional)</em> A list of fish types that can be caught by
crab pots within the area. This is matched against field index 4 in <a
href="Modding_Fish_data" class="wikilink"
title="Data/Fish"><samp>Data/Fish</samp></a> for 'trap' (i.e. crab pot)
fish. The vanilla types are <samp>freshwater</samp> and
<samp>ocean</samp>. If omitted, defaults to
<samp>freshwater</samp>.</p></td>
</tr>
<tr>
<td><p><samp>CrabPotJunkChance</samp></p></td>
<td><p><em>(Optional)</em> The chance that crab pots within the area
will find junk instead of a fish each time they produce a harvest. This
is ignored if the player has the <a href="Fishing#Fishing_Skill"
class="wikilink" title="Mariner">Mariner</a> profession. Default
<samp>0.2</samp> (20%).</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Fish</samp></p></td>
<td><p><em>(Optional)</em> The fish that can be caught in the
location.</p>
<p>A fish is selected by combining this field with the equivalent field
on the <samp>Default</samp> entry, sorting by <samp>Precedence</samp>
value (and randomly shuffling entries with the same precedence), and
then choosing the first entry whose fields match.</p>
<p>Note: the produced item ID is saved to recreate the fish later. Any
item info that's not based on the item ID is ignored (like stack size,
quality, flavored variants like Blueberry Wine vs Wine, and the
is-recipe flag).</p>
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
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported by forage items.</p>
<p>This must return an <samp>Object</samp> item (or subclass of
<samp>Object</samp>). If set to an <a href="Modding_Item_queries"
class="wikilink" title="item query">item query</a> which returns
multiple items, one of them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that the fish will spawn if
selected, as a decimal value between 0 (never) and 1 (always). Default
1.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> If set, the specific season when the fish can
be caught. This is much more efficient than using
<samp>Condition</samp>, but only supports a single season. Defaults to
<samp>null</samp> (all seasons).</p></td>
</tr>
<tr>
<td><p><samp>FishAreaId</samp></p></td>
<td><p><em>(Optional)</em> If set, the fish area in which the fish can
be caught (as an area ID defined under <samp>FishAreas</samp>). Defaults
to <samp>null</samp> (all zones).</p></td>
</tr>
<tr>
<td><p><samp>BobberPosition</samp></p></td>
<td><p><em>(Optional)</em> If set, the tile area within the location
where the fishing rod's bobber must land to catch the fish. Default
<samp>null</samp> (anywhere).</p></td>
</tr>
<tr>
<td><p><samp>PlayerPosition</samp></p></td>
<td><p><em>(Optional)</em> If set, the tile area within the location
where the player must be standing to catch the fish. Default
<samp>null</samp> (anywhere).</p></td>
</tr>
<tr>
<td><p><samp>MinFishingLevel</samp></p></td>
<td><p><em>(Optional)</em> The minimum fishing level needed for the fish
to appear. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>ApplyDailyLuck</samp></p></td>
<td><p><em>(Optional)</em> Whether to add the player's <a href="Luck"
class="wikilink" title="daily luck">daily luck</a> to the spawn chance.
This affects both the <samp>Chance</samp> field and the
<samp>Data\Fish</samp> chance, if applicable. Default false.</p></td>
</tr>
<tr>
<td><p><samp>CuriosityLureBuff</samp></p></td>
<td><p><em>(Optional)</em> The value to add to the spawn chance when the
player has the <a href="Curiosity_Lure" class="wikilink"
title="Curiosity Lure">Curiosity Lure</a> equipped, if set to 0 or
higher. This affects both the <samp>Chance</samp> field and the
<samp>Data\Fish</samp> chance, if applicable. Default -1, which keeps
the default behavior (i.e. no effect on the <samp>Chance</samp> field
and a scaled boost to the <samp>Data\Fish</samp> chance).</p></td>
</tr>
<tr>
<td><p><samp>SpecificBaitBuff</samp></p></td>
<td><p><em>(Optional)</em> A flat increase to the spawn chance when the
player has a specific bait equipped which targets this fish. Default
0.</p></td>
</tr>
<tr>
<td><p><samp>SpecificBaitMultiplier</samp></p></td>
<td><p><em>(Optional)</em> A multiplier applied to the spawn chance when
the player has a specific bait equipped which targets this fish. Default
1.66.</p></td>
</tr>
<tr>
<td><p><samp>CatchLimit</samp></p></td>
<td><p><em>(Optional)</em> The maximum number of this fish which can be
caught by each player. This limit is permanent (i.e. once it's reached,
that fish will never appear again). For example, legendary fish set this
to one. Default -1 (no limit).</p></td>
</tr>
<tr>
<td><p><samp>CanUseTrainingRod</samp></p></td>
<td><p><em>(Optional)</em> Whether the player can catch this fish using
a training rod. This can be <samp>true</samp> (always allowed),
<samp>false</samp> (never allowed), or <samp>null</samp> (apply default
logic, i.e. allowed for difficulty ratings under 50). Default
null.</p></td>
</tr>
<tr>
<td><p><samp>IsBossFish</samp></p></td>
<td><p><em>(Optional)</em> Whether this is a 'boss fish' catch. This
shows a crowned fish sprite in the fishing minigame and gives five times
normal XP, like <a href="Legendary_Fish" class="wikilink"
title="legendary fish">legendary fish</a>.</p></td>
</tr>
<tr>
<td><p><samp>RequireMagicBait</samp></p></td>
<td><p><em>(Optional)</em> Whether the player must fish with Magic Bait
for this fish to spawn. Default false.</p></td>
</tr>
<tr>
<td><p><samp>MinDistanceFromShore</samp></p></td>
<td><p><em>(Optional)</em> The minimum distance from the nearest shore
(measured in tiles) at which the fish can be caught, where zero is water
directly adjacent to shore.</p></td>
</tr>
<tr>
<td><p><samp>MaxDistanceFromShore</samp></p></td>
<td><p><em>(Optional)</em> The maximum distance from the nearest shore
(measured in tiles) at which the fish can be caught, where zero is water
directly adjacent to shore. Default -1 (no limit).</p></td>
</tr>
<tr>
<td><p><samp>Precedence</samp></p></td>
<td><p><em>(Optional)</em> The order in which this entry should be
checked, where lower values are checked first. This can be a negative
value. Fish with the same precedence are shuffled randomly. Default
0.</p>
<p>For consistency, vanilla fish mostly use values in these ranges:</p>
<ul>
<li><samp>-1100</samp> to <samp>-1000</samp>: global priority items
(e.g. Qi Beans);</li>
<li><samp>-200</samp> to <samp>-100</samp>: unique location items (e.g.
legendary fish or secret items);</li>
<li><samp>-50</samp> to <samp>-1</samp>: normal high-priority
items;</li>
<li><samp>0</samp>: normal items;</li>
<li><samp>1</samp> to <samp>100</samp>: normal low-priority items;</li>
<li><samp>1000+</samp>: global fallback items (e.g. trash).</li>
</ul></td>
</tr>
<tr>
<td><p><samp>IgnoreFishDataRequirements</samp></p></td>
<td><p><em>(Optional)</em> Whether to ignore spawn requirements listed
in <a href="Modding_Fish_data" class="wikilink"
title="Data/Fish"><samp>Data/Fish</samp></a>, if applicable.</p>
<p>The <samp>Data/Fish</samp> requirements are ignored regardless of
this field for non-object (<samp>(O)</samp>)-type items, or objects
whose ID isn't listed in <samp>Data/Fish</samp>.</p></td>
</tr>
<tr>
<td><p><samp>CanBeInherited</samp></p></td>
<td><p><em>(Optional)</em> Whether this fish can be spawned in another
location via the <samp>LOCATION_FISH</samp> <a
href="Modding_Item_queries" class="wikilink" title="item query">item
query</a>. Default true.</p></td>
</tr>
<tr>
<td><p><samp>SetFlagOnCatch</samp></p></td>
<td><p><em>(Optional)</em> The mail flag to set for the current player
when this fish is successfully caught. Default none.</p></td>
</tr>
<tr>
<td><p><samp>ChanceModifiers</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="Quantity modifiers">Quantity modifiers</a>
applied to the <samp>Chance</samp> value. Default none.</p></td>
</tr>
<tr>
<td><p><samp>ChanceModifierMode</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="quantity modifier modes">quantity modifier
modes</a> which indicate what to do if multiple modifiers in the
<samp>ChanceModifiers</samp> field apply at the same time. Default
<samp>Stack</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ChanceBoostPerLuckLevel</samp></p></td>
<td><p><em>(Optional)</em> How much to increase the <samp>Chance</samp>
per player's Luck level.</p></td>
</tr>
<tr>
<td><p><samp>UseFishCaughtSeededRandom</samp></p></td>
<td><p><em>(Optional)</em> Whether the chance roll will use a seed value
based on the number of fish caught.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Forage</samp></p></td>
<td><p><em>(Optional)</em> The <a href="forage" class="wikilink"
title="forage">forage</a> that can spawn in the location.</p>
<p>Notes:</p>
<ul>
<li>Unlike other item spawn lists, these entries aren't checked
sequentially. Instead, the game...
<ol>
<li>combines this list with any forage in the <samp>Default</samp>
location entry;</li>
<li>adds every forage entry whose <samp>Condition</samp> and
<samp>Season</samp> match to a spawn pool;</li>
<li>chooses a random number of spawn <em>opportunities</em> (between 1
and 4);</li>
<li>for each spawn opportunity, chooses a random tile position and
forage to spawn. If the spawn fails (e.g. the tile is water/occupied or
the forage's <samp>Chance</samp> doesn't pass), the game will make nine
other attempts with a re-randomized tile &amp; forage before skipping
this spawn opportunity.</li>
</ol></li>
<li>The stack size is ignored.</li>
</ul>
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
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported by forage items.</p>
<p>This must return an <samp>Object</samp> (<samp>(O)</samp>)-type item.
If it uses an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> that returns multiple items, one will
be selected at random. If it returns null or a non-<samp>Object</samp>
item, the spawn attempt will be skipped (with a logged warning if the
item type is invalid).</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that the item will spawn if
selected, as a decimal value between 0 (never) and 1 (always). Default
1.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> The specific season when the forage should
apply. This is more efficient than using <samp>Condition</samp>, but
only supports a single season. Defaults to <samp>null</samp> (all
seasons).</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>MinDailyWeeds</samp><br />
<samp>MaxDailyWeeds</samp></p></td>
<td><p><em>(Optional)</em> The minimum and maximum number of weeds to
spawn in a day, if applicable. Default 1 and 5 respectively.</p></td>
</tr>
<tr>
<td><p><samp>FirstDayWeedMultiplier</samp></p></td>
<td><p><em>(Optional)</em> On the first day of each year, a multiplier
to apply to the number of daily weeds spawned. Default 15.</p></td>
</tr>
<tr>
<td><p><samp>MinDailyForageSpawn</samp><br />
<samp>MaxDailyForageSpawn</samp></p></td>
<td><p><em>(Optional)</em> The minimum and maximum number of forage to
try spawning in one day, if applicable and the location has fewer than
<samp>MaxSpawnedForageAtOnce</samp> forage. Default 1 and 4
respectively.</p></td>
</tr>
<tr>
<td><p><samp>MaxSpawnedForageAtOnce</samp></p></td>
<td><p><em>(Optional)</em> The maximum number of spawned forage that can
be present at once on the map before they stop spawning. Default
6.</p></td>
</tr>
<tr>
<td><p><samp>ChanceForClay</samp></p></td>
<td><p><em>(Optional)</em> The probability that digging a tile will
produce clay, as a value between 0 (never) and 1 (always).</p></td>
</tr>
</tbody>
</table>

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
<td><p><samp>Music</samp></p></td>
<td><p><em>(Optional)</em> The music to play when the player enters the
location (subject to the other fields like
<samp>MusicContext</samp>).</p>
<p>The first matching entry is used. If none match, falls back to
<samp>MusicDefault</samp>.</p>
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
<td><p>The <a href="Modding_Audio" class="wikilink"
title="audio track ID">audio track ID</a> to play.</p></td>
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
<td><p><samp>MusicDefault</samp></p></td>
<td><p><em>(Optional)</em> The music to play if none of the options in
<samp>Music</samp> matched. If this is null, falls back to the
<samp>Music</samp> <a href="Modding_Maps" class="wikilink"
title="map property">map property</a> (if set).</p></td>
</tr>
<tr>
<td><p><samp>MusicContext</samp></p></td>
<td><p><em>(Optional)</em> The music context for this location. The
recommended values are <samp>Default</samp> or <samp>SubLocation</samp>.
Default <samp>Default</samp>.</p>
<p>Setting <samp>SubLocation</samp> has two effects:</p>
<ul>
<li><samp>SubLocation</samp> has a lower priority than
<samp>Default</samp>. In split-screen mode, that means if player A is at
a location with a <samp>Default</samp> music context, and player B is a
location with a <samp>SubLocation</samp> context, the game will choose
player A's music.</li>
<li>When the player leaves a location with <samp>SubLocation</samp>
music, the music will be stopped unless the new location has the same
music and music context set.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>MusicIgnoredInRain</samp></p></td>
<td><p><em>(Optional)</em> Whether the location music is ignored when
it's raining in this location. Default false.</p></td>
</tr>
<tr>
<td><p><samp>MusicIgnoredInSpring</samp><br />
<samp>MusicIgnoredInSummer</samp><br />
<samp>MusicIgnoredInFall</samp><br />
<samp>MusicIgnoredInWinter</samp></p></td>
<td><p><em>(Optional)</em> Whether the location music is ignored in the
given season. Default false.</p></td>
</tr>
<tr>
<td><p><samp>MusicIgnoredInFallDebris</samp></p></td>
<td><p><em>(Optional)</em> Whether the location music is ignored in fall
during windy weather. Default false.</p></td>
</tr>
<tr>
<td><p><samp>MusicIsTownTheme</samp></p></td>
<td><p><em>(Optional)</em> Whether to use the same behavior as <a
href="Pelican_Town" class="wikilink" title="Pelican Town">Pelican
Town</a>'s music: it will start playing after the day music has
finished, and will continue playing while the player travels through
indoor areas, but will stop when entering another outdoor area that
isn't marked with the same <samp>Music</samp> and
<samp>MusicIsTownTheme</samp> values. Default false.</p></td>
</tr>
</tbody>
</table>

### Advanced

| field | effect |
|----|----|
| `CustomFields` | *(Optional)* The <a href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry. |
| `FormerLocationNames` | *(Optional)* The former location names which may appear in save data. See *<a href="#Can_I_rename_a_location?" class="wikilink"
title="Can I rename a location?">Can I rename a location?</a>* in the FAQs for more info. |

## Default entry

The `Data/Locations` asset has a location with the key `Default`. The
`ArtifactSpots`, `Fish`, and `Forage` fields for this entry are added to
every other location's equivalent fields, so this lets you add artifact
spots / fish / forage in all locations.

## Examples

### Simple location

Here's how you'd add a simple location with the default behavior.

Note that is a Content Patcher token, which will be replaced with your
mod ID automatically for the
<a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a>
convention.

1.  <a href="Modding_Content_Patcher" class="wikilink"
    title="Create an empty Content Patcher content pack">Create an empty
    Content Patcher content pack</a>.
2.  <a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
    title="Unpack the game assets">Unpack the game assets</a>, then copy
    & paste a similar vanilla map into your content pack's `assets`
    folder.
3.  Edit the `content.json` to add the location data:

That's it! If you load your game and walk onto tile (10, 10) in town,
you should warp to your custom location.

You can then add more fields to your `Data/Locations` entry (for music,
forage, artifact spots, fish, etc) or
<a href="Modding_Maps" class="wikilink" title="edit the map">edit the
map</a> as needed.

## FAQs

### How do I get to a custom location in-game?

Adding a location to `Data/Locations` only adds the location to the
game. Don't forget to give players some way to reach it, usually by
adding warps from another map using `EditMap` in a
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher content pack">Content Patcher content pack</a>.

For a quick test, you can run the `debug warp <location name>`
<a href="Modding_Console_commands" class="wikilink"
title="console command">console command</a> to warp directly into it.

### Can I make the location conditional?

There's many ways you can decide when players have access. For example,
you can use `EditMap` in a
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher content pack">Content Patcher content pack</a> to
add warps conditionally or to add some form of roadblock that must be
cleared (e.g. a landslide).

**Note:** don't make the existence of the location itself conditional,
just make it unreachable. Removing the location will permanently delete
everything inside it.

### Can I rename a location?

**Renaming a location will permanently lose player changes made for the
old name if you're not careful.**

You can avoid that by setting the `FormerLocationNames` field in
`Data/Locations`. If a location in save data has a name which (a)
matches one of the `FormerLocationNames` and (b) doesn't match the name
of a loaded location, its data will be loaded into the location which
specified the `FormerLocationNames` field instead.

For example:

``` js
"FormerLocationNames": [ "Custom_SomeOldName" ]
```

Legacy names can have any format, but they must be **globally** unique.
They can't match the `Name` or `FormerLocationNames` of any other
location in `Data/Locations` (whether vanilla or custom).

## Location names

In-game locations like the farm or beach are represented by the
<a href="Modding_Modder_Guide_Game_Fundamentals#GameLocation_et_al"
class="wikilink" title="GameLocation class"><samp>GameLocation</samp>
class</a> (or a subclass), and are identified by a unique name.

Here are some of the vanilla locations:

| Name | Class | Description |
|----|----|----|
| `Farm` | `StardewValley.Farm` | The outdoor area of the Pelican Town <a href="The_Farm" class="wikilink" title="farm">farm</a>. |
| `FarmHouse` | `StardewValley.Locations.FarmHouse` | The interior of the <a href="The_Farm#Farmhouse" class="wikilink" title="farm house">farm
house</a>. |
| `FarmCave` | `StardewValley.Locations.FarmCave` | The bats/mushroom <a href="The_Farm#The_Cave" class="wikilink" title="cave">cave</a> on the farm. |
| `Town` | `StardewValley.Locations.Town` | The outdoor area of <a href="Pelican_Town" class="wikilink" title="Pelican Town">Pelican
Town</a>. |
| `JoshHouse` | `StardewValley.GameLocation` | <a href="Alex" class="wikilink" title="Alex">Alex</a>/<a href="George" class="wikilink" title="George">George</a>/<a href="Evelyn" class="wikilink" title="Evelyn">Evelyn</a>'s house. (Josh was the old name for the Alex character.) |
| `HaleyHouse` | `StardewValley.GameLocation` | <a href="Haley" class="wikilink" title="Haley">Haley</a>/<a href="Emily" class="wikilink" title="Emily">Emily</a>'s house. |
| `SamHouse` | `StardewValley.GameLocation` | <a href="Sam" class="wikilink" title="Sam">Sam</a>/<a href="Jodi" class="wikilink" title="Jodi">Jodi</a>/<a href="Kent" class="wikilink" title="Kent">Kent</a>/<a href="Vincent" class="wikilink" title="Vincent">Vincent</a>'s house. |
| `Blacksmith` | `StardewValley.GameLocation` | <a href="Clint" class="wikilink" title="Clint">Clint</a>'s <a href="Blacksmith" class="wikilink" title="blacksmith">blacksmith</a> shop. |
| `ManorHouse` | `StardewValley.Locations.ManorHouse` | Mayor <a href="Lewis" class="wikilink" title="Lewis">Lewis</a>' house. |
| `SeedShop` | `StardewValley.Locations.SeedShop` | <a href="Pierre" class="wikilink" title="Pierre">Pierre</a>'s <a href="Pierre&#39;s_General_Store" class="wikilink"
title="general store">general store</a> (also <a href="Caroline" class="wikilink" title="Caroline">Caroline</a>/<a href="Abigail" class="wikilink" title="Abigail">Abigail</a>'s house and church) |
| `Saloon` | `StardewValley.GameLocation` | <a href="The_Stardrop_Saloon" class="wikilink"
title="The Stardrop Saloon">The Stardrop Saloon</a> (and <a href="Gus" class="wikilink" title="Gus">Gus</a>' house) |
| `Trailer` | `StardewValley.GameLocation` | <a href="Pam" class="wikilink" title="Pam">Pam</a>/<a href="Penny" class="wikilink" title="Penny">Penny</a>'s <a href="trailer" class="wikilink" title="trailer">trailer</a>. |
| `Hospital` | `StardewValley.GameLocation` | <a href="Harvey&#39;s_Clinic" class="wikilink"
title="Harvey&#39;s clinic.">Harvey's clinic.</a> |
| `HarveyRoom` | `StardewValley.GameLocation` | <a href="Harvey" class="wikilink" title="Harvey">Harvey</a>'s room upstairs from the clinic. |
| `Beach` | `StardewValley.Locations.Beach` | <a href="The_Beach" class="wikilink" title="The beach">The beach</a> south of Pelican Town. |
| `ElliottHouse` | `StardewValley.GameLocation` | <a href="Elliott" class="wikilink" title="Elliott">Elliott</a>'s cabin on the beach. |
| `Mountain` | `StardewValley.Locations.Mountain` | The <a href="The_Mountain" class="wikilink"
title="outdoor mountain area">outdoor mountain area</a> where the Carpenter, Linus' tent, and Adventurer's Guild are. |
| `ScienceHouse` | `StardewValley.GameLocation` | The <a href="Carpenter&#39;s_Shop" class="wikilink"
title="Carpenter&#39;s Shop">Carpenter's Shop</a>. |
| `SebastianRoom` | `StardewValley.GameLocation` | <a href="Sebastian" class="wikilink" title="Sebastian">Sebastian</a>'s room in the basement of the carpenter house. |
| `Tent` | `StardewValley.GameLocation` | <a href="Linus" class="wikilink" title="Linus">Linus</a>' <a href="tent" class="wikilink" title="tent">tent</a>. |
| `Forest` | `StardewValley.Locations.Forest` | Cindersap <a href="Cindersap_Forest" class="wikilink" title="forest">forest</a> south of the farm. |
| `WizardHouse` | `StardewValley.Locations.WizardHouse` | The <a href="Wizard" class="wikilink"
title="wizard/Rasmodius">wizard/Rasmodius</a>'s <a href="Wizard&#39;s_Tower" class="wikilink" title="tower">tower</a> |
| `AnimalShop` | `StardewValley.GameLocation` | <a href="Marnie&#39;s_Ranch" class="wikilink"
title="Marnie&#39;s Ranch">Marnie's Ranch</a> |
| `LeahHouse` | `StardewValley.GameLocation` | <a href="Leah&#39;s_Cottage" class="wikilink"
title="Leah&#39;s Cottage">Leah's Cottage</a>. |
| `BusStop` | `StardewValley.Locations.BusStop` | The <a href="Bus_Stop" class="wikilink" title="bus stop">bus stop</a> area between the farm and Pelican Town. |
| `Mine` | `StardewValley.Locations.Mine` | The first room of <a href="The_Mines" class="wikilink" title="the mines">the mines</a>, where the <a href="dwarf" class="wikilink" title="dwarf">dwarf</a>'s shop is. |
| `Sewer` | `StardewValley.Locations.Sewer` | The <a href="The_Sewers" class="wikilink" title="sewers">sewers</a> where <a href="Krobus" class="wikilink" title="Krobus">Krobus</a>' shop is. |
| `BugLand` | `StardewValley.Locations.BugLand` | The <a href="Mutant_Bug_Lair" class="wikilink"
title="mutant bug lair">mutant bug lair</a> in the sewers. |
| `Desert` | `StardewValley.Locations.Desert` | <a href="The_Desert" class="wikilink" title="Calico Desert">Calico
Desert</a> where <a href="Sandy" class="wikilink" title="Sandy">Sandy</a>'s <a href="Oasis" class="wikilink" title="Oasis">Oasis</a> shop and the <a href="Skull_Cavern" class="wikilink" title="skull cavern">skull
cavern</a> are. |
| `Club` | `StardewValley.Locations.Club` | Mr. Qi's <a href="Casino" class="wikilink" title="casino">casino</a> in Sandy's Oasis shop. |
| `SandyHouse` | `StardewValley.GameLocation` | The <a href="Oasis" class="wikilink" title="Oasis">Oasis</a>, Sandy's shop in Calico Desert. |
| `ArchaeologyHouse` | `StardewValley.Locations.LibraryMuseum` | The <a href="Museum" class="wikilink" title="Museum">Museum</a> in Pelican Town, south of the Blacksmith. |
| `WizardHouseBasement` | `StardewValley.GameLocation` | The basement of the <a href="Wizard&#39;s_Tower" class="wikilink"
title="Wizard&#39;s Tower">Wizard's Tower</a> |
| `AdventureGuild` | `StardewValley.Locations.AdventureGuild` | The <a href="Adventurer&#39;s_Guild" class="wikilink"
title="Adventurer&#39;s Guild">Adventurer's Guild</a>, home of <a href="Marlon" class="wikilink" title="Marlon">Marlon</a> and <a href="Gil" class="wikilink" title="Gil">Gil</a>. |
| `Woods` | `StardewValley.Locations.Woods` | The <a href="Secret_Woods" class="wikilink" title="secret woods">secret
woods</a> in Cindersap forest blocked by a large log. |
| `Railroad` | `StardewValley.Locations.Railroad` | The <a href="Railroad" class="wikilink" title="railroad">railroad</a> north of the mountains, where the <a href="Spa" class="wikilink" title="spa">spa</a> is located. |
| `WitchSwamp` | `StardewValley.GameLocation` | The <a href="Witch&#39;s_Swamp" class="wikilink" title="swamp">swamp</a> area where the Witch's Hut is. |
| `WitchHut` | `StardewValley.GameLocation` | The interior of the <a href="Witch&#39;s_Hut" class="wikilink"
title="Witch&#39;s Hut">Witch's Hut</a>. |
| `WitchWarpCave` | `StardewValley.GameLocation` | The cave accessible at the top right of the railroad, which warps to the Witch's swamp. |
| `Summit` | `StardewValley.Locations.Summit` | The <a href="The_Summit" class="wikilink" title="summit">summit</a> north of the railroad. |
| `FishShop` | `StardewValley.Locations.FishShop` | <a href="Willy" class="wikilink" title="Willy">Willy</a>'s <a href="Fish_Shop" class="wikilink" title="shop">shop</a>. |
| `BathHouse_Entry` | `StardewValley.GameLocation` | The entrance room in the <a href="spa" class="wikilink" title="spa">spa</a>, leading to the men's and women's locker rooms. |
| `BathHouse_MensLocker` | `StardewValley.GameLocation` | The men's locker room in the spa. |
| `BathHouse_WomensLocker` | `StardewValley.GameLocation` | The women's locker room in the spa. |
| `BathHouse_Pool` | `StardewValley.Locations.BathHousePool` | The bathhouse pool in the spa. |
| `CommunityCenter` | `StardewValley.Locations.CommunityCenter` | The inside of the <a href="Community_Center" class="wikilink"
title="Community Center">Community Center</a>. |
| `JojaMart` | `StardewValley.Locations.JojaMart` | The inside of Pelican Town's <a href="JojaMart" class="wikilink" title="JojaMart">JojaMart</a>. |
| `Greenhouse` | `StardewValley.GameLocation` | The <a href="Greenhouse" class="wikilink" title="Greenhouse">Greenhouse</a> on the player's farm. |
| `SkullCave` | `StardewValley.GameLocation` | The entrance of the Skull Cavern in Calico desert. |
| `Backwoods` | `StardewValley.GameLocation` | The <a href="Backwoods" class="wikilink" title="backwoods">backwoods</a> area north of the farm/west of the bus stop, leading to the bus tunnel or to the mountains. |
| `Tunnel` | `StardewValley.GameLocation` | The dark <a href="The_Tunnel" class="wikilink" title="bus tunnel">bus tunnel</a> to the west of the bus stop. |
| `Trailer_Big` | `StardewValley.GameLocation` | The inside of Pam/Penny's house after the <a href="Trailer#Community_Upgrade" class="wikilink"
title="Community Upgrade">Community Upgrade</a>. |
| `Cellar` | `StardewValley.Locations.Cellar` |  |
| `Cellar2` | `StardewValley.Locations.Cellar` |  |
| `Cellar3` | `StardewValley.Locations.Cellar` |  |
| `Cellar4` | `StardewValley.Locations.Cellar` |  |
| `BeachNightMarket` | `StardewValley.Locations.BeachNightMarket` | The beach south of Pelican Town during the <a href="Night_Market" class="wikilink" title="Night Market">Night
Market</a>. |
| `MermaidHouse` | `StardewValley.Locations.MermaidHouse` | The interior of the <a href="Night_Market#Mermaid_Boat" class="wikilink"
title="mermaid boat">mermaid boat</a> at the <a href="Night_Market" class="wikilink" title="Night Market">Night
Market</a>. |
| `Submarine` | `StardewValley.Locations.Submarine` | The interior of the <a href="Night_Market#Fishing_Submarine" class="wikilink"
title="fishing submarine">fishing submarine</a> during the Night Market. |
| `AbandonedJojaMart` | `StardewValley.Locations.AbandonedJojaMart` | The small interior of the <a href="Bundles#Abandoned_JojaMart" class="wikilink"
title="abandoned JojaMart">abandoned JojaMart</a> where the Missing Bundle is. |
| `MovieTheater` | `StardewValley.Locations.MovieTheater` | The interior of the <a href="Movie_Theater" class="wikilink" title="Movie Theater">Movie
Theater</a> that replaces JojaMart. |
| `Sunroom` | `StardewValley.GameLocation` | <a href="Caroline" class="wikilink" title="Caroline">Caroline</a>'s sunroom inside Pierre's General Store. |
| `BoatTunnel` | `StardewValley.Locations.BoatTunnel` | Where <a href="Fish_Shop#Willy&#39;s_Boat" class="wikilink"
title="Willy&#39;s Boat">Willy's Boat</a> is, in back of the fish shop. |
| `IslandSouth` | `StardewValley.Locations.IslandSouth` | Ginger Island, <a href="Ginger_Island#Island_South" class="wikilink"
title="the docks">the docks</a> where the player first lands and where the beach resort is. |
| `IslandSouthEast` | `StardewValley.Locations.IslandSouthEast` | Ginger Island, <a href="Ginger_Island#Island_Southeast" class="wikilink"
title="where the mermaid and pirate cove are">where the mermaid and
pirate cove are</a>. |
| `IslandSouthEastCave` | `StardewValley.Locations.IslandSouthEastCave` | The <a href="Ginger_Island#Pirate_Cove" class="wikilink"
title="pirate cove">pirate cove</a>. |
| `IslandEast` | `StardewValley.Locations.IslandEast` | <a href="Ginger_Island#Island_East" class="wikilink"
title="Ginger Island jungle">Ginger Island jungle</a>, where <a href="Leo" class="wikilink" title="Leo">Leo</a>'s hut is. |
| `IslandWest` | `StardewValley.Locations.IslandWest` | Ginger Island, <a href="Ginger_Island#Island_West" class="wikilink"
title="Island West">Island West</a>, where the farm and Birdie's Shack are. |
| `IslandNorth` | `StardewValley.Locations.IslandNorth` | Ginger Island, <a href="Ginger_Island#Island_North" class="wikilink"
title="Island North">Island North</a>, where the volcano and Professor Snail's tent are. |
| `IslandHut` | `StardewValley.Locations.IslandHut` | The interior of <a href="Leo" class="wikilink" title="Leo">Leo</a>'s hut on <a href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a>. |
| `IslandWestCave1` | `StardewValley.Locations.IslandWestCave1` | The Ginger Island cave where the <a href="Ginger_Island#Colored_Crystals_Puzzle" class="wikilink"
title="colored crystals puzzle">colored crystals puzzle</a> can be found. |
| `IslandNorthCave1` | `StardewValley.Locations.IslandLocation` | The <a href="Ginger_Island#Dig_Site" class="wikilink"
title="mushroom cave">mushroom cave</a> on Ginger Island where Professor Snail is initially blocked in by a boulder. |
| `IslandFieldOffice` | `StardewValley.Locations.IslandFieldOffice` | The interior of Professor Snail's <a href="Island_Field_Office" class="wikilink"
title="Island Field Office">Island Field Office</a> tent. |
| `IslandFarmHouse` | `StardewValley.Locations.IslandFarmHouse` | The interior of the <a href="Island_Farmhouse" class="wikilink" title="farm house">farm
house</a> on Ginger Island. |
| `CaptainRoom` | `StardewValley.Locations.IslandLocation` | The interior of the <a href="Ginger_Island#Shipwreck" class="wikilink"
title="shipwreck">shipwreck</a> on Ginger Island West. |
| `IslandShrine` | `StardewValley.Locations.IslandShrine` | The <a href="Ginger_Island#Gem_Birds" class="wikilink"
title="area East of the jungle">area East of the jungle</a> on Ginger Island. |
| `IslandFarmCave` | `StardewValley.Locations.IslandFarmCave` | The interior of <a href="Ginger_Island#Gourmand_Frog" class="wikilink"
title="Gourmand Frog&#39;s cave">Gourmand Frog's cave</a> on Ginger Island. |
| `Caldera` | `StardewValley.Locations.Caldera` | The <a href="Forge" class="wikilink" title="volcano caldera">volcano
caldera</a> on Ginger Island at the end of the volcano dungeon. |
| `LeoTreeHouse` | `StardewValley.GameLocation` | Leo's <a href="Treehouse" class="wikilink" title="tree house">tree house</a> home. |
| `QiNutRoom` | `StardewValley.Locations.IslandLocation` | <a href="Qi&#39;s_Walnut_Room" class="wikilink"
title="Mr. Qi&#39;s Walnut Room">Mr. Qi's Walnut Room</a> |
|  |  |  |

## See also

- <a href="Modding_Location_contexts" class="wikilink"
  title="Modding:Location contexts">Modding:Location contexts</a>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Местоположение" class="wikilink"
title="ru:Модификации:Местоположение">ru:Модификации:Местоположение</a>
<a href="zh_模组_地点数据" class="wikilink"
title="zh:模组:地点数据">zh:模组:地点数据</a>
