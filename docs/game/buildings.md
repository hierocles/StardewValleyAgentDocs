---
title: "Buildings"
wiki_source: "Modding:Buildings"
permalink: /Modding:Buildings/
category: game
tags: [buildings, format, for-c-mods]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the define custom buildings. This is an advanced
guide for mod developers.

## Format

You can create/edit buildings by editing the `Data/Buildings` asset.
Vanilla buildings have their names and descriptions defined as
<a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable strings">tokenizable strings</a> in
`Strings/Buildings`.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  building type.
- The value is a model with the fields listed below.

#### Required fields

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Name</samp><br />
<samp>Description</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the display name
and description (e.g. shown in the construction menu).</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture under the game's Content
folder.</p></td>
</tr>
</tbody>
</table>

#### Construction

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Builder</samp></p></td>
<td><p><em>(Optional)</em> The NPC from whom you can request
construction. The vanilla values are <a href="Carpenter&#39;s_Shop"
class="wikilink" title="Robin"><samp>Robin</samp></a> and <a
href="Wizard&#39;s_Tower#Buildings" class="wikilink"
title="Wizard"><samp>Wizard</samp></a>, but you can specify a different
name if a C# mod opens a construction menu for them. Defaults to
<samp>Robin</samp>. If set to null, it won't appear in any
menu.</p></td>
</tr>
<tr>
<td><p><samp>BuildCost</samp></p></td>
<td><p><em>(Optional)</em> The gold cost to construct the building.
Defaults to .</p></td>
</tr>
<tr>
<td><p><samp>BuildMaterials</samp></p></td>
<td><p><em>(Optional)</em> The materials you must provide to start
construction, as a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Unique_string_ID" class="wikilink"
title="unique string ID">unique string ID</a> for this entry within the
current list. Defaults to the <samp>ItemId</samp> if not
specified.</p></td>
</tr>
<tr>
<td><p><samp>ItemId</samp></p></td>
<td><p>The required item ID (qualified or unqualified).</p></td>
</tr>
<tr>
<td><p><samp>Amount</samp></p></td>
<td><p>The number of the item required.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>BuildDays</samp></p></td>
<td><p><em>(Optional)</em> The number of days needed to complete
construction (e.g. <samp>1</samp> for a building completed the next
day). If set to 0, construction finishes instantly. Defaults to
0.</p></td>
</tr>
<tr>
<td><p><samp>BuildCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the building should be available in the construction
menu. Defaults to always available.</p></td>
</tr>
<tr>
<td><p><samp>BuildMenuDrawOffset</samp></p></td>
<td><p><em>(Optional)</em> A pixel offset to apply to the building
sprite when drawn in the construction menu. Default none.</p></td>
</tr>
<tr>
<td><p><samp>AdditionalPlacementTiles</samp></p></td>
<td><p><em>(Optional)</em> The extra tiles to treat as part of the
building when placing it through the construction menu. For example, the
farmhouse uses this to make sure the stairs are clear. This consists of
a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>TileArea</samp></p></td>
<td><p>The tile area relative to the top-left corner of the building,
specified as an object with <samp>X</samp>, <samp>Y</samp>,
<samp>Width</samp>, and <samp>Height</samp> fields.</p></td>
</tr>
<tr>
<td><p><samp>OnlyNeedsToBePassable</samp></p></td>
<td><p><em>(Optional)</em> Whether this area allows tiles that would
normally not be buildable, so long as they are passable. For example,
this is used to ensure that an entrance is accessible. Default
false.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>IndoorItems</samp></p></td>
<td><p><em>(Optional)</em> The items to place in the building interior
when it's constructed or upgraded. This consists of a list of models
with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry within the current list.</p></td>
</tr>
<tr>
<td><p><samp>ItemId</samp></p></td>
<td><p>The <a href="#Custom_items" class="wikilink"
title="qualified item ID">qualified item ID</a> for the item to
place.</p></td>
</tr>
<tr>
<td><p><samp>Tile</samp></p></td>
<td><p>The tile position at which to place the item, specified as an
object with <samp>X</samp> and <samp>Y</samp> fields.</p></td>
</tr>
<tr>
<td><p><samp>Indestructible</samp></p></td>
<td><p><em>(Optional)</em> Whether to prevent the player from
destroying, picking up, or moving the item. Default false.</p></td>
</tr>
<tr>
<td><p><samp>ClearTile</samp></p></td>
<td><p><em>(Optional)</em> Whether to remove any item on the target
tile, except for one matching the indoor item's <samp>ItemId</samp>. The
previous contents of the tile will be moved into the lost and found if
applicable. Default true.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>MagicalConstruction</samp></p></td>
<td><p><em>(Optional)</em> Whether the building is magical. This changes
the carpenter menu to a mystic theme while this building's blueprint is
selected, and completes the construction instantly when placed.</p></td>
</tr>
<tr>
<td><p><samp>AddMailOnBuild</samp></p></td>
<td><p><em>(Optional)</em> A list of <a href="Modding_Mail_data"
class="wikilink" title="letter IDs">letter IDs</a> to send to all
players when the building is constructed for the first time.</p></td>
</tr>
</tbody>
</table>

