---
title: "Item Queries"
wiki_source: "Modding:Item queries"
permalink: /Modding:Item_queries/
category: reference
tags: [item-queries, overview, valid-fields, query-format, argument-format, available-queries, general-use, specific-items]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents **item queries**, a built-in way to create one or
more items dynamically, instead of specifying a single item ID.

## Overview

### Valid fields

These are used in various places like
<a href="Modding_Machines" class="wikilink" title="machine data">machine
data</a> and
<a href="Modding_Shops" class="wikilink" title="shop data">shop data</a>.
These can only be used if the field's docs specifically mention that it
allows item queries.

### Query format

An item query consists of a string containing a query name with zero or
more <a href="#Argument_format" class="wikilink"
title="arguments">arguments</a>. See the
<a href="#Available_queries" class="wikilink"
title="list of queries below">list of queries below</a>.

**⚠** Item queries are partly case-sensitive. While some values are
case-insensitive, this isn't consistent. Using the exact capitalization
is recommended to avoid issues.

### Argument format

Item queries can take space-delimited arguments. For example,
`RANDOM_ITEMS (F) 1376 1390` has three arguments: `(F)`, `1376`, and
`1390`.

If you have spaces within an argument, you can surround it with quotes
to keep it together. For example, `LOST_BOOK_OR_ITEM "RANDOM_ITEMS (O)"`
passes `RANDOM_ITEMS (O)` as one argument. You can escape inner quotes
with backslashes if needed.

Remember that quotes and backslashes inside JSON strings need to be
escaped too. For example,
`"ItemId": "LOST_BOOK_OR_ITEM \"RANDOM_ITEMS (O)\""` will send
`LOST_BOOK_OR_ITEM "RANDOM_ITEMS (O)"` to the game code. Alternatively,
you can use single-quotes for the JSON string instead, like
`"ItemId": 'LOST_BOOK_OR_ITEM "RANDOM_ITEMS (O)"'`.

## Available queries

### General use

