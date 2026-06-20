---
title: "Mannequins"
wiki_source: "Modding:Mannequins"
permalink: /Modding:Mannequins/
category: items
tags: [mannequins, overview, data-format, see-also]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses mannequin-type item
data. For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

<a href="Mannequins" class="wikilink" title="Mannequins">Mannequins</a>
are decorative items which can be placed in the world, and used to store
and display clothing.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(M)` (or `ItemRegistry.type_mannequin`
in C# code), their data in `Data/Mannequins`, their icon sprites in
`TileSheets/Mannequins` by default, and their code in
`StardewValley.Objects.Mannequin`.

## Data format

The mannequin data in `Data/Mannequins` consists of a string → model
lookup, where...

- The key is the
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="unqualified item ID">unqualified item ID</a> and internal name.
- The value is a model with the fields listed below.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DisplayName</samp><br />
<samp>Description</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the item's in-game
display name and description.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Asset_name"
class="wikilink" title="asset name">asset name</a> for the texture
containing the item's sprite. Defaults to
<samp>TileSheets/Mannequins</samp>.</p></td>
</tr>
<tr>
<td><p><samp>SpriteIndex</samp></p></td>
<td><p>The sprite's index within the <samp>Texture</samp>, where 0 is
the top-left sprite.</p></td>
</tr>
<tr>
<td><p><samp>FarmerTexture</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Asset_name"
class="wikilink" title="asset name">asset name</a> for the texture to
show when it's placed in the world. This should match the layout of a
farmer spritesheet like
<samp>Characters/Farmer/farmer_base</samp>.</p></td>
</tr>
<tr>
<td><p><samp>DisplaysClothingAsMale</samp></p></td>
<td><p><em>(Optional)</em> For clothing with gender variants, whether to
display the male (<samp>true</samp>) or female (<samp>false</samp>)
variant. Default true.</p></td>
</tr>
<tr>
<td><p><samp>Cursed</samp></p></td>
<td><p><em>(Optional)</em> Whether to enable rare Easter egg 'cursed'
behavior. Default false.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry.</p></td>
</tr>
</tbody>
</table>

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Манекены" class="wikilink"
title="ru:Модификации:Манекены">ru:Модификации:Манекены</a>
<a href="zh_模组_假人模特" class="wikilink"
title="zh:模组:假人模特">zh:模组:假人模特</a>
