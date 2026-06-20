---
title: "World Map"
wiki_source: "Modding:World map"
permalink: /Modding:World_map/
category: game
tags: [world-map, data, overview, format, example, real-time-positioning, automatic-positioning-recommended, manual-positioning]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how to edit the world map shown in the game menu.

**To edit location maps, see <a href="Modding_Maps" class="wikilink"
title="Modding:Maps">Modding:Maps</a>. See also
<a href="Modding_Index#Creating_mods" class="wikilink"
title="an intro to making mods">an intro to making mods</a>.**

## Data

### Overview

You can change the world map by editing the `Data/WorldMap` asset. You
can add custom maps for certain locations, apply texture overlays,
add/edit tooltips, set player marker positioning, etc.

<a href="File_Modding_map_area.png" class="wikilink"
title="thumb">thumb</a>

The game divides the world map into three main concepts (see example at
right):

- A **region** is a large-scale part of the world containing everything
  shown on the map. For example, the default world map is the Valley
  region.
- A **map area** is a subset of the world map which optionally add
  tooltips, scroll text, texture overlays, and player marker positioning
  info.
- A **map area position** matches in-game locations and
  <a href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
  title="tile coordinates">tile coordinates</a> to the drawn world map.
  The game uses this to automatically position player markers at a
  relative position on the world map (e.g. so you can watch other
  players move across the location on the map).

In the data model:

- each entry is a region;
- each entry's `MapAreas` are the region's map area;
- and each map area's `WorldPositions` are the world map positions.

The game will find the first `WorldPositions` entry which matches the
current location, and assume you're in the region and map area which
contains it. If there's none found, it defaults to the farm.

### Format