<table>
<thead>
<tr>
<th><p>query</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ALL_ITEMS [type ID] [flags]</samp></p></td>
<td><p>Every item provided by the <a href="Modding_Items"
class="wikilink" title="item data definitions">item data
definitions</a>. If [type ID] is set to an item type identifier (like
<samp>(O)</samp> for object), only returns items from the matching item
data definition.</p>
<p>The [flags] specify options to apply. If specified, they must be at
the end of the argument list (with or without [type ID]). The flags can
be any combination of:</p>
<table>
<thead>
<tr>
<th><p>flag</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>@isRandomSale</samp></p></td>
<td><p>Don't return items marked 'exclude from random sale' in
<samp>Data/Furniture</samp> or <samp>Data/Objects</samp>.</p></td>
</tr>
<tr>
<td><p><samp>@requirePrice</samp></p></td>
<td><p>Don't return items with a sell-to-player price below .</p></td>
</tr>
</tbody>
</table>
<p>For example:</p>
<ul>
<li><code>ALL_ITEMS</code> will return every item in the game.</li>
<li><code>ALL_ITEMS @isRandomSale</code> will return every item in the
game that's not excluded from random sale.</li>
<li><code>ALL_ITEMS (F) @isRandomSale</code> will return every furniture
item in the game that's not excluded from random sale.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>FLAVORED_ITEM &lt;type&gt; &lt;ingredient ID&gt;
[ingredient flavor ID]</samp></p></td>
<td><p>A flavored item like Apple Wine. The &lt;type&gt; can be one of
<a href="Wine" class="wikilink" title="Wine"><samp>Wine</samp></a>, <a
href="Jellies_and_Pickles" class="wikilink"
title="Jelly"><samp>Jelly</samp></a>, <a href="Jellies_and_Pickles"
class="wikilink" title="Pickle"><samp>Pickle</samp></a>, <a href="Juice"
class="wikilink" title="Juice"><samp>Juice</samp></a>, <a href="Roe"
class="wikilink" title="Roe"><samp>Roe</samp></a>, <a href="Aged_Roe"
class="wikilink" title="AgedRoe"><samp>AgedRoe</samp></a>, <a
href="Honey" class="wikilink" title="Honey"><samp>Honey</samp></a>, <a
href="Bait" class="wikilink" title="Bait"><samp>Bait</samp></a>, <a
href="Dried_Fruit" class="wikilink"
title="DriedFruit"><samp>DriedFruit</samp></a>, <a
href="Dried_Mushrooms" class="wikilink"
title="DriedMushroom"><samp>DriedMushroom</samp></a>, or <a
href="Smoked_Fish" class="wikilink"
title="SmokedFish"><samp>SmokedFish</samp></a>. The &lt;ingredient
ID&gt; is the qualified or unqualified item ID which provides the flavor
(like Apple in Apple Wine). For <samp>Honey</samp>, you can set the
&lt;flavor ID&gt; to <samp>-1</samp> for Wild Honey.</p>
<p>For aged roe only, the [ingredient flavor ID] is the flavor of the
&lt;ingredient ID&gt;. For example, <samp>FLAVORED_ITEM AgedRoe (O)812
128</samp> creates Aged Pufferfish Roe (812 is <a href="roe"
class="wikilink" title="roe">roe</a> and 128 is <a href="pufferfish"
class="wikilink" title="pufferfish">pufferfish</a>).</p></td>
</tr>
<tr>
<td><p><samp>RANDOM_ITEMS &lt;type definition ID&gt; [min ID] [max ID]
[flags]</samp></p></td>
<td><p>All items from the given <a href="Modding_Items#Item_types"
class="wikilink" title="type definition ID">type definition ID</a> in
randomized order, optionally filtered to those with a numeric ID in the
given [min ID] and [max ID] range (inclusive).</p>
<p>The [flags] specify options to apply. If specified, they must be at
the end of the argument list (with or without [min ID] and/or [max ID]).
The flags can be any combination of:</p>
<p>The flags can be any combination of:</p>
<table>
<thead>
<tr>
<th><p>flag</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>@isRandomSale</samp></p></td>
<td><p>Don't return items marked 'exclude from random sale' in
<samp>Data/Furniture</samp> or <samp>Data/Objects</samp>.</p></td>
</tr>
<tr>
<td><p><samp>@requirePrice</samp></p></td>
<td><p>Don't return items with a sell-to-player price below .</p></td>
</tr>
</tbody>
</table>
<p>For example, you can sell a random <a href="wallpaper"
class="wikilink" title="wallpaper">wallpaper</a> for in
<samp>Data/Shops</samp>:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;ItemId&quot;</span><span class="fu">:</span> <span class="st">&quot;RANDOM_ITEMS (WP)&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;MaxItems&quot;</span><span class="fu">:</span> <span class="dv">1</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Price&quot;</span><span class="fu">:</span> <span class="dv">200</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div>
<p>Or a random <a href="House_Plant" class="wikilink"
title="house plant">house plant</a>:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;ItemId&quot;</span><span class="fu">:</span> <span class="st">&quot;RANDOM_ITEMS (F) 1376 1390&quot;</span><span class="fu">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;MaxItems&quot;</span><span class="fu">:</span> <span class="dv">1</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div>
<p>Or a random <a href="Modding_Items" class="wikilink"
title="custom item">custom item</a> added by a mod by its item ID
prefix:</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;ItemId&quot;</span><span class="fu">:</span> <span class="st">&quot;RANDOM_ITEMS (O)&quot;</span><span class="fu">,</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;MaxItems&quot;</span><span class="fu">:</span> <span class="dv">1</span><span class="fu">,</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;PerItemCondition&quot;</span><span class="fu">:</span> <span class="st">&quot;ITEM_ID_PREFIX Target AuthorName.ModName_&quot;</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div>
<p>Or 10 random objects with any category except <samp>-13</samp> or
<samp>-14</samp>:</p>
<div class="sourceCode" id="cb4"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;ItemId&quot;</span><span class="fu">:</span> <span class="st">&quot;RANDOM_ITEMS (O)&quot;</span><span class="fu">,</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;MaxItems&quot;</span><span class="fu">:</span> <span class="dv">10</span><span class="fu">,</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;PerItemCondition&quot;</span><span class="fu">:</span> <span class="st">&quot;ITEM_CATEGORY, !ITEM_CATEGORY Target -13 -14&quot;</span></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

### Specific items