#### Upgrades

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>BuildingToUpgrade</samp></p></td>
<td><p><em>(Optional)</em> The ID of the building for which this is an
upgrade, or omit to allow constructing it as a new building. For
example, the <a href="Coop" class="wikilink" title="Big Coop">Big
Coop</a> sets this to <samp>"Coop"</samp>. Any numbers of buildings can
be an upgrade for the same building, in which case the player can choose
one upgrade path.</p></td>
</tr>
<tr>
<td><p><samp>IndoorItemMoves</samp></p></td>
<td><p><em>(Optional)</em> When applied as an upgrade to an existing
building, the placed items in its interior to move when transitioning to
the new map. This is a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry within the current list.</p></td>
</tr>
<tr>
<td><p><samp>Source</samp></p></td>
<td><p>The tile position on which any item will be moved.</p></td>
</tr>
<tr>
<td><p><samp>Destination</samp></p></td>
<td><p>The tile position to which to move the item.</p></td>
</tr>
<tr>
<td><p><samp>Size</samp></p></td>
<td><p><em>(Optional)</em> The tile size of the area to move, specified
as a model with <samp>X</samp> and <samp>Y</samp> fields. Defaults to a
1×1 area. If this is multiple tiles, the <samp>Source</samp> and
<samp>Destination</samp> specify the top-left coordinate of the
area.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>UpgradeSignTile</samp></p></td>
<td><p><em>(Optional)</em> The tile position relative to the top-left
corner of the building where the upgrade sign will be placed when Robin
is building an upgrade, in the form <samp>"&lt;x&gt;, &lt;y&gt;"</samp>.
Defaults to approximately <samp>"5, 1"</samp> if the building interior
type is <samp>Shed</samp>, else <samp>"0, 0"</samp>.</p></td>
</tr>
<tr>
<td><p><samp>UpgradeSignHeight</samp></p></td>
<td><p><em>(Optional)</em> The pixel height of the upgrade sign when
Robin is building an upgrade. Defaults to 0.</p></td>
</tr>
</tbody>
</table>

#### Exterior behavior

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Size</samp></p></td>
<td><p><em>(Optional)</em> The building's width and height when
constructed, measured in tiles. Defaults to a 1 x 1 area.</p></td>
</tr>
<tr>
<td><p><samp>CollisionMap</samp></p></td>
<td><p><em>(Optional)</em> An ASCII text block which indicates which of
the building's tiles the players can walk onto, where each character can
be <samp>X</samp> (blocked) or <samp>O</samp> (passable). Defaults to
all tiles blocked.</p>
<p>For example, a <a href="stable" class="wikilink"
title="stable">stable</a> covers a 2x4 tile area with the front two
tiles passable:</p>
<pre><code>XXXX
XOOX</code></pre>
<p>When the collision map is parsed, leading/trailing whitespace is
trimmed (both for the entire map and for each line). In JSON, you can
specify it in two forms:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">// single line with \n line breaks</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;CollisionMap&quot;</span><span class="op">:</span> <span class="st">&quot;XXXX</span><span class="sc">\n</span><span class="st">XOOX&quot;</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="co">// multi-line with optional indentation</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;CollisionMap&quot;</span><span class="op">:</span> <span class="st">&quot;</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    XXXX</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    XOOX</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>HumanDoor</samp></p></td>
<td><p><em>(Optional)</em> The position of the door that can be clicked
to warp into the building interior. This is measured in tiles relative
to the top-left corner tile. Defaults to disabled.</p></td>
</tr>
<tr>
<td><p><samp>AnimalDoor</samp></p></td>
<td><p><em>(Optional)</em> The position and size of the door that
animals use to enter/exit the building, if the building interior is an
animal location, specified as an object with <samp>X</samp>,
<samp>Y</samp>, <samp>Width</samp>, and <samp>Height</samp> fields. This
is measured in tiles relative to the top-left corner tile. Defaults to
disabled.</p></td>
</tr>
<tr>
<td><p><samp>AnimalDoorOpenDuration</samp><br />
<samp>AnimalDoorCloseDuration</samp></p></td>
<td><p><em>(Optional)</em> The duration of the open/close animation for
the animal door, measured in milliseconds. If omitted, the door switches
to the open/closed state instantly.</p></td>
</tr>
<tr>
<td><p><samp>AnimalDoorOpenSound</samp><br />
<samp>AnimalDoorCloseSound</samp></p></td>
<td><p><em>(Optional)</em> The sound which is played once each time the
animal door is opened/closed. Disabled by default.</p></td>
</tr>
</tbody>
</table>

