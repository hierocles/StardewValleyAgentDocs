---
title: "Advanced Edits"
wiki_source: "Modding:Maps"
permalink: /Modding:Maps/
category: locations
tags: [maps, advanced-edits, sitting-on-non-furniture-chairs, custom-wallpaper-and-flooring-in-decoratable-locations]
---
## Advanced edits

### Sitting on non-furniture chairs

Players can sit on chairs that are part of the map. This works by
checking the tile on the `Buildings` layer, and comparing its tilesheet
and tile index to the data in `Data/ChairTiles`.

Each entry has a key in the form `tilesheet/tile X/tile Y`:

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>tilesheet</p></td>
<td><p>The tilesheet's <a
href="Modding_Common_data_field_types#Asset_name" class="wikilink"
title="asset name">asset name</a> (<em>not</em> the tilesheet ID)
without the path and file extension. For example:</p>
<ul>
<li>For a local tilesheet loaded automatically from
<code>assets/some-tilesheet.png</code>, this would be
<code>some-tilesheet</code>.</li>
<li>For a tilesheet accessed through the content folder from
<code>Maps/SomeModId/SomeTilesheet</code>, this would be
<code>SomeTilesheet</code>.</li>
</ul>
<p>This value should be unique to your mod to avoid conflicting with
other mods which add tilesheets or edit
<samp>Data/ChairTiles</samp>.</p>
<p><strong>Bug:</strong> the last period in the asset name is always
treated as a file extension. For example, the asset name
<code>YourName.YourMod_sampleTilesheet.png</code> will have the key
<code>YourName</code> in <samp>Data/ChairTiles</samp>.</p></td>
</tr>
<tr>
<td><p>tile X<br />
tile Y</p></td>
<td><p>The tile's X and Y position in the map tilesheet, starting at
zero.</p></td>
</tr>
</tbody>
</table>

And a value in the form
`width in tiles/height in tiles/direction/type/draw tile X/draw tile Y/is seasonal/alternate tilesheet`:

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>width in tiles<br />
height in tiles</p></td>
<td><p>The size of the seat in tiles. For example, a width of 2 lets the
player sit on the next tile to the right of it too.</p></td>
</tr>
<tr>
<td><p>direction</p></td>
<td><p>The direction the player should face when sitting. The possible
values are <samp>down</samp>, <samp>left</samp>, <samp>right</samp>,
<samp>up</samp>, or <samp>opposite</samp>. Any other value defaults to
<samp>up</samp>.</p></td>
</tr>
<tr>
<td><p>type</p></td>
<td><p>Either:</p>
<ul>
<li>An arbitrary seat code (like <samp>playground</samp> or
<samp>ccdesk</samp>), which affects hardcoded game logic for specific
seats in the game. You can specify an invalid value like
<samp>default</samp> to ignore this. The seat code
<samp>highback_chair</samp> is needed to draw a chair overlay one tile
taller than the height of the chair. Set the draw tile (below) to the
bottom-left tile when using. This is useful for chairs with a back (i.e
shaped like the <a href="Oak_Chair" class="wikilink"
title="Oak Chair">Oak Chair</a>).</li>
<li><em>Or</em> you can write <samp>custom &lt;offset_x&gt;
&lt;offset_y&gt; &lt;extra_height&gt;</samp> to override the hardcoded
offset and height values. The three values are measured in tiles
(<em>e.g.,</em> an X offset value of 0.5 would shift the sitting
location by half a tile).</li>
</ul></td>
</tr>
<tr>
<td><p>draw tile X<br />
draw tile Y</p></td>
<td><p>The X and Y position in <samp>TileSheets/ChairTiles</samp> (or
the custom tilesheet) to draw when the player is sitting, starting at 0.
If the width and/or height are more than 1, this is the position of the
top-left tile.</p></td>
</tr>
<tr>
<td><p>is seasonal</p></td>
<td><p>Whether to draw seasonal variants when sitting. If enabled, the
&lt;draw tile X&gt; and &lt;draw tile Y&gt; are offset by one width for
each season. In other words, the spring/summer/fall/winter sprites
should appear in the draw tilesheet directly adjacent, moving rightward
in that order.</p></td>
</tr>
<tr>
<td><p>alternate tilesheet</p></td>
<td><p><em>(Optional)</em> The asset name for the tilesheet from which
to get the draw tiles, using <samp>\\</samp> (two backslashes) as the
path separator. The default value is
<samp>TileSheets\\ChairTiles</samp>.</p></td>
</tr>
</tbody>
</table>

