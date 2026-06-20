---
title: "Dialogue"
wiki_source: "Modding:Dialogue"
permalink: /Modding:Dialogue/
category: npcs
tags: [dialogue, dialogue-data, characters-dialogue-directory, data-directory, strings-directory, algorithm, format, gender-switch]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores dialogue text, its format, and
how the game parses it. This is an advanced guide for mod developers.

## Dialogue data

Character dialogue is stored in many different files: The
`Characters\Dialogue` directory is where the majority of NPC-specific
dialogue is stored. `Data\ExtraDialogue.xnb`, `Strings\Characters.xnb`,
`Strings\Events.xnb`, `Strings\SpeechBubbles.xnb`, and
`Strings\StringsFromCSFiles.xnb` contain various other pieces of
dialogue, some generic, and some NPC-specific.

### Characters\Dialogue directory

#### Characters\Dialogue\\NPC\>.xnb

An NPC's named file in `Characters\Dialogue` contains most of their
dialogue. The game will select dialogue from one of the sections below,
in the order shown. This means keys listed earlier in each table are
checked first (and thus have higher priority), but note that some keys
only apply in certain circumstances or have a random chance to be
chosen, in which case lower-priority entries may appear.

##### Special dialogue

There are a few predefined keys for specific cases:

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>breakUp</samp></p></td>
<td><p>An NPC's response to being broken up with by giving them a <a
href="Wilted_Bouquet" class="wikilink" title="wilted bouquet">wilted
bouquet</a>.</p></td>
</tr>
<tr>
<td><p><samp>divorced</samp></p></td>
<td><p>Dialogue shown when you speak to your divorced spouse.</p></td>
</tr>
<tr>
<td><p><samp>DumpsterDiveComment</samp></p></td>
<td><p>Shown when the NPC catches the player digging through a trash
can. Defaults to a generic dialogue based on the NPC's age.</p></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>GreenRain</samp></p></td>
<td><p>Shown on <a href="Weather#Green_Rain" class="wikilink"
title="green rain">green rain</a> days, unless overridden by
<samp>GreenRain_2</samp>.</p></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>GreenRain_2</samp></p></td>
<td><p>Shown on <a href="Weather#Green_Rain" class="wikilink"
title="green rain">green rain</a> days in year two and subsequent years.
If not set, defaults to <samp>GreenRain</samp>.</p></td>
</tr>
<tr>
<td><p><samp>HitBySlingshot</samp></p></td>
<td><p>Shown when the player shoots them with a <a href="slingshot"
class="wikilink" title="slingshot">slingshot</a>. Defaults to a generic
dialogue.</p></td>
</tr>
<tr>
<td><p><samp>&lt;location&gt;_Entry</samp></p></td>
<td><p>Possible dialogue lines shown above the NPC's name when they
enter the named &lt;location&gt;, with a 50% chance. This dialogue entry
can contain multiple options separated by <code>/</code>; the game will
randomly choose one to display.<br />
<small>Example: <samp>SeedShop_Entry: "Hi, Pierre!/Now, what do I
need.../Ah, that looks good!/Makin' my special sauce tonight!/Pierre!
What's fresh?/Pierre! Waddya got for me?"</samp></br>Note: This key is
not to be confused with <a href="Modding_Dialogue#Speech_bubbles"
class="wikilink"
title="Modding:Dialogue#Speech_bubbles">Modding:Dialogue#Speech_bubbles</a>.</p></td>
</tr>
<tr>
<td><p><samp>Resort_Entering</samp><br />
<samp>Resort</samp><br />
<samp>Resort_&lt;random&gt;</samp><br />
<samp>Resort_Bar</samp><br />
<samp>Resort_Bar_&lt;random&gt;</samp><br />
<samp>Resort_Chair</samp><br />
<samp>Resort_Chair_&lt;random&gt;</samp><br />
<samp>Resort_Dance</samp><br />
<samp>Resort_Dance_&lt;random&gt;</samp><br />
<samp>Resort_Shore</samp><br />
<samp>Resort_Shore_&lt;random&gt;</samp><br />
<samp>Resort_Towel</samp><br />
<samp>Resort_Towel_&lt;random&gt;</samp><br />
<samp>Resort_Umbrella</samp><br />
<samp>Resort_Umbrella_&lt;random&gt;</samp><br />
<samp>Resort_Wander</samp><br />
<samp>Resort_Wander_&lt;random&gt;</samp><br />
<samp>Resort_Leaving</samp></p></td>
<td><p>Various dialogue keys used when an NPC is visiting the Ginger
Island Resort. &lt;random&gt; is a number between 2 and N (dynamically
determined by existing keys of the same type, provided that all from 2
to N are defined). Keys with a &lt;random&gt; require a base key
(without a suffix) to be defined. The game rolls a number from 1 to N,
and if 1 is chosen, the base key is used.</p></td>
</tr>
<tr>
<td><p><samp>SpouseFarmhouseClutter</samp></p></td>
<td><p>Shown by an NPC spouse when they couldn't pathfind to their
kitchen standing spot in the farmhouse.</p></td>
</tr>
<tr>
<td><p><samp>SpouseGiftJealous</samp></p></td>
<td><p>Shown by an NPC spouse if they become jealous after the player
gives a gift to another NPC that the player is dating. Spouses have a
20-40% chance to become jealous of the gift-giving if the giftee is of
the same gender as the spouse (unless it's the giftee's birthday). You
can use <samp>{0}</samp> in the dialogue for the other NPC's name, and
<samp>{1}</samp> for the gifted item name.</p></td>
</tr>
<tr>
<td><p><samp>Spouse_MonstersInHouse</samp></p></td>
<td><p>Shown by an NPC spouse when they're in the farmhouse and there's
a monster close to them.</p></td>
</tr>
<tr>
<td><p><samp>SpouseStardrop</samp></p></td>
<td><p>Shown when receiving the <a href="stardrop" class="wikilink"
title="stardrop">stardrop</a> from your spouse.</p></td>
</tr>
<tr>
<td><p><samp>WipedMemory</samp></p></td>
<td><p>Shown the first time you talk to the NPC after erasing their
memory using the <a href="Dark_Shrine_of_Memory" class="wikilink"
title="Dark Shrine of Memory">Dark Shrine of Memory</a>.</p></td>
</tr>
</tbody>
</table>

##### Item dialogue

These keys apply when you present an item to an NPC:

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AcceptBirthdayGift_&lt;id&gt;</samp><br />
<samp>AcceptBirthdayGift_&lt;tag&gt;</samp><br />
<samp>AcceptBirthdayGift_&lt;taste&gt;_&lt;context tag&gt;</samp><br />
<samp>AcceptBirthdayGift_&lt;taste&gt;</samp><br />
<samp>AcceptBirthdayGift_Negative</samp><br />
<samp>AcceptBirthdayGift_Positive</samp><br />
<samp>AcceptBirthdayGift</samp></p></td>
<td><p>Shown when receiving a birthday gift from the player. If omitted,
defaults to the generic translations for all NPCs. These keys will
override <samp>AcceptGift_&lt;id&gt;</samp> and
<samp>AcceptGift_&lt;tag&gt;</samp> even if the birthday key is less
specific.</p>
<p>The first matching dialogue is used in this order:</p>
<ol>
<li>by item ID (like <samp>AcceptBirthdayGift_(O)128</samp>);</li>
<li>by context tag (like
<samp>AcceptBirthdayGift_category_fish</samp>);</li>
<li>by context tag and gift taste (see below for valid gift
tastes);</li>
<li>by gift taste (one of <samp>AcceptBirthdayGift_Loved</samp>,
<samp>AcceptBirthdayGift_Liked</samp>,
<samp>AcceptBirthdayGift_Neutral</samp>,
<samp>AcceptBirthdayGift_Disliked</samp>, or
<samp>AcceptBirthdayGift_Hated</samp>);</li>
<li><samp>AcceptBirthdayGift_Negative</samp> (hated or disliked gift) or
<samp>AcceptBirthdayGift_Positive</samp> (neutral, liked, or loved
gift);</li>
<li>for all items (via <samp>AcceptBirthdayGift</samp>).</li>
</ol></td>
</tr>
<tr>
<td><p><samp>AcceptBouquet</samp></p></td>
<td><p>Shown when the NPC accepts a <a href="bouquet" class="wikilink"
title="bouquet">bouquet</a> from the player. Defaults to a generic
dialogue.</p></td>
</tr>
<tr>
<td><p><samp>AcceptGift_&lt;id&gt;</samp><br />
<samp>AcceptGift_&lt;tag&gt;</samp><br />
<samp>AcceptGift_&lt;taste&gt;_&lt;context tag&gt;</samp><br />
<samp>AcceptGift_&lt;taste&gt;</samp><br />
<samp>AcceptGift</samp></p></td>
<td><p>Shown when receiving a non-birthday gift from the player. If
omitted, defaults to the dialogue in
<samp>Data/NPCGiftTastes</samp>.</p>
<p>The first matching dialogue is used in this order:</p>
<ol>
<li>by item ID (like <samp>AcceptGift_(O)128</samp>);</li>
<li>by context tag (like <samp>AcceptGift_category_fish</samp>);</li>
<li>by context tag and gift taste (see below for valid gift
tastes);</li>
<li>by gift taste (one of <samp>Loved</samp>, <samp>Liked</samp>,
<samp>Neutral</samp>, <samp>Disliked</samp>, <samp>Hated</samp>,
<samp>Positive</samp> (neutral/liked/loved), or <samp>Negative</samp>
(disliked/hated));</li>
<li>for all items (via <samp>AcceptGift</samp>).</li>
</ol></td>
</tr>
<tr>
<td><p><samp>MovieInvitation</samp></p></td>
<td><p>An NPC's response to being invited to the <a href="Movie_Theater"
class="wikilink" title="Movie Theater">Movie Theater</a>. If not
defined, the NPC will use a generic line from
<samp>Strings\Characters.xnb</samp> depending on the NPC's <a
href="Modding_NPC_data" class="wikilink"
title="manners">manners</a>.</p></td>
</tr>
<tr>
<td><p><samp>RejectBouquet_NotDatable</samp><br />
<samp>RejectBouquet_NpcAlreadyMarried</samp><br />
<samp>RejectBouquet_AlreadyAccepted_Engaged</samp><br />
<samp>RejectBouquet_AlreadyAccepted_Married</samp><br />
<samp>RejectBouquet_AlreadyAccepted</samp><br />
<samp>RejectBouquet_Divorced</samp><br />
<samp>RejectBouquet_VeryLowHearts</samp><br />
<samp>RejectBouquet_LowHearts</samp><br />
<samp>RejectBouquet</samp></p></td>
<td><p>Shown when the NPC rejects a <a href="bouquet" class="wikilink"
title="bouquet">bouquet</a>. A specific dialogue is shown if
possible:</p>
<ul>
<li><samp>RejectBouquet_NotDatable</samp>: the NPC isn't
romanceable.</li>
<li><samp>RejectBouquet_NpcAlreadyMarried</samp>: the NPC is already
married to another player. You can use <samp>{0}</samp> in the dialogue
for the other player's name.</li>
<li><samp>RejectBouquet_AlreadyAccpeted_*</samp>: the NPC already
accepted a bouquet from the player.</li>
<li><samp>RejectBouquet_Divorced</samp>: the NPC won't accept this
bouquet because you divorced them.</li>
<li><samp>RejectBouquet_VeryLowHearts</samp>: you have less than 4
hearts with the NPC.</li>
<li><samp>RejectBouquet_LowHearts</samp>: you have less than 8 hearts
with the NPC.</li>
</ul>
<p>If the specific dialogue isn't set, the game will use the
<samp>RejectBouquet</samp> dialogue (if set), else it'll default to
generic dialogue for each case.</p></td>
</tr>
<tr>
<td><p><samp>RejectGift_Divorced</samp></p></td>
<td><p>Shown when the NPC rejects a gift because you divorced
them.</p></td>
</tr>
<tr>
<td><p><samp>RejectItem_&lt;id&gt;</samp><br />
<samp>RejectItem_&lt;tag&gt;</samp></p></td>
<td><p>If set, the NPC will refuse to accept any matching item and show
this dialogue instead. This can be by item ID (like
<samp>RejectItem_(O)128</samp>) or context tag (like
<samp>RejectItem_category_fish</samp>). This can prevent gifting, movie
tickets, bouquets, mermaid pendants, etc. However it won't prevent
accepting an item for an active quest or special order.<br />
<br />
Note: These dialogue keys will take precedence over the gift acceptance
dialogue keys even if the rejection key is for a tag (less specific) and
the acceptance key is for the ID (more specific). This means you cannot
use these keys to reject a group of items (via a tag like
<samp>category_gem</samp>, for example) and then use an
<samp>AcceptGift_&lt;id&gt;</samp> to accept only one item from within
that group. Instead, you must individually reject all the unwanted items
within that group.</p></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>''(Obsolete)'' give_pendant</samp></p></td>
<td><p>Would show when an NPC accepted a <a href="Mermaid&#39;s_Pendant"
class="wikilink" title="mermaid&#39;s pendant">mermaid's pendant</a>
pre-1.6 update. As a workaround, add
<samp>&lt;NPCInternalName&gt;_Engaged</samp> as an entry to
Strings/StringsFromCSFiles instead.</p></td>
</tr>
<tr>
<td><p><samp>RejectMermaidPendant_AlreadyAccepted_Engaged</samp><br />
<samp>RejectMermaidPendant_AlreadyAccepted_Married</samp><br />
<samp>RejectMermaidPendant_AlreadyAccepted</samp><br />
<samp>RejectMermaidPendant_Divorced</samp><br />
<samp>RejectMermaidPendant_NeedHouseUpgrade</samp><br />
<samp>RejectMermaidPendant_NotDatable</samp><br />
<samp>RejectMermaidPendant_NpcWithSomeoneElse</samp><br />
<samp>RejectMermaidPendant_PlayerWithSomeoneElse</samp><br />
<samp>RejectMermaidPendant_Under8Hearts</samp><br />
<samp>RejectMermaidPendant_Under10Hearts</samp><br />
<samp>RejectMermaidPendant_Under10Hearts_AskedAgain</samp><br />
<samp>RejectMermaidPendant</samp></p></td>
<td><p>Shown when the NPC rejects a <a href="Mermaid&#39;s_Pendant"
class="wikilink" title="mermaid&#39;s pendant">mermaid's
pendant</a>.</p>
<p>A specific dialogue is shown if possible. The cases are checked in
this order:</p>
<ol>
<li><samp>RejectMermaidPendant_AlreadyAccepted_*</samp>: the player
gives a mermaid's pendant to an NPC who already accepted one from
them.</li>
<li><samp>RejectMermaidPendant_PlayerWithSomeoneElse</samp>: the player
is already engaged or married to someone else. You can use
<samp>{0}</samp> in the dialogue for the player's spouse name.</li>
<li><samp>RejectMermaidPendant_NotDatable</samp>: the NPC isn't
romanceable.</li>
<li><samp>RejectMermaidPendant_Divorced</samp>: you divorced them, so
they won't accept gifts or proposals from you.</li>
<li><samp>RejectMermaidPendant_NpcWithSomeoneElse</samp>: the NPC is
already engaged or married to someone else. You can use <samp>{0}</samp>
in the dialogue for the other player's name.</li>
<li><samp>RejectMermaidPendant_Under8Hearts</samp>: you have under 8
hearts with the NPC.</li>
<li><samp>RejectMermaidPendant_Under10Hearts</samp>: you have under 10
hearts with the NPC.</li>
<li><samp>RejectMermaidPendant_Under10Hearts_AskedAgain</samp>: you have
under 10 hearts with the NPC, and asked again after they already said
no. (Defaults to the previous dialogue if not set.)</li>
<li><samp>RejectMermaidPendant_NeedHouseUpgrade</samp>: you need to
upgrade your house before they can accept.</li>
</ol>
<p>If the specific dialogue isn't set, the game will use the
<samp>RejectMermaidPendant</samp> dialogue (if set), else it'll default
to generic dialogue for each case.</p></td>
</tr>
<tr>
<td><p><samp>RejectMovieTicket_AlreadyInvitedBySomeoneElse</samp><br />
<samp>RejectMovieTicket_AlreadyWatchedThisWeek</samp><br />
<samp>RejectMovieTicket_Divorced</samp><br />
<samp>RejectMovieTicket_DontWantToSeeThatMovie</samp><br />
<samp>RejectMovieTicket</samp></p></td>
<td><p>Show when the NPC rejects a <a href="Movie_Ticket"
class="wikilink" title="movie ticket">movie ticket</a>.</p>
<p>A specific dialogue is shown if possible:</p>
<ul>
<li><samp>RejectMovieTicket_AlreadyInvitedBySomeoneElse</samp>: someone
else already invited the NPC to a movie. You can use <samp>{0}</samp> in
the dialogue for the other player's name.</li>
<li><samp>RejectMovieTicket_AlreadyWatchedThisWeek</samp>: the NPC
already watched a movie this week.</li>
<li><samp>RejectMovieTicket_Divorced</samp>: you divorced the NPC, so
they won't accept gifts from you.</li>
<li><samp>RejectMovieTicket_DontWantToSeeThatMovie</samp>: the movie
data marks that NPC as unwilling to watch it (e.g. kids for horror
movies).</li>
</ul>
<p>If the specific dialogue isn't set, the game will use the
<samp>RejectMovieTicket</samp> dialogue (if set), else it'll default to
generic dialogue for each case.</p></td>
</tr>
<tr>
<td><p><samp>RejectRoommateProposal_AlreadyAccepted</samp><br />
<samp>RejectRoommateProposal_NpcWithSomeoneElse</samp><br />
<samp>RejectRoommateProposal_PlayerWithSomeoneElse</samp><br />
<samp>RejectRoommateProposal_LowFriendship</samp><br />
<samp>RejectRoommateProposal_SmallHouse</samp><br />
<samp>RejectRoommateProposal</samp></p></td>
<td><p><em>(Optional)</em> Shown when the NPC rejects a roommate
proposal because the player doesn't meet a specific requirement:</p>
<ul>
<li><samp>AlreadyAccepted</samp>: the NPC is already a roommate with
this player.</li>
<li><samp>NpcWithSomeoneElse</samp>: the NPC is already a roommate with
another player.</li>
<li><samp>PlayerWithSomeoneElse</samp>: the player making the proposal
already has a roommate.</li>
<li><samp>LowFriendship</samp>: the player doesn't have 10+ <a
href="Friendship" class="wikilink" title="hearts">hearts</a> with the
NPC.</li>
<li><samp>SmallHouse</samp>: the player hasn't upgraded their house
yet.</li>
</ul>
<p>If the specific dialogue isn't set, the game will use the
<samp>RejectRoommateProposal</samp> dialogue (if set), else it'll
default to generic dialogue.</p></td>
</tr>
<tr>
<td><p><samp>accept_&lt;item_id&gt;</samp><br />
<samp>reject_&lt;item_id&gt;</samp></p></td>
<td><p><em>(Obsolete)</em> These are specialized keys meant for the
pirate lady quest. Use <samp>AcceptGift_*</samp> and
<samp>RejectItem_*</samp> instead.</p></td>
</tr>
</tbody>
</table>

