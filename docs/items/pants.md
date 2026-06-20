---
title: "Pants"
wiki_source: "Modding:Pants"
permalink: /Modding:Pants/
category: items
tags: [pants, overview, data-format, basic-data, appearance, other, see-also]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses pants-type item data.
For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

Pants are items that can be equipped in the player's
<a href="Tailoring#Pants" class="wikilink" title="pants">pants</a> slot.
These change the player sprite.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(P)` (or `ItemRegistry.type_pants` in
C# code), their data in `Data/Pants`, their icon sprites in
`Characters/Farmer/pants` by default, and their code in
`StardewValley.Objects.Clothing`.

## Data format

The pants data in `Data/Pants` consists of a string → model lookup,
where...

- The key is the
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="unqualified item ID">unqualified item ID</a>.
- The value is a model with the fields listed below.

### Basic data

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
<td><p><em>(Optional)</em> The internal name for the item. Default
<samp>Pants</samp>.</p></td>
</tr>
<tr>
<td><p><samp>DisplayName</samp><br />
<samp>Description</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the item's in-game display name and description. Defaults to the generic
pants text (<em>Pants</em> and <em>A wearable pair of
pants</em>).</p></td>
</tr>
<tr>
<td><p><samp>Price</samp></p></td>
<td><p><em>(Optional)</em> The default price when the item is sold to
the player in a shop. Default 50.</p></td>
</tr>
</tbody>
</table>

### Appearance

| field | purpose |
|----|----|
| `Texture` | The asset name for the texture containing the pants' sprite. Defaults to `Characters/Farmer/pants`. |
| `SpriteIndex` | The pants' sprite index within the `Texture`, where 0 is the top-left set. |
| `DefaultColor` | *(Optional)* The dye color to apply to the sprite when the player hasn't <a href="dyeing" class="wikilink" title="dyed">dyed</a> it yet, if any. See <a href="Modding_Common_data_field_types#Color" class="wikilink"
title="color format">color format</a>. Default `255 235 203` (which matches the color of the cloth item). |
| `CanBeDyed` | *(Optional)* Whether the player can <a href="dyeing" class="wikilink" title="dye">dye</a> these pants. Default false. |
| `IsPrismatic` | *(Optional)* Whether the pants continuously shift colors. This overrides `DefaultColor` and `CanBeDyed` if set. Default false. |

### Other

| field | purpose |
|----|----|
| `CanChooseDuringCharacterCustomization` | *(Optional)* Whether these pants can be selected on the character customization screen (e.g. when creating a character). Default false. |
| `CustomFields` | The <a href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry. |

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Штаны" class="wikilink"
title="ru:Модификации:Штаны">ru:Модификации:Штаны</a>
<a href="zh_模组_裤子" class="wikilink"
title="zh:模组:裤子">zh:模组:裤子</a>
