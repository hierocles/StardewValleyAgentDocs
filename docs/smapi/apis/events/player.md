---
title: "Player"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, player]
---
### Player

`this.Helper.Events.Player` has events raised when the player data
changes.

**Currently these events are only raised for the current player. That
will likely change in a future version, so make sure to check
`e.IsLocalPlayer` if you only want to handle the current player.**

<table>
<thead>
<tr>
<th><p>event</p></th>
<th><p>summary</p>
<h4 id="inventorychanged">InventoryChanged</h4>
<p><em>Group:</em> <code>Player</code></p>
<p>Raised after items are added or removed from the player
inventory.</p>
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
<td><p><samp>e.Player</samp></p></td>
<td><p><samp>Farmer</samp></p></td>
<td><p>The player whose inventory changed.</p></td>
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
<tr>
<td><p><samp>e.IsLocalPlayer</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether the affected player is the local one.</p></td>
</tr>
</tbody>
</table>
<h4 id="levelchanged">LevelChanged</h4>
<p><em>Group:</em> <code>Player</code></p>
<p>Raised after a player's skill level changes. When the player levels
up normally, this is raised immediately (not when the game notifies the
player after they go to bed).</p>
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
<td><p><samp>e.Player</samp></p></td>
<td><p><samp>Farmer</samp></p></td>
<td><p>The player whose skill level changed.</p></td>
</tr>
<tr>
<td><p><samp>e.Skill</samp></p></td>
<td><p><samp>SkillType</samp></p></td>
<td><p>The skill whose level changed. This is a constant like
<code>SkillType.Combat</code>, which can be converted to the game's
internal skill ID using <code>(int)e.Skill</code>.</p></td>
</tr>
<tr>
<td><p><samp>e.OldLevel</samp></p></td>
<td><p><samp>int</samp></p></td>
<td><p>The player's previous level for that skill.</p></td>
</tr>
<tr>
<td><p><samp>e.NewLevel</samp></p></td>
<td><p><samp>int</samp></p></td>
<td><p>The player's new level for that skill.</p></td>
</tr>
<tr>
<td><p><samp>e.IsLocalPlayer</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether the affected player is the local one.</p></td>
</tr>
</tbody>
</table>
<h4 id="warped">Warped</h4>
<p><em>Group:</em> <code>Player</code></p>
<p>Raised after the current player moves to a new location.</p>
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
<td><p><samp>e.Player</samp></p></td>
<td><p><samp>Farmer</samp></p></td>
<td><p>The player who warped to a new location.</p></td>
</tr>
<tr>
<td><p><samp>e.OldLocation</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The player's previous location.</p></td>
</tr>
<tr>
<td><p><samp>e.NewLocation</samp></p></td>
<td><p><samp>GameLocation</samp></p></td>
<td><p>The player's new location.</p></td>
</tr>
<tr>
<td><p><samp>e.IsLocalPlayer</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether the affected player is the local one.</p></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
