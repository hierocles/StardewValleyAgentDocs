---
title: "Map Properties And Tiles"
wiki_source: "Modding:Maps"
permalink: /Modding:Maps/
category: locations
tags: [maps, known-map-properties, building-construction, crops, plants-forage-item-spawning, warps-map-positions, audio, lighting]
---
## Known map properties

Arguments in \< \> are required. Arguments in \[ \] are optional;
however, optional arguments must be provided sequentially and may not be
skipped.

### Building construction

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>CanBuildHere T</samp><br />
<em>(valid in any outdoor location)</em></p></td>
<td><p>Whether to allow constructing buildings in this location. The
game will adjust automatically to account for it (e.g. Robin will let
you choose where to build).</p></td>
</tr>
<tr>
<td><p><samp>BuildConditions &lt;query&gt;</samp><br />
<em>(valid in any outdoor location)</em></p></td>
<td><p>If <samp>CanBuildHere</samp> is set, an optional <a
href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> which indicates whether
building is allowed currently.</p></td>
</tr>
<tr>
<td><p><samp>LooserBuildRestrictions T</samp><br />
<em>(valid in any outdoor location)</em></p></td>
<td><p>If set, tiles don't need to be marked <samp>Buildable T</samp> or
<samp>Diggable T</samp> in their properties. Tiles can be blocked with
<samp>Buildable F</samp> instead. The other restrictions still
apply.</p></td>
</tr>
<tr>
<td><p><samp>ValidBuildRect &lt;x&gt; &lt;y&gt; &lt;width&gt;
&lt;height&gt;</samp><br />
<em>(valid in any outdoor location)</em></p></td>
<td><p>The tile area within the map where buildings may be placed. If
omitted, buildings may be placed in any open space in the map.</p></td>
</tr>
</tbody>
</table>

### Crops

| property | explanation |
|----|----|
| `AllowGiantCrops T` | If set with any non-blank value, <a href="Crops#Giant_Crops" class="wikilink" title="giant crops">giant
crops</a> can grow in this location (if crops are also allowed per the <a href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_crops"
class="wikilink" title="crop data">crop data</a> or <a href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_location_contexts"
class="wikilink"
title="PlantableLocations context field"><samp>PlantableLocations</samp>
context field</a>). |
| `DirtDecayChance <chance>` | The probability that each dirt tile will disappear overnight if it doesn't contain a crop, as a value between 0 (never) and 1 (always). Defaults to 0 (greenhouses), 0.1 (farms), and 1 (anywhere else). |

