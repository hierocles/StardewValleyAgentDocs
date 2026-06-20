---
title: "Mail"
wiki_source: "Modding:Mail data"
permalink: /Modding:Mail_data/
category: world-systems
tags: [mail-data, raw-data, format, key, value, examples, mail-flags, overview]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses mail data. This is an
advanced guide for mod developers.

## Raw data

Object data is stored in `Content\Data\Mail.xnb`, which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of for reference:

## Format

### Key

Each mail entry has a unique key which identifies the message (*e.g.,*
to track whether the player already received it). For example, `Robin`
at the start of this entry is the mail key:

``` json
"Robin": "Hey there!^I had some extra wood lying around... I thought maybe you could use it. Take care!  ^   -Robin %item object 388 50 %%[#]A Gift From Robin"
```

The key can be one of these formats:

<table>
<thead>
<tr>
<th><p>syntax</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>&lt;season&gt;_&lt;day of
month&gt;_&lt;year&gt;</samp></p></td>
<td><p>Sent on the given date.<br />
<small>Example: <samp>spring_15_3</samp> applies on spring 15 in year
3.</small></p></td>
</tr>
<tr>
<td><p><samp>&lt;season&gt;_&lt;day of month&gt;</samp></p></td>
<td><p>Sent on the given date in any year. This is ignored if mail was
sent for the previous format.<br />
<small>Example: <samp>spring_15</samp> applies on spring
15.</small></p></td>
</tr>
<tr>
<td><p><em>arbitrary key</em></p></td>
<td><p>Anything else is just a unique letter ID, which can be sent in
code or via <a href="Modding_Event_data" class="wikilink"
title="an event script">an event script</a>.</p></td>
</tr>
</tbody>
</table>

It's not recommended to use the date-based format for compatibility
reasons, because if multiple mods add mail with the same key only one
will get sent. If you need your mail to be sent on a specific date, see
<a href="Modding_Trigger_actions" class="wikilink"
title="trigger actions">trigger actions</a>.

Careful! Any keys which contain the words '`Cooking`' or '`passOut`',
case sensitive, will never be "received" when sent through the mailbox
(i.e. have a Letter attached). This impacts their ability to be used in
<a href="Modding_Game_state_queries" class="wikilink"
title="game state queries">game state queries</a> or other conditions,
consider adjusting the key if you need to check for it later.

### Value

