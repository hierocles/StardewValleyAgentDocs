---
title: "World"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, world]
---
### World

`this.Helper.Events.World` has events raised when the in-game world
changes in some way.

<table>
<thead>
<tr>
<th><p>event</p></th>
<th><p>summary</p>
<h4 id="locationlistchanged">LocationListChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after a game location is added or removed (including building
interiors).</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;GameLocation&gt;</samp></p></td>
<td><p>A list of locations added since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;GameLocation&gt;</samp></p></td>
<td><p>A list of locations removed since the last update tick.</p></td>
</tr>
</tbody>
</table>
<h4 id="buildinglistchanged">BuildingListChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after buildings are added/removed in any location.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Location</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The location which changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;Building&gt;</samp></p></td>
<td><p>A list of buildings added since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;Building&gt;</samp></p></td>
<td><p>A list of buildings removed since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.IsCurrentLocation</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether <samp>e.Location</samp> is the location containing the
local player.</p></td>
</tr>
</tbody>
</table>
<h4 id="chestinventorychanged">ChestInventoryChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after items are added or removed from a chest's inventory.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Chest</samp></p></td>
<td><p><samp>Chest</samp></p></td>
<td><p>The chest whose inventory changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Location</samp></p></td>
<td><p><samp>Location</samp></p></td>
<td><p>The location containing the chest.</p></td>
</tr>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;Item&gt;</samp></p></td>
<td><p>The added item stacks.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;Item&gt;</samp></p></td>
<td><p>The removed item stacks.</p></td>
</tr>
<tr>
<td><p><samp>e.QuantityChanged</samp></p></td>
<td><p><samp>IEnumerable&lt;ItemStackSizeChange&gt;</samp></p></td>
<td><p>The item stacks whose quantity changed. Each
<samp>ItemStackSizeChange</samp> instance includes <samp>Item</samp>
(the affected item stack), <samp>OldSize</samp> (the previous stack
size), and <samp>NewSize</samp> (the new stack size).</p></td>
</tr>
</tbody>
</table>
<h4 id="debrislistchanged">DebrisListChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after debris is added/removed in any location (including
dropped or spawned floating items).</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Location</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The location which changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;Debris&gt;</samp></p></td>
<td><p>A list of debris added since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;Debris&gt;</samp></p></td>
<td><p>A list of debris removed since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.IsCurrentLocation</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether <samp>e.Location</samp> is the location containing the
local player.</p></td>
</tr>
</tbody>
</table>
<h4 id="furniturelistchanged">FurnitureListChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after furniture are added/removed in any location.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Location</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The location which changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;Furniture&gt;</samp></p></td>
<td><p>A list of furniture added since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;Furniture&gt;</samp></p></td>
<td><p>A list of furniture removed since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.IsCurrentLocation</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether <samp>e.Location</samp> is the location containing the
local player.</p></td>
</tr>
</tbody>
</table>
<h4
id="largeterrainfeaturelistchanged">LargeTerrainFeatureListChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after large terrain features (like bushes) are added/removed
in any location.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Location</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The location which changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;LargeTerrainFeature&gt;</samp></p></td>
<td><p>A list of large terrain features added since the last update
tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;LargeTerrainFeature&gt;</samp></p></td>
<td><p>A list of large terrain features removed since the last update
tick.</p></td>
</tr>
<tr>
<td><p><samp>e.IsCurrentLocation</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether <samp>e.Location</samp> is the location containing the
local player.</p></td>
</tr>
</tbody>
</table>
<h4 id="npclistchanged">NpcListChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after NPCs are added/removed in any location (including
villagers, horses, Junimos, monsters, and pets).</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Location</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The location which changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;NPC&gt;</samp></p></td>
<td><p>A list of NPCs added since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;NPC&gt;</samp></p></td>
<td><p>A list of NPCs removed since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.IsCurrentLocation</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether <samp>e.Location</samp> is the location containing the
local player.</p></td>
</tr>
</tbody>
</table>
<h4 id="objectlistchanged">ObjectListChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after objects are added/removed in any location (including
machines, fences, etc). This doesn't apply for floating items (see
<samp>DebrisListChanged</samp>) or furniture (see
<samp>FurnitureListChanged</samp>).</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Location</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The location which changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;KeyValuePair&lt;Vector2,
Object&gt;&gt;</samp></p></td>
<td><p>A list of <a href="Modding_Modder_Guide_Game_Fundamentals#Tiles"
class="wikilink" title="tile coordinate">tile coordinate</a> + object
pairs added since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;KeyValuePair&lt;Vector2,
Object&gt;&gt;</samp></p></td>
<td><p>A list of <a href="Modding_Modder_Guide_Game_Fundamentals#Tiles"
class="wikilink" title="tile coordinate">tile coordinate</a> + object
pairs removed since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.IsCurrentLocation</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether <samp>e.Location</samp> is the location containing the
local player.</p></td>
</tr>
</tbody>
</table>
<h4 id="terrainfeaturelistchanged">TerrainFeatureListChanged</h4>
<p><em>Group:</em> <code>World</code></p>
<p>Raised after terrain features are added/removed in any location
(including trees, hoed dirt, and flooring). For bushes, see
<samp>LargeTerrainFeatureListChanged</samp>.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Location</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The location which changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Added</samp></p></td>
<td><p><samp>IEnumerable&lt;KeyValuePair&lt;Vector2,
TerrainFeature&gt;&gt;</samp></p></td>
<td><p>A list of <a href="Modding_Modder_Guide_Game_Fundamentals#Tiles"
class="wikilink" title="tile coordinate">tile coordinate</a> + terrain
feature pairs added since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.Removed</samp></p></td>
<td><p><samp>IEnumerable&lt;KeyValuePair&lt;Vector2,
TerrainFeature&gt;&gt;</samp></p></td>
<td><p>A list of <a href="Modding_Modder_Guide_Game_Fundamentals#Tiles"
class="wikilink" title="tile coordinate">tile coordinate</a> + terrain
feature pairs removed since the last update tick.</p></td>
</tr>
<tr>
<td><p><samp>e.IsCurrentLocation</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether <samp>e.Location</samp> is the location containing the
local player.</p></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