The `Data/WorldMap` data asset consists of a string → model lookup,
where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  region.
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
<td><p><samp>BaseTexture</samp></p></td>
<td><p><em>(Optional)</em> The base texture to draw for the map, if any.
The first matching texture is applied. If map areas provide their own
texture too, they're drawn on top of this base texture.</p>
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
class="wikilink" title="unique string ID">unique string ID</a> for the
texture entry within the list.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture to draw.</p></td>
</tr>
<tr>
<td><p><samp>SourceRect</samp></p></td>
<td><p><em>(Optional)</em> The pixel area within the
<samp>Texture</samp> to draw, specified as an object with
<samp>X</samp>, <samp>Y</samp>, <samp>Width</samp>, and
<samp>Height</samp> fields. Defaults to the entire texture
image.</p></td>
</tr>
<tr>
<td><p><samp>MapPixelArea</samp></p></td>
<td><p><em>(Optional)</em> The pixel area within the map which is
covered by this area, specified as an object with <samp>X</samp>,
<samp>Y</samp>, <samp>Width</samp>, and <samp>Height</samp> fields. If
omitted, draws the entire <samp>SourceRect</samp> area starting from the
top-left corner of the map.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this texture should be selected. Defaults to always
selected.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>MapAreas</samp></p></td>
<td><p>The areas to draw on top of the <samp>BaseTexture</samp>. These
can provide tooltips, scroll text, texture overlays, and player marker
positioning info.</p>
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
class="wikilink" title="unique string ID">unique string ID</a> for the
map area within the list.</p></td>
</tr>
<tr>
<td><p><samp>PixelArea</samp></p></td>
<td><p>The pixel area within the map which is covered by this area. This
is used to set the default player marker position, and is the default
value for pixel areas in other fields below.</p></td>
</tr>
<tr>
<td><p><samp>ScrollText</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the scroll text (shown at the bottom of the map when the player is in
this area). Defaults to none.</p></td>
</tr>
<tr>
<td><p><samp>Textures</samp></p></td>
<td><p><em>(Optional)</em> The image overlays to apply to the map. All
matching textures are applied.</p>
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
class="wikilink" title="unique string ID">unique string ID</a> for the
texture entry within the area.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture to draw.</p>
<p>If set to the exact string <samp>MOD_FARM</samp>, the game will apply
the texture for the current farm type (regardless of whether it's a
vanilla or mod farm type). This should usually be used with
<code>"MapPixelArea": "0 43 131 61"</code> (the farm area on the default
map).</p></td>
</tr>
<tr>
<td><p><samp>SourceRect</samp></p></td>
<td><p><em>(Optional)</em> The pixel area within the
<samp>Texture</samp> to draw, specified as an object with
<samp>X</samp>, <samp>Y</samp>, <samp>Width</samp>, and
<samp>Height</samp> fields. Defaults to the entire texture
image.</p></td>
</tr>
<tr>
<td><p><samp>MapPixelArea</samp></p></td>
<td><p><em>(Optional)</em> The pixel area within the map which is
covered by this area, specified as an object with <samp>X</samp>,
<samp>Y</samp>, <samp>Width</samp>, and <samp>Height</samp> fields. If
omitted, defaults to the map area's <samp>PixelArea</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this texture should be selected. Defaults to always
selected.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Tooltips</samp></p></td>
<td><p><em>(Optional)</em> The tooltips to show when hovering over parts
of this area on the world map.</p>
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
class="wikilink" title="unique string ID">unique string ID</a> for the
tooltip within the area.</p></td>
</tr>
<tr>
<td><p><samp>Text</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the text to show in a tooltip.</p></td>
</tr>
<tr>
<td><p><samp>PixelArea</samp></p></td>
<td><p><em>(Optional)</em> The pixel area within the map which can be
hovered to show this tooltip. Defaults to the area's
<samp>PixelArea</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this tooltip should be available. Defaults to always
available.</p></td>
</tr>
<tr>
<td><p><samp>KnownCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the area is known by the player, so the
<samp>Text</samp> is shown as-is. If this is false, the tooltip text is
replaced with <samp>???</samp>. Defaults to always known.</p></td>
</tr>
<tr>
<td><p><samp>LeftNeighbor</samp><br />
<samp>RightNeighbor</samp><br />
<samp>UpNeighbor</samp><br />
<samp>DownNeighbor</samp></p></td>
<td><p><em>(Optional)</em> When navigating the world map with a
controller, the tooltip to snap to when the player moves the cursor
while it's on this tooltip.</p>
<p>This must specify the area and tooltip formatted like
<samp>areaId/tooltipId</samp> (not case-sensitive). If there are
multiple possible neighbors, they can be specified in comma-delimited
form; the first valid one will be used.</p>
<p>For example, this will snap to the community center when the user
moves the cursor to the right:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RightNeighbor&quot;</span><span class="er">:</span> <span class="st">&quot;Town/CommunityCenter&quot;</span></span></code></pre></div>
<p>A blank value will be ignored, but the game will log a warning if you
specify neighbor IDs and none of them match. To silently ignore them
instead (e.g. for a conditional location), you can add 'ignore' as an
option:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RightNeighbor&quot;</span><span class="er">:</span> <span class="st">&quot;Town/SomeOptionalLocation, ignore&quot;</span></span></code></pre></div>
<p>See also the <samp>MapNeighborIdAliases</samp> field in the region
data.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>WorldPositions</samp></p></td>
<td><p><em>(Optional)</em> The in-world locations and <a
href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
title="tile coordinates">tile coordinates</a> to match to this map area.
The game uses this to automatically position player markers at a
relative position on the world map (e.g. so you can watch other players
move across the location on the map).</p>
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
entry within the area.</p></td>
</tr>
<tr>
<td><p><samp>LocationContext</samp></p></td>
<td><p><em>(Optional)</em> The location context in which this world
position applies. The vanilla contexts are <samp>Default</samp> (valley)
and <samp>Island</samp> (<a href="Ginger_Island" class="wikilink"
title="Ginger Island">Ginger Island</a>).</p></td>
</tr>
<tr>
<td><p><samp>LocationName</samp></p></td>
<td><p><em>(Optional)</em> The location name to which this world
position applies. Any location within <a href="The_Mines"
class="wikilink" title="the mines">the mines</a> and the <a
href="Skull_Cavern" class="wikilink" title="Skull Cavern">Skull
Cavern</a> will be <samp>Mines</samp> and <samp>SkullCave</samp>
respectively, and festivals use the map asset name (like
<samp>Town-EggFestival</samp>).</p></td>
</tr>
<tr>
<td><p><samp>LocationNames</samp></p></td>
<td><p><em>(Optional)</em> Equivalent to <samp>LocationName</samp>, but
you can specify multiple locations as an array.</p></td>
</tr>
<tr>
<td><p><samp>TileArea</samp><br />
<samp>MapPixelArea</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
title="tile area">tile area</a> within the in-game location
(<samp>TileArea</samp>) and the equivalent pixel area on the world map
(<samp>MapPixelArea</samp>). These are used to calculate the position of
a character or player within the map view, given their real position
in-game. For example, if the player is in the top-right corner of the
tile area in-game, they'll be shown in the top-right corner of the drawn
area on the world map.</p>
<p>Both are specified as an object with <samp>X</samp>, <samp>Y</samp>,
<samp>Width</samp>, and <samp>Height</samp> fields.
<samp>TileArea</samp> defaults to the entire location, and
<samp>MapPixelArea</samp> defaults to the map area's
<samp>PixelArea</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ScrollText</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the scroll text shown at the bottom of the map when the player is within
this position. Defaults to the map area's <samp>ScrollText</samp>, if
any.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry should be applied. Defaults to always
applied.</p></td>
</tr>
<tr>
<td><p><samp>ScrollTextZones</samp></p></td>
<td><p><em>(Optional, specialized)</em> Smaller areas within the world
map position which have their own scroll text (like "Mountains" vs
"Mountain Lake" in the <a href="The_Mountain" class="wikilink"
title="mountain area">mountain area</a>).</p>
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
entry within the list.</p></td>
</tr>
<tr>
<td><p><samp>TileArea</samp></p></td>
<td><p>The tile area within the position's <samp>TileArea</samp> for
which this entry applies. See details on the parent field.</p></td>
</tr>
<tr>
<td><p><samp>ScrollText</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the scroll text
shown at the bottom of the map when the player is within this scroll
text zone.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>ExtendedTileArea</samp></p></td>
<td><p><em>(Optional, specialized)</em> The <a
href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
title="tile area">tile area</a> within the in-game location to which
this position applies, including tiles that are outside the
<samp>TileArea</samp>. The <samp>ExtendedTileArea</samp> must fully
contain <samp>TileArea</samp>, since the latter won't be checked for the
initial detection anymore.</p>
<p>For example, let's say we have this <samp>ExtendedTileArea</samp>
(the larger box) and <samp>TileArea</samp> (the smaller box inside it),
and the player is at position X:</p>
<pre><code>┌────────────────────┐
│    ┌────────┐      │
│ X  │        │      │
│    │        │      │
│    └────────┘      │
└────────────────────┘</code></pre>
<p>In this case, the entry would be selected (since the player is inside
the <samp>ExtendedTileArea</samp>), and their coordinates would be
shifted into the nearest <samp>TileArea</samp> position:</p>
<pre><code>┌────────────────────┐
│    ┌────────┐      │
│    │X       │      │
│    │        │      │
│    └────────┘      │
└────────────────────┘</code></pre>
<p>This is used for complex locations that use multiple tile areas to
match a drawn map with a different layout. This can be omitted in most
cases.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>MapNeighborIdAliases</samp></p></td>
<td><p><em>(Optional)</em> A set of aliases that can be used in tooltip
fields like <samp>LeftNeighbor</samp> instead of the specific values
they represent. Aliases can't be recursive.</p>
<p>For example, this lets you use <samp>Beach/FishShop</samp> in
neighbor fields instead of specifying the specific tooltip IDs each
time:</p>
<div class="sourceCode" id="cb5"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;MapNeighborIdAliases&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Beach/FishShop&quot;</span><span class="fu">:</span> <span class="st">&quot;Beach/FishShop_DefaultHours, Beach/FishShop_ExtendedHours&quot;</span></span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