### Plants, forage, & item spawning

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AllowGrassGrowInWinter T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Allows <a href="grass" class="wikilink" title="grass">grass</a>
to spread in winter.</p></td>
</tr>
<tr>
<td><p><samp>AllowGrassSurviveInWinter T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Allows <a href="grass" class="wikilink" title="grass">grass</a>
that's alive on the last day of fall to survive through to
winter.</p></td>
</tr>
<tr>
<td><p><samp>EnableGrassSpread T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Gives <a href="grass" class="wikilink" title="grass">grass</a> in
the location a chance to spread each day.</p></td>
</tr>
<tr>
<td><p><samp>Fall_Objects T</samp>²<br />
<samp>Spring_Objects T</samp>²<br />
<samp>Summer_Objects T</samp>²<br />
<samp>Winter_Objects T</samp>²</p></td>
<td><p>Do not use this to spawn seasonal forage objects. Spawn forage by
editing the <samp>Forage</samp> field in <a href="Modding_Location_data"
class="wikilink" title="Data/Locations">Data/Locations</a>
instead.<br />
<br />
This property only works in very specific contexts in conjunction with
the <samp>forceLoadObjects</samp> map property (not listed). Do not use
either property.</p></td>
</tr>
<tr>
<td><p><s><samp>Feed &lt;int x&gt; &lt;int y&gt;</samp><br />
<em>(valid in coops and barns)</em></s></p></td>
<td><p><s>Sets the spawn location of the <a href="Hay_Hopper"
class="wikilink" title="Hay Hopper">Hay Hopper</a> in a coop or
barn.<br />
<em>Example: <samp>Feed 3 2</samp>.</em></s><br />
The Feed map property has been deprecated with 1.6. The FeedHopper is
now being defined in Data/Buildings as a IndoorItems entry
"(BC)99"</p></td>
</tr>
<tr>
<td><p><samp>ForceAllowTreePlanting T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Allows planting trees (both wild and fruit) in this location,
even if it normally wouldn't be allowed.</p></td>
</tr>
<tr>
<td><p><samp>ForceSpawnForageables T</samp>²<br />
<em>(valid in indoor locations)</em></p></td>
<td><p>Enables forage items spawning in that location.</p></td>
</tr>
<tr>
<td><p><samp>skipWeedGrowth T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Prevents weeds from spawning and spreading in this
location.</p></td>
</tr>
<tr>
<td><p><samp>SpawnBeachFarmForage T</samp>²<br />
<em>(valid in farm)</em></p></td>
<td><p>Randomly spawns beach forage and <a href="Supply_Crate"
class="wikilink" title="supply crates">supply crates</a> on the farm
(like the <a href="Farm_Maps" class="wikilink"
title="vanilla beach farm">vanilla beach farm</a>). Forage and crates
will only appear on tiles which have the <samp>BeachSpawn T</samp>
property on the <samp>Back</samp> layer, are clear for placement, and
don't have a tile on the <samp>AlwaysFront</samp> layer.</p></td>
</tr>
<tr>
<td><p><samp>SpawnForestFarmForage T</samp>²<br />
<em>(valid in farm)</em></p></td>
<td><p>Randomly spawns forest forage on the farm (like the <a
href="Farm_Maps" class="wikilink" title="vanilla forest farm">vanilla
forest farm</a>). Forage will only spawn on tiles which have the
<samp>Type Grass</samp> tile property, are clear for placement, and
don't have a tile on the <samp>AlwaysFront</samp> layer.</p></td>
</tr>
<tr>
<td><p><samp>SpawnGrassFromPathsOnNewYear T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Spawns grass on every tile with index 22 on the
<samp>Paths</samp> layer when a new year starts. See also
<samp>SpawnRandomGrassOnNewYear</samp>.</p></td>
</tr>
<tr>
<td><p><samp>SpawnDebrisOnNewMonth T</samp><br />
<samp>SpawnDebrisOnNewYear T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Spawns weeds, stones, or twigs at random positions when a new
month/year starts (subject to their usual spawn rules).</p></td>
</tr>
<tr>
<td><p><samp>SpawnMountainFarmOreRect &lt;tile X&gt; &lt;tile Y&gt;
&lt;tile width&gt; &lt;tile height&gt;</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The tile area on the farm map where ores should randomly spawn
(like the <a href="Farm_Maps" class="wikilink"
title="vanilla hilltop farm">vanilla hilltop farm</a>). Ores will only
spawn on tiles which have the <samp>Type Dirt</samp> tile property and
are clear for object placement.</p></td>
</tr>
<tr>
<td><p><samp>SpawnRandomGrassOnNewYear T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Spawns grass at random positions when a new year starts (subject
to its usual spawn rules). See also
<samp>SpawnGrassFromPathsOnNewYear</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Stumps [&lt;int x&gt; &lt;int y&gt;
&lt;unused&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Adds stumps to the Secret Woods map daily. The third field for
each stump appears to be unused.<br />
<em>Example: <samp>Stumps 24 6 3 29 7 3 26 10 3 46 6 3 34 26 3 41 26
3</samp>.</em></p></td>
</tr>
<tr>
<td><p><samp>Treasure &lt;type&gt; &lt;int id&gt;</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Adds buried treasure that the player can dig up. &lt;type&gt; can
be any of the following:<br />
<samp>Coins, Copper, Coal, Iron, Gold, Iridium, CaveCarrot, Arch,
Object</samp>.<br />
If set to <samp>Arch</samp> or <samp>Object</samp>, &lt;id&gt; may be
used to specify the ID of the item that is buried. - Per Esca, this is
actually a Tile Property. Also, per Elizabeth, this is not fully
implemented, advise against use.</p></td>
</tr>
<tr>
<td><p><samp>Trees [&lt;int x&gt; &lt;int y&gt; &lt;int
type&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Adds trees to the map. The &lt;x&gt; &lt;y&gt; fields are the
tile coordinates, and &lt;type&gt; is the tree type (0: oak, 1: maple,
2: pine, 5: palm, 6: mushroom tree, 7: mahogany).<br />
<em>Example: <samp>Trees 17 18 2 20 31 2</samp>.</em></p></td>
</tr>
</tbody>
</table>

### Warps & map positions

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AllowWakeUpWithoutBed &lt;allow&gt;</samp></p></td>
<td><p>Whether the player can wake up in this location without a bed,
similar to the island farmhouse. This is typically used with
<samp>PassOutLocations</samp> in <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_location_contexts"
class="wikilink"
title="Data/LocationContexts"><samp>Data/LocationContexts</samp></a>.</p></td>
</tr>
<tr>
<td><p><samp>BackwoodsEntry [&lt;int x&gt; &lt;int y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The position the player is warped to when entering the farm from
the Backwoods.</p></td>
</tr>
<tr>
<td><p><samp>BusStopEntry [&lt;int x&gt; &lt;int y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The position the player is warped to when entering the farm from
the Bus Stop.</p></td>
</tr>
<tr>
<td><p><samp>DefaultWarpLocation &lt;x&gt; &lt;y&gt;</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>The default arrival tile, used when a player or NPC is added to
the location without a target tile (e.g. using <a
href="Modding_Console_commands" class="wikilink"
title="debug commands">debug commands</a> like <samp>debug warp</samp>
or <samp>debug eventbyid</samp>).</p></td>
</tr>
<tr>
<td><p><samp>EntryLocation &lt;tile X&gt; &lt;tile Y&gt;</samp><br />
<em>(valid in farmhouse)</em></p></td>
<td><p>Sets the tile on which the player appears when they warp into the
farmhouse.</p></td>
</tr>
<tr>
<td><p><samp>FarmCaveEntry [&lt;int x&gt; &lt;int y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The position the player is warped to when entering the farm from
the farm cave.</p></td>
</tr>
<tr>
<td><p><samp>FarmHouseEntry [&lt;int x&gt; &lt;int y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>Changes the position of the Farm House. Corresponds to the front
door, or the position the player will be warped to when leaving the
house.</p></td>
</tr>
<tr>
<td><p><samp>ForestEntry [&lt;int x&gt; &lt;int y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The position the player is warped to when entering the farm from
the Cindersap Forest.</p></td>
</tr>
<tr>
<td><p><samp>GrandpaShrineLocation [&lt;int x&gt; &lt;int
y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The position of grandpa's shrine. Corresponds to the upper left
corner of note.</p></td>
</tr>
<tr>
<td><p><samp>GreenhouseLocation [&lt;int x&gt; &lt;int
y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The default position of the greenhouse. Corresponds to the upper
left corner of the greenhouse's foundation.</p></td>
</tr>
<tr>
<td><p><samp>KitchenStandingLocation [&lt;int x&gt; &lt;int
y&gt;]</samp><br />
<em>(valid in farmhouse)</em></p></td>
<td><p>The position the player's spouse will stand when using the
kitchen.</p></td>
</tr>
<tr>
<td><p><samp>MailboxLocation [&lt;int x&gt; &lt;int y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>Used as part of moving a farmhouse's mailbox, this property
controls where the mail icon is drawn. &lt;int x&gt; &lt;int y&gt; is
the tile coordinates of the base of the mailbox, the tile you interact
with. In order to properly move the farmhouse mailbox you must also
patch <samp>Data/Buildings</samp> to remove the
<samp>Default_Mailbox</samp> entries from <samp>ActionTiles</samp> and
<samp>DrawLayers</samp> and add an Action Mailbox property to the same
tile as this property.</p></td>
</tr>
<tr>
<td><p><samp>NPCWarp [&lt;int fromX&gt; &lt;int fromY&gt; &lt;string
toArea&gt; &lt;int toX&gt; &lt;int toY&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Equivalent to <samp>Warp</samp>, but only usable by
npcs.</p></td>
</tr>
<tr>
<td><p><samp>PetBowlLocation &lt;x&gt; &lt;y&gt;</samp><br />
<em>(valid in the farm)</em></p></td>
<td><p>The default position of the pet bowl</p></td>
</tr>
<tr>
<td><p><samp>ShippingBinLocation [&lt;int x&gt; &lt;int
y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The position of the default shipping bin. Corresponds to the
upper left corner.</p></td>
</tr>
<tr>
<td><p><samp>SpouseAreaLocation [&lt;int x&gt; &lt;int
y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The position of the the 4x4 outdoor spouse area. Corresponds to
the upper left corner.<a href="File_SpouseArea.png" class="wikilink"
title="upright=0.5">upright=0.5</a></p></td>
</tr>
<tr>
<td><p><samp>SpouseRoomPosition &lt;x&gt; &lt;y&gt;</samp><br />
<em>(valid in farmhouse)</em></p></td>
<td><p>The top-left position at which to place the <a
href="Marriage#Spouse_Rooms" class="wikilink" title="spouse room">spouse
room</a>.</p></td>
</tr>
<tr>
<td><p><samp>TravelingCartPosition &lt;x&gt; &lt;y&gt;</samp><br />
<em>(valid in the forest)</em></p></td>
<td><p>The top-left position at which to place the <a
href="Traveling_Cart" class="wikilink" title="Traveling Cart">Traveling
Cart</a>. This is the top-left corner of the collision box, so the roof
will extend two tiles above this tile.</p></td>
</tr>
<tr>
<td><p><samp>Warp [&lt;int fromX&gt; &lt;int fromY&gt; &lt;string
toArea&gt; &lt;int toX&gt; &lt;int toY&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Sets the tiles which warp players or NPCs to another map
(<em>e.g.,</em> doors). The &lt;fromX&gt; &lt;fromY&gt; fields are the
tile coordinates that initiate the warp, and &lt;toArea&gt; &lt;toX&gt;
&lt;toY&gt; are the name of the in-game location to warp to and the tile
coordinates within it.<br />
<em>Example: 6 20 Mountain 76 9.</em></p></td>
</tr>
<tr>
<td><p><samp>WarpTotemEntry[&lt;int x&gt; &lt;int y&gt;]</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>The position the player is warped to when teleporting to the farm
via Warp Totem or Return Scepter.</p></td>
</tr>
</tbody>
</table>

### Audio

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>BrookSounds [&lt;int x&gt; &lt;int y&gt; &lt;int
type&gt;]</samp><br />
<em>(valid in outdoor locations)</em></p></td>
<td><p>Adds sound sources. The &lt;x&gt; &lt;y&gt; fields are the tile
coordinates, and &lt;type&gt; is the ambient sound ID. The &lt;type&gt;
of sound can be one of...</p>
<ul>
<li><samp>0</samp> (babblingBrook);</li>
<li><samp>1</samp> (cracklingFire);</li>
<li><samp>2</samp> (engine);</li>
<li><samp>3</samp> (cricket);</li>
<li><samp>4</samp> (waterfall);</li>
<li><samp>5</samp> (big waterfall).</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Music &lt;string name&gt;</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Sets the music that plays when the player enters, where
&lt;name&gt; is the cue name in the audio files.<br />
<em>Example: <samp>Music MarlonsTheme</samp>.</em> (Deprecated; use the
music fields in <a href="Modding_Location_data#Music" class="wikilink"
title="Data/Locations"><samp>Data/Locations</samp></a> instead. This
property is only applied if the location has no music in
<samp>Data/Locations</samp>.)</p></td>
</tr>
<tr>
<td><p><samp>Music &lt;int start&gt; &lt;int end&gt; &lt;string
name&gt;</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Sets the music that plays when the player enters, where
&lt;name&gt; is the cue name in the audio files, music will only play if
the time is between &lt;int start&gt; (inclusive) and &lt;int end&gt;
(exclusive).<br />
<em>Example: <samp>Music 800 1200 MarlonsTheme</samp>.</em> (Deprecated;
use the music fields in <a href="Modding_Location_data#Music"
class="wikilink" title="Data/Locations"><samp>Data/Locations</samp></a>
instead. This property is only applied if the location has no music in
<samp>Data/Locations</samp>.)</p></td>
</tr>
</tbody>
</table>

### Lighting

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AmbientLight &lt;byte r&gt; &lt;byte g&gt; &lt;byte
b&gt;</samp><br />
<em>(valid in indoor locations and locations that ignore outdoor
lighting)</em></p></td>
<td><p>Sets the <a href="wikipedia_RGB_color_model" class="wikilink"
title="RGB color">RGB color</a> that is subtracted from white
(255,255,255) in order to create the ambient light.<br />
<em>Example: <samp>AmbientLight 95 95 95</samp> for a normal indoor
daytime lighting.</em></p></td>
</tr>
<tr>
<td><p><samp>AmbientNightLight &lt;byte r&gt; &lt;byte g&gt; &lt;byte
b&gt;</samp><br />
<em>(valid in indoor locations and locations that ignore outdoor
lighting)</em></p></td>
<td><p>Sets the <a href="wikipedia_RGB_color_model" class="wikilink"
title="RGB color">RGB color</a> that is subtracted from white
(255,255,255) in order to create the ambient night light.<br />
<em>Example: <samp>AmbientLight 150 150 30</samp> for greenhouse
nighttime lighting.</em></p></td>
</tr>
<tr>
<td><p><samp>forceLoadPathLayerLights T</samp>²<br />
<em>(valid in outdoor non-festival locations)</em></p></td>
<td><p>Whether to load lights from the <samp>Paths</samp> layer on maps
where they would not normally be.<br />
<em>Example: <samp>forceLoadPathLayerLights true</samp>.</em></p></td>
</tr>
<tr>
<td><p><samp>IgnoreLightingTiles T</samp>²<br />
<em>(valid in indoor locations)</em></p></td>
<td><p>Whether to ignore lights on the <samp>Front</samp> and
<samp>Buildings</samp> layers.<br />
<em>Example: <samp>IgnoreLightingTiles true</samp>.</em></p></td>
</tr>
<tr>
<td><p><samp>Light [&lt;int x&gt; &lt;int y&gt; &lt;int
type&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Adds light sources. The &lt;type&gt; field is the kind of light
source (<em>e.g.,</em> 4 for twin candles), and &lt;x&gt; &lt;y&gt; are
the tile coordinates.The &lt;type&gt; of light source can be one of...
<a href="File_LightReference.png" class="wikilink"
title="upright=0.75">upright=0.75</a></p>
<ul>
<li><samp>1</samp> (lantern);</li>
<li><samp>2</samp> (window);</li>
<li><samp>4</samp> (sconce);</li>
<li><samp>5</samp> (cauldron);</li>
<li><samp>6</samp> (indoor window);</li>
<li><samp>7</samp> (projector);</li>
<li><samp>8</samp> (fish tank);</li>
<li><samp>9</samp> (winter town tree lights);</li>
<li><samp>10</samp> (pinpoint).</li>
</ul>
<p>Any other value will crash the game.<br />
<em>Example: <samp>Light 3 8 4 6 8 4 11 8 4 3 2 5 10 2 5 6 19 5 5 15 5 5
11 5 11 12 5</samp> (Adventurer's Guild).</em></p></td>
</tr>
<tr>
<td><p><samp>WindowLight [&lt;int x&gt; &lt;int y&gt; &lt;int
type&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Adds light sources that are only lit during the day when it is
not raining (like the light coming through a window). See
<samp>Light</samp> for details.</p></td>
</tr>
</tbody>
</table>

### Map & tile changes

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ClearEmptyDirtOnNewMonth T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Destroy most tilled dirt that doesn't contain crops when a new
year starts.</p></td>
</tr>
<tr>
<td><p><samp>DayTiles [&lt;string layerName&gt; &lt;int x&gt; &lt;int
y&gt; &lt;int tilesheetIndex&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Sets tiles to appear between 6AM to 7PM. Anytime before 7pm, this
finds the tile at position (&lt;x&gt;, &lt;y&gt;) on the map layer
matching &lt;layerName&gt;, changes its tilesheet index to the specified
&lt;tilesheetIndex&gt;, and adds a glow to simulate daylight. The glow
will only be added if the location is indoors and the
&lt;tilesheetIndex&gt; is 256, 288, 405, 469, or 1224. The parameters
can be repeated to affect multiple tiles.<br />
<em>Example: <samp>DayTiles Front 3 1 256 Front 3 2
288</samp>.</em></p></td>
</tr>
<tr>
<td><p><samp>NightTiles [&lt;string layerName&gt; &lt;int x&gt; &lt;int
y&gt; &lt;int tilesheetIndex&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Changes the tile after 7pm. Outside, it works along
<samp>DayTiles</samp>: set a <samp>DayTiles</samp> tile for the map to
load between 6am to 7pm, then a <samp>NightTiles</samp> to load between
7pm to the end of the day. It is mostly used for lamps in the game. Note
that night time starts at different times depending on season (<a
href="Day_Cycle#Darkness" class="wikilink" title="Day Cycle">Day
Cycle</a>).</p></td>
</tr>
<tr>
<td><p><samp>&lt;span id="anchor_doors"&gt;Doors&lt;/span&gt; [&lt;int
x&gt; &lt;int y&gt; &lt;string sheetID&gt; &lt;int
tileID&gt;]+</samp><br />
<em>(valid in indoor locations)</em></p></td>
<td><p>Adds functionality to interior doors. Used with
<samp>[[#anchor_door|Action Door]]</samp> tile properties - both are
required for interior doors to function. The &lt;x&gt; &lt;y&gt; fields
are the tile coordinates, &lt;sheetID&gt; is the name of the sheet
containing the door sprite, and &lt;tileID&gt; is the tile index in the
spritesheet.</p></td>
</tr>
</tbody>
</table>

### Fishing

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>FarmFishLocationOverride &lt;location name&gt;
&lt;chance&gt;</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>Adds an alternative location name when catching fish, where the
&lt;chance&gt; is a decimal value between 0 (never happens) and 1
(always happens). For example, <samp>FarmFishLocationOverride Mountain
0.5</samp> adds a 50% chance of catching mountain fish instead of the
normal fish for that location. The location name is case-sensitive, and
matches those shown by the .</p></td>
</tr>
<tr>
<td><p><samp>FarmOceanCrabPotOverride T</samp>²<br />
<em>(valid in farm)</em></p></td>
<td><p>Causes crab pots on the farm should catch ocean fish.</p></td>
</tr>
</tbody>
</table>

### Farmhouse interior

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AdditionalRenovations &lt;renovation&gt;+</samp><br />
<em>(valid in farmhouse)</em></p></td>
<td><p>Used to create custom farmhouse renovations. See <a
href="Modding_Farmhouse_Renovations" class="wikilink"
title="Modding:Farmhouse Renovations">Modding:Farmhouse Renovations</a>
for details.</p></td>
</tr>
<tr>
<td><p><samp>FarmHouseFlooring &lt;flooring id&gt;</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>Sets the initial farmhouse floor to the given ID when creating a
new save. These are mapped to the 4x4 tile areas in the
<samp>Maps/walls_and_floors</samp> tilesheet starting at tile index 336
(where index 0 is mapped to the top-left square).</p></td>
</tr>
<tr>
<td><p><samp>FarmHouseFurniture [&lt;furniture ID&gt; &lt;tile X&gt;
&lt;tile Y&gt; &lt;rotations&gt;]+</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>Spawns initial furniture in the farmhouse when creating a new
save. If you add multiple furniture to the same tile, the first one will
be placed on the ground and the last one will be placed on the first
one.<br />
</p></td>
</tr>
<tr>
<td><p><samp>FarmHouseStarterGift [&lt;id&gt; [count]]+</samp></p></td>
<td><p>The items that should appear in the initial gift box placed in
the farmhouse when the save is created. This consists of one or more
pairs of item ID (which can be qualified or unqualified) and count. The
count is optional on the last entry.</p>
<p>For example, this will add 10 pufferfish (object 128) and a blobfish
mask (hat 56):</p>
<pre><code>FarmHouseStarterGift (O)128 10 (H)56 1</code></pre>
<p>If omitted, the default items (usually a 15 parsnip seeds) are added
instead.</p></td>
</tr>
<tr>
<td><p><samp>FarmHouseStarterSeedsPosition &lt;tile X&gt; &lt;tile
Y&gt;</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>Sets the tile position in the farmhouse where the seed package is
placed when creating a new save.</p></td>
</tr>
<tr>
<td><p><samp>FarmHouseWallpaper &lt;wallpaper id&gt;</samp><br />
<em>(valid in farm)</em></p></td>
<td><p>Sets the initial farmhouse wallpaper to the given ID when
creating a new save. These are mapped to the 1x4 tile areas in the
<samp>Maps/walls_and_floors</samp> tilesheet starting from the
top-left.</p></td>
</tr>
</tbody>
</table>

### Other location metadata

<table>
<thead>
<tr>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AllowBeds &lt;allowed&gt;</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Whether <a href="Furniture#Beds" class="wikilink"
title="beds">beds</a> can be placed in this location. This can be
<samp>true</samp> or <samp>false</samp>. If specified, this bypasses the
usual specific requirements (e.g. farmhouse upgrade level), though
general furniture restrictions still apply (e.g. the 'placement
restriction' field in <samp>Data/Furniture</samp>).</p></td>
</tr>
<tr>
<td><p><samp>AllowMiniFridges &lt;allowed&gt;</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Whether <a href="Mini-Fridge" class="wikilink"
title="mini-fridges">mini-fridges</a> can be placed in this location.
This can be <samp>true</samp> or <samp>false</samp>. If specified, this
bypasses the usual specific requirements (e.g. farmhouse upgrade level),
though general furniture restrictions still apply (e.g. the 'placement
restriction' field in <samp>Data/Furniture</samp>).</p></td>
</tr>
<tr>
<td><p><samp>AutoFeed T</samp>²<br />
<em>(valid in coops and barns)</em></p></td>
<td><p>Allows a barn or a coop to automatically pull hay from silos for
animals to eat (Same as in Deluxe Barns and Coops).<br />
</p></td>
</tr>
<tr>
<td><p><samp>CanCaskHere T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Allows casks to work in that location.</p></td>
</tr>
<tr>
<td><p><samp>indoorWater T</samp>²<br />
<em>(valid in indoor locations)</em></p></td>
<td><p>Enables water logic (ie. fishing, etc.) in that
location.</p></td>
</tr>
<tr>
<td><p><samp>IsFarm T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Marks the location as a farm. This only affects generic
location/interaction logic which checks the in-code
<code>location.IsFarm</code> property; logic hardcoded into the game's
<code>Farm</code> class (<em>e.g.,</em> pets, crows/scarecrows,
greenhouse, etc) is still limited to the actual farm. As of , farm
buildings other than <a href="Cabin" class="wikilink"
title="cabins">cabins</a> and the <a href="Farmhouse" class="wikilink"
title="farmhouse">farmhouse</a>, as well as farm animals, are
<em>not</em> limited to the actual farm.</p></td>
</tr>
<tr>
<td><p><samp>IsGreenhouse T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Marks the location as a greenhouse.</p></td>
</tr>
<tr>
<td><p><samp>LocationContext Default</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Sets the map to be part of the mainland for game logic purposes,
like weather.</p></td>
</tr>
<tr>
<td><p><samp>LocationContext Island</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Sets the map to be part of Ginger Island for game logic purposes,
like weather.</p></td>
</tr>
<tr>
<td><p><samp>Outdoors T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Sets whether the location is outdoors.<br />
<em>Example: <samp>Outdoors true</samp>.</em></p></td>
</tr>
<tr>
<td><p><samp>ProduceArea &lt;int x&gt; &lt;int y&gt; &lt;int width&gt;
&lt;int height&gt;</samp><br />
<em>(valid in coops and barns)</em></p></td>
<td><p>Sets the area where animals can spawn within a coop or
barn.<br />
<em>Example: <samp>ProduceArea 6 4 8 7</samp>.</em></p></td>
</tr>
<tr>
<td><p><samp>PassOutSafe T</samp><sup>2</sup><br />
<em>(valid in any location)</em></p></td>
<td><p>Marks a map as safe to pass out in. Player wakes up in their bed
the next day with no money penalty.<br />
<em>Example: <samp>PassOutSafe T</samp></em></p></td>
</tr>
<tr>
<td><p><samp>ScreenshotRegion &lt;int left&gt; &lt;int top&gt; &lt;int
right&gt; &lt;int bottom&gt;</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Constrains the portion of the map rendered when screenshots are
taken.<br />
<em>Example: <samp>ScreenshotRegion 0 27 69 61</samp>.</em></p></td>
</tr>
<tr>
<td><p><samp>SeasonOverride &lt;string season&gt;</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Assumes a specific season for most game checks. (If a crop is in
season, which tilesheet to use, etc.)</p></td>
</tr>
<tr>
<td><p><samp>TreatAsOutdoors T</samp>²<br />
<em>(valid in indoor locations)</em></p></td>
<td><p>The location is treated as outdoors for the purposes of spawning
anything other than lights from the <samp>Paths</samp> layer and
yielding <a href="Coal" class="wikilink" title="Coal">Coal</a> from
breaking rocks.<br />
<em>Example: <samp>TreatAsOutdoors true</samp>.</em></p></td>
</tr>
<tr>
<td><p><samp>UniquePortrait [&lt;str name&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Switches the portraits for the named NPCs to the unique variants
for the location. An NPC <samp>Jane</samp> in location <samp>Room</samp>
will switch to portrait <samp>Portraits/Jane_Room</samp>.<br />
<em>Example: <samp>UniquePortrait Maru</samp>.</em> (Deprecated; use <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_NPC_appearance"
class="wikilink" title="custom NPC appearances">custom NPC
appearances</a> instead. These properties will override NPC
appearances.)</p></td>
</tr>
<tr>
<td><p><samp>UniqueSprite [&lt;str name&gt;]+</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Switches the spritesheets for the named NPCs to the unique
variants for the location. An NPC <samp>Jane</samp> in location
<samp>Room</samp> will switch to spritesheet
<samp>Characters/Jane_Room</samp>.<br />
<em>Example: <samp>UniqueSprite Maru</samp>.</em> (Deprecated; use <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_NPC_appearance"
class="wikilink" title="custom NPC appearances">custom NPC
appearances</a> instead. These properties will override NPC
appearances.)</p></td>
</tr>
<tr>
<td><p><samp>ViewportClamp &lt;int x&gt; &lt;int y&gt; &lt;int width&gt;
&lt;int height&gt;</samp></p></td>
<td><p>Stops viewport from moving outside of the specified area.<br />
<em>Example: <samp>ViewportClamp 10 0 35 30</samp></em> (Used on the
BusStop map, end result is the top left-most visible tile is at 10, 0
and the bottom right-most visible tile is at 44, 29.)</p></td>
</tr>
<tr>
<td><p><samp>ViewportFollowPlayer T</samp>²<br />
<em>(valid in any location)</em></p></td>
<td><p>Forces the viewport to stay centered on the player.<br />
<em>Example: <samp>ViewportFollowPlayer</samp>.</em></p></td>
</tr>
</tbody>
</table>

<small>¹ Map properties are primarily handled in various methods of the
`GameLocation` class, particularly `resetLocalState`.</small>\
<small>² The `T` value (short for *true*) is conventional, but any
non-empty value will work too.</small>

## Known tile properties

This excludes very specialised properties like
`TouchAction WomensLocker`.¹

### General

<table>
<thead>
<tr>
<th><p>layer</p></th>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>BeachSpawn T</samp>²</p></td>
<td><p>Allows spawning of beach-related forage and supply crates on this
tile, when using the beach farm type.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>Bed T</samp>²</p></td>
<td><p>If the player stands on this tile, they're considered in bed for
the purposes of stamina regen (in multiplayer) and pass-out
logic.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>Buildable T</samp>²</p></td>
<td><p>Allows farm buildings to be placed on this tile if there are no
other obstructions.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>DefaultBedPosition T</samp>²</p></td>
<td><p>Used in the upgraded farmhouse for the initial placement of the
player bed and when migrating saves.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>DefaultChildBedPosition T</samp>²</p></td>
<td><p>Used in the upgraded farmhouse for the initial placement of the
child beds.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>Diggable T</samp>²</p></td>
<td><p>Marks the tile as diggable with the hoe and enables planting
crops. Also allows <a href="grass" class="wikilink"
title="grass">grass</a> to spread to this tile.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NoFishing T</samp>²</p></td>
<td><p>Prevents the player from casting the line onto this tile when
fishing.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NoFurniture T</samp>²</p></td>
<td><p>Prevents the player from placing objects on this tile (not just
furniture).</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NoPath T</samp>²</p></td>
<td><p>Excludes this tile from NPC pathing, making them go around it if
necesssary.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NoSpawn All</samp><br />
<samp>NoSpawn True</samp></p></td>
<td><p>Prevents spawning of forage items, debris (<em>e.g.,</em> weeds
or stones), and wild trees on this tile.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NoSpawn False</samp></p></td>
<td><p>Disables any previous <samp>NoSpawn</samp> property on the tile.
For example, this can be used to enable spawning on a tile which has a
<samp>NoSpawn</samp> tile index property.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NoSpawn Grass</samp></p></td>
<td><p>Prevents debris (<em>e.g.,</em> weeds or stones) from spawning on
this tile.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NoSpawn Tree</samp></p></td>
<td><p>Prevents trees from spawning on this tile. Prevents the player
from planting trees on this tile, except on the farm. If a tree is
already on this tile, prevents it from growing.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NoSprinklers T</samp>²</p></td>
<td><p>Prevents sprinklers from being placed on this tile.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>NPCBarrier T</samp>²</p></td>
<td><p>Prevents NPCs from crossing this tile when used on the Farm
(including coops, barns, and slime hutches), UndergroundMine, or the
island. Also prevents some spawns on this tile, in those
locations.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>Passable T</samp>²</p></td>
<td><p>Prevents players from walking or placing objects on this tile,
even if they'd normally be able to do. (Direct opposite of
<samp>Buildings Passable T</samp> below.) Commonly used on certain water
tiles for bordering the sides of bridges, to prevent players from
walking off into open water. Can be added as a single TileData object
for a specific tile, or (more commonly) to every instance of a tile by
editing the tileset and adding it to the tile index.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TemporaryBarrier T</samp>²</p></td>
<td><p>Used only briefly when doors open. Marks this tile impassable to
a player, while NPCs will treat it as an obstacle to pause before
rushing through.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>Type &lt;str type&gt;</samp></p></td>
<td><p>Sets the tile type for various game logic (<em>e.g.,</em> step
sounds or planting crops), where &lt;type&gt; is one of <em>Dirt</em>,
<em>Stone</em>, <em>Grass</em>, or <em>Wood</em>.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>Water T</samp>²</p></td>
<td><p>Marks the tile as a water tile for various game logic
(<em>i.e.,</em> items splash into it, can refill watering can from it,
can possibly fish in it, can possibly place crab pots in it, will water
nearby paddy crops, will block most open-tile checks, will regenerate
health in it if indoors, and will draw animated overlay over it if
indoors, outdoors, in the Mines, Sewer, or Submarine; or otherwise not
in the Desert). <em>Setting the value to I (uppercase i) will make the
tile behave like normal water, without rendering the water animation
overlay.</em></p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>WaterSource T</samp>²</p></td>
<td><p>Lets the player refill the watering can from this tile.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>Trough T</samp>²</p></td>
<td><p>Allows hay to be placed on this tile for animals to eat</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>LockedDoorMessage &lt;string data asset
path&gt;</samp></p></td>
<td><p>Used to produce a dialogue box when the conditions of
<samp>ConditionalDoor</samp> aren't met. Uses the text string from the
supplied string data asset. See <a href="Modding_Dialogue"
class="wikilink" title="dialogue format">dialogue format</a> for how to
format the string.<br />
<em>Example: LockedDoorMessage
Strings\\\\1_6_Strings:guild_door</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>NPCPassable T</samp>²</p></td>
<td><p>NPC-only version of <samp>Passable</samp> below. Allows NPCs to
pass through this tile.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Passable T</samp>²</p></td>
<td><p>Allows passing through a tile, even though Buildings tiles can't
normally be walked through. Often used for small footbridges that need
to be on Buildings, over water. Direct opposite of <samp>Back Passable
T</samp> above. Can be added as a single TileData object for a specific
tile, or (more commonly) to every instance of a tile by editing the
tileset and adding it to the tile index.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>ProjectilePassable T</samp>²</p></td>
<td><p>Allows projectiles to cross tiles that would normally block them
(<em>e.g.,</em> to allow shooting into lava pools)</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Shadow T</samp>²</p></td>
<td><p>Player-only version of <samp>Passable</samp> above. Allows the
player to pass through this tile, but not NPCs.</p></td>
</tr>
<tr>
<td><p><samp>Paths</samp></p></td>
<td><p><samp>Order &lt;I&gt;</samp></p></td>
<td><p>To place on index 29 and 30 of the Paths tilsheet. Set the order
the cabins will spawn at the creation of a Multiplayer save.</p></td>
</tr>
<tr>
<td><p><samp>Paths</samp></p></td>
<td><p><samp>SpawnTree &lt;type&gt; &lt;ID&gt; [stage on spawn] [stage
on regrow]</samp></p></td>
<td><p>Spawns a tree when the map is created, where:</p>
<ul>
<li>&lt;type&gt; is <samp>wild</samp> (spawn a <a href="trees"
class="wikilink" title="wild tree">wild tree</a>) or <samp>fruit</samp>
(spawn a <a href="Fruit_Trees" class="wikilink" title="fruit tree">fruit
tree</a>).</li>
<li>&lt;ID&gt; is the tree's key in <samp>Data/FruitTrees</samp> or
<samp>Data/WildTrees</samp>.</li>
<li>[stage on spawn] is the preferred tree growth stage when first
populating the save (if applicable).</li>
<li>[stage on regrow] is the preferred tree growth stage when regrowing
trees on day update (if applicable).</li>
</ul>
<p>The tile must have <a href="#Paths_layer" class="wikilink"
title="Paths tile index"><samp>Paths</samp> tile index</a> 34.</p></td>
</tr>
</tbody>
</table>

### TouchAction

The `TouchAction` property makes something happen when the player steps
on the tile:

<table>
<thead>
<tr>
<th><p>layer</p></th>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction ChangeIntoSwimsuit</samp></p></td>
<td><p>Changes the player into their swimsuit and disables
running.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction ChangeOutOfSwimsuit</samp></p></td>
<td><p>Changes the player into their regular clothes and enables
running.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction ConditionalDoor &lt;query&gt;</samp></p></td>
<td><p>Uses a <a href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> to check if the player is
allowed to pass this tile. If a <samp>LockedDoorMessage</samp> tile
property is on the same tile and the query fails, a dialogue box with
the supplied text string will be dislayed; Otherwise, if the query fails
then a generic "It's locked..." dialogue will be shown.<br />
<em>Example: ConditionalDoor PLAYER_STAT Current monstersKilled
1000</em></p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction DesertBus</samp></p></td>
<td><p>Lets you ride the bus back to the Bus Stop.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction Emote &lt;string npc&gt; &lt;int
emoteID&gt;</samp></p></td>
<td><p>Finds the NPC whose name matches the &lt;npc&gt; field, and
causes them to show the given &lt;emoteID&gt; above their head (4: empty
can, 8: question mark, 12: angry, 16: exclamation, 20: heart, 24: sleep,
28: sad, 32: happy, 36: x, 40: pause, 52: videogame, 56: music note, 60:
blush).</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction FaceDirection &lt;string npc&gt; &lt;int
direction&gt;</samp></p></td>
<td><p>Finds the NPC whose name matches the &lt;npc&gt; field, and make
them face the given direction (0: up, 1: right, 2: down, 3:
left).</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction legendarySword</samp></p></td>
<td><p>Gives them the <a href="Galaxy_Sword" class="wikilink"
title="Galaxy Sword">Galaxy Sword</a> when holding a <a
href="Prismatic_Shard" class="wikilink"
title="Prismatic Shard">Prismatic Shard</a>.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction MagicWarp &lt;string area&gt; &lt;int x&gt;
&lt;int y&gt; [string prerequisite]</samp></p></td>
<td><p>Warps the player to the &lt;x&gt; &lt;y&gt; tile coordinates in
the given &lt;area&gt; with a magic sound and effects. If the
[prerequisite] field is specified, only occurs if that flag is set via
<samp>Game1.player.mailReceived</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction PlayEvent &lt;event id&gt; [check
preconditions] [skip if seen] [fallback action]</samp></p></td>
<td><p>Equivalent to <samp>Action PlayEvent</samp>, but activated on
touch. Note that [fallback action] is an <samp>Action</samp> tile
property, <em>not</em> a <samp>TouchAction</samp> tile
property.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction PoolEntrance</samp></p></td>
<td><p>Switches the player between swimming and walking mode.</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction Sleep</samp></p></td>
<td><p>Ends the day if the player confirms. (Requires the Bed tile
property to function as a bed)</p></td>
</tr>
<tr>
<td><p><samp>Back</samp></p></td>
<td><p><samp>TouchAction Warp &lt;string area&gt; &lt;int x&gt; &lt;int
y&gt; [string prerequisite]</samp></p></td>
<td><p>Adds a player-only warp on the tile to the specified location
name and position. This is exactly equivalent to <samp>TouchAction
MagicWarp</samp>, but without the magic sound/visual effect.</p></td>
</tr>
</tbody>
</table>

### Action

The `Action` property makes something happen when the player interacts
(*e.g.,* clicks) with the tile:

<table>
<thead>
<tr>
<th><p>layer</p></th>
<th><p>property</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action AdventureShop</samp></p></td>
<td><p>Shows the Adventurer's Guild shop screen.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Arcade_Prairie</samp></p></td>
<td><p>Shows the <em>Journey of the Prairie King</em> arcade
game.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Arcade_Minecart</samp></p></td>
<td><p>Shows the <em>Junimo Kart</em> arcade game.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Bobbers</samp></p></td>
<td><p>Shows the Fishing Bobber customization menu.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action BuyBackpack</samp></p></td>
<td><p>Shows a menu which lets the player upgrade their backpack if an
upgrade is available.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Billboard</samp></p></td>
<td><p>Shows the calendar menu.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Blacksmith</samp></p></td>
<td><p>Opens Clint's shop menu, if Clint is nearby.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Buy</samp></p></td>
<td><p>In the SeedShop, opens Pierre's shop menu, if Pierre is nearby
(or the box version if he's visiting Ginger Island). In Sandy's house,
opens Sandy's shop menu, if Sandy is neaby. Does nothing in other
locations.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action BrokenBeachBridge</samp></p></td>
<td><p>Prompts you to use wood to repair the bridge.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action BuildingSilo</samp></p></td>
<td><p>If a building covers this tile, enables <a href="silo"
class="wikilink" title="silo">silo</a> interactions on this tile subject
to the building's <samp>HayCapacity</samp> field in
<samp>Data/Buildings</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action BuildingToggleAnimalDoor</samp></p></td>
<td><p>If a building covers this tile, opens or closes its animal
door.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action BuyQiCoins</samp></p></td>
<td><p>Shows a dialogue which lets the player buy 100 Casino club
coins.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Concessions</samp></p></td>
<td><p>Opens the snack shop in the theater. (Only from inside the
theater.)</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ConditionalDoor &lt;query&gt;</samp></p></td>
<td><p>Place on an interior door's bottom tile. Must be used in
conjunction with the <samp>Doors</samp> map property. Uses a <a
href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> to check if the player can
open the door. If a <samp>LockedDoorMessage</samp> tile property is on
the same tile and the query fails, a dialogue box with the supplied text
string will be dislayed; Otherwise, if the query fails then a generic
"It's locked..." dialogue will be shown.<br />
<em>Example: ConditionalDoor PLAYER_STAT Current monstersKilled
1000</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Carpenter</samp></p></td>
<td><p>Opens the carpenter menu, if Robin is nearby.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ColaMachine</samp></p></td>
<td><p>Offers to let the player buy a Joja cola.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ClubCards</samp><br />
<samp>Action Blackjack</samp></p></td>
<td><p>Shows the casino blackjack minigame.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ClubComputer</samp><br />
<samp>Action FarmerFile</samp></p></td>
<td><p>Shows a dialogue with play stats (steps taken, gifts given, dirt
hoed, etc).</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ClubSeller</samp></p></td>
<td><p>Shows a dialogue which lets the player buy a <a
href="Statue_Of_Endless_Fortune" class="wikilink"
title="Statue Of Endless Fortune">Statue Of Endless Fortune</a> for one
million gold.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ClubShop</samp></p></td>
<td><p>Shows the casino shop menu.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ClubSlots</samp></p></td>
<td><p>Shows the casino slots minigame.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ForestPylon</samp></p></td>
<td><p>Shows the event giving you the <a href="Meowmere"
class="wikilink" title="Meowmere">Meowmere</a> sword if the player is
holding the <a href="Far_Away_Stone" class="wikilink"
title="Far Away Stone">Far Away Stone</a>. If the player isn't holding
the stone a dialogue box appears saying "It is a receptacle of unknown
origins."</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Dialogue &lt;text&gt;</samp></p></td>
<td><p>Shows a generic dialogue box with the given text. See <a
href="Modding_Dialogue" class="wikilink"
title="dialogue format">dialogue format</a>.<br />
<em>Example: Action Dialogue Hi there @!</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action DivorceBook</samp></p></td>
<td><p>Shows divorce options for the player's current marriage status
(as if they clicked the <a href="Marriage#Divorce" class="wikilink"
title="divorce book">divorce book</a>).</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>&lt;span id="anchor_door"&gt;Action Door&lt;/span&gt;
[npcName]+</samp></p></td>
<td><p>Sets up an interior door. If used without NPC names, the door can
be opened at any time. If used with one or more (internal) NPC names it
cannot be opened unless the player has two or more hearts of friendship
with any of the named NPC(s). Placed on the lower of the two door tiles.
Used with the <samp>[[#anchor_doors|Doors]]</samp> map property - both
are required for interior doors to function.<br />
<em>Example: Action Door Abigail</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action DropBox &lt;ID&gt;</samp></p></td>
<td><p>A location that allows the player to drop off items when a <a
href="Modding_Special_orders" class="wikilink"
title="special order">special order</a> with the given &lt;ID&gt; is
active.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action DyePot</samp></p></td>
<td><p>Opens the Dye Pot menu, Must have seen event <em>992559</em> for
it to open. (The event of Emily visiting the farmhouse after you have
gotten your first piece of cloth.)</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ElliottBook</samp></p></td>
<td><p>Displays the text <em>Blank book</em>.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ElliottPiano &lt;1-4&gt;</samp></p></td>
<td><p>Plays one of four possible piano notes. <em>ElliottPiano 1</em>
plays the lowest note and <em>ElliottPiano 4</em> plays the highest
note.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action EnterSewer</samp></p></td>
<td><p>Warps you to the sewer if you have obtained the key.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action EvilShrineLeft</samp></p></td>
<td><p>Turns your kids into doves for a prismatic shard.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action EvilShrineCenter</samp></p></td>
<td><p>Erases your ex-spouses memory of you.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action EvilShrineRight</samp></p></td>
<td><p>Toggles monster spawning for your farm.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action FixRaccoonStump</samp></p></td>
<td><p>Prompts you to use 100 Hardwood to fix the stump.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Forge</samp></p></td>
<td><p>Opens the <a href="Forge" class="wikilink"
title="Forge">Forge</a> menu.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Garbage &lt;ID&gt;</samp></p></td>
<td><p>Has a chance to give a specific item to the player based on the
&lt;ID&gt;. Can only be clicked once per day. TODO: Explain what each
&lt;ID&gt; means.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Gunther</samp></p></td>
<td><p>Opens the museum menu where you can donate artifacts or claim
rewards.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action HMTGF</samp></p></td>
<td><p>Gives you "<a href="??HMTGF??" class="wikilink"
title="??HMTGF??">??HMTGF??</a>" when you have a <a
href="Super_Cucumber" class="wikilink" title="Super Cucumber">Super
Cucumber</a> in your hand.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action IceCreamStand</samp></p></td>
<td><p>If Summer, shows the Ice Cream Stand shopping screen. Otherwise,
the player will be told to come back in the summer. (Needs an NPC behind
the stand.)</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action JojaShop</samp></p></td>
<td><p>Shows the Joja shopping screen.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Jukebox</samp></p></td>
<td><p>Shows the jukebox menu to choose the ambient music.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action kitchen</samp><br />
<em>(valid in any location)</em></p></td>
<td><p>Shows the cooking menu.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Letter &lt;string messageKey&gt;</samp></p></td>
<td><p>Loads a message with the given key from the
<em>Content\Strings\StringsFromMaps.xnb</em> file and displays it
on-screen as a letter. Uses the same syntax as
<em>Data\mail.xnb</em>.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action LockedDoorWarp &lt;int toX&gt; &lt;int toY&gt;
&lt;string toArea&gt; &lt;int openTime&gt; &lt;int closeTime&gt; [NPC]
[friendship]</samp></p></td>
<td><p>Creates an activation warp normally used on doors with a time
window for when it can be used (the times can be set to <samp>600
2600</samp> to keep the door unlocked all the time). Note that you must
use 24-hour times, <em>i.e.,</em> 2000 for 8pm. The last two terms, if
specified, add a friendship requirement on top of the time
requirement.<br />
<em>Example: 7 9 LeahHouse 1000 1800 Leah 500</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action LuauSoup</samp></p></td>
<td><p>Used for the Luau Festival, this is where you insert a food item
for the soup.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action MagicInk</samp></p></td>
<td><p>Adds the Magic Ink to your wallet.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action MasteryRoom</samp></p></td>
<td><p>If you don't have skill 10 in every skill a dialogue box appears
saying "Only a master of the five ways may enter (X/5)", If you do it
warps you into the <a href="Mastery_Cave" class="wikilink"
title="Mastery Cave">Mastery Cave</a>.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Mailbox</samp></p></td>
<td><p>Shows the next letter from the player's mailbox (if
any).</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Message &lt;string messageKey&gt;</samp></p></td>
<td><p>Loads a message with the given key from the
<em>Content\Strings\StringsFromMaps.xnb</em> file and displays it in a
dialogue box.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action MessageOnce &lt;int eventID&gt; &lt;string
message&gt;</samp></p></td>
<td><p>If the player hasn't seen the event with ID &lt;eventID&gt;,
marks that event seen and displays the given message text in a dialogue
box. This does <em>not</em> parse <a href="Modding_Dialogue"
class="wikilink" title="dialogue format">dialogue format</a>.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action MessageSpeech &lt;string
messageKey&gt;</samp></p></td>
<td><p>Identical to <samp>Action Message</samp>, but replaces the usual
inspection cursor with a speech cursor.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action MineSign &lt;string message&gt;</samp></p></td>
<td><p>Shows a mini-dialogue box with the given raw message text. This
does <em>not</em> parse <a href="Modding_Dialogue" class="wikilink"
title="dialogue format">dialogue format</a>.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action MinecartTransport</samp></p></td>
<td><p>Shows the minecart destination menu (or a message if not
unlocked).</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action MineElevator</samp></p></td>
<td><p>Shows the mine elevator menu (to warp to a mine level) if the
player has reached mine level 5+, else a mine elevator not working
message.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action NextMineLevel</samp></p></td>
<td><p>Warps the player to the next mine level (or level 1 if they're
not in the mine).</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action None</samp></p></td>
<td><p>Does nothing. This is used to mark the tile interactive if the
click will be handled separately.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Notes &lt;int noteID&gt;</samp></p></td>
<td><p>If the player has found the specified lost book, displays its
museum note text and marks it read.<br />
<em>Example: Action Notes 17</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action NPCMessage &lt;str name&gt; "&lt;str
dialogueKey1&gt;/&lt;str dialogueKey2&gt;"</samp></p></td>
<td><p>If the named NPC is within 14 tiles of the player, reads
dialogueKey1 from the string files and displays a dialogue box, and
broadcasts a chat to multiplayer games that player was caught snooping.
Otherwise, reads dialogueKey2 in a dialogue box. See <a
href="Modding_Dialogue" class="wikilink"
title="dialogue format">dialogue format</a>.<br />
<em>Example: Action NPCMessage Marnie
"Strings\\StringsFromMaps:AnimalShop.20/Strings\\StringsFromMaps:AnimalShop.21"</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action NPCSpeechMessageNoRadius &lt;str name&gt; &lt;str
messageKey&gt;</samp></p></td>
<td><p>Loads a message with the given key from the
<em>Content\Strings\StringsFromMaps.xnb</em> file and displays it in a
dialogue box with the named NPC portrait.<br />
<em>Note: This is currently only used in the C# source for NPCs at the
MovieTheater, but can be used elsewhere. The NPC does not have to be a
fully-realized character as long as it has a portrait matching the name
loaded into the Portraits directory.</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action ObeliskWarp &lt;location name&gt; &lt;x&gt;
&lt;y&gt; [whether to dismount]</samp></p></td>
<td><p>Warps the player to the specified location name and position with
the <a href="Warp_Totem" class="wikilink" title="Obelisk">Obelisk</a>
animation/sound effects. This map property will generate a warning in
the log about being an unknown warp property even when used correctly -
this warning can be ignored.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action OpenShop &lt;shop id&gt; [from direction] [open
time] [close time] [owner tile area]</samp></p></td>
<td><p>Open the <a href="Modding_Shops" class="wikilink"
title="shop">shop</a> with the given &lt;shop id&gt;. All arguments
besides the ID are optional:</p>
<ul>
<li>[from direction]: if specified, the player must be standing in this
direction relative to the shop (one of <samp>down</samp>,
<samp>up</samp>, <samp>left</samp>, <samp>right</samp>, or
<samp>none</samp>). Setting this to <samp>none</samp> disables the
requirement. The default for most vanilla shops is
<samp>down</samp>.</li>
<li>[open time] and [close time]: the start &amp; end times in 26-hour
format when the shop is interactable. During this time, the shop can be
closed using a <samp>ClosedMessage</samp> in its <a href="Modding_Shops"
class="wikilink" title="Data/Shops">Data/Shops</a> entry. Interacting
with the tile outside of [open time] and [close time] does nothing. If
omitted, the shop will default to being open at all hours.</li>
<li>[owner tile area]: if specified, the tile area which must contain
one of the shop owners for the shop to be interactable. For a custom
shop, these are defined by its <samp>Owners</samp> field. This must be
written as: <samp>&lt;x&gt; &lt;y&gt; &lt;width&gt;
&lt;height&gt;</samp>. If omitted, the shop menu will force open
regardless of whether the shop owner is present and skip any
<samp>Owners</samp> entries containing <samp>ClosedMessage</samp>.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action PlayEvent &lt;event id&gt; [check preconditions]
[skip if seen] [fallback action]</samp></p></td>
<td><p>Immediately start an <a href="Modding_Event_data"
class="wikilink" title="event">event</a>, subject to the conditions:</p>
<ul>
<li>[check preconditions]: whether to ignore the action if the <a
href="Modding_Event_data#Event_preconditions" class="wikilink"
title="event&#39;s preconditions">event's preconditions</a> don't match
(one of <samp>true</samp> or <samp>false</samp>). Default true.</li>
<li>[skip if seen]: whether to ignore the action if the player has
already seen the given event. Default true.</li>
</ul>
<p>If the event doesn't start for any reason (including the preceding
conditions):</p>
<ul>
<li>If [fallback action] is specified, it'll be run as an action. This
can be any <samp>Action</samp> tile property (without the "Action "
prefix), like
<code>Action PlayEvent 60367 true true PlayEvent 520702 false false</code>
to play a different event.</li>
<li>Otherwise the action is silently ignored.</li>
</ul>
<p>For example, <code>Action PlayEvent 60367 false false</code> will
replay the bus arrival event from the start of the game.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action playSound &lt;str cueName&gt;</samp></p></td>
<td><p>Play the sound or music with the given name.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action QiChallengeBoard</samp></p></td>
<td><p>Opens the request/challenge board from the Mr Qi walnut
room.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action QiCoins</samp></p></td>
<td><p>Shows a dialogue which lets the player buy 10 Casino club coins
if they have none, else shows how many they have.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action QiGemShop</samp></p></td>
<td><p>Opens the Mr Qi walnut room shop.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Saloon</samp></p></td>
<td><p>Opens the Saloon menu, if Gus is nearby.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action SandDragon</samp></p></td>
<td><p>Used for Part 3 of the Mysterious Mr. Qi Quest.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action SpecialWaterDroppable</samp></p></td>
<td><p>If the player is holding an <a href="Ancient_Doll"
class="wikilink" title="Ancient Doll">Ancient Doll</a>, it will be
thrown to the right of the tile and the player will receive a <a
href="Far_Away_Stone" class="wikilink" title="Far Away Stone">Far Away
Stone</a>.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Shop</samp></p></td>
<td><p>On festival maps, opens the festival shop. No effect on
non-festival maps.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action SkullDoor</samp></p></td>
<td><p>Warps the player into the skull caverns if they have the <a
href="Skull_Key" class="wikilink" title="Skull Key">Skull Key</a> if
they have it unlocked.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Theater_BoxOffice</samp></p></td>
<td><p>Opens the ticket menu for the theater, if you have it
unlocked.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action TownMailbox &lt;ID&gt;</samp></p></td>
<td><p>Unused.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Tailoring</samp></p></td>
<td><p>Opens the tailoring menu like the one in Emily and Haleys house.
Must have seen event <em>992559</em> for it to open. (The event of Emily
visiting the farmhouse after you have gotten your first piece of
cloth.)</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action TunnelSafe</samp></p></td>
<td><p>Starts the The Mysterious Qi quest if you have a Battery Pack
selected.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action Warp &lt;int x&gt; &lt;int y&gt; &lt;str
area&gt;</samp></p></td>
<td><p>Warps the player to the &lt;x&gt; &lt;y&gt; tile coordinate in
the &lt;area&gt; game location.<br />
<em>Example: Action Warp 76 9 Mountain</em></p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action WarpCommunityCenter</samp></p></td>
<td><p>Warps the player to the inside of the Community Center if they
have access (else show an "it's locked" message).</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action WarpGreenhouse</samp></p></td>
<td><p>Warps the player to the inside of their greenhouse if they've
unlocked it, else shows a message about the greenhouse ruins.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action WizardBook</samp></p></td>
<td><p>If unlocked, you buy buildings from the wizard here.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action WizardHatch</samp></p></td>
<td><p>If you're good enough friends with the wizard you warp to his
basement, if not you get told you can't go in.</p></td>
</tr>
<tr>
<td><p><samp>Buildings</samp></p></td>
<td><p><samp>Action WizardShrine</samp></p></td>
<td><p>Shows the character customisation menu normally available from
the Wizard's tower.</p></td>
</tr>
</tbody>
</table>

<small>¹ Tile properties are handled throughout the codebase using
`GameLocation::doesTileHaveProperty`. Actions and touch actions are
handled by `GameLocation::performAction` and
`GameLocation::performTouchAction` respectively. Emote IDs are listed as
`Character` constants.</small>\
<small>² The `T` value (short for *true*) is conventional, but any
non-empty value will work too.</small>

### Custom Actions

C# mods can handle custom `Action` & `TouchAction` map properties by
calling `GameLocation.RegisterTileAction` & `RegisterTouchAction`, and
passing a callback which receives the location, map property arguments,
player who activated it, and tile position.

For example, let's say you want a locked gate which needs a custom key
item. You can add a regular `TouchAction Example.ModId_UnlockGate` map
property (e.g. by adding it directly in the map file, or using
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a>'s `EditMap`, or using the
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="content API">content API</a>). Then you can just handle the logic
from your C# mod:

As another example, let's say you want the gate to unlock when the
player presses the action key. You can add a regular
`Action Example.ModId_UnlockGate` map property (e.g. by adding it
directly in the map file, or using
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a>'s `EditMap`, or using the
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="content API">content API</a>). Then you can just handle the logic
from your C# mod:
