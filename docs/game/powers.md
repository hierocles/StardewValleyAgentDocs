---
title: "Powers"
wiki_source: "Modding:Powers"
permalink: /Modding:Powers/
category: game
tags: [powers, overview, data-format]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses data for
<a href="Special_Items_&amp;_Powers" class="wikilink"
title="Special Items &amp; Powers">Special Items &amp; Powers</a>. This
is an advanced guide for mod developers.

## Overview

Powers are unique "items" that can be obtained only once per player, and
permanently unlock new abilities. Information for powers is stored in
`Data/Powers`. This does **not**, by itself, add any abilities to the
player. It contains information used to display powers in the menu, and
unlock them when needed.

## Data format

You can add/edit <a href="Special_Items_&amp;_Powers" class="wikilink"
title="Special Items &amp; Powers">Special Items &amp; Powers</a> by
editing the `Data/Powers` data asset.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  entry.
- The value is a model with the fields listed below.

| Field | Description |
|----|----|
| `DisplayName` | A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> used to display the translated name of the item, once unlocked. |
| `Description` *(Optional)* | A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> used to display the translated description of the item, once unlocked. |
| `TexturePath` | The asset name for the power's icon texture. |
| `TexturePosition` | The pixel coordinates of the upper left corner of the sprite in the texture, provided as an object with `X` and `Y` fields. Sprites are always 16 by 16. |
| `UnlockedCondition` | A <a href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> used to determine whether or not the item has been unlocked. |
| `CustomFields` *(Optional)* | The <a href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry. |

For example, this Content Patcher pack adds a custom pufferfish power,
which is unlocked after the player catches a pufferfish:

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Способности" class="wikilink"
title="ru:Модификации:Способности">ru:Модификации:Способности</a>
<a href="zh_模组_能力" class="wikilink"
title="zh:模组:能力">zh:模组:能力</a>
