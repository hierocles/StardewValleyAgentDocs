---
title: "Boots"
wiki_source: "Modding:Boots"
permalink: /Modding:Boots/
category: items
tags: [boots, overview, data-format, example, see-also]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses boots-type item data.
For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

Boots are items which can be equipped in the player's
<a href="boots" class="wikilink" title="boots">boots</a> slot. These
change the player sprite and may provide buffs.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(B)` (or `ItemRegistry.type_boots` in
C# code), their data in `Data/Boots`, their sprites in
`Maps/springobjects` (item) and `Characters/Farmer/shoeColors` (shoe
color) by default, and their code in `StardewValley.Objects.Boots`.

## Data format

The boots data in `Data/Boots` consists of a string → string dictionary,
where...

- The key is the
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="unqualified item ID">unqualified item ID</a>.
- The value is a slash-delimited string with the fields listed below.

| index | field | effect |
|----|----|----|
| 0 | Name | The internal item name (and display name in English). |
| 1 | Description | The translated item description shown in-game. |
| 2 | Price | **Unused.** The actual price is calculated as `(''added defence'' × 100) + (''added immunity'' × 100)`. |
| 3 | Added Defense | A <a href="defense" class="wikilink" title="defense">defense</a> bonus applied to the player while equipped. |
| 4 | Added Immunity | An <a href="immunity" class="wikilink" title="immunity">immunity</a> bonus applied to the player while equipped. |
| 5 | Color Index | The boots color index within the Color Texture, where 0 is the top-left set, if present, otherwise the `Characters/Farmer/shoeColors` spritesheet. |
| 6 | Display Name | The translated item name shown in-game (for non-English assets only). |
| 7 | Color Texture | The asset name for the texture containing the boots color sprite. |
| 8 | Sprite Index | The boots sprite index within the Texture, where 0 is the top-left set. |
| 9 | Texture | The asset name for the texture containing the boots sprite. |

## Example

You can add a custom boots item using
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> like this:

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Обувь" class="wikilink"
title="ru:Модификации:Обувь">ru:Модификации:Обувь</a>
<a href="zh_模组_靴子" class="wikilink"
title="zh:模组:靴子">zh:模组:靴子</a>
