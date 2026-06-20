---
title: "Big Craftables"
wiki_source: "Modding:Big craftables"
permalink: /Modding:Big_craftables/
category: items
tags: [big-craftables, overview, data-format, basic-info, behavior, appearance, context-tags, advanced]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses 'big craftable'-type
item data. For items in general, see
<a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

Big craftables are items which can be placed in the world and are two
tiles tall (instead of one like
<a href="Modding_Objects" class="wikilink" title="objects">objects</a>).
Unlike objects, they can't be eaten or sold to most shops.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(BC)` (or
`ItemRegistry.type_bigCraftable` in C# code), their data in
`Data/BigCraftables`, their in-game sprites in `TileSheets/Craftables`
by default, and their code in `StardewValley.Object` (based on the
`bigCraftable` field).

## Data format

The big craftable data in `Data/BigCraftables` consists of a string →
model lookup, where...

- The key is the unqualified
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="item ID">item ID</a>.
- The value is a model with the fields listed below.

### Basic info

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p>The internal item name.</p></td>
</tr>
<tr>
<td><p><samp>DisplayName</samp><br />
<samp>Description</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the item's in-game
display name and description.</p></td>
</tr>
<tr>
<td><p><samp>Price</samp></p></td>
<td><p><em>(Optional)</em> The price when sold by the player. This is
not the price when bought from a shop. Default 0.</p></td>
</tr>
</tbody>
</table>

### Behavior

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Fragility</samp></p></td>
<td><p><em>(Optional)</em> How the item can be picked up. The possible
values are 0 (pick up with any tool), 1 (destroyed if hit with an
axe/hoe/pickaxe, or picked up with any other tool), or 2 (can't be
removed once placed). Default 0.</p></td>
</tr>
<tr>
<td><p><samp>CanBePlacedIndoors</samp><br />
<samp>CanBePlacedOutdoors</samp></p></td>
<td><p><em>(Optional)</em> Whether the item can be placed indoors or
outdoors. Default true.</p></td>
</tr>
<tr>
<td><p><samp>IsLamp</samp></p></td>
<td><p><em>(Optional)</em> Whether this is a lamp and should produce
light when dark. Default false.</p></td>
</tr>
</tbody>
</table>

### Appearance

| field | purpose |
|----|----|
| `Texture` | *(Optional)* The asset name for the texture containing the item's sprite. Defaults to `TileSheets/Craftables`. |
| `SpriteIndex` | *(Optional)* The sprite's index within the `Texture`, where 0 is the top-left sprite. |

### Context tags

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ContextTags</samp></p></td>
<td><p><em>(Optional)</em> The custom <a href="Modding_Context_tags"
class="wikilink" title="context tags">context tags</a> to add for this
item (in addition to the tags added automatically based on the other
object data). This is formatted as a list; for example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ContextTags&quot;</span><span class="er">:</span> <span class="ot">[</span> <span class="st">&quot;light_source&quot;</span><span class="ot">,</span> <span class="st">&quot;torch_item&quot;</span> <span class="ot">]</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

### Advanced

| field | purpose |
|----|----|
| `CustomFields` | *(Optional)* The <a href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry. |

## Unobtainable items

The data asset has items that can't normally be picked up or may be
unimplemented in-game. They may be completely absent from the game, or
they may be unused as craftables and instead appear in
<a href="Modding_Objects" class="wikilink" title="object data">object
data</a> or <a href="Modding_Furniture" class="wikilink"
title="furniture data">furniture data</a>.

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Изготовляемые_предметы" class="wikilink"
title="ru:Модификации:Изготовляемые предметы">ru:Модификации:Изготовляемые
предметы</a> <a href="zh_模组_大型打造品" class="wikilink"
title="zh:模组:大型打造品">zh:模组:大型打造品</a>
