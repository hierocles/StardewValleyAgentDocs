---
title: "Stats"
wiki_source: "Modding:Stats"
permalink: /Modding:Stats/
category: reference
tags: [stats, overview, format, reference-stats-in-mod-code, caveats, built-in-stats, currency-scores, player-activity]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents **stats**, which track simple numeric values in the
game state. Stats are tracked separately for each player, though some
stats represent global values.

## Overview

### Format

Each stat is identified by a
<a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> (i.e. the
*stat key*). Stat keys are case-insensitive, so `stepsTaken` and
`STEPSTAKEN` are equivalent.

Stat values are positive integers from 0 to [4.2
billion](https://learn.microsoft.com/en-us/dotnet/api/system.uint32.maxvalue)
(default 0).

### Reference stats in mod code

You can check stats...

- using a <a href="Modding_Game_state_queries" class="wikilink"
  title="game state query">game state query</a> like
  `PLAYER_STAT Current stepsTaken 500` (i.e. current player has taken
  500+ steps);
- using a <a href="Modding_Console_commands" class="wikilink"
  title="debug command">debug command</a> like
  `debug getStat stepsTaken`;
- or in C# like
  `uint stepsTaken = Game1.player.stats.Get(StatKeys.StepsTaken)` (where
  `StatKeys` has constants for all of the base game's stats).

Mods can set stats...

- in <a href="Modding_Content_Patcher" class="wikilink"
  title="Content Patcher packs">Content Patcher packs</a> via the
  `IncrementStat` <a href="Modding_Trigger_actions" class="wikilink"
  title="trigger action">trigger action</a> or data fields like
  `StatsToIncrementWhenLoaded` in
  <a href="Modding_Machines" class="wikilink"
  title="Data/Machines"><samp>Data/Machines</samp></a>;
- or in C# code via the `Game1.player.stats` API (like
  `Game1.player.stats.Increment($"{this.ModManifest.UniqueID}_ExampleStat")`).

Stats can have arbitrary keys and are managed automatically by the game.
For example:

- getting a stat which doesn't exist will just return zero;
- setting a stat which doesn't exist like `IncrementStat _CustomStat`
  will just add it with the new value;
- and reducing a stat to zero will remove the stat (since a stat which
  doesn't exist has a zero value).

### Caveats

Stats are *not* synced in <a href="multiplayer" class="wikilink"
title="multiplayer">multiplayer</a>, so farmhands can only access their
own stats (not stats on the host or other farmhands).

## Built-in stats

This section lists the stats tracked by the base game.

### Currency & scores

| stat key | tracks |
|----|----|
| `SpecialOrderPrizeTickets` | The player's current number of <a href="Prize_Ticket" class="wikilink" title="prize tickets">prize
tickets</a>. |
| `SquidFestScore_<day>_<year>` | The player's <a href="SquidFest" class="wikilink" title="SquidFest">SquidFest</a> score for a specific date. |

### Player activity

<table>
<thead>
<tr>
<th><p>stat key</p></th>
<th><p>tracks</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ArtifactSpotsDug</samp></p></td>
<td><p>The number of <a href="Artifact_Spot" class="wikilink"
title="artifact spots">artifact spots</a> dug up by this player using a
<a href="hoe" class="wikilink" title="hoe">hoe</a>.</p></td>
</tr>
<tr>
<td><p><samp>AverageBedTime</samp></p></td>
<td><p>The average in-game time when the player went to sleep each day
since the save started.</p>
<p><strong>Bug:</strong> this stat tracks the average <em>display
time</em>, not the actual time. For example, the average of 6am (0600) +
7am (0700) is incorrectly calculated as 0650 instead of 0630.</p></td>
</tr>
<tr>
<td><p><samp>BillboardQuestsDone</samp></p></td>
<td><p>The number of <a href="Quests" class="wikilink"
title="&#39;help wanted&#39; billboard quests">'help wanted' billboard
quests</a> completed by the player.</p></td>
</tr>
<tr>
<td><p><samp>BoatRidesToIsland</samp></p></td>
<td><p>The number of times the player took <a
href="Fish_Shop#Willy&#39;s_Boat" class="wikilink"
title="Willy&#39;s boat">Willy's boat</a> to <a href="Ginger_Island"
class="wikilink" title="Ginger Island">Ginger Island</a>.</p></td>
</tr>
<tr>
<td><p><samp>ChildrenTurnedToDoves</samp></p></td>
<td><p>The number of children which the player sacrificed to the <a
href="Dark_Shrine_of_Selfishness" class="wikilink"
title="Dark Shrine of Selfishness">Dark Shrine of
Selfishness</a>.</p></td>
</tr>
<tr>
<td><p><samp>CompletedJunimoKart</samp></p></td>
<td><p>The number of times the player completed <a href="Junimo_Kart"
class="wikilink" title="Junimo Kart">Junimo Kart</a>.</p>
<p>⚠ This was added in , so multiple completions in previous versions
count as 1.</p></td>
</tr>
<tr>
<td><p><samp>CompletedPrairieKing</samp></p></td>
<td><p>The number of times the player completed <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie King</a>.</p>
<p>⚠ This was added in , so multiple completions in previous versions
count as 1.</p></td>
</tr>
<tr>
<td><p><samp>CompletedPrairieKingWithoutDying</samp></p></td>
<td><p>The number of times the player completed <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie King</a>
without dying.</p>
<p>⚠ This was added in , so completions in previous versions aren't
counted.</p></td>
</tr>
<tr>
<td><p><samp>DirtHoed</samp></p></td>
<td><p>The number of times the player tiled dirt using a <a href="hoe"
class="wikilink" title="hoe">hoe</a>.</p></td>
</tr>
<tr>
<td><p><samp>ExMemoriesWiped</samp></p></td>
<td><p>The number of times the player sacrificed their ex-spouse's
memories at the <a href="Dark_Shrine_of_Memory" class="wikilink"
title="Dark Shrine of Memory">Dark Shrine of Memory</a>.</p></td>
</tr>
<tr>
<td><p><samp>FishCaught</samp><br />
<samp>PreciseFishCaught</samp></p></td>
<td><p>The number of fish caught by the player while fishing.</p>
<p><samp>PreciseFishCaught</samp> is a subset of <samp>FishCaught</samp>
which ignores some catches which don't strictly count as 'fish' (i.e.
items which don't have the <em>Fish</em> <a
href="Modding_Items#Categories" class="wikilink"
title="category">category</a> or <samp>counts_as_fish_catch</samp> <a
href="Modding_Context_tags" class="wikilink" title="context tag">context
tag</a>). For example, <a href="seaweed" class="wikilink"
title="seaweed">seaweed</a> counts for <samp>FishCaught</samp> but not
for <samp>PreciseFishCaught</samp>.</p></td>
</tr>
<tr>
<td><p><samp>FishingTreasures</samp></p></td>
<td><p>The number of treasure boxes opened while catching a
fish.</p></td>
</tr>
<tr>
<td><p><samp>GeodesCracked</samp></p></td>
<td><p>The number of <a href="geode" class="wikilink"
title="geode">geodes</a> <strong>and</strong> <a href="Mystery_Box"
class="wikilink" title="mystery boxes">mystery boxes</a> broken open by
the player at Clint's shop or by placing them in a <a
href="Geode_Crusher" class="wikilink" title="geode crusher">geode
crusher</a>. See also <samp>MysteryBoxesOpened</samp>.</p></td>
</tr>
<tr>
<td><p><samp>GiftsGiven</samp></p></td>
<td><p>The number of items which the player gave to NPCs as gifts. (This
doesn't count items given to NPCs for other purposes like events or
quests.)</p></td>
</tr>
<tr>
<td><p><samp>GoldenTagsTurnedIn</samp></p></td>
<td><p>The number of <a href="Golden_Tag" class="wikilink"
title="golden tags">golden tags</a> redeemed by the player at the <a
href="Trout_Derby" class="wikilink" title="Trout Derby">Trout
Derby</a>.</p></td>
</tr>
<tr>
<td><p><samp>GoodFriends</samp></p></td>
<td><p>The number of NPCs with which the player has 8+ hearts of <a
href="friendship" class="wikilink"
title="friendship">friendship</a>.</p></td>
</tr>
<tr>
<td><p><samp>hardModeMonstersKilled</samp></p></td>
<td><p>The number of <a href="The_Mines#Shrine_of_Challenge"
class="wikilink" title="&#39;dangerous&#39;">'dangerous'</a> monsters
killed by the player.</p></td>
</tr>
<tr>
<td><p><samp>IndividualMoneyEarned</samp></p></td>
<td><p>The total gold earned by the player while the multiplayer <a
href="Multiplayer#Money" class="wikilink"
title="separate wallets option">separate wallets option</a> is
enabled.</p></td>
</tr>
<tr>
<td><p><samp>ItemsCooked</samp></p></td>
<td><p>The number of items created from <a href="cooking"
class="wikilink" title="cooking">cooking</a> recipes by the
player.</p></td>
</tr>
<tr>
<td><p><samp>ItemsCrafted</samp></p></td>
<td><p>The number of items created from <a href="crafting"
class="wikilink" title="crafting">crafting</a> recipes by the
player.</p></td>
</tr>
<tr>
<td><p><samp>ItemsForaged</samp></p></td>
<td><p>The number of <a href="forage" class="wikilink"
title="forage">forage</a> items harvested by the player (including
forage crops).</p></td>
</tr>
<tr>
<td><p><samp>MonstersKilled</samp></p></td>
<td><p>The number of monsters killed by the player.</p></td>
</tr>
<tr>
<td><p><samp>MossHarvested</samp></p></td>
<td><p>The number of times moss was harvested from trees by the
player.</p></td>
</tr>
<tr>
<td><p><samp>MysteryBoxesOpened</samp></p></td>
<td><p>The number of mystery boxes opened by the player at Clint's shop
or by placing them in a geode crusher. See also
<samp>GeodesCracked</samp>.</p></td>
</tr>
<tr>
<td><p><samp>MysticStonesCrushed</samp></p></td>
<td><p>The number of <a href="Mining#Mystic_Stone" class="wikilink"
title="mystic mine nodes">mystic mine nodes</a> broken by the
player.</p></td>
</tr>
<tr>
<td><p><samp>OtherPreciousGemsFound</samp></p></td>
<td><p>The number of <a href="Mining#Gem_Node" class="wikilink"
title="gem mine nodes">gem mine nodes</a> broken by the player.</p>
<p><strong>Bug:</strong> this stat isn't tracked correctly in later
versions of the game.</p></td>
</tr>
<tr>
<td><p><samp>PiecesOfTrashRecycled</samp></p></td>
<td><p>The number of items placed in <a href="Recycling_Machine"
class="wikilink" title="recycling machines">recycling machines</a> by
the player.</p></td>
</tr>
<tr>
<td><p><samp>PreservesMade</samp></p></td>
<td><p>The number of items collected from <a href="Preserves_Jar"
class="wikilink" title="preserves jars">preserves jars</a> by the
player.</p></td>
</tr>
<tr>
<td><p><samp>QuestsCompleted</samp></p></td>
<td><p>The number of <a href="quests" class="wikilink"
title="quests">quests</a> and <a href="Special_Orders" class="wikilink"
title="special orders">special orders</a> completed by the player.</p>
<p>For farmhands, a special order is counted if they're online when it's
completed.</p></td>
</tr>
<tr>
<td><p><samp>RocksCrushed</samp></p></td>
<td><p>The number of times the player broke a rock using a <a
href="pickaxe" class="wikilink" title="pickaxe">pickaxe</a>.</p></td>
</tr>
<tr>
<td><p><samp>SeedsSown</samp></p></td>
<td><p>The number of <a href="crops" class="wikilink"
title="crop">crop</a> seeds planted by the player (including seeds
planted in <a href="Garden_Pot" class="wikilink"
title="garden pots">garden pots</a> or in dirt).</p></td>
</tr>
<tr>
<td><p><samp>SlimesKilled</samp></p></td>
<td><p>The number of slimes killed by the player. This includes <a
href="slimes" class="wikilink" title="slime monsters">slime
monsters</a>, <a href="Slimes#Big_Slimes" class="wikilink"
title="big slime monsters">big slime monsters</a>, and slimes bred by
the player (e.g. in a <a href="Slime_Hutch" class="wikilink"
title="slime hutch">slime hutch</a>).</p></td>
</tr>
<tr>
<td><p><samp>StepsTaken</samp></p></td>
<td><p>The total number of steps taken by the player.</p></td>
</tr>
<tr>
<td><p><samp>StumpsChopped</samp></p></td>
<td><p>The number of <a href="Large_Stump" class="wikilink"
title="large stumps">large stumps</a> and <a href="Large_Log"
class="wikilink" title="hollow logs">hollow logs</a> broken by the
player.</p></td>
</tr>
<tr>
<td><p><samp>TicketPrizesClaimed</samp></p></td>
<td><p>The number of times the player redeemed a <a href="Prize_Ticket"
class="wikilink" title="prize ticket">prize ticket</a>.</p></td>
</tr>
<tr>
<td><p><samp>TimesEnchanted</samp></p></td>
<td><p>The number of times the player enchanted a tool or weapon at the
<a href="forge" class="wikilink" title="forge">forge</a>.</p></td>
</tr>
<tr>
<td><p><samp>TimesFished</samp></p></td>
<td><p>The number of times the player cast the fishing rod into water
(regardless of whether they caught anything).</p></td>
</tr>
<tr>
<td><p><samp>TimesPanned</samp></p></td>
<td><p>The number of times the player found items while <a href="pan"
class="wikilink" title="pan">panning</a>.</p></td>
</tr>
<tr>
<td><p><samp>TimesTossedBaby</samp></p></td>
<td><p>The number of times the player tossed a baby in the air.</p></td>
</tr>
<tr>
<td><p><samp>TimesUnconscious</samp></p></td>
<td><p>The number of times the player was knocked out due to their
health reaching zero.</p></td>
</tr>
<tr>
<td><p><samp>TotalMoneyGifted</samp></p></td>
<td><p>The total gold which this player sent to other players through
the <a href="Mayor&#39;s_Manor#Multiplayer_Funds" class="wikilink"
title="town ledger">town ledger</a>.</p></td>
</tr>
<tr>
<td><p><samp>TrashCansChecked</samp></p></td>
<td><p>The number of times the player rummaged through a <a
href="Garbage_Can" class="wikilink" title="trash can">trash
can</a>.</p></td>
</tr>
<tr>
<td><p><samp>TreesChopped</samp></p></td>
<td><p>The number of <a href="Trees" class="wikilink"
title="wild trees">wild trees</a> chopped down by the player.</p></td>
</tr>
<tr>
<td><p><samp>WeedsEliminated</samp></p></td>
<td><p>The number of <a href="weeds" class="wikilink"
title="weeds">weeds</a> destroyed by the player (including with bombs or
scythes).</p>
<p><strong>Bug:</strong> this stat only tracks weeds destroyed
indirectly (e.g. using a <a href="bomb" class="wikilink"
title="bomb">bomb</a>), not those cut directly using a tool.</p></td>
</tr>
<tr>
<td><p><samp>WildTreesPlanted</samp></p></td>
<td><p>The number of <a href="Trees" class="wikilink"
title="wild tree">wild tree</a> seeds planted by the player.</p></td>
</tr>
</tbody>
</table>

### Items collected

These track the number of individual items collected by players. Some
stats under <a href="#Player_activity" class="wikilink"
title="player activity"><em>player activity</em></a> track how many
times the player performed a related action (e.g. `ItemsForaged` counts
the number of times they harvested forage crops).

<table>
<thead>
<tr>
<th><p>stat key</p></th>
<th><p>tracks</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>BeveragesMade</samp></p></td>
<td><p>The number of items collected from <a href="keg" class="wikilink"
title="keg">kegs</a> by the player.</p></td>
</tr>
<tr>
<td><p><samp>CaveCarrotsFound</samp></p></td>
<td><p>The number of <a href="Cave_Carrot" class="wikilink"
title="cave carrots">cave carrots</a> found by the player by digging
them up. (Cave carrots found any other way aren't counted.)</p>
<p><strong>Bug:</strong> this stat isn't actually tracked correctly, and
will always be zero.</p></td>
</tr>
<tr>
<td><p><samp>CheeseMade</samp><br />
<samp>GoatCheeseMade</samp></p></td>
<td><p>The number of items collected from <a href="Cheese_Press"
class="wikilink" title="cheese presses">cheese presses</a> by the
player. <a href="Goat_Cheese" class="wikilink" title="Goat cheese">Goat
cheese</a> increments <samp>GoatCheeseMade</samp> (not
<samp>CheeseMade</samp>); any other item increments
<samp>CheeseMade</samp>.</p></td>
</tr>
<tr>
<td><p><samp>CopperFound</samp><br />
<samp>DiamondsFound</samp><br />
<samp>GoldFound</samp><br />
<samp>IridiumFound</samp><br />
<samp>IronFound</samp><br />
<samp>NotesFound</samp></samp><br />
<samp>PrismaticShardsFound</samp><br />
<samp>StoneGathered</samp></p></td>
<td><p>The number of each item received by the player which was never
previously in a player inventory.</p>
<p>For example: copper ore collected after breaking a mine rock counts,
but dropping the copper ore and picking it back up would not, nor would
receiving copper ore from another player.</p>
<p>The matching items are:</p>
<ul>
<li><a href="Copper_Ore" class="wikilink" title="copper ore">copper
ore</a>: <samp>CopperFound</samp>;</li>
<li><a href="Diamond" class="wikilink" title="diamonds">diamonds</a>:
<samp>DiamondsFound</samp>;</li>
<li><a href="Gold_Ore" class="wikilink" title="gold ore">gold ore</a>:
<samp>GoldFound</samp>;</li>
<li><a href="Iridium_Ore" class="wikilink" title="iridium ore">iridium
ore</a>: <samp>IridiumFound</samp>;</li>
<li><a href="Iron_Ore" class="wikilink" title="iron ore">iron ore</a>:
<samp>IronFound</samp>;</li>
<li><a href="Lost_Books" class="wikilink" title="lost books">lost
books</a>: <samp>NotesFound</samp> (not to be confused with <a
href="Secret_Notes" class="wikilink" title="secret notes">secret
notes</a>);</li>
<li><a href="Prismatic_Shard" class="wikilink"
title="prismatic shards">prismatic shards</a>:
<samp>PrismaticShardsFound</samp>;</li>
<li><a href="stone" class="wikilink" title="stone">stone</a>:
<samp>StoneGathered</samp>.</li>
</ul></td>
</tr>
</tbody>
</table>

### Buffs & skills

<table>
<thead>
<tr>
<th><p>stat key</p></th>
<th><p>tracks</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>BlessingOfWaters</samp></p></td>
<td><p>The current <a href="Statue_Of_Blessings" class="wikilink"
title="Blessings of Waters">Blessings of Waters</a> count. This starts
at 3 when the blessing is granted, and decrements by one for each fish
caught.</p></td>
</tr>
<tr>
<td><p><samp>Book_&lt;book ID&gt;</samp></p></td>
<td><p>Whether the player has read a <a href="Books" class="wikilink"
title="power or skill book">power or skill book</a>, where
<samp>0</samp> is false and <samp>1</samp> (or higher values) means
true. The &lt;book ID&gt; is the <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="unqualified item ID">unqualified item ID</a> for the book <a
href="Modding_Objects" class="wikilink" title="object">object</a>.</p>
<p>The matching books are:</p>
<ul>
<li><a href="Animal_Catalogue" class="wikilink"
title="Animal Catalogue">Animal Catalogue</a>:
<samp>Book_AnimalCatalogue</samp>;</li>
<li><a href="Book_of_Mysteries" class="wikilink"
title="Book of Mysteries">Book of Mysteries</a>:
<samp>Book_Mystery</samp>;</li>
<li><a href="Dwarvish_Safety_Manual" class="wikilink"
title="Dwarvish Safety Manual">Dwarvish Safety Manual</a>:
<samp>Book_Bombs</samp>.</li>
<li><a href="Friendship_101" class="wikilink"
title="Friendship 101">Friendship 101</a>:
<samp>Book_Friendship</samp>;</li>
<li><a href="Horse_The_Book" class="wikilink"
title="Horse: The Book">Horse: The Book</a>:
<samp>Book_Horse</samp>;</li>
<li><a href="Jack_Be_Nimble,_Jack_Be_Thick" class="wikilink"
title="Jack Be Nimble, Jack Be Thick">Jack Be Nimble, Jack Be Thick</a>:
<samp>Book_Defense</samp>;</li>
<li><a href="Jewels_Of_The_Sea" class="wikilink"
title="Jewels Of The Sea">Jewels Of The Sea</a>:
<samp>Book_Roe</samp>;</li>
<li><a href="Mapping_Cave_Systems" class="wikilink"
title="Mapping Cave Systems">Mapping Cave Systems</a>:
<samp>Book_Marlon</samp>;</li>
<li><a href="Monster_Compendium" class="wikilink"
title="Monster Compendium">Monster Compendium</a>:
<samp>Book_Void</samp>;</li>
<li><a href="Ol&#39;_Slitherlegs" class="wikilink"
title="Ol&#39; Slitherlegs">Ol' Slitherlegs</a>:
<samp>Book_Grass</samp>;</li>
<li><a href="Price_Catalogue" class="wikilink"
title="Price Catalogue">Price Catalogue</a>:
<samp>Book_PriceCatalogue</samp>;</li>
<li><a href="Queen_Of_Sauce_Cookbook" class="wikilink"
title="Queen Of Sauce Cookbook">Queen Of Sauce Cookbook</a>:
<samp>Book_QueenOfSauce</samp>;</li>
<li><a href="Raccoon_Journal" class="wikilink"
title="Raccoon Journal">Raccoon Journal</a>:
<samp>Book_WildSeeds</samp>;</li>
<li><a href="The_Alleyway_Buffet" class="wikilink"
title="The Alleyway Buffet">The Alleyway Buffet</a>:
<samp>Book_Trash</samp>;</li>
<li><a href="The_Art_O&#39;_Crabbing" class="wikilink"
title="The Art O&#39; Crabbing">The Art O' Crabbing</a>:
<samp>Book_Crabbing</samp>;</li>
<li><a href="The_Diamond_Hunter" class="wikilink"
title="The Diamond Hunter">The Diamond Hunter</a>:
<samp>Book_Diamonds</samp>;</li>
<li><a href="Treasure_Appraisal_Guide" class="wikilink"
title="Treasure Appraisal Guide">Treasure Appraisal Guide</a>:
<samp>Book_Artifact</samp>;</li>
<li><a href="Way_Of_The_Wind_pt._1" class="wikilink"
title="Way Of The Wind pt. 1">Way Of The Wind pt. 1</a>:
<samp>Book_Speed</samp>;</li>
<li><a href="Way_Of_The_Wind_pt._2" class="wikilink"
title="Way Of The Wind pt. 2">Way Of The Wind pt. 2</a>:
<samp>Book_Speed2</samp>;</li>
<li><a href="Woody&#39;s_Secret" class="wikilink"
title="Woody&#39;s Secret">Woody's Secret</a>:
<samp>Book_Woodcutting</samp>.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>MasteryExp</samp></p></td>
<td><p>The total <a href="Mastery_Cave" class="wikilink"
title="mastery">mastery</a> experience points earned by the
player.</p></td>
</tr>
<tr>
<td><p><samp>MasteryLevelsSpent</samp></p></td>
<td><p>The number of <a href="Mastery_Cave" class="wikilink"
title="mastery">mastery</a> levels claimed by the player.</p></td>
</tr>
<tr>
<td><p><samp>Mastery_&lt;skill ID&gt;</samp></p></td>
<td><p>Whether the player has unlocked a <a href="Mastery_Cave"
class="wikilink" title="mastery level">mastery level</a> for a <a
href="Skills" class="wikilink" title="skill">skill</a>. The &lt;skill
ID&gt; is one of <samp>0</samp> (farming), <samp>1</samp> (fishing),
<samp>2</samp> (foraging), <samp>3</samp> (mining), or <samp>4</samp>
(combat).</p></td>
</tr>
<tr>
<td><p><samp>TrinketSlots</samp></p></td>
<td><p>The number of trinket slots unlocked by the player.</p>
<p>This should be 0 or 1; any number beyond that is equivalent to
1.</p></td>
</tr>
</tbody>
</table>

### World activity

**⚠ In <a href="multiplayer" class="wikilink"
title="multiplayer">multiplayer</a>, these are primarily tracked for the
main player. Make sure to read the full description before using them
with a farmhand.**

<table>
<thead>
<tr>
<th><p>stat key</p></th>
<th><p>tracks</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>BeachFarmSpawns</samp></p></td>
<td><p>The total number of beach forage which spawned on the <a
href="Farm_Maps" class="wikilink" title="beach farm">beach farm</a>.</p>
<p>⚠ For farmhands in multiplayer, the value is always zero.</p></td>
</tr>
<tr>
<td><p><samp>ChickenEggsLayed</samp></p></td>
<td><p>The number of eggs produced by <a href="chicken" class="wikilink"
title="chicken">chickens</a>.</p>
<p>⚠ For farmhands in multiplayer, the value is always zero.</p></td>
</tr>
<tr>
<td><p><samp>CowMilkProduced</samp></p></td>
<td><p>The number of milk items produced by <a href="cow"
class="wikilink" title="cow">cows</a>.</p>
<p>⚠ For farmhands in multiplayer, the value is always zero.</p></td>
</tr>
<tr>
<td><p><samp>CropsShipped</samp></p></td>
<td><p>The number of items with the <em>Fruit</em> or <em>Vegetable</em>
<a href="Modding_Items#Categories" class="wikilink"
title="category">category</a> shipped by any players. See also
<samp>ItemsShipped</samp>.</p>
<p>⚠ For farmhands in multiplayer, this is the number shipped while they
were online to see the end-of-day shipping screen.</p></td>
</tr>
<tr>
<td><p><samp>DuckEggsLayed</samp></p></td>
<td><p>The number of eggs produced by <a href="duck" class="wikilink"
title="duck">ducks</a>.</p>
<p>⚠ For farmhands in multiplayer, the value is always zero.</p></td>
</tr>
<tr>
<td><p><samp>DaysPlayed</samp></p></td>
<td><p>The number of days completed (i.e. times slept) by the player,
including the new-game intro (even if it was skipped).</p>
<p>⚠ For farmhands in multiplayer, this is the value received from the
host player the last time they were online when everyone went to
sleep.</p></td>
</tr>
<tr>
<td><p><samp>GoatMilkProduced</samp></p></td>
<td><p>The number of milk items produced by <a href="goat"
class="wikilink" title="goat">goats</a>.</p>
<p>⚠ For farmhands in multiplayer, the value is always zero.</p></td>
</tr>
<tr>
<td><p><samp>SheepWoolProduced</samp></p></td>
<td><p>The number of wool items produced by <a href="sheep"
class="wikilink" title="sheep">sheep</a>.</p>
<p>⚠ For farmhands in multiplayer, the value is always zero.</p></td>
</tr>
<tr>
<td><p><samp>RabbitWoolProduced</samp></p></td>
<td><p>The number of wool items produced by <a href="rabbit"
class="wikilink" title="rabbit">rabbits</a>.</p>
<p>⚠ For farmhands in multiplayer, the value is always zero.</p></td>
</tr>
<tr>
<td><p><samp>ItemsShipped</samp></p></td>
<td><p>The number of items shipped by any players. See also
<samp>CropsShipped</samp>.</p>
<p>⚠ For farmhands in multiplayer, this is the number shipped while they
were online to see the end-of-day shipping screen.</p></td>
</tr>
<tr>
<td><p><samp>TrufflesFound</samp></p></td>
<td><p>The number of truffles found by <a href="pig" class="wikilink"
title="pig">pigs</a>.</p>
<p>⚠ For farmhands in multiplayer, the value is always zero.</p></td>
</tr>
</tbody>
</table>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Статистика" class="wikilink"
title="ru:Модификации:Статистика">ru:Модификации:Статистика</a>
<a href="zh_模组_统计数据" class="wikilink"
title="zh:模组:统计数据">zh:模组:统计数据</a>