<table>
<thead>
<tr>
<th><p>query</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DISH_OF_THE_DAY</samp></p></td>
<td><p>The <a href="The_Stardrop_Saloon#Rotating_Stock" class="wikilink"
title="Saloon&#39;s dish of the day">Saloon's dish of the
day</a>.</p></td>
</tr>
<tr>
<td><p><samp>LOST_BOOK_OR_ITEM [alternate query]</samp></p></td>
<td><p>A <a href="Lost_Books" class="wikilink" title="lost book">lost
book</a> if the player hasn't found them all yet, else the result of the
[alternate query] if specified, else nothing.</p>
<p>For example, <code>LOST_BOOK_OR_ITEM (O)770</code> returns <a
href="Mixed_Seeds" class="wikilink" title="mixed seeds">mixed seeds</a>
if the player found every book already.</p></td>
</tr>
<tr>
<td><p><samp>RANDOM_BASE_SEASON_ITEM</samp></p></td>
<td><p>A random seasonal vanilla item which can be found by searching
garbage cans, breaking containers in the mines, etc.</p></td>
</tr>
<tr>
<td><p><samp>SECRET_NOTE_OR_ITEM [alternate query]</samp></p></td>
<td><p>A <a href="Secret_Notes" class="wikilink"
title="secret note">secret note</a> (or <a href="Journal_Scraps"
class="wikilink" title="journal scrap">journal scrap</a> on the island)
if the player hasn't found them all yet, else the result of the
[alternate query] if specified, else nothing.</p>
<p>For example, <code>SECRET_NOTE_OR_ITEM (O)390</code> returns <a
href="clay" class="wikilink" title="clay">clay</a> if the player found
every secret note already.</p></td>
</tr>
<tr>
<td><p><samp>SHOP_TOWN_KEY</samp></p></td>
<td><p>The special <a href="Key_To_The_Town" class="wikilink"
title="town key">town key</a> item. This is only valid in
shops.</p></td>
</tr>
</tbody>
</table>

### Specialized