### Example

This <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> content pack adds a new
world map for
<a href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a>. If the player unlocked the
<a href="Ginger_Island#Beach_Resort" class="wikilink"
title="beach resort">beach resort</a>, it applies the beach resort
texture.

## Real-time positioning

The world map generally shows players' positions in real-time. There are
three main approaches to do this for a custom location.

### Automatic positioning (recommended)

If the drawn map area closely matches the in-game location, the game can
determine positions automatically based on the `PixelArea` and
`LocationName` fields in `Data/WorldMap`. For example, a player in the
exact center of the in-game location will be drawn in the center of the
drawn map area.

To do that:

1.  <a href="Options#Screenshot" class="wikilink"
    title="Take a screenshot">Take a screenshot</a> of the full in-game
    location.
2.  Open the screenshot in an image editor like
    [Paint.NET](https://www.getpaint.net/) or
    [GIMP](https://www.gimp.org/).
3.  Crop as needed, then rescale it to the size you want on the world
    map. Make sure you use 'nearest neighbor' as the scale algorithm.
4.  Redraw parts if needed to clean it up.

That's it! If you use that as the map area's texture in `Data/WorldMap`,
the game will be able to determine positions automatically. You can omit
the `WorldPositions` field with this approach.

### Manual positioning

If the in-game layout doesn't match the drawn world map, you can use the
`WorldPositions` field in `Data/WorldMap` to manually align positions
between them. **This can be tricky; usually
<a href="#Automatic_positioning_(recommended)" class="wikilink"
title="automatic positioning">automatic positioning</a> is recommended
instead.**

For example, the mountain's map area was very stylized before Stardew
Valley 1.6 (the mine and adventure guild were right next to each other,
there were no islands, there was no water south of the guild, etc):
<a href="File_Modding_-_manual_world_map_positioning_1.png"
class="wikilink" title="thumb">thumb</a>'s in-game location (top) and
world map area (bottom).\]\]

