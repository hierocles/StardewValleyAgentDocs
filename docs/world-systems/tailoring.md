---
title: "Tailoring"
wiki_source: "Modding:Tailoring"
permalink: /Modding:Tailoring/
category: world-systems
tags: [tailoring, overview, data-format, examples, open-the-tailoring-menu, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and uses tailoring recipe data.
This is an advanced guide for mod developers.

## Overview

Tailoring recipes are recipes that can be made in the tailoring menu,
which can be opened by interacting with the
<a href="Sewing_Machine" class="wikilink" title="Sewing Machine">Sewing
Machine</a> either at Emily's house or once the player obtains it.

Tailoring recipe data is stored in the `Data/TailoringRecipes` asset.

## Data format

The `Data/TailoringRecipes` asset consists of a string → model lookup,
where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  tailoring recipe.
- The value is a model with the fields listed below.

| field | effect |
|----|----|
| `FirstItemTags` | A list of <a href="Modding_Context_tags" class="wikilink"
title="context tags">context tags</a> for items that can be accepted by the feed slot on the left-hand side of the tailoring menu for this recipe. Typically contains the `item_cloth` context tag. |
| `SecondItemTags` | A list of <a href="Modding_Context_tags" class="wikilink"
title="context tags">context tags</a> for items that can be accepted by the spool slot on the right-hand side of the tailoring menu for this recipe. If a specific item is needed, the item's automatically generated context tag should be used, for example `item_magic_rock_candy`. |
| `SpendRightItem` | *(Optional)* Whether to consume the item in the spool slot on the right-hand side of the tailoring menu when crafting the item. Default `true`. |
| `CraftedItemId` | The <a href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_items"
class="wikilink" title="qualified item ID">qualified item ID</a> of the crafted item. |
| `CraftedItemIds` | *(Optional)* A list of <a href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_items"
class="wikilink" title="qualified item IDs">qualified item IDs</a> of possible crafted item outputs. For example, placing a <a href="Prismatic_Shard" class="wikilink"
title="Prismatic Shard">Prismatic Shard</a> in the feed slot of the tailoring menu has multiple possible clothing item outputs. Default `null`. |
| `CraftedItemIdFeminine` | *(Optional)* The <a href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_items"
class="wikilink" title="qualified item ID">qualified item ID</a> of the alternate crafted item output based on the player's gender. Assumes the CraftedItemId field contains the masculine version of the crafted item. Default `null`. |

### Examples

You can add or replace tailoring recipes. For example, this content pack
adds a recipe to tailor a rain coat using cloth and a pufferchick:

## Open the Tailoring Menu

You can place an <a href="Modding_Maps#Action" class="wikilink"
title="Action Tailoring tile property"><samp>Action Tailoring</samp>
tile property</a> on the map, which will open the tailoring menu when
the player clicks it. The player must have seen event 992559 (the event
where Emily visits the farmhouse after you have gotten your first piece
of cloth) for it to open.

## See also

<a href="Modding_Recipe_data" class="wikilink"
title="Modding:Recipe data">Modding:Recipe data</a> for data about
cooking and crafting recipes.

<a href="Modding_Hats" class="wikilink"
title="Modding:Hats">Modding:Hats</a> for data about hat items.

<a href="Modding_Shirts" class="wikilink"
title="Modding:Shirts">Modding:Shirts</a> for data about shirt items.

<a href="Modding_Pants" class="wikilink"
title="Modding:Pants">Modding:Pants</a> for data about pant items.

<a href="Modding_Boots" class="wikilink"
title="Modding:Boots">Modding:Boots</a> for data about boot items .

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Шитьё" class="wikilink"
title="ru:Модификации:Шитьё">ru:Модификации:Шитьё</a>
