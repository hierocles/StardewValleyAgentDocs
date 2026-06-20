---
title: "Monster Eradication Goals"
wiki_source: "Modding:Monster eradication goals"
permalink: /Modding:Monster_eradication_goals/
category: game
tags: [monster-eradication-goals, format, flag-changes]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains monster eradication goals. This is an advanced guide
for mod developers.

## Format

You can add/edit <a href="Adventurer&#39;s_Guild" class="wikilink"
title="Adventurer&#39;s Guild">Adventurer's Guild</a> monster
eradication goals by editing the `Data/MonsterSlayerQuests` data asset.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  monster eradication goal.
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
<td><p><samp>DisplayName</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the goal's display
name, shown on the board in the Adventurer's Guild.</p></td>
</tr>
<tr>
<td><p><samp>Targets</samp></p></td>
<td><p>A list of <a href="Modding_Monster_data#Monster_IDs"
class="wikilink" title="monster IDs">monster IDs</a> that are counted
towards the <samp>Count</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Count</samp></p></td>
<td><p>The total number of monsters (matching the <samp>Targets</samp>)
which must be defeated to complete this goal.</p></td>
</tr>
<tr>
<td><p><samp>RewardItemId</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified ID">qualified ID</a> for the item that can be collected
from <a href="Gil" class="wikilink" title="Gil">Gil</a> when this goal
is completed. Default none.</p></td>
</tr>
<tr>
<td><p><samp>RewardItemPrice</samp></p></td>
<td><p><em>(Optional)</em> The price of the <samp>RewardItemId</samp> in
<a href="Marlon" class="wikilink" title="Marlon">Marlon</a>'s shop after
the goal is completed, or -1 to disable buying it from Marlon. Default
-1.</p></td>
</tr>
<tr>
<td><p><samp>RewardDialogue</samp><br />
<samp>RewardDialogueFlag</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
custom <a href="Gil" class="wikilink" title="Gil">Gil</a> dialogue shown
when talking to him after completing the goal, and an optional <a
href="Modding_Mail_data" class="wikilink" title="mail flag">mail
flag</a> to set when the player has seen the dialogue. Both default to
none.</p>
<p>If there are reward items, they're shown after this dialogue.</p>
<p>If <samp>RewardDialogue</samp> is used without
<samp>RewardDialogueFlag</samp>, then this dialogue will be shown each
time the reward menu is opened after completing the goal, until the
player collects the reward items. If the <samp>RewardItems</samp> isn't
set, this can safely be omitted since the goal will be marked collected
immediately.</p>
<p>This doesn't send a letter; see <samp>RewardMail</samp> or
<samp>RewardMailAll</samp> for that.</p></td>
</tr>
<tr>
<td><p><samp>RewardFlag</samp><br />
<samp>RewardFlagAll</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Mail_data"
class="wikilink" title="mail flag ID">mail flag ID</a> to set for the
current player (<samp>RewardFlag</samp>) or all players
(<samp>RewardFlagAll</samp>) when talking to <a href="Gil"
class="wikilink" title="Gil">Gil</a> after completing the goal. Default
none.</p>
<p>Note that <samp>RewardFlag</samp> is usually not needed, since the
game will also set a <samp>Gil_&lt;goal ID&gt;</samp> flag
regardless.</p>
<p>This doesn't send a letter; see <samp>RewardMail</samp> or
<samp>RewardMailAll</samp> for that.</p></td>
</tr>
<tr>
<td><p><samp>RewardMail</samp><br />
<samp>RewardMailAll</samp></p></td>
<td><p><em>(Optional)</em> The mail letter ID to add to the mailbox
tomorrow for the current player (<samp>RewardMail</samp>) or all players
(<samp>RewardMailAll</samp>). Default none.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

## Flag changes

The game now tracks <a href="Adventurer&#39;s_Guild" class="wikilink"
title="Adventurer&#39;s Guild">Adventurer's Guild</a> monster
eradication goal completion by the goal ID, instead of the produced
item. Here is a list for vanilla goal IDs:

| goal | flag |
|----|----|
| <a href="Slimes" class="wikilink" title="Slimes">Slimes</a> ×1000 | `Gil_Slimes` |
| Void Sprits ×150 | `Gil_Shadows` |
| Bats ×200 | `Gil_Bats` |
| Skeletons ×50 | `Gil_Skeletons` |
| Cave Insects ×80 | `Gil_Insects` |
| Duggies ×30 | `Gil_Duggy` |
| Dust Sprites ×500 | `Gil_DustSpirits` |
| Rock Crabs ×60 | `Gil_Crabs` |
| Mummies ×100 | `Gil_Mummies` |
| Pepper Rex ×50 | `Gil_Dinos` |
| Serpents ×250 | `Gil_Serpents` |
| Magma Spirits ×150 | `Gil_FlameSpirits` |

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Истребление_чудовищ" class="wikilink"
title="ru:Модификации:Истребление чудовищ">ru:Модификации:Истребление
чудовищ</a> <a href="zh_模组_杀怪目标" class="wikilink"
title="zh:模组:杀怪目标">zh:模组:杀怪目标</a>
