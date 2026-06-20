---
title: "Quests"
wiki_source: "Modding:Quest data"
permalink: /Modding:Quest_data/
category: npcs
tags: [quest-data, raw-data, format, completion-requirements, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses
<a href="quests" class="wikilink" title="quests">quests</a>. This is an
advanced guide for mod developers.

## Raw data

Scripted quests are stored in `Content\Data\Quests.xnb`, which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of for reference:

## Format

The entry for each quest contains these slash-delimited quest fields:

<table>
<thead>
<tr>
<th><p>Index</p></th>
<th><p>Field</p></th>
<th><p>Example Value</p></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><p>Key</p></td>
<td><p>A <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for the
quest.</p></td>
<td><p><samp>MyQuestId</samp></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>0</p></td>
<td><p>The quest type.</p></td>
<td><p>Valid types are <code>Basic</code>, <code>Crafting</code>,
<code>Location</code>, <code>Building</code>, <code>ItemDelivery</code>,
<code>Monster</code>, <code>ItemHarvest</code>, <code>LostItem</code>,
<code>SecretLostItem</code>*, and <code>Social</code><br />
<br />
<small>If a quest uses the <samp>Social</samp> type, the completion
requirement will always be to speak to everyone in town (like the
Introductions quest and Emily's Say Hello quest), regardless of what you
write in field 4.</small></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>1</p></td>
<td><p>The title that will be in the player's journal.</p></td>
<td><p><samp>A Cool Quest</samp></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>2</p></td>
<td><p>Description that will appear in the quest log.</p></td>
<td><p><samp>Abigail wants an amethyst. You should probably deliver one
to her before she gets impatient.</samp></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>3</p></td>
<td><p><em>(Optional)</em> Objective instructions that will appear in
the quest log</p></td>
<td><p><samp>Deliver an amethyst to Abigail.</samp></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>4</p></td>
<td><p><em>(Optional)</em> Completion Requirements</p></td>
<td><p>The format of this field will vary depending on the quest
<samp>Type</samp>. See <a
href="Modding_Quest_data#Completion_Requirements" class="wikilink"
title="completion requirements">completion requirements</a>.</p></td>
</tr>
<tr>
<td style="text-align: center;"><p>5</p></td>
<td><p><em>(Optional)</em> Next Quest Ids<br />
<small>Upon completing this quest, each of these next quests will be
added to the player's quest log. Leave blank or use <samp>0</samp> or
<samp>-1</samp> for none.<br />
If a quest Id is prefixed with <code>h</code> and the player is not the
host, they will not receive the quest. The <code>h</code> will be
removed automatically.</p></td>
<td><p><samp>30 MySecondQuest hMyHostOnlyQuest</samp></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>6</p></td>
<td><p>The amount of money given upon completing the quest.</p></td>
<td><p><samp>500</samp></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>7</p></td>
<td><p><em>(Unused)</em> Reward description<br />
<small>Leave this blank or less than 2 characters long or else it will
show a blank reward when <samp>Money Reward</samp> is less than or equal
to 0.</p></td>
<td><p><samp>-1</samp></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>8</p></td>
<td><p><em>(Optional)</em> Can be cancelled (default false)</p></td>
<td><p><samp>true</samp></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>9</p></td>
<td><p><em>(Optional)</em> Reaction dialogue<br />
Required for <samp>ItemDelivery</samp>, <samp>LostItem</samp>, and
<samp>SecretLostItem</samp> quests, as well as <samp>Monster</samp>
quests when an NPC is specified. Not used in other quest
types.</small></p></td>
<td><p><samp>Wow, thanks for the Amethyst!</p></td>
</tr>
</tbody>
</table>

<small>\*A `SecretLostItem` quest will be hidden from the player's quest
log.</small>\

### Completion Requirements

The format of the **completion requirements** field will vary depending
on what `Type` is listed in the first field:

| Type | Format | Additional Info |
|----|----|----|
| `Basic` | `N/A` | A `Basic` quest is handled manually and it is up to you to complete it when appropriate. |
| `Crafting` | \<Item Id\> \[isBigCraftable\] | \<Item Id\> can be a qualified or unqualified item id. If it is unqualified, it will create either an <a href="Modding_Objects" class="wikilink" title="Object">Object</a> or a <a href="Modding_Big_craftables" class="wikilink"
title="Big Craftable">Big Craftable</a> depending on \[isBigCraftable\] (default false). |
| `Location` | \<Location\> | The player must warp to the location in order to complete the quest, even if they have already visited it before receiving the quest. |
| `Building` | \<Building Type\> | If the player has already constructed at least one \<Building Type\>, the quest will be completed immediately. |
| `ItemDelivery` | \<NPC\> \<Item Id\> \[Count\] | \<Item Id\> can be a qualified or unqualified item id. \[Count\] defaults to 1. |
| `Monster` | \<Monster Name\> \<Count\> \[NPC\] \[ignoreFarmMonsters\] | If the monster name has spaces in it, they must be replaced with underscores (e.g. `Green Slime` becomes `Green_Slime`). If you specify an \[NPC\], the player must talk to them after killing enough monsters in order to complete the quest. \[ignoreFarmMonsters\] defaults to `true`. |
| `ItemHarvest` | \<Item Id\> \[Count\] | \<Item Id\> can be a qualified or unqualified item id. \[Count\] defaults to 1. |
| `LostItem` | \<NPC\> \<Item Id\> \<Location\> \<x\> \<y\> | \<NPC\> is who the player must deliver the item to. \<Item Id\> can be a qualified or unqualified item id, however it *must* be an <a href="Modding_Objects" class="wikilink" title="Object">Object</a>. \<x\> and \<y\> are the X and Y tile coordinates to place the item at inside the given \<Location\>. If provided, the NPC will use the `Reaction Text` field in the quest data, otherwise they will use default dialogue. |
| `SecretLostItem` | \<NPC\> \<Item Id\> \<Friendship\> \[Quest Id\] | \<NPC\> is who the player must deliver the item to. \<Item Id\> can be a qualified or unqualified item id. \<Friendship\> determines how many friendship points (not hearts) the player will receive upon delivering the item. If \[Quest Id\] is provided, then upon completing this quest, the game will *remove* the quest whose Id matches the given \[Quest Id\] from the player's active quest log without completing it. |

Here is the string in an easy to edit format:\
ID: Type/Title/Description/Hint/Requirement/Next Quests/Money
Reward/-1/Cancellable/Reaction Text

## See also

- <a href="Modding_Special_orders" class="wikilink"
  title="Modding:Special orders">Modding:Special orders</a>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Datos_de_misiones" class="wikilink"
title="es:Modding:Datos de misiones">es:Modding:Datos de misiones</a>
<a href="ru_Модификации_Задания" class="wikilink"
title="ru:Модификации:Задания">ru:Модификации:Задания</a>
<a href="zh_模组_任务数据" class="wikilink"
title="zh:模组:任务数据">zh:模组:任务数据</a>