<table>
<thead>
<tr>
<th><p>query</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ITEMS_SOLD_BY_PLAYER &lt;shop location&gt;</samp></p></td>
<td><p>Random items the player has recently sold to the &lt;shop
location&gt;, which can be one of <samp>SeedShop</samp> (Pierre's store)
or <samp>FishShop</samp> (Willy's fish shop).</p></td>
</tr>
<tr>
<td><p><samp>LOCATION_FISH &lt;location&gt; &lt;bobber tile&gt;
&lt;depth&gt;</samp></p></td>
<td><p>A random item that can be found by fishing in the given location.
The &lt;location&gt; should be the internal name of the location,
&lt;bobber tile&gt; is the position of the fishing rod's bobber in the
water (in the form <samp>&lt;x&gt; &lt;y&gt;</samp>), and &lt;depth&gt;
is the bobber's distance from the nearest shore measured in tiles (where
0 is directly adjacent to the shore).</p>
<p><strong>Careful:</strong> since the target location might use
<samp>LOCATION_FISH</samp> queries in its list, it's easy to cause a
circular reference by mistake (e.g. location A gets fish from B, which
gets fish from A). If this happens, the game will log an error and
return no item.</p></td>
</tr>
<tr>
<td><p><samp>MONSTER_SLAYER_REWARDS</samp></p></td>
<td><p>All items unlocked by <a
href="Adventurer&#39;s_Guild#Monster_Eradication_Goals" class="wikilink"
title="monster eradication goals">monster eradication goals</a> which
have been completed and collected from Gil by the current player at the
current time. The list sort order follows the order of monsters in
MonsterSlayerQuests.xnb, e.g., Slime Ring, Savage Ring, Burglar Ring,
etc.</p></td>
</tr>
<tr>
<td><p><samp>MOVIE_CONCESSIONS_FOR_GUEST [NPC name]</samp></p></td>
<td><p>Get the <a href="Movie_Theater#Concessions" class="wikilink"
title="movie concessions">movie concessions</a> shown when watching a
movie with the given [NPC name]. If omitted, the NPC defaults to the one
currently invited to watch a movie (or Abigail if none).</p></td>
</tr>
<tr>
<td><p><samp>RANDOM_ARTIFACT_FOR_DIG_SPOT</samp></p></td>
<td><p>A random item which is defined in <samp>Data/Objects</samp> with
the <samp>Arch</samp> (artifact) type, and whose spawn rules in the
<samp>Miscellaneous</samp> field match the current location and whose
random probability passes. This is mainly used by <a
href="Artifact_Spot" class="wikilink" title="artifact spots">artifact
spots</a>.</p></td>
</tr>
<tr>
<td><p><samp>TOOL_UPGRADES [tool ID]</samp></p></td>
<td><p>The tool upgrades listed in <samp>Data/Shops</samp> whose
conditions match the player's inventory (i.e. the same rules as <a
href="Blacksmith" class="wikilink"
title="Clint&#39;s tool upgrade shop">Clint's tool upgrade shop</a>). If
[tool ID] is specified, only upgrades which consume that tool ID are
shown.</p></td>
</tr>
</tbody>
</table>

## Item spawn fields

*Item spawn fields* are a common set of fields to use item queries in
data assets like <a href="Modding_Machines" class="wikilink"
title="machines">machines</a> and
<a href="Modding_Shops" class="wikilink" title="shops">shops</a>. These
are only available for data assets which specifically mention they
support item spawn fields in their docs.

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
entry (not the item itself) within the current list.</p>
<p>This is semi-optional — if omitted, it'll be auto-generated from the
<samp>ItemId</samp>, <samp>RandomItemId</samp>, and
<samp>IsRecipe</samp> fields. However multiple entries with the same ID
may cause unintended behavior (e.g. shop items reducing each others'
stock limits), so it's often a good idea to set a globally unique ID
instead.</p></td>
</tr>
<tr>
<td><p><samp>ItemId</samp></p></td>
<td><p>One of:</p>
<ul>
<li>the <a href="Modding_Items" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a> (like <samp>(O)128</samp> for a <a href="pufferfish"
class="wikilink" title="pufferfish">pufferfish</a>);</li>
<li>or an <a href="#Available_queries" class="wikilink"
title="item query">item query</a> to dynamically choose one or more
items.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>RandomItemId</samp></p></td>
<td><p><em>(Optional)</em> A list of item IDs to randomly choose from,
using the same format as <samp>ItemId</samp> (including item queries).
If set, <samp>ItemId</samp> is optional and ignored. Each entry in the
list has an equal probability of being chosen. For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="er">//</span> <span class="er">wood,</span> <span class="er">stone,</span> <span class="er">or</span> <span class="er">pizza</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RandomItemId&quot;</span><span class="er">:</span> <span class="ot">[</span> <span class="st">&quot;(O)388&quot;</span><span class="ot">,</span> <span class="st">&quot;(O)390&quot;</span><span class="ot">,</span> <span class="st">&quot;(O)206&quot;</span> <span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry should be applied. Defaults to always
true.</p>
<p><strong>Note:</strong> not supported for weapon projectiles.</p></td>
</tr>
<tr>
<td><p><samp>PerItemCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether an item produced from the other fields should be
returned. Defaults to always true.</p>
<p>For example, this can be used to filter queries like
<samp>RANDOM_ITEMS</samp>:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="er">//</span> <span class="er">random</span> <span class="er">mineral</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ItemId&quot;</span><span class="er">:</span> <span class="st">&quot;RANDOM_ITEMS (O)&quot;</span><span class="er">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;PerItemCondition&quot;</span><span class="er">:</span> <span class="st">&quot;ITEM_CATEGORY Target -12&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>MaxItems</samp></p></td>
<td><p><em>(Optional)</em> If this entry produces multiple separate item
stacks, the maximum number to return. (This does <em>not</em> affect the
size of each stack; see <samp>MinStack</samp> and <samp>MaxStack</samp>
for that.) Default unlimited.</p></td>
</tr>
<tr>
<td><p><samp>IsRecipe</samp></p></td>
<td><p><em>(Optional)</em> Whether to get the crafting/cooking recipe
for the item, instead of the item itself. Default false.</p>
<p>The game will unlock the recipe with the ID equal to the item query's
<samp>ObjectInternalName</samp> field, or the target item's internal
<samp>Name</samp> if not set.</p></td>
</tr>
<tr>
<td><p><samp>Quality</samp></p></td>
<td><p><em>(Optional)</em> The quality of the item to find. One of
<samp>0</samp> (normal), <samp>1</samp> (silver), <samp>2</samp> (gold),
or <samp>4</samp> (iridium). Invalid values will snap to the closest
valid one (e.g. <samp>7</samp> will become iridium). Default -1, which
keeps the value set by the item query (usually 0).</p></td>
</tr>
<tr>
<td><p><samp>MinStack</samp></p></td>
<td><p><em>(Optional)</em> The item's minimum and default stack size.
Default -1, which keeps the value set by the item query (usually
1).</p></td>
</tr>
<tr>
<td><p><samp>MaxStack</samp></p></td>
<td><p><em>(Optional)</em> If set to a value higher than
<samp>MinStack</samp>, the stack is set to a random value between them
(inclusively). Default -1.</p></td>
</tr>
<tr>
<td><p><samp>ObjectInternalName</samp></p></td>
<td><p><em>(Optional)</em> For objects only, the internal name to use.
Defaults to the item's name in <samp>Data/Objects</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ObjectDisplayName</samp></p></td>
<td><p><em>(Optional)</em> For objects only, a <a
href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the item's display
name. Defaults to the item's display name in <samp>Data/Objects</samp>.
This can optionally contain <code>%DISPLAY_NAME</code> (the item's
default display name) and <code>%PRESERVED_DISPLAY_NAME</code> (the
preserved item's display name if applicable, <em>e.g.</em> if set via
<samp>PreserveId</samp> in <a href="Modding_Machines" class="wikilink"
title="machine data">machine data</a>).</p>
<p><strong>Careful:</strong> text in this field will be saved
permanently in the object's info and won't be updated when the player
changes language or the content pack changes. That includes Content
Patcher translations (like <code>%DISPLAY_NAME</code>), which will save
the translated text for the current language. Instead, add the text to a
strings asset like <samp>Strings/Objects</samp> and then use the <a
href="Modding_Tokenizable_strings" class="wikilink"
title="[LocalizedText] token"><samp>[LocalizedText]</samp>
token</a>.</p></td>
</tr>
<tr>
<td><p><samp>ObjectColor</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Color" class="wikilink"
title="tint color">tint color</a> to apply to the produced item. Default
none.</p></td>
</tr>
<tr>
<td><p><samp>ToolUpgradeLevel</samp></p></td>
<td><p><em>(Optional)</em> For tools only, the initial upgrade level for
the tool when created (like <a href="Axes" class="wikilink"
title="Copper vs Gold Axe">Copper vs Gold Axe</a>, or <a
href="Training_Rod" class="wikilink" title="Training Rod">Training
Rod</a> vs <a href="Iridium_Rod" class="wikilink"
title="Iridium Rod">Iridium Rod</a>). Default -1, which keeps the value
set by the item query (usually 0).</p></td>
</tr>
<tr>
<td><p><samp>QualityModifiers</samp><br />
<samp>StackModifiers</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Common_data_field_types#Quantity_modifiers"
class="wikilink" title="Quantity modifiers">Quantity modifiers</a>
applied to the <samp>Quality</samp> or <samp>Stack</samp> value. Default
none.</p>
<p>The quality modifiers operate on the numeric quality values
(<em>i.e.</em> <samp>0</samp> = normal, <samp>1</samp> = silver,
<samp>2</samp> = gold, and <samp>4</samp> = iridium). For example,
silver × 2 is gold.</p></td>
</tr>
<tr>
<td><p><samp>QualityModifierMode</samp><br />
<samp>StackModifierMode</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Common_data_field_types#Quantity_modifiers"
class="wikilink" title="Quantity modifier modes">Quantity modifier
modes</a> which indicate what to do if multiple modifiers in the
<samp>QualityModifiers</samp> or <samp>StackModifiers</samp> field apply
at the same time. Default <samp>Stack</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ModData</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Mod_data" class="wikilink"
title="mod data fields">mod data fields</a> to add to created items.
Default none.</p>
<p>For example:</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ModData&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Example.ModId_FieldName&quot;</span><span class="fu">:</span> <span class="st">&quot;some custom data&quot;</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

## For C# mod authors

### Use queries in custom data assets

You can use the `ItemQueryResolver` class to parse item queries.

For example, let's say a custom data model uses
<a href="#Item_spawn_fields" class="wikilink"
title="item spawn fields">item spawn fields</a> to choose which gifts
are added to the starting gift box:

``` c#
public class InitialGiftsModel
{
    public List<GenericSpawnItemData> Items = new();
}
```

You can spawn items from it like this:

``` c#
ItemQueryContext itemQueryContext = new();
foreach (GenericSpawnItemData entry in model.Items)
{
    Item item = ItemQueryResolver.TryResolveRandomItem(entry, itemQueryContext, logError: (query, message) => this.Monitor.Log($"Failed parsing item query '{query}': {message}", LogLevel.Warn));
    // or TryResolve to get all items
}
```

You can also use `GenericSpawnItemDataWithCondition` to combine it with
<a href="Modding_Game_state_queries" class="wikilink"
title="game state queries">game state queries</a>:

``` c#
ItemQueryContext itemQueryContext = new();
foreach (GenericSpawnItemDataWithCondition entry in model.Items)
{
    if (!GameStateQuery.CheckConditions(entry.Condition))
        continue;

    Item item = ItemQueryResolver.TryResolveRandomItem(entry, itemQueryContext, logError: (query, message) => this.Monitor.Log($"Failed parsing item query '{query}': {message}", LogLevel.Warn));
}
```

### Add custom item queries

You can define new item queries
`ItemQueryResolver.Register("Example.ModId_QueryName", handleQueryMethod)`.
To avoid conflicts, custom query names should apply the
<a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a>
conventions.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Запросы_предметов" class="wikilink"
title="ru:Модификации:Запросы предметов">ru:Модификации:Запросы
предметов</a> <a href="zh_模组_物品查询" class="wikilink"
title="zh:模组:物品查询">zh:模组:物品查询</a>
