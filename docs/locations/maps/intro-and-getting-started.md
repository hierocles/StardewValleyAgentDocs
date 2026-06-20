---
title: "Intro And Getting Started"
wiki_source: "Modding:Maps"
permalink: /Modding:Maps/
category: locations
tags: [maps, intro, basic-concepts, tile-coordinates, map-formats, tilesets-vs-tilesheets, getting-started, using-smapi]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how to edit maps. This is an advanced guide for
modders.

## Intro

### Basic concepts

- A **map** is the layout of the terrain (like water, cliffs, and land),
  terrain features (like bushes), buildings, paths, and triggers for a
  particular area. When you reach the edge of an area or enter a
  building, and the screen fades to black during the transition, you're
  moving between maps.
- Each map consists of several **layers** stacked one in front of the
  other. Objects in a layer closer to the front will hide objects in
  layers behind them. From back to front, the standard layers are...
  | layer name | typical contents |
  |----|----|
  | Back | Terrain, water, and basic features (like permanent paths). |
  | Buildings | Placeholders for buildings (like the farmhouse). Any tiles placed on this layer will act like a wall unless the tile property has a "Passable" "T". |
  | Paths | Flooring, paths, grass, and debris (like stones, weeds, and stumps from the 'paths' tilesheet) which can be removed by the player. |
  | Front | Objects that are drawn on top of things behind them, like most trees. These objects will be drawn on top of the player if the player is North of them but behind the player if the player is south of them. |
  | AlwaysFront | Objects that are always drawn on top of other layers as well as the player. This is typically used for foreground effects like foliage cover. |

<a href="File_MapLayers.png" class="wikilink"
title="File:MapLayers.png"><span>File:MapLayers.png</span></a>

<li>

You can add any number of map layers by suffixing a vanilla layer name
(i.e. `Back`, `Buildings`, `Front`, or `AlwaysFront`) with an offset.
For example, `Back-1` will be drawn before/under `Back`, and `Back2`
will be drawn after/over it. You can increment the number to add more
layers. This only affects layer rendering; The original layers must be
used for tile properties and collisions (i.e. Buildings tiles acting as
a wall).

</li>

<li>

(Using Tiled) There are 2 different types of layers along with the 5
main layers, Objects Layer (cloud-like icon) and Tile Layer (grid icon).
The Tile Layer is where you make map edits (placing and removing tiles)
and the Objects Layers is where you add and edit tile data. Your layers
must match the ones above. Note that depending on the map, they may be
missing a Paths or AlwaysFront layer

</li>

<li>

Each layer consists of many **tiles**, which are 16×16 pixel squares
placed in a grid to form the visible map. Each tile can have properties
(*e.g.,* passable / blocked), special logic (*e.g.,* an action to
perform when the player steps on them), and a picture to show. The
picture is represented by a sprite index (or tile index), which is its
position in an associated spritesheet (see next).

</li>

<li>

Each map has one or more spritesheets (also known as tilesheets when
talking about mods), which contains the available tiles and images that
are put together to form the visible map.

</li>

</ul>

### Tile coordinates

Each tile has an (x, y) coordinate which represents its position on the
map, where (0, 0) is the top-left tile. The *x* value increases towards
the right, and *y* increases downwards. For example:

<a href="File_Modding_-_creating_an_XNB_mod_-_tile_coordinates.png"
class="wikilink"
title="File:Modding - creating an XNB mod - tile coordinates.png"><span>File:Modding</span>
- creating an XNB mod - tile coordinates.png</a>

You can use the mod to see tile coordinates in-game.

### Map formats

There are two map formats used in Stardew Valley modding: `.tmx` (from
the Tiled map editor) and `.tbin` (from the now-deprecated tIDE map
editor). The features supported by both formats are almost identical,
but there are a few differences:

| feature | `.tmx` | `.tbin` |
|----|----|----|
| format | ✓ XML (basically text) | ✘ binary |
| edit in Tiled | ✓ supported | ✓ supported with plugin |
| edit directly | ✓ can open in a text editor | ✘ not supported |
| tile flip | ✓ supported | ✘ not supported |
| tile rotation | ✓ supported | ✘ not supported |
| source control | ✓ efficient storage, can diff changes | ✘ inefficient storage (need to copy entire file with each commit), can't diff changes |

`.tmx` is recommended per the above, but both formats are fine to use,
and you can convert between them in Tiled by clicking *File \> Export
As*.

### Tilesets vs Tilesheets

`Tilesheets` are the `.png` files used as source images. Tilesheets have
no animation, properties, terrains, or anything else but pixels
associated with them -- they're just images. `Tilesets` are Tiled's XML
files that contain all the information about how the map uses the source
image. They are confusingly named and often used interchangeably.

## Getting started

There are two main ways to edit a map and two main ways to get your map
into the game.

### Using SMAPI

Creating a SMAPI mod requires programming, but it's much more powerful
and multiple SMAPI mods can edit the same map. If you want to use this
approach:

1.  <a href="Modding_Modder_Guide_Get_Started" class="wikilink"
    title="Create a SMAPI mod">Create a SMAPI mod</a>.
2.  See *<a href="#Making_changes_with_SMAPI" class="wikilink"
    title="Making changes with SMAPI">Making changes with SMAPI</a>*
    below.

The rest of this guide assumes you're using Tiled, but many of the
concepts are transferrable and you can use both Tiled and SMAPI (*e.g.,*
create/edit maps in Tiled and load/edit them in SMAPI).

### Using Tiled

Tiled is a popular map editor that can be used to edit Stardew Valley
maps, no programming needed. You need to
<a href="Modding_Editing_XNB_files" class="wikilink"
title="unpack the map&#39;s XNB">unpack the map's XNB</a>, edit the map,
and make a or SMAPI mod to load your map. If you want to use this
approach:

1.  Install the [latest version of Tiled](http://www.mapeditor.org/).
2.  Set the following settings:
    | setting | value | reason |
    |----|----|----|
    | *View \> Snapping \> Snap to Grid* | ✓ enabled | This is required to convert objects back into the game's format. |
    | *View \> Highlight Current Layer* | ✓ enabled | This makes it more clear which tile you're editing. |
3.  See <a href="Modding_Editing_XNB_files" class="wikilink"
    title="Modding:Editing XNB files">Modding:Editing XNB files</a> for
    help unpacking & packing the map files.
4.  See instructions below for map changes.

### Getting your map in game

Once you've used the tips on this page to create your map you will need
to make it show up in the game. You can do this by editing a vanilla
location to replace/edit the existing map with your own or by adding a
new location. After loading your save, you can use this console command
to jump to the map: `debug warp YourLocationName`.

Most mods will use <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> to add a map to the game but
it is also possible to do so with C#.

**NOTE:**

#### Editing a vanilla location

##### Using Content Patcher

Use a Content Patcher action to replace a vanilla map in its entirety.
*This is not recommended in most circumstances outside of testing due to
low compatibility with other mods.*

It is also possible to replace a vanilla map in its entirety by using a
Content Patcher action. It is more frequently used to replace part of a
map instead (such as to add a new building to the Town, for example).

#### Adding a new location

##### Using Content Patcher

New locations are added to the game by your map with a unique asset name
(e.g., `Maps/_MountainForest`) and then editing the
`[[Modding_Location_data|Data/Locations]]` asset to add a new location
entry containing your map.