##### Festival dialogue

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Fair_Judging</samp></p></td>
<td><p>Shown at the <a href="Stardew_Valley_Fair" class="wikilink"
title="Stardew Valley Fair">Stardew Valley Fair</a> while Lewis is
judging the grange displays. If omitted, the NPC will keep their normal
festival dialogue.</p>
<p>If this is set without <samp>Fair_Judged*</samp>, the NPC will keep
this dialogue after judging is done.</p></td>
</tr>
<tr>
<td><p><samp>Fair_Judged_PlayerLost_PurpleShorts</samp><br />
<samp>Fair_Judged_PlayerLost_Skipped</samp><br />
<samp>Fair_Judged_PlayerLost</samp><br />
<samp>Fair_Judged_PlayerWon</samp><br />
<samp>Fair_Judged</samp></p></td>
<td><p>Shown at the <a href="Stardew_Valley_Fair" class="wikilink"
title="Stardew Valley Fair">Stardew Valley Fair</a> after Lewis finishes
judging the grange displays.</p>
<p>The first matching dialogue is used in this order:</p>
<ol>
<li><samp>Fair_Judged_PlayerLost_PurpleShorts</samp>: the player put the
<a href="Secrets#Lucky_Purple_Shorts" class="wikilink"
title="lucky purple shorts">lucky purple shorts</a> in their display
(which is an automatic loss). Defaults to
<samp>Fair_Judged_PlayerLost</samp> if omitted.</li>
<li><samp>Fair_Judged_PlayerLost_Skipped</samp>: the player didn't put
anything in their display. Defaults to
<samp>Fair_Judged_PlayerLost</samp> if omitted.</li>
<li><samp>Fair_Judged_PlayerLost</samp> or
<samp>Fair_Judged_PlayerWon</samp>: the player didn't/did win first
place. Defaults to <samp>Fair_Judged</samp> if omitted.</li>
<li><samp>Fair_Judged</samp>: shown if a more specific dialogue didn't
match. If omitted, the NPC will keep their current dialogue.</li>
</ol></td>
</tr>
<tr>
<td><p><samp>FlowerDance_Accept_Roommate</samp><br />
<samp>FlowerDance_Accept_Spouse</samp><br />
<samp>FlowerDance_Accept</samp></p></td>
<td><p>Shown at the <a href="Flower_Dance" class="wikilink"
title="Flower Dance">Flower Dance</a> when the NPC agrees to dance. The
game will prefer the <samp>_Roommate</samp> (if roommates) or
<samp>_Spouse</samp> (if married) variant if applicable, else it'll
check for the normal key. If omitted, defaults to a generic accept
dialogue.</p></td>
</tr>
<tr>
<td><p><samp>FlowerDance_Decline</samp><br />
<s><samp>danceRejection</samp></s></p></td>
<td><p>Shown at the <a href="Flower_Dance" class="wikilink"
title="Flower Dance">Flower Dance</a> when the NPC declines to dance. (A
different dialogue is used if they've already agreed to dance with
another player.)</p>
<p><samp>danceRejection</samp> is a deprecated older name (which still
works as a fallback).</p></td>
</tr>
<tr>
<td><p><samp>WinterStar_GiveGift_Before_Roommate</samp><br />
<samp>WinterStar_GiveGift_Before_Spouse</samp><br />
<samp>WinterStar_GiveGift_Before</samp><br />
<samp>WinterStar_GiveGift_After_Roommate</samp><br />
<samp>WinterStar_GiveGift_After_Spouse</samp><br />
<samp>WinterStar_GiveGift_After</samp></p></td>
<td><p>Shown at the <a href="Feast_of_the_Winter_Star" class="wikilink"
title="Feast of the Winter Star">Feast of the Winter Star</a> when the
NPC gives the player their gift (before and after the player opens it).
The game will prefer the <samp>_Roommate</samp> (if roommates) or
<samp>_Spouse</samp> (if married) variant if applicable, else it'll
check for the normal key. If omitted, the before/after dialogues each
separately default to a generic translation for all NPCs.</p></td>
</tr>
<tr>
<td><p><samp>WinterStar_ReceiveGift_&lt;id&gt;</samp><br />
<samp>WinterStar_ReceiveGift_&lt;tag&gt;</samp><br />
<samp>WinterStar_ReceiveGift</samp></p></td>
<td><p>Shown at the <a href="Feast_of_the_Winter_Star" class="wikilink"
title="Feast of the Winter Star">Feast of the Winter Star</a> when
receiving their gift from the player. This can be by item ID (like
<samp>WinterStar_ReceiveGift_(O)128</samp>), context tag (like
<samp>WinterStar_ReceiveGift_category_fish</samp>), or for any item
(like <samp>WinterStar_ReceiveGift</samp>). If omitted, defaults to the
generic translation for all NPCs.</p></td>
</tr>
</tbody>
</table>

##### Location dialogue

Otherwise the game will choose dialogue in this order.

Variants:

- Each key can optionally be prefixed with a
  <a href="#Seasons" class="wikilink" title="season name">season name</a>,
  like `springMountain_47_23`.

The game will check variants in this order: `<season><key>`, and
`<key>`. The variants aren't listed below for simplicity. Unlike daily
dialogue, location dialogue is endlessly repeatable as long as the
trigger conditions are fulfilled, *e.g.,* Being in the location. They
will not remove daily dialogue from an npc's dialogue rotation, but will
merely overwrite it when the NPC is in the specified location.

**Note:** For location dialogue to work, an NPC must be giftable. If the
NPC is not giftable (either because they lack gift tastes or have
`CanSocialize` set to false), one workaround is to set their `SocialTab`
field to `AlwaysShown`.

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>&lt;location&gt;_&lt;x&gt;_&lt;y&gt;</samp></p></td>
<td><p>Dialogue shown in the named location when the NPC is standing at
tile position &lt;x&gt;, &lt;y&gt;.<br />
<small>Example: <samp>Mountain_47_23: "I come here for the peace and
quiet."</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;location&gt;_&lt;dayName&gt;</samp></p></td>
<td><p>Dialogue shown in the named location on the given <a
href="#Days_of_week" class="wikilink" title="day of week">day of
week</a>.<br />
<small>Example: <samp>Saloon_Fri: "Business has been really good
tonight. I'm pleased."</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;location&gt;&lt;hearts&gt;</samp></p></td>
<td><p>Dialogue shown in the named location if you have at least
&lt;hearts&gt; hearts with them. The &lt;hearts&gt; will be checked in
the order 10, 8, 6, 4, 2 (no other value will be recognised).<br />
<small>Example: <samp>Saloon8: "Hi there @. I'm glad to see you! You're
always welcome here."</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;location&gt;</samp></p></td>
<td><p>Dialogue shown in the named location.<br />
<small>Example: <samp>Saloon: "Now that I'm here I can finally relax and
socialize a bit."</samp></small></p>
<ul>
<li>Note: Location dialogue will be accessible even if the NPC is only
walking through the specified map unlike schedule strings that will only
be accessible once the schedule end location is reached.</li>
</ul></td>
</tr>
</tbody>
</table>

##### Generic dialogue

Otherwise the game will choose a dialogue using one of these key formats
(in precedence order):

1.  `<season>_<key>_inlaw_<spouse>`
2.  `<season>_<key>`
3.  `<key>_inlaw_<spouse>`
4.  `<key>`

