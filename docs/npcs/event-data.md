---
title: "Event Data"
wiki_source: "Modding:Event data"
permalink: /Modding:Event_data/
category: npcs
tags: [event-data, raw-data, event-preconditions, format, built-in-preconditions, event-scripts, basic-format, comments]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses event data. This is an
advanced guide for mod developers.

## Raw data

Events are stored according to the location they occur in, in the asset
`Data/Events/<LocationName>`. You can
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpack your XNB files">unpack your XNB files</a> for reference.

For example, here's the raw data (in English) for events in
<a href="Trailer" class="wikilink" title="Pam&#39;s trailer">Pam's
trailer</a> (`Data/Events/Trailer`) as of :

## Event preconditions

### Format

Each event has a key in the form `<event ID>/[preconditions]`, which has
two components:

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>event ID</p></td>
<td><p>A <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> which
identifies the event. Older vanilla events use a number for legacy
reasons, but mod events are <strong>strongly encouraged</strong> to
follow the <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID format">unique string ID
format</a> (including the mod ID prefix) to prevent conflicts between
mods.</p></td>
</tr>
<tr>
<td><p>preconditions</p></td>
<td><p>A slash (<samp>/</samp>)-delimited list of the preconditions
listed in the sections below. You can prefix any precondition with
<code>!</code> to negate it (e.g. <code>!Season Winter</code> for any
season except winter). If an event has no preconditions, it must have a
trailing slash to distinguish it from forks.</p>
<p>Precondition keys are case-insensitive, but their arguments may not
be. Using the exact capitalization shown is recommended to avoid
issues.</p>
<p>You can escape spaces and slashes in arguments using quotes like
this: <code>/GameStateQuery "SEASON Spring"/</code>.</p></td>
</tr>
</tbody>
</table>

For example (assuming you use
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> with its token):

- `_EventId/`: event ID is `_EventId` with no preconditions.
- `_EventId/Time 1900 2300/Friendship Clint 750`: event ID is
  `_EventId`; the event only happens between 7pm and 11pm when you have
  3 hearts (750
  <a href="Friendship" class="wikilink" title="points">points</a>) with
  Clint.

### Built-in preconditions

#### Game state queries

This lets you check arbitrary conditions not covered by another
precondition.

| name and arguments | description |
|----|----|
| `GameStateQuery <query>` | A <a href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> matches, like `GameStateQuery !WEATHER Here Sun` for 'not sunny in this location'. |

#### World/Context

These check the current time, date, weather, etc. They're not
player-specific.

| name and arguments | description |
|----|----|
| `ActiveDialogueEvent <ID>` | The special dialogue event with the given ID (including <a href="Modding_Dialogue#Conversation_topics" class="wikilink"
title="Conversation Topics">Conversation Topics</a>) is in progress. |
| `DayOfMonth <number>+` | Today is one of the specified days of the month (may specify multiple days). Days should be integers (*e.g.*, `12`). |
| `DayOfWeek <day>+` | Today is one of the specified days (may specify multiple days). This can be a case-insensitive three-letter abbreviation (like `Mon`) or full name (like `Monday`). |
| `FestivalDay` | Today is a <a href="Festivals" class="wikilink" title="festival">festival</a> day. |
| `GoldenWalnuts <number>` | The players in total have found at least this many <a href="Golden_Walnut" class="wikilink" title="golden walnuts">golden
walnuts</a>, including spent walnuts. |
| `InUpgradedHouse [level]` | The current location is a farmhouse or cabin, and it has been upgraded at least \[level\] times. Default value: `2`. |
| `NPCVisible <name>` | The NPC with that internal name is present and visible in any location. |
| `NpcVisibleHere <name>` | The NPC with that internal name is present and visible in the current location. |
| `Random <number>` | Matches randomly, where \<number\> is the probability between 0 and 1 of permitting the event (*e.g.,* `0.2` for a 20% chance). |
| `Season <season>+` | The current season is one of the given values (may specify multiple seasons). |
| `Time <min> <max>` | The current time of day is between the given values, inclusive. Values use the 26-hour clock (`600` to `2600`). |
| `UpcomingFestival <number>` | A <a href="Festivals" class="wikilink" title="festival">festival</a> day will occur within the given number of days. |
| `Weather <weather>` | The weather in the current location's context matches \<weather\>. Valid values: `rainy`, `sunny`, or a specific weather ID. |
| `WorldState <ID>` | The given world state ID is active anywhere. |
| `Year <year>` | If \<year\> is 1, must be in the first year. Otherwise, year must be at least this value. |

#### Current player

These check the current player (the one playing this instance of the
game).

| name and arguments | description |
|----|----|
| `ChoseDialogueAnswers <dialogue ID>+` | Current player has chosen all of the given dialogue answer IDs (can specify multiple IDs). |
| `Dating <name>` | Current player is dating the NPC with that internal name. |
| `EarnedMoney <number>` | Current player has earned at least this much money (including spent money). |
| `FreeInventorySlots <number>` | Current player has at least this many free inventory slots. |
| `Friendship <name> <number>+` | Current player has at least this many <a href="friendship" class="wikilink"
title="friendship points">friendship points</a> with all of the NPCs with those internal names (can specify multiple name/number pairs). |
| `Gender <gender>` | Current player is male (if \<gender\> is `male`, case-insensitive) or not male (if \<gender\> is anything else). |
| `HasItem <item ID>` | Current player has the given item in their inventory. |
| `HasMoney <number>` | Current player has at least this much money on hand (does not include spent money). |
| `LocalMail <letter ID>` | Current player has received the given mail. |
| `MissingPet [pet]` | Current player has not yet received a pet, and their preference matches \[pet\] (can be any pet type). Default: matches any preference. |
| `ReachedMineBottom [number]` | Current player has reached the bottom floor of the <a href="The_Mines" class="wikilink" title="Mines">Mines</a> at least this many times. Default value: `1`. |
| `Roommate` | Current player is roommates with any NPC. |
| `SawEvent <event ID>+` | Current player has seen *any* of the given events (may specify multiple IDs). To check whether the player has seen *all* of several events, use this precondition multiple times. |
| `SawSecretNote <number>` | Current player has seen the <a href="Secret_Notes" class="wikilink" title="Secret Note">Secret
Note</a> with the given (integer) ID. |
| `Shipped <item ID> <number>+` | Current player has shipped at least this many of each specified item (can specify multiple item/number pairs). This only works for the items tracked by the game for shipping stats (shown in the <a href="Shipping#Collection" class="wikilink"
title="shipping collections menu">shipping collections menu</a>). |
| `Skill <name> <level>` | Current player has reached at least this level in the given skill (one of `Combat`, `Farming`, `Fishing`, `Foraging`, `Luck`, or `Mining`) |
| `Spouse <name>` | Current player is married or engaged to the NPC with that internal name. |
| `SpouseBed` | Current player has a double bed in their house (or, if they have a roommate, a single bed). But if the roommate is Krobus, will never match. |
| `Tile <x> <y>+` | Current player is standing on one of the given tile positions (can specify multiple x/y positions). |

#### Host player

These check the host player (the one running a multiplayer farm, not
necessarily the current player). If single-player, this is always the
current player.

| name and arguments | description |
|----|----|
| `CommunityCenterOrWarehouseDone` | The <a href="Community_Center" class="wikilink"
title="Community Center">Community Center</a> or <a href="Joja_Warehouse" class="wikilink" title="Joja Warehouse">Joja
Warehouse</a> has been completed. |
| `DaysPlayed <number>` | Host player has played at least this many days. |
| `HostMail <letter ID>` | Host player has received the indicated mail. |
| `HostOrLocalMail <letter ID>` | Either the host or the current player has received the indicated mail. |
| `IsHost` | Current player is the host player. |
| `JojaBundlesDone` | All <a href="JojaMart#Community_Development_Projects" class="wikilink"
title="Joja bundles">Joja bundles</a> have been completed. |

#### Deprecated

Deprecated aliases
Some older preconditions have a short-form alias, like `j` for
`DaysPlayed`. These are deprecated, **case-sensitive**, and shouldn't be
used in new events.

