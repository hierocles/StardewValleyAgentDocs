---
title: "Special Orders"
wiki_source: "Modding:Special orders"
permalink: /Modding:Special_orders/
category: world-systems
tags: [special-orders, raw-data, format, basic-fields, randomized-elements, objectives, rewards, context-tags]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

<a href="Quests#Quests#List_of_Special_Orders" class="wikilink"
title="Special orders">Special orders</a> are a more flexible and
customizable <a href="Quests" class="wikilink" title="quest">quest</a>
system unlocked in late game. Special orders can be added to
<a href="#Raw_data" class="wikilink" title="the data file">the data
file</a> with options like duration, repeatability, objectives, and
rewards.

This page explains how the game stores and uses special orders. This is
an advanced guide for mod developers.

## Raw data

Special orders are stored in `Content\Data\SpecialOrders.xnb`, which can
be <a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of :

## Format

### Basic Fields

Each special order has a few basic fields, as well as some more complex
fields (which are explained below).

<table>
<thead>
<tr>
<th><p>Field Name</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p>Name of the special order. This is in brackets, referring to a
string in <samp>Strings/SpecialOrderStrings</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Requester</samp></p></td>
<td><p>The name of the NPC the order is for. Can take the form of
non-friendable NPCs such as Qi or Gunther.</p></td>
</tr>
<tr>
<td><p><samp>Duration</samp></p></td>
<td><p>How long you have to complete the order before it auto-fails. Can
be one of the following: <samp>OneDay</samp>, <samp>ThreeDays</samp>,
<samp>Week</samp>, <samp>TwoWeeks</samp>, or
<samp>Month</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Repeatable</samp></p></td>
<td><p>Whether or not the order can be repeated. Either
<samp>true</samp> or <samp>false</samp>.</p></td>
</tr>
<tr>
<td><p><samp>RequiredTags</samp></p></td>
<td><p>Defines conditions for the order appearing. Can be one or several
of the following in a comma-delimited list:</p>
<ul>
<li><samp>season_&lt;season&gt;</samp>: must currently be the specified
season.</li>
<li><samp>event_&lt;ID&gt;</samp>: the host player has seen the event
with the specified ID.</li>
<li><samp>mail_&lt;ID&gt;</samp>: the host player has the specified mail
key.</li>
<li><samp>rule_&lt;name&gt;</samp>: the specified rule is in effect.
(See below.)</li>
<li><samp>dropbox_&lt;name&gt;</samp>: the specified dropbox is
currently in use by another quest or special order. (See below.)</li>
<li><samp>island</samp>: Ginger Island has been unlocked. This also adds
an island motif to the note.</li>
<li><samp>knows_&lt;NPCname&gt;</samp>: Returns true if any farmer knows
the specified NPC.</li>
<li><samp>NOT_IMPLEMENTED</samp>: Always returns false.</li>
</ul>
<p>Additionally, requirements may be prefixed with <samp>!</samp> to
invert the condition. For example, <samp>!dropbox_&lt;name&gt;</samp>
returns true only if the specified dropbox is <em>not</em> in
use.</p></td>
</tr>
<tr>
<td><p><samp>OrderType</samp></p></td>
<td><p>Is either blank (for the town board), <samp>Qi</samp> (for Qi's
board) or <samp>DesertFestivalMarlon</samp> (for Marlon's desert
festival challenges). Mods can add their own special order boards that
only fetch orders of a certain type.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p>A <a href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> which determines whether
this order can appear.</p></td>
</tr>
<tr>
<td><p><samp>SpecialRule</samp></p></td>
<td><p>A comma-delimited list of <a href="#Special_rules"
class="wikilink" title="special rules">special rules</a> that apply
while this special order is active.</p></td>
</tr>
<tr>
<td><p><samp>Text</samp></p></td>
<td><p>Put in brackets, refers to a string in
<samp>Strings/SpecialOrderStrings</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ItemToRemoveOnEnd</samp></p></td>
<td><p>Removes all instances of the specified item ID from all
inventories and containers. Used to prevent keeping hold of quest
items.</p></td>
</tr>
<tr>
<td><p><samp>MailToRemoveOnEnd</samp></p></td>
<td><p>Sets the specified mail as unread.</p></td>
</tr>
<tr>
<td><p><samp>Objectives</samp></p></td>
<td><p>The <a href="#Objectives" class="wikilink"
title="objectives">objectives</a> for this order.</p></td>
</tr>
<tr>
<td><p><samp>Rewards</samp></p></td>
<td><p>The <a href="#Rewards" class="wikilink"
title="rewards">rewards</a> upon completing this order.</p></td>
</tr>
<tr>
<td><p><samp>RandomizedElements</samp></p></td>
<td><p>The <a href="#Randomized_Elements" class="wikilink"
title="randomized elements">randomized elements</a> of this
order.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