The value for each letter entry has this format: \<letter
text\>\[#\]\<letter name\>.

The \<letter name\> field is just a unique human-readable name for the
letter, shown in the mail collections tab.

The \<letter text\> field is the text to show when the player opens the
letter. This recognizes some special tokens:

<table>
<thead>
<tr>
<th><p>token</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>^</samp></p></td>
<td><p>Replaced with a line break. Can be repeated to insert multiple
line breaks.</p></td>
</tr>
<tr>
<td><p><samp>@</samp></p></td>
<td><p>Replaced with the player name.<br />
<small>Example: <samp>Hello @!</samp></small></p></td>
</tr>
<tr>
<td><p><samp>¦</samp></p></td>
<td><p>Switches between gendered versions of the letter. Male players
see the text before <samp>¦</samp>, and others see the text after it.
Only the first instance is recognized. If the text doesn't contain it,
all players see the same version.</p></td>
</tr>
<tr>
<td><p><samp>%secretsanta</samp></p></td>
<td><p>Replaced with a random town NPC name if the date is winter 18–25
inclusively, else replaced with <samp>???</samp>.</p></td>
</tr>
</tbody>
</table>

Some special commands are also supported in the letter's text:

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>%action &lt;action&gt; %%</samp></p></td>
<td><p>Run a <a href="Modding_Trigger_actions" class="wikilink"
title="trigger action string">trigger action string</a>, like
<samp>%action AddMoney 500%%</samp> to add to the current
player.</p></td>
</tr>
<tr>
<td><p><samp>%item id [&lt;item id&gt; [count]]+ %%</samp></p></td>
<td><p>Accepts a <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a>. If multiple items are listed (<em>e.g.,</em>
<samp>%item id (BC)12 3 (O)34 5 %%</samp>) one set will be picked
randomly.</p></td>
</tr>
<tr>
<td><p><samp>%item money &lt;amount&gt; %%</samp><br />
<samp>%item money &lt;min&gt; &lt;max&gt; %%</samp></p></td>
<td><p>Attach the given amount of money, or a random amount between an
inclusive &lt;min&gt; and exclusive &lt;max&gt; value. In either case,
the value is rounded down to the nearest 10 (<em>e.g.,</em>
156→150).</p></td>
</tr>
<tr>
<td><p><samp>%item conversationTopic &lt;key&gt; &lt;days&gt;
%%</samp></p></td>
<td><p>Start an <a href="Modding_Dialogue#Active_dialogue_events"
class="wikilink" title="active dialogue event">active dialogue event</a>
for the given number of days.</p></td>
</tr>
<tr>
<td><p><samp>%item cookingRecipe [key]%%</samp></p></td>
<td><p>If <samp>key</samp> is provided, the player will learn a specific
<a href="Modding_Recipe_data" class="wikilink"
title="cooking recipe">cooking recipe</a> with that ID. Otherwise,
teaches the player the cooking recipe whose requirement field starts
with <samp>f &lt;npc name&gt;</samp>, where &lt;npc name&gt; is the mail
key with 'Cooking' removed. For example, if the mail key is
<samp>RobinCooking</samp>, this command would find a cooking recipe with
a requirement starting with <samp>f Robin</samp> that the player doesn't
already know.</p></td>
</tr>
<tr>
<td><p><samp>%item craftingRecipe &lt;key&gt; %%</samp></p></td>
<td><p>Teach the player the crafting recipe with the given ID. The key
is the item name. The command first checks for an exact match for the
key. Otherwise, it tries using underscores in place of spaces, (e.g.
"Mayonnaise Machine" becomes "Mayonnaise_Machine").</p></td>
</tr>
<tr>
<td><p><samp>%item itemRecovery &lt;key&gt; %%</samp></p></td>
<td><p>Attach the item that the player asked <a href="Marlon"
class="wikilink" title="Marlon">Marlon</a> to find in the mines, if
any.</p></td>
</tr>
<tr>
<td><p><samp>%item quest &lt;quest ID&gt; %%</samp></p></td>
<td><p>Attach the given quest ID to the letter, so the player can choose
to accept it.</p></td>
</tr>
<tr>
<td><p><samp>%item quest &lt;quest ID&gt; true %%</samp></p></td>
<td><p>Attach the given quest ID to the letter and add it automatically.
(If the player has the <samp>NOQUEST_&lt;quest ID&gt;</samp> mail flag
set, it won't be added automatically.)</p></td>
</tr>
<tr>
<td><p><samp>%item specialOrder &lt;order ID&gt; [immediately]
%%</samp></p></td>
<td><p>Attach a special order with the given ID to the letter. If
[immediately] is true, the order is accepted automatically. (If the
player has the <samp>NOSPECIALORDER_&lt;order ID&gt;</samp> mail flag
set, it won't be added automatically.)</p></td>
</tr>
</tbody>
</table>

### Examples

You can add mail that the player can view once they receive it from
their mailbox. For example, this content pack adds a letter that
includes a pufferchick object, as well as starting a conversation topic
using a trigger action:

This letter will have to be sent in a separate patch, such as by using
<a href="Modding_Trigger_actions" class="wikilink"
title="trigger actions">trigger actions</a> or
<a href="Modding_Event_data" class="wikilink"
title="event commands">event commands</a>.

#### Deprecated mail commands

These are deprecated and should no longer be used in newer letters.

## Mail flags

### Overview

The game tracks *mail flags* for each player. This is used for two
purposes:

- Tracking received letters. The key for each letter in `Data\Mail` is a
  mail flag; if the player has the flag for a letter, the game considers
  it to be received.
- Tracking non-mail changes in the world. For example, `artifactFound`
  means the player has found at least one artifact, `jojaMember` means
  the player has a Joja membership, etc. These have no letter associated
  with them.

Letter IDs can be used as mail flags once they are received by the
player. Alternatively, you can define and send a letter ID in the mail
send command itself (such as by using
<a href="Modding_Trigger_actions" class="wikilink"
title="trigger actions">trigger actions</a> or
<a href="Modding_Event_data" class="wikilink"
title="event commands">event commands</a>) without including a
corresponding Data/Mail entry. Doing so will lead to the player
receiving the mail flag, which can be checked using the methods below,
without the player receiving an actual letter in their mailbox.

In other words, if the letter has a Data/Mail entry, the player will
receive both the mail flag and the visible mail in their mailbox. If the
letter does not have a Data/Mail entry, the player will only receive the
mail flag, which is invisible to them.

You can check the mail flags in-game:

<table>
<thead>
<tr>
<th><p>mod type</p></th>
<th><p>info</p></th>
</tr>
</thead>
<tbody>
<tr>
<td data-valign="top"><p><a href="Modding_Content_Patcher"
class="wikilink" title="Content Patcher">Content Patcher</a>
packs</p></td>
<td><p>You can check mail flags using the <samp>HasFlag</samp>
condition. For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>{</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Action&quot;</span><span class="op">:</span> <span class="st">&quot;EditImage&quot;</span><span class="op">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Target&quot;</span><span class="op">:</span> <span class="st">&quot;Portraits/Abigail&quot;</span><span class="op">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;FromFile&quot;</span><span class="op">:</span> <span class="st">&quot;assets/abigail-bow.png&quot;</span><span class="op">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;When&quot;</span><span class="op">:</span> {</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;HasFlag&quot;</span><span class="op">:</span> <span class="st">&quot;Beat_PK&quot;</span> <span class="co">// player beat the Prairie King game</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td data-valign="top"><p>C# mods</p></td>
<td><p>Mail flags are tracked in three main fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Game1.player.mailForTomorrow</samp></p></td>
<td><p>Letters to add to the player's mailbox at the start of the next
day.</p></td>
</tr>
<tr>
<td><p><samp>Game1.player.mailbox</samp></p></td>
<td><p>Letters currently in the player's mailbox.</p></td>
</tr>
<tr>
<td><p><samp>Game1.player.mailReceived</samp></p></td>
<td><p>All mail flags set for the player. That includes both letters and
non-mail flags.</p></td>
</tr>
</tbody>
</table>
<p>You can either check the fields individually, or use the game's
<samp>Game1.player.hasOrWillReceiveMail(string id)</samp> method to
check all three.</p></td>
</tr>
</tbody>
</table>

### List

There are far too many flags to list, but here are some useful ones:

<a href="Community_Center" class="wikilink"
title="Community Center">Community Center</a> and <a href="JojaMart" class="wikilink" title="JojaMart">JojaMart</a>
{\| class="wikitable"

\|- ! flag ! meaning \|- \| `abandonedJojaMartAccessible` \| The
<a href="Bundles#Abandoned_JojaMart" class="wikilink"
title="abandoned JojaMart">abandoned JojaMart</a> is accessible. \|- \|
`canReadJunimoText` \| The player can read the language of Junimos
(*i.e.,* the plaques in the Community Center). \|- \| `ccIsComplete` \|
The player has completed the <a href="Community_Center" class="wikilink"
title="community center">community center</a>. Note that this isn't set
reliably; if using <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a>, use the
`IsCommunityCenterComplete` and `IsJojaMartComplete` tokens instead.

These flags are set when completing each bundle (in both community
center and Joja paths):

- `ccBoilerRoom` (repairs minecarts);
- `ccBulletin` (friendship bonus with many villagers);
- `ccCraftsRoom` (repairs bridge to the
  <a href="quarry" class="wikilink" title="quarry">quarry</a>);
- `ccFishTank` (unlocks the
  <a href="Pans" class="wikilink" title="copper pan">copper pan</a>);
- `ccPantry` (unlocks the
  <a href="greenhouse" class="wikilink" title="greenhouse">greenhouse</a>);
- `ccVault` (repairs the bus and unlocks access to
  <a href="The_Desert" class="wikilink" title="the desert">the desert</a>).

You can also check for Joja specifically using `jojaBoilerRoom`,
`jojaCraftsRoom`, `jojaFishTank`, `jojaPantry`, and `jojaVault`. \|- \|
`ccMovieTheater`\
`ccMovieTheaterJoja` \| The movie theater has been constructed, either
through the community path (only `ccMovieTheater` is set) or through
Joja (both are set). \|- \| `jojaMember` \| The player bought a
<a href="JojaMart" class="wikilink" title="JojaMart">JojaMart</a>
membership. \|}

Found items
{\| class="wikitable"

\|- ! flag ! meaning \|- \| `artifactFound` \| The player has found at
least one artifact. \|- \| `galaxySword` \| The player has acquired the
<a href="Galaxy_Sword" class="wikilink" title="Galaxy Sword">Galaxy
Sword</a>. \|- \| `geodeFound` \| The player has found at least one
geode. \|}

Unlocked areas & upgrades
{\| class="wikitable"

\|- ! area ! flag ! meaning \|- \|
<a href="Secret_Woods" class="wikilink" title="Secret Woods">Secret
Woods</a> \| `beenToWoods` \| The player has entered the
<a href="Secret_Woods" class="wikilink" title="Secret Woods">Secret
Woods</a> at least once. \|- \|
<a href="Pelican_Town" class="wikilink" title="Town">Town</a> \|
`doorUnlock*` \| The player has unlocked access to a given NPC's room.
See the flag for each NPC: `doorUnlockAbigail`, `doorUnlockAlex`,
`doorUnlockCaroline`, `doorUnlockEmily`, `doorUnlockHaley`,
`doorUnlockHarvey`, `doorUnlockJas`, `doorUnlockJodi`,
`doorUnlockMarnie`, `doorUnlockMaru`, `doorUnlockPenny`,
`doorUnlockPierre`, `doorUnlockRobin`, `doorUnlockSam`,
`doorUnlockSebastian`, `doorUnlockVincent`. \|- \|
<a href="The_Mountain" class="wikilink" title="Mountain">Mountain</a> \|
`landslideDone` \| The landside blocking access to
<a href="The_Mines" class="wikilink" title="the mines">the mines</a> has
been cleared. \|- \|
<a href="The_Sewers" class="wikilink" title="Sewers">Sewers</a> \|
`openedSewer` \| The player has unlocked the sewers. \|- \|
<a href="The_Beach" class="wikilink" title="Beach">Beach</a> \|
`beachBridgeFixed` \| The player repaired the bridge to the
<a href="The_Beach#Tide_Pools" class="wikilink" title="East Pier">East
Pier</a>. \|- \|
<a href="Fish_Shop" class="wikilink" title="Fish Shop">Fish Shop</a> \|
`willyBoatFixed` \| The player fixed Willy's boat, so they can now
access
<a href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a>. \|- \| <a href="Ginger_Island#Island_West" class="wikilink"
title="Island farm">Island farm</a> \| `Island_UpgradeParrotPlatform` \|
The player unlocked the
<a href="Ginger_Island#Parrot_Express" class="wikilink"
title="Parrot Express">Parrot Express</a>. \|- \|
<a href="Ginger_Island#Island_West" class="wikilink"
title="Island farm">Island farm</a> \| `Island_UpgradeHouse` \| The
player unlocked the island house. \|- \|
<a href="Ginger_Island#Island_West" class="wikilink"
title="Island farm">Island farm</a> \| `Island_UpgradeHouse_Mailbox` \|
The player unlocked the island mailbox. \|- \|
<a href="Ginger_Island#Island_West" class="wikilink"
title="Island farm">Island farm</a> \| `Island_W_Obelisk` \| The player
unlocked the island
<a href="Farm_Obelisk" class="wikilink" title="Farm Obelisk">Farm
Obelisk</a>. \|- \|
<a href="Ginger_Island#Island_North" class="wikilink"
title="Island north">Island north</a> \| `Island_FirstParrot` \| The
player unlocked access to the norther section of the island. \|- \|
<a href="Ginger_Island#Island_North" class="wikilink"
title="Island north">Island north</a> \| `Island_UpgradeBridge` \| The
player repaired the bridge to the
<a href="Ginger_Island#Dig_Site" class="wikilink"
title="island dig site">island dig site</a>. \|- \|
<a href="Ginger_Island#Island_North" class="wikilink"
title="Island north">Island north</a> \| `Island_UpgradeTrader` \| The
player unlocked the
<a href="Island_Trader" class="wikilink" title="Island Trader">Island
Trader</a>. \|- \| <a href="Ginger_Island#Island_South" class="wikilink"
title="Island south">Island south</a> \| `Island_Resort` \| The player
built the island resort. \|- \|
<a href="Ginger_Island#Island_South" class="wikilink"
title="Island south">Island south</a> \| `Island_Turtle` \| The player
unlocked access to the island farm. \|- \|
<a href="Skull_Cavern" class="wikilink" title="Skull Cavern">Skull
Cavern</a> \| `HasUnlockedSkullDoor` \| Whether the player has used the
<a href="Skull_Key" class="wikilink" title="Skull Key">Skull Key</a> to
unlock the door in
<a href="Skull_Cavern" class="wikilink" title="Skull Cavern">Skull
Cavern</a>. \|- \|
<a href="Volcano_Dungeon" class="wikilink" title="Volcano">Volcano</a>
\| `Island_VolcanoBridge` \| The player unlocked the bridge at the
Volcano Dungeon entrance. \|- \|
<a href="Volcano_Dungeon" class="wikilink" title="Volcano">Volcano</a>
\| `Island_VolcanoShortcutOut` \| The player unlocked the shortcut exit
from the <a href="Volcano_Dungeon#Shop" class="wikilink"
title="volcano shop">volcano shop</a>. \|}

Completed <a href="Adventurer&#39;s_Guild#Monster_Eradication_Goals"
class="wikilink"
title="Adventurer&#39;s guild monster eradication goals">Adventurer's
guild monster eradication goals</a>
{\| class="wikitable"

\|- ! flag ! goal ! reward \|- \| `Gil_Arcane Hat` \| Kill 100 mummies
\| \|- \| `Gil_Burglar's Ring` \| Kill 500 dust sprites \| \|- \|
`Gil_Crabshell Ring` \| Kill 60 crabs \| \|- \| `Gil_Hard Hat` \| Kill
30 duggies \| \|- \| `Gil_Insect Head` \| Kill 125 cave insects \| \|-
\| `Gil_Knight's Helmet` \| Kill 50 pepper rexes \| \|- \|
`Gil_Napalm Ring` \| Kill 250 serpents \| \|- \| `Gil_Savage Ring` \|
Kill 150 void spirits \| \|- \| `Gil_Skeleton Mask` \| Kill 50 skeletons
\| \|- \| `Gil_Slime Charmer Ring` \| Kill 1000 slimes \| \|- \|
`Gil_Telephone` \| Kill 150 magma sprites \|
<a href="Telephone" class="wikilink" title="Telephone">Telephone</a>
number for adventurer's guild \|- \| `Gil_Vampire Ring` \| Kill 200 bats
\| \|}

<a href="Special_Items_&amp;_Powers" class="wikilink"
title="Special Items &amp; Powers">Special Items &amp; Powers</a>
{\| class="wikitable"

\|- ! flag ! special item/power \|- \| `HasClubCard` \| \|- \|
`HasDarkTalisman` \| \|- \| `HasDwarvishTranslationGuide` \| \|- \|
`HasMagicInk` \| \|- \| `HasMagnifyingGlass` \| \|- \| `HasRustyKey` \|
\|- \| `HasSkullKey` \| \|- \| `HasSpecialCharm` \| \|- \| `HasTownKey`
\| \|}

Other
{\| class="wikitable"

\|- ! flag ! meaning \|- \| `Beat_PK` \| The player has beaten the
<a href="Prairie_King_Arcade_System" class="wikilink"
title="Prairie King">Prairie King</a> arcade game. \|- \| `Farm_Eternal`
\| The player has reached a 100%
<a href="perfection" class="wikilink" title="perfection">perfection</a>
score. \|- \| `guildMember` \| The player is a member of the
<a href="Adventurer&#39;s_Guild" class="wikilink"
title="Adventurer&#39;s Guild">Adventurer's Guild</a>. \|- \|
`JunimoKart` \| The player has beaten the
<a href="Junimo_Kart" class="wikilink" title="Junimo Kart">Junimo
Kart</a> arcade game. \|- \| `museumComplete` \| The player has
completed the
<a href="Museum" class="wikilink" title="Museum">Museum</a> artifact
collection. \|- \| `qiChallengeComplete` \| The player completed the
Qi's Challenge <a href="Quests" class="wikilink" title="quest">quest</a>
by reaching level 25 in the Skull Cavern. \|}

## Custom mail formatting

You can customize mail and
<a href="Secret_Notes" class="wikilink" title="secret notes">secret
notes</a> by including three custom commands in the letter text
(including the `[]` characters). This needs to be added before the
`[#]<letter_name>` tag:

| command | effect |
|----|----|
| `[letterbg <index>]` | Changes the default letter background to a vanilla background from `LooseSprites/letterBG`. The index can be 0 (default letter), 1 (Sandy's lined paper), 2 (Wizard style), 3 (Krobus style) or 4 (JojaMart style). This will also set the default text color for that style, unless overridden by `textcolor`. |
| `[letterbg <asset name> <index>]` | Changes the default letter background to the given texture. The asset name should match a texture containing two rows: one with 320x180 pixel letter background images, and one with 24x24 pixel button backgrounds shown behind attached items. The index is the sprite to use from those rows, starting at 0 for the first one. Only the first 4 letter background images of a row will be properly displayed. Only one row of button may exist. See image below |
| `[textcolor <color>]` | Changes the letter text color. The valid colors are `black`, `blue`, `cyan`, `gray`, `green`, `orange`, `purple`, `red`, and `white`. |

<a href="File_Lettersbglayers.png" class="wikilink"
title="center">center</a>

<a href="ru_Модификации_Почта" class="wikilink"
title="ru:Модификации:Почта">ru:Модификации:Почта</a>
<a href="zh_模组_信件数据" class="wikilink"
title="zh:模组:信件数据">zh:模组:信件数据</a>
<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>