### Custom Wallpaper and Flooring in Decoratable Locations

You can enable Wallpaper, Flooring, and wall furniture (windows,
paintings) in decoratable locations like farmhouses, cabins, or sheds by
adding these map and tile properties. The location must have or be
subclass of `StardewValley.Locations.DecoratableLocation`.

First, you can define distinct areas using two new map properties:

<table>
<thead>
<tr>
<th><p>valid in</p></th>
<th><p>map property</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><em>decoratable locations</em></p></td>
<td><p><samp>FloorIDs [area]+</samp><br />
<samp>WallIDs [area]+</samp><br />
</p></td>
<td><p>A comma-separated list of the distinct areas which have flooring
or walls. The <samp>FloorIDs</samp> and <samp>WallIDs</samp> don't need
to match. Each area has the form
<code>&lt;area ID&gt; [default flooring/wallpaper ID]</code>, where:</p>
<ul>
<li><samp>&lt;area ID&gt;</samp> uniquely identifies the area or
room.</li>
<li><samp>[default flooring/wallpaper ID]</samp> (optional) sets the
initial flooring/wallpaper ID if that area hasn't been customized by the
player yet. This can be defined in three forms:
<ul>
<li><code>&lt;index&gt;</code>: get the floor/wallpaper matching that
index in the vanilla <samp>Maps/walls_and_floors</samp> tilesheet.</li>
<li><code>&lt;tilesheet&gt;:&lt;index&gt;</code>: add
<samp>Maps/&lt;tilesheet&gt;</samp> to the map, and match the index in
that tilesheet.</li>
<li><code>&lt;area ID&gt;</code>: inherit the default floor/wallpaper
from the named area. For example, <samp>Hallway_Bedroom Bedroom</samp>
applies the bedroom wallpaper to the hallway between the bedroom and
living room when the farmhouse is first upgraded.</li>
<li>If omitted, the default will be flooring/wallpaper #0.</li>
</ul></li>
</ul>
<p>For example:</p>
<pre><code>FloorIDs: Kitchen 22, LivingRoom Bedroom, Hallway_Bedroom Bedroom, Bedroom
WallIDs: LivingRoom, Hallway_Bedroom Bedroom, Bedroom</code></pre>
<p>You don't need to add every area to the
<samp>FloorIDs</samp>/<samp>WallIDs</samp> list; assigning a
flooring/wall to an unlisted value will be handled correctly. You only
really need to add an area to <samp>FloorIDs</samp>/<samp>WallIDs</samp>
to set the default flooring/wallpaper value, or for cases where the
order of the walls/floors is important (for backwards compatibility with
code that sets wallpaper/flooring by an integer room index, as is the
case with the floors/walls in the vanilla farmhouse).</p></td>
</tr>
</tbody>
</table>

Then you can add individual tiles to each area with two new tile
properties:

<table>
<thead>
<tr>
<th><p>layer</p></th>
<th><p>property</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>WallID &lt;area ID&gt;</samp><br />
<samp>FloorID &lt;area ID&gt;</samp></p></td>
<td><p>Adds this tile to the given floor/wall area. Each floor tile
should have the <samp>FloorID</samp> property, but only the top edge of
the wall should have <samp>WallID</samp>.</p></td>
</tr>
</tbody>
</table>
