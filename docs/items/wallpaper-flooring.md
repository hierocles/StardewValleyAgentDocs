---
title: "Wallpaper Flooring"
wiki_source: "Modding:Wallpaper and flooring"
permalink: /Modding:Wallpaper_and_flooring/
category: items
tags: [wallpaper-and-flooring, overview, data-format, example, see-also]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses wallpaper and
flooring-type item data. For items in general, see
<a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

Wallpaper and flooring (or *floorpaper*) are items which can be applied
to a decoratable location like a
<a href="farmhouse" class="wikilink" title="farmhouse">farmhouse</a> or
<a href="shed" class="wikilink" title="shed">shed</a> to visually change
its floor or wall design. These are separate from placeable flooring
items like
<a href="Brick_Floor" class="wikilink" title="brick floor">brick
floor</a>.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item types">item types</a> `(WP)` and `(FL)` respectively (or
`ItemRegistry.type_wallpaper` and `ItemRegistry.type_floorpaper` in C#
code); their data in `Data/AdditionalWallpaperFlooring`; their icon
sprites in `Maps/walls_and_floors`, `Maps/floors_2`, or
`Maps/wallpapers_2` by default; and their code in
`StardewValley.Objects.Wallpaper`.

## Data format

The wallpaper and flooring data in `Data/AdditionalWallpaperFlooring`
consists of a list of models, where each value is a model with the
fields listed below.

| field | description |
|----|----|
| `ID` | A unique ID value. This is not shown in-game. |
| `Texture` | The asset name which contains 32x32 pixel (flooring) or 16x48 pixel (wallpaper) sprites. The tilesheet must be 256 pixels wide, but can have any number of flooring/wallpaper rows. |
| `IsFlooring` | Whether this is a flooring tilesheet; else it's a wallpaper tilesheet. |
| `Count` | The number of flooring or wallpaper sprites in the tilesheet. |

## Example

For example, this <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> pack would add three new
wallpapers to the game:

## See also

- The `logWallAndFloorWarnings`
  <a href="Modding_Console_commands" class="wikilink"
  title="console command">console command</a>
- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Обои_и_напольные_покрытия" class="wikilink"
title="ru:Модификации:Обои и напольные покрытия">ru:Модификации:Обои и
напольные покрытия</a> <a href="zh_模组_墙纸和地板" class="wikilink"
title="zh:模组:墙纸和地板">zh:模组:墙纸和地板</a>
