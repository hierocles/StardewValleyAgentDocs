---
title: "Lost Items Shop"
wiki_source: "Modding:Lost items shop"
permalink: /Modding:Lost_items_shop/
category: world-systems
tags: [lost-items-shop, data-format]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses lost items shop data.
This is an advanced guide for mod developers.

1.6.9 adds a hidden shop in the secret woods which sells unique items
you've already unlocked but no longer own. For example, the
<a href="Soda_Machine" class="wikilink" title="soda machine">soda
machine</a> is received from the JojaMart completion event; if you lose
it, it would otherwise be gone forever. All items are sold for a flat
price.

## Data Format

You can add/edit lost items shop data by editing the the new
`Data/LostItemsShop` asset, which consists of a list of models with
these fields:

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
entry.</p></td>
</tr>
<tr>
<td><p><samp>ItemId</samp></p></td>
<td><p>The qualified item ID of the item to add to the shop.</p></td>
</tr>
<tr>
<td><p><samp>RequireMailReceived</samp><br />
<samp>RequireEventSeen</samp></p></td>
<td><p>The requirement for this item to be added to the shop.</p></td>
</tr>
</tbody>
</table>

You can specify either `RequireMailReceived` (a
<a href="Modding_Mail_data#Mail_flags" class="wikilink"
title="mail flag">mail flag</a> to match in players' received mail) or
`RequireEventSeen` (an
<a href="Modding_Event_data" class="wikilink" title="event ID">event
ID</a> players have seen). If you specify both, only
`RequireMailReceived` is used.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Магазин_потерянных_вещей" class="wikilink"
title="ru:Модификации:Магазин потерянных вещей">ru:Модификации:Магазин
потерянных вещей</a> <a href="zh_模组_遗失物品商店" class="wikilink"
title="zh:模组:遗失物品商店">zh:模组:遗失物品商店</a>