{\| class="wikitable sortable mw-collapsible mw-collapsed"

\|- ! legacy alias (do not use) ! use instead \|- \| `*` \|
<a href="#WorldState" class="wikilink"
title="WorldState"><samp>WorldState</samp></a> \|- \| `*n` \|
<a href="#HostOrLocalMail" class="wikilink"
title="HostOrLocalMail"><samp>HostOrLocalMail</samp></a> \|- \| `a` \|
<a href="#Tile" class="wikilink" title="Tile"><samp>Tile</samp></a> \|-
\| `b` \| <a href="#ReachedMineBottom" class="wikilink"
title="ReachedMineBottom"><samp>ReachedMineBottom</samp></a> \|- \| `B`
\| <a href="#SpouseBed" class="wikilink"
title="SpouseBed"><samp>SpouseBed</samp></a> \|- \| `C` \|
<a href="#CommunityCenterOrWarehouseDone" class="wikilink"
title="CommunityCenterOrWarehouseDone"><samp>CommunityCenterOrWarehouseDone</samp></a>
\|- \| `c` \| <a href="#FreeInventorySlots" class="wikilink"
title="FreeInventorySlots"><samp>FreeInventorySlots</samp></a> \|- \|
`D` \| <a href="#Dating" class="wikilink"
title="Dating"><samp>Dating</samp></a> \|- \| `e` \|
<a href="#SawEvent" class="wikilink"
title="SawEvent"><samp>SawEvent</samp></a> \|- \| `f` \|
<a href="#Friendship" class="wikilink"
title="Friendship"><samp>Friendship</samp></a> \|- \| `G` \|
<a href="#GameStateQuery" class="wikilink"
title="GameStateQuery"><samp>GameStateQuery</samp></a> \|- \| `g` \|
<a href="#Gender" class="wikilink"
title="Gender"><samp>Gender</samp></a> \|- \| `H` \|
<a href="#IsHost" class="wikilink"
title="IsHost"><samp>IsHost</samp></a> \|- \| `h` \|
<a href="#MissingPet" class="wikilink"
title="MissingPet"><samp>MissingPet</samp></a> \|- \| `Hn` \|
<a href="#HostMail" class="wikilink"
title="HostMail"><samp>HostMail</samp></a> \|- \| `i` \|
<a href="#HasItem" class="wikilink"
title="HasItem"><samp>HasItem</samp></a> \|- \| `j` \|
<a href="#DaysPlayed" class="wikilink"
title="DaysPlayed"><samp>DaysPlayed</samp></a> \|- \| `J` \|
<a href="#JojaBundlesDone" class="wikilink"
title="JojaBundlesDone"><samp>JojaBundlesDone</samp></a> \|- \| `L` \|
<a href="#InUpgradedHouse" class="wikilink"
title="InUpgradedHouse"><samp>InUpgradedHouse</samp></a> \|- \| `m` \|
<a href="#EarnedMoney" class="wikilink"
title="EarnedMoney"><samp>EarnedMoney</samp></a> \|- \| `M` \|
<a href="#HasMoney" class="wikilink"
title="HasMoney"><samp>HasMoney</samp></a> \|- \| `N` \|
<a href="#GoldenWalnuts" class="wikilink"
title="GoldenWalnuts"><samp>GoldenWalnuts</samp></a> \|- \| `n` \|
<a href="#LocalMail" class="wikilink"
title="LocalMail"><samp>LocalMail</samp></a> \|- \| `O` \|
<a href="#Spouse" class="wikilink"
title="Spouse"><samp>Spouse</samp></a> \|- \| `p` \|
<a href="#NpcVisibleHere" class="wikilink"
title="NpcVisibleHere"><samp>NpcVisibleHere</samp></a> \|- \| `q` \|
<a href="#ChoseDialogueAnswers" class="wikilink"
title="ChoseDialogueAnswers"><samp>ChoseDialogueAnswers</samp></a> \|-
\| `r` \| <a href="#Random" class="wikilink"
title="Random"><samp>Random</samp></a> \|- \| `R` \|
<a href="#Roommate" class="wikilink"
title="Roommate"><samp>Roommate</samp></a> \|- \| `S` \|
<a href="#SawSecretNote" class="wikilink"
title="SawSecretNote"><samp>SawSecretNote</samp></a> \|- \| `s` \|
<a href="#Shipped" class="wikilink"
title="Shipped"><samp>Shipped</samp></a> \|- \| `t` \|
<a href="#Time" class="wikilink" title="Time"><samp>Time</samp></a> \|-
\| `u` \| <a href="#DayOfMonth" class="wikilink"
title="DayOfMonth"><samp>DayOfMonth</samp></a> \|- \| `v` \|
<a href="#NPCVisible" class="wikilink"
title="NPCVisible"><samp>NPCVisible</samp></a> \|- \| `w` \|
<a href="#Weather" class="wikilink"
title="Weather"><samp>Weather</samp></a> \|- \| `y` \|
<a href="#Year" class="wikilink" title="Year"><samp>Year</samp></a> \|}

Deprecated preconditions
These are deprecated and should no longer be used in newer events.

{\| class="wikitable sortable mw-collapsible mw-collapsed"

\|- ! precondition (do not use) ! legacy alias (do not use) !
description \|- \| `SendMail <letter ID> [true]` \| `x` \|

**Obsolete <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Send-mail_(x)_precondition_deprecated"
class="wikilink" title="since Stardew Valley 1.6">since Stardew Valley
1.6</a>.** Use a <a href="Modding_Trigger_actions" class="wikilink"
title="trigger action">trigger action</a> in the event instead to send
mail.

For the current player: mark this event as seen, add the specified
letter to tomorrow's mail, then abort without starting the event. Use
the optional argument `true` to add the letter directly to the mailbox
instead of sending it tomorrow.

\|}

Deprecated negations
Some older preconditions had custom negative forms. These have been
replaced by the newer `!` syntax.

{\| class="wikitable sortable mw-collapsible mw-collapsed"

\|- ! legacy name (do not use) ! legacy alias (do not use) ! use instead
\|- \| `NotActiveDialogueEvent` \| `A` \| `!ActiveDialogueEvent` \|- \|
`NotCommunityCenterOrWarehouseDone` \| `X` \|
`!CommunityCenterOrWarehouseDone` \|- \| `NotDayOfWeek` \| `d` \|
`!DayOfWeek` \|- \| `NotFestivalDay` \| `F` \| `!FestivalDay` \|- \|
`NotHostMail` \| `Hl` \| `!HostMail` \|- \| `NotHostOrLocalMail` \| `*l`
\| `!HostOrLocalMail` \|- \| `NotLocalMail` \| `l` \| `!LocalMail` \|-
\| `NotRoommate` \| `Rf` \| `!Roommate` \|- \| `NotSawEvent` \| `k` \|
`!SawEvent` \|- \| `NotSeason` \| `z` \| `!Season` \|- \| `NotSpouse` \|
`o` \| `!Spouse` \|- \| `NotUpcomingFestival` \| `U` \|
`!UpcomingFestival` \|}

## Event scripts

### Basic format

Each event has a value which is the event script. This specifies what
happens in the event — everything from lighting and music to NPC
movement and dialogue. The script consists of multiple commands
separated by forward slash (`/`) characters. Event commands are
quote-aware, so you can use spaces and slashes in arguments like
`speak Penny \"I'm running A/B tests\"` without needing to escape them
(the quote marks themselves do need to be escaped).

Every script must start with three commands in this exact order:

<table>
<thead>
<tr>
<th><p>index</p></th>
<th><p>syntax</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0</p></td>
<td><p><samp>&lt;music ID&gt;</samp></p></td>
<td><p>The background music or ambient sounds to play during the event.
This can be...</p>
<ul>
<li>an <a href="Modding_Audio#Track_list" class="wikilink"
title="audio track ID">audio track ID</a> to play;</li>
<li>or <code>none</code> to stop any existing music and use the default
ambient background noise for the location;</li>
<li>or <code>continue</code> to keep playing the current background
music.</li>
</ul>
<p>This can be changed later using the <code>playMusic</code> or
<code>stopMusic</code> event commands.</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p><samp>&lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p>The tile coordinates the camera should center on at the start of
the event.</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p><samp>[&lt;character ID&gt; &lt;x&gt; &lt;y&gt;
&lt;direction&gt;]+</samp></p></td>
<td><p>Initialises one or more characters' starting tile positions and
<a href="#Directions" class="wikilink"
title="directions">directions</a>. The character ID can be
<samp>farmer</samp> or an NPC name like <samp>Abigail</samp>. Note:
Unlike other commands with a &lt;direction&gt; argument, directions in
this command <em>must</em> be numeric values.</p></td>
</tr>
</tbody>
</table>

