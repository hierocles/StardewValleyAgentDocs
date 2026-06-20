---
title: "Shirts"
wiki_source: "Modding:Shirts"
permalink: /Modding:Shirts/
category: items
tags: [shirts, overview, data-format, basic-data, appearance, other, see-also]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses shirt-type item data.
For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

Shirts are items that can be equipped in the player's
<a href="Tailoring#Shirts" class="wikilink" title="shirt">shirt</a>
slot. These change the player sprite.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(S)` (or `ItemRegistry.type_shirt` in
C# code), their data in `Data/Shirts`, their icon sprites in
`Characters/Farmer/shirts` by default, and their code in
`StardewValley.Objects.Clothing`.

## Data format

The shirt data in `Data/Shirts` consists of a string → model lookup,
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
<samp>Shirt</samp>.</p></td>
</tr>
<tr>
<td><p><samp>DisplayName</samp><br />
<samp>Description</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the item's in-game display name and description. Defaults to the generic
shirt text (<em>Shirt</em> and <em>A wearable shirt</em>).</p></td>
</tr>
<tr>
<td><p><samp>Price</samp></p></td>
<td><p><em>(Optional)</em> The default price when the item is sold to
the player in a shop. Default 50.</p></td>
</tr>
</tbody>
</table>

### Appearance

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture containing the shirt's sprite.
Defaults to <samp>Characters/Farmer/shirts</samp>.</p>
<p>Shirt textures must be exactly 256 pixels wide, divided into two
halves: the left half for the shirt sprites, and the right half for any
dye masks. The remaining space can be left blank if needed. They can
have any number of rows.</p>
<pre><code>      sprites       dye masks
   /-----------\  /-----------\
┌────────────────────────────────┐
│ ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐ │
│ │ 0 ││ 1 ││ 2 ││ a ││ b ││ c │ │
│ └───┘└───┘└───┘└───┘└───┘└───┘ │
│ ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐ │
│ │ 3 ││ 4 ││ 5 ││ d ││ e ││ f │ │
│ └───┘└───┘└───┘└───┘└───┘└───┘ │
└────────────────────────────────┘</code></pre></td>
</tr>
<tr>
<td><p><samp>SpriteIndex</samp></p></td>
<td><p>The shirt's sprite index within the <samp>Texture</samp>, where 0
is the top-left set.</p></td>
</tr>
<tr>
<td><p><samp>DefaultColor</samp></p></td>
<td><p><em>(Optional)</em> The dye color to apply to the sprite when the
player hasn't <a href="dyeing" class="wikilink" title="dyed">dyed</a> it
yet, if any. See <a href="Modding_Common_data_field_types#Color"
class="wikilink" title="color format">color format</a>. Default
none.</p></td>
</tr>
<tr>
<td><p><samp>CanBeDyed</samp></p></td>
<td><p><em>(Optional)</em> Whether the player can <a href="dyeing"
class="wikilink" title="dye">dye</a> this shirt. Default false.</p></td>
</tr>
<tr>
<td><p><samp>IsPrismatic</samp></p></td>
<td><p><em>(Optional)</em> Whether the shirt continuously shifts colors.
This overrides <samp>DefaultColor</samp> and <samp>CanBeDyed</samp> if
set. Default false.</p></td>
</tr>
<tr>
<td><p><samp>HasSleeves</samp></p></td>
<td><p><em>(Optional)</em> Whether to draw shirt sleeves. Default
true.</p></td>
</tr>
</tbody>
</table>

### Other

| field | purpose |
|----|----|
| `CanChooseDuringCharacterCustomization` | *(Optional)* Whether this shirt can be selected on the character customization screen (e.g. when creating a character). Default false. |
| `CustomFields` | The <a href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry. |

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>
<a href="ru_Модификации_Топы" class="wikilink"
title="ru:Модификации:Топы">ru:Модификации:Топы</a>
<a href="zh_模组_上衣" class="wikilink"
title="zh:模组:上衣">zh:模组:上衣</a>