### Randomized Elements

This field, if not null, is a collection of blocks, each representing a
random element. The format for each one is as follows:

<table>
<thead>
<tr>
<th><p>Field Name</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p>The name of the random element, used within the special order
data and in the order's strings in
<samp>Strings/SpecialOrderStrings</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Values</samp></p></td>
<td><p>A list of blocks, each containing required tags and a value to
set the random element to if the tags are met. <samp>RequiredTags</samp>
here follows the same format as the field of the same name in the main
block. (See above.)</p>
<p><samp>Value</samp> is a text string in the following format:</p>
<ul>
<li>If randomly selecting items, the format is: <samp>PICK_ITEM,
&lt;item name&gt;, &lt;item name&gt;, &lt;item name&gt;...</samp>. Items
are checking for an ID match then if there's none, their internal names,
i.e. field 0 in <samp>Data/ObjectInformation</samp>.</li>
<li>If randomly selecting groups of items by context tag, the format is:
<samp>Text|[&lt;string key&gt;]|Tags|&lt;context tags&gt;</samp>.</li>
<li>If randomly selecting a monster, the format is:
<samp>Target|&lt;monster name&gt;|LocalizedName|[&lt;string
key&gt;]</samp></li>
<li>If simply setting the value of the random element to a string in
<samp>Strings/SpecialOrderStrings</samp>, the format is simply:
<samp>[&lt;string key&gt;]</samp>.</li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Random elements can then be called in the following ways, depending on
what the format of their `Value` field is:

- If the random element is simply a string, just the random element name
  surrounded by single curly braces will return the string.
- `{<element name>:Text}`: If the random element is an item, returns its
  name.
- `{<element name>:TextPlural}`: If the random element is an item,
  returns its name in plural form.
- `{<element name>:TextPluralCapitalized}`: If the random element is an
  item, returns its name in plural form, capitalized.
- `{<element name>:Tags}`: If the random element is an item, returns its
  tags.
- `{<element name>:Price}`: If the random element is an item, returns
  its price.
- `{<element name>:Target}`: If the random element is a monster, returns
  its name.

### Objectives

Each order can have any number of objectives of the given types. The
format for each objective is below:

| Field Name | Description |
|----|----|
| `Type` | The type of objective; see below for a list of possible objective types. |
| `Text` | The description of the objective. This is in brackets, referring to a string in `Strings/SpecialOrderStrings`. |
| `RequiredCount` | The number required for the objective, depending on its type (items to collect, monsters to slay, etc.). |
| `Data` | The extra data required for this special order objective. Each objective type requires different fields. |
|  |  |

The following is a list of possible objective types, as well as the data
they expect in the `Data` field:

<table>
<thead>
<tr>
<th><p>Objective type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Collect</samp></p></td>
<td><p>The player must obtain items that match the <a
href="#Context_tags" class="wikilink"
title="AcceptedContextTags field"><samp>AcceptedContextTags</samp>
field</a>. The items must never have been in a player inventory. This
applies to any method of collecting items (<em>e.g.,</em> harvesting
crops, slaying monsters, collecting from a machine, cooking a dish,
etc). There's no restriction to how the item can be collected;
<em>e.g.,</em> a special order for emeralds will be equally find with
gems found in the mines or produced in a crystalarium.</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Collect&quot;</span><span class="op">,</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[Willy_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;100&quot;</span><span class="op">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;AcceptedContextTags&quot;</span><span class="op">:</span> <span class="st">&quot;item_bug_meat&quot;</span><span class="op">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Deliver</samp></p></td>
<td><p>The player must give items that match the <a href="#Context_tags"
class="wikilink"
title="AcceptedContextTags field"><samp>AcceptedContextTags</samp>
field</a> to a given character. This doesn't count towards the
character's gift limit.</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Deliver&quot;</span><span class="op">,</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[Emily_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;1&quot;</span><span class="op">,</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;AcceptedContextTags&quot;</span><span class="op">:</span> <span class="st">&quot;item_ruby&quot;</span><span class="op">,</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;TargetName&quot;</span><span class="op">:</span> <span class="st">&quot;Emily&quot;</span><span class="op">,</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Fish</samp></p></td>
<td><p>Equivalent to <samp>Collect</samp>, but only counts items found
by <a href="fishing" class="wikilink" title="fishing">fishing</a>.</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Fish&quot;</span><span class="op">,</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[Demetrius_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;10&quot;</span><span class="op">,</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;AcceptedContextTags&quot;</span><span class="op">:</span> <span class="st">&quot;{FishType:Tags}&quot;</span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Gift</samp></p></td>
<td><p>The player must give items that match the <a href="#Context_tags"
class="wikilink"
title="AcceptedContextTags field"><samp>AcceptedContextTags</samp>
field</a> to a given character. This <strong>does</strong> count towards
the character's gift limit. Parameters can include a minimum gift taste
level.</p>
<div class="sourceCode" id="cb4"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Gift&quot;</span><span class="op">,</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[QiChallenge7_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;50&quot;</span><span class="op">,</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;MinimumLikeLevel&quot;</span><span class="op">:</span> <span class="st">&quot;Loved&quot;</span> <span class="co">// Possible values: None, Hated, Disliked, Neutral, Liked, Loved</span></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>JKScore</samp></p></td>
<td><p>The player must achieve at least the given score in <a
href="Junimo_Kart" class="wikilink" title="Junimo Kart">Junimo Kart</a>.
This tracks the highest score reached while the special order is
active.</p>
<div class="sourceCode" id="cb5"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;JKScore&quot;</span><span class="op">,</span></span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[QiChallenge3_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;50000&quot;</span><span class="op">,</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>ReachMineFloor</samp></p></td>
<td><p>The player must reach or exceed the given floor in the <a
href="The_Mines" class="wikilink" title="mines">mines</a> or the <a
href="Skull_Cavern" class="wikilink" title="Skull Cavern">Skull
Cavern</a> (depending on the <samp>SkullCave</samp> field) while the
special order is active.</p>
<div class="sourceCode" id="cb6"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;ReachMineFloor&quot;</span><span class="op">,</span></span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[QiChallenge5_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;100&quot;</span><span class="op">,</span></span>
<span id="cb6-4"><a href="#cb6-4" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb6-5"><a href="#cb6-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;SkullCave&quot;</span><span class="op">:</span> <span class="st">&quot;true&quot;</span> <span class="co">// or &quot;false&quot;</span></span>
<span id="cb6-6"><a href="#cb6-6" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Ship</samp></p></td>
<td><p>The player must ship items through their <a href="Shipping"
class="wikilink" title="shipping bin">shipping bin</a> which match the
<a href="#Context_tags" class="wikilink"
title="AcceptedContextTags field"><samp>AcceptedContextTags</samp>
field</a>. The quest objective progresses when the items are collected,
not when they're put in the bin. Player still get money for the shipped
items as they would normally. The <samp>UseShipmentValue</samp> field
(<samp>"false"</samp> by default) can be set to <samp>"true"</samp> to
require shipping a certain amount of money worth of items, instead of a
certain number of items.</p>
<div class="sourceCode" id="cb7"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Ship&quot;</span><span class="op">,</span></span>
<span id="cb7-2"><a href="#cb7-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[QiChallenge6_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb7-3"><a href="#cb7-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;100000&quot;</span><span class="op">,</span></span>
<span id="cb7-4"><a href="#cb7-4" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb7-5"><a href="#cb7-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;AcceptedContextTags&quot;</span><span class="op">:</span> <span class="st">&quot;quality_qi&quot;</span><span class="op">,</span></span>
<span id="cb7-6"><a href="#cb7-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;UseShipmentValue&quot;</span><span class="op">:</span> <span class="st">&quot;True&quot;</span></span>
<span id="cb7-7"><a href="#cb7-7" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Donate</samp></p></td>
<td><p>The player must add items that match the <a href="#Context_tags"
class="wikilink"
title="AcceptedContextTags field"><samp>AcceptedContextTags</samp>
field</a> to a dropbox. The map for the associated DropBoxGameLocation
must have a DropBox Action that matches the DropBox value given in this
objective for the player to access it. See <a href="Modding_Maps#Action"
class="wikilink" title="Modding:Maps#Action">Modding:Maps#Action</a>.
<samp>MinimumCapacity</samp> can be set to resize the capacity of the
dropoff box (9 by default).</p>
<div class="sourceCode" id="cb8"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Donate&quot;</span><span class="op">,</span></span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[QiChallenge12_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;100&quot;</span><span class="op">,</span></span>
<span id="cb8-4"><a href="#cb8-4" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb8-5"><a href="#cb8-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;DropBox&quot;</span><span class="op">:</span> <span class="st">&quot;QiChallengeBox&quot;</span><span class="op">,</span></span>
<span id="cb8-6"><a href="#cb8-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;DropBoxGameLocation&quot;</span><span class="op">:</span> <span class="st">&quot;QiNutRoom&quot;</span><span class="op">,</span></span>
<span id="cb8-7"><a href="#cb8-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;DropBoxIndicatorLocation&quot;</span><span class="op">:</span> <span class="st">&quot;1 3&quot;</span><span class="op">,</span></span>
<span id="cb8-8"><a href="#cb8-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;MinimumCapacity&quot;</span><span class="op">:</span> <span class="st">&quot;36&quot;</span><span class="op">,</span></span>
<span id="cb8-9"><a href="#cb8-9" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;AcceptedContextTags&quot;</span><span class="op">:</span> <span class="st">&quot;color_red/color_dark_red&quot;</span></span>
<span id="cb8-10"><a href="#cb8-10" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Slay</samp></p></td>
<td><p>The player must kill a minimum number of monsters of the given
name while the special order is active. If
<samp>IgnoreFarmMonsters</samp> is set, this will not count monsters on
the farm.</p>
<div class="sourceCode" id="cb9"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb9-1"><a href="#cb9-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Slay&quot;</span><span class="op">,</span></span>
<span id="cb9-2"><a href="#cb9-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Text&quot;</span><span class="op">:</span> <span class="st">&quot;[Clint_Objective_0_Text]&quot;</span><span class="op">,</span></span>
<span id="cb9-3"><a href="#cb9-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RequiredCount&quot;</span><span class="op">:</span> <span class="st">&quot;50&quot;</span><span class="op">,</span></span>
<span id="cb9-4"><a href="#cb9-4" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb9-5"><a href="#cb9-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;TargetName&quot;</span><span class="op">:</span> <span class="st">&quot;{Monster:Target}&quot;</span><span class="op">,</span></span>
<span id="cb9-6"><a href="#cb9-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;IgnoreFarmMonsters&quot;</span><span class="op">:</span> <span class="st">&quot;true&quot;</span></span>
<span id="cb9-7"><a href="#cb9-7" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
</tbody>
</table>

### Rewards

Each order can have any number of rewards of the given types. The format
for each reward is below:

| Field Name | Description |
|----|----|
| `Type` | The type of reward; see below for a list of possible reward types. |
| `Data` | The extra data required for this special order reward. Each reward type requires different fields. |
|  |  |

The following is a list of possible rewards types, as well as the data
they expect in the `Data` field:

<table>
<thead>
<tr>
<th><p>Reward</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Friendship</samp></p></td>
<td><p>Increases the amount of <a href="Friendship" class="wikilink"
title="friendship">friendship</a>, which is by default 250 points (1
heart) and for the requesting NPC. If specified, the units are in terms
of number of friendship points, not hearts.</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Friendship&quot;</span><span class="op">,</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Amount&quot;</span><span class="op">:</span> <span class="st">&quot;Number of friendship points to add&quot;</span><span class="op">,</span> <span class="co">// integer</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;TargetName&quot;</span><span class="op">:</span> <span class="st">&quot;Name of NPC to add them to&quot;</span> <span class="co">// string</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Gems</samp></p></td>
<td><p>Rewards the farmer a set amount of <a href="Qi_Gem"
class="wikilink" title="Qi Gems">Qi Gems</a>.</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Gems&quot;</span><span class="op">,</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Amount&quot;</span><span class="op">:</span> <span class="st">&quot;Number of Qi Gems to award&quot;</span> <span class="co">// integer</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Mail</samp></p></td>
<td><p>Sets a mail flag, which can be used to trigger custom events,
dialogue, or other changes. "MailReceived" sets the name of the mail
flag that is set upon completion of the special order. "NoLetter"
controls whether there is an actual letter corresponding to the mail
flag, and is true by default (no mail sent). "Host" seems to be intended
to control whether only the host receives the quest completion letter,
but due to "send to everyone" being always true, appears to have no real
effect in the game. (TODO: verify this.) "Host" is false by default.</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Mail&quot;</span><span class="op">,</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;MailReceived&quot;</span><span class="op">:</span> <span class="st">&quot;Name of mail flag&quot;</span><span class="op">,</span> <span class="co">// string</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;NoLetter&quot;</span><span class="op">:</span> <span class="st">&quot;true/false&quot;</span><span class="op">,</span> <span class="co">// boolean</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Host&quot;</span><span class="op">:</span> <span class="st">&quot;true/false&quot;</span> <span class="co">// boolean</span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Money</samp></p></td>
<td><p>Rewards the farmer a set amount of money or a value that depends
on the donated item. The total money rewarded is
<code>Amount * Multiplier</code>.</p>
<div class="sourceCode" id="cb4"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Money&quot;</span><span class="op">,</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Amount&quot;</span><span class="op">:</span> <span class="st">&quot;Amount of money&quot;</span><span class="op">,</span> <span class="co">// integer</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Multiplier&quot;</span><span class="op">:</span> <span class="st">&quot;Multiplier on amount&quot;</span> <span class="co">// float</span></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>ResetEvent</samp></p></td>
<td><p>Removes the event IDs from the list of event IDs seen by the
player, thus making the events repeatable.</p>
<div class="sourceCode" id="cb5"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;ResetEvent&quot;</span><span class="op">,</span></span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;ResetEvents&quot;</span><span class="op">:</span> <span class="st">&quot;eventID1 eventID2 eventID3&quot;</span> <span class="co">// space-separated integers</span></span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Object</samp></p></td>
<td><p>Rewards the farmer with an item.</p>
<div class="sourceCode" id="cb6"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Type&quot;</span><span class="op">:</span> <span class="st">&quot;Object&quot;</span><span class="op">,</span></span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Data&quot;</span><span class="op">:</span> {</span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Item&quot;</span><span class="op">:</span> <span class="st">&quot;CalicoEgg&quot;</span><span class="op">,</span> <span class="co">// string</span></span>
<span id="cb6-4"><a href="#cb6-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Amount&quot;</span><span class="op">:</span> <span class="st">&quot;40&quot;</span> <span class="co">// integer</span></span>
<span id="cb6-5"><a href="#cb6-5" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
</tbody>
</table>

### Context tags

The `AcceptedContextTags` fields in the `Data` field of certain special
order objectives specify <a href="Modding_Context_tags" class="wikilink"
title="context tags">context tags</a> for required items. This consists
of a string with the following format:

| syntax | effect |
|----|----|
| `!` | When prefixed to a context tag, indicates that an item must *not* have that tag. |
| `,` | Separates any number of required context tags. For example, `A, B, C` matches items that have *all* of those tags. |
| `/` | Separates any number of alternate context tags. For example, `A/B/C` matches items that have *at least one* of those tags. |

For example,
`!forage_item, category_vegetable/category_fruit, quality_gold` would
match non-forage gold-quality items which are either fruits or
vegetables.

## Special rules

Special rules are
<a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string IDs">unique string IDs</a> that
can be used to apply logic while the special order is active.

The game has some predefined rules:

<table>
<thead>
<tr>
<th><p>rule ID</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DROP_QI_BEANS</samp></p></td>
<td><p>The player can find <a href="Qi_Bean" class="wikilink"
title="Qi Bean">Qi Beans</a> for the <em>Qi's Crop</em> order.</p></td>
</tr>
<tr>
<td><p><samp>LEGENDARY_FAMILY</samp></p></td>
<td><p>The player can catch the new legendary fish for the <em>Extended
Family</em> order.</p></td>
</tr>
<tr>
<td><p><samp>MINE_HARD</samp><br />
<samp>SC_HARD</samp></p></td>
<td><p>Raises the difficulty level of the mines or <a
href="Skull_Cavern" class="wikilink" title="Skull Cavern">Skull
Cavern</a>.</p></td>
</tr>
<tr>
<td><p><samp>SC_NO_FOOD</samp></p></td>
<td><p>The player can't eat food in the <a href="Skull_Cavern"
class="wikilink" title="Skull Cavern">Skull Cavern</a>.</p></td>
</tr>
<tr>
<td><p><samp>QI_BEANS</samp></p></td>
<td><p>Remove all <a href="Qi_Bean" class="wikilink" title="Qi Bean">Qi
Beans</a> and <a href="Qi_Fruit" class="wikilink" title="Qi Fruit">Qi
Fruits</a> from player and chest inventories when the special order
ends. Similar effects for other items can be achieved with the
<samp>ItemToRemoveOnEnd</samp> field.</p></td>
</tr>
<tr>
<td><p><samp>QI_COOKING</samp></p></td>
<td><p>Food cooked during the special order has the "Fresh" prefix and
the <a href="Modding_Context_tags" class="wikilink"
title="quality_qi"><samp>quality_qi</samp></a> context tag.</p></td>
</tr>
<tr>
<td><p><samp>FIVE_PLAGUES</samp><br />
<samp>QI_DOUBLE</samp></p></td>
<td><p>Unused.</p></td>
</tr>
</tbody>
</table>

Special orders can also have arbitrary rule IDs, which can be checked
using <a href="Modding_Game_state_queries" class="wikilink"
title="game state queries">game state queries</a> (via
`PLAYER_SPECIAL_ORDER_RULE_ACTIVE`) or in C# (via
`Game1.player.team.SpecialOrderRuleActive`).

## See also

- <a href="Modding_Quest_data" class="wikilink"
  title="Modding:Quest data">Modding:Quest data</a>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Особые_задания" class="wikilink"
title="ru:Модификации:Особые задания">ru:Модификации:Особые задания</a>
<a href="zh_模组_特别任务" class="wikilink"
title="zh:模组:特别任务">zh:模组:特别任务</a>