For each variation above: `<season>` is a
<a href="#Seasons" class="wikilink" title="season name">season name</a>
(like `spring_14`); `_inlaw_<spouse>` matches if the player is married
to the named NPC, regardless of whether the speaking NPC is related to
the named one (like `Sat_inlaw_Abigail`); and `<key>` is one of the
formats listed below.

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>&lt;dayOfMonth&gt;</samp></p></td>
<td><p>Dialogue shown on the given day of month in the <strong>first
year only.</strong><br />
<strong>WARNING: this first-year-only behavior is different from other
keys and often catches unsuspecting modders!</strong> You usually want
<samp>&lt;dayOfMonth&gt;_*</samp> instead.<br />
<small>Example: <samp>10: "Did you watch the game last night?#$b#Or
wait, do you even have a TV set...?"</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;dayOfMonth&gt;_&lt;firstOrLaterYear&gt;</samp></p></td>
<td><p>Dialogue shown on the given day of month in the <a
href="#First_later_year" class="wikilink"
title="first/later year">first/later year</a>.<br />
<small>Example: <samp>2_1: "My husband Kent is a soldier, working
overseas. That's why he's not here right now.#$b#I know he'll come back
safe once his tour is over</p></td>
</tr>
<tr>
<td><p><samp>&lt;dayOfMonth&gt;_*</samp></p></td>
<td><p>Dialogue shown on the given day of month in any year.<br />
<small>Example: <samp>18_*: "I try not to make too much noise down here.
Imagine if the townspeople heard my weird sounds coming from the sewer
drain..."</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;dayOfWeek&gt;&lt;hearts&gt;_&lt;firstOrLaterYear&gt;</samp></p></td>
<td><p>Dialogue shown on the given <a href="#Days_of_week"
class="wikilink" title="day of week">day of week</a> if you have at
least &lt;hearts&gt; hearts with them, in the <a
href="#First_later_year" class="wikilink"
title="first/later year">first/later year</a>. The &lt;hearts&gt; will
be checked in the order 10, 8, 6, 4, 2 (no other value will be
recognised).<br />
<small>Example: <samp>Thu2_2: "Well, my Dad is back. Have you met
him?#$b#I'm just glad he's okay."</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;dayOfWeek&gt;&lt;hearts&gt;</samp></p></td>
<td><p>Dialogue shown on the given <a href="#Days_of_week"
class="wikilink" title="day of week">day of week</a> if you have at
least &lt;hearts&gt; hearts with them. The &lt;hearts&gt; will be
checked in the order 10, 8, 6, 4, 2 (no other value will be
recognised).<br />
<small>Example: <samp>Sun4: "Hey, @.#$e#How's your day
going?"</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;dayOfWeek&gt;_&lt;firstOrLaterYear&gt;</samp></p></td>
<td><p>Dialogue shown on the given <a href="#Days_of_week"
class="wikilink" title="day of week">day of week</a> in the <a
href="#First_later_year" class="wikilink"
title="first/later year">first/later year</a>.<br />
<small>Example: <samp>Sat_1: "Dad's coming back soon!#$b#I hope he
brings me some toys.$u"</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;dayOfWeek&gt;</samp></p></td>
<td><p>Dialogue shown on the given <a href="#Days_of_week"
class="wikilink" title="day of week">day of week</a>.<br />
<small>Example: <samp>Mon: "Oh, hey. Taking a break from
work?"</samp></small></p></td>
</tr>
</tbody>
</table>

##### Specific NPCs

<table>
<thead>
<tr>
<th><p>NPC</p></th>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="Gil" class="wikilink" title="Gil">Gil</a></p></td>
<td><p><samp>ComeBackLater</samp><br />
<samp>Snoring</samp></p></td>
<td><p>Gil's dialogue when you haven't completed any new Adventure Quest
goals. <samp>ComeBackLater</samp> will be shown once, and all subsequent
dialogues will show <samp>Snoring</samp>.</p></td>
</tr>
</tbody>
</table>

#### Rain dialogue

`Characters\Dialogue\rainy.xnb` contains one dialogue entry per NPC.
There's a roughly 50% chance they'll use this dialogue if a special or
location dialogue doesn’t match, it's raining, and you're not married to
or divorced from them.

#### Marriage dialogue

`Characters\Dialogue\MarriageDialogue.xnb` contains dialogue text for
all spouses, and each NPC may optionally have their own dialogue file
like `Characters\Dialogue\MarriageDialogueAbigail.xnb`. When looking up
a dialogue key, it will use the one in the NPC's file if it exists, else
the one in the generic file, else a default text (usually blank).

Each dialogue entry has a key with one of these formats:

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>&lt;season&gt;_&lt;day&gt;</samp></p></td>
<td><p>Dialogue shown when the day starts, if &lt;season&gt; and
&lt;day&gt; match the current date.<br />
<small>Example: <samp>fall_1</samp>: "<em>The scent is unmistakable...
mushroom, rotting leaves, pumpkin. It's fall, alright. Isn't it
lovely?</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>patio_&lt;spouse&gt;</samp></p></td>
<td><p>Dialogue shown when the NPC is standing on the patio.</p></td>
</tr>
<tr>
<td><p><samp>&lt;weather&gt;_Day_&lt;random&gt;</samp></p></td>
<td><p>Daily dialogue added when the day starts, based on the
&lt;weather&gt; (<samp>Rainy</samp> if it's raining, else
<samp>Indoor</samp> even if they're not indoors) and &lt;random&gt; (a
random number between 0 and 4). If the game chooses a &lt;random&gt;
value that doesn't have a dialogue, it'll use the default text
instead.</p></td>
</tr>
<tr>
<td><p><samp>Rainy_Night_&lt;random&gt;</samp></p></td>
<td><p>Daily dialogue in the farmhouse after 6pm when it's raining.
&lt;random&gt; is a number between 0–5 inclusively <em>or</em> the NPC
name, each of which has an equal chance of being randomly chosen. If the
game chooses a &lt;random&gt; value that doesn't have a dialogue, it'll
use the default text instead.<br />
<small>Example: <samp>Rainy_Night_3</samp>: "<em>On nights like this, I
like to turn the light down low and just
listen...$8</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>Indoor_Night_&lt;random&gt;</p></td>
<td><p>Daily dialogue in the farmhouse after 6pm when it's <em>not</em>
raining. &lt;random&gt; is a number between 0–4 inclusively <em>or</em>
the NPC name, each of which has an equal chance of being randomly
chosen. If the game chooses a &lt;random&gt; value that doesn't have a
dialogue, it'll use the default text instead.</p></td>
</tr>
<tr>
<td><p><samp>funLeave_&lt;spouse&gt;</samp></p></td>
<td><p>Dialogue used when leaving the farmhouse (except when using the
hardcoded marriageJob schedule key)</p></td>
</tr>
<tr>
<td><p><samp>jobLeave_&lt;spouse&gt;</samp></p></td>
<td><p>Dialogue used when leaving to go to their job. Only used for
Maru, Penny, and Harvey.</p></td>
</tr>
<tr>
<td><p><samp>funReturn_&lt;spouse&gt;</samp></p></td>
<td><p>Dialogue shown after 1pm when they enter the farmhouse but before
reaching their target position (except when using the hardcoded
marriageJob schedule key)<br />
<small>Example: <samp>funReturn_Abigail</samp>: "<em>Hey! Did you have a
good day? Mine went well. It was refreshing to take a
walk.$h</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>jobReturn_&lt;spouse&gt;</samp></p></td>
<td><p>Dialogue shown after 1pm when for Maru, Penny, and Harvey enter
the farmhouse but before reaching their target position, when using the
hardcoded marriageJob schedule key.<br />
<small>Example: <samp>jobReturn_Penny</samp>: "<em>#$c .5#Good evening.
My day was fine, thanks! How was yours?$h#$e#Jas and Vincent weren't
behaving very well today. I'm still all wound
up...</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>&lt;season&gt;_&lt;spouse&gt;</samp></p></td>
<td><p>Dialogue shown at 9+ heart levels with a 5% chance each
day.<br />
<small>Example: <samp>fall_Abigail</samp>: "<em>Do I smell pumpkin on
you? Maybe I'm just dreaming...$h</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>Outdoor_&lt;spouse&gt;</samp></p></td>
<td><p>Dialogue shown on the farm with a 20% chance.<br />
<small>Example: <samp>Outdoor_Abigail</samp>: "<em>I'm just going to
hang out here, okay?#$e#There's a lot of interesting bugs and things out
here. *chuckle*$h</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>Outdoor_&lt;random&gt;</samp></p></td>
<td><p>Dialogue shown on the farm with an 80% chance. &lt;random&gt; is
a number 0–4, used to randomly select an entry.<br />
<small>Example: <samp>Outdoor_3</samp>: "<em>It's pretty cool that we
have a cave on our property. It's something I always dreamed
about.$h</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>spouseRoom_&lt;spouse&gt;</samp></p></td>
<td><p>Dialogue shown when the NPC is in their room.<br />
<small>Example: <samp>spouseRoom_Abigail</samp>: "<em>$c .5#I got up a
little before you and fed David Jr. He's very active this morning.#$e#I
hope you don't mind the guinea pig smell."</em></small></p></td>
</tr>
<tr>
<td><p><samp>OneKid_&lt;random&gt;</samp></p></td>
<td><p>Dialogue shown when standing in the kitchen, if they have one
child. &lt;random&gt; is a number 0–4, used to randomly select an
entry.<br />
<small>Example: <samp>OneKid_1</samp>: "<em>I wonder if %kid1 will grow
up to be a farmer like you?</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>TwoKids_&lt;random&gt;</samp></p></td>
<td><p>Dialogue shown when standing in the kitchen, if they have two
children. &lt;random&gt; is a number 0–4, used to randomly select an
entry.<br />
<small>Example: <samp>TwoKids_2</samp>: "<em>I had a dream that %kid2
will grow up to be a famous monster hunter. I've already been thinking
about a little armor set.</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>NoBed_&lt;random&gt;</samp></p></td>
<td><p>Dialogue shown if there was no bed available the previous night.
&lt;random&gt; is a number 0–3, used to randomly select an entry.<br />
<small>Example: <samp>NoBed_3</samp>: "<em>Did something happen to our
bed...?$s</em>"</small></p></td>
</tr>
<tr>
<td><p><samp>&lt;affection&gt;_&lt;random&gt;</samp></p></td>
<td><p>Dialogue shown inside the farmhouse between 11am and 6pm,
<em>or</em> when the day starts if a different dialogue isn't selected.
&lt;affection&gt; is randomly <samp>Bad</samp> or <samp>Neutral</samp>
if they have less than 9 hearts; 50% chance of <samp>Good</samp> if you
have 10 hearts, 87.5% chance of <samp>Good</samp> if you have 11 hearts,
and 99.4% chance of <samp>Good</samp> if you have 12+ hearts; else
<samp>Neutral</samp> &lt;random&gt; is a number 0–9, used to randomly
select an entry.<br />
<small>Example: <samp>Good_5</samp>: "<em>I was just admiring the
mermaid's pendant you gave me... I'll proudly wear this to my
grave.$l</em>"</small></p></td>
</tr>
</tbody>
</table>

#### Roommate dialogue

The game's
<a href="marriage" class="wikilink" title="marriage">marriage</a> logic
can treat any NPC (including custom NPCs), not just
<a href="Krobus" class="wikilink" title="Krobus">Krobus</a>, as a
roommate.

These keys apply before they move in:

<table>
<thead>
<tr>
<th><p>content file</p></th>
<th><p>key</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Strings/StringsFromCSFiles</samp></p></td>
<td><p><samp>&lt;NPC name&gt;_EngagedRoommate</samp></p></td>
<td><p>The NPC's roommate proposal accept dialogue.<br />
⚠ Ignored if you don't specify <samp>Data/EngagementDialogue:&lt;NPC
name&gt;Roommate0</samp>.<br />
For example: <em>A Void Ghost pendant! How did you...?$3#$b#Oh,
wow.$7#$b#@... yes, I'll come live with you, if you like. But we have to
keep it secret from everyone.#$b#I'll be at your house in a few days...
okay?$h</em></p></td>
</tr>
<tr>
<td><p><samp>Strings/Characters</samp></p></td>
<td><p><samp>MovieInvite_NoTheater</samp></p></td>
<td><p>The NPC's roommate proposal rejection text when you don't meet
the requirements (<em>i.e.,</em> min friendship + house upgrade level,
and not already having a roommate/spouse). This is the same dialogue
used when you can't invite someone to the movies.</p></td>
</tr>
<tr>
<td><p><samp>Data/EngagementDialogue</samp></p></td>
<td><p><samp>&lt;NPC name&gt;Roommate0</samp><br />
<samp>&lt;NPC name&gt;Roommate1</samp></p></td>
<td><p>The NPC's normal dialogue after accepting the proposal, but
before moving in. The <samp>Roommate0</samp> variant is always used on
the day the NPC accepted; on subsequent days the NPC randomly chooses
<samp>Roommate0</samp> or <samp>Roommate1</samp>. If the
<samp>Roommate0</samp> variant isn't defined, the NPC will use the
normal <samp>&lt;NPC Name&gt;0</samp> and <samp>&lt;NPC Name&gt;1</samp>
keys. If the <samp>Roommate0</samp> variant is defined,
<samp>Roommate1</samp> must be set too to avoid errors.<br />
For example: <em>@... I'm afraid we'll have to keep this a secret...
Neither my people nor yours would accept us living
together.</em></p></td>
</tr>
</tbody>
</table>

And after they move in:

| content file | key | effect |
|----|----|----|
| `Characters/Dialogue/MarriageDialogue<NPC name>Roommate` | *all keys* | Equivalent to `Characters/Dialogue/MarriageDialogue<NPC name>`, but only applies if the NPC is a roommate. If the file exists, it completely replaces the spouse version; otherwise the game defaults to the spouse version. |
| `Characters/Dialogue/MarriageDialogue` | `*Roommate` | Keys with the `Roommate` suffix take priority if they exist (only in this file, not the `MarriageDialogue<NPC name>` files). |
| `Data/Festivals/*` | `<NPC name>_roommate` | The NPC's normal dialogue at the festival if they're a roommate. If the key isn't defined, they'll use `<NPC name>_spouse` instead. |

And for other NPCs:

| content file | key | effect |
|----|----|----|
| `Characters/Dialogue/*` | `*_roommate_*` | Equivalent to the `*_inlaw_*` infix in <a href="Modding_Dialogue#Generic_dialogue" class="wikilink"
title="generic dialogue">generic dialogue</a>, used if you're a roommate with the NPC. If not defined, the game will fallback to the non-infixed dialogue (it won't use the `*_inlaw_*` variant). |

### Data directory

#### Engagement dialogue

Similar to the rain dialogue, `Data\EngagementDialogue.xnb` contains
entries in the form of `<NPC>0` and `<NPC>1`, which are used when you
are engaged but not yet married to an NPC, or, in the case of a
roommate, when they have been invited but have not yet moved in.

#### Event files

`Data\Events\*.xnb` contains event scripts, including any dialogue in
the event (see <a href="Modding_Event_data" class="wikilink"
title="Modding:Event data">Modding:Event data</a>).

#### Extra dialogue

`Data\ExtraDialogue.xnb` contains miscellaneous strings, some of which
are NPC specific:

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>PurchasedItem_*</samp></p></td>
<td><p>Randomly shown by a non-child town NPC after you sell an edible
item to a shop. These keys are hardcoded, and you can't add new keys
with a similar pattern.</p>
<p>For keys with a number infix (like
<samp>PurchasedItem_5_Cooking</samp>), the number is selected as
such:</p>
<ul>
<li>If the NPC is marked as rude in their data, they use 3.</li>
<li>Otherwise they randomly choose 1-5.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Town_DumpsterDiveComment_Child</samp><br />
<samp>Town_DumpsterDiveComment_Teen</samp><br />
<samp>Town_DumpsterDiveComment_Adult</samp><br />
<samp>Town_DumpsterDiveComment_Linus</samp></p></td>
<td><p>Shown when an NPC catches you rummaging through trash cans,
depending on the NPC's age. Linus has his own dialogue, but other NPCs
don't.</p></td>
</tr>
<tr>
<td><p><samp>SummitEvent_Dialogue3_&lt;spouse&gt;</samp></p></td>
<td><p>Shown for your NPC spouse near the start of the <a
href="perfection" class="wikilink" title="perfection">perfection</a>
cutscene.</p></td>
</tr>
</tbody>
</table>

#### Movie theater dialogue

An NPC's reaction to a movie is stored in `Data\MoviesReactions.xnb`,
which is structured far differently from every other dialogue file. See
<a href="Modding_Movie_theater_data" class="wikilink"
title="Modding:Movie theater data">Modding:Movie theater data</a> for
more details.

### Strings directory

#### Animation descriptions

`Strings\animationDescriptions.xnb` contains short bits of dialogue to
go with certain schedule points. **Not to be confused to
`Data\animationDescriptions.xnb`, which contains the data of animations,
rather than the strings for their description.**

#### Characters

`Strings\Characters.xnb` contains miscellaneous dialogue, some of which
is NPC-specific:

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>MovieInvite_Spouse_&lt;NPC name&gt;</samp></p></td>
<td><p>Shown when the NPC accepts a <a href="Movie_Ticket"
class="wikilink" title="movie ticket">movie ticket</a> when they're
married to you. If missing, defaults to a
<samp>MovieInvite_Invited_*</samp> key.</p></td>
</tr>
<tr>
<td><p><samp>MovieInvite_Invited_&lt;NPC name&gt;</samp><br />
<samp>MovieInvite_Invited_&lt;manner&gt;</samp><br />
<samp>MovieInvite_Invited_&lt;socialAnxiety&gt;</samp><br />
<samp>MovieInvite_Invited_&lt;optimism&gt;</samp><br />
<samp>MovieInvite_Invited_&lt;age&gt;</samp><br />
<samp>MovieInvite_Invited</samp></p></td>
<td><p>Shown when the NPC accepts a <a href="Movie_Ticket"
class="wikilink" title="movie ticket">movie ticket</a>. The NPC will use
the first key that exists in the order listed here.</p>
<p>The &lt;manner&gt;, &lt;socialAnxiety&gt;, and &lt;optimism&gt;
values are those specified in the <a href="Modding_NPC_data"
class="wikilink" title="NPC&#39;s equivalent data fields">NPC's
equivalent data fields</a>. The &lt;age&gt; value is one of
<samp>Child</samp>, <samp>Teen</samp>, or <samp>Adult</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Phone_*</samp></p></td>
<td><p>Shown when calling a shop owner NPC on the <a href="telephone"
class="wikilink" title="telephone">telephone</a>. These keys are
hardcoded, so new keys with the same pattern will be ignored.</p></td>
</tr>
</tbody>
</table>

#### Events

`Strings\Events.xnb` contains miscellaneous dialogue related to events
and festivals, some of which is NPC-specific.

#### Speech bubbles

`Strings\SpeechBubbles.xnb` contains dialogue spoken by NPCs through
speech bubbles when **the player** enters a given location. This is
distinct from the `<location>_Entry` field in an NPC's
`Characters\Dialogue\*.xnb` file, which is triggered when **the NPC**
enters a given location.

These keys are hardcoded, so new keys with the same pattern will be
ignored.

#### Strings from CS files

`Strings\StringsFromCSFiles.xnb` contains miscellaneous strings, such as
dialogue that's shared between multiple characters, dialogue for some
hardcoded events like marriage, etc.

The file has entries in the form `"<key>": "dialogue string"`, where the
key is an arbitrary unique identifier. These must exactly match the key
expected by the game, but the keys are just unique identifiers — even
though most keys look like `<file name>.<line number>`, that's just the
convention originally used to assign IDs and it has no meaning or effect
(nor does it even necessarily match the current file name or line
number).

In most situations, if the game is unable to find a string for an NPC to
say, it will default to `NPC.cs.4061` (English version: "Hi.").

Some other useful NPC-specific strings stored here are as follows:

| key format | description |
|----|----|
| `<NPC name>_AfterWedding` | Shown after marrying an NPC, when you talk to them on the farm on the same day. |
| `<NPC name>_Engaged`</br>`<NPC name>_EngagedRoommate` | Shown when the NPC accepts an engagement item (e.g. <a href="Mermaid&#39;s_Pendant" class="wikilink"
title="mermaid&#39;s pendant">mermaid's pendant</a> or <a href="Void_Ghost_Pendant" class="wikilink"
title="void ghost pendant">void ghost pendant</a> for vanilla NPCs), after accept/reject checks are complete. |

## Algorithm

The game finds dialogue as follows:

1.  Event dialogue is read from the appropriate event commands (see
    <a href="Modding_Event_data" class="wikilink"
    title="Modding:Event data">Modding:Event data</a>).
2.  Location-specific dialogue is read from
    `StringsFromCSFiles <location>.cs`.
3.  Else character dialogue is read from the character-specific files.
4.  If no dialogues were found, the game resorts to hardcoded dialogue
    from the `StringsFromCSFiles` files (specifically keys prefixed with
    `NPC.cs` NPC.cs).

## Format

Dialogue text can contain tokens and commands which control the dialogue
box, change the text (*e.g.,* switch between gender-specific strings),
inject values, etc. These are parsed by the `Dialogue` class.

### Gender switch

<table>
<thead>
<tr>
<th><p>syntax</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>${male^female}$</samp><br />
<samp>${male^female^non-binary}$</samp></p></td>
<td><p>Change text depending on the player's gender. The non-binary
value is only used if a mod overrides the player's gender, since the
in-game UI only allows male or female.</p>
<p>This is applied before most other commands or parsing, so it can
safely be used in cases where <samp>^</samp> might have a different
meaning (e.g. mail text). You can also use <samp>¦</samp> instead of
<samp>^</samp>, in which case any <samp>^</samp> characters are left
as-is.</p>
<p><em>Example: <code>Ahoy there ${lad^lass}$!</code></em></p></td>
</tr>
</tbody>
</table>

### Special tokens

