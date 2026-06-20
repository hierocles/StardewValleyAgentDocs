---
title: "Hats"
wiki_source: "Modding:Hats"
permalink: /Modding:Hats/
category: items
tags: [hats, overview, data-format, see-also]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses hat-type item data.
For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

Hats are items that can be equipped in the player's
<a href="hats" class="wikilink" title="hat">hat</a> slot. These change
the player sprite.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(H)` (or `ItemRegistry.type_hat` in C#
code), their data in `Data/Hats`, their in-game sprites in
`Characters/Farmer/hats` by default, and their code in
`StardewValley.Objects.Hat`.

## Data format

The hat data in `Data/Hats` consists of a string → string lookup,
where...

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
<td><p>description</p></td>
<td><p>The translated item description shown in-game.</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>show real hair</p></td>
<td><p>Whether to show the player's hairstyle as-is when the hat is worn
(<samp>true</samp>), change the hairstyle to fit the hat
(<samp>false</samp>), or hide their hair completely
(<samp>hide</samp>).</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>skip hairstyle offset</p></td>
<td><p>Whether to ignore the current style when positioning the hat (one
of <samp>true</samp> or <samp>false</samp>). For example, the <a
href="Eye_Patch" class="wikilink" title="eye patch">eye patch</a> sets
<samp>true</samp> since its position isn't affected by the hair, but the
<a href="Butterfly_Bow" class="wikilink" title="butterfly bow">butterfly
bow</a> sets <samp>false</samp> to adjust its position on top of your
hair.</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>tags</p></td>
<td><p>A space-separated list of "tags". These are separate from context
tags, and used to contain miscellaneous information. Currently, the only
tag used by the game is <samp>Prismatic</samp>, which marks a hat as
prismatic and causes it to cycle through colors.</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>display name</p></td>
<td><p>The translated item name shown in-game.</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>sprite index</p></td>
<td><p>The index in the hat spritesheet used to display this hat (see
field 7 for the texture layout).</p></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p>texture name</p></td>
<td><p>The name of the game texture to use for the hat. If empty, the
game will use the default hat sheet
<samp>Characters/Farmer/hats</samp>.</p>
<p>Each hat in the texture should have a 20x80 pixel area, consisting of
four 20x20 hat sprites from top to bottom: facing down, right, left, and
up. The texture can have any width and height that's evenly divisible by
20 and 80 respectively.</p></td>
</tr>
</tbody>
</table>

Hats have a hardcoded category of -95 (see `HatDataDefinition.GetData`
in the game code).

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="zh_模组_帽子" class="wikilink"
title="zh:模组:帽子">zh:模组:帽子</a>