#### Exterior appearance

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>SourceRect</samp></p></td>
<td><p><em>(Optional)</em> The building's pixel area within the
<samp>Texture</samp>, specified as an object with <samp>X</samp>,
<samp>Y</samp>, <samp>Width</samp>, and <samp>Height</samp> fields.
Defaults to the entire texture.</p></td>
</tr>
<tr>
<td><p><samp>Skins</samp></p></td>
<td><p><em>(Optional)</em> The appearances which can be selected from
Robin's menu (like stone/plank/log <a href="cabin" class="wikilink"
title="cabin">cabins</a>), in addition to the default appearance based
on <samp>Texture</samp>. This consists of a list of models with these
fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for the
skin.</p></td>
</tr>
<tr>
<td><p><samp>Name</samp><br />
<samp>Description</samp></p></td>
<td><p><a href="Modding_Tokenizable_strings" class="wikilink"
title="Tokenizable strings">Tokenizable strings</a> for the skin's
display name and description.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture under the game's Content
folder.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this skin should be available to apply. This doesn't
change buildings which already have it applied. Defaults to always
true.</p></td>
</tr>
<tr>
<td><p><samp>BuildDays</samp><br />
<samp>BuildCost</samp><br />
<samp>BuildMaterials</samp></p></td>
<td><p><em>(Optional)</em> If set, overrides the equivalent field in the
building data.</p></td>
</tr>
<tr>
<td><p><samp>ShowAsSeparateConstructionEntry</samp></p></td>
<td><p><em>(Optional)</em> Whether this skin should be shown as a
separate building option in the construction menu (like cabins). Default
false.</p></td>
</tr>
<tr>
<td><p><samp>Metadata</samp></p></td>
<td><p><em>(Optional)</em> Equivalent to the <samp>Metadata</samp> field
on the building. Properties defined in this field are added to the
building's metadata when this skin is active, overwriting the previous
property with the same name if applicable. Default none.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>FadeWhenBehind</samp></p></td>
<td><p><em>(Optional)</em> Whether the building should become
semi-transparent when the player is behind it. Default true.</p></td>
</tr>
<tr>
<td><p><samp>DrawOffset</samp></p></td>
<td><p><em>(Optional)</em> A pixel offset applied to the building
sprite's placement in the world. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>SeasonOffset</samp></p></td>
<td><p><em>(Optional)</em> A pixel offset to apply each season. This is
applied to the <samp>SourceRect</samp> position by multiplying the
offset by 0 (spring), 1 (summer), 2 (fall), or 3 (winter). Default 0, so
all seasons use the same source rect.</p></td>
</tr>
<tr>
<td><p><samp>SortTileOffset</samp></p></td>
<td><p><em>(Optional)</em> A Y tile offset applied when figuring out
render layering. For example, a value of <samp>2.5</samp> will treat the
building as if it was 2.5 tiles further up the screen for the purposes
of layering. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>AllowsFlooringUnderneath</samp></p></td>
<td><p><em>(Optional)</em> Whether flooring can be placed underneath,
and when the building is placed, if it will leave flooring beneath it.
Default true.</p></td>
</tr>
<tr>
<td><p><samp>DrawLayers</samp></p></td>
<td><p><em>(Optional)</em> A list of textures to draw over or behind the
building, with support for conditions and animations. This consists of a
list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry within the current list.</p></td>
</tr>
<tr>
<td><p><samp>SourceRect</samp></p></td>
<td><p>The pixel area within the <samp>texture</samp> to draw, formatted
like <samp>"&lt;x&gt; &lt;y&gt; &lt;width&gt; &lt;height&gt;"</samp>. If
the overlay is animated via <samp>FrameCount</samp>, this is the area of
the first frame.</p></td>
</tr>
<tr>
<td><p><samp>DrawPosition</samp></p></td>
<td><p>The position at which to draw the top-left corner of the texture,
relative to the building's top-left corner. Measured in pixels.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p><em>(Optional)</em> The asset name of the texture to draw.
Defaults to the building's default <samp>Texture</samp> field.</p></td>
</tr>
<tr>
<td><p><samp>DrawInBackground</samp></p></td>
<td><p><em>(Optional)</em> Whether to draw the texture behind the
building sprite (i.e. underlay) instead of over it.</p></td>
</tr>
<tr>
<td><p><samp>SortTileOffset</samp></p></td>
<td><p><em>(Optional)</em> A Y tile offset applied when figuring out
render layering. For example, a value of <samp>2.5</samp> will treat the
texture as if it was 2.5 tiles further up the screen for the purposes of
layering. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>OnlyDrawIfChestHasContents</samp></p></td>
<td><p><em>(Optional)</em> The ID of a chest defined in the
<samp>Chests</samp> field which must contain items. If it's empty, this
overlay won't be rendered. Default none.</p></td>
</tr>
<tr>
<td><p><samp>FrameCount</samp><br />
<samp>FramesPerRow</samp><br />
<samp>FrameDuration</samp></p></td>
<td><p><em>(Optional)</em> If <samp>FrameCount</samp> is more than one,
the building overlay will be animated automatically. For each frame, the
<samp>SourceRect</samp> will be offset by its <samp>Width</samp> to the
right up to <samp>FramesPerRow - 1</samp> times, and then down by its
<samp>Height</samp>. Each frame will be rendered on-screen for
<samp>FrameDuration</samp> milliseconds before switching to the next
frame.</p>
<p>For example, if you set <samp>FrameCount</samp> to 6 and
<samp>FramesPerRow</samp> to 3, the building will expect the frames to
be laid out like this in the spritesheet (where frame 1 matches
<samp>SourceRect</samp>):</p>
<pre><code>┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
└───┴───┴───┘</code></pre></td>
</tr>
<tr>
<td><p><samp>AnimalDoorOffset</samp></p></td>
<td><p><em>(Optional)</em> A pixel offset applied to the draw layer when
the animal door is open. While the door is opening, the percentage open
is applied to the offset (e.g. 50% open = 50% offset).</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>DrawShadow</samp></p></td>
<td><p><em>(Optional)</em> Whether to draw an automatic shadow along the
bottom edge of the building's sprite. Default true.</p></td>
</tr>
</tbody>
</table>

