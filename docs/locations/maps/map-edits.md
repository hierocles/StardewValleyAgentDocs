---
title: "Map Edits"
wiki_source: "Modding:Maps"
permalink: /Modding:Maps/
category: locations
tags: [maps, map-edits, editing-maps, adding-tilesets, painting-tiles-onto-your-map, map-properties, tile-properties, tiles]
---
## Map edits

### Editing maps

Important note: when making custom maps, always start with a vanilla map
and edit it. Don't try to create a new map in Tiled; the game needs
certain tiles, map properties, etc to be present. Also note that when
making a map edit or adding a custom map, width sizes larger than 200
will break layering. Height can be any size.

1.  <a href="Modding_Editing_XNB_files" class="wikilink"
    title="Unpack">Unpack</a> the game's `Content/Maps` folder and
    create a copy to edit your maps in. Use this copy of the folder to
    edit any maps in before moving them to your mod release folder.
2.  Use the same method to unpack the map you want to edit if it is not
    a vanilla one, then place the map in your editing folder.
3.  Open the `.tbin` or `.tmx` file via Tiled. Note: make sure the file
    is in the same folder as the unpacked tilesheets!
4.  Make your changes.
5.  Save the file. Don't use `Save as` to change folders, as your
    tilesheet paths will be wrong.
6.  Move the `.tbin` or `.tmx` file, and any custom tilesheets it needs,
    to your mod release folder. Place them in the `assets` folder.
7.  Load your map via SMAPI or Content Patcher (or another framework
    mod).

### Adding tilesets

You can add new sprites, tiles, or images to a map, from both custom and
vanilla sources. If you're editing a vanilla map, make sure to
<a href="#Tilesheet_order" class="wikilink"
title="prefix custom tileset names with z_">prefix custom tileset names
with <code>z_</code></a> to avoid shifting the vanilla tilesheet
indexes.

1.  Open the map that you created or are editing.
2.  Click `Map` then *Add External Tileset...* in the top menu, and open
    a `.tsx` file you have in the same folder.
3.  You should have a new copy of the tileset in your map, with any
    saved animations, properties, or terrains still intact.

#### Re-using vanilla tilesets

