---
title: "Giant Crops"
wiki_source: "Modding:Giant crops"
permalink: /Modding:Giant_crops/
category: items
tags: [giant-crops, data-format, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page describes how the game stores and parses
<a href="Crops#Giant_Crops" class="wikilink" title="Giant Crop">Giant
Crop</a> data. This is an advanced guide for mod developers.

## Data format

You can now add/edit
<a href="Crops#Giant_Crops" class="wikilink" title="giant crops">giant
crops</a> by editing the `Data/GiantCrops` data asset.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  giant crop.
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
<td><p><samp>FromItemId</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="item ID">item ID</a> (qualified or unqualified)
for the harvest ID of the regular crop which can turn into this giant
crop. For example, <samp>(O)254</samp> is <a href="melon"
class="wikilink" title="melon">melon</a>.</p>
<p>Any number of giant crops can use the same <samp>FromItemId</samp>
value. The first giant crop whose other fields match (if any) will
spawn.</p></td>
</tr>
<tr>
<td><p><samp>HarvestItems</samp></p></td>
<td><p>The items which can be dropped when you break the giant crop. If
multiple items match, they'll all be dropped.</p>
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
generic item fields supported for harvest items.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that this entry is selected,
as a value between 0 (never drops) and 1 (always drops). Default 1 (100%
chance).</p></td>
</tr>
<tr>
<td><p><samp>ForShavingEnchantment</samp></p></td>
<td><p><em>(Optional)</em> Whether this item is only dropped for <a
href="Enchantments#Tool_enchantments" class="wikilink"
title="Shaving enchantment">Shaving enchantment</a> drops
(<samp>true</samp>), only when the giant crop is broken
(<samp>false</samp>), or both (<samp>null</samp>). Default
both.</p></td>
</tr>
<tr>
<td><p><samp>ScaledMinStackWhenShaving</samp><br />
<samp>ScaledMaxStackWhenShaving</samp></p></td>
<td><p><em>(Optional)</em> If set, the min/max stack size when this item
is dropped due to the <a href="Forge#Enchantments" class="wikilink"
title="shaving enchantment">shaving enchantment</a>, scaled to the
tool's power level.</p>
<p>This value is multiplied by the health deducted by the tool hit which
triggered the enchantment. For example, an iridium axe which reduced the
giant crop's health by 3 points will produce three times this value per
hit.</p>
<p>If both fields are set, the stack size is randomized between them. If
only one is set, it's applied as a limit after the generic fields. If
neither is set, the generic <samp>MinStack</samp>/<samp>MaxStack</samp>
fields are applied as usual without scaling.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture containing the giant crop's
sprite.</p></td>
</tr>
<tr>
<td><p><samp>TexturePosition</samp></p></td>
<td><p><em>(Optional)</em> The top-left pixel position of the sprite
within the <samp>Texture</samp>, specified as a model with
<samp>X</samp> and <samp>Y</samp> fields. Defaults to (0, 0).</p></td>
</tr>
<tr>
<td><p><samp>TileSize</samp></p></td>
<td><p><em>(Optional)</em> The area in tiles occupied by the giant crop,
specified as a model with <samp>X</samp> and <samp>Y</samp> fields. This
affects both its sprite size (which should be 16 pixels per tile) and
the grid of crops needed for it to grow. Note that giant crops are drawn
with an extra tile's height. Defaults to (3, 3).</p></td>
</tr>
<tr>
<td><p><samp>Health</samp></p></td>
<td><p><em>(Optional)</em> The health points that must be depleted to
break the giant crop. The number of points depleted per <a href="axe"
class="wikilink" title="axe">axe</a> chop depends on the axe power
level. Default 3.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The percentage chance that a given grid of
crops will grow into the giant crop each night, as a value between 0
(never) and 1 (always). Default 0.01 (1%).</p>
<p>Note that the chance is checked for each giant crop that applies. If
three giant crops each have a 1% chance of spawning for the same crop,
then there's a 3% chance that one of them will spawn.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this giant crop is available to spawn. Defaults to
always true.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

## See also

- <a href="Modding_Crop_data" class="wikilink"
  title="Modding:Crop data">Modding:Crop data</a> for information about
  regular crops.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Гигантские_культуры" class="wikilink"
title="ru:Модификации:Гигантские культуры">ru:Модификации:Гигантские
культуры</a>
