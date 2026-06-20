---
title: "Paths Troubleshooting Smapi"
wiki_source: "Modding:Maps"
permalink: /Modding:Maps/
category: locations
tags: [maps, paths-layer, potential-issues, tilesheet-order, local-copy-of-a-vanilla-tilesheet, map-specific-issues, save-as-in-tiled, locating-tilesheets-in-tiled]
---
## Paths layer

The `Paths` layer has icon tiles from the `paths` tilesheet which affect
game behavior on the map:

<a href="File_PathsExplanation.png" class="wikilink"
title="thumb">thumb</a>

<table>
<thead>
<tr>
<th><p>tile index</p></th>
<th><p>explanation</p></th>
<th><p>restrictions</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0–6</p></td>
<td><p>Unused.</p></td>
<td></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p>Used in the <a href="Modding_NPC_data" class="wikilink"
title="spouse patio/room">spouse patio/room</a> and <a
href="Movie_Theater" class="wikilink" title="movie theater">movie
theater</a> to mark where an NPC should stand.</p>
<p>For the movie theater only, you can add a <samp>direction</samp> tile
property on the <samp>Paths</samp> layer with the <a
href="Modding_Event_data#Directions" class="wikilink"
title="facing direction">facing direction</a> numeric value (default
down). In the spouse patio/room, you can't set the initial facing
direction.</p></td>
<td><p>Used for spouse areas and the Movie Theater.</p></td>
</tr>
<tr>
<td><p>8</p></td>
<td><p>Add this tile to the <a href="#Map_properties_2" class="wikilink"
title="Light map property"><samp>Light</samp> map property</a> with
light type 4 (sconce).</p></td>
<td><p>Indoors and festivals only.²</p></td>
</tr>
<tr>
<td><p>9–12</p></td>
<td><p>Spawn a <a href="trees" class="wikilink" title="tree">tree</a>
when the location is created. Trees have a 50% chance to respawn each
day outside the farm. (See also 31–32.)<br />
Available trees: oak (9), maple (10), pine (11), and palm 1
(12).</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>13–18</p></td>
<td><p>Spawn debris when the location is created, or randomly each day.
Outside the farm, respawn in spring.<br />
Available debris: <a href="weeds" class="wikilink"
title="seasonal weed">seasonal weed</a> (13–15), rock (16–17), twig
(18).</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>19</p></td>
<td><p>Spawn a <a href="Large_Log" class="wikilink"
title="large log">large log</a> when the farm is created, with the
top-left corner on this tile.</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>20</p></td>
<td><p>Spawn a <a href="boulder" class="wikilink"
title="boulder">boulder</a> when the farm is created, with the top-left
corner on this tile.</p></td>
<td><p>Farm only.</p></td>
</tr>
<tr>
<td><p>21</p></td>
<td><p>Spawn a <a href="Large_Stump" class="wikilink"
title="hardwood stump">hardwood stump</a> when the farm is created (and
every day on the forest farm), with the top-left corner on this
tile.</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>22</p></td>
<td><p>Spawn <a href="grass" class="wikilink" title="grass">grass</a>
when the location is created, or randomly afterwards.</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>23</p></td>
<td><p>Spawn a random oak, maple, or pine <a href="trees"
class="wikilink" title="tree">tree</a> at growth stage 2–3 when the
location is created.</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>24–26</p></td>
<td><p>Spawn a normal bush when the location is created. Medium bushes
grow <a href="blackberry" class="wikilink"
title="blackberries">blackberries</a> and <a href="salmonberry"
class="wikilink" title="salmonberries">salmonberries</a>.<br />
Available bushes: large (24), medium (25), small (26).</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>27</p></td>
<td><p>When the location is created, add this tile to the <a
href="#Map_properties_2" class="wikilink"
title="BrookSounds map property"><samp>BrookSounds</samp> map
property</a> with the <samp>babblingBrook</samp> sound.</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>28</p></td>
<td><p>Spawn a <a href="grub" class="wikilink" title="grub">grub</a>
here (33% chance per day, unless the map already has 50 grubs).</p></td>
<td><p><a href="Mutant_Bug_Lair" class="wikilink"
title="Mutant Bug Lair">Mutant Bug Lair</a> only.</p></td>
</tr>
<tr>
<td><p>29–30</p></td>
<td><p>Place prebuilt <a href="cabin" class="wikilink"
title="cabin">cabins</a> in <a href="multiplayer" class="wikilink"
title="multiplayer">multiplayer</a> based on the layout (29=nearby or
30=separate) and <a href="#Tile_properties_2" class="wikilink"
title="Order tile property"><samp>Order</samp> tile property</a>, with
the top-left corner on this tile.</p></td>
<td><p>Farm only.</p></td>
</tr>
<tr>
<td><p>31–32</p></td>
<td><p>Spawn a <a href="trees" class="wikilink" title="tree">tree</a>
when the location is created. Trees have a 50% chance to respawn each
day outside the farm. (See also 9–12.)<br />
Available trees: palm 2 (31), mahogany (32).</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>33</p></td>
<td><p>Spawn a <a href="Golden_Walnut" class="wikilink"
title="golden walnut">golden walnut</a> bush when the location is
created.</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>34</p></td>
<td><p>Enables the <samp>SpawnTree</samp> <a
href="Modding_Maps#Known_tile_properties" class="wikilink"
title="tile property">tile property</a> on this tile, which lets you
spawn/regrow wild or fruit trees.</p></td>
<td><p>Outdoors only.</p></td>
</tr>
<tr>
<td><p>35</p></td>
<td><p>Has no effect in-game. This is just a visual indicator you can
use when editing maps (e.g. to keep track of where you set tile
properties).</p></td>
<td></td>
</tr>
<tr>
<td><p>36</p></td>
<td><p>Spawn blue <a href="grass" class="wikilink"
title="grass">grass</a> when the location is created, or randomly
afterwards.</p></td>
<td><p>Outdoors only.</p></td>
</tr>
</tbody>
</table>

