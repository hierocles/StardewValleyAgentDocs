---
title: "Game Fundamentals"
wiki_source: "Modding:Modder Guide/Game Fundamentals"
permalink: /Modding:Modder_Guide/Game_Fundamentals/
category: smapi
tags: [game-fundamentals, general-concepts, time-format, tiles, positions, zoom-level, ui-scaling, multiplayer-concepts-for-c-mods]
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

This page explains some of the Stardew Valley fundamentals that are
useful for modders. See also
<a href="Modding_Common_tasks" class="wikilink"
title="Modding:Common tasks">Modding:Common tasks</a>.

## General concepts

### Time format

The in-game time of day is tracked using a version of
<a href="wikipedia_24-hour_clock" class="wikilink"
title="24-hour format">24-hour format</a> informally called "26-hour
time", measured in 10-minute intervals. This is the format used by
`Game1.timeOfDay` in a
<a href="Modding_Modder_Guide_Get_Started" class="wikilink"
title="C# mod">C# mod</a> or `<nowiki></nowiki>` in a
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher pack">Content Patcher pack</a>.

Sample times:

| time value | display text              |
|------------|---------------------------|
| 600        | 6:00 am                   |
| 1250       | 12:50 am                  |
| 1300       | 1:00 pm                   |
| 2600       | 2:00 am (before sleeping) |

The internal time will continue incrementing forever until you sleep
(e.g. 6am the next day would be 3000 in that case).

### Tiles

The world is laid out as a grid of *tiles*. Each tile has an (x, y)
coordinate which represents its position on the map, where (0, 0) is the
top-left tile. The *x* value increases towards the right, and *y*
increases downwards. For example:

<a href="File_Modding_-_creating_an_XNB_mod_-_tile_coordinates.png"
class="wikilink"
title="File:Modding - creating an XNB mod - tile coordinates.png"><span>File:Modding</span>
- creating an XNB mod - tile coordinates.png</a>

You can use the mod to see tile coordinates in-game.

### Positions

The game uses three related coordinate systems:

| coordinate system | relative to | notes |
|----|----|----|
| tile position | top-left corner of the map | measured in <a href="#Tiles" class="wikilink" title="tiles">tiles</a>; used when placing things on the map (*e.g.,* `location.Objects` uses tile positions). |
| absolute position | top-left corner of the map | measured in pixels; used when more granular measurements are needed (*e.g.,* NPC movement). |
| screen position | top-left corner of the visible screen | measured in pixels; used when drawing to the screen. |

Here's how to convert between them (there are also helpful methods in
Utility for some of these):

<table>
<thead>
<tr>
<th colspan="3"><p>conversion</p></th>
<th><p>formula</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>absolute</p></td>
<td><p>→</p></td>
<td><p>screen</p></td>
<td><p><code>x - Game1.viewport.X, y - Game1.viewport.Y</code></p></td>
</tr>
<tr>
<td><p>absolute</p></td>
<td><p>→</p></td>
<td><p>tile</p></td>
<td><p><code>x / Game1.tileSize, y / Game1.tileSize</code></p></td>
</tr>
<tr>
<td><p>screen</p></td>
<td><p>→</p></td>
<td><p>absolute</p></td>
<td><p><code>x + Game1.viewport.X, y + Game1.viewport.Y</code></p></td>
</tr>
<tr>
<td><p>screen</p></td>
<td><p>→</p></td>
<td><p>tile</p></td>
<td><p><code>(x + Game1.viewport.X) / Game1.tileSize, (y + Game1.viewport.Y) / Game1.tileSize</code></p></td>
</tr>
<tr>
<td><p>tile</p></td>
<td><p>→</p></td>
<td><p>absolute</p></td>
<td><p><code>x * Game1.tileSize, y * Game1.tileSize</code></p></td>
</tr>
<tr>
<td><p>tile</p></td>
<td><p>→</p></td>
<td><p>screen</p></td>
<td><p><code>(x * Game1.tileSize) - Game1.viewport.X, (y * Game1.tileSize) - Game1.viewport.Y</code></p></td>
</tr>
</tbody>
</table>

### Zoom level

The player can set an in-game zoom level between 75% and 200%, which
adjusted the size of all pixels shown on the screen. For example, here's
a player with the same window size at different zoom levels:

| min zoom level (75%) | max zoom level (200%) |
|----|----|
| <a href="File_Zoom_level_75.png" class="wikilink"
title="300px">300px</a> | <a href="File_Zoom_level_200.png" class="wikilink"
title="300px">300px</a> |

