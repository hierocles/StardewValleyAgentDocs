---
title: "Minecarts"
wiki_source: "Modding:Minecarts"
permalink: /Modding:Minecarts/
category: game
tags: [minecarts, format, open-a-minecart-menu, example]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains minecarts. This is an advanced guide for mod
developers.

## Format

You can now extend
<a href="minecart" class="wikilink" title="minecart">minecarts</a> by
editing the `Data\Minecarts` data asset.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  minecart network. When you interact with a minecart, the destinations
  listed for its network are shown.
- The value is a model with the fields listed below.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Destinations</samp></p></td>
<td><p>The destinations which the player can travel to from minecarts in
this network. This consists of a list of model with these fields:</p>
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
<td><p>A <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
destination within the network.</p></td>
</tr>
<tr>
<td><p><samp>DisplayName</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the destination
name shown in the minecart menu. You can use the location's display name
with the <samp>LocationName</samp> token (like
<code>[LocationName Desert]</code> for the <a href="desert"
class="wikilink" title="desert">desert</a>).</p></td>
</tr>
<tr>
<td><p><samp>TargetLocation</samp></p></td>
<td><p>The <a href="Modding_Location_data" class="wikilink"
title="location ID">location ID</a> for the destination.</p></td>
</tr>
<tr>
<td><p><samp>TargetTile</samp></p></td>
<td><p>The destination tile position within the location, specified as a
model with <samp>X</samp> and <samp>Y</samp> fields.</p></td>
</tr>
<tr>
<td><p><samp>TargetDirection</samp></p></td>
<td><p>The direction the player should face after arrival (one of
<samp>down</samp>, <samp>left</samp>, <samp>right</samp>, or
<samp>up</samp>).</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this minecart destination is available. Defaults to
always available.</p></td>
</tr>
<tr>
<td><p><samp>Price</samp></p></td>
<td><p><em>(Optional)</em> The gold price that must be paid each time to
use this destination. Default none.</p></td>
</tr>
<tr>
<td><p><samp>BuyTicketMessage</samp></p></td>
<td><p><em>(Optional)</em> If the destination costs money to use, a <a
href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the purchase
confirmation message shown. If present, <code>{0}</code> is replaced
with the purchase price. Defaults to the network's
<samp>BuyTicketMessage</samp> field.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>UnlockCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this minecart network is unlocked. Default always
enabled.</p></td>
</tr>
<tr>
<td><p><samp>LockedMessage</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the message shown when interacting with a minecart when the
<samp>UnlockCondition</samp> false. Defaults to an "<em>Out of
order</em>" translation.</p></td>
</tr>
<tr>
<td><p><samp>ChooseDestinationMessage</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the message shown when listing destinations to choose from. Defaults to
a "<em>Choose destination:</em>" translation.</p></td>
</tr>
<tr>
<td><p><samp>BuyTicketMessage</samp></p></td>
<td><p><em>(Optional)</em> When a destination costs money to use, a <a
href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the purchase
confirmation message shown. If present, <code>{0}</code> is replaced
with the purchase price. Defaults to a "<em>Buy a ticket for {0}g?</em>"
translation.</p></td>
</tr>
</tbody>
</table>

## Open a minecart menu

You can use an
`Action: MinecartTransport [network ID] [exclude destination ID]`
<a href="Modding_Maps" class="wikilink" title="map property">map
property</a> to open the minecart menu. When the player interacts with
the tile, it'll open the menu for the \[network ID\] network (default
`Default`). if \[exclude destination ID\] is specified, the matching
destination will be hidden from the list (usually because you're at that
minecart). For example, the
<a href="Bus_Stop" class="wikilink" title="bus stop">bus stop</a>
minecart uses `Action: MinecartTransport Default Bus`.

From a C# mod, you can call
`Game1.currentLocation.ShowMineCartMenu(networkId, excludeDestinationId)`
which works the same way (except that `networkId` is required).

## Example

This <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> content pack adds the
<a href="Railroad" class="wikilink" title="Railroad">Railroad</a> as a
minecart destination, complete with a map edit adding a decorative
minecart. It is available after the
<a href="Random_Events" class="wikilink"
title="Earthquake">Earthquake</a> has occurred and minecarts have been
unlocked.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Вагонетки" class="wikilink"
title="ru:Модификации:Вагонетки">ru:Модификации:Вагонетки</a>
<a href="zh_模组_矿车" class="wikilink"
title="zh:模组:矿车">zh:模组:矿车</a>