With manual positioning, you add any number of *world positions* with a
`TileArea` (the
<a href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
title="tile coordinates">tile coordinates</a> where the player is
standing in the actual location) and `MapPixelArea` (where that area is
on the map). When the player is within the `TileArea`, they'll be mapped
to the relative position within the matching `MapPixelArea`. For
example, if they're in the exact center of the `TileArea`, they'll be
drawn in the center of the `MapPixelArea`.

For example, you could divide the pre-1.6 mountain into multiple areas
like this (see the
<a href="#Format" class="wikilink" title="data format">data format</a>
for info on each field):

``` json
"WorldPositions": [
    {
        "Id": "Quarry",
        "LocationName": "Mountain",
        "TileArea": { "X": 95, "Y": 11, "Width": 36, "Height": 24 },
        "ExtendedTileArea": { "X": 95, "Y": 0, "Width": 255, "Height": 255 },
        "MapPixelArea": { "X": 236, "Y": 29, "Width": 28, "Height": 19 }
    },
    {
        "Id": "Lake_Guild",
        "LocationName": "Mountain",
        "TileArea": { "X": 73, "Y": 5, "Width": 22, "Height": 30 },
        "ExtendedTileArea": { "X": 73, "Y": 0, "Width": 22, "Height": 255 },
        "MapPixelArea": { "X": 227, "Y": 29, "Width": 9, "Height": 19 }
    },
    {
        "Id": "Lake_BetweenGuildAndMine",
        "LocationName": "Mountain",
        "TileArea": { "X": 57, "Y": 5, "Width": 16, "Height": 32 },
        "ExtendedTileArea": { "X": 57, "Y": 0, "Width": 16, "Height": 255 },
        "MapPixelArea": { "X": 224, "Y": 29, "Width": 3, "Height": 19 }
    },
    {
        "Id": "Lake_Mine",
        "LocationName": "Mountain",
        "TileArea": { "X": 52, "Y": 5, "Width": 5, "Height": 30 },
        "ExtendedTileArea": { "X": 52, "Y": 0, "Width": 5, "Height": 255 },
        "MapPixelArea": { "X": 220, "Y": 29, "Width": 4, "Height": 19 }
    },
    {
        "Id": "Lake_MineBridge",
        "LocationName": "Mountain",
        "TileArea": { "X": 44, "Y": 5, "Width": 8, "Height": 30 },
        "ExtendedTileArea": { "X": 44, "Y": 0, "Width": 8, "Height": 255 },
        "MapPixelArea": { "X": 210, "Y": 29, "Width": 10, "Height": 19 }
    },
    {
        "Id": "West",
        "LocationName": "Mountain",
        "TileArea": { "X": 0, "Y": 5, "Width": 44, "Height": 30 },
        "ExtendedTileArea": { "X": 0, "Y": 0, "Width": 44, "Height": 255 },
        "MapPixelArea": { "X": 175, "Y": 29, "Width": 35, "Height": 19 }
    },
    {
        "Id": "Default",
        "LocationName": "Mountain"
    }
]
```