Effect on SMAPI mods
In game code, this is represented by the `Game1.options.zoomLevel`
field. Coordinates are generally adjusted for zoom level automatically,
so you rarely need to account for this; but you can convert an
unadjusted coordinate using `position * (1f / Game1.options.zoomLevel)`
if needed.

### UI scaling

The player can scale the UI between 75% and 150%, separately from and
alongside the
<a href="#Zoom_level" class="wikilink" title="zoom level">zoom level</a>.
That adjusts the size of pixels shown on the screen for UI elements
only. For example, here's a player with the same window size at
different UI scaling levels:

| min UI scale (75%) | max UI scale (150%) |
|----|----|
| <a href="File_UI_scale_75.png" class="wikilink" title="300px">300px</a> | <a href="File_UI_scale_150.png" class="wikilink" title="300px">300px</a> |

Effect on SMAPI mods
The game has two distinct scaling modes depending on the context: *UI
mode* and *non-UI mode*. You can check `Game1.uiMode` to know which mode
is active. You should be careful not to mix UI and non-UI coordinates to
avoid tricky calculations; for example, do all your work in one
coordinate system and then convert them once.

<!-- -->


A quick reference of common scenarios:

{\| class="wikitable"

\|- ! context ! scaling mode which applies \|- \| clickable menus \| UI
mode (usually) \|- \| HUD elements \| UI mode \|- \|
<a href="Modding_Modder_Guide_APIs_Events#Display.RenderingActiveMenu"
class="wikilink"
title="RenderingActiveMenu"><samp>RenderingActiveMenu</samp></a>\
<a href="Modding_Modder_Guide_APIs_Events#Display.RenderedActiveMenu"
class="wikilink"
title="RenderedActiveMenu"><samp>RenderedActiveMenu</samp></a> \| UI
mode \|- \| <a href="Modding_Modder_Guide_APIs_Events#Display.Rendering"
class="wikilink" title="Rendering"><samp>Rendering</samp></a>\
<a href="Modding_Modder_Guide_APIs_Events#Display.Rendering"
class="wikilink" title="Rendered"><samp>Rendered</samp></a> \| depends
on the context; check `Game1.uiMode` \|- \| `draw` method for world
objects \| non-UI mode \|- \| tile (non-pixel) coordinates \| not
affected by UI scaling \|}


If you need to draw UI when the game isn't in UI mode, you can
explicitly set UI scaling mode:

:

``` c#
Game1.game1.InUIMode(() =>
{
   // your UI draw code here
});
```


In UI mode, you should usually replace `Game1.viewport` with
`Game1.uiViewport`. **Don't** do this if you'll adjust the positions for
UI scaling separately, since double-conversion will give you incorrect
results. You can convert between UI and non-UI coordinates using
`Utility.ModifyCoordinatesForUIScale` and
`Utility.ModifyCoordinatesFromUIScale`.

<!-- -->


You can test whether your mod accounts for this correctly by setting the
zoom to maximum and the UI scale to minimum (*i.e.,* have them at
opposite values) or vice versa; in particular check any logic which
handles pixel positions, like menus clicking.

## Multiplayer concepts for C# mods

### Net fields

A 'net type' is any of several classes which Stardew Valley uses to sync
data between players, and a 'net field' is any field or property of
those types. They're named for the `Net` prefix in their type names. Net
types can represent simple values like `NetBool`, or complex values like
`NetFieldDictionary`. The game will regularly collect all the net fields
reachable from `Game1.netWorldState` and sync them with other players.
That means that many mod changes will be synchronised automatically in
multiplayer.

Here's how to access the data in some common net types:

