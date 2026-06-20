---
title: "Floors And Paths"
wiki_source: "Modding:Floors and Paths"
permalink: /Modding:Floors_and_Paths/
category: game
tags: [floors-and-paths, data-format]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page covers the data format for
<a href="Crafting#Decor" class="wikilink"
title="craftable floors &amp; paths">craftable floors &amp; paths</a>.
This is an advanced guide for mod developers

## Data Format

You can add or customize <a href="Crafting#Decor" class="wikilink"
title="craftable floors &amp; paths">craftable floors &amp; paths</a> by
editing the `Data/FloorsAndPaths` asset.

This consists of a string → model lookup, where the key matches the `ID`
field and the value is a model with these fields:

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
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
floor/path.</p></td>
</tr>
<tr>
<td><p><samp>ItemId</samp></p></td>
<td><p>The unqualified <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="item ID">item ID</a> for the corresponding
object-type item.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture (under the game's
<samp>Content</samp> folder) when the flooring is applied or the path is
placed. Use <samp>\</samp> (or <samp>\\</samp> in JSON) to separate name
segments if needed. For example, the vanilla tilesheet is
<samp>TerrainFeatures\Flooring</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Corner</samp></p></td>
<td><p>The top-left pixel position for the sprite within the
<samp>Texture</samp> spritesheet, specified as a model with
<samp>X</samp> and <samp>Y</samp> fields.</p></td>
</tr>
<tr>
<td><p><samp>PlacementSound</samp></p></td>
<td><p>The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> played when the item is
applied/placed (e.g. <samp>axchop</samp> used by <a href="Wood_Floor"
class="wikilink" title="Wood Floor">Wood Floor</a>).</p></td>
</tr>
<tr>
<td><p><samp>FootstepSound</samp></p></td>
<td><p>The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> played when the player steps on
the tile (e.g. <samp>woodyStep</samp> used by <a href="Wood_Floor"
class="wikilink" title="Wood Floor">Wood Floor</a>).</p></td>
</tr>
<tr>
<td><p><samp>WinterTexture</samp><br />
<samp>Corner</samp></p></td>
<td><p><em>(Optional)</em> Equivalent to <samp>Texture</samp> and
<samp>Corner</samp>, but applied if the current location is in
winter.</p></td>
</tr>
<tr>
<td><p><samp>RemovalSound</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> played when the item is unapplied
or picked up. Defaults to the same sound as
<samp>PlacementSound</samp>.</p></td>
</tr>
<tr>
<td><p><samp>RemovalDebrisType</samp></p></td>
<td><p><em>(Optional)</em> The type of cosmetic debris particles to
'splash' from the tile when the item is unapplied or picked up. The
defined values are 0 (copper), 2 (iron), 4 (coal), 6 (gold), 8 (coins),
10 (iridium), 12 (wood), 14 (stone), 32 (big stone), and 34 (big wood).
Default 14 (stone).</p></td>
</tr>
<tr>
<td><p><samp>ShadowType</samp></p></td>
<td><p><em>(Optional)</em> The type of shadow to draw under the tile
sprite. Default <samp>None</samp>.</p>
<p>The possible values are:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>None</samp></p></td>
<td><p>Don't draw a shadow.</p></td>
</tr>
<tr>
<td><p><samp>Square</samp></p></td>
<td><p>Draw a shadow under the entire tile.</p></td>
</tr>
<tr>
<td><p><samp>Contoured</samp></p></td>
<td><p>raw a shadow that follows the lines of the path sprite.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>ConnectType</samp></p></td>
<td><p><em>(Optional)</em> When drawing the flooring across multiple
tiles, how the flooring sprite for each tile is selected. Defaults to
<samp>Default</samp>.</p>
<p>The possible values are:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Default</samp></p></td>
<td><p>For normal floors, intended to cover large square areas. This
uses some logic to draw inner corners.</p></td>
</tr>
<tr>
<td><p><samp>Path</samp></p></td>
<td><p>For floors intended to be drawn as narrow paths. These are drawn
without any consideration for inner corners.</p></td>
</tr>
<tr>
<td><p><samp>CornerDecorated</samp></p></td>
<td><p>For floors that have a decorative corner. Use
<samp>CornerSize</samp> to change the size of this corner.</p></td>
</tr>
<tr>
<td><p><samp>Random</samp></p></td>
<td><p>For floors that don't connect. When placed, one of the tiles is
randomly selected.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>CornerSize</samp></p></td>
<td><p><em>(Optional)</em> The pixel size of the decorative border when
the <samp>ConnectType</samp> field is set to
<samp>CornerDecorated</samp> or <samp>Default</samp>.</p></td>
</tr>
<tr>
<td><p><samp>FarmSpeedBuff</samp></p></td>
<td><p><em>(Optional)</em> The speed boost applied to the player, on the
<a href="farm" class="wikilink" title="farm">farm</a> only, when they're
walking on paths of this type. Negative values are ignored. Default
0.1.</p></td>
</tr>
</tbody>
</table>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Полы_и_дорожки" class="wikilink"
title="ru:Модификации:Полы и дорожки">ru:Модификации:Полы и дорожки</a>
<a href="zh_模组_地板和小径" class="wikilink"
title="zh:模组:地板和小径">zh:模组:地板和小径</a>