If you want to use a tilesheet like `spring_outdoorsTileSheet.png` in
your map, adding a new tileset from a `.png` file means you need to
re-animate any animated tiles, and re-add properties like diggable.
(You'll also lose any terrain types that had been created for that set.)
You can avoid this by first exporting them from an existing map, then
using external tilesets, instead.

1.  Open an existing map that already has the properties and animations
    you want.
2.  In the tileset pane, click the wrench to *Edit Tileset*. It should
    open a new edit tab.
3.  In the new window that opens, click *File*, then *Export as...* and
    save it as a .tsx file.
4.  Close the tileset editor.

#### Replace existing tileset

If you are already using a tilesheet image, you can replace its tileset.

1.  Open the map that you created or are editing.
2.  In the tileset pane on the right, click the tab for your existing
    version.
3.  Under that, click the *Replace Tileset* button.
4.  Choose the `.tsx` file you saved, and click Open.

#### Adding a new custom tilesheet

If you made a your own tilesheet and are adding it to a map the first
time, you can create a new tileset from image.

1.  Create your spritesheet and place it in the same folder as your
    `.tbin` or `.tmx` map file. This should be a PNG image with images
    divided into 16x16 tiles (see
    <a href="Modding_Editing_XNB_files#Intro" class="wikilink"
    title="Modding:Editing XNB files#Intro">Modding:Editing XNB
    files#Intro</a> for examples).
2.  Open the map in Tiled.
3.  Add the custom spritesheet:
    1.  In the *Tilesets* pane, click the <a
        href="File_Modding_-_creating_an_XNB_mod_-_Tiled_&#39;new_tilesheet&#39;_button.png"
        class="wikilink"
        title="File:Modding - creating an XNB mod - Tiled &#39;new tilesheet&#39; button.png"><span>File:Modding</span>
        - creating an XNB mod - Tiled 'new tilesheet' button.png</a>
        button.
    2.  Give it a descriptive name (like 'zcute bugs') and choose the
        image source.
    3.  Make sure that *Embed in map* is checked.
    4.  Keep the defaults for the other settings and click *OK*.

### Painting tiles onto your map

1.  In the *Layers* pane, click the layer you want to edit.
2.  At the top left of Tiled's toolbar, click the Stamp Brush.
3.  In the *Tilesets* pane, click the tab for the tileset you want to
    use.
4.  In the *Tilesets* pane, click one tile to select it. To choose
    multiple, click and drag the cursor.
5.  Move the cursor to the map, and you'll see an overlay with the tiles
    you selected.
6.  Click the map to place those tiles on the selected layer.

### Map properties

Each map can have multiple map properties, which define attributes and
behaviour associated with the map like lighting, music, warp points,
etc. Each property has a name (which defines the type of property), type
(always 'string' in Stardew Valley), and value (which configures the
property). See <a href="#Known_map_properties" class="wikilink"
title="known properties">known properties</a> below.

In Tiled:

1.  Click *Map* on the toolbar and choose *Map Properties*.
2.  View and edit properties using the GUI.

### Tile properties

Tile properties are set on individual map tiles. They can change game
behaviour (like whether the player can cross them), or perform actions
when the player steps on or clicks the tile. Each property has a name,
type (always 'string' in Stardew Valley), and value. In Tiled these are
represented by two types: *object properties* only apply to the selected
tile, while *tile properties* apply to every instance of that tile. In
general you'll always set *object properties*, so we'll only cover
those.

Note that tile properties need to have a tile associated with them; if
there is no tile, they'll simply not be applied.

To view tile properties:

1.  Select the object layer in the *Layers* pane.
2.  Choose the <a
    href="File_Modding_-_creating_an_XNB_mod_-_Tiled_&#39;select_object&#39;_button.png"
    class="wikilink"
    title="File:Modding - creating an XNB mod - Tiled &#39;select object&#39; button.png"><span>File:Modding</span>
    - creating an XNB mod - Tiled 'select object' button.png</a> *select
    object* tool in the toolbar.
3.  Click the object whose properties you want to view. Objects are
    represented with a gray selection box on the map:\
    <a href="File_Modding_-_creating_an_XNB_mod_-_map_object.png"
    class="wikilink"
    title="File:Modding - creating an XNB mod - map object.png"><span>File:Modding</span>
    - creating an XNB mod - map object.png</a>
4.  The object properties will be shown in the *Properties* pane.\
    <a
    href="File_Modding_-_creating_an_XNB_mod_-_Tiled_tile_properties_pane.png"
    class="wikilink"
    title="File:Modding - creating an XNB mod - Tiled tile properties pane.png"><span>File:Modding</span>
    - creating an XNB mod - Tiled tile properties pane.png</a>

To edit properties for an existing object:

- Change a value: click the value field and enter the new value.
- Change a name: select the property and click the <a
  href="File_Modding_-_creating_an_XNB_mod_-_Tiled_&#39;edit&#39;_button.png"
  class="wikilink"
  title="File:Modding - creating an XNB mod - Tiled &#39;edit&#39; button.png"><span>File:Modding</span>
  - creating an XNB mod - Tiled 'edit' button.png</a> icon.
- Add a property: click the <a
  href="File_Modding_-_creating_an_XNB_mod_-_Tiled_&#39;add&#39;_button.png"
  class="wikilink"
  title="File:Modding - creating an XNB mod - Tiled &#39;add&#39; button.png"><span>File:Modding</span>
  - creating an XNB mod - Tiled 'add' button.png</a> icon, enter the
  property name, make sure the selected type is "string", and click OK.

To add a new object:

1.  Select the object layer in the *Layers* pane.\
    *There should be one object layer for each tile layer. If the object
    layer is missing, create one with the same name as the right tile
    layer.*
2.  Choose the <a
    href="File_Modding_-_creating_an_XNB_mod_-_Tiled_&#39;insert_rectangle&#39;_button.png"
    class="wikilink"
    title="File:Modding - creating an XNB mod - Tiled &#39;insert rectangle&#39; button.png"><span>File:Modding</span>
    - creating an XNB mod - Tiled 'insert rectangle' button.png</a>
    *insert rectangle* tool from the toolbar.
3.  Click and drag the rectangle over the tile you want to edit . Make
    sure it snaps to the tile grid (see
    <a href="#Using_Tiled" class="wikilink" title="#Using Tiled">#Using
    Tiled</a>), and only one tile is selected.
4.  Change its Name field to `TileData`.
5.  See previous for how to edit its properties.

### Tiles

You can edit the tiles for an existing map. See the [Tiled
documentation](http://doc.mapeditor.org) for more info.

### Tile animation

<a href="File_Modding_-_creating_an_XNB_mod_-_example_animation.gif"
class="wikilink" title="right">right</a> You can animate tiles to create
effects like Gil in his rocking chair (see example at right).

In Tiled:

:# Click the edit button (wrench icon) for the tilesheet in the
*Tilesets* pane.

:# Select the tile you want to animate in the new view.

:# Click *Tileset \> Tile Animation Editor* in the toolbar to show that
window.

:# In the new window, drag tiles from the tilesheet into the box on the
left to create a *frame* (one image in the sequence). If you need to
delete frames, select the frame(s) and press Backspace/Delete(Windows)
or fn + Backspace(Apple)

:# Double-click the numbers to change how long each frame stays on the
screen before the next one (in milliseconds). **Make sure every frame
has the same time; the game can't handle variable frame times.** For
example, here's the animation editor showing one of the tiles of Gil
rocking:\
<a
href="File_Modding_-_creating_an_XNB_mod_-_Tiled_example_animation_pane.gif"
class="wikilink"
title="File:Modding - creating an XNB mod - Tiled example animation pane.gif"><span>File:Modding</span>
- creating an XNB mod - Tiled example animation pane.gif</a>

:# When you're done, close the pane.

:# The animated tiles in the *Tilesets* pane will now have a little
symbol in the bottom-right corner:\
<a
href="File_Modding_-_creating_an_XNB_mod_-_Tiled_example_animation_tileset.png"
class="wikilink"
title="File:Modding - creating an XNB mod - Tiled example animation tileset.png"><span>File:Modding</span>
- creating an XNB mod - Tiled example animation tileset.png</a>\
The animation is now part of that tile. Every instance of that tile on
the map will now have the same animation.

### Tile flip/rotation

<a href="File_Tiled_tile_rotation.png" class="wikilink"
title="thumb">thumb</a>

You can rotate and flip tiles without needing to create rotated/flipped
versions of the tilesheet.

In Tiled:

:# With the stamp tool selected, click the tile in the tilesheet you
want to use.

:# Click the flip or rotate buttons (see image at right).

:# Click the map to place the flipped/rotated tile.

**NOTE:**