#### Interior

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>IndoorMap</samp></p></td>
<td><p><em>(Optional)</em> The name of the map asset under
<samp>Maps</samp> to load for the building interior. For example,
<samp>"Shed"</samp> will load the <a href="shed" class="wikilink"
title="shed">shed</a>'s <samp>Maps/Shed</samp> map.</p></td>
</tr>
<tr>
<td><p><samp>IndoorMapType</samp></p></td>
<td><p><em>(Optional)</em> The full name of the C# location class which
will manage the building's interior location. This must be one of the
vanilla types to avoid a crash when saving. There are too many to list
here, but the most useful types are likely...</p>
<ul>
<li><samp>StardewValley.AnimalHouse</samp>;</li>
<li><samp>StardewValley.Locations.Cabin</samp>;</li>
<li><samp>StardewValley.Locations.Cellar</samp>;</li>
<li><samp>StardewValley.Locations.DecoratableLocation</samp>;</li>
<li><samp>StardewValley.Locations.FarmCave</samp>;</li>
<li><samp>StardewValley.Locations.FarmHouse</samp>;</li>
<li><samp>StardewValley.Shed</samp>;</li>
<li>and <samp>StardewValley.SlimeHutch</samp>.</li>
</ul>
<p>Defaults to the generic <samp>StardewValley.GameLocation</samp>
class.</p></td>
</tr>
<tr>
<td><p><samp>NonInstancedIndoorLocation</samp></p></td>
<td><p><em>(Optional)</em> The name of the existing global location to
treat as the building's interior, like <samp>FarmHouse</samp> and
<samp>Greenhouse</samp> for their buildings.</p>
<p>Each location can only be used by one building. If the location is
already in use (e.g. because the player has two of this building), each
subsequent building will use the <samp>IndoorMap</samp> and
<samp>IndoorMapType</samp> instead. For example, the first greenhouse
will use the global <samp>Greenhouse</samp> location, and any subsequent
greenhouse will use a separate instanced location.</p></td>
</tr>
<tr>
<td><p><samp>MaxOccupants</samp></p></td>
<td><p><em>(Optional)</em> The maximum number of animals who can live in
this building.</p></td>
</tr>
<tr>
<td><p><samp>AllowAnimalPregnancy</samp></p></td>
<td><p><em>(Optional)</em> Whether animals can get pregnant and produce
offspring in this building. Default false.</p></td>
</tr>
<tr>
<td><p><samp>ValidOccupantTypes</samp></p></td>
<td><p><em>(Optional)</em> A list of building IDs whose animals to allow
in this building too. For example, <code>[ "Barn", "Coop" ]</code> will
allow <a href="barn" class="wikilink" title="barn">barn</a> and <a
href="coop" class="wikilink" title="coop">coop</a> animals in this
building. Default none.</p></td>
</tr>
</tbody>
</table>

