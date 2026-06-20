---
title: "Locations"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, locations]
---
### Locations

#### Terrain, trees, and crops

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>artifactSpots</samp></p></td>
<td><p>| Spawn an <a href="Artifact_Spot" class="wikilink"
title="artifact spot">artifact spot</a> in each empty tile around the
player.</p></td>
<td><p>|<a href="#artifactSpots" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearfarm</samp></p></td>
<td><p>| Removes nearly everything from the Farm map such as grass,
trees, debris, paths, and placed objects (including working machines and
filled chests.)</p></td>
<td><p>|<a href="#clearfarm" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dayupdate</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dayupdate</code> [I:number]</p>
<p>Runs the DayUpdate for the current location the specified number of
times. If the number of updates is not specified, it will default to 1.
This simulates days passing for some things such as grass and fruit
trees growing or fish reproducing in ponds. Other things may not
progress the full amount; for example crop growth only advances one day
because sprinklers will not be triggered and the <a href="#growcrops"
class="wikilink" title="growcrops">growcrops</a> command should be used
for that instead.</p></td>
<td><p>|<a href="#dayupdate" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fruittrees</samp></p></td>
<td><p>| Adds a month of growth to all fruit trees in the current
location, causing even newly-planted saplings to instantly
mature.</p></td>
<td><p>|<a href="#fruittrees" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>grass</samp></p></td>
<td><p>| Spawns long grass on all available tiles in the current
location.</p></td>
<td><p>|<a href="#grass" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>growcrops</samp></p></td>
<td><p>| <em>Syntax</em>: <code>growcrops</code> &lt;I:number&gt;</p>
<p>Grows all crops in the current location the specified number of
days.</p></td>
<td><p>|<a href="#growcrops" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>growgrass</samp></p></td>
<td><p>| <em>Syntax</em>: <code>growgrass</code> &lt;I:number&gt;</p>
<p>Grows long grass the specified number of times in the current
location. This will cause already-placed grass to spread but will not
necessarily create grass in clear areas.</p></td>
<td><p>|<a href="#growgrass" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>growwildtrees</samp></p></td>
<td><p>| Grows all wild trees (such as Oak) in the current location to
maturity. This command may be broken as it can de-age fully grown trees,
even ones with existing tappers.</p></td>
<td><p>|<a href="#growwildtrees" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>localinfo</samp></p></td>
<td><p>| Outputs counts of grass, trees, other terrain features,
objects, and temporary sprites for the current location. May be
broken.</p></td>
<td><p>|<a href="#localinfo" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>mushroomtrees</samp></p></td>
<td><p>| Turns all wild trees in the current location into mushroom
trees.</p></td>
<td><p>|<a href="#mushroomtrees" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>r</samp><br />
<samp>resetForPlayerEntry</samp></p></td>
<td><p>| Resets current location which essentially simulates the player
leaving and reentering. Most noticeable effect is the restarting of
music tracks.</p></td>
<td><p>|<a href="#r" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removedebris</samp></p></td>
<td><p>| Removes all dropped items from the current location.</p></td>
<td><p>|<a href="#removedebris" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removedirt</samp></p></td>
<td><p>| Removes (<em>i.e.,</em> untills) all tilled dirt in the current
location.<br />
<strong>Warning: this includes removing any currently-planted crops
(including fully-grown ones).</strong></p></td>
<td><p>|<a href="#removedirt" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removelargetf</samp><br />
<samp>removeLargeTerrainFeature</samp></p></td>
<td><p>| Removes all large terrain features (such as bushes) from the
current location.</p></td>
<td><p>|<a href="#removelargetf" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removeterrainfeatures</samp><br />
<samp>removetf</samp></p></td>
<td><p>| Removes all (small) terrain features such as grass and tilled
dirt from the current location.<br />
<strong>Warning: this includes removing any currently-planted crops
(including fully-grown ones).</strong></p></td>
<td><p>|<a href="#removeterrainfeatures" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>spawnweeds</samp></p></td>
<td><p>| <em>Syntax</em>: <code>spawnweeds</code> &lt;I:number&gt;</p>
<p>Spawns weeds the specified number of times. This will cause
already-placed weeds to spread but will not necessarily create new weeds
in clear areas.</p></td>
<td><p>|<a href="#spawnweeds" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>spreaddirt</samp></p></td>
<td><p>| Tills all unoccupied diggable tiles in the current
location.</p></td>
<td><p>|<a href="#spreaddirt" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>spreadseeds</samp></p></td>
<td><p>| <em>Syntax</em>: <code>spreadseeds</code> &lt;I:seedID&gt;</p>
<p>Plants specified seed in all tilled dirt in the current location. The
argument is the <a href="Modding_Objects" class="wikilink"
title="object ID">object ID</a> for the seed item. Out of season crops
can be planted this way but will not survive outside of the
greenhouse.<br />
<strong>Warning: this will replace any currently-planted crops
(including fully-grown ones) with the new seeds.</strong></p>
<p><em>Example:</em> <code>debug spreadseeds 472</code> would plant <a
href="Parsnip" class="wikilink" title="parsnips">parsnips</a> on all
hoed dirt tiles.</p></td>
<td><p>|<a href="#spreadseeds" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>water</samp></p></td>
<td><p>| Waters all tilled soil on the current map.</p></td>
<td><p>|<a href="#water" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>watercolor</samp></p></td>
<td><p>| <em>Syntax</em>: <code>watercolor</code>
&lt;I:R&gt;,&lt;I:G&gt;,&lt;I:B&gt;</p>
<p>Tints the water color for the current location. The parameters are
red, green, and blue components and the actual RGBA color used will be
(R/2, G/2, B/2, 127). This affects fishing ponds as well as lakes,
rivers, etc., but the effect is temporary and the color will reset to
normal if you leave and re-enter the map.</p></td>
<td><p>|<a href="#watercolor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>whereore</samp></p></td>
<td><p>| Outputs (to the SMAPI console) the coordinates of any "shiny
spots" suitable for panning on the current map. Will output <samp>{X:0
Y:0}</samp> if there are no active panning spots.</p></td>
<td><p>|<a href="#whereore" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Objects and lights

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearfurniture</samp></p></td>
<td><p>| Removes all furniture from the current location. Can be used in
a farmhouse/cabin, or outside the farmhouse as well.</p></td>
<td><p>|<a href="#clearfurniture" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearlightglows</samp></p></td>
<td><p>| Removes all light glows from the current location.</p></td>
<td><p>|<a href="#clearlightglows" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fencedecay</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fencedecay</code> &lt;I:amount&gt;</p>
<p>Ages all fences in the current location the specified amount of
days.</p>
<p><em>Example:</em> <code>debug fencedecay 60</code> would age all
fences by 60 days which would break any basic Wood Fences (their base
health is 54-58 days).</p></td>
<td><p>|<a href="#fencedecay" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fillwithobject</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fillwithobject</code>
&lt;I:itemID&gt;,[S:isBigCraftable]</p>
<p>Places the specified item on all open tiles in the current location.
The first argument is the <a href="Modding_Objects" class="wikilink"
title="object">object</a> or <a href="Modding_Big_craftables"
class="wikilink" title="big craftable">big craftable</a> ID. If the
second argument is "<samp>true</samp>", the ID will be interpreted as a
craftable, but if it is anything else (or missing) the ID will be
interpreted as an object. Note that many objects spawned this way cannot
be easily removed.</p>
<p><em>Example:</em> <code>debug fillwithobject 13 true</code> would
fill the map with <a href="Furnace" class="wikilink"
title="furnaces">furnaces</a>.</p></td>
<td><p>|<a href="#fillwithobject" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>readyforharvest</samp><br />
<samp>rfh</samp></p></td>
<td><p>| <em>Syntax</em>: <code>readyforharvest</code>
&lt;I:X&gt;,&lt;I:Y&gt;</p>
<p>Sets the machine at the specified coordinates to finish processing at
the next clock update. If used to target a rock in the mine, quarry,
etc. the rock's health will be reduced such that it only needs 1 more
hit to break. A mod such as <a
href="https://www.nexusmods.com/stardewvalley/mods/679">Debug Mode</a>
may be useful for getting coordinates.</p></td>
<td><p>|<a href="#readyforharvest" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>listLights</samp></p></td>
<td><p>| Show debug info about all currently active light
sources.</p></td>
<td><p>|<a href="#listLights" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removefurniture</samp></p></td>
<td><p>| Removes all furniture from the current location. Similar to <a
href="#clearfurniture" class="wikilink"
title="clearfurniture">clearfurniture</a> but will also work in other
decoratable locations such as sheds.</p></td>
<td><p>|<a href="#removefurniture" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removelights</samp></p></td>
<td><p>| Removes all light sources from the current location. This is
temporary and they will be restored if the location is reset or
re-entered.</p></td>
<td><p>|<a href="#removelights" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removeobjects</samp></p></td>
<td><p>| Removes all placed objects from the current location. This
includes things like fences, machines, and chests, but does not include
flooring or long grass.</p></td>
<td><p>|<a href="#removeobjects" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Farm buildings

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>build</samp></p></td>
<td><p>| <em>Syntax</em>: <code>build</code>
&lt;S:Name&gt;,[I:X],[I:Y]</p>
<p>Builds the specified building at the given coordinates. Names are
case-insensitive, and will list fuzzy matches if an exact match isn't
found. If the name includes spaces, quote them (e.g. <samp>"Junimo
Hut"</samp>). If the coordinates are not specified, it will build just
to the right of your farmer. While higher-level farm buildings such as
Deluxe Barns can be immediately built this way, the incubator will be
missing from Big or Deluxe Coops.</p>
<p><em>Example:</em> <code>debug build "Stone Cabin"</code> would build
a new Stone Cabin next to the player.</p></td>
<td><p>|<a href="#build" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>buildcoop</samp><br />
<samp>bc</samp></p></td>
<td><p>| <em>Syntax</em>: <code>buildcoop</code>
&lt;I:X&gt;,&lt;I:Y&gt;</p>
<p>Tries to build a new coop at the specified position in the current
location. Finishes construction instantly.</p></td>
<td><p>|<a href="#buildcoop" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>finishallbuilds</samp><br />
<samp>fab</samp></p></td>
<td><p>| Finishes all buildings under construction. Only the host player
can use this command in multiplayer.</p></td>
<td><p>|<a href="#finishallbuilds" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>forcebuild</samp></p></td>
<td><p>| <em>Syntax</em>: <code>forcebuild</code>
&lt;S:Name&gt;,[I:X],[I:Y]</p>
<p>Equivalent to <samp>build</samp>, but disables all safety checks so
you can build in a location that wouldn't normally allow buildings,
build on top of farm animals or placed objects, etc.</p>
<p><em>Example:</em> <code>debug build "Stone Cabin"</code> would build
a new Stone Cabin next to the player.</p></td>
<td><p>|<a href="#forcebuild" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>movebuilding</samp></p></td>
<td><p>| <em>Syntax</em>: <code>movebuilding</code>
&lt;I:sourceX&gt;,&lt;I:sourceY&gt;,&lt;I:destX&gt;,&lt;I:destY&gt;</p>
<p>Moves building in the current location from specified source
coordinates to specified destination coordinates. The coordinates are
the upper-left corner of the building's footprint. The <a
href="https://www.nexusmods.com/stardewvalley/mods/541">Lookup
Anything</a> mod is one of the easier ways to get the source coordinates
of a building; they are listed under <samp>tileX</samp> and
<samp>tileY</samp> in the debug info (needs
<samp>ShowDataMiningFields</samp> enabled.)</p></td>
<td><p>|<a href="#movebuilding" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>paintBuilding</samp><br />
<samp>bpm</samp></p></td>
<td><p>| Gets the building the player is standing in front of and opens
a paint menu for that building if it can be painted. If the player is
not standing in front of a building, defaults to the main
farmhouse.</p></td>
<td><p>|<a href="#paintBuilding" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removebuildings</samp></p></td>
<td><p>| Destroys all farm buildings. Animals within any of the
buildings will also be removed, but animals which are outside will not
be.</p></td>
<td><p>|<a href="#removebuildings" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skinbuilding</samp><br />
<samp>bsm</samp></p></td>
<td><p>| If the player is standing right under a building, open a menu
to change the building appearance.</p></td>
<td><p>|<a href="#skinbuilding" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>spawncoopsandbarns</samp></p></td>
<td><p>| <em>Syntax</em>: <code>spawncoopsandbarns</code>
&lt;I:number&gt;</p>
<p>Spawns the specified number of buildings. The game will randomly
choose either a Deluxe Barn full of cows or a Deluxe Coop full of
chickens for each (equal chance). Their locaions are also randomly
chosen and the game will try 20 times to find a spot for each before
giving up. The coops created by this command will not have
incubators.</p></td>
<td><p>|<a href="#spawncoopsandbarns" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Farmhouse

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>crib</samp></p></td>
<td><p>| <em>Syntax</em>: <code>crib</code> &lt;I:mapID&gt;</p>
<p>Sets the current crib style to the specified value. In the base game,
valid values are <samp>0</samp> (no crib) or <samp>1</samp> (default
crib). Additional styles may be possible through modding as the ID is
appended to the map filename. For example, crib style 1 is specified by
the file <samp>Maps/FarmHouse_Crib_1</samp>.</p></td>
<td><p>|<a href="#crib" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>floor</samp></p></td>
<td><p>| <em>Syntax</em>: <code>floor</code> [I:textureID]</p>
<p>Sets all floors of your farmhouse to the specified texture. Valid
texture numbers are <samp>0 - 55</samp>; see <a href="Flooring"
class="wikilink" title="Flooring">Flooring</a> for previews but note
that the IDs used by the game are 1 less than the numbers used for the
wiki filenames. If no texture is specified, the game will use the next
ID after the current floor texture without checking for overflow which
can create bugged textures.</p>
<p><em>Example:</em> <code>debug floor 22</code> would set all flooring
in the house to the white and grey checkerboard style.</p></td>
<td><p>|<a href="#floor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>houseupgrade</samp><br />
<samp>house</samp><br />
<samp>hu</samp></p></td>
<td><p>| <em>Syntax</em>: <code>houseupgrade</code>
&lt;I:upgradeLevel&gt;</p>
<p>Sets upgrade level of your farmhouse/cabin to the specified value.
Valid values are <samp>0 - 3</samp>. Furniture and placed items will not
be automatically moved and may wind up out of bounds. If done while the
player is inside the house, warp points may not immediately
update.</p></td>
<td><p>|<a href="#houseupgrade" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>logWallAndFloorWarnings</samp></p></td>
<td><p>| Enable debug logs when applying wallpaper and flooring to a
farmhouse (or other decoratable location) to help troubleshoot cases
where they don't work with a custom map. You'd usually enable this
before loading the save.</p></td>
<td><p>|<a href="#logWallAndFloorWarnings" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>renovate</samp></p></td>
<td><p>| Opens the <a href="Carpenter&#39;s_Shop#House_Renovations"
class="wikilink" title="farmhouse renovation">farmhouse renovation</a>
menu.</p></td>
<td><p>|<a href="#renovate" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>thishouseupgrade</samp><br />
<samp>thishouse</samp><br />
<samp>thu</samp></p></td>
<td><p>| <em>Syntax</em>: <code>thishouseupgrade</code>
&lt;I:upgradeLevel&gt;</p>
<p>Equivalent to <samp>houseupgrade</samp>, but can be used to upgrade
another player's house by running it from inside or just south of its
exterior.</p></td>
<td><p>|<a href="#thishouseupgrade" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>upgradehouse</samp></p></td>
<td><p>| Increases the upgrade level of your farmhouse/cabin to the next
level (max 3). Furniture and placed items will not be automatically
moved and may wind up out of bounds. If done while the player is inside
the house, warp points may not immediately update.</p></td>
<td><p>|<a href="#upgradehouse" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>wall</samp><br />
<samp>w</samp></p></td>
<td><p>| <em>Syntax</em>: <code>wall</code> [I:textureID]</p>
<p>Sets all walls of your farmhouse to the specified texture. Valid
texture numbers are <samp>0 - 111</samp>; see <a href="Wallpaper"
class="wikilink" title="Wallpaper">Wallpaper</a> for previews but note
that the IDs used by the game are 1 less than the numbers used for the
wiki filenames. If no texture is specified, the game will use the next
ID after the current wallpaper texture without checking for overflow
which can create bugged textures.</p>
<p><em>Example:</em> <code>debug wall 21</code> would set all wallpaper
in the house to the Joja style.</p></td>
<td><p>|<a href="#wall" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Special farm setups

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>farmmap</samp></p></td>
<td><p>| <em>Syntax</em>: <code>farmmap</code> [I:mapID]</p>
<p>Removes the current farm map and farmhouse from the game and creates
a new farm of the specified type. The farm will be named after the type
(<em>e.g.,</em> "Standard Farm"). Valid types are: <samp>0</samp>
(Standard), <samp>1</samp> (Riverland), <samp>2</samp> (Forest),
<samp>3</samp> (Hilltop), <samp>4</samp> (Wilderness), <samp>5</samp>
(Four Corners), <samp>6</samp> (Beach), and <samp>7</samp>
(Meadowlands)</p></td>
<td><p>|<a href="#farmmap" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setupbigfarm</samp></p></td>
<td><p>| Clears the farm and then does the following:</p></td>
<td><p>|<a href="#setupbigfarm" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setupfarm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setupfarm</code> [S:clearMore]</p>
<p>Removes all farm buildings and completely clears large areas of the
current farm. After this, the following things are done:</p></td>
<td><p>|<a href="#setupfarm" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setupfishpondfarm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setupfishpondfarm</code>
[I:population]</p>
<p>Clears farm and then builds up to 96 fish ponds randomly filled with
various types of fish. The population of each of the ponds will be set
to the specified value and defaults to 10. The ponds are built in a
large 12 x 8 grid but will not be placed in a spot blocked by other
buildings, animals, or map features.</p></td>
<td><p>|<a href="#setupfishpondfarm" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Community center and bundles

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>addjunimo</samp><br />
<samp>aj</samp><br />
<samp>j</samp></p></td>
<td><p>| <em>Syntax</em>: <code>addjunimo</code>
&lt;I:X&gt;,&lt;I:Y&gt;,&lt;I:area&gt;</p>
<p>Adds a junimo at the specified coordinates and assigned to the given
Community Center area. Valid areas are <samp>0</samp> (Pantry),
<samp>1</samp> (Crafts Room), <samp>2</samp> (Fish Tank), <samp>3</samp>
(Boiler Room), <samp>4</samp> (Vault), or <samp>5</samp> (Bulletin
Board).</p></td>
<td><p>|<a href="#addjunimo" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>allbundles</samp></p></td>
<td><p>| Marks all bundles complete.</p></td>
<td><p>|<a href="#allbundles" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>bundle</samp></p></td>
<td><p>| <em>Syntax</em>: <code>bundle</code> &lt;I:ID&gt;</p>
<p>Marks the specified bundle as complete. Valid IDs are listed
below.</p></td>
<td><p>|<a href="#bundle" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>ccload</samp></p></td>
<td><p>| <em>Syntax</em>: <code>ccload</code> &lt;I:area&gt;</p>
<p>Removes the junimo note from and restores the specified area. Valid
areas are <samp>0</samp> (Pantry), <samp>1</samp> (Crafts Room),
<samp>2</samp> (Fish Tank), <samp>3</samp> (Boiler Room), <samp>4</samp>
(Vault), or <samp>5</samp> (Bulletin Board).</p></td>
<td><p>|<a href="#ccload" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>ccloadcutscene</samp></p></td>
<td><p>| <em>Syntax</em>: <code>ccloadcutscene</code> &lt;I:area&gt;</p>
<p>Plays the full restoration cutscene for the specified area including
junimo dance and star retrieval. Valid areas are <samp>0</samp>
(Pantry), <samp>1</samp> (Crafts Room), <samp>2</samp> (Fish Tank),
<samp>3</samp> (Boiler Room), <samp>4</samp> (Vault), or <samp>5</samp>
(Bulletin Board).</p></td>
<td><p>|<a href="#ccloadcutscene" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>completecc</samp></p></td>
<td><p>| Adds all of the appropriate flags for Community Center
completion and restores all areas.</p></td>
<td><p>|<a href="#completecc" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>completejoja</samp></p></td>
<td><p>| Adds all of the appropriate flags for Joja membership and
Community Development purchases.</p></td>
<td><p>|<a href="#completejoja" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>junimogoodbye</samp></p></td>
<td><p>| Plays the animation where 6 junimos wave goodbye in front of
the hut in the Community Center and then that corner of the Community
Center gets restored.</p></td>
<td><p>|<a href="#junimogoodbye" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>junimonote</samp><br />
<samp>jn</samp></p></td>
<td><p>| <em>Syntax</em>: <code>junimonote</code> &lt;I:area&gt;</p>
<p>Adds a junimo note (bundle scroll) for the specified area. Valid
areas are <samp>0</samp> (Pantry), <samp>1</samp> (Crafts Room),
<samp>2</samp> (Fish Tank), <samp>3</samp> (Boiler Room), <samp>4</samp>
(Vault), or <samp>5</samp> (Bulletin Board).</p></td>
<td><p>|<a href="#junimonote" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>junimostar</samp></p></td>
<td><p>| Causes a junimo to run to the hut and retrieve a star which is
then placed on the plaque above the fireplace. Must be done in the
Community Center.</p></td>
<td><p>|<a href="#junimostar" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>plaque</samp></p></td>
<td><p>| Adds a star to the plaque above the Community Center
fireplace.</p></td>
<td><p>|<a href="#plaque" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>resetjunimonotes</samp></p></td>
<td><p>| Resets all bundles.</p></td>
<td><p>|<a href="#resetjunimonotes" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>shufflebundles</samp></p></td>
<td><p>| Regenerates bundles using remixed bundle logic and without a
specific random seed.</p></td>
<td><p>|<a href="#shufflebundles" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Other location-specific functions

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>activatecalicostatue</samp></p></td>
<td><p>| Spawns and activates a new Calico Statue from the <a
href="Desert_Festival#Skull_Cavern" class="wikilink"
title="Desert Festival">Desert Festival</a> at point (8, 8) on the
player's current mines level. If the player is in the regular mines
instead of the Skull Cavern, the statue will not visually spawn but some
animations and effects will still occur.</p></td>
<td><p>|<a href="#activatecalicostatue" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>beachbridge</samp></p></td>
<td><p>| Toggles the state of the beach bridge between fixed and not
fixed.</p></td>
<td><p>|<a href="#beachbridge" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>ladder</samp><br />
<samp>shaft</samp></p></td>
<td><p>| <em>Syntax</em>: <code>ladder</code> [I:X],[I:Y]</p>
<p>Creates a ladder or mineshaft at the specified coordinates. If no
coordinates are given, it will spawn 1 tile north of the player. In the
regular mines, both versions of the command will create a ladder. In the
Skull Caverns, <samp>ladder</samp> will randomly spawn either a ladder
or mineshaft while <samp>shaft</samp> will always spawn a
mineshaft.</p></td>
<td><p>|<a href="#ladder" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>minedifficulty</samp><br />
<samp>md</samp></p></td>
<td><p>| <em>Syntax</em>: <code>minedifficulty</code>
[I:difficultyLevel]</p>
<p>Sets the difficulty of the mines to the specified level. In the base
game, normal difficulty is <samp>0</samp> and the harder difficulty
corresponding to the "Danger in the Deep" quest or <a
href="The_Mines#Shrine_of_Challenge" class="wikilink"
title="Shrine of Challenge">Shrine of Challenge</a> activation is
<samp>1</samp>. Higher numbers can be used. If no difficulty level is
specified, command will simply print the current difficulty level to the
console.</p></td>
<td><p>|<a href="#minedifficulty" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>movie</samp></p></td>
<td><p>| <em>Syntax</em>: <code>movie</code>
[S:movieID],[S:inviteNpcName]</p>
<p>Starts a movie. The movie ID defaults to today's movie, and the NPC
name can be omitted to watch the movie without an invitee. Note that
this command can create a group with up to 3 guests instead of just the
single guest allowed in normal play. Valid vanilla movie IDs are listed
below.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug movie</code> would show <em>It Howls in the Rain</em>
with random NPC guests.</li>
</ul>
<ul>
<li><code>debug movie spring_movie_1</code> would show <em>Natural
Wonders</em> with random NPC guests.</li>
</ul>
<ul>
<li><code>debug movie summer_movie_0 Abi</code> would show <em>Journey
of the Prairie King</em> with Abigail and possibly 1 or 2 additional
random NPC guests.</li>
</ul></td>
<td><p>|<a href="#movie" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pgb</samp><br />
<samp>printGemBirds</samp></p></td>
<td><p>| Prints the <a href="Ginger_Island#Gem_Birds" class="wikilink"
title="Gem Bird Puzzle">Gem Bird Puzzle</a> solution to the
console.</p></td>
<td><p>|<a href="#pgb" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>resetmines</samp></p></td>
<td><p>| Resets "permanent mine changes" such as coal carts and treasure
chests. Does not affect mines level progress or monster eradication
goals.</p></td>
<td><p>|<a href="#resetmines" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>returneddonations</samp></p></td>
<td><p>| Opens the "returned donations" menu of the Lost and Found box
from the <a href="Mayor&#39;s_Manor" class="wikilink"
title="Mayor&#39;s Manor">Mayor's Manor</a>.</p></td>
<td><p>|<a href="#returneddonations" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skullcavedifficulty</samp><br />
<samp>scd</samp></p></td>
<td><p>| <em>Syntax</em>: <code>skullcavedifficulty</code>
[I:difficultyLevel]</p>
<p>Sets the difficulty of the Skull Cavern to the specified level. In
the base game, normal difficulty is <samp>0</samp> and the harder
difficulty corresponding to the "Skull Cavern Invasion" quest is
<samp>1</samp>. Higher numbers can be used. If no difficulty level is
specified, command will simply print the current difficulty level to the
console.</p>
<p><em>Example:</em> <code>debug scd 1</code> would activate hard mode
Skull Cavern outside of the "Skull Cavern Invasion" quest.</p></td>
<td><p>|<a href="#skullcavedifficulty" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>train</samp></p></td>
<td><p>| Causes a train to spawn at the Railroad.</p></td>
<td><p>|<a href="#train" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