Those three commands may be followed by any sequence of the following
commands:

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>action &lt;action&gt;</samp></p></td>
<td><p>Run a <a href="Modding_Trigger_actions" class="wikilink"
title="trigger action string">trigger action string</a>, like
<samp>action AddMoney 500</samp> to add to the current player.</p></td>
</tr>
<tr>
<td><p><samp>addBigProp &lt;x&gt; &lt;y&gt; &lt;object
ID&gt;</samp></p></td>
<td><p>Adds an object at the specified tile from the
<samp>TileSheets\Craftables.png</samp> sprite sheet.</p></td>
</tr>
<tr>
<td><p><samp>addConversationTopic &lt;ID&gt; [length]</samp></p></td>
<td><p>Starts a <a href="Modding_Dialogue#Conversation_topics"
class="wikilink" title="conversation topic">conversation topic</a> with
the given ID and day length (or 4 days if no length given). Setting
length as 0 will have the topic last only for the current day.</p></td>
</tr>
<tr>
<td><p><samp>addCookingRecipe &lt;recipe&gt;</samp></p></td>
<td><p>Adds the specified cooking recipe to the player.</p></td>
</tr>
<tr>
<td><p><samp>addCraftingRecipe &lt;recipe&gt;</samp></p></td>
<td><p>Adds the specified crafting recipe to the player.</p></td>
</tr>
<tr>
<td><p><samp>addFloorProp &lt;prop index&gt; &lt;x&gt; &lt;y&gt; [solid
width] [solid height] [display height]</samp></p></td>
<td><p>Add a non-solid prop from the current festival texture. Default
solid width/height is 1. Default display height is solid
height.</p></td>
</tr>
<tr>
<td><p><samp>addItem &lt;item ID&gt; [count] [quality]</samp></p></td>
<td><p>Add an item to the player inventory (or open a grab menu if their
inventory is full). The &lt;item ID&gt; is the <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a>, and [quality] is a <a href="Modding_Items#Quality"
class="wikilink" title="numeric quality value">numeric quality
value</a>.</p></td>
</tr>
<tr>
<td><p><samp>addLantern &lt;row in texture&gt; &lt;x&gt; &lt;y&gt;
&lt;light radius&gt;</samp></p></td>
<td><p>Adds a glowing temporary sprite at the specified tile from the
<samp>Maps\springobjects.png</samp> sprite sheet. A light radius of
<samp>0</samp> just places the sprite. Sprites are in 20 columns of
16x16 squares. The index for the default lantern sprite is 735.</p></td>
</tr>
<tr>
<td><p><samp>addObject &lt;x&gt; &lt;y&gt; &lt;item ID&gt; [layer
depth]</samp></p></td>
<td><p>Adds a temporary sprite at the tile specified by &lt;x&gt; and
&lt;y&gt; using a <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a> from <samp>Data/Objects</samp>.</p>
<p>The optional [layer depth] is the depth at which to draw the sprite
on the screen. The value starts at 0, and higher numbers draw it over
more things. If omitted (or set to a value below 0), defaults to an
auto-calculated depth.</p></td>
</tr>
<tr>
<td><p><samp>addProp &lt;prop index&gt; &lt;x&gt; &lt;y&gt; [solid
width] [solid height] [display height]</samp></p></td>
<td><p>Add a solid prop from the current festival texture. Default solid
width/height is 1. Default display height is solid height.</p></td>
</tr>
<tr>
<td><p><samp>addQuest &lt;quest ID&gt;</samp></p></td>
<td><p>Add the specified quest to the quest log.</p></td>
</tr>
<tr>
<td><p><samp>addSpecialOrder &lt;order ID&gt;</samp></p></td>
<td><p>Add a special order to the player team. This affects all players,
since special orders are shared.</p></td>
</tr>
<tr>
<td><p><samp>addTemporaryActor &lt;spriteAssetName&gt; &lt;sprite
width&gt; &lt;sprite height&gt; &lt;tile x&gt; &lt;tile y&gt;
&lt;direction&gt; [breather]  [override name]</samp></p></td>
<td><p>Add a temporary actor. <samp>spriteAssetName</samp> is the name
of the sprite to add (e.g., <samp>Ghost</samp>). Underscores in the
asset name are now only replaced with spaces if an exact match wasn't
found. You should quote arguments containing spaces instead, like
<code>addTemporaryActor "White Chicken" …</code>.</p>
<p>[breather] is boolean (default <samp>true</samp>).</p>
<p><code>(default </code><samp>Character</samp><code>) determines whether the sprite will be loaded from </code><samp>"Characters/"</samp><code>, </code><samp>"Animals/"</samp><code>, or </code><samp>"Characters/Monsters/"</samp><code>.</code></p>
<p>[override name] can be used to give the temporary actor a different
name.</p></td>
</tr>
<tr>
<td><p><samp>advancedMove &lt;actor&gt; &lt;loop&gt; &lt;x y&gt;... OR
&lt;direction duration&gt;</samp></p></td>
<td><p>Set multiple movements for an actor. You can set True to have the
actor walk the path continuously. Example:
<code>/advancedMove Robin false 0 3 2 0 0 2 -2 0 0 -2 2 0/</code></p>
<p>To make the actor move along the x axis (left/right), use the number
of tiles to move and 0. For example, <code>-3 0</code> will cause the
actor to walk three tiles to the left while facing left.
<code>2 0</code> will cause the actor to walk two tiles to the right
while facing right.</p>
<p>To make the actor move along the y axis (up/down), use 0 and the
number of tiles to move. For example, <code>0 1</code> will cause the
actor to walk one tile down while facing down. <code>0 -5</code> will
cause the actor to walk five tiles up while facing up.</p>
<p>To make an actor pause, use the direction to face and the number of
milliseconds to pause. 1 is right, 2 is down, 3 is left, and 4 is up.
The reason 4 is up and not 0 is so that advancedMove can tell the
difference between a pause command and a move up/down command.</p>
<p>The code can tell the difference between a move command and a pause
command because a move command must have 0 for either x or y. A pause
command must have non-zero numbers for both numbers in the pair.</p>
<p>Example:
<code>/advancedMove Clint true 4 0 2 5000 -4 0 1 3000/</code> Clint will
have continuous movement moving 4 tiles to the right, facing down upon
arriving, waiting for 5 seconds, then moving 4 tiles to the left, facing
right upon arriving, then waiting for 3 seconds, then loops because the
loop was set to true(see above).</p>
<p>Example:
<code>/advancedMove Pam true 5 0 0 3 3 5000 -6 0 0 -4/</code> Pam first
moves 5 tiles to the right, then directly moves 3 tiles downward, faces
the to the left upon arriving then waits 5 seconds before moving 6 tiles
to the left then moves up 4 tiles directly.</p></td>
</tr>
<tr>
<td><p><samp>ambientLight &lt;r&gt; &lt;g&gt; &lt;b&gt;</samp></p></td>
<td><p>Modifies the ambient light level, with RGB values from 0 to
255.</p></td>
</tr>
<tr>
<td><p><samp>animalNaming</samp></p></td>
<td><p>Show the animal naming menu if no other menu is open. Uses the
current location as Coop. Appears to only work for 'hatched'
animals.</p></td>
</tr>
<tr>
<td><p><samp>animate &lt;actor&gt; &lt;flip&gt; &lt;loop&gt; &lt;frame
duration&gt; &lt;frames...&gt;</samp></p></td>
<td><p>Animate a named actor, using one or more &lt;frames&gt; from
their sprite sheet, for &lt;frame duration&gt; milliseconds per frame.
&lt;frames&gt; are indexed numerically, based on 16x32 pieces of the
image. This index increases as you go from left to right, starting from
0. &lt;flip&gt; indicates whether to flip the sprites along the Y axis;
&lt;loop&gt; indicates whether to repeat the animation until
<samp>stopAnimation</samp> is used. If you're animating the farmer, it
may be helpful to reference <a
href="Modding_Farmer_sprite#Sprite_Index_Breakdown" class="wikilink"
title="Modding:Farmer_sprite#Sprite_Index_Breakdown">Modding:Farmer_sprite#Sprite_Index_Breakdown</a></p></td>
</tr>
<tr>
<td><p><samp>attachCharacterToTempSprite &lt;actor&gt;</samp></p></td>
<td><p>Attach an actor to the most recent temporary sprite.</p></td>
</tr>
<tr>
<td><p><samp>awardFestivalPrize</samp></p></td>
<td><p>Awards the festival prize to the winner for the easter egg hunt
and ice fishing contest. Will not do anything outside those festivals;
see the <samp>awardFestivalPrize</samp> entry with arguments just below
for how to use it in events.</p></td>
</tr>
<tr>
<td><p><samp>awardFestivalPrize </samp></p></td>
<td><p>Awards the specified item to the player (shows a HUD message and
adds the item to the player's inventory). Possible item types are "pan",
"sculpture", "rod", "sword", "hero", "joja", "slimeegg", "emilyClothes",
and "jukebox". <samp>item id</samp> can be any qualified item id. This
command causes an event to skip the next command that comes after it, so
it's recommended to add a <samp>pause</samp> command to stop it skipping
anything important.</p></td>
</tr>
<tr>
<td><p><samp>beginSimultaneousCommand</samp></p></td>
<td><p>Starts a block of commands which the game will attempt to execute
at the same time. End the block with its partner
<samp>endSimultaneousCommand</samp>, like so:</p>
<p><code>beginSimultaneousCommand/&lt;command&gt;/&lt;command&gt;/.../endSimultaneousCommand</code></p>
<p>If the commands can be completed instantly, they will all be set to
run on the same tick. Normally, each command in an event script starts a
minimum of one tick after the previous command, so this block lets you
compress a sequence of quick things down to one tick (some examples of
"quick" commands: <samp>showFrame</samp>, <samp>positionOffset</samp>,
<samp>warp</samp>, etc.). <strong>However</strong>, any event commands
which block the event loop and consume time <em>will still do so</em>
even inside a simultaneousCommand block. This applies to
<samp>move</samp> (without its optional <samp>true</samp> argument to
remove the blocking behavior), <samp>faceDirection</samp> (ditto),
<samp>emote</samp> (ditto), <samp>speak</samp>, <samp>pause</samp>, and
many others. Commands like this are not suitable for use in these
blocks, and commands following them will not execute simultaneously.</p>
<p>As a result of the blocking command behavior, <strong>this command is
not suitable for achieving parallel action in an event</strong> (e.g.
one character walks to a target spot while another speaks); for that you
will want to use optional <samp>true</samp>s, <samp>advancedMove</samp>,
and the like. This command is only useful if you want to avoid a
one-frame delay between instant commands, for example between
<samp>addItem</samp> and <samp>setSkipActions</samp> (one-frame window
to get an item twice), or between <samp>showFrame</samp> and
<samp>positionOffset</samp> (one frame where only one is
applied).</p></td>
</tr>
<tr>
<td><p><samp>broadcastEvent [bool useLocalFarmer]</samp></p></td>
<td><p>Makes the event a "broadcast event", forcing others players
connected to also see it. Any players connected will be forced to warp
to this event. This is used in some vanilla events like when Lewis shows
the farmer the abandoned Community Center.</p>
<p>If <samp>true</samp>, <samp>useLocalFarmer</samp> will make the
Farmer actor in the event the individual player's Farmer, otherwise if
omitted or <samp>false</samp> it will be the host's Farmer. The
<samp>useLocalFarmer</samp> option isn't used anywhere in the vanilla
game.</p></td>
</tr>
<tr>
<td><p><samp>catQuestion</samp></p></td>
<td><p>Trigger question about adopting your pet.</p></td>
</tr>
<tr>
<td><p><samp>cave</samp></p></td>
<td><p>Trigger the question for the farm cave type. This will work again
later, however changing from bats to mushrooms will not remove the
mushroom spawning objects.</p></td>
</tr>
<tr>
<td><p><samp>changeLocation &lt;location&gt;</samp></p></td>
<td><p>Change to another location and run the remaining event script
there.</p></td>
</tr>
<tr>
<td><p><samp>changeMapTile &lt;layer&gt; &lt;x&gt; &lt;y&gt; &lt;tile
index&gt;</samp></p></td>
<td><p>Change the specified tile to a particular value.</p></td>
</tr>
<tr>
<td><p><samp>changeName &lt;actor&gt; &lt;displayName&gt;</p></td>
<td><p>Sets the display name of the actor to displayName. Quote
arguments containing spaces, like
<code>changeName Leo "Neo Leo"</code>.</p></td>
</tr>
<tr>
<td><p><samp>changePortrait &lt;npc&gt; [portrait]</samp></p></td>
<td><p>Change the portrait asset for specified NPC's portrait to one
matching the form <samp>"Portraits/&lt;actor&gt;_[portrait]"</samp>. For
example, <code>changePortrait Shane JojaMart</code> would make Shane use
his JojaMart portrait. Repeat the command without the [portrait]
argument to change the NPC back to their normal portrait.</p></td>
</tr>
<tr>
<td><p><samp>changeSprite &lt;actor&gt; [sprite]</samp></p></td>
<td><p>Change the sprite asset for specified NPC's portrait to one
matching the form <samp>"Characters/&lt;actor&gt;_[sprite]"</samp>. For
example, <code>changeSprite Shane JojaMart</code> would make Shane use
his JojaMart sprite. Repeat the command without the [sprite] argument to
change the NPC back to their normal sprite.</p></td>
</tr>
<tr>
<td><p><samp>changeToTemporaryMap &lt;map&gt; [clamp]</samp></p></td>
<td><p>Change the location to a temporary one loaded from the map file
specified by &lt;map&gt;. The [clamp] argument (<samp>true/false</samp>,
default <samp>true</samp>) reclamps the viewport to be in-bounds when
<samp>true</samp>.</p></td>
</tr>
<tr>
<td><p><samp>changeYSourceRectOffset &lt;npc&gt;
&lt;offset&gt;</samp></p></td>
<td><p>Changes the NPC's vertical texture offset. Example:
<samp>changeYSourceRectOffset Abigail 96</samp> will offset her sprite
sheet, showing her looking left instead of down. This persists for the
rest of the event. This is only used in Emily's <em>Clothing
Therapy</em> event to display the various outfits properly.</p></td>
</tr>
<tr>
<td><p><samp>characterSelect</samp></p></td>
<td><p>Seemingly unused. Sets Game1.gameMode to 5 and Game1.menuChoice =
0.</p></td>
</tr>
<tr>
<td><p><samp>cutscene &lt;cutscene&gt;</samp></p></td>
<td><p>Activate a cutscene. See <a href="Modding_Event_data#Cutscenes"
class="wikilink" title="cutscene list">cutscene list</a>.</p></td>
</tr>
<tr>
<td><p><samp>doAction &lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p>Acts as if the player had clicked the specified x/y coordinate
and triggers any relevant action. It is commonly used to open doors from
inside events, but it can be used for other purposes. If you use it on
an NPC you will talk to them, and if the player is holding an item they
will give that item as a gift. <samp>doAction</samp> activates objects
in the main game world (their actual location outside of the event), so
activating NPCs like this is very tricky, and their reaction varies
depending on what the player is holding.</p></td>
</tr>
<tr>
<td><p><samp>dump &lt;group&gt;</samp></p></td>
<td><p>Starts the special "cold shoulder" and "second chance" dialogue
events for the given group (women if group is <samp>girls</samp> and men
if it is anything else.) The cold shoulder event has an id of
<samp>dumped_Girls</samp> or <samp>dumped_Guys</samp> and lasts 7 days;
the second chance event has an id of <samp>secondChance_Girls</samp> or
<samp>secondChance_Guys</samp> and lasts 14 days. During open beta
testing of version 1.3 there was a second parameter which determined the
amount of hearts lost, but support for that parameter was removed before
release.</p></td>
</tr>
<tr>
<td><p><samp>elliotbooktalk</samp></p></td>
<td><p>Elliot book talk.</p></td>
</tr>
<tr>
<td><p><samp>emote &lt;actor&gt; &lt;emote ID&gt;
[continue]</samp></p></td>
<td><p>Make the given NPC name perform an emote, which is a little icon
shown above the NPC's head. If <samp>continue</samp> is specified, the
next command will play out immediately. Emotes are stored in
<samp>Content\TileSheets\emotes.xnb</samp>; see <a href="#Emotes"
class="wikilink" title="list of emotes">list of emotes</a>.</p></td>
</tr>
<tr>
<td><p><samp>end</samp></p></td>
<td><p>Ends the current event by fading out, then resumes the game world
and places the player on the square where they entered the zone. All
<samp>end</samp> parameters do this by default <em>unless otherwise
stated</em>.</p></td>
</tr>
<tr>
<td><p><samp>end bed</samp></p></td>
<td><p>Same as <samp>end</samp>, but warps the player to the x/y
coordinate of their most recent bed. This does not warp them to the
farmhouse, only to the x/y coordinate of the bed regardless of
map.</p></td>
</tr>
<tr>
<td><p><samp>end beginGame</samp></p></td>
<td><p><em>Used only during the introduction sequence in the bus stop
event.</em> It sets the game mode to <samp>playingGameMode</samp>, warps
the player to the farmhouse (9, 9), ends the current event, and starts a
new day.</p></td>
</tr>
<tr>
<td><p><samp>end credits</samp></p></td>
<td><p><em>Not used in any normal events.</em> Clears debris weather,
changes the music to wedding music, sets game mode to
<samp>creditsMode</samp> and ends the current event.</p></td>
</tr>
<tr>
<td><p><samp>end dialogue &lt;NPC&gt; &lt;"Text for next
chat"&gt;</samp></p></td>
<td><p>Same as <samp>end</samp>, and additionally clears the existing
NPC dialogue for the day and replaces it with the line(s) specified at
the end of the command. Example usage: <em>end dialogue Abigail "It was
fun talking to you today.$h"</em></p></td>
</tr>
<tr>
<td><p><samp>end dialogueWarpOut &lt;NPC&gt; &lt;"Text for next
chat"&gt;</samp></p></td>
<td><p>See <samp>end dialogue</samp> and <samp>end
warpOut</samp>.</p></td>
</tr>
<tr>
<td><p><samp>end invisible &lt;NPC&gt;</samp></p></td>
<td><p>Same as <samp>end</samp>, and additionally turns the specified
NPC invisible (cannot be interacted with until the next day).</p></td>
</tr>
<tr>
<td><p><samp>end invisibleWarpOut &lt;NPC&gt;</samp></p></td>
<td><p>See <samp>end invisible</samp> and <samp>end
warpOut</samp>.</p></td>
</tr>
<tr>
<td><p><samp>end newDay</samp></p></td>
<td><p>Ends both the event and the day (warping player to their bed,
saving the game, selling everything in the shipping box, etc).</p></td>
</tr>
<tr>
<td><p><samp>end position &lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p>Same as <samp>end</samp>, and additionally warps the player to
the map coordinates specified in <em>x y</em>.</p></td>
</tr>
<tr>
<td><p><samp>end warpOut</samp></p></td>
<td><p>Same as <samp>end</samp>, and additionally finds the first warp
out of the current location (second warp if male and in the bathhouse),
and warps the player to its endpoint.</p></td>
</tr>
<tr>
<td><p><samp>end wedding</samp></p></td>
<td><p><em>Used only in the hardcoded wedding event.</em> Changes the
character's clothes back to normal, sets Lewis' post-event chat to
<em>"That was a beautiful ceremony. Congratulations!$h"</em>, and warps
the player to their farm.</p></td>
</tr>
<tr>
<td><p><samp>endSimultaneousCommand</samp></p></td>
<td><p>Ends a simultaneous command block started by
<samp>beginSimultaneousCommand</samp>.</p></td>
</tr>
<tr>
<td><p><samp>eventSeen &lt;event ID&gt; [seen]</samp></p></td>
<td><p>Add or remove an event ID from the player's list of seen events,
based on [seen] (default <samp>true</samp> to add).</p>
<p>Can be used to prevent a mutually exclusive event from being seen by
setting it to <samp>true</samp>.</p>
<p>An event can mark <em>itself</em> unseen using <samp>eventSeen
&lt;event ID&gt; false</samp>. This takes effect immediately (i.e. the
event won't be added to the list when it completes), but the game will
prevent the event from playing again until the player changes location
to avoid event loops. The event will still replay when re-entering the
location, making it useful for creating repeatable events.</p></td>
</tr>
<tr>
<td><p><samp>extendSourceRect &lt;actor&gt; reset</samp></p></td>
<td><p>Resets the actors sprite.</p></td>
</tr>
<tr>
<td><p><samp>extendSourceRect &lt;actor&gt; &lt;horizontal&gt;
&lt;vertical&gt; [ignoreUpdates]</samp></p></td>
<td><p>TODO: Explain Character.extendSourceRect</p></td>
</tr>
<tr>
<td><p><samp>eyes &lt;eyes&gt; &lt;blink&gt;</samp></p></td>
<td><p>Change the player's eyes. Eyes is represented by and Integer from
0 - 5 (open, closed, right, left, half closed, wide open). Blink is a
timer that is represented with a negative number. -1000 is the default
timer.</p></td>
</tr>
<tr>
<td><p><samp>faceDirection &lt;actor&gt; &lt;direction&gt;
[continue]</samp></p></td>
<td><p>Make a named NPC face a <a href="#Directions" class="wikilink"
title="direction">direction</a>. If [continue] is false (default) the
game will pause while the NPC changes their direction.</p></td>
</tr>
<tr>
<td><p><samp>fade [unfade]</samp></p></td>
<td><p>Fades out to black if no parameter is supplied. If the parameter
is <samp>unfade</samp> (not <samp>true</samp>), fades in from
black.</p></td>
</tr>
<tr>
<td><p><samp>farmerAnimation &lt;anim&gt;</samp></p></td>
<td><p>Briefly sets the farmer's sprite to &lt;anim&gt; for a variable
(depending on sprite) interval. Only used once in vanilla events. Using
<samp>showFrame farmer &lt;sprite&gt;</samp> twice (to set a new frame
and back) is more powerful as it lets you control the interval using
<samp>pause n</samp>.</p></td>
</tr>
<tr>
<td><p><samp>farmerEat &lt;object ID&gt;</samp></p></td>
<td><p>Make the player eat an object. (The farmer actually does eat the
object, so buffs will apply, healing will occur, etc.). If the object's
<samp>IsDrink</samp> value in <samp>Data/Objects</samp> is set to true,
the drinking animation will play instead of the eating one.</p></td>
</tr>
<tr>
<td><p><samp>fork [req] &lt;event ID&gt;</samp></p></td>
<td><p>End the current command script and starts a different script with
the given ID, but only if the [req] condition is met. (Example:
<samp>/fork choseWizard finalBossWizard</samp> in the
<em>"Necromancer"</em> script of Sebastian's 6-heart event.) The [req]
condition can be a mail ID or dialogue answer ID; if not specified, it
checks if the <samp>specialEventVariable1</samp> variable was set
(<em>e.g.,</em> by a <samp>question</samp> event command or
<samp>%fork</samp> dialogue command). The new script should have the
same format as a normal event script, but without the mandatory three
start fields.</p></td>
</tr>
<tr>
<td><p><samp>friendship &lt;npc&gt; &lt;amount&gt;</samp></p></td>
<td><p>Add the given number of friendship points with the named NPC.
(There are 250 points per heart.)</p></td>
</tr>
<tr>
<td><p><samp>globalFade [speed] [continue]</samp></p></td>
<td><p>Fade to black at a particular speed (default 0.007). If
[continue] is false (default) the event pauses during the fade,
otherwise the event continues as the screen fades to black. The fade
effect disappears when this command is done; to avoid that, use the
<samp>viewport</samp> command to move the camera off-screen.</p></td>
</tr>
<tr>
<td><p><samp>globalFadeToClear [speed] [continue]</samp></p></td>
<td><p>Fade in from black at a particular speed (default 0.007). If
[continue] is false (default) the event pauses during the fade,
otherwise the event continues as the screen fades in. If the screen is
not already black when this command starts it will abruptly set it to
black before fading back in.</p></td>
</tr>
<tr>
<td><p><samp>glow &lt;r&gt; &lt;g&gt; &lt;b&gt;
&lt;hold&gt;</samp></p></td>
<td><p>Make the screen glow once, fading into and out of the &lt;r&gt;
&lt;g&gt; <b> values over the course of a second. If &lt;hold&gt; is
<samp>true</samp> it will fade to and hold that color until
<samp>stopGlowing</samp> is used.</p></td>
</tr>
<tr>
<td><p><samp>grandpaCandles</samp></p></td>
<td><p>Do grandpa candles</p></td>
</tr>
<tr>
<td><p><samp>grandpaEvaluation</samp></p></td>
<td><p>Do grandpa evaluation</p></td>
</tr>
<tr>
<td><p><samp>grandpaEvaluation2</samp></p></td>
<td><p>Do grandpa evaluation (manually resummoned)</p></td>
</tr>
<tr>
<td><p><samp>halt</samp></p></td>
<td><p>Make everyone stop.</p></td>
</tr>
<tr>
<td><p><samp>hideShadow &lt;actor&gt; &lt;true/false&gt;</samp></p></td>
<td><p>Hide the shadow of the named actor. False unhides it.</p>
<ul>
<li>Note: This command will not work on the farmer.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>hospitaldeath</samp></p></td>
<td><p>Forces you to lose money and items, pulls up the dialogue box
with Harvey. IS NOT THE SAME AS ANY OF THE END COMMANDS.</p></td>
</tr>
<tr>
<td><p><samp>ignoreCollisions &lt;character ID&gt;</samp></p></td>
<td><p>Make a character ignore collisions when moving for the remainder
of the event. For example, they'll walk through walls if needed to reach
their destination. The character ID can be <samp>farmer</samp> or an NPC
name like <samp>Abigail</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ignoreEventTileOffset</samp></p></td>
<td><p>Tile positions in farm events are offset to match the farmhouse
position. If an event shouldn't be based on the farmhouse position, add
an ignoreEventTileOffset command to disable the offset for that event.
This must be the 4th command (after the 3 initial setup ones) to take
effect.</p></td>
</tr>
<tr>
<td><p><samp>ignoreMovementAnimation &lt;actor&gt;
[ignore]</samp></p></td>
<td><p>Causes the specified NPC to move without their walk animations,
based on the boolean argument [ignore] (default <samp>true</samp> to
ignore animation, set to <samp>false</samp> to enable walk animation
again).</p></td>
</tr>
<tr>
<td><p><samp>itemAboveHead  [show message]</samp></p></td>
<td><p>Show an item above the player's head and displays a message about
it. The [type] can be "pan", "hero", "sculpture", "joja", "slimeEgg",
"rod", "sword", or "ore". [item id] can be any qualified item id. If no
item is specified, then they will hold the furnace blueprint and no
message will be displayed. <samp>item id</samp> can be any qualified
item id. This command does not add the item to the player's inventory
(except when used with "slimeEgg"). If [show message] (true by default)
is true, then the 'you received' message will be shown.</p>
<p>The message box from <samp>itemAboveHead</samp> will cancel dialogue
from commands that come after it unless at least 1,200ms has passed, so
it is recommended to use a <samp>pause</samp> command after
<samp>itemAboveHead</samp>.</p></td>
</tr>
<tr>
<td><p><samp>jump &lt;actor&gt; [intensity]</samp></p></td>
<td><p>Make a the named NPC jump. The default <samp>intensity</samp> is
8.</p></td>
</tr>
<tr>
<td><p><samp>loadActors &lt;layer&gt;</samp></p></td>
<td><p>Load the actors from a layer in the map file.</p></td>
</tr>
<tr>
<td><p><samp>makeInvisible &lt;x&gt; &lt;y&gt; [x-dimension]
[y-dimension]</samp></p></td>
<td><p>Temporarily hides selected objects or terrain features: the
tile(s) will become passable for the duration of the event. Useful for
clearing a walking area during events, especially in the FarmHouse.
(Example: <samp>/makeInvisible 8 14</samp> hides any object or terrain
feature at tile 8, 14 in the current map.) The optional [x-dimension]
and [y-dimension] arguments allow you to specify a larger area to be
cleared. (Example: <samp>/makeInvisible 68 36 13 7</samp> in Leah's
14-heart event clears a 13 × 7 tile rectangular area with the top-left
corner at coordinate 68, 36.). Known bugs: some furniture may not
re-appear immediately?</p></td>
</tr>
<tr>
<td><p><samp>mail &lt;letter ID&gt;</samp></p></td>
<td><p>Queue a letter to be received tomorrow (see
<samp>Content\Data\mail.xnb</samp> for available mail).</p></td>
</tr>
<tr>
<td><p><samp>mailReceived &lt;letter ID&gt; [add]</samp></p></td>
<td><p>Add or remove a letter to the player's received list (bypassing
the mailbox), based on [add] (default <samp>true</samp> to add). Useful
for setting mail flags.</p>
<p>Its old name is <samp>addMailReceived</samp> which can still be used
as an alias.</p></td>
</tr>
<tr>
<td><p><samp>mailToday &lt;letter ID&gt;</samp></p></td>
<td><p>Adds a letter to the mailbox immediately, given the &lt;letter
ID&gt; in <samp>Data/Mail</samp>.</p></td>
</tr>
<tr>
<td><p><samp>message "&lt;text&gt;"</samp></p></td>
<td><p>Show a dialogue box (no speaker). See <a href="#Dialogue_format"
class="wikilink" title="dialogue format">dialogue format</a> for the
&lt;text&gt; format.</p></td>
</tr>
<tr>
<td><p><samp>minedeath</samp></p></td>
<td><p>Forces you to lose money and items, pulls up the dialogue box
with Harvey. IS NOT THE SAME AS ANY OF THE END COMMANDS.</p></td>
</tr>
<tr>
<td><p><samp>money &lt;amount&gt;</samp></p></td>
<td><p>Adds/removes the specified amount of money.</p></td>
</tr>
<tr>
<td><p><samp>move &lt;actor&gt; &lt;x&gt; &lt;y&gt; &lt;direction&gt;
[continue]</samp></p></td>
<td><p>Make a named NPC move by the given tile offset from their current
position (along one axis <em>only</em>), and face the given <a
href="#Directions" class="wikilink" title="direction">direction</a> when
they're done. To move along multiple axes, you must specify multiple
<samp>move</samp> commands. By default the event pauses while a move
command is occurring, but if [continue] (default <samp>false</samp>) is
set to <em>true</em> the movement is asynchronous and will run
simultaneously with other event commands. You can also move multiple
people at a time in a single event command with move - an example of
<samp>/move Abigail 1 0 1 Sam 0 1 1 Sebastian 2 0 1/</samp> will have
Abigail, Sam, and Sebastian all move at the same time in their
respective directions.</p></td>
</tr>
<tr>
<td><p><samp>pause &lt;duration&gt;</samp></p></td>
<td><p>Pause the game for the given number of milliseconds.</p></td>
</tr>
<tr>
<td><p><samp>playMusic &lt;track&gt;</samp></p></td>
<td><p>Play the specified <a href="Modding_Audio#Track_list"
class="wikilink" title="music track ID">music track ID</a>. If the track
is 'samBand', the track played will change depend on certain dialogue
answers (76-79).</p></td>
</tr>
<tr>
<td><p><samp>playSound &lt;sound&gt;</samp></p></td>
<td><p>Play a given <a href="Modding_Audio#Track_list" class="wikilink"
title="sound ID">sound ID</a> from the game's sound bank.</p></td>
</tr>
<tr>
<td><p><samp>playerControl</samp></p></td>
<td><p>Give the player control back.</p></td>
</tr>
<tr>
<td><p><samp>positionOffset &lt;actor&gt; &lt;x&gt; &lt;y&gt;
[continue]</samp></p></td>
<td><p>Offset the position of the named NPC by the given number of
pixels. This happens instantly, with no walking animation. If [continue]
is false (default) the event will pause while the NPC's position is
being offset.</p></td>
</tr>
<tr>
<td><p><samp>proceedPosition &lt;actor&gt;</samp></p></td>
<td><p>Waits for the specified actor to stop moving before executing the
next command.</p></td>
</tr>
<tr>
<td><p><samp>question null
"&lt;question&gt;#&lt;answer1&gt;#&lt;answer2&gt;"</samp></p></td>
<td><p>Show a dialogue box with some answers and an optional question.
When the player chooses an answer, the event script continues with no
other effect.</p></td>
</tr>
<tr>
<td><p><samp>question fork&lt;answer index&gt;
"&lt;question&gt;#&lt;answer 0&gt;#&lt;answer 1&gt;#..."</samp></p></td>
<td><p>Show a dialogue with some answers and an optional question. When
the player chooses the answer matching the <samp>fork&lt;answer
index&gt;</samp> (like <samp>fork0</samp> for the first answer), the
<samp>specialEventVariable1</samp> variable is set. Usually followed by
a <samp>fork</samp> command. Example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="er">.../question</span> <span class="er">fork0</span> <span class="er">\</span><span class="st">&quot;#answer0#answer1#answer3</span><span class="ch">\&quot;</span><span class="st">/fork eventidhere/...&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>questionAnswered &lt;answer ID&gt;
[answered]</samp></p></td>
<td><p>Add or remove an answer ID from the player's list of chosen
dialogue answers, based on [answered] (default <samp>true</samp> to
add).</p></td>
</tr>
<tr>
<td><p><samp>quickQuestion
&lt;question&gt;#&lt;answer1&gt;#&lt;answer2&gt;#&lt;answer3&gt;(break)&lt;answer1
script&gt;(break)&lt;answer2 script&gt;(break)&lt;answer3
script&gt;</samp></p></td>
<td><p>Show a dialogue box with an optional question and some answers.
The answer scripts are sequences of commands separated by
<samp>\\</samp>. When the player chooses an answer, the relevant answer
script is executed and then the event continues. Usually used when an
NPC's response will depend on the answer chosen but nothing else in the
event has to depend on it.</p>
<ul>
<li>Note: If quickQuestion is used immediately at the start of an event
block (Example: "ExampleEvent": "quickQuestion [rest of the event]"), it
will cause a dialogue loop. Adding another command in front of
quickQuestion resolves this issue (Example: "ExampleEvent": "pause
1/quickQuestion [rest of the event]").</li>
</ul></td>
</tr>
<tr>
<td><p><samp>removeItem &lt;object ID&gt; [count]</samp></p></td>
<td><p>Remove one instance of an item from a player's inventory. Use
[count] to specify the number to be removed.</p></td>
</tr>
<tr>
<td><p><samp>removeObject &lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p>Remove the prop at a position.</p></td>
</tr>
<tr>
<td><p><samp>removeQuest &lt;quest ID&gt;</samp></p></td>
<td><p>Remove the specified quest from the quest log.</p></td>
</tr>
<tr>
<td><p><samp>removeSpecialOrder &lt;order ID&gt;</samp></p></td>
<td><p>Remove a special order from the player team. This affects all
players, since special orders are shared.</p></td>
</tr>
<tr>
<td><p><samp>removeSprite &lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p>Remove the temporary sprite at a position.</p></td>
</tr>
<tr>
<td><p><samp>removeTemporarySprites</samp></p></td>
<td><p>Remove all temporary sprites.</p></td>
</tr>
<tr>
<td><p><samp>removeTile &lt;x&gt; &lt;y&gt;
&lt;layer&gt;</samp></p></td>
<td><p>Remove a tile from the specified layer.</p></td>
</tr>
<tr>
<td><p><samp>replaceWithClone &lt;NPC name&gt;</samp></p></td>
<td><p>Replace an NPC already in the event with a temporary copy. This
allows changing the NPC for the event without affecting the real
NPC.</p>
<p>For example, this event changes Marnie's name/portrait only within
the event:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Some.ModId_ExampleEvent/&quot;</span><span class="er">:</span> <span class="st">&quot;continue/64 15/farmer 64 15 2 Marnie 64 17 0/replaceWithClone Marnie/changeName Marnie Pufferchick/changePortrait Marnie Pufferchick/[...]/end&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>resetVariable</samp></p></td>
<td><p>Set the <samp>specialEventVariable1</samp> to false.</p></td>
</tr>
<tr>
<td><p><samp>rustyKey</samp></p></td>
<td><p>Adds the <samp>HasRustyKey</samp> mail flag to the host player,
allowing all players to enter the Sewer from the Forest outlet pipe or
an <samp>EnterSewer</samp> tile action.</p></td>
</tr>
<tr>
<td><p><samp>screenFlash &lt;alpha&gt;</samp></p></td>
<td><p>Flashes the screen white for an instant. An alpha value from
<samp>0</samp> to <samp>1</samp> adjusts the brightness, and values from
<samp>1</samp> and out flashes pure white for <samp>x</samp>
seconds.</p></td>
</tr>
<tr>
<td><p><samp>setRunning</samp></p></td>
<td><p>Set the player as running.</p></td>
</tr>
<tr>
<td><p><samp>setSkipActions [actions]</samp></p></td>
<td><p>Set <a href="Modding_Trigger_actions" class="wikilink"
title="trigger actions">trigger actions</a> that should run if the
player skips the event. You can list multiple actions delimited with
<samp>#</samp>, or omit [actions] so no actions are run. When the player
skips, the last <samp>setSkipActions</samp> before that point is
applied.</p>
<p>For example, this adds the <a href="Garden_Pot" class="wikilink"
title="garden pot">garden pot</a> recipe and item to the player if the
event is skipped, but avoids adding the item if the event already did
it:</p>
<pre><code>/setSkipActions AddCraftingRecipe Current &quot;Garden Pot&quot;#AddItem (BC)62
/skippable
/...
/addItem (BC)62
/setSkipActions AddCraftingRecipe Current &quot;Garden Pot&quot;</code></pre>
<p>Skip actions aren't applied if the event completes normally without
being skipped.</p></td>
</tr>
<tr>
<td><p><samp>shake &lt;actor&gt; &lt;duration&gt;</samp></p></td>
<td><p>Shake the given NPC actor for the given duration in
milliseconds.</p>
<p>Has no effect on <samp>farmer</samp> actors. See
<samp>startJittering</samp> instead.</p></td>
</tr>
<tr>
<td><p><samp>showFrame &lt;actor&gt; &lt;frame&gt; [flip]</samp><br />
<samp>showFrame &lt;frame&gt;</samp></p></td>
<td><p>Set the sprite index of the given actor by name, or the
<samp>farmer</samp> actor if none was provided.</p>
<p>&lt;actor&gt; is given as an actor's name, including
<samp>spouse</samp> and <samp>farmer</samp> actors.<br />
[flip] is given as <samp>true</samp> or <samp>false</samp>, and cannot
be used if &lt;actor&gt; was omitted. Only affects <samp>farmer</samp>
actors.</p>
<p>Note that setting the farmer's sprite only changes <em>parts</em> of
the sprite (some times arms, some times arms and legs and torso but not
the head, etc). To rotate the whole sprite, use <em>faceDirection farmer
&lt;0/1/2/3&gt;</em> first before modifying the sprite with
<em>showFrame</em>.</p></td>
</tr>
<tr>
<td><p><samp>skippable</samp></p></td>
<td><p>Allow skipping this event.</p></td>
</tr>
<tr>
<td><p><samp>speak &lt;character&gt; "&lt;text&gt;"</samp></p></td>
<td><p>Show dialogue text from the named NPC; (see <a
href="#Dialogue_format" class="wikilink"
title="dialogue format">dialogue format</a>) with <a
href="Modding_Dialogue#Dialogue_commands" class="wikilink"
title="dialogue commands">dialogue commands</a> parsed and applied just
like in standard dialogue. The quotation marks need to be escaped, or
preceded with backslashes (<samp>\</samp>) when events are written in
JSON as with . For example
<code>speak Leah \" My dialogue has been escaped! \"</code>.</p></td>
</tr>
<tr>
<td><p><samp>specificTemporarySprite &lt;sprite&gt; [other
params]</samp></p></td>
<td><p>Shows the given temporary sprite. Parameters change depending on
the sprite. <strong>These are quite hardcoded and probably not easily
reusable, other than the little heart.</strong></p></td>
</tr>
<tr>
<td><p><samp>speed farmer &lt;modifier&gt;</samp></p></td>
<td><p>Add a speed modifier to the farmer. Is persistent and you will
have to use the command again to return to normal speed.</p></td>
</tr>
<tr>
<td><p><samp>speed &lt;actor&gt; &lt;speed&gt;</samp></p></td>
<td><p>Sets the named NPC's speed (default speed is 3). Not applicable
to the farmer. Applies only through the end of the next movement or
animation on that NPC.</p></td>
</tr>
<tr>
<td><p><samp>splitSpeak &lt;actor&gt; "&lt;text&gt;"</samp></p></td>
<td><p>Dialogue, but chosen based on previous answer. ('~' is the
separator used.)</p></td>
</tr>
<tr>
<td><p><samp>startJittering</samp></p></td>
<td><p>Make the player start jittering.</p></td>
</tr>
<tr>
<td><p><samp>stopAdvancedMoves</samp></p></td>
<td><p>Stop movement from advancedMove.</p></td>
</tr>
<tr>
<td><p><samp>stopAnimation farmer</samp></p></td>
<td><p>Stop the farmer's current animation.</p></td>
</tr>
<tr>
<td><p><samp>stopAnimation &lt;actor&gt; [end frame]</samp></p></td>
<td><p>Stop the named NPC's current animation. Not applicable to the
farmer.</p></td>
</tr>
<tr>
<td><p><samp>stopGlowing</samp></p></td>
<td><p>Make the screen stop glowing.</p></td>
</tr>
<tr>
<td><p><samp>stopJittering</samp></p></td>
<td><p>Make the player stop jittering.</p></td>
</tr>
<tr>
<td><p><samp>stopMusic</samp></p></td>
<td><p>Stop any currently playing music.</p></td>
</tr>
<tr>
<td><p><samp>stopRunning</samp></p></td>
<td><p>Make the farmer stop running.</p></td>
</tr>
<tr>
<td><p><samp>stopSound &lt;sound ID&gt; [immediate]</samp></p></td>
<td><p>Stop a sound started with the <samp>startSound</samp> command.
This has no effect if the sound has already stopped playing on its own
(or hasn't been started). If you started multiple sounds with the same
ID, this will stop all of them (e.g.
<code>startSound fuse/startSound fuse/stopSound fuse</code>).</p>
<p>By default the sound will stop immediately. For looping sounds, you
can pass <samp>false</samp> to the [immediate] argument to stop the
sound when it finishes playing the current iteration instead (e.g.
<code>stopSound fuse false</code>).</p></td>
</tr>
<tr>
<td><p><samp>stopSwimming &lt;actor&gt;</samp></p></td>
<td><p>Make an actor stop swimming.</p></td>
</tr>
<tr>
<td><p><samp>swimming &lt;actor&gt;</samp></p></td>
<td><p>Make an actor start swimming.</p></td>
</tr>
<tr>
<td><p><samp>switchEvent &lt;event ID&gt;</samp></p></td>
<td><p>Changes the current event (ie. event commands) to another event
in the same location. The event switched to should not have the initial
3 commands (music, viewpoint coordinates, character locations) and
should instead be treated as a continuation of the first event.</p></td>
</tr>
<tr>
<td><p><samp>temporarySprite &lt;x&gt; &lt;y&gt; &lt;row in texture&gt;
&lt;animation length&gt; &lt;animation interval&gt; &lt;flipped&gt;
&lt;layer depth&gt;</samp></p></td>
<td><p>Create a temporary sprite with the given parameters, from the
resource <samp>TileSheets/animations</samp>.</p></td>
</tr>
<tr>
<td><p><samp>temporaryAnimatedSprite …</samp></p></td>
<td><p>Add a temporary animated sprite to the event.</p>
<p>This has 17 required fields (space-delimited):</p>
<table>
<thead>
<tr>
<th><p>index</p></th>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0</p></td>
<td><p><samp>texture</samp></p></td>
<td><p>The asset name for texture to draw.</p></td>
</tr>
<tr>
<td><p>1–4</p></td>
<td><p><samp>rectangle</samp></p></td>
<td><p>The pixel area within the <samp>texture</samp> to draw, in the
form <samp>&lt;x&gt; &lt;y&gt; &lt;width&gt;
&lt;height&gt;</samp>.</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p><samp>interval</samp></p></td>
<td><p>The millisecond duration for each frame in the
animation.</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p><samp>frames</samp></p></td>
<td><p>The number of frames in the animation.</p></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p><samp>loops</samp></p></td>
<td><p>The number of times to repeat the animation.</p></td>
</tr>
<tr>
<td><p>8–9</p></td>
<td><p><samp>tile</samp></p></td>
<td><p>The tile position at which to draw the sprite, in the form
<samp>&lt;x&gt; &lt;y&gt;</samp>.</p></td>
</tr>
<tr>
<td><p>10</p></td>
<td><p><samp>flicker</samp></p></td>
<td><p>Causes the sprite to flicker in and out of view repeatedly. (one
of <samp>true</samp> or <samp>false</samp>).</p></td>
</tr>
<tr>
<td><p>11</p></td>
<td><p><samp>flip</samp></p></td>
<td><p>Whether to flip the sprite horizontally when it's drawn (one of
<samp>true</samp> or <samp>false</samp>).</p></td>
</tr>
<tr>
<td><p>12</p></td>
<td><p><samp>sort tile Y</samp></p></td>
<td><p>The tile Y position to use in the layer depth calculation, which
affects which sprite is drawn on top if two sprites overlap. The larger
the number, the higher layer the sprite is on.</p></td>
</tr>
<tr>
<td><p>13</p></td>
<td><p><samp>alpha fade</samp></p></td>
<td><p>Fades out the sprite based on alpha set. The larger the number,
the faster the fade out. 1 is instant.</p></td>
</tr>
<tr>
<td><p>14</p></td>
<td><p><samp>scale</samp></p></td>
<td><p>A multiplier applied to the sprite size (in addition to the
normal 4× pixel zoom).</p></td>
</tr>
<tr>
<td><p>15</p></td>
<td><p><samp>scale change</samp></p></td>
<td><p>Changes the scale based on the multiplier applied on top of the
normal zoom. Continues endlessly.</p></td>
</tr>
<tr>
<td><p>16</p></td>
<td><p><samp>rotation</samp></p></td>
<td><p>The rotation to apply to the sprite, measured in <a
href="wikipedia_radians" class="wikilink"
title="radians">radians</a>.</p></td>
</tr>
<tr>
<td><p>17</p></td>
<td><p><samp>rotation change</samp></p></td>
<td><p>Continuously rotates the sprite, causing it to spin. The speed is
determined by input value.</p></td>
</tr>
</tbody>
</table>
<p>After the required fields, you can set any number of 'flag' options
(space-delimited). Each option consists of the flag name followed by any
arguments it needs. For example, <code>color Red hold_last_frame</code>
sets two flags (<samp>color</samp> and
<samp>hold_last_frame</samp>)..</p>
<p>The available flag options are:</p>
<table>
<thead>
<tr>
<th><p>flag</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>color &lt;color&gt;</samp></p></td>
<td><p>Apply a <a href="Modding_Common_data_field_types#Color"
class="wikilink" title="standard color">standard color</a> to the
sprite.</p></td>
</tr>
<tr>
<td><p><samp>hold_last_frame</samp></p></td>
<td><p>After playing the animation once, freeze the last frame as long
as the sprite is shown.</p></td>
</tr>
<tr>
<td><p><samp>ping_pong</samp></p></td>
<td><p>Causes the animation frames to play forwards and backwards
alternatingly. Example: An animation with the frames 0, 1, 2 will play
"0 1 2 0 1 2" without the ping_pong flag and play "0 1 2 1 0" with the
ping_pong flag.</p></td>
</tr>
<tr>
<td><p><samp>motion &lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p>Sprite moves based on the values set. Numbers can be decimals or
negative.</p></td>
</tr>
<tr>
<td><p><samp>acceleration &lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p><strong>[TODO: document what this does]</strong></p></td>
</tr>
<tr>
<td><p><samp>acceleration_change &lt;x&gt; &lt;y&gt;</samp></p></td>
<td><p><strong>[TODO: document what this does]</strong></p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>textAboveHead &lt;actor&gt;
\"&lt;text&gt;\"</samp></p></td>
<td><p>Show a small text bubble over the named NPC's head with the given
text; see <a href="#Dialogue_format" class="wikilink"
title="dialogue format">dialogue format</a>. Note: <samp>@</samp> does
not get replaced with the farmer's name the way it does in dialogue or
with the <samp>speak</samp> command. Instead, use the token
<samp>&lt;nowiki&gt;&lt;/nowiki&gt;</samp>.</p></td>
</tr>
<tr>
<td><p><samp>tossConcession &lt;actor&gt;
&lt;concessionId&gt;</samp></p></td>
<td><p>Causes an NPC to throw their concession in the air.
<samp>concessionId</samp> is from Data/Concessions.</p></td>
</tr>
<tr>
<td><p><samp>translateName &lt;actor&gt; &lt;translation
key&gt;</samp></p></td>
<td><p>Set the display name for an NPC in the event to match the given
translation key.</p></td>
</tr>
<tr>
<td><p><samp>tutorialMenu</samp></p></td>
<td><p>Show the tutorial menu if no other menu is open.</p></td>
</tr>
<tr>
<td><p><samp>updateMinigame &lt;event data&gt;</samp></p></td>
<td><p>Send an event to the current minigame.</p></td>
</tr>
<tr>
<td><p><samp>viewport move &lt;x&gt; &lt;y&gt;
&lt;duration&gt;</samp></p></td>
<td><p>Pan the the camera in the direction (and with the velocity)
defined by <em>x/y</em> for the given duration in milliseconds. Example:
<em>"viewport move 2 -1 5000"</em> moves the camera 2 pixels right and 1
pixel up for 5 seconds. The total distance moved is based on framerate,
rather than time, and may be inconsistent.</p></td>
</tr>
<tr>
<td><p><samp>viewport &lt;actor&gt; [clamp] [fade]</samp><br />
<samp>viewport &lt;actor&gt; [fade]</samp><br />
<samp>viewport &lt;x&gt; &lt;y&gt; [clamp] [fade]
[unfreeze]</samp><br />
<samp>viewport &lt;x&gt; &lt;y&gt; [fade] [unfreeze]</samp></p></td>
<td><p>Set the camera to center on the given target, given as an actor
by name, or as integer tile coordinates.</p>
<p>Can be formatted using one of several different groups of
arguments.</p>
<p>&lt;actor&gt; centers the camera on an actor. Given as the actor's
name or <samp>player</samp>.<br />
[clamp] adjusts the camera position ensure it remains within the map
bounds.<br />
[fade] adds a quick fade-in from black after repositioning the camera.
Given as <samp>true</samp> or <samp>false</samp>.<br />
[unfreeze] applies the default game camera behaviour, following the
player throughout the event. Any values given for the &lt;x&gt;
&lt;y&gt; &lt;actor&gt; [clamp] arguments will be ignored, and the
<samp>viewport move</samp> command will have no effect while set. This
effect can be removed by using the <samp>viewport</samp> command again
without the [unfreeze] argument.</p></td>
</tr>
<tr>
<td><p><samp>waitForAllStationary</samp></p></td>
<td><p>Waits for all actors to stop moving before executing the next
command.</p></td>
</tr>
<tr>
<td><p><samp>waitForOtherPlayers</samp></p></td>
<td><p>Wait for other players (vanilla MP).</p></td>
</tr>
<tr>
<td><p><samp>warp &lt;actor&gt; &lt;x&gt; &lt;y&gt;
[continue]</samp></p></td>
<td><p>Warp the named NPC to a position to the given X, Y tile
coordinate. This can be used to warp characters off-screen. If
[continue] is false (default) the event will pause while the NPC is
being warped.</p></td>
</tr>
<tr>
<td><p><samp>warpFarmers [&lt;x&gt; &lt;y&gt; &lt;direction&gt;]+
&lt;default offset&gt; &lt;default x&gt; &lt;default y&gt;
&lt;direction&gt;</samp></p></td>
<td><p>Warps connected players to the given <a
href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
title="tile coordinates">tile coordinates</a> and <a
href="Modding_Event_data#Directions" class="wikilink"
title="numeric directions">numeric directions</a>. The &lt;x&gt;
&lt;y&gt; &lt;direction&gt; triplet is repeated for each connected
player (e.g. the first triplet is for the main player, second triplet is
for the first farmhand, etc). The triplets are followed by an offset
direction (one of <samp>up</samp>, <samp>down</samp>, <samp>left</samp>,
or <samp>right</samp>), and a final triplet which defines the default
values used by any other player.</p></td>
</tr>
</tbody>
</table>

Some commands are broken or unusable:

| command | description |
|----|----|
| `end busIntro` | Supposed to start the bus intro scene, presumably the one that was cut before release. |

### Comments

A command which begins with `--` is ignored. This can be used to insert
comments or to disable commands temporarily while debugging an event.
The comment ends at the next slash delimiter (`/`), so it can't contain
slashes. Comments cannot be added between the first three commands
(music, viewport coordinates, character setup). This means you can't add
a comment after the music or viewport coordinates commands, but you can
add a comment after character setup.

For example:

``` js
"666/": "none/-1000 -1000/farmer 5 7 0/--you can add comments from here/skippable/viewport 5 7 10/--set viewport near door/pause 2000/end"
```

### Multilining

Event commands trim surrounding whitespace, so they can be multilined
for readability. Line breaks must be before or after the `/` delimiter.
For example:

``` json
"SomeEventId/": "
    none/
    -1000 -1000/
    farmer 5 7 0/
    ...
"
```

This can be also combined with the
<a href="Modding_Event_data#Comments" class="wikilink"
title="comment syntax">comment syntax</a> to add notes. (Reminder:
comments can't be used between the first three commands). For example:

``` json
"SomeEventId/": "
    none/
    -1000 -1000/
    farmer 5 7 0/    -- actor positions/
    ...
"
```

### Optional NPCs

You can mark NPCs optional in event commands by suffixing their name
with `?`. For example, `jump Kent?` won't log an error if Kent is
missing. When used in the initial event positions, the NPC is only added
if they exist in `Data/Characters` and their `UnlockConditions` match.

### Directions

When using an event command with a `direction` argument, use one of
these numeric values or case-insensitive names:

| Numeric Value | Name  | Meaning       |
|---------------|-------|---------------|
| 0             | up    | looking up    |
| 1             | right | looking right |
| 2             | down  | looking down  |
| 3             | left  | looking left  |

### Cutscenes

The `cutscene` command will accept the following values:

| Value | In-game scene |
|----|----|
| AbigailGame | Sets up `Journey of the Prairie King` mini-game with Abigail |
| addSecretSantaItem | Feast of the Winter Star gift scene |
| balloonChangeMap | Changes to the "in the balloon" map for Harvey's 10 heart event |
| balloonDepart | Balloon taking off in Harvey's 10 heart event |
| bandFork | Plays correct scene for Sam's 8 heart event, based on response given in 2 heart event |
| boardGame | Sets up `Solarion Chronicles` mini-game |
| clearTempSprites | Removes all temporary sprites from map |
| eggHuntWinner | Egg Hunt winner scene |
| governorTaste | Luau soup scene |
| greenTea | Caroline sunroom scene from her 2 heart event |
| haleyCows | Haley meeting the cows from her 8 heart event |
| iceFishingWinner | Festival of Ice fishing contest winner scene |
| iceFishingWinnerMP | Sets up text message displayed when leaving Festival of Ice |
| linusMoneyGone | ??? (seems to be unused) |
| marucomet | Maru Comet scene from her 14 heart event |
| plane | Plane flying by from Harvey's 8 heart scene |
| robot | MarILDA taking off from Maru's 10 heart scene |

### Dialogue format

See <a href="Modding_Dialogue#Format" class="wikilink"
title="Modding:Dialogue#Format">Modding:Dialogue#Format</a>.

## Common values

### Emotes

An *emote* is an animated icon bubble shown above an NPC's head to
indicate a mood or reaction. Emote icons are stored in the
`TileSheets\emotes` asset.

| ID  | `Character` constant |
|-----|----------------------|
| 4   | `emptyCanEmote`      |
| 8   | `questionMarkEmote`  |
| 12  | `angryEmote`         |
| 16  | `exclamationEmote`   |
| 20  | `heartEmote`         |
| 24  | `sleepEmote`         |
| 28  | `sadEmote`           |
| 32  | `happyEmote`         |
| 36  | `xEmote`             |
| 40  | `pauseEmote`         |
| 44  | *unused*             |
| 48  | *unused*             |
| 52  | `videoGameEmote`     |
| 56  | `musicNoteEmote`     |
| 60  | `blushEmote`         |

## Using C#

You can add custom event preconditions & commands using new `Event`
methods.

| Method                      |
|-----------------------------|
| `RegisterPrecondition`      |
| `RegisterPreconditionAlias` |
| `RegisterCommand`           |
| `RegisterCommandAlias`      |

These are some useful fields:

| Field | Usage |
|----|----|
| `Event.fromAssetName` | Indicates which data asset (if any) the event was loaded from. |
| `Game1.eventsSeenSinceLastLocationChange` | Tracks the events that played since the player arrived in their current location. |

## See also

- [JavaScript to parse an event precondition
  string](https://gist.github.com/Pathoschild/95efc5ba5a23dc2c4da219ca2ddde679)
- [LINQ
  script](https://gist.github.com/Pathoschild/4e0af42158583983a4206d4d734bfc0b)
  to format an event for
  <a href="Modding_Modder_Guide_APIs_Translation" class="wikilink"
  title="translations (i18n)">translations (i18n)</a>
- <a href="Modding_Custom_wedding_events" class="wikilink"
  title="Modding:Custom wedding events">Modding:Custom wedding events</a>
  for specific details about custom weddings

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="pt_Modificações_Dados_de_Eventos" class="wikilink"
title="pt:Modificações:Dados de Eventos">pt:Modificações:Dados de
Eventos</a> <a href="ru_Модификации_События" class="wikilink"
title="ru:Модификации:События">ru:Модификации:События</a>
<a href="zh_模组_事件数据" class="wikilink"
title="zh:模组:事件数据">zh:模组:事件数据</a>
