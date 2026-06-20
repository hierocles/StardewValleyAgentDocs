---
title: "Multiplayer"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, multiplayer]
---
### Multiplayer

`this.Helper.Events.Multiplayer` has events raised for multiplayer
messages and connections.

<table>
<thead>
<tr>
<th><p>event</p></th>
<th><p>summary</p>
<h4 id="peercontextreceived">PeerContextReceived</h4>
<p><em>Group:</em> <code>Multiplayer</code></p>
<p>Raised after the mod context for a player is received. The event is
raised for any player (whether host or farmhand), including when the
connecting player doesn't have SMAPI installed. This is the earliest
point where messages can be sent to the player via SMAPI.</p>
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
<td><p><samp>e.Peer</samp></p></td>
<td><p><samp>IMultiplayerPeer</samp></p></td>
<td><p>The peer whose context was received (see <a
href="Modding_Modder_Guide_APIs_Multiplayer#Get_connected_player_info"
class="wikilink"
title="Multiplayer#Get connected player info">Multiplayer#Get connected
player info</a>).</p></td>
</tr>
</tbody>
</table>
<h4 id="peerconnected">PeerConnected</h4>
<p><em>Group:</em> <code>Multiplayer</code></p>
<p>Raised after a connection from another player is approved by the
game. The event is raised for any player (whether host or farmhand),
including when the connecting player doesn't have SMAPI installed. This
happens after <samp>PeerContextReceived</samp>.</p>
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
<td><p><samp>e.Peer</samp></p></td>
<td><p><samp>IMultiplayerPeer</samp></p></td>
<td><p>The peer who connected (see <a
href="Modding_Modder_Guide_APIs_Multiplayer#Get_connected_player_info"
class="wikilink"
title="Multiplayer#Get connected player info">Multiplayer#Get connected
player info</a>).</p></td>
</tr>
</tbody>
</table>
<h4 id="modmessagereceived">ModMessageReceived</h4>
<p><em>Group:</em> <code>Multiplayer</code></p>
<p>Raised after <a
href="Modding_Modder_Guide_APIs_Multiplayer#Send_messages"
class="wikilink" title="a mod message">a mod message</a> is received
over the network.</p>
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
<td><p><samp>e.FromPlayerID</samp></p></td>
<td><p><samp>long</samp></p></td>
<td><p>The unique ID of the player from whose computer the message was
sent.</p></td>
</tr>
<tr>
<td><p><samp>e.FromModID</samp></p></td>
<td><p><samp>string</samp></p></td>
<td><p>The unique ID of the mod which sent the message.</p></td>
</tr>
<tr>
<td><p><samp>e.Type</samp></p></td>
<td><p><samp>string</samp></p></td>
<td><p>A message type which you can use to decide whether it's the one
you want to handle. This isn't necessarily globally unique, so you
should also check the <samp>FromModID</samp> field.</p></td>
</tr>
<tr>
<td><p><samp>e.ReadAs&lt;TModel&gt;()</samp></p></td>
<td><p><em><code>method</code></em><code> returns </code><samp>TModel</samp></p></td>
<td><p>Read the underlying message data into the given model type (like
<code>e.ReadAs&lt;MyMessageClass&gt;()</code> or
<code>e.ReadAs&lt;string&gt;()</code>). This will return a new instance
each time.</p></td>
</tr>
</tbody>
</table>
<h4 id="peerdisconnected">PeerDisconnected</h4>
<p><em>Group:</em> <code>Multiplayer</code></p>
<p>Raised after the connection to a player is severed.</p>
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
<td><p><samp>e.Peer</samp></p></td>
<td><p><samp>IMultiplayerPeer</samp></p></td>
<td><p>The peer whose connection was severed (see <a
href="Modding_Modder_Guide_APIs_Multiplayer#Get_connected_player_info"
class="wikilink"
title="Multiplayer#Get connected player info">Multiplayer#Get connected
player info</a>).</p></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