Notes:

1.  In the <a href="Mutant_Bug_Lair" class="wikilink"
    title="Mutant Bug Lair">Mutant Bug Lair</a>, debris spawn rate is
    reduced to 33% chance per day.
2.  Restriction can be overridden with `forceLoadPathLayerLights` map
    property.

## Potential issues

### Tilesheet order

When you replace a vanilla map, **don't** change the order or IDs of the
original tilesheets. Prefix new tilesheet IDs with `z_` to avoid
changing the original order.

Why this causes problems
For example, let's say you replace a map which normally has these
tilesheets in Tiled:

<a href="File_Tiled_tileset_order_A.png" class="wikilink"
title="thumb">thumb</a>

<!-- -->


When you add a new tilesheet, note that the order changes from *\[paths,
untitled tile sheet\]* to *\[customSheet, paths, untitled tile sheet\]*:

<a href="File_Tiled_tileset_order_B.png" class="wikilink"
title="thumb">thumb</a>

<!-- -->


If the game tries to access a tile from the first tilesheet, it will get
it from `customSheet` instead of the expected `Paths` tilesheet. That
can cause anything from visual glitches (*e.g.,* showing the wrong tile
images) to outright crashes (especially if the new tilesheet is smaller
than the one it expected).

<!-- -->


To avoid that, always keep the original tilesheets in the same order and
prefix new tilesheets with `z_` so they're added at the end:

<a href="File_Tiled_tileset_order_C.png" class="wikilink"
title="thumb">thumb</a>

<!-- -->

How to fix an affected tilesheet
See *<a href="#&quot;mod_reordered_the_original_tilesheets&quot;"
class="wikilink"
title="&quot;mod reordered the original tilesheets&quot;">"mod reordered
the original tilesheets"</a>* below.

### Local copy of a vanilla tilesheet

When editing a map in Tiled, you may need to copy vanilla tilesheets
like `path.png` or `spring_town.png` into the map folder for Tiled to
find. If the tilesheet is still there when you load the game, SMAPI will
use it for your map instead of the game's vanilla tilesheet, which may
have unintended effects (*e.g.,* edits from recolor mods won't work in
your map).

To avoid issues, you can either...

- Delete vanilla tilesheets from the folder before testing or releasing
  the mod.
- Rename the tilesheet file to start with a dot (like
  `.spring_town.png`) and reference that. When SMAPI loads the map
  in-game, it'll automatically ignore the dot and look for
  `spring_town.png` in the local files or `Content/Maps` folder.

### Map-specific issues

The game makes some assumptions about maps which may break for modded
maps. These are the known issues:

<table>
<thead>
<tr>
<th><p>affected maps</p></th>
<th><p>issue</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Maps/Farm</samp><br />
<samp>Maps/Farm_Combat</samp><br />
<samp>Maps/Farm_Fishing</samp><br />
<samp>Maps/Farm_Foraging</samp><br />
<samp>Maps/Farm_Mining</samp></p></td>
<td><ul>
<li>The farm's <samp>Paths</samp> layer must have at least one tile with
index 22 (grass spawn). This is used to initialise the grass code when
the save is loaded, even if no grass is spawned.<a href="#fn1"
class="footnote-ref" id="fnref1"
role="doc-noteref"><sup>1</sup></a></li>
</ul></td>
</tr>
<tr>
<td><p><samp>Maps/FarmHouse*</samp></p></td>
<td><ul>
<li>The two bed tiles where the player can walk must have two
properties: <samp>Bed T</samp> (used to decide if the player is in bed)
and <samp>TouchAction Sleep</samp>.</li>
<li>Deleting or changing the wallpapers and floors will cause a game
crash.</li>
<li>The <samp>DayTiles</samp> and <samp>NightTiles</samp> map properties
are cleared when loading the spouse room, so custom values for those
properties won't work for married players.</li>
<li>Changes that overlap renovation areas will be overwritten by the
renovation. In order to fix this you have to replace the renovation map
file with an empty map file.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Maps/SpouseRooms</samp></p></td>
<td><ul>
<li>If you add or resize any tilesheet, you must also edit
<samp>Maps/FarmHouse1_marriage</samp> and
<samp>Maps/FarmHouse2_marriage</samp> to have the same changes (even if
you don't make any other changes to the farmhouse). This is needed
because the tilesheet references and sizes are stored as part of the map
file.</li>
</ul></td>
</tr>
</tbody>
</table>
<section id="footnotes" class="footnotes footnotes-end-of-document"
role="doc-endnotes">
<hr />
<ol>
<li id="fn1">The grass sound is set in <samp>Grass::loadSprite</samp>,
which is called from <samp>GameLocation::loadObjects</samp> if the
<samp>Paths</samp> layer has tile index 22. (The game spawns a grass for
each such tile, and later removes them.)<a href="#fnref1"
class="footnote-back" role="doc-backlink">↩︎</a></li>
</ol>
</section>

<small>

<references />

</small>

### 'Save as' in Tiled

When you use 'save as' in Tiled, never save into a different folder.
That will change all the tilesheet references to point to the old
folder, so it'll no longer work in-game. Instead, copy/move the map
files to a different folder if needed.

### Locating tilesheets in Tiled

When a map tilesheet is missing, never use the locate option to use a
tilesheet from a different folder. That will add a complex tilesheet
path which won't work in-game. Instead copy the tilesheets into the same
folder as the map, and reference them from there.

## Troubleshooting

See also <a href="#Potential_issues" class="wikilink"
title="potential issues"><em>potential issues</em></a> above for common
issues.

### "Directory climbing (../) is only permitted once at the start of the path"

What does this mean?
You can reference a tilesheet that's either (a) within the map asset's
folder, or (b) within the game's `Content` folder in the pipeline.

<!-- -->


Your map can't use a tilesheet that's outside those folder roots. That
might happen if you
<a href="#&#39;Save_as&#39;_in_Tiled" class="wikilink"
title="used &#39;save as&#39; in Tiled to save into a different folder">used
'save as' in Tiled to save into a different folder</a>, copied & pasted
tiles between maps in different folders, or manually added a tilesheet
from a different folder.

<!-- -->


For example:

<!-- -->

    📁 Stardew Valley/
       📁 Content/
          📁 Maps/
             🗎 townInterior     <──┐
       📁 Mods/                    │
          📁 YourModName/          │ ../../../Content/Maps/townInterior
             📁 assets/            │
                🗎 your-map.tmx  ───┘


This isn't allowed since it's very fragile (*e.g.,* players might
install your mod in a different folder path).

<!-- -->

How do I fix it?

:# Copy the tilesheets you're using into the same folder as the map.

:# For unchanged vanilla tilesheets, rename them to start with a dot
(like `.townInterior.png`). This tells SMAPI to ignore the file when
loading the map in-game, and load the one in the `Content` folder
instead.

:# In Tiled, click the edit icon under the tilesheet.

:# In the tab that opens, click *Tileset \> Tileset Properties*.

:# Click the 'Image' field, then the 'Edit' button to locate the
tilesheet in the same folder. For a screenshot guide of steps 3-5, [see
these images](https://imgur.com/a/rukygAr) provided by Discord user
foggywizard#7430.


After fixing it, the above example would look like this:

<!-- -->

    📁 Stardew Valley/
       📁 Mods/
          📁 YourModName/
             📁 assets/
                🗎 your-map.tmx       ───┐
                🗎 .townInterior.png  <──┘ .townInterior.png

### "mod reordered the original tilesheets"

What does this mean?
See <a href="#Tilesheet_order" class="wikilink"
title="tilesheet order"><em>tilesheet order</em></a> for more info.

<!-- -->

How do I fix it?
Always keep the original tilesheets in the same order and prefix new
tilesheets with `z_` so they're added at the end:

<a href="File_Tiled_tileset_order_C.png" class="wikilink"
title="thumb">thumb</a>

<!-- -->


To rename an affected tilesheet in Tiled:

<File:Tiled> rename tileset A.png\|In the tileset pane, click the tab
for the tileset and then click the edit icon. <File:Tiled> rename
tileset B.png\|Click *Tileset \> Tileset Properties* from the top menu
to show the properties pane. <File:Tiled> rename tileset C.png\|Change
the name in the *Name* field.

### "mod has no tilesheet with ID '\<name\>'"

What does this mean?
You replaced one of the vanilla maps, but your custom map doesn't have
all of the original map's tilesheets (or you changed their names in
Tiled). This will cause a crash if the game tries to access the missing
tilesheet.

<!-- -->

How do I fix it?
Compare the original and custom maps in Tiled. For each tilesheet in the
original map, make sure it's also in the custom map **and** has the same
name (even if you're not using it).

<!-- -->


If you need to rename a tilesheet:

1.  In the tileset pane, click the tab for the tileset and then click
    the edit icon.
2.  Click *Tileset \> Tileset Properties* from the top menu to show the
    properties pane.
3.  Change the *Name* field to match the original map's tilesheet name.

### "Invalid tile GID: \<#\>"

What does this mean?
You edited your map without one of the tilesheets present in the same
folder as your tmx, causing the XML data to lose information about the
tilesheet and recalculate the starting GID's for the other tilesets
incorrectly.

And/Or


A tilesheet your map references no longer exists in the files, causing
the same above problem.

<!-- -->

How do I fix it?
Make sure all the tilesheets your map uses are in the same folder as
your tmx, then make any small change to your map, and finally save your
map.

This should cause Tiled to update the XML data and recalculate the
starting GID's. You can then remove the change you made and save again.

Always make sure to have your tilesheets in the same folder as your tmx
when editing your map in order to avoid invalid tile GID errors.

And/Or


If your map was using a tilesheet that no longer exists (several were
removed in 1.6.9+), then you need to replace any reference to that
tilesheet with one that does still exist or get a copy of it and ship it
with your mod.

## Making changes with SMAPI

This page mainly covers editing maps with Tiled, but you can make the
same changes programmatically using a
<a href="Modding_Modder_Guide_Get_Started" class="wikilink"
title="C# SMAPI mod">C# SMAPI mod</a>. There are two main approaches to
changing a location in C# code.

### Using the `AssetRequested` event

Most map edits should be applied using
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="the AssetRequested event">the <samp>AssetRequested</samp>
event</a>, so your changes aren't lost if another mod reloads the map.
This works with the `Map` asset directly before it's used by the
<a href="Modding_Modder_Guide_Game_Fundamentals#GameLocation_et_al"
class="wikilink" title="in-game location">in-game location</a>; that
means you can't use location methods at this point, but you can make any
changes you want before the map is read (e.g. change warps). See the
<a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="events page">events page</a> for help using events.

For example, this mod code edits the town map and adds an optional
`GetTile` helper method:

``` C#
/// <summary>The mod entry point.</summary>
internal sealed class ModEntry : Mod
{
    /// <inheritdoc />
    public override void Entry(IModHelper helper)
    {
        helper.Events.Content.AssetRequested += this.OnAssetRequested;
    }

    /// <inheritdoc cref="IContentEvents.AssetRequested"/>
    private void OnAssetRequested(object? sender, AssetRequestedEventArgs e)
    {
        if (e.Name.IsEquivalentTo("Maps/Town"))
        {
            e.Edit(asset =>
            {
                IAssetDataForMap editor = asset.AsMap();
                Map map = editor.Data;

                // your code here
            });
        }
    }

    /// <summary>Get a tile from the map.</summary>
    /// <param name="map">The map instance.</param>
    /// <param name="layerName">The name of the layer from which to get a tile.</param>
    /// <param name="tileX">The X position measured in tiles.</param>
    /// <param name="tileY">The Y position measured in tiles.</param>
    /// <returns>Returns the tile if found, else <c>null</c>.</returns>
    private Tile GetTile(Map map, string layerName, int tileX, int tileY)
    {
        Layer layer = map.GetLayer(layerName);
        Location pixelPosition = new Location(tileX * Game1.tileSize, tileY * Game1.tileSize);

        return layer.PickTile(pixelPosition, Game1.viewport.Size);
    }
}
```

Now you can make any changes you want to the map before it's loaded by
location. For example, you can...

- Add a custom tilesheet:
  ``` C#
  map.AddTileSheet(new TileSheet(
      id: "z_custom-tilesheet", // always prefix custom tilesheets with z_ to avoid reordering vanilla tilesheets
      map: map,
      imageSource: this.Helper.Content.GetActualAssetKey("assets/tilesheet.png", ContentSource.ModFolder), // get a unique asset name for local mod file which can be passed to the game
      sheetSize: new Size(32, 64), // the size in tiles for the tilesheet image
      tileSize: new Size(16)       // the size of each tile in pixels, should always be 16
  ));
  ```
- Manage map properties:
  ``` C#
  // get a property value
  string currentMusic = map.Properties.TryGetValue("Music", out PropertyValue rawMusic)
      ? rawMusic.ToString()
      : null;

  // add/replace a property
  map.Properties["Music"] = "MarlonsTheme";

  // delete a property
  map.Properties.Remove("Music");
  ```
- Manage tile properties:
  ``` C#
  // get tile
  Tile tile = this.GetTile(map, layerName: "Back", tileX: 10, tileY: 20);
  if (tile == null)
      return; // you should handle the tile not being there to avoid errors

  // get a property value
  string diggable = tile.TileIndexProperties.TryGetValue("Diggable", out PropertyValue rawDiggable) || tile.Properties.TryGetValue("Diggable", out rawDiggable)
      ? rawDiggable?.ToString()
      : null;

  // set a property
  tile.Properties["Diggable"] = "T";

  // delete a property
  tile.Properties.Remove("Diggable");
  ```
- Add new tiles:
  ``` C#
  int tileX = 10;
  int tileY = 20;
  Layer layer = map.GetLayer("Back");

  // add a static tile
  layer.Tiles[tileX, tileY] = new StaticTile(
      layer: layer,
      tileSheet: map.GetTileSheet("z_custom-tilesheet"),
      tileIndex: 100,            // the sprite index in the tilesheet
      blendMode: BlendMode.Alpha // should usually be Alpha
  );

  // add an animated tile
  layer.Tiles[tileX, tileY] = new AnimatedTile(
      layer: layer,
      tileFrames: new StaticTile[]
      {
          new StaticTile(...),
          new StaticTile(...),
          new StaticTile(...),
      },
      frameInterval: 100 // frame duration in milliseconds
  );
  ```
- Delete tiles:
  ``` C#
  layer.Tiles[tileX, tileY] = null;
  ```
- Apply tile transformations:
  ``` C#
  Tile tile = this.GetTile(map, layerName: "Back", tileX, tileY);
  tile.Properties["@Rotation"] = 45; // rotate it 45° clockwise
  tile.Properties["@Flip"] = 1; // flip the tile: 0 (normal), 1 (horizontal), 2 (vertical)
  ```

See also
<a href="Modding_Modder_Guide_APIs_Content#Edit_a_map" class="wikilink"
title="SMAPI&#39;s map edit helper">SMAPI's map edit helper</a>, which
lets you do things like merge a custom map area into the map.

### After location is loaded

After the
<a href="Modding_Modder_Guide_Game_Fundamentals#GameLocation_et_al"
class="wikilink" title="in-game location">in-game location</a> is
loaded, you can edit locations and their maps using the game's helpers.
Be careful doing this though: another mod (or sometimes the game itself)
may reload the location at any time, which would lose your changes if
you're not careful.

For example, within any
<a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="in-game events">in-game events</a> you can...

- Access the map to use the methods described above:
  ``` C#
  Map map = location.map;
  ```
- Manage tile properties:
  ``` C#
  Town town = (Town)Game1.getLocationFromName("Town");
  int tileX = 10;
  int tileY = 20;

  // get property value
  string diggable = town.doesTileHaveProperty(tileX, tileY, "Diggable", "Back");

  // set property value
  location.setTileProperty(tileX, tileY, "Back", "Diggable", "T");
  ```
- Manage tiles:
  ``` C#
  location.removeTile(tileX, tileY, "Back");
  ```

## Modder Help and Tricks

- Feel Free to visit the Stardew Valley Discord and ask for help if you
  need it in the \#Making Mods Section.
- Discord user foggywizard#7430 [annotated some screenshot guides for
  using Tiled](https://imgur.com/a/l1Ql16D). These include an annotated
  overview, how to find where the coordinates are, and how to rename a
  tilesheet.
- [Tutorial](https://stardewmodding.wiki.gg/wiki/Tutorial:How_Draylon_curves_his_cliffs):
  How Discord user Draylon curves his cliffs

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Карты" class="wikilink"
title="ru:Модификации:Карты">ru:Модификации:Карты</a>
<a href="zh_模组_地图" class="wikilink"
title="zh:模组:地图">zh:模组:地图</a>