Note: the player's entry position after entering the building will be 1
tile North of the first warp in the location's warp list.

#### Item processing

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>HayCapacity</samp></p></td>
<td><p><em>(Optional)</em> The amount of hay that can be stored in this
building. If built on the <a href="The_Farm" class="wikilink"
title="farm">farm</a>, this works just like <a href="silo"
class="wikilink" title="silo">silos</a> and contributes to the farm's
available hay.</p></td>
</tr>
<tr>
<td><p><samp>ItemConversions</samp></p></td>
<td><p><em>(Optional)</em> The item processing rules which take input
items and convert them into output items using the inventories defined
by <samp>Chests</samp>. This consists of a list of models with these
fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
rule within the current list.</p></td>
</tr>
<tr>
<td><p><samp>RequiredTags</samp></p></td>
<td><p>A list of <a href="Modding_Context_tags" class="wikilink"
title="context tags">context tags</a> to match against an input item. An
item must have <em>all</em> of these tags to be accepted.</p></td>
</tr>
<tr>
<td><p><samp>SourceChest</samp></p></td>
<td><p>The ID of the inventory defined in <samp>Chests</samp> from which
to take input items.</p></td>
</tr>
<tr>
<td><p><samp>DestinationChest</samp></p></td>
<td><p>The ID of the inventory defined in <samp>Chests</samp> in which
to store output items.</p></td>
</tr>
<tr>
<td><p><samp>ProducedItems</samp></p></td>
<td><p>The output items produced when an input item is converted. This
consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported by machine output.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that the item will be
produced, as a value between 0 (never drops) and 1 (always drops).
Default 1 (100% chance).</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>RequiredCount</samp></p></td>
<td><p><em>(Optional)</em> The number of the input item to consume.
Default 1.</p></td>
</tr>
<tr>
<td><p><samp>MaxDailyConversions</samp></p></td>
<td><p><em>(Optional)</em> The maximum number of the input item which
can be processed each day. Each conversion rule has its own separate
maximum (e.g. if you have two rules each with a max of 1, then you can
convert one of each daily). Set to -1 to allow unlimited conversions.
Default 1.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Chests</samp></p></td>
<td><p><em>(Optional)</em> The input/output inventories that can be
accessed from a tile on the building exterior. The allowed items are
defined by the separate <samp>ItemConversions</samp> field. This is a
list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
chest within the current list.</p>
<p>This is referenced from the <samp>ItemConversions</samp>
field.</p></td>
</tr>
<tr>
<td><p><samp>Type</samp></p></td>
<td><p>The inventory type. This must be one of:</p>
<ul>
<li><samp>Chest</samp>: show a normal chest UI on click.</li>
<li><samp>Collect</samp>: provides items for the player to collect.
Clicking the tile will do nothing (if empty), grab the item directly (if
it only contains one item), else show a grab-only inventory UI.</li>
<li><samp>Load</samp>: lets the player add items for the building to
process.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Sound</samp></p></td>
<td><p><em>(Optional)</em> The sound to play once when the player clicks
the chest.</p></td>
</tr>
<tr>
<td><p><samp>InvalidItemMessage</samp><br />
<samp>InvalidCountMessage</samp><br />
<samp>ChestFullMessage</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> to
show when the player tries to add an item to the chest when...</p>
<ul>
<li>it isn't a supported item;</li>
<li>it's supported but they don't have enough in their inventory;</li>
<li>the chest has no more room to accept it.</li>
</ul>
<p>If omitted, the player interaction is ignored with no message
shown.</p></td>
</tr>
<tr>
<td><p><samp>InvalidItemMessageCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether <samp>InvalidItemMessage</samp> should be shown. This
can use item-related queries like <samp>ITEM_TYPE</samp>. Defaults to
always true.</p></td>
</tr>
<tr>
<td><p><samp>DisplayTile</samp></p></td>
<td><p><em>(Optional)</em> The chest's position on the building
exterior, measured in tiles from the top-left corner of the building,
specified in the form <samp>"&lt;x&gt;, &lt;y&gt;"</samp>. This affects
the position of the 'item ready to collect' bubble. If omitted, the
bubble is disabled.</p></td>
</tr>
<tr>
<td><p><samp>DisplayHeight</samp></p></td>
<td><p><em>(Optional)</em> If <samp>DisplayTile</samp> is set, the
chest's tile height like <samp>1.5</samp>.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

