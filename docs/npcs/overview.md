---
title: "Overview"
wiki_source: "Modding:NPC data"
permalink: /Modding:NPC_data/
category: npcs
tags: [npc-data, files-to-edit, main-data, gift-tastes, overworld-sprites, portraits, schedule, dialogue]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page provides an overview of what's needed to create a custom NPC.
This is an advanced guide for mod developers.

## Files to edit

To create a new NPC, you need to edit a number of different files.
However, you don't need any programming experience and it can be done
with <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a>.

### Main data

The `Data/Characters` asset contains most of the data about an NPC. That
includes their name, social info (e.g. personality, birthday, and
romance), appearance, spouse room & patio, festival participation, etc.
(Note that all translated vanilla NPC names are in `Strings/NPCNames`).

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  NPC like `Example.ModId_NpcName`, which will be used as the internal
  `Name` (not `DisplayName`).
- The value is a model with the following fields.

#### Basic info

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
title="tokenizable string">tokenizable string</a> for the NPC's display
name.</p></td>
</tr>
<tr>
<td><p><samp>Language</samp></p></td>
<td><p><em>(Optional)</em> The language spoken by the NPC. One of
<samp>Default</samp> (the default language understood by the player) or
<samp>Dwarvish</samp> (which the player can only understand after
finding the <a href="Dwarvish_Translation_Guide" class="wikilink"
title="Dwarvish translation guide">Dwarvish translation guide</a>).
Default <samp>Default</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Gender</samp></p></td>
<td><p><em>(Optional)</em> The NPC's gender identity. One of
<samp>Female</samp>, <samp>Male</samp>, or <samp>Undefined</samp>.
Default <samp>Undefined</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Age</samp></p></td>
<td><p><em>(Optional)</em> The general age of the NPC. One of
<samp>Child</samp>, <samp>Teen</samp>, or <samp>Adult</samp>. Default
<samp>Adult</samp>.</p>
<p>This affects generated dialogue lines (e.g. a child might say
"stupid" and an adult might say "depressing"), generic dialogue (e.g. a
child might respond to dumpster diving with "<em>Eww... What are you
doing?</em>" and a teen would say "<em>Um... Why are you digging in the
trash?</em>"), and the gift they choose as <a
href="Feast_of_the_Winter_Star" class="wikilink"
title="Feast of the Winter Star">Feast of the Winter Star</a>
gift-giver. Children are also excluded from item delivery
quests.</p></td>
</tr>
<tr>
<td><p><samp>Manner</samp></p></td>
<td><p><em>(Optional)</em> A measure of the character's general
politeness, which affects some generic dialogue lines. One of
<samp>Neutral</samp>, <samp>Polite</samp>, or <samp>Rude</samp>. Default
<samp>Neutral</samp>.</p></td>
</tr>
<tr>
<td><p><samp>SocialAnxiety</samp></p></td>
<td><p><em>(Optional)</em> A measure of the character's comfort with
social situations, which affects some generic dialogue lines. One of
<samp>Neutral</samp>, <samp>Outgoing</samp>, or <samp>Shy</samp>.
Default <samp>Neutral</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Optimism</samp></p></td>
<td><p><em>(Optional)</em> A measure of the character's overall
optimism. One of <samp>Neutral</samp>, <samp>Negative</samp>, or
<samp>Positive</samp>. Default <samp>Neutral</samp>.</p></td>
</tr>
<tr>
<td><p><samp>BirthSeason</samp></p></td>
<td><p><em>(Optional if non-social)</em> The season name
(case-sensitive) for the NPC's birthday. One of <samp>spring</samp>,
<samp>summer</samp>, <samp>fall</samp>, or <samp>winter</samp>. Default
none.</p></td>
</tr>
<tr>
<td><p><samp>BirthDay</samp></p></td>
<td><p><em>(Optional if non-social)</em> The day number for the NPC's
birthday. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>HomeRegion</samp></p></td>
<td><p><em>(Optional)</em> The region of the world in which the NPC
lives (one of <samp>Desert</samp>, <samp>Town</samp>, or
<samp>Other</samp>). For example, only <samp>Town</samp> NPCs are
counted for the introductions <a href="Quests#List_of_Story_Quests"
class="wikilink" title="quest">quest</a>, can be selected as a secret
santa for the <a href="Feast_of_the_Winter_Star" class="wikilink"
title="Feast of the Winter Star">Feast of the Winter Star</a>, or get a
friendship boost from the <a href="Luau" class="wikilink"
title="Luau">Luau</a>. Default <samp>Other</samp>.</p></td>
</tr>
<tr>
<td><p><samp>IsDarkSkinned</samp></p></td>
<td><p><em>(Optional)</em> Whether the NPC has dark skin, which affects
the chance of children with the player having dark skin too. Default
false.</p></td>
</tr>
</tbody>
</table>

#### Social features

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>CanSocialize</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether to enable social features (like birthdays, gift
giving, <a href="friendship" class="wikilink"
title="friendship">friendship</a>, and an entry in the social tab).
Default true.</p></td>
</tr>
<tr>
<td><p><samp>CanBeRomanced</samp></p></td>
<td><p><em>(Optional)</em> Whether the NPC can be dated and romanced.
This enables romance features for this NPC (like a 'single' label in the
social menu, bouquet gifting, and marriage). Default false.</p></td>
</tr>
<tr>
<td><p><samp>CanReceiveGifts</samp></p></td>
<td><p><em>(Optional)</em> Whether players can give gifts to this NPC.
Default true.</p>
<p>The NPC must also be social per <samp>CanSocialize</samp> and have an
entry in <samp>Data/NPCGiftTastes</samp> to be giftable, regardless of
this value.</p></td>
</tr>
<tr>
<td><p><samp>CanCommentOnPurchasedShopItems</samp></p></td>
<td><p><em>(Optional)</em> Whether this NPC can comment on items that a
player sold to a shop which then resold it to them. If null (or
omitted), this will default to true if their <samp>HomeRegion</samp> is
set to <samp>Town</samp>.</p>
<p>The NPC must also be social per <samp>CanSocialize</samp> to allow
it, regardless of this value.</p></td>
</tr>
<tr>
<td><p><samp>CanGreetNearbyCharacters</samp></p></td>
<td><p><em>(Optional)</em> Whether this NPC can show a speech bubble
greeting nearby players or NPCs, and or be greeted by other NPCs.
Default true.</p></td>
</tr>
<tr>
<td><p><samp>CanVisitIsland</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the NPC can visit the <a href="Ginger_Island"
class="wikilink" title="Ginger Island">Ginger Island</a> resort once
it's unlocked. Default true.</p>
<p>The NPC must also be social per <samp>CanSocialize</samp> to visit
the island, regardless of this value.</p></td>
</tr>
<tr>
<td><p><samp>LoveInterest</samp></p></td>
<td><p><em>(Optional)</em> Unused.</p></td>
</tr>
<tr>
<td><p><samp>Calendar</samp></p></td>
<td><p><em>(Optional)</em> Determines when the NPC's birthday is shown
in the <a href="calendar" class="wikilink"
title="calendar">calendar</a>. Possible values:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>HiddenAlways</samp></p></td>
<td><p>They never appear in the calendar.</p></td>
</tr>
<tr>
<td><p><samp>HiddenUntilMet</samp></p></td>
<td><p>Until the player meets them, they don't appear in the
calendar.</p></td>
</tr>
<tr>
<td><p><samp>AlwaysShown</samp></p></td>
<td><p>They always appear in the calendar.</p></td>
</tr>
</tbody>
</table>
<p>Defaults to <samp>AlwaysShown</samp>.</p></td>
</tr>
<tr>
<td><p><samp>SocialTab</samp></p></td>
<td><p><em>(Optional)</em> Determines how the NPC is shown on the <a
href="friendship" class="wikilink" title="social tab">social tab</a>
when unlocked. Possible values:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>HiddenAlways</samp></p></td>
<td><p>They never appear in the social tab.</p></td>
</tr>
<tr>
<td><p><samp>HiddenUntilMet</samp></p></td>
<td><p>Until the player meets them, they don't appear on the social
tab.</p></td>
</tr>
<tr>
<td><p><samp>UnknownUntilMet</samp></p></td>
<td><p>Until the player meets them, their name on the social tab is
replaced with "???".</p></td>
</tr>
<tr>
<td><p><samp>AlwaysShown</samp></p></td>
<td><p>They always appear in the social tab (including their
name).</p></td>
</tr>
</tbody>
</table>
<p>Defaults to <samp>UnknownUntilMet</samp>.</p></td>
</tr>
<tr>
<td><p><samp>SpouseAdopts</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the player will need to adopt children with this
spouse, instead of either the player or NPC giving birth. If null,
defaults to true for same-gender and false for opposite-gender
spouses.</p>
<p>The <samp>Target</samp> player is the one they're married
to.</p></td>
</tr>
<tr>
<td><p><samp>SpouseWantsChildren</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the spouse will ask to have children. Defaults to
true.</p>
<p>The <samp>Target</samp> player is the one they're married
to.</p></td>
</tr>
<tr>
<td><p><samp>SpouseGiftJealousy</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the <a href="Marriage#Jealousy" class="wikilink"
title="spouse will get jealous of gifts to other NPCs">spouse will get
jealous of gifts to other NPCs</a>. Defaults to true.</p>
<p>The <samp>Target</samp> player is the one they're married to, and the
<samp>Target</samp> item is the one that was gifted.</p></td>
</tr>
<tr>
<td><p><samp>SpouseGiftJealousyFriendshipChange</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Friendship" class="wikilink"
title="friendship point">friendship point</a> effect when the
<samp>SpouseGiftJealously</samp> is triggered. Default -30.</p></td>
</tr>
<tr>
<td><p><samp>SpouseRoom</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Marriage#Spouse_Rooms"
class="wikilink" title="NPC&#39;s spouse room">NPC's spouse room</a> in
the farmhouse when the player marries them, if applicable. If this is
omitted for a marriageable NPC, they'll use Abigail's spouse room by
default.</p>
<p>This consists of a model with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>MapAsset</samp></p></td>
<td><p><em>(Optional)</em> The asset name for the spouse room map. The
<samp>Maps/</samp> prefix is added automatically and shouldn't be
included. Defaults to <samp>spouseRooms</samp>.</p></td>
</tr>
<tr>
<td><p><samp>MapSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The tile area within the
<samp>MapAsset</samp> containing the spouse's room. This should usually
be a 6x9 tile area, though the game will try to adjust to a different
size. Specified as a model with <samp>X</samp>, <samp>Y</samp>,
<samp>Width</samp>, and <samp>Height</samp> fields. Defaults to
<samp>(0, 0, 6, 9)</samp>.</p></td>
</tr>
</tbody>
</table>
<p>You can mark where the spouse stands in their spouse room by placing
the red circle path tile (tile index 7) on <a
href="Modding_Maps#Paths_layer" class="wikilink"
title="the Paths layer">the <samp>Paths</samp> layer</a>.</p></td>
</tr>
<tr>
<td><p><samp>SpousePatio</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Marriage#Spouse_Outside_Area"
class="wikilink" title="NPC&#39;s patio area">NPC's patio area</a> on
the farm when the player marries them, if any. Default none.</p>
<p>This consists of a model with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>MapAsset</samp></p></td>
<td><p><em>(Optional)</em> The asset name for the patio area. The
<samp>Maps/</samp> prefix is added automatically and shouldn't be
included. Defaults to <samp>spousePatios</samp>.</p></td>
</tr>
<tr>
<td><p><samp>MapSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The tile area within the
<samp>MapAsset</samp> containing the spouse's patio area. This must be a
4x4 tile area. Specified as a model with <samp>X</samp>, <samp>Y</samp>,
<samp>Width</samp>, and <samp>Height</samp> fields. Defaults to
<samp>(0, 0, 4, 4)</samp>.</p></td>
</tr>
<tr>
<td><p><samp>SpriteAnimationFrames</samp></p></td>
<td><p><em>(Optional)</em> The spouse's animation frames when they're in
the patio. Each frame is an array containing [0] the sprite index in
their spritesheet, and [1] the optional duration in milliseconds
(default 100). If omitted or empty, the NPC won't be animated.</p>
<p>For example, here is Abigail playing the flute:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;SpriteAnimationFrames&quot;</span><span class="op">:</span> [</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    [<span class="dv">16</span><span class="op">,</span> <span class="dv">500</span>]<span class="op">,</span> <span class="co">// show index 16 for 500ms</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    [<span class="dv">17</span><span class="op">,</span> <span class="dv">500</span>]<span class="op">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    [<span class="dv">18</span><span class="op">,</span> <span class="dv">500</span>]<span class="op">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    [<span class="dv">19</span>]       <span class="co">// if duration is omitted, defaults to 100ms</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>]</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>SpriteAnimationPixelOffset</samp></p></td>
<td><p><em>(Optional)</em> The pixel offset to apply to the NPC's sprite
when they're animated in the patio, specified as a model with
<samp>X</samp> and <samp>Y</samp> fields. This is ignored if the NPC
isn't animated via <samp>SpriteAnimationFrames</samp>. Default
none.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>SpouseFloors</samp><br />
<samp>SpouseWallpapers</samp></p></td>
<td><p><em>(Optional)</em> The floors and wallpapers which the NPC may
randomly apply to the farmhouse when married to the player. If omitted
or empty, the NPC will randomly choose a base floor (0–39) or wallpaper
(0–111).</p></td>
</tr>
<tr>
<td><p><samp>IntroductionsQuest</samp></p></td>
<td><p><em>(Optional)</em> Whether to include this NPC in <a
href="Quests#List_of_Story_Quests" class="wikilink"
title="the introductions quest">the <em>introductions</em> quest</a>. If
<samp>null</samp> (or omitted), this will default to true if the
<samp>HomeRegion</samp> field is set to <samp>Town</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ItemDeliveryQuests</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this NPC can give item delivery quests. If
<samp>null</samp> (or omitted), this will default to true if the
<samp>HomeRegion</samp> field is set to <samp>Town</samp>.</p>
<p>The NPC must also be social per <samp>CanSocialize</samp> to allow
it, regardless of this value.</p></td>
</tr>
<tr>
<td><p><samp>PerfectionScore</samp></p></td>
<td><p><em>(Optional)</em> Whether to include this NPC when checking
whether the player has max friendships with every NPC for the perfection
score. Default true.</p>
<p>The NPC must also be social per <samp>CanSocialize</samp> to be
counted, regardless of this value.</p></td>
</tr>
<tr>
<td><p><samp>EndSlideShow</samp></p></td>
<td><p><em>(Optional)</em> How the NPC appears in the end-game
perfection slide show. Possible values:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Hidden</samp></p></td>
<td><p>The NPC doesn't appear in the slide show.</p></td>
</tr>
<tr>
<td><p><samp>MainGroup</samp></p></td>
<td><p>The NPC is added to the main group of NPCs which walk across the
screen.</p></td>
</tr>
<tr>
<td><p><samp>TrailingGroup</samp></p></td>
<td><p>The NPC is added to the trailing group of NPCs which follow the
main group.</p></td>
</tr>
</tbody>
</table>
<p>Defaults to <samp>MainGroup</samp>.</p></td>
</tr>
<tr>
<td><p><samp>FriendsAndFamily</samp></p></td>
<td><p><em>(Optional)</em> The NPC's closest friends and family, as a
dictionary where the key is the other NPC's internal name and the value
is an optional tokenizable string for the name to use in dialogue text
(like 'mom'). Default none.</p>
<p>This affects generic dialogue for revealing likes and dislikes to
family members, and may affect <samp>inlaw_&lt;NPC&gt;</samp> dialogues.
This isn't necessarily comprehensive.</p></td>
</tr>
</tbody>
</table>

#### Dumpster diving

| field | effect |
|----|----|
| `DumpsterDiveEmote` | *(Optional)* The emote ID to show above the NPC's head when they see a player rummaging through trash. See <a href="Modding_event_data#Emotes" class="wikilink"
title="emote IDs">emote IDs</a>. If omitted or `null`, the default depends on the NPC's age: a child will show sad (28), a teen will show a question mark (8), and an adult will show angry (12). |
| `DumpsterDiveFriendshipEffect` | *(Optional)* The friendship point change if this NPC sees a player rummaging through trash. Default -25. |

#### Festivals

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>FlowerDanceCanDance</samp></p></td>
<td><p><em>(Optional)</em> Whether players can ask the NPC to dance at
the Flower Dance festival. The possible values are <samp>true</samp>
(can always ask), <samp>false</samp> (can never ask), or
<samp>null</samp> (can ask if they're romanceable). Default
<samp>null</samp>.</p>
<p>If the NPC can dance, you should also add the <a
href="Modding_NPC_data#Overworld_sprites" class="wikilink"
title="dance sprite frames">dance sprite frames</a> and
<samp>FlowerDance_Decline</samp> <a href="Modding_Dialogue"
class="wikilink" title="dialogue text">dialogue text</a>. You can
optionally set the <samp>FlowerDance_Accept</samp> dialogue too (though
NPCs have a default accept dialogue if not).</p></td>
</tr>
<tr>
<td><p><samp>WinterStarParticipant</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this NPC can give and receive gifts at the <a
href="Feast_of_the_Winter_Star" class="wikilink"
title="Feast of the Winter Star">Feast of the Winter Star</a>. If
<samp>null</samp> (or omitted), this will default to true if the
<samp>HomeRegion</samp> field is set to <samp>Town</samp>.</p></td>
</tr>
<tr>
<td><p><samp>WinterStarGifts</samp></p></td>
<td><p>At the <a href="Feast_of_the_Winter_Star" class="wikilink"
title="Feast of the Winter Star">Feast of the Winter Star</a>, the
possible gifts this NPC can give to players. A matching entry is
selected at random.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
</tbody>
</table>
<p>For example, an NPC gifting you a <a href="Tea_Set" class="wikilink"
title="Tea Set">Tea Set</a> would look like this:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;WinterStarGifts&quot;</span><span class="er">:</span> <span class="ot">[</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>   <span class="fu">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Id&quot;</span><span class="fu">:</span> <span class="st">&quot;Tea Set&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;ItemId&quot;</span><span class="fu">:</span> <span class="st">&quot;(O)341&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>   <span class="fu">}</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

#### Spawn rules

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>UnlockConditions</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the NPC should be added to the world, checked when
loading a save and when ending each day. This only affects whether the
NPC is added when missing; returning false won't remove an NPC that's
already been added. Defaults to true.</p></td>
</tr>
<tr>
<td><p><samp>SpawnIfMissing</samp></p></td>
<td><p><em>(Optional)</em> Whether to add this NPC to the world if
they're missing (if the <samp>UnlockConditions</samp> match and
<samp>HomeLocation</samp> is valid). Default true.</p></td>
</tr>
<tr>
<td><p><samp>Home</samp></p></td>
<td><p><em>(Optional)</em> The default place where this NPC spawns and
returns each day. If there are multiple entries, the first matching one
is used.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ID</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry within the current list.</p></td>
</tr>
<tr>
<td><p><samp>Location</samp></p></td>
<td><p><em>(Optional)</em> The internal name for the home location where
this NPC spawns and returns each day. Default none.</p></td>
</tr>
<tr>
<td><p><samp>Tile</samp></p></td>
<td><p><em>(Optional)</em> The tile position within the home location
where this NPC spawns and returns each day. Specified as a model with
<samp>X</samp> and <samp>Y</samp> fields. Defaults to <samp>(0,
0)</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Direction</samp></p></td>
<td><p><em>(Optional)</em> The default direction the NPC faces when they
start each day. The possible values are <samp>down</samp>,
<samp>left</samp>, <samp>right</samp>, and <samp>up</samp>. Defaults to
<samp>up</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry can be selected. Default true.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

#### Appearance & sprite

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>TextureName</samp></p></td>
<td><p><em>(Optional)</em> The <strong>last segment</strong> of the
NPC's portrait and sprite asset names. For example, set to
<samp>Abigail</samp> to use <samp>Portraits/Abigail</samp> and
<samp>Characters/Abigail</samp> respectively. Defaults to the internal
NPC name. The Calendar and Social Tab use this texture, ignoring any
currently applied appearance options.</p></td>
</tr>
<tr>
<td><p><samp>Appearance</samp></p></td>
<td><p><em>(Optional)</em> The portrait/sprite textures to use.</p>
<p>This can list any number of appearance options. They'll be sorted by
<samp>Precedence</samp> value (with lower values taking priority), then
filtered to those whose fields match. If multiple matching appearances
have precedence, one entry is randomly chosen based on their relative
weight. This randomization is stable per day, so the NPC always makes
the same choice until the next day. If a portrait/sprite can't be loaded
(or no appearances match), the NPC will use the default asset based on
<samp>TextureName</samp>.</p>
<p>The NPC rechecks this field each time they change location.</p>
<p>This consists of a list of models with these fields:</p>
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
entry within the current list.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> The season in which this appearance should be
used (one of <samp>spring</samp>, <samp>summer</samp>,
<samp>fall</samp>, or <samp>winter</samp>), or omit for any season.
Defaults to any season.</p></td>
</tr>
<tr>
<td><p><samp>Indoors</samp><br />
<samp>Outdoors</samp></p></td>
<td><p><em>(Optional)</em> Whether this appearance should be used when
indoors and/or outdoors. Both default to true.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry can be selected. Default true.</p></td>
</tr>
<tr>
<td><p><samp>Portrait</samp><br />
<samp>Sprite</samp></p></td>
<td><p><em>(Optional)</em> The asset name for the portraits and/or
sprites texture to load. If omitted or it can't be loaded, it will
default to the default asset per the <samp>Texture</samp>
field.</p></td>
</tr>
<tr>
<td><p><samp>IsIslandAttire</samp></p></td>
<td><p><em>(Optional)</em> Whether this is island beach attire worn at
the resort. Default false.</p>
<p>This is mutually exclusive: NPCs will never wear it in other contexts
if it's true, and will never wear it as island attire if it's
false.</p></td>
</tr>
<tr>
<td><p><samp>Precedence</samp></p></td>
<td><p><em>(Optional)</em> The order in which this entry should be
checked, where lower values are checked first. This can be a negative
value. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>Weight</samp></p></td>
<td><p><em>(Optional)</em> If multiple entries with the same
<samp>Precedence</samp> match, the relative weight to use when randomly
choosing one. Default 1.</p>
<p>For example, let's say two appearance entries match: one has a weight
of 2, and the other has a weight of 1. Their probability of being chosen
is 2/3 and 1/3 respectively.</p></td>
</tr>
</tbody>
</table>
<p><strong>Note:</strong> the default textures based on
<samp>TextureName</samp> must still exist, even if you use this field to
override them. The image of the NPC in the Calendar and Social Tab will
ignore appearance options.</p></td>
</tr>
<tr>
<td><p><samp>MugShotSourceRect</samp></p></td>
<td><p><em>(Optional)</em> A <a
href="Modding_Common_data_field_types#Rectangle" class="wikilink"
title="rectangle">rectangle</a> specifying the portion of the
character's sprite texture to show as their mug shot icon in the
calendar, social menu, and other contexts. Defaults to part of their
first sprite, based on <samp>Age</samp>: <samp>(0, 4, 16, 24)</samp> for
a <samp>Child</samp> and <samp>(0, 0, 16, 24)</samp> for a
<samp>Teen</samp> or <samp>Adult</samp>.</p>
<p>For best results, use an area 16 by 24 pixels in size.</p></td>
</tr>
<tr>
<td><p><samp>Size</samp></p></td>
<td><p><em>(Optional)</em> The pixel size of the individual sprites in
their overworld sprite spritesheet. Specified as a model with
<samp>X</samp> and <samp>Y</samp> fields. Defaults to <samp>(16,
32)</samp>.</p>
<p><strong>Note:</strong> sizes bigger than 16×32 will cause issues like
broken spawning, pathfinding, misalignment in the <a href="perfection"
class="wikilink" title="perfection">perfection</a> end-game slide show,
etc.</p></td>
</tr>
<tr>
<td><p><samp>Breather</samp></p></td>
<td><p><em>(Optional)</em> Whether the chest on the NPC's overworld
sprite puffs in and out as they breathe. Default true</samp>.</p></td>
</tr>
<tr>
<td><p><samp>BreathChestRect</samp></p></td>
<td><p><em>(Optional)</em> A <a
href="Modding_Common_data_field_types#Rectangle" class="wikilink"
title="rectangle">rectangle</a> pixel area within the spritesheet which
expands and contracts to simulate breathing, relative to the top-left
corner of the source rectangle for their current sprite. Omit to
calculate it automatically. This should be omitted for most NPCs, unless
they have a non-standard size.</p></td>
</tr>
<tr>
<td><p><samp>BreathChestPosition</samp></p></td>
<td><p><em>(Optional)</em> A <a
href="Modding_Common_data_field_types#Point" class="wikilink"
title="point">point</a> pixel offset to apply to the NPC's
<samp>BreathChestPosition</samp> when drawn over the NPC. Omit to
calculate it automatically. This should be omitted for most NPCs, unless
they have a non-standard size.</p></td>
</tr>
<tr>
<td><p><samp>Shadow</samp></p></td>
<td><p><em>(Optional)</em> The options for the shadow to draw under the
NPC, or omit to apply the default shadow behavior.</p>
<p>This consists of a model with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Visible</samp></p></td>
<td><p><em>(Optional)</em> Whether the shadow should be drawn. Default
true.</p></td>
</tr>
<tr>
<td><p><samp>Offset</samp></p></td>
<td><p><em>(Optional)</em> A <a
href="Modding_Common_data_field_types#Point" class="wikilink"
title="point">point</a> pixel offset applied to the shadow position.
Default <samp>(0, 0)</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Scale</samp></p></td>
<td><p><em>(Optional)</em> The scale at which to draw the shadow.
Default 1.</p>
<p>This is a multiplier applied to the default shadow scale, which can
change based on factors like whether the NPC is jumping. For example,
<samp>0.5</samp> means half the size it'd be drawn if you didn't specify
a scale.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>EmoteOffset</samp></p></td>
<td><p><em>(Optional)</em> A <a
href="Modding_Common_data_field_types#Point" class="wikilink"
title="point">point</a> pixel offset applied to emote drawn over the
NPC. Default zero.</p></td>
</tr>
<tr>
<td><p><samp>ShakePortraits</samp></p></td>
<td><p><em>(Optional)</em> The portrait indexes which should shake when
displayed. Default none.</p></td>
</tr>
<tr>
<td><p><samp>KissSpriteIndex</samp></p></td>
<td><p><em>(Optional)</em> If the NPC can be married, the sprite index
within their <samp>Texture</samp> to use when kissing a player. Default
28.</p></td>
</tr>
<tr>
<td><p><samp>KissSpriteFacingRight</samp></p></td>
<td><p><em>(Optional)</em> Whether the character is facing right (true)
or left (false) in their <samp>KissSpriteIndex</samp>. The sprite will
be flipped as needed to face the player. Default true.</p></td>
</tr>
</tbody>
</table>

#### <a href="Secrets#Gift_Log" class="wikilink"
title="Hidden gift log emote">Hidden gift log emote</a>

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>HiddenProfileEmoteSound</samp></p></td>
<td><p><em>(Optional)</em> For the <a href="Secrets#Gift_Log"
class="wikilink" title="hidden gift log emote">hidden gift log
emote</a>, the <a href="Modding_Audio#Sound" class="wikilink"
title="cue ID">cue ID</a> for the sound played when clicking the sprite.
Defaults to <samp>drumkit6</samp>.</p></td>
</tr>
<tr>
<td><p><samp>HiddenProfileEmoteDuration</samp></p></td>
<td><p><em>(Optional)</em> For the <a href="Secrets#Gift_Log"
class="wikilink" title="hidden gift log emote">hidden gift log
emote</a>, how long the animation plays measured in milliseconds.
Defaults to 4000 (4 seconds).</p></td>
</tr>
<tr>
<td><p><samp>HiddenProfileEmoteStartFrame</samp></p></td>
<td><p><em>(Optional)</em> For the <a href="Secrets#Gift_Log"
class="wikilink" title="hidden gift log emote">hidden gift log
emote</a>, the index within the NPC's overworld sprite spritesheet at
which the animation starts. If omitted for a vanilla NPC, the game plays
a default animation specific to that NPC; if omitted for a custom NPC,
the game just shows them walking while facing down.</p></td>
</tr>
<tr>
<td><p><samp>HiddenProfileEmoteFrameCount</samp></p></td>
<td><p><em>(Optional)</em> For the <a href="Secrets#Gift_Log"
class="wikilink" title="hidden gift log emote">hidden gift log
emote</a>, the number of frames in the animation. The first frame
corresponds to <samp>HiddenProfileEmoteStartFrame</samp>, and each
subsequent frame will use the next sprite in the spritesheet. Default
1.</p>
<p>This has no effect if <samp>HiddenProfileEmoteStartFrame</samp> isn't
set.</p></td>
</tr>
<tr>
<td><p><samp>HiddenProfileEmoteFrameDuration</samp></p></td>
<td><p><em>(Optional)</em> For the <a href="Secrets#Gift_Log"
class="wikilink" title="hidden gift log emote">hidden gift log
emote</a>, how long each animation frame is shown on-screen before
switching to the next one, measured in milliseconds. Default 200.</p>
<p>This has no effect if <samp>HiddenProfileEmoteStartFrame</samp> isn't
set.</p></td>
</tr>
</tbody>
</table>

#### Advanced

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
<tr>
<td><p><samp>FormerCharacterNames</samp></p></td>
<td><p><em>(Optional)</em> The former NPC names which may appear in save
data. If matched, the game will rename the NPC and update related data
(e.g. friendship).</p>
<p>A former name is only applied if:</p>
<ol>
<li>it doesn't match a current ID in <samp>Data/Characters</samp>;</li>
<li>the save has an NPC with the former name;</li>
<li>the save doesn't already have an NPC with the new name.</li>
</ol>
<p>For example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;FormerCharacterNames&quot;</span><span class="op">:</span> [ <span class="st">&quot;SomeOldName&quot;</span> ]</span></code></pre></div>
<p>Former names can have any format, but they must be
<strong>globally</strong> unique. They can't match the ID or
<samp>FormerCharacterNames</samp> of any other NPC in
<samp>Data/Characters</samp> (whether vanilla or custom).</p></td>
</tr>
<tr>
<td><p><samp>FestivalVanillaActorIndex</samp></p></td>
<td><p><em>(Optional, Specialized)</em> The NPC's index in the
<samp>Maps/characterSheet</samp> tilesheet, if applicable. This is used
for placing vanilla NPCs in festivals from the map; custom NPCs should
use the <samp>&lt;layer&gt;_additionalCharacters</samp> field in the
festival data instead.</p></td>
</tr>
</tbody>
</table>

### Gift tastes

main gift data
The `Data/NPCGiftTastes` asset contains their gift preferences (*e.g.,*
which gifts they love or hate), and their responses when they receive
one. See <a href="Modding_Gift_taste_data" class="wikilink"
title="Modding:Gift taste data">Modding:Gift taste data</a> for more
info.

<!-- -->


The file has one row per NPC like this:

``` yaml
Abigail: "I seriously love this! You're the best, @!/66 128 220 226 276 611/Hey, how'd you know I was hungry? This looks delicious!//What am I supposed to do with this?/-5 -75 -79 16 245 246/What were you thinking? This is awful!/330/You brought me a present? Thanks.//"
```

<!-- -->


The line can be broken down into 5 pairs of dialogue + item IDs in this
order: Love, Like, Dislike, Hate, Neutral. These dialogue pairs can be
multilined after the / delimiter for readability. If a dialogue field is
empty, the game will use a generic dialogue text. See
<a href="Modding_Objects" class="wikilink"
title="Modding:Objects">Modding:Objects</a> for the object IDs.

<!-- -->

gift dialogue
When you gift an NPC, they'll show a
<a href="Modding_Dialogue" class="wikilink"
title="dialogue">dialogue</a> in this order:

1.  on their birthday, an `AcceptBirthdayGift` dialogue key, else a
    default dialogue like `NPC.cs.4274` ("*You remembered my birthday?
    I'm impressed. Thanks.\$h*");
2.  an `AcceptGift_*` dialogue;
3.  else the dialogue in `Data/NPCGiftTastes` with a default portrait
    (which can be overridden with
    <a href="Modding_Dialogue#Portrait_commands" class="wikilink"
    title="portrait commands">portrait commands</a> like `$h`).

### Overworld sprites

<a href="File_Abigail-sprite-sheet.png" class="wikilink"
title="thumb">thumb</a>

The overworld sprites are stored in `Characters/NpcName`, including
movement and animation frames. Each frame is exactly 16x32 pixels. Note
that the first frame counts as frame 0.

- the first sixteen frames are generic movement (four frames per
  direction);
- frames 40–47 (female) and 44–47 (male) must be the Flower Dance dance,
  if they participate;
- frames 36–38 (female) 48–50 (male) are reserved for marriageable NPCs
  (Contains Wedding sprite);
- and the kissing sprite/direction varies depending on NPC:
  | character | kissing frame | facing direction |
  |----|----|----|
  | <a href="Abigail" class="wikilink" title="Abigail">Abigail</a> and <a href="Emily" class="wikilink" title="Emily">Emily</a> | 33 | left |
  | <a href="Alex" class="wikilink" title="Alex">Alex</a> | 42 | right |
  | <a href="Elliott" class="wikilink" title="Elliott">Elliott</a> | 35 | left |
  | <a href="Haley" class="wikilink" title="Haley">Haley</a> | 28 | right |
  | <a href="Harvey" class="wikilink" title="Harvey">Harvey</a> | 31 | left |
  | <a href="Leah" class="wikilink" title="Leah">Leah</a> | 25 | right |
  | <a href="Maru" class="wikilink" title="Maru">Maru</a> | 28 | left |
  | <a href="Penny" class="wikilink" title="Penny">Penny</a> | 35 | right |
  | <a href="Sam" class="wikilink" title="Sam">Sam</a> | 36 | right |
  | <a href="Sebastian" class="wikilink" title="Sebastian">Sebastian</a> | 40 | left |
  | <a href="Shane" class="wikilink" title="Shane">Shane</a> | 34 | left |
  | *any other NPC* | 28 | right |

### Portraits

<a href="File_Modding_-_creating_an_XNB_mod_-_example_portraits.png"
class="wikilink" title="thumb">thumb</a>

The dialogue portraits are stored in `Portraits/NpcName`. Each frame is
exactly 64x64 per portrait. The first six represent specific emotions
(see <a href="Modding_Dialogue#Portrait_commands" class="wikilink"
title="Modding:Dialogue#Portrait commands">Modding:Dialogue#Portrait
commands</a>), followed by any number of custom portraits. The first
portrait is used when the dialogue doesn't specify one.

### Schedule

Their schedule file tells the game where the NPC starts and moves based
on on the time. You need to add strings to a separate schedules file
found in the Strings folder to allow custom dialogue. See
<a href="Modding_Schedule_data" class="wikilink"
title="Modding:Schedule data">Modding:Schedule data</a> for more info.

### Dialogue

The NPC dialogue and events are stored in several files; see
<a href="Modding_Dialogue" class="wikilink"
title="Modding:Dialogue">Modding:Dialogue</a>.

### Sleep animation

When the NPC goes to bed, they'll play the looping sleep animation set
via `<lowercase NPC name>_sleep` in `Data/animationDescriptions`, if it
exists. For example, this content pack adds a sleep animation for an NPC
named 'Pufferbob':

### Secondary assets

- See
  <a href="Modding_Event_data" class="wikilink" title="event data">event
  data</a> for the NPC's cutscenes.
- See <a href="Modding_Festival_data" class="wikilink"
  title="festival data">festival data</a> for an NPC's positions (via
  the `Set-Up_additionalCharacters` and `MainEvent_additionalCharacters`
  fields) and dialogue in festivals.
- See <a href="Modding_Movie_theater_data" class="wikilink"
  title="movie theater data">movie theater data</a> for an NPC's taste
  in movies and concessions.

## Non-Krobus roommates

The game's
<a href="marriage" class="wikilink" title="marriage">marriage</a> logic
can treat any NPC (including custom NPCs), not just
<a href="Krobus" class="wikilink" title="Krobus">Krobus</a>, as a
roommate.

Specifically:

- Items with the "`propose_roommate_<NPC name>`"
  <a href="Modding_Context_tags" class="wikilink"
  title="context tag">context tag</a> will trigger a roommate proposal
  when given to the named NPC. The NPC name must be lowercase with
  underscores instead of spaces (*e.g.,* `propose_roommate_dwarf`).
- Roommates will sleep in a
  <a href="Single_Bed" class="wikilink" title="Single Bed">Single Bed</a>
  if one is available and unused in the house; otherwise they'll use a
  double bed like a normal spouse. (Krobus is an exception, since he
  doesn't sleep in a bed.)

See <a href="Modding_Dialogue#Roommate_dialogue" class="wikilink"
title="Modding:Dialogue#Roommate_dialogue">Modding:Dialogue#Roommate_dialogue</a>
for relevant dialogue keys for roommates.

## Examples

### Full NPC

Here's how you'd create an example NPC named Dobson with full social
features.

Note that is a Content Patcher token, which will be replaced with your
mod ID automatically for the
<a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a>
convention.

1.  [Create an empty Content Patcher content
    pack](https://github.com/Pathoschild/StardewMods/blob/develop/ContentPatcher/docs/author-guide.md#format).
    By convention, we'll name the folder `[CP] Dobson`.
2.  Create the following files:
    - `assets/dialogue.json` containing the dialogue.
    - `assets/marriageDialogue.json` containing the marriage dialogue
      (if applicable).
    - `assets/sprites.png` containing their overworld sprites.
    - `assets/portraits.png` containing their portraits.
    - `assets/schedule.json` containing their schedule data.
3.  Edit the `content.json` to load the files:

That's it! If you load your game, the NPC should appear. If you want to
create events, don't forget to add that file too.

### Dynamic appearances

The <a href="#Appearance_&amp;_sprite" class="wikilink"
title="Appearance field in Data/Characters"><samp>Appearance</samp>
field in <samp>Data/Characters</samp></a> lets NPCs have any number of
custom portraits & sprites with arbitrary conditions, without the
performance cost of reloading NPCs' textures.

For example, this adds indoor/outdoor sprites for the previous Dobson
example:

``` js
// add base indoor/outdoor sprites
{
    "Action": "Load",
    "Target": "
        Characters/_Dobson_Indoor,
        Characters/_Dobson_Outdoor,
        Portraits/_Dobson_Indoor,
        Portraits/_Dobson_Outdoor
    ",
    "FromFile": "assets/.png"
},

// apply any overlays needed
{
    "Action": "EditImage",
    "Target": "Characters/_Dobson_Indoor, Portraits/_Dobson_Indoor",
    "FromFile": "assets/overlays/_married.png",
    "When": {
        "Spouse": "Dobson"
    }
},

// add appearance to NPC
{
    "Action": "EditData",
    "Target": "Data/Characters",
    "Entries": {
        "_Dobson": {
            ...,
            "Appearance": [
                {
                    "Id": "Outdoors",
                    "Indoors": false,
                    "Portrait": "Portraits/_Dobson_Outdoor",
                    "Sprite": "Characters/_Dobson_Outdoor"
                },
                {
                    "Id": "Default",
                    "Portrait": "Portraits/_Dobson_Indoor",
                    "Sprite": "Characters/_Dobson_Indoor"
                }
            ]
        }
    }
}
```

## Limitations

- When an NPC is added to an existing save, they generally don't follow
  their schedule correctly until you've slept once in-game (which
  triggers their first day update).

## See also

- See <a href="Modding_Index#See_also" class="wikilink"
  title="Modding:Index#See also">Modding:Index#See also</a> for
  recommended guides on pixel art.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Datos_de_NPC" class="wikilink"
title="es:Modding:Datos de NPC">es:Modding:Datos de NPC</a>
<a href="pt_Modificações_Dados_do_NPC" class="wikilink"
title="pt:Modificações:Dados do NPC">pt:Modificações:Dados do NPC</a>
<a href="ru_Модификации_Данные_NPC" class="wikilink"
title="ru:Модификации:Данные NPC">ru:Модификации:Данные NPC</a>
<a href="zh_模组_NPC数据" class="wikilink"
title="zh:模组:NPC数据">zh:模组:NPC数据</a>