<table>
<thead>
<tr>
<th><p>net type</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>NetBool</samp><br />
<samp>NetColor</samp><br />
<samp>NetFloat</samp><br />
<samp>NetInt</samp><br />
<samp>NetPoint</samp><br />
<samp>NetString</samp></p></td>
<td><p>A simple synchronised value. Access the value using
<samp>field.Value</samp>.</p></td>
</tr>
<tr>
<td><p><samp>NetCollection&lt;T&gt;</samp><br />
<samp>NetList&lt;T&gt;</samp><br />
<samp>NetObjectList&lt;T&gt;</samp></p></td>
<td><p>A list of <samp>T</samp> values. This implements the standard
interfaces like <a
href="https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1"><samp>IEnumerable&lt;T&gt;</samp></a>
and <a
href="https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.ilist-1"><samp>IList&lt;T&gt;</samp></a>,
so you can iterate it directly like
<code>foreach (T value in field)</code>.</p></td>
</tr>
<tr>
<td><p><samp>NetLongDictionary&lt;TValue, TNetValue&gt;</samp><br />
<samp>NetPointDictionary&lt;TValue, TNetValue&gt;</samp><br />
<samp>NetVector2Dictionary&lt;TValue, TNetValue&gt;</samp></p></td>
<td><p>Maps <samp>Long</samp>, <samp>Point</samp>, or
<samp>Vector2</samp> keys to instances of <samp>TValue</samp> (the
underlying value type) and <samp>TNetValue</samp> (the synchronised net
type). You can iterate key/value pairs like
<code>foreach (KeyValuePair&lt;Long, TValue&gt; pair in field.Pairs)</code>
(replacing <samp>Long</samp> with <samp>Point</samp> or
<samp>Vector2</samp> if needed).</p></td>
</tr>
</tbody>
</table>

### Farmhand shadow world

In <a href="multiplayer" class="wikilink"
title="multiplayer">multiplayer</a>, only the main player has access to
all the locations in the game; the game then synchronizes a few of those
locations (called *active locations*) to secondary players (i.e.
*farmhands*). The default active locations are the farmhand's current
location, farm, farm cave, main farmhouse (not cabins or cellars), and
greenhouse.

Otherwise a farmhand's game creates a single-player copy of the world
before they join. The unsynchronized locations often don't match what
players within those locations see.

This has some significant implications for C# mods:

- The `Game1.locations` list shows both active and shadow locations.
  While mods can access the shadow locations, these don't reflect the
  real data on the server and any changes to them won't be synced to the
  host.
- There may be duplicate copies of NPCs, horses, etc in the shadow
  world. Only those in active locations are 'real'.
- Game methods (like `Game1.getCharacterByName`) may not correctly
  distinguish between the 'real' and 'shadow' copies.
- When a farmhand warps to a location, the game fetches the real
  location from the host player before the warp completes. For a short
  while, the farmhand may have a null `currentLocation` field while
  they're between locations.

You can check whether a location is active using its `IsActiveLocation`
method:

``` c#
foreach (GameLocation location in Game1.locations)
{
    if (!location.IsActiveLocation())
        continue; // shadow location

    ...
}
```

## Main classes

### Game1