<table>
<thead>
<tr>
<th><p>character</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>#</samp></p></td>
<td><p>Separates two commands in a dialogue string.</p></td>
</tr>
<tr>
<td><p><samp>{</samp></p></td>
<td><p>TODO. Stands for "breakSpecialCharacter".</p></td>
</tr>
<tr>
<td><p><samp>%</samp></p></td>
<td><p>Turns the dialogue box into a generic text box.<br />
<em>Example: <code>"%Abigail is lost in her music."</code></em></p></td>
</tr>
<tr>
<td><p><samp>*</samp></p></td>
<td><p>Stands for "quickResponseDelineator". Converted in code to
<samp>#$b#</samp>. Use in <samp>$y</samp> (dialogueQuickReponse) to
achieve the effects of <samp>#$b#</samp>. You can use double asterisks
<samp>**</samp> to escape a literal asterisk.</p></td>
</tr>
<tr>
<td><p><samp></p></td>
<td><p></samp></p></td>
</tr>
<tr>
<td><p><samp>^</samp></p></td>
<td><p><em>(Deprecated)</em> Most code should use the <a
href="#Gender_switch" class="wikilink" title="newer ${...} form">newer
<samp>${...}</samp> form</a> above, which is supported in more
places.</p>
<p>Gender switch character. The text before it is shown for male
farmers, the text after it for female farmers.<br />
<em>Example:
<code>Oh, good morning Mr. @!^Oh, good morning Ms. @!</code></em></p></td>
</tr>
</tbody>
</table>

### Portrait commands

These set the portrait shown in the dialogue box for the current line of
dialogue. If there's no portrait command, the neutral portrait is used.

Portraits are numbered left-to-right and top-to-bottom, starting at
`$0`. The first six portraits are standard, and can be identified by the
number (like `$2`) or a unique alias (like `$s`). All potential spouses
and many other characters have these six portraits, but it's not fully
consistent; for example, Caroline only has four.

| numbered | alias | description |
|----|----|----|
| `$0` |  | Use their neutral portrait. |
| `$1` | `$h` | Use their happy portrait. |
| `$2` | `$s` | Use their sad portrait. |
| `$3` | `$u` | Use their unique portrait. This is different for each NPC: grumpy (<a href="Abigail" class="wikilink" title="Abigail">Abigail</a>), holding football (<a href="Alex" class="wikilink" title="Alex">Alex</a>), angry (<a href="Caroline" class="wikilink" title="Caroline">Caroline</a>), sick (<a href="Governor" class="wikilink" title="Governor">Governor</a>), etc. |
| `$4` | `$l` | Use their love portrait. |
| `$5` | `$a` | Use their angry portrait. |
| `$<id>` |  | A custom portrait beyond the standard six. |

Portrait commands should be at the end of a dialogue line:


`"fall_Fri6": "When I was a little girl, my father abandoned us.$s#$b#I'm sorry to make things uncomfortable for you...$u#$e#Anyway... How's the farming life going?",`

### Dialogue commands

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>$action &lt;action&gt;</samp></p></td>
<td><p>Run a <a href="Modding_Trigger_actions" class="wikilink"
title="trigger action string">trigger action string</a>, like
<samp>$action AddMoney 500</samp> to add to the current player.</p></td>
</tr>
<tr>
<td><p><samp>$b</samp></p></td>
<td><p>Indicates pauses in dialogue, where the player will need to click
for the next part to load in a new dialogue box.</p></td>
</tr>
<tr>
<td><p><samp>$c
&lt;probability&gt;#&lt;text1&gt;#&lt;text2&gt;</samp></p></td>
<td><p>Show &lt;text1&gt; with a &lt;probability&gt; between 0 and 1;
otherwise, show &lt;text2&gt;. E.g. <code>$c 0.9</code> for a 90% chance
of &lt;text1&gt; and a 10% chance of &lt;text2&gt;. NOTE: Replacer
commands (see below) do not work in &lt;text1&gt;. This does not need to
be the first command in a dialogue string. It is unaffected by daily
luck.</p></td>
</tr>
<tr>
<td><p><samp>$d &lt;state
id&gt;#&lt;text1&gt;|&lt;text2&gt;</samp></p></td>
<td><p>Show one of two dialogue strings based on a predefined condition:
<samp>bus</samp> (whether the bus is repaired), <samp>joja</samp>
(whether the Joja Mart is still in business), <samp>cc</samp> or
<samp>communitycenter</samp> (whether the Community Center is
accessible), or <samp>kent</samp> (whether <a href="Kent"
class="wikilink" title="Kent">Kent</a> has returned to the valley). The
dialogue string must start with <samp>$d</samp>, everything up to the
first <code>|</code> symbol is shown if the condition matches, and
everything after that is shown if the condition doesn't match.</p>
<p>For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Mon2&quot;</span><span class="op">:</span> <span class="st">&quot;$d kent#Yesterday I visited Yoba&#39;s Altar to give thanks for my husband&#39;s safe return.|Yesterday I visited Yoba&#39;s Altar to ask for my husband&#39;s safe return.#$e#I&#39;m trying to stay positive, but it&#39;s hard sometimes.$s&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>$e</samp></p></td>
<td><p>Ends the current dialogue, closing the dialogue box and resuming
player control. The dialogue following <samp>$e</samp> will require a
new interaction with the NPC.</p></td>
</tr>
<tr>
<td><p><samp>$k</samp></p></td>
<td><p>Short for <em>dialogueKill</em>. Removes all dialogue messages
after the current one.</p></td>
</tr>
<tr>
<td><p><samp>$p &lt;response ID&gt;#&lt;match text&gt;|&lt;no-match
text&gt;</samp></p></td>
<td><p>Stands for "dialoguePrerequisite". Shows different text depending
on whether the player gave a particular answer to a previously-asked
question. If &lt;response ID&gt; matches an answer the player gave,
&lt;match text&gt; is shown; otherwise, &lt;no-match text&gt; is shown.
These texts are separated by <code>|</code> and only &lt;no-match
text&gt; can contain additional commands. This does not need to be the
first command in the dialogue string.</p>
<p>You can check multiple response IDs. For example, this will show the
first dialogue if the player chose dialogue answer <samp>17</samp>,
<samp>18</samp>, or <samp>Apple</samp>:</p>
<pre><code>$p 17|18|Apple#I guess you think nothing would happen, right?$u|Maybe a wicked ghost would appear!</code></pre></td>
</tr>
<tr>
<td><p><samp>$q &lt;response IDs&gt;
&lt;fallback&gt;#&lt;text&gt;</samp></p></td>
<td><p>Show a dialogue box containing the given question text. If
&lt;response IDs&gt; (a list delimited by <code>/</code>) contains an
answer already given, the question is skipped (along with the rest of
this dialogue line), and instead the dialogue entry identified by
&lt;fallback&gt; will be appended to whatever precedes this $q command.
The &lt;fallback&gt; dialogue typically uses a $p command to adjust the
text based on the player's answer to this question. NOTE: dialogue
questions must use unique IDs, similar to events. See <a
href="Modding_Event_data" class="wikilink"
title="the event data page">the event data page</a> for more
information.</p></td>
</tr>
<tr>
<td><p><samp>$query &lt;query&gt;#&lt;if true&gt;|&lt;if
false&gt;</samp></p></td>
<td><p>Show different dialogue text depending on the <a
href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> in &lt;query&gt;. For
example:</p>
<div class="sourceCode" id="cb3"><pre class="sourceCode js"><code class="sourceCode javascript"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Mon&quot;</span><span class="op">:</span> <span class="st">&quot;$query !PLAYER_VISITED_LOCATION Current Mine#Did you know there&#39;s an old abandoned mine up in the mountain? Apparently it&#39;s crawling with monsters!|I heard you went into the old mines up in the mountain!#Did you find anything tasty?$h&quot;</span></span></code></pre></div>
<p><strong>⚠ Careful:</strong> the query is checked when the dialogue is
parsed, which isn't always when the player speaks to the NPC. For
example, the NPC may check its dialogue after it finishes pathfinding
somewhere. You shouldn't expect the query to be realtime (e.g. checking
the player's location or equipped items may reflect an earlier point in
the day).</p></td>
</tr>
<tr>
<td><p><samp>$r &lt;response ID&gt; &lt;friendship&gt; &lt;reaction&gt;
[observerfriendship]#&lt;answer text&gt;</samp></p></td>
<td><p>Define a response option to a $q question dialogue. &lt;answer
text&gt; is the text shown. &lt;response ID&gt; is used to group
responses for future reference (multiple answers can share an answer
ID). &lt;friendship&gt; defines the change in friendship value with the
speaker, positive or negative, if this response is selected.
&lt;reaction&gt; names the dialogue entry from the NPC's
<samp>Content\Characters\Dialogue\*.xnb</samp> file that will be the
NPC's reaction if this response is selected by the player.
[observerfriendship] is an underscore (_) separated string which, if
included, affects the friendship with another NPC if this response is
selected. It takes the format of <code>friend_NPCID_Integer</code>, e.g.
"friend_George_-20" or "friend_Penny_40".</p></td>
</tr>
<tr>
<td><p><samp>$t &lt;topic ID&gt; [day length]</samp></p></td>
<td><p>Add a <a href="Modding_Dialogue#Conversation_topics"
class="wikilink" title="conversation topic">conversation topic</a> for
the next [day length] days (default 4 days).</p></td>
</tr>
<tr>
<td><p><samp>$v &lt;event id&gt; [check preconditions] [skip if
seen]</samp></p></td>
<td><p>Immediately start an <a href="Modding_Event_data"
class="wikilink" title="event">event</a> and end the current dialogue,
subject to the conditions:</p>
<ul>
<li>[check preconditions]: whether to ignore the command if the <a
href="Modding_Event_data#Event_preconditions" class="wikilink"
title="event&#39;s preconditions">event's preconditions</a> don't match
(one of <samp>true</samp> or <samp>false</samp>). Default true.</li>
<li>[skip if seen]: whether to ignore the command if the player has
already seen the given event. Default true.</li>
</ul>
<p>If the event is not played, the dialogue continues to the next line
instead.</p>
<p>For example, <code>$v 60367 false false</code> will replay the bus
arrival event from the start of the game.
<code>$v SomeMod.Test true false#$b#Wow! Good timing!$1</code> will play
the event "SomeMod.Test" if the player meets the precondition
requirements. If they do not, the dialogue "Wow! Good timing!$1" will
play instead.</p>
<p>Note: The command will only work if it is at the very start of the
dialogue. Adding any dialogue or other commands before it will cause it
not to trigger the event and display the event commands as dialogue
instead.</p></td>
</tr>
<tr>
<td><p><samp>$y '&lt;answer&gt;_&lt;reply&gt;'</samp></p></td>
<td><p>Stands for "dialogueQuickResponse"; A simpler form of question.
Works like <samp>$q</samp>, but within one and the same text line. It
doesn't have response IDs that can be used with "dialoguePrerequisite"
(<samp>$p</samp>). It can't be used for friendship point changes. It can
be triggered indefinitely. It doesn't have to be the first command in a
dialogue string as long as the dialogue before it ends with
<samp>#$e#</samp> or <samp>#$b#</samp>. It can have more than two
answer/reply pairs.<br />
<small>Example: <samp>Penny: "$y 'Breakfast?_Yes please._Here you
go._No, I'm good_More for me then!'"</samp></small></p></td>
</tr>
<tr>
<td><p><samp>$1 &lt;letter ID&gt;#&lt;1st-time text&gt; #$e#
&lt;nth-time text&gt;</samp></p></td>
<td><p>Creates a line of dialogue which the character will only see once
(at most). &lt;1st-time text&gt; is shown only if &lt;letter ID&gt; has
not been marked as sent yet (and this marks it as sent); otherwise,
&lt;nth-time text&gt; is shown. &lt;letter ID&gt; should not correspond
to an actual piece of mail (because it will not be sent), but it can be
referenced by events or other dialogue lines.</p></td>
</tr>
<tr>
<td><p><samp>%fork</samp></p></td>
<td><p>Sets the the <samp>specialEventVariable1</samp> variable, which
can be checked by a later <samp>fork</samp> event command. Mainly useful
in reaction dialogue for <samp>$q</samp> questions during
events.</p></td>
</tr>
<tr>
<td><p><samp>%revealtaste:&lt;NPC name&gt;:&lt;item ID&gt;</samp><br />
<s><samp>%revealtaste&lt;NPC&gt;&lt;object ID&gt;</samp></s></p></td>
<td><p>Reveals the named character's gift taste for an <a
href="Modding_Objects" class="wikilink" title="object">object</a> in
their social menu profile. For example,
<samp>%revealtaste:Lewis:(O)258</samp> will update Lewis's profile to
show that he likes blueberries. This only works if it's in the first
message in a dialogue box (<em>i.e.,</em> before any <code>#$b#</code>
break, though <code>#$e#</code> breaks are fine).</p>
<p>The second form is deprecated and only works with unqualified numeric
item IDs.</p></td>
</tr>
<tr>
<td><p><samp>[&lt;id&gt;+]</samp></p></td>
<td><p>Gives the player a random item, from the pool of <a
href="Modding_Objects_Object_sprites" class="wikilink"
title="item IDs">item IDs</a> within the brackets. For example,</p>
<div class="sourceCode" id="cb4"><pre class="sourceCode js"><code class="sourceCode javascript"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;I spent the afternoon daydreaming about the ocean. So I decided to cook some seafood. [(O)198 (O)202 (O)727 (O)MossSoup]$h&quot;</span></span></code></pre></div>
<p>...gives one of <samp>198</samp> (Baked Fish), <samp>202</samp>
(Fried Calamari), <samp>727</samp> (Chowder), or <samp>MossSoup</samp>
(Moss Soup) as a gift.</p>
<p>Each one can be a qualified or unqualified item ID.</p></td>
</tr>
</tbody>
</table>

#### Question example

To understand how \$q, \$r, and \$p work, an example may be helpful.
Note how you can format the script to be easier to read:

``` yaml
summer_Fri:
    "I think I'll go to the beach tomorrow!
    #$q 305/306 beachquestion_followup#Would you like to go with me?
        #$r 305 15 beachquestion_yes#Sure, I would love to!
        #$r 306 0 beachquestion_sorry#Oh, sorry, I've already made plans with someone else...
        #$r 306 -10 beachquestion_no#No thank you.
    ",
    "beachquestion_yes": "Good! It's a date.$h",
    "beachquestion_sorry": "Oh. Darn. Okay.$6",
    "beachquestion_no": "Oh. Um. Sorry.$s",
    "beachquestion_followup":
        "$p 305
            #Tomorrow should be a lot of fun!$h
            |Hmm, I wonder if I can get someone to go with me...$s
        ",

summer_Sat:
    "The beach is lovely this time of year...
    #$p 305
        #Thanks for coming with me today.$h
        |Oh, hi @, how's it going?
    ",
```

The dialogue above triggers on any Friday in the summer. The NPC begins
with a response that is always shown: "I think I'll go to the beach
tomorrow!"

Next they ask you a question.

``` yaml
#$q 305/306 beachquestion_followup#Would you like to go with me?
```

**\$q** starts the question. **305/306** checks to see if this question
has been asked before, and if it has it sends you to the dialogue key
**beachquestion_followup**. (Note that you can name your dialogue keys
whatever you like which makes it easier to read.)

Next are the responses the player can give. You can add any number of
**\$r** lines; here we have three:

``` yaml
    #$r 305 15 beachquestion_yes#Sure, I would love to!
    #$r 306 0 beachquestion_sorry#Oh, sorry, I've already made plans with someone else...
    #$r 306 -10 beachquestion_no#No thank you.
```

If you say yes (first option), the game will store **ID 305** as the
answer given to this question. Next, your friendship with that person
increases by **15**. **beachquestion_yes** tells the script which
dialogue key continuation to use as a response to your answer.

If you say no (second and third option) the game will store **ID 306**
as the answer given, then depending on which answer you gave will either
not change your friendship with the person, **0**, or reduce it,
**-10**. Then it will use either **beachquestion_sorry** or
**beachquestion_no** to continue the dialogue.

Now we need to make dialogue keys for each response:

``` yaml
    beachquestion_yes: "Good! It's a date.$h",
    beachquestion_sorry: "Oh. Darn. Okay.$6",
    beachquestion_no: "Oh. Um. Sorry.$s",
    beachquestion_followup:
        "$p 305
            #Tomorrow should be a lot of fun!$h
            |Hmm, I wonder if I can get someone to go with me...$s
        ",
```

Of note here is **beachquestion_followup**. If the player talks to the
NPC again, **\$q 305/306** will check that the question has already been
answered and instead go directly to this key.

**\$p 305** begins a variable response which means "**if** the player
chose yes, say this line, **else** say this line instead". If the player
answered yes, the NPC responds happily. Otherwise, they will comment
that they need to find someone to go with them.

There is another variable response the next day:

``` yaml
summer_Sat:
    "The beach is lovely this time of year...
    #$p 305
        #Thanks for coming with me today.$h
        |Oh, hi @, how's it going?
    ",
```

Once again the first line (The beach is lovely...) always shows up when
the player talks to the NPC, but the next line depends on whether or not
they've answered yes the previous day.

------------------------------------------------------------------------

Here is another example from Haley's existing dialogue file. Note how
the script formatting is harder to read, but the game is able to process
both.

``` yaml
    summer_Sat: "Farming sounds so boring...#$q 42/43 summer_Sat_old#What do you even do all day?#$r 42 10 summer_Sat_12#Care for plants#$r 42 10 summer_Sat_12#Explore the caves#$r 43 -10 summer_Sat_13#Snoop around in your room#$r 42 10 summer_Sat_12#Dig for treasure" #!String
    summer_Sat_old: "#$p 43#Hey, you better not be snooping around in my room anymore!$a|But I guess it could get you in pretty good shape." #!String
    summer_Sat_12: "Hmm... sounds like a lot of work." #!String
    summer_Sat_13: "What? You'd better not be doing that!$a" #!String
```

The first time the `summer_Sat` dialogue is chosen, neither response 42
nor 43 will have been given (because this question is the only one which
has them as responses), so Haley will say, "Farming sounds so boring...
What do you even do all day?" The player can select among these
responses:

- Care for plants
- Explore the caves
- Snoop around in your room
- Dig for treasure

The third response, `$r 43 -10 summer_Sat_13#Snoop around in your room`,
sets response ID 43, reduces Haley's friendship by 10 points, and brings
up the dialogue `summer_Sat_13` (Haley says, "What? You'd better not be
doing that!"). All of the other responses set response ID 42, increase
Haley's friendship by 10 points, and bring up the dialogue
`summer_Sat_12` ("Hmm... sounds like a lot of work.").

The next time `summer_Sat` is chosen, one of the response IDs listed in
the `$q` command will have been given (either 42 or 43). Therefore, the
`$q` and everything after is scrapped, and dialogue `summer_Sat_old` is
put in its place. This new dialogue uses the `$p` command to change
Haley's dialogue based on whether or not you gave response ID 43 to any
previous question. If you answered "Snoop around your room," everything
before the `|` will be used, so Haley will now say, "Farming sounds so
boring... Hey, you better not be snooping around in my room anymore!" If
response ID 43 has not been given (in this case, you must have given
response ID 42, *i.e.,* one of the other three responses to the previous
question), everything after the `|` will be used, so Haley will instead
say, "Farming sounds so boring... But I guess it could get you in pretty
good shape."

### Replacer commands

Replacer commands will be replaced with the relevant string. Note that
in mail entries, only the `@` replacer works.

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>@</samp></p></td>
<td><p>Farmer's name.<br />
<em>Example: <code>Hi there @!</code></em></p></td>
</tr>
<tr>
<td><p><samp>%adj</samp></p></td>
<td><p>Random adjective. (Defined in StringsFromCSFiles.xnb)</p></td>
</tr>
<tr>
<td><p><samp>%noun</samp></p></td>
<td><p>Random noun. (Defined in StringsFromCSFiles.xnb)</p></td>
</tr>
<tr>
<td><p><samp>%place</samp></p></td>
<td><p>Random place name. (Defined in StringsFromCSFiles.xnb)</p></td>
</tr>
<tr>
<td><p><samp>%spouse</samp></p></td>
<td><p>The name of Farmer's spouse.</p></td>
</tr>
<tr>
<td><p><samp>%name</samp></p></td>
<td><p>A randomly-generated name.</p></td>
</tr>
<tr>
<td><p><samp>%firstnameletter</samp></p></td>
<td><p>The first half of the farmer's name (rounded down), like
<em>Nat</em> if the farmer's name is Natalie.</p></td>
</tr>
<tr>
<td><p><samp>%time</samp></p></td>
<td><p>Current time.</p></td>
</tr>
<tr>
<td><p><samp>%band</samp></p></td>
<td><p>The name of Sam and Sebastian's band.</p></td>
</tr>
<tr>
<td><p><samp>%book</samp></p></td>
<td><p>The title of Elliott's book.</p></td>
</tr>
<tr>
<td><p><samp>%pet</samp></p></td>
<td><p>The name of Farmer's pet.</p></td>
</tr>
<tr>
<td><p><samp>%farm</samp></p></td>
<td><p>Farm name.</p></td>
</tr>
<tr>
<td><p><samp>%favorite</samp></p></td>
<td><p>The Farmer's favorite thing.</p></td>
</tr>
<tr>
<td><p><samp>%kid1</samp></p></td>
<td><p>The name of Farmer's first child.</p></td>
</tr>
<tr>
<td><p><samp>%kid2</samp></p></td>
<td><p>The name of Farmer's second child.</p></td>
</tr>
</tbody>
</table>

## Values

The game uses these predefined values in some dialogue keys. This
section is linked from above where needed.

### Days of week

- `Mon`
- `Tue`
- `Wed`
- `Thu`
- `Fri`
- `Sat`
- `Sun`

### Seasons

- `spring`
- `summer`
- `fall`
- `winter`

### First/later year

In some cases the game uses a "first/later year" value for dialogue
conditions. This only has two possible values:

| value | meaning                                               |
|-------|-------------------------------------------------------|
| `1`   | Occurs in the first year.                             |
| `2`   | Occurs in any year after the first (not only year 2). |

### Response IDs

A response ID identifies an answer chosen by the player in response to a
<a href="#Question_example" class="wikilink"
title="question dialogue">question dialogue</a>. In some cases a
question may have several answers with the same ID (*e.g.,* several
variations of "yes"), or use the same ID for *every* question (in which
case the ID just shows whether the player has answered the question).

Mods can add their own response IDs, but here are the vanilla IDs as of
¹:

Dialogue
{\| class="wikitable"

\|- ! NPC ! question ! answers \|- \| Abigail \| `fall_Sun`\
*I was thinking about dyeing my hair again... what do you think?* \|
`27`: *Dye it black.*\
`27`: *Why not blonde?*\
`27`: *How about bubblegum pink?*\
`28`: *I like your hair just the way it is!* \|- \| Abigail \|
`summer_Sun`\
*Okay... pretend you just won a free vacation. Where would you go?* \|
`25`: *The beach*\
`26`: *In a dark cave*\
`26`: *The old, gnarled forest*\
`25`: *Joja Mega-Mall* \|- \| Abigail \| `Sun2`\
*@, What do you think happens to us after we die?* \| `17`: *I have no
idea.*\
`18`: *We come back as spooky ghosts.*\
`17`: *We go to Heaven.*\
`18`: *Our energy bodies enter the astral plane.*\
`17`: *Nothing. We just cease to exist.* \|- \| Abigail \| `winter_Sun`\
*I made these two drawings. What do you think?* \| `29`: *I like the
jungle island and the tiger.*\
`30`: *I like the orc with the battleaxe.*\
`29`: *I don't like either of them.* \|- \| Alex \| `fall_Wed`\
*Do you think the ladies like my haircut?^What do you think about my
haircut?* \| `54`: *It looks very fashionable.*\
`55`: *It looks like some kind of fungal growth.* \|- \| Alex \|
`summer_Wed`\
*Do you think I'll ever turn pro?* \| `52`: *You're destined to be a
sports legend*\
`52`: *Maybe, if you practice a lot*\
`53`: *No, you'll most likely fail and become a salesman* \|- \| Alex \|
`Wed`\
*I'd ask you to throw the ball around, but you don't really seem like
the sports type.^If you weren't a girl I'd ask you to play catch.* \|
`6`: *I'm fine just watching you from a distance.*\
`5`: *I want to play catch with you!*\
`5`: *(angry) What's that supposed to mean?* \|- \| Clint \| `Mon`\
*I bet you can't guess what my great-grandfather was...* \| `9`: *A
blacksmith.*\
`9`: *A silly clown.*\
`9`: *A sarcastic jerk.* \|- \| Haley \| `fall_Sat`\
*\*sigh\*...what do you think I should do today?* \| `44`: *Watercolor
painting*\
`44`: *Relax and read a magazine*\
`44`: *Stop being a selfish crybaby* \|- \| Haley \| `summer_Sat`\
*What do you even do all day?* \| `42`: *Care for plants*\
`42`: *Explore the caves*\
`43`: *Snoop around in your room*\
`42`: *Dig for treasure* \|- \| Leah \| `Mon`\
*So why did you become a farmer?* \| `21`: *I want to make tons of
money.*\
`22`: *It's more "real" than living in the city.*\
`211132`: *To follow in grandpa's footsteps.*\
`22`: *I wanted to escape my old life.* \|- \| Maru \| `summer_Thu`\
*I've decided I'm going to build a robot someday.* \| `35`: *That should
be very easy for you*\
`36`: *You should be more realistic*\
`35`: *It sounds challenging* \|- \| Maru \| `Sun`\
*Do you have fun working on the farm?* \| `3`: *Yes.*\
`4`: *No.* \|- \| Penny \| `Mon4`\
*But it's best not to dwell on bad things, right?* \| `7`: *Right. It's
best to be positive!*\
`8`: *I think it's good to be realistic.* \|- \| Sam \| `Wed`\
*Hey.. What do you think my new song should be about?* \| `20`:
*Farming, mining, and chopping wood.*\
`8820`: *A city in the sea.*\
`8821`: *Trains.*\
`19`: *Choose anything. It'll still be a horrible song.* \|- \|
Sebastian \| `fall_Fri`\
*Do you read, @?* \| `62`: *Yep. The classics.*\
`63`: *Only Sci-fi and Fantasy*\
`62`: *I like a good Romance*\
`63`: *No, I don't read books* \|- \| Sebastian \| `Fri2`\
*So what do you do when you aren't working?* \| `15`: *More Farming*\
`16`: *Comic books*\
`15`: *Shopping*\
`15`: *Sports* \|}

Events
{\| class="wikitable"

\|- ! event ! question ! answers \|- \|
<a href="Abigail#Four_Hearts" class="wikilink"
title="Abigail&#39;s 4-heart event">Abigail's 4-heart event</a> \| *@!
Why are you out here in the rain?\$7* \| `32`: *Just doing some work*\
`32`: *Enjoying the weather*\
`32`: *I could ask you the same question* \|- \|
<a href="Abigail#Six_Hearts" class="wikilink"
title="Abigail&#39;s 6-heart event">Abigail's 6-heart event</a> \|
*You've used a sword before, haven't you?* \| `847951`: *Yes, and it's
exciting!*\
`847951`: *Yes, but only in self-defense*\
`847951`: *Yes, but it's dangerous. You should stay safe.*\
`847951`: *No* \|- \| <a href="Abigail#Ten_Hearts" class="wikilink"
title="Abigail&#39;s 10-heart event">Abigail's 10-heart event</a> \|
*\*sniff\*\$s* \| `776589`: *What happened?*\
`776589`: *Are you okay?* \|- \|
<a href="Abigail#Ten_Hearts" class="wikilink"
title="Abigail&#39;s 10-heart event">Abigail's 10-heart event</a> \| *I
guess I'm not as tough as I thought...\$8* \| `34`: *You're safe with
me.*\
`34`: *I get scared too.*\
`34`: *You're crying like a little baby. Stop.* \|- \|
<a href="Alex#Five_Hearts" class="wikilink"
title="Alex&#39;s 5-heart event">Alex's 5-heart event</a> \| *I'm
worthless...\$s* \| `57`: *That's crazy. You're a genius!*\
`57`: *We all have our strengths and weaknesses*\
`57`: *Worthless? Yeah, that about sums it up.* \|- \|
<a href="Clint#Three_Hearts_I" class="wikilink"
title="Clint&#39;s 3-heart event">Clint's 3-heart event</a> \| *Got any
tips?^What advice can you give me?* \| `211`: *Impress women with your
strength and charm*\
`211`: *Act crazy, to keep people guessing*\
`211`: *Just act natural... be yourself*\
`211`: *Treat women the same as men* \|- \|
<a href="Demetrius#Six_Hearts" class="wikilink"
title="Demetrius&#39;s 6-heart event">Demetrius's 6-heart event</a> \|
*How would you classify a tomato?* \| `59`: *Vegetable*\
`59`: *Fruit* \|- \| <a href="Elliott#Two_Hearts" class="wikilink"
title="Elliott&#39;s 2-heart event">Elliott's 2-heart event</a> \| *A
question... What kind of books do you like, @?* \| `958699`: *Mystery*\
`958700`: *Romance*\
`958701`: *Sci-Fi* \|- \| <a href="Elliott#Four_Hearts" class="wikilink"
title="Elliott&#39;s 4-heart event">Elliott's 4-heart event</a> \|
*Wait. I propose a toast! To...* \| `28376`: *To Pelican Town!*\
`28376`: *To our friendship!*\
`28376`: *To my good health!*\
`28376`: *To your doom!* \|- \|
<a href="Emily#Six_Hearts" class="wikilink"
title="Emily&#39;s 6-heart event">Emily's 6-heart event</a> \| *So...
\*gasp\*... what did you think?\$h* \| `213`: *That was amazing!*\
`213`: *That was embarrassing...*\
`213`: *(Say nothing and do a slow clap)* \|- \|
<a href="Evelyn#Four_Hearts" class="wikilink"
title="Evelyn&#39;s 4-heart event">Evelyn's 4-heart event</a> \| *Well,
what do you think?* \| `51`: *It's delicious!*\
`51`: *It was like chewing on a hockey puck* \|- \|
<a href="Gus#Four_Hearts" class="wikilink"
title="Gus&#39;s 4-heart event">Gus's 4-heart event</a> \| *@, what's
going on here?* \| `207`: *You need to pay your tab right now!*\
`208`: *The saloon isn't doing well, financially* \|- \|
<a href="Haley#Two_Hearts" class="wikilink"
title="Haley&#39;s 2-heart event">Haley's 2-heart event</a> \| *It's
only because I cleaned them last week!\$a* \| `46`: *Stop whining and
just clean it!*\
`45`: *Haley, why not have this be your one weekly job?*\
`46`: *Emily, take the high road and do it this time.* \|- \|
<a href="Haley#Four_Hearts" class="wikilink"
title="Haley&#39;s 4-heart event">Haley's 4-heart event</a> \| *Say...
you're pretty strong, aren't you?* \| `47`: *Yes*\
`47`: *No* \|- \| <a href="Haley#Six_Hearts" class="wikilink"
title="Haley&#39;s 6-heart event">Haley's 6-heart event</a> \| *I'll
never find another one like it...\$s* \| `48`: *Relax, I'll just buy you
a new one!*\
`48`: *I'm really sorry...* \|- \|
<a href="Harvey#Two_Hearts" class="wikilink"
title="Harvey&#39;s 2-heart event">Harvey's 2-heart event</a> \| *@,
what do you think George should do?* \| `84`: *George should follow Dr.
Harvey's advice.*\
`85`: *George knows what's best for his own body.* \|- \|
<a href="Harvey#Four_Hearts" class="wikilink"
title="Harvey&#39;s 4-heart event">Harvey's 4-heart event</a> \| *Hmm...
Your pulse is high.\$u* \| `86`: *I'm a little nervous...*\
`86`: *I'm out of breath from working on the farm.*\
`86`: *Are you really a doctor? My pulse is fine!* \|- \|
<a href="Kent#Three_Hearts_I" class="wikilink"
title="Kent&#39;s 3-heart event">Kent's 3-heart event</a> \| *(Say
something to Kent)\$s* \| `215`: *Jodi's to blame... she should've known
better!*\
`215`: *I know you're hurting... but don't blame your wife.*\
`215`: *(Lie) Blame me... I asked for popcorn* \|- \|
<a href="Leah#Four_Hearts" class="wikilink"
title="Leah&#39;s 4-heart event">Leah's 4-heart event</a> \| *Was that
selfish of me, @?\$s* \| `83`: *No, it had to be done.*\
`83`: *No, and your ex sounds like an idiot.*\
`83`: *No, but you would've been better off staying in the city.*\
`83`: *Yeah, a little.*\
`83`: *Yeah, but it's natural to care about yourself first.* \|- \|
<a href="Lewis#Six_Hearts" class="wikilink"
title="Lewis&#39;s 6-heart event">Lewis's 6-heart event</a> \| *@...You
overheard everything, didn't you?\$s* \| `200`: *Yes... but I'll keep it
a secret.*\
`201`: *Yes... and I'm going to tell everyone.* \|- \|
<a href="Maru#Two_Hearts" class="wikilink"
title="Maru&#39;s 2-heart event">Maru's 2-heart event</a> \| *Right, @?*
\| `15933`: *(Say nothing)*\
`15933`: *Actually, your Dad was being weird.* \|- \|
<a href="Maru#Four_Hearts" class="wikilink"
title="Maru&#39;s 4-heart event">Maru's 4-heart event</a> \| *@, what
should I do?* \| `38`: *Just scoop it off the floor. He won't know the
difference.*\
`39`: *Tell Harvey it was my fault.*\
`38`: *Tell Harvey it was an accident.* \|- \|
<a href="Maru#Six_Hearts" class="wikilink"
title="Maru&#39;s 6-heart event">Maru's 6-heart event</a> \| *What do
you see?* \| `40`: *A beautiful planet.*\
`40`: *A cold, dark abyss.* \|- \|
<a href="Maru#Eight_Hearts" class="wikilink"
title="Maru&#39;s 8-heart event">Maru's 8-heart event</a> \| *I'm so
sorry.\$8* \| `41`: *It's okay, it doesn't even hurt.*\
`41`: *You'd better be. This hurts like crazy!* \|- \|
<a href="Maru#Ten_Hearts" class="wikilink"
title="Maru&#39;s 10-heart event">Maru's 10-heart event</a> \| *Well,
what do you think, @?* \| `18981`: *I'm so impressed with your
inventions.*\
`18981`: *I'm disappointed... You should've made that robot your
slave.*\
`18981`: *So is your Dad okay with 'us' now?*\
`18981`: *(Just stare at Maru and say nothing)* \|- \|
<a href="Maru#Ten_Hearts" class="wikilink"
title="Maru&#39;s 10-heart event">Maru's 10-heart event</a> \| *You must
have a good reason for saying that...\$a* \| `18982`: *MarILDA's just a
piece of machinery designed to act human.*\
`18982`: *I was just kidding. MarILDA deserves her freedom.*\
`18982`: *I would've put her to work on the farm.* \|- \|
<a href="Penny#Two_Hearts" class="wikilink"
title="Penny&#39;s 2-heart event">Penny's 2-heart event</a> \| *@? You
were watching us?* \| `71`: *I was. You did a kind thing there, Penny.*\
`71`: *You should've left him alone. Now he's grumpy.*\
`71`: *I'm just taking a walk, minding my own business.* \|- \|
<a href="Penny#Six_Hearts" class="wikilink"
title="Penny&#39;s 6-heart event">Penny's 6-heart event</a> \|
*...well?* \| `72`: *(Lie) Mmm! That was delicious!*\
`73`: *Uh... can I get the rest to go?*\
`73`: *Well it's definitely unique... how did you get it so rubbery?*
\|- \| <a href="Pierre#Six_Hearts" class="wikilink"
title="Pierre&#39;s 6-heart event">Pierre's 6-heart event</a> \|
*Promise me you won't tell anyone about this.* \| `50`: *Your secret is
safe with me.*\
`50`: *Your wife deserves to know about this.* \|- \|
<a href="Robin#Six_Hearts" class="wikilink"
title="Robin&#39;s 6-heart event">Robin's 6-heart event</a> \| *Have you
ever made anything out of wood, @?* \| `66`: *Yes*\
`66`: *No* \|- \| <a href="Sam#Two_Hearts" class="wikilink"
title="Sam&#39;s 2-heart event">Sam's 2-heart event</a> \| *Say, @...
what kind of music do you like?* \| `76`: *Cheerful pop music.*\
`77`: *Experimental noise rock.*\
`78`: *Hi-Energy dance music.*\
`79`: *Honky-tonky country music.* \|- \|
<a href="Sam#Four_Hearts" class="wikilink"
title="Sam&#39;s 4-heart event">Sam's 4-heart event</a> \| *...Tell her,
@.\$s* \| `80`: *Sam dropped the snack as he was handing it to me.*\
`80`: *Sam handed me the snack and then I dropped it.*\
`81`: *Sam dropped it on purpose. He thought it would be funny.* \|}

<small>¹ Extracted using [this LINQPad
script](https://gist.github.com/Pathoschild/6a133fd567d724cc2e3057a8acf448b8).</small>

## Conversation topics

A *conversation topic* is a temporary flag which can be checked in
<a href="Modding_Event_data" class="wikilink"
title="event preconditions">event preconditions</a> and
<a href="Modding_Game_state_queries" class="wikilink"
title="game state queries">game state queries</a> and can trigger
one-time NPC dialogue (if they have a matching dialogue key). They're
stored in `Farmer.activeDialogueEvents` while active, and are moved from
there into `Farmer.previousActiveDialogueEvents` once they expire.

Since they are temporary, they are very useful for scheduling delays
between events: for example, once a topic is added, you can have a
subsequent event precondition only satisfied if the topic is *not*
active, so the topic's duration in days must elapse before the event can
be viewed.

A conversation topic can be started in a number of ways:

- using the `addConversationTopic`
  <a href="Modding_Event_data" class="wikilink"
  title="event command">event command</a>
- using the `AddConversationTopic`
  <a href="Modding_Trigger_actions" class="wikilink"
  title="trigger action">trigger action</a>
- using the `$t` <a href="#Dialogue_commands" class="wikilink"
  title="dialogue command">dialogue command</a>
- using the `%item conversationTopic`
  <a href="Modding_Mail_data" class="wikilink" title="mail command">mail
  command</a>
- in code by calling `Farmer.activeDialogueEvents.TryAdd(string, int)`

A conversation topic lasts four days by default. All methods listed
above can optionally specify a preferred duration instead.

### Topic memory

In addition to the normal active time, the game also keeps track of how
long ago topics were set and automatically generates additional topics
after a certain number of days. These topics always use the original key
and append <code>_memory_

<time>

</code> to it (please note: **the game checks for keys to contain the
string "`_memory_`" to control its behavior here, so you should avoid
using that string in your topic IDs if possible**).

Here are the keys and how long they take to appear. All of them last for
four days.

| id                        | days since original key |
|---------------------------|-------------------------|
| `<key>_memory_oneday`     | 1                       |
| `<key>_memory_oneweek`    | 7                       |
| `<key>_memory_twoweeks`   | 14                      |
| `<key>_memory_fourweeks`  | 28                      |
| `<key>_memory_eightweeks` | 56                      |
| `<key>_memory_oneyear`    | 104                     |

Note that the `_memory_oneyear` key entry is not a typo, and starts
after 104 days, which is slightly less than one full year (112 days).

### Generic topics

These topics are generated by the game in response to the player
fulfilling certain conditions. These topics automatically cover any mods
that add data alongside vanilla, so (for example) any mod-added events
will generate `eventSeen_` topics, any NPCs will generate `married_`
when the player marries them, etc. Combined with topic memory, this
gives you a lot of power to time events and coordinate NPC behavior
without having to do any extra work.

All of these topics last for four days.

| id | trigger |
|----|----|
| `achievement_<id>` | Player earns the given <a href="Achievements" class="wikilink"
title="achievement">achievement</a> for the first time. |
| `cropMatured_<object id>` | Player has harvested a fully-grown crop of the given type for the first time. |
| `dating_<npc internal name>` | Player begins dating the given <a href="Modding_NPC_data" class="wikilink" title="NPC">NPC</a> for the first time (only set when the player gives the NPC a bouquet and it is accepted; other means of changing the relationship do not count). |
| `divorced_<npc internal name>` | Player divorces the given <a href="Modding_NPC_data" class="wikilink" title="NPC">NPC</a> for the first time (only set when using the book in the <a href="Mayor&#39;s_Manor" class="wikilink"
title="Mayor&#39;s Manor">Mayor's Manor</a>; does not apply to roommates). |
| `eventSeen_<id>` | Player sees the given <a href="Modding_Event_data" class="wikilink" title="event">event</a> for the first time. |
| `firstVisit_<location name>` | Player enters the given <a href="Modding_Location_data" class="wikilink"
title="location">location</a> for the first time. |
| `fishCaught_<id>` | Player catches the given <a href="Modding_Fish_data" class="wikilink" title="fish">fish</a> for the first time. |
| `houseUpgrade_<level>` | Player upgrades their house to the given level (*e.g.* `2`). |
| `married_<npc internal name>` | Player marries the given <a href="Modding_NPC_data" class="wikilink" title="NPC">NPC</a> for the first time (only set by watching the wedding event with that NPC; other means of changing the relationship do not count). |
| `mineArea_<area>` | Player enters the given <a href="The_Mines" class="wikilink" title="mine">mine</a> area (an integer) for the first time. This is `0` for floors 1-10, `10` for floors 11-39, `40` for floors 40-79, `80` for floors 80-120, `121` for any <a href="Skull_Cavern" class="wikilink" title="Skull Cavern">Skull
Cavern</a> floors, and `77377` for the <a href="Quarry_Mine" class="wikilink" title="Quarry Mine">Quarry
Mine</a>. (*FIXME: there may be other values for MineShafts with level == -1*) |
| `purchasedAnimal_<type>` | Player buys the given <a href="Modding_Animal_data" class="wikilink" title="animal">animal</a> type for the first time. |
| `questComplete_<id>` | Player completes the given <a href="Modding_Quest_data" class="wikilink" title="quest">quest</a> for the first time. |
| `roommates_<npc internal name>` | The given <a href="Modding_NPC_data" class="wikilink" title="NPC">NPC</a> moves in as the player's roommate for the first time. |
| `structureBuilt_<type>` | Player builds the given type of <a href="Modding_Buildings" class="wikilink" title="farm building">farm
building</a> for the first time. |

### Specific topics

These topics are generated by the game in response to specific events
and don't use any variables in their keys.

<table>
<thead>
<tr>
<th><p>id</p></th>
<th><p>duration</p></th>
<th><p>trigger</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Bundles</p></td>
</tr>
<tr>
<td><p><samp>cc_Begin</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set in the <a href="Wizard" class="wikilink"
title="Wizard">Wizard</a>'s cutscene after reading the first Junimo note
in the community center.</p></td>
</tr>
<tr>
<td><p><samp>cc_Complete</samp></p></td>
<td><p>4 days</p></td>
<td><p><a href="Community_Center" class="wikilink"
title="Community Center">Community Center</a> completed. (Does not apply
to JojaMart path.)</p></td>
</tr>
<tr>
<td><p><samp>cc_Boulder</samp></p></td>
<td><p>7 days</p></td>
<td><p><a href="The_Mountain" class="wikilink"
title="Mountain">Mountain</a> boulder is removed through community
center bundle or Joja improvement form.</p></td>
</tr>
<tr>
<td><p><samp>cc_Bridge</samp></p></td>
<td><p>7 days</p></td>
<td><p><a href="Quarry" class="wikilink" title="Quarry">Quarry</a>
bridge is repaired through community center bundle or Joja improvement
form.</p></td>
</tr>
<tr>
<td><p><samp>cc_Bus</samp></p></td>
<td><p>7 days</p></td>
<td><p><a href="Bus_Stop" class="wikilink" title="Bus">Bus</a> is
repaired through community center bundle or Joja improvement
form.</p></td>
</tr>
<tr>
<td><p><samp>cc_Greenhouse</samp></p></td>
<td><p>3 days</p></td>
<td><p><a href="Greenhouse" class="wikilink"
title="Greenhouse">Greenhouse</a> is constructed through community
center bundle. (Does not apply to JojaMart path.)</p></td>
</tr>
<tr>
<td><p><samp>cc_Minecart</samp></p></td>
<td><p>7 days</p></td>
<td><p><a href="Minecart" class="wikilink"
title="Minecart">Minecarts</a> are unlocked through community center
bundle or Joja improvement form.</p></td>
</tr>
<tr>
<td><p><samp>joja_Begin</samp></p></td>
<td><p>7 days</p></td>
<td><p>First time that player opens the <a
href="Joja_Community_Development_Form" class="wikilink"
title="Joja Community Development Form">Joja Community Development
Form</a>.</p></td>
</tr>
<tr>
<td><p><samp>movieTheater</samp></p></td>
<td><p>3 days</p></td>
<td><p><a href="Movie_Theater" class="wikilink"
title="movie theatre">movie theatre</a> is constructed.</p></td>
</tr>
<tr>
<td colspan="3"><p>Spouse events</p></td>
</tr>
<tr>
<td><p><samp>elliottGone</samp></p></td>
<td><p>6 days</p></td>
<td><p>Set when <a href="Elliott" class="wikilink"
title="Elliott">Elliott</a>'s fourteen-heart event starts.</p></td>
</tr>
<tr>
<td><p><samp>ElliottGone1</samp><br />
<samp>ElliottGone2</samp><br />
<samp>ElliottGone3</samp><br />
<samp>ElliottGone4</samp><br />
<samp>ElliottGone5</samp><br />
<samp>ElliottGone6</samp><br />
<samp>ElliottGone7</samp></p></td>
<td><p>same day</p></td>
<td><p>Part of <a href="Elliott" class="wikilink"
title="Elliott">Elliott</a>'s fourteen-heart event. The first flag is
set when it starts; the subsequent flags are set by subsequent letters
from Elliott.</p></td>
</tr>
<tr>
<td><p><samp>emilyFiber</samp></p></td>
<td><p>2 days</p></td>
<td><p>Part of <a href="Emily" class="wikilink"
title="Emily">Emily</a>'s fourteen-heart event. Set after completing the
quest.</p></td>
</tr>
<tr>
<td><p><samp>haleyCakewalk1</samp><br />
<samp>haleyCakewalk2</samp></p></td>
<td><p>same day</p></td>
<td><p>Part of <a href="Haley" class="wikilink"
title="Haley">Haley</a>'s fourteen-heart event.</p></td>
</tr>
<tr>
<td><p><samp>leahPaint</samp></p></td>
<td><p>same day</p></td>
<td><p>Set when <a href="Leah" class="wikilink" title="Leah">Leah</a>'s
fourteen-heart event starts.</p></td>
</tr>
<tr>
<td><p><samp>pennyRedecorating</samp></p></td>
<td><p>2 days</p></td>
<td><p>Part of <a href="Penny" class="wikilink"
title="Penny">Penny</a>'s fourteen-heart event.</p></td>
</tr>
<tr>
<td><p><samp>samJob1</samp><br />
<samp>samJob2</samp></p></td>
<td><p>2 days</p></td>
<td><p>Part of <a href="Sam" class="wikilink" title="Sam">Sam</a>'s
fourteen-heart event.</p></td>
</tr>
<tr>
<td><p><samp>samJob3</samp></p></td>
<td><p>3 days</p></td>
<td><p>Part of <a href="Sam" class="wikilink" title="Sam">Sam</a>'s
fourteen-heart event.</p></td>
</tr>
<tr>
<td><p><samp>sebastianFrog</samp></p></td>
<td><p>same day</p></td>
<td><p>Set when <a href="Sebastian" class="wikilink"
title="Sebastian">Sebastian</a>'s fourteen-heart event starts.</p></td>
</tr>
<tr>
<td><p><samp>sebastianFrog2</samp></p></td>
<td><p>6 days</p></td>
<td><p>Part of <a href="Sebastian" class="wikilink"
title="Sebastian">Sebastian</a>'s fourteen-heart event.</p></td>
</tr>
<tr>
<td><p><samp>shaneSaloon1</samp><br />
<samp>shaneSaloon2</samp></p></td>
<td><p>same day</p></td>
<td><p>Part of <a href="Shane" class="wikilink"
title="Shane">Shane</a>'s fourteen-heart event.</p></td>
</tr>
<tr>
<td colspan="3"><p>Other events</p></td>
</tr>
<tr>
<td><p><samp>gotPet</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set if the player chooses to adopt the first pet when Marnie
brings it to their front porch.</p></td>
</tr>
<tr>
<td><p><samp>dumped_Guys</samp><br />
<samp>dumped_Girls</samp></p></td>
<td><p>7 days</p></td>
<td><p>Set after the corresponding ten-heart group event (<em>e.g.,</em>
see <a href="Abigail#Group_Ten-Heart_Event" class="wikilink"
title="Abigail#Group Ten-Heart Event">Abigail#Group Ten-Heart
Event</a>).</p></td>
</tr>
<tr>
<td><p><samp>secondChance_Girls</samp><br />
<samp>secondChance_Guys</samp></p></td>
<td><p>14 days</p></td>
<td><p>Set after the corresponding ten-heart group event (<em>e.g.,</em>
see <a href="Abigail#Group_Ten-Heart_Event" class="wikilink"
title="Abigail#Group Ten-Heart Event">Abigail#Group Ten-Heart
Event</a>).</p></td>
</tr>
<tr>
<td><p><samp>GreenRainFinished</samp></p></td>
<td><p>2 days</p></td>
<td><p>Set after the Green Rain event in year one.</p></td>
</tr>
<tr>
<td><p><samp>dating</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set when the player starts dating an NPC for the first
time.</p></td>
</tr>
<tr>
<td><p><samp>married</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set when the player marries for the first time.</p></td>
</tr>
<tr>
<td><p><samp>married_twice</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set when the player marries for the second time.</p></td>
</tr>
<tr>
<td><p><samp>divorced_once</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set when the player divorces for the first time.</p></td>
</tr>
<tr>
<td><p><samp>divorced_twice</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set when the player divorces for the second time.</p></td>
</tr>
<tr>
<td><p><samp>LeoDeparture</samp></p></td>
<td><p>same day</p></td>
<td><p>Set when <a href="Leo" class="wikilink" title="Leo">Leo</a> moves
to the island (during the departure event at the island docks).</p></td>
</tr>
<tr>
<td><p><samp>pamHouseUpgrade</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set after seeing the <a href="Pam" class="wikilink"
title="Pam">Pam</a> house upgrade event, if the player chose to be
revealed as the donor.</p></td>
</tr>
<tr>
<td><p><samp>pamHouseUpgradeAnonymous</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set after seeing the <a href="Pam" class="wikilink"
title="Pam">Pam</a> house upgrade event, if the player chose to be
anonymous.</p></td>
</tr>
<tr>
<td><p><samp>willyCrabs</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set after <a href="Willy" class="wikilink"
title="Willy">Willy</a>'s six-heart event.</p></td>
</tr>
<tr>
<td><p><samp>wonEggHunt</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set when the player wins the <a href="Egg_Festival"
class="wikilink" title="Egg Hunt">Egg Hunt</a> for the first
time.</p></td>
</tr>
<tr>
<td><p><samp>wonGrange</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set when the player wins the <a href="Stardew_Valley_Fair"
class="wikilink" title="Grange Display showcase">Grange Display
showcase</a> for the first time.</p></td>
</tr>
<tr>
<td><p><samp>wonIceFishing</samp></p></td>
<td><p>4 days</p></td>
<td><p>Set when the player wins the <a href="Festival_of_Ice"
class="wikilink" title="Ice Fishing Contest">Ice Fishing Contest</a> for
the first time.</p></td>
</tr>
<tr>
<td colspan="3"><p>Other</p></td>
</tr>
<tr>
<td><p><samp>Introduction</samp></p></td>
<td><p>6 days</p></td>
<td><p>Farmer is created (<em>e.g.,</em> starting a new save, or joining
a multiplayer game for the first time).</p></td>
</tr>
<tr>
<td><p><samp>FullCrabPond</samp></p></td>
<td><p>14 days</p></td>
<td><p>First time any <a href="Fish_Pond" class="wikilink"
title="fish pond">fish pond</a> contains 10 <a href="crab"
class="wikilink" title="crab">crabs</a>.</p></td>
</tr>
</tbody>
</table>

## For C# mods

### `Dialogue` class

A sequence of NPC dialogues is represented by a `Dialogue` instance.
Some useful fields/methods include:

<table>
<thead>
<tr>
<th><p>member</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>dialogues</samp></p></td>
<td><p>The 'dialogue lines' to display. Each entry is shown in a single
dialogue box (but isn't necessarily a single line or sentence).</p>
<p>Each dialogue line can have text to show, a side effect (i.e. code to
run when it's displayed), or both. If an entry has a side-effect, it's
applied as soon as that dialogue entry is shown in the dialogue box. If
the entry has no text, the game skips to the next entry in the list (if
any) after applying the side-effect.</p></td>
</tr>
<tr>
<td><p><samp>speaker</samp></p></td>
<td><p>The NPC instance speaking the dialogue line, if
applicable.</p></td>
</tr>
<tr>
<td><p><samp>CurrentEmotion</samp></p></td>
<td><p>The <a href="#Portrait_commands" class="wikilink"
title="portrait command">portrait command</a> for the current dialogue
line.</p></td>
</tr>
<tr>
<td><p><samp>TranslationKey</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Translation_key"
class="wikilink" title="translation key">translation key</a> from which
the current dialogue line was taken, if applicable.</p></td>
</tr>
<tr>
<td><p><samp>getCurrentDialogue()</samp></p></td>
<td><p>Get the formatted dialogue text currently being
displayed.</p></td>
</tr>
<tr>
<td><p><samp>getPortraitIndex()</samp></p></td>
<td><p>The index from the NPC's portraits spritesheet to display for the
current dialogue line.</p></td>
</tr>
<tr>
<td><p><samp>isOnFinalDialogue()</samp></p></td>
<td><p>Whether the dialogue is currently showing last dialogue line
which has text to display.</p></td>
</tr>
<tr>
<td><p><samp>isDialogueFinished()</samp></p></td>
<td><p>Whether all dialogue lines have been shown.</p></td>
</tr>
<tr>
<td><p><samp>convertToDwarvish()</samp></p></td>
<td><p>Replace the current dialogue line with the Dwarvish translation
(as spoken by <a href="Dwarf" class="wikilink" title="Dwarf">Dwarf</a>
when the player doesn't have the <a href="Dwarvish_Translation_Guide"
class="wikilink" title="dwarvish translation guide">dwarvish translation
guide</a>).</p></td>
</tr>
</tbody>
</table>

The `Dialogue` class also provides a number of static methods for
working with dialogues. Some of the main ones include:

<table>
<thead>
<tr>
<th><p>method</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>TryGetDialogue(…)</samp></p></td>
<td><p>Create a dialogue for a given NPC and translation key, or return
null if the translation key isn't found.</p>
<p>This is commonly used to implement fallback dialogues. For
example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>Dialogue<span class="op">?</span> dialogue <span class="op">=</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    Dialogue<span class="op">.</span><span class="fu">TryGetDialogue</span><span class="op">(</span>npc<span class="op">,</span> $<span class="st">&quot;Charaxters</span><span class="sc">\\</span><span class="st">Dialogue</span><span class="sc">\\</span><span class="st">{npc.Name}:SomeKey_{relationship}&quot;</span><span class="op">)</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="op">??</span> Dialogue<span class="op">.</span><span class="fu">TryGetDialogue</span><span class="op">(</span>npc<span class="op">,</span> <span class="st">&quot;Charaxters</span><span class="sc">\\</span><span class="st">Dialogue</span><span class="sc">\\</span><span class="st">{npc.Name}:SomeKey&quot;</span><span class="op">);</span></span></code></pre></div>
<p>Note that this is somewhat low-level. In most cases, you should use
the equivalent <samp>NPC.TryGetDialogue</samp> method which reads from
the NPC's dialogue file. For example:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>Dialogue<span class="op">?</span> dialogue <span class="op">=</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    npc<span class="op">.</span><span class="fu">TryGetDialogue</span><span class="op">(</span>$<span class="st">&quot;SomeKey_{relationship}&quot;</span><span class="op">)</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="op">??</span> npc<span class="op">.</span><span class="fu">TryGetDialogue</span><span class="op">(</span><span class="st">&quot;SomeKey&quot;</span><span class="op">);</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>FromTranslation(…)</samp></p></td>
<td><p>Create a dialogue for a given NPC and translation key. This is
similar to <samp>TryGetDialogue</samp>, but an invalid dialogue key is
shown as-is instead.</p></td>
</tr>
<tr>
<td><p><samp>GetFallbackForError()</samp></p></td>
<td><p>Get a fallback dialogue to show when an error happens and a
suitable dialogue can't be loaded. This is some variation of "..."
depending on the language.</p></td>
</tr>
<tr>
<td><p><samp>applyGenderSwitchBlocks(…)</samp></p></td>
<td><p>Process <a href="#Gender_switch" class="wikilink"
title="gender switch blocks">gender switch blocks</a> in a given text.
This works with any text by design, not just dialogue text. You can
either use the current player's gender, or specify a gender to use.</p>
<p>For example:</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="dt">string</span> text <span class="op">=</span> Dialogue<span class="op">.</span><span class="fu">applyGenderSwitchBlocks</span><span class="op">(</span><span class="st">&quot;Hello ${lad^lass}$!&quot;</span><span class="op">);</span> <span class="co">// results in &quot;Hello lad!&quot; or &quot;Hello lass!&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>convertToDwarvish(text)</samp></p></td>
<td><p>Get the Dwarvish translation for a given dialogue line (as spoken
by <a href="Dwarf" class="wikilink" title="Dwarf">Dwarf</a> when the
player doesn't have the <a href="Dwarvish_Translation_Guide"
class="wikilink" title="dwarvish translation guide">dwarvish translation
guide</a>).</p></td>
</tr>
</tbody>
</table>

### `DialogueBox` class

`DialogueBox` is the menu shown in-game when a message box is displayed.
This is usually an NPC dialogue, but it's also used for some non-NPC
messages.

Some useful fields include:

| field | usage |
|----|----|
| `characterDialogue` | If this is a standard NPC dialogue, the <a href="#Dialogue_class" class="wikilink"
title="Dialogue instance"><samp>Dialogue</samp> instance</a> being shown. |
| `dialogues` | If this is a custom dialogue, the dialogue lines being shown. |
| `isPortraitBox()` | Whether the dialogue box has an NPC portrait. |

For NPC dialogues, you can use the
<a href="Modding_Modder_Guide_APIs_Events#Display" class="wikilink"
title="MenuChanged event"><samp>MenuChanged</samp> event</a> to detect
when a specific dialogue is shown. For example:

``` c#
private void OnMenuChanged(object sender, MenuChangedEventArgs e)
{
    bool isAbigailDanceRejection =
        e.NewMenu is DialogueBox dialogueBox
        && dialogueBox.characterDialogue is {} dialogue
        && dialogue.speaker?.Name == "Abigail"
        && dialogue.TranslationKey == "Characters\\Dialogue\\Abigail:danceRejection";
}
```

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="pt_Modificações_Diálogo" class="wikilink"
title="pt:Modificações:Diálogo">pt:Modificações:Diálogo</a>
<a href="ru_Модификации_Диалоги" class="wikilink"
title="ru:Модификации:Диалоги">ru:Модификации:Диалоги</a>
<a href="zh_使用模组_对话" class="wikilink"
title="zh:使用模组:对话">zh:使用模组:对话</a>