Here's a visual representation of those areas:
<a href="File_Modding_-_manual_world_map_positioning_2.png"
class="wikilink" title="thumb">thumb</a>'s in-game location with
highlighted `TileArea` positions (top) and world map with highlighted
`MapPixelArea` positions (bottom).\]\]

Note how the area between the mine and adventurer's guild is wide in the
location, but narrow on the drawn world map. When the player is walking
across that part of the location, they'll be shown walking slowly across
the equivalent location on the drawn map.

If the player is outside a `TileArea` but within the `ExtendedTileArea`
(if set), their position is snapped to the nearest position within the
`TileArea`. For example, notice how the bottom of the location south of
the carpenter shop isn't part of the red area. It *is* part of that
area's `ExtendedTileArea` though, so a player there will be snapped to
the bottom of the red area on the world map.

### Fixed positions

For very complex locations, real-time positions on the world map may not
be possible (e.g. because the drawn world map is very stylized). In that
case you can set a fixed position (or multiple fixed positions) on the
world map.

For example, this draws the player marker at one of five world map
positions depending where they are in town. The `TileArea` indicates the
<a href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
title="tile coordinates">tile coordinates</a> where the player is
standing in the actual town, and `MapPixelArea` is where to draw them on
the map. Note that the latter is always 1x1 pixel in the code below,
which means that anywhere within the `TileArea` will be placed on that
specific pixel on the world map. The last entry has no `TileArea`, which
means it applies to all positions that didn't match a previous entry.

``` json
"WorldPositions": [
    {
        "Id": "East_NearJojaMart",
        "LocationName": "Town",
        "TileArea": { "X": 85, "Y": 0, "Width": 255, "Height": 68 },
        "MapPixelArea": { "X": 225, "Y": 81, "Width": 1, "Height": 1 }
    },
    {
        "Id": "East_NearMuseum",
        "LocationName": "Town",
        "TileArea": { "X": 81, "Y": 68, "Width": 255, "Height": 255 },
        "MapPixelArea": { "X": 220, "Y": 108, "Width": 1, "Height": 1 }
    },
    {
        "Id": "West_North",
        "LocationName": "Town",
        "TileArea": { "X": 0, "Y": 0, "Width": 85, "Height": 43 },
        "MapPixelArea": { "X": 178, "Y": 64, "Width": 1, "Height": 1 }
    },
    {
        "Id": "West_Center",
        "LocationName": "Town",
        "TileArea": { "X": 0, "Y": 43, "Width": 85, "Height": 33 },
        "MapPixelArea": { "X": 175, "Y": 88, "Width": 1, "Height": 1 }
    },
    {
        "Id": "West_South",
        "LocationName": "Town",
        "MapPixelArea": { "X": 182, "Y": 109, "Width": 0, "Height": 0 }
    }
]
```

## Interacting with the world map in C#

SMAPI mods (written in C#) can use the game's
`StardewValley.WorldMaps.WorldMapManager` class to interact with the
world map.

For example, you can get the pixel position on the world map which
matches an in-game tile coordinate (if the location appears in
`Data/WorldMap`):

``` c#
MapAreaPosition mapAreaPosition = WorldMapManager.GetPositionData(location, tile);
if (mapAreaPosition != null)
    return mapAreaPosition.GetMapPixelPosition(location, tile);
```

## Debug view

You can run `debug worldMapLines` in the SMAPI console window to enable
the world map's debug view. This will outline map areas (black), map
area positions (blue), and tooltips (green):

<a href="File_Modding_-_world_map_debug_mode.png" class="wikilink"
title="thumb">thumb</a>

You can optionally specify which types to highlight, like
`debug worldMapLines areas positions tooltips`.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Карта_мира" class="wikilink"
title="ru:Модификации:Карта мира">ru:Модификации:Карта мира</a>
<a href="zh_模组_世界地图" class="wikilink"
title="zh:模组:世界地图">zh:模组:世界地图</a>