#### Tile interactions

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ActionTiles</samp></p></td>
<td><p><em>(Optional)</em> A list of tiles which the player can click to
trigger an <samp>Action</samp> <a href="Modding_Maps" class="wikilink"
title="map tile property">map tile property</a>. This consists of a list
of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry within the current list.</p></td>
</tr>
<tr>
<td><p><samp>Tile</samp></p></td>
<td><p>The tile position, relative to the building's top-left corner
tile.</p></td>
</tr>
<tr>
<td><p><samp>Action</samp></p></td>
<td><p>The <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the action to
perform, excluding the <samp>Action</samp> prefix. For example,
<samp>"Dialogue Hi there @!"</samp> to show a messagebox like "<em>Hi
there &lt;player name&gt;!</em>". The tokenizable string is expected
before the action is raised. See the <a
href="Modding_Maps#Tile_properties_2" class="wikilink"
title="list of tile properties">list of tile properties</a> for useful
<samp>Action</samp> values.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>DefaultAction</samp></p></td>
<td><p><em>(Optional)</em> The default tile action if the clicked tile
isn't in <samp>ActionTiles</samp>. Default none.</p></td>
</tr>
<tr>
<td><p><samp>TileProperties</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Maps" class="wikilink"
title="map tile properties">map tile properties</a> to set. This
consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry within the current list.</p></td>
</tr>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p>The tile property name to set.</p></td>
</tr>
<tr>
<td><p><samp>Value</samp></p></td>
<td><p><em>(Optional)</em> The tile property value to set, or omit to
set a null value.</p></td>
</tr>
<tr>
<td><p><samp>Layer</samp></p></td>
<td><p>The name of the map layer whose tiles to change.</p></td>
</tr>
<tr>
<td><p><samp>TileArea</samp></p></td>
<td><p>The tiles to which to add the property, relative to the top-left
corner of the building's collision box. This is specified as an object
with <samp>X</samp>, <samp>Y</samp>, <samp>Width</samp>, and
<samp>Height</samp> fields.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>AdditionalTilePropertyRadius</samp></p></td>
<td><p><em>(Optional)</em> When checking whether the player clicked on a
<samp>TileProperties</samp> tile, an added distance around the building
at which tile locations may be placed. Default 0, so only tile
properties within the normal building bounds will work.</p></td>
</tr>
</tbody>
</table>

#### Advanced

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Metadata</samp></p></td>
<td><p><em>(Optional)</em> A list of custom properties applied to the
building, which can optionally be overridden per-skin in the
<samp>Skins</samp> field. Default none.</p>
<p>The base game recognizes these properties:</p>
<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ChimneyPosition: &lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p><em>(Optional)</em> The pixel position at which to place a
chimney on the building exterior, relative to the top-left corner of the
sprite. This will apply the same logic as the farmhouse chimney (e.g.
producing smoke if there's a lit fireplace inside the
building).</p></td>
</tr>
<tr>
<td><p><samp>ChimneyPosition[upgrade level]: &lt;x&gt;
&lt;y&gt;</samp></p></td>
<td><p><em>(Optional, for farmhouses/cabins only)</em> Override
<samp>ChimneyPosition</samp> for the given upgrade level, starting from
0 for the initial farmhouse/cabin. If there's no override for the
current upgrade level, the highest override for a lower upgrade level is
used (if any). For example, <samp>ChimneyPosition3</samp> would be used
for the third house upgrade (and the fourth if there's no
<samp>ChimneyPosition4</samp>).</p></td>
</tr>
</tbody>
</table>
<p>This can also contain arbitrary custom properties, which C# mods can
read using <samp>building.GetMetadata(key)</samp>.</p></td>
</tr>
<tr>
<td><p><samp>NameForGeneralType</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the display name which represents the general building type, like 'Coop'
for a Deluxe Coop. For example, this can be shown in Robin's
started-construction dialogue. If omitted, it defaults to the
<samp>Name</samp> field.</p></td>
</tr>
<tr>
<td><p><samp>BuildingType</samp></p></td>
<td><p><em>(Optional)</em> The full name of the C# type to instantiate
for the building instance. Defaults to a generic <samp>Building</samp>
instance.</p>
<p><strong>⚠ Caution:</strong> this is meant to support vanilla building
types like <samp>StardewValley.Shed</samp>. Setting this to a
non-vanilla type will cause a crash when it's written to the save file,
and may cause crashes in multiplayer. If you need custom behavior,
consider handling it in C# based on the building type instead of
creating a custom subclass; otherwise you'll need a framework mod like
to handle serialization and multiplayer sync.</p></td>
</tr>
<tr>
<td><p><samp>ModData</samp></p></td>
<td><p><em>(Optional)</em> A string → string lookup of arbitrary
<samp>modData</samp> values to attach to the building when it's
constructed.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

## For C# mods

The following methods are available to simplify common operations on
buildings:

<table>
<thead>
<tr>
<th><p>type</p></th>
<th><p>method</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="13"><p><samp>Building</samp></p></td>
<td><p><samp>CreateInstanceFromId</samp></p></td>
<td><p>Create a building instance from its type ID in
<samp>Data/Buildings</samp>. For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>Building shippingBin <span class="op">=</span> Building<span class="op">.</span><span class="fu">CreateInstanceFromId</span><span class="op">(</span><span class="st">&quot;Shipping Bin&quot;</span><span class="op">,</span> Vector2<span class="op">.</span><span class="fu">Zero</span><span class="op">);</span> <span class="co">// creates an instance of StardewValley.Buildings.ShippingBin</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>FinishConstruction</samp></p></td>
<td><p>If the building is being constructed or upgrade, instantly finish
doing so.</p></td>
</tr>
<tr>
<td><p><samp>GetData</samp><br />
<samp>TryGetData</samp></p></td>
<td><p>Get the data for the building's type from
<samp>Data/Building</samp>.</p></td>
</tr>
<tr>
<td><p><samp>GetIndoors</samp></p></td>
<td><p>Get the location within this building, if applicable.</p></td>
</tr>
<tr>
<td><p><samp>GetIndoorsName</samp></p></td>
<td><p>Get the unique name of the location within this building, if
applicable.</p></td>
</tr>
<tr>
<td><p><samp>GetMetadata</samp></p></td>
<td><p>Get a value from <a href="Modding_Buildings" class="wikilink"
title="the Metadata field in Data/Buildings">the <samp>Metadata</samp>
field in <samp>Data/Buildings</samp></a> for this building.</p></td>
</tr>
<tr>
<td><p><samp>GetPaintDataKey</samp></p></td>
<td><p>Get the key in <samp>Data/PaintData</samp> for this building, if
it has any.</p></td>
</tr>
<tr>
<td><p><samp>GetParentLocation</samp></p></td>
<td><p>Get the location which contains this building.</p></td>
</tr>
<tr>
<td><p><samp>HasIndoors</samp></p></td>
<td><p>Get whether the building has an interior location.</p></td>
</tr>
<tr>
<td><p><samp>HasIndoorsName</samp></p></td>
<td><p>Get whether the building has an interior location and its unique
name matches the given value (like
<code>building.HasIndoorsName("FarmHouse")</code>).</p></td>
</tr>
<tr>
<td><p><samp>IsInCurrentLocation</samp></p></td>
<td><p>Get whether the building is in the same location as the current
player.</p></td>
</tr>
<tr>
<td><p><samp>ReloadBuildingData</samp></p></td>
<td><p>Apply the latest data in <samp>Data/Buildings</samp> to this
building.</p></td>
</tr>
<tr>
<td><p><samp>UpdateTransparency</samp></p></td>
<td><p>Update the building transparency on tick for the local player's
position.</p>
<p>This method mainly exists to let mods override/patch the transparency
logic.</p></td>
</tr>
<tr>
<td rowspan="7"><p><samp>Cabin</samp><br />
<samp>FarmHouse</samp></p></td>
<td><p><samp>GetCellar</samp></p></td>
<td><p>Get the <a href="Farmhouse#Upgrades" class="wikilink"
title="cellar">cellar</a> location linked to this cabin, if
any.</p></td>
</tr>
<tr>
<td><p><samp>CanAssignFarmhand</samp><br />
<samp>AssignFarmhand</samp></p></td>
<td><p><em>(Cabin only)</em> Check whether the cabin is available to
assign to a farmhand, or perform the assignment.</p></td>
</tr>
<tr>
<td><p><samp>HasOwner</samp></p></td>
<td><p>Get whether the home has an assigned player, regardless of
whether they've finished creating their character.</p></td>
</tr>
<tr>
<td><p><samp>OwnerId</samp></p></td>
<td><p>Get the unique ID of the player who owns this home, if
any.</p></td>
</tr>
<tr>
<td><p><samp>IsOwnedByCurrentPlayer</samp></p></td>
<td><p>Get whether the cabin belongs to the current player.</p></td>
</tr>
<tr>
<td><p><samp>IsOwnerActivated</samp></p></td>
<td><p>Get whether the home has an assigned player and they've finished
creating their character.</p></td>
</tr>
<tr>
<td><p><samp>HasNpcSpouse</samp></p></td>
<td><p>Get whether the player who owns this home is married to any NPC
(when used like <samp>HasNpcSpouse()</samp>) or a specific NPC (like
<samp>HasNpcSpouse(name)</samp>). This also replaces
<samp>shouldShowSpouseRoom()</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Farm</samp></p></td>
<td><p><samp>GetMainFarmHouse</samp></p></td>
<td><p>Get the main <a href="farmhouse" class="wikilink"
title="farmhouse">farmhouse</a> building.</p></td>
</tr>
<tr>
<td rowspan="5"><p><samp>GameLocation</samp></p></td>
<td><p><samp>AddDefaultBuildings</samp></p></td>
<td><p>Can be overridden to add custom buildings when the location is
created and/or loaded. These can either be re-added whenever they're
missing (like the vanilla farmhouse), or only built once on save
creation (like the vanilla pre-built cabins).</p></td>
</tr>
<tr>
<td><p><samp>GetContainingBuilding</samp></p></td>
<td><p>Get the building instance which contains this location (like the
cabin for a cabin interior), if applicable.</p></td>
</tr>
<tr>
<td><p><samp>GetInstancedBuildingInteriors</samp></p></td>
<td><p>Get all building interiors within this location which are
instanced to the building (i.e. not in <samp>Game1.locations</samp>
separately).</p></td>
</tr>
<tr>
<td><p><samp>OnBuildingConstructed</samp><br />
<samp>OnBuildingMoved</samp><br />
<samp>OnBuildingDemolished</samp></p></td>
<td><p>These methods are called for all players when any player
constructs, moves, or demolishes a building.</p></td>
</tr>
<tr>
<td><p><samp>OnParentBuildingUpgraded</samp></p></td>
<td><p>Called when the building containing this location is upgraded, if
applicable.</p></td>
</tr>
</tbody>
</table>

- All buildings have an `id` field, which uniquely identifies each
  building in the world.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Чертежи" class="wikilink"
title="ru:Модификации:Чертежи">ru:Модификации:Чертежи</a>
<a href="zh_模组_建筑" class="wikilink"
title="zh:模组:建筑">zh:模组:建筑</a>
