---
title: "Furniture"
wiki_source: "Modding:Furniture"
permalink: /Modding:Furniture/
category: items
tags: [furniture, overview, data-format, furniture-types, see-also]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses furniture-type item
data. For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

Furniture are decorative items which can be placed in the world. In some
cases, players can sit on them or place items on them.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(F)` (or `ItemRegistry.type_furniture`
in C# code), their data in `Data/Furniture`, their sprites in
`TileSheets/furniture` by default, their vanilla translations in
`Strings/Furniture`, and their code in
`StardewValley.Objects.Furniture`.

## Data format

The furniture data in `Data/Furniture` consists of an string → string
lookup, where...

- The key is the
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="unqualified item ID">unqualified item ID</a>.
- The value is a slash-delimited strings with the fields listed below.

<table>
<thead>
<tr>
<th><p>index</p></th>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0</p></td>
<td><p>name</p></td>
<td><p>The internal item name.</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>type</p></td>
<td><p>The furniture type. See <a href="#Furniture_types"
class="wikilink" title="table of possible values">table of possible
values</a>.</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>tilesheet size</p></td>
<td><p>The furniture sprite size on the tilesheet, measured in tiles.
This can be <samp>&lt;width&gt; &lt;height&gt;</samp> (e.g. <samp>1
2</samp>), or <samp>-1</samp> to use the default size for the
type.</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>bounding box size</p></td>
<td><p>The size of the hitbox when the furniture is placed in-game,
measured in tiles. The bounding box will be anchored to the bottom-left
corner and extend upwards and rightwards. This can be
<samp>&lt;width&gt; &lt;height&gt;</samp> (e.g. <samp>1 2</samp>), or
<samp>-1</samp> to use the default size for the type.</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>rotations</p></td>
<td><p>The number of rotations possible (1, 2, or 4).</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>price</p></td>
<td><p>The price when purchased from a shop.</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>placement restriction</p></td>
<td><p>Where the furniture can be placed.</p>
<p>Possible values:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-1</p></td>
<td><p>default (uses furniture type)</p></td>
</tr>
<tr>
<td><p>0</p></td>
<td><p>indoors-only</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>outdoors-only</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>indoors or outdoors</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p>display name</p></td>
<td><p>The translated furniture name, which allows <a
href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable strings">tokenizable strings</a>.</p></td>
</tr>
<tr>
<td><p>8</p></td>
<td><p>sprite index</p></td>
<td><p>The sprite index within the spritesheet texture to draw.</p></td>
</tr>
<tr>
<td><p>9</p></td>
<td><p>texture</p></td>
<td><p><em>(Optional)</em> The asset name of the texture to draw.
Defaults to <samp>TileSheets/furniture</samp>.</p></td>
</tr>
<tr>
<td><p>10</p></td>
<td><p>off limits for random sale</p></td>
<td><p><em>(Optional)</em> Whether to prevent this furniture from
appearing in randomly generated shop stocks and the furniture catalogue.
Default false.</p></td>
</tr>
<tr>
<td><p>11</p></td>
<td><p>context tags</p></td>
<td><p><em>(Optional)</em> A space-delimited list of <a
href="Modding_Context_tags" class="wikilink"
title="context tags">context tags</a> which apply to this furniture.
Default none.</p></td>
</tr>
</tbody>
</table>

## Furniture types

The 'type' field can be set to one of these values. (The '1.7' column
shows the equivalent values in the
<a href="Modding_Migrate_to_Stardew_Valley_1.7" class="wikilink"
title="upcoming Stardew Valley 1.7">upcoming Stardew Valley 1.7</a>.)

<table>
<thead>
<tr>
<th><p>type (current)</p></th>
<th><p>type (1.7)</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>chairs</p></td>
</tr>
<tr>
<td><p><samp>armchair</samp></p></td>
<td><p><samp>Armchair</samp></p></td>
<td><p>An armchair which lets one player sit on it.</p></td>
</tr>
<tr>
<td><p><samp>bench</samp></p></td>
<td><p><samp>Bench</samp></p></td>
<td><p>A bench which lets two players sit on it if it's wide
enough.</p></td>
</tr>
<tr>
<td><p><samp>chair</samp></p></td>
<td><p><samp>Chair</samp></p></td>
<td><p>A chair which lets one player sit on it.</p></td>
</tr>
<tr>
<td><p><samp>couch</samp></p></td>
<td><p><samp>Couch</samp></p></td>
<td><p>A couch which lets an arbitrary number of players sit on it
depending on its tile width.</p></td>
</tr>
<tr>
<td colspan="3"><p>tables</p></td>
</tr>
<tr>
<td><p><samp>long table</samp></p></td>
<td><p><samp>LongTable</samp></p></td>
<td><p>A long table which allows placing an item on it.</p></td>
</tr>
<tr>
<td><p><samp>table</samp></p></td>
<td><p><samp>Table</samp></p></td>
<td><p>A table which allows placing an item on it.</p></td>
</tr>
<tr>
<td colspan="3"><p>lighting</p></td>
</tr>
<tr>
<td><p><samp>fireplace</samp></p></td>
<td><p><samp>Fireplace</samp></p></td>
<td><p>A fireplace which can be lit.</p></td>
</tr>
<tr>
<td><p><samp>lamp</samp></p></td>
<td><p><samp>Lamp</samp></p></td>
<td><p>A lamp which can be lit.</p></td>
</tr>
<tr>
<td><p><samp>sconce</samp></p></td>
<td><p><samp>Sconce</samp></p></td>
<td><p>A sconce light which can be lit.</p></td>
</tr>
<tr>
<td><p><samp>torch</samp></p></td>
<td><p><samp>Torch</samp></p></td>
<td><p>A torch which can be lit.</p></td>
</tr>
<tr>
<td><p><samp>window</samp></p></td>
<td><p><samp>Window</samp></p></td>
<td><p>A window which can be placed on a wall and lets through light
from outside.</p></td>
</tr>
<tr>
<td colspan="3"><p>other interactions</p></td>
</tr>
<tr>
<td><p><samp>bed</samp><br />
<samp>bed child</samp><br />
<samp>bed double</samp></p></td>
<td><p><samp>Bed</samp></p></td>
<td><p>A bed which players can sleep in.</p></td>
</tr>
<tr>
<td><p><samp>dresser</samp></p></td>
<td><p><samp>Dresser</samp></p></td>
<td><p>A dresser which allows storing clothes within it.</p></td>
</tr>
<tr>
<td><p><samp>fishtank</samp></p></td>
<td><p><samp>FishTank</samp></p></td>
<td><p>A fish tank which can display fish placed inside it.</p></td>
</tr>
<tr>
<td></td>
<td><p><samp>Television</samp></p></td>
<td></td>
</tr>
<tr>
<td colspan="3"><p>decorative</p></td>
</tr>
<tr>
<td><p><samp>bookcase</samp></p></td>
<td><p><samp>Bookcase</samp></p></td>
<td><p>A decorative bookcase which has no special behavior.</p></td>
</tr>
<tr>
<td><p><samp>decor</samp></p></td>
<td><p><samp>Decor</samp></p></td>
<td><p>A general decor item which has no special behavior.</p></td>
</tr>
<tr>
<td><p><samp>painting</samp></p></td>
<td><p><samp>Painting</samp></p></td>
<td><p>A painting which can be hung on a wall.</p></td>
</tr>
<tr>
<td><p><samp>randomized_plant</samp></p></td>
<td><p><samp>RandomizedPlant</samp></p></td>
<td><p>A plant whose appearance is dynamic by randomizing each of its
three vertical tiles (usually a pot, stem, and head).</p></td>
</tr>
<tr>
<td><p><samp>rug</samp></p></td>
<td><p><samp>Rug</samp></p></td>
<td><p>A rug which can be placed on the ground and under furniture, and
which lets players and NPCs walk over it.</p></td>
</tr>
<tr>
<td><p><samp>other</samp></p></td>
<td><p><samp>Other</samp></p></td>
<td><p>A miscellaneous furniture which has no special behavior.</p></td>
</tr>
</tbody>
</table>

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Мебель" class="wikilink"
title="ru:Модификации:Мебель">ru:Модификации:Мебель</a>
<a href="zh_模组_家具" class="wikilink"
title="zh:模组:家具">zh:模组:家具</a>