`Game1` is the game's core logic. Most of the game state is tracked
through this class. Here are some of the most useful fields:

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>type</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Game1.player</samp></p></td>
<td><p><samp>Farmer</samp></p></td>
<td><p>The current player.</p></td>
</tr>
<tr>
<td><p><samp>Game1.currentLocation</samp></p></td>
<td><p><samp>[[#GameLocation|GameLocation]]</samp></p></td>
<td><p>The game location containing the current player. <strong>For a
non-main player, may be <samp>null</samp> when transitioning between
locations.</strong></p></td>
</tr>
<tr>
<td><p><samp>Game1.locations</samp></p></td>
<td><p><samp>IList&lt;[[#GameLocation|GameLocation]]&gt;</samp></p></td>
<td><p>All locations in the game. <strong>For a non-main player, use <a
href="Modding_Modder_Guide_APIs_Multiplayer#Get_active_locations"
class="wikilink" title="SMAPI&#39;s GetActiveLocations method">SMAPI's
<samp>GetActiveLocations</samp> method</a> instead.</strong></p></td>
</tr>
<tr>
<td><p><samp>Game1.timeOfDay</samp><br />
<samp>Game1.dayOfMonth</samp><br />
<samp>Game1.currentSeason</samp><br />
<samp>Game1.year</samp></p></td>
<td><p><samp>int</samp><br />
<samp>int</samp><br />
<samp>string</samp><br />
<samp>int</samp></p></td>
<td><p>The current time, day, season, and year. See also <a
href="Modding_Modder_Guide_APIs_Utilities#Dates" class="wikilink"
title="SMAPI&#39;s date utility">SMAPI's date utility</a>.</p></td>
</tr>
<tr>
<td><p><samp>Game1.itemsToShip</samp></p></td>
<td><p><samp>IList&lt;Item&gt;</samp></p></td>
<td><p>Do not use (this is part of the save logic). See
<samp>Game1.getFarm().getShippingBin(Farmer)</samp> instead.</p></td>
</tr>
<tr>
<td><p><samp>Game1.activeClickableMenu</samp></p></td>
<td><p><samp>IClickableMenu</samp></p></td>
<td><p>The modal menu being displayed. Creating an
<samp>IClickableMenu</samp> subclass and assigning an instance to this
field will display it.</p></td>
</tr>
</tbody>
</table>

### <span id="GameLocation"></span>GameLocation et al

- `GameLocation` represents an in-game location players can visit. Each
  location has a map (the tile layout), objects, trees, characters, etc.
  Here are some of the most useful fields for any location:
  | field | type | purpose |
  |----|----|----|
  | `Name` | `string` | The unique name for this location. (This isn't unique for constructed building interiors like cabins; see `uniqueName` instead.) |
  | `IsFarm` | `bool` | Whether this is a farm, where crops can be planted. |
  | `IsGreenhouse` | `bool` | Whether this is a greenhouse, where crops can be planted and grown all year. |
  | `IsOutdoors` | `bool` | Whether the location is outdoors (as opposed to a greenhouse, building, etc). |
  | `characters` | <a href="#Net_fields" class="wikilink"
  title="NetCollection"><samp>NetCollection</samp></a> of `NPC` | The villagers, pets, horses, and monsters in the location. |
  | `critters` | `List` of `Critter` | The temporary birds, squirrels, or other critters in the location. |
  | `debris` | <a href="#Net_fields" class="wikilink"
  title="NetCollection"><samp>NetCollection</samp></a> of `Debris` | The floating items in the location. |
  | `farmers` | `FarmerCollection` | The players in the location. |
  | `Objects` | `OverlaidDictionary` | The placed fences, crafting machines, and other objects in the current location. (`OverlaidDictionary` is basically a <a href="#Net_fields" class="wikilink"
  title="NetVector2Dictionary"><samp>NetVector2Dictionary</samp></a> with logic added to show certain quest items over pre-existing objects.) |
  | `terrainFeatures` | <a href="#Net_fields" class="wikilink"
  title="NetVector2Dictionary"><samp>NetVector2Dictionary</samp></a> of `TerrainFeature` | The trees, fruit trees, tall grass, tilled dirt (including crops), and flooring in the location. For each pair, the key is their tile position and the value is the terrain feature instance. |
  | `waterTiles` | `bool[,]` | A multi-dimensional array which indicates whether each tile on the map is a lake/river tile. For example, `if (location.waterTiles[10, 20])` checks the tile at <a href="#Tiles" class="wikilink" title="position">position</a> (10, 20). |
- `BuildableGameLocation` is a subclass of `GameLocation` for locations
  where players can construct buildings. In the vanilla game, only the
  farm is a buildable location. Here are the most useful fields:
  | field | type | purpose |
  |----|----|----|
  | `buildings` | <a href="#Net_fields" class="wikilink"
  title="NetCollection"><samp>NetCollection</samp></a> of `Building` | The buildings in the location. |
- `Farm` is a subclass of both `GameLocation` and
  `BuildableGameLocation` for locations where the player can have
  animals and grow crops. In the vanilla, there's only one farm location
  (accessed using `Game1.getFarm()`). Here are its most useful
  properties:
  | field | type | purpose |
  |----|----|----|
  | `animals` | <a href="#Net_fields" class="wikilink"
  title="NetLongDictionary"><samp>NetLongDictionary</samp></a> of `FarmAnimal` | The farm animals currently in the location. |
  | `resourceClumps` | <a href="#Net_fields" class="wikilink"
  title="NetCollection"><samp>NetCollection</samp></a> of `ResourceClump` | The giant crops, large stumps, boulders, and meteorites in the location. |
  | `piecesOfHay` | <a href="#Net_fields" class="wikilink"
  title="NetInt"><samp>NetInt</samp></a> | The amount of hay stored in silos. |
  | `shippingBin` | <a href="#Net_fields" class="wikilink"
  title="NetCollection"><samp>NetCollection</samp></a> of `Item` | The items in the shipping bin. |
- There are a number of subclasses for specific location (like
  `AdventureGuild`) which have fields useful for specific cases.

<a href="es_Modding_Guía_del_Modder_Fundamentos_del_juego"
class="wikilink"
title="es:Modding:Guía del Modder/Fundamentos del juego">es:Modding:Guía
del Modder/Fundamentos del juego</a>
<a href="ru_Модификации_Руководство_мододела_Основы_игры"
class="wikilink"
title="ru:Модификации:Руководство мододела/Основы игры">ru:Модификации:Руководство
мододела/Основы игры</a>
<a href="zh_模组_制作指南_游戏基本架构" class="wikilink"
title="zh:模组:制作指南/游戏基本架构">zh:模组:制作指南/游戏基本架构</a>
