---
title: "Garbage Cans"
wiki_source: "Modding:Garbage cans"
permalink: /Modding:Garbage_cans/
category: game
tags: [garbage-cans, format, examples, new-garbage-can, change-an-existing-garbage-can, changes-for-c-mods]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains garbage cans. This is an advanced guide for mod
developers.

## Format

You can add or edit
<a href="Garbage_Can" class="wikilink" title="garbage cans">garbage
cans</a> on any map by editing the `Data/GarbageCans` asset (see
examples below).

The asset consists of a data model with these fields:

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DefaultBaseChance</samp></p></td>
<td><p>The probability that an item will be found when searching garbage
cans, as a value between 0 (never) and 1 (always). If the probability
check fails, only items that set <samp>IgnoreBaseChance</samp> can
spawn. This can be overridden by the per-garbage-can
<samp>BaseChance</samp> field. Default 0.2.</p></td>
</tr>
<tr>
<td><p><samp>BeforeAll</samp><br />
<samp>AfterAll</samp></p></td>
<td><p>The items to prepend (<samp>BeforeAll</samp>) or append
(<samp>AfterAll</samp>) to the <samp>GarbageCans</samp> →
<samp>Items</samp> field for all garbage cans. These work exactly like
the items in that field (e.g. subject to the garbage can's base
chance).</p></td>
</tr>
<tr>
<td><p><samp>GarbageCans</samp></p></td>
<td><p>The data for individual garbage cans. This consists of a string →
model lookup with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><em>entry key</em></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
garbage can.</p></td>
</tr>
<tr>
<td><p><samp>BaseChance</samp></p></td>
<td><p><em>(Optional)</em> If set, overrides the root
<samp>DefaultBaseChance</samp> field for this garbage can. Defaults to
<samp>DefaultBaseChance</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Items</samp></p></td>
<td><p><em>(Optional)</em> The items to try spawning when the player
searches the garbage can. The first matching item in
<samp>BeforeAll</samp> + <samp>Items</samp> + <samp>AfterAll</samp> will
be spawned, and any further items will be ignored. Defaults to none.</p>
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
generic item fields supported by garbage cans.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>IgnoreBaseChance</samp></p></td>
<td><p><em>(Optional)</em> Whether this item can spawn even if the
<samp>BaseChance</samp> probability check didn't pass. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>IsMegaSuccess</samp></p></td>
<td><p><em>(Optional)</em> Whether to treat this item as a 'mega
success' if it's selected, which plays a special <samp>crit</samp> sound
and bigger animation. Default false.</p></td>
</tr>
<tr>
<td><p><samp>IsDoubleMegaSuccess</samp></p></td>
<td><p><em>(Optional)</em> Whether to treat this item as an 'double mega
success' if it's selected, which plays an explosion sound and dramatic
animation. Default false.</p></td>
</tr>
<tr>
<td><p><samp>AddToInventoryDirectly</samp></p></td>
<td><p><em>(Optional)</em> Whether to add the item to the player's
inventory directly, opening an item grab menu if they don't have room in
their inventory. If false, the item will be dropped on the ground next
to the garbage can instead. Default false.</p></td>
</tr>
<tr>
<td><p><samp>CreateMultipleDebris</samp></p></td>
<td><p><em>(Optional)</em> Whether to split the spawned item into
multiple stacks which each have a stack size of one. This has no effect
if <samp>AddToInventoryDirectly</samp> is enabled. Default
false.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p>If the garbage can being searched doesn't have its own entry under
<samp>GarbageCans</samp>, the game will just use the
<samp>BeforeAll</samp> and <samp>AfterAll</samp> fields.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

## Examples

### New garbage can

You can add garbage cans using only
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> or
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="SMAPI&#39;s content API">SMAPI's content API</a>. For example,
this content pack adds a new garbage can entry with the ID
`Example.ModId_Carpenter`:

Then you'd place an `Action: Garbage Example.ModId_Carpenter`
<a href="Modding_Maps" class="wikilink" title="map tile property">map
tile property</a> to mark a tile as a garbage can using this data.

### Change an existing garbage can

You can edit an existing garbage cans using only
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> or
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="SMAPI&#39;s content API">SMAPI's content API</a>. For example,
this content pack adds pufferfish to the Saloon garbage can, and moves
it above the dish of the day.

Note that this uses `TargetField` to 'move into' the item list for the
saloon, and then treat those items as the entry list being edited.
Specifying an ID which isn't in the list will add a new entry, just like
when editing a regular list asset.

## Changes for C# mods

Previously garbage cans were tracked by `Town.garbageChecked`, an array
of boolean fields. That approach doesn't work in Stardew Valley 1.6,
since we're no longer limited to a specific set of garbage cans in the
town map. This has been replaced by
`Game1.netWorldState.Value.CheckedGarbage`, which is a hash set of
garbage can IDs.

To migrate code:

<table>
<thead>
<tr>
<th><p>action</p></th>
<th><p>code in 1.5.6</p></th>
<th><p>code in 1.6</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>check if a garbage can was searched</p></td>
<td><div class="sourceCode" id="cb1"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>Town town <span class="op">=</span> <span class="op">(</span>Town<span class="op">)</span>Game1<span class="op">.</span><span class="fu">getLocationFromName</span><span class="op">(</span><span class="st">&quot;Town&quot;</span><span class="op">);</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="kw">if</span> <span class="op">(</span>town<span class="op">.</span><span class="fu">garbageChecked</span><span class="op">[</span><span class="dv">5</span><span class="op">])</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>   <span class="op">...</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="kw">if</span> <span class="op">(</span>Game1<span class="op">.</span><span class="fu">netWorldState</span><span class="op">.</span><span class="fu">Value</span><span class="op">.</span><span class="fu">CheckedGarbage</span><span class="op">.</span><span class="fu">Contains</span><span class="op">(</span><span class="st">&quot;Saloon&quot;</span><span class="op">))</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>   <span class="op">...</span></span></code></pre></div></td>
</tr>
<tr>
<td><p>mark a garbage can searched</p></td>
<td><div class="sourceCode" id="cb3"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>Town town <span class="op">=</span> <span class="op">(</span>Town<span class="op">)</span>Game1<span class="op">.</span><span class="fu">getLocationFromName</span><span class="op">(</span><span class="st">&quot;Town&quot;</span><span class="op">);</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>town<span class="op">.</span><span class="fu">garbageChecked</span><span class="op">[</span><span class="dv">5</span><span class="op">]</span> <span class="op">=</span> <span class="kw">true</span><span class="op">;</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb4"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>Game1<span class="op">.</span><span class="fu">netWorldState</span><span class="op">.</span><span class="fu">Value</span><span class="op">.</span><span class="fu">CheckedGarbage</span><span class="op">.</span><span class="fu">Add</span><span class="op">(</span><span class="st">&quot;Saloon&quot;</span><span class="op">);</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

To migrate former vanilla trash can IDs:

| position | ID in 1.5.6 | ID in 1.6 |
|----|----|----|
| Near <a href="Jodi" class="wikilink" title="Jodi">Jodi</a> and <a href="Kent" class="wikilink" title="Kent">Kent</a>'s house | `0` | `JodiAndKent` |
| Near <a href="Emily" class="wikilink" title="Emily">Emily</a> and <a href="Haley" class="wikilink" title="Haley">Haley</a>'s house | `1` | `EmilyAndHaley` |
| Near <a href="Lewis" class="wikilink" title="Lewis">Lewis</a>' house | `2` | `Mayor` |
| Near <a href="Museum" class="wikilink" title="Museum">Museum</a> | `3` | `Museum` |
| Near <a href="Blacksmith" class="wikilink"
title="Clint&#39;s blacksmith">Clint's blacksmith</a> | `4` | `Blacksmith` |
| Near <a href="The_Stardrop_Saloon" class="wikilink" title="the Saloon">the
Saloon</a> | `5` | `Saloon` |
| Near <a href="Evelyn" class="wikilink" title="Evelyn">Evelyn</a> and <a href="George" class="wikilink" title="George">George</a>'s house | `6` | `Evelyn` |
| Near <a href="JojaMart" class="wikilink" title="JojaMart">JojaMart</a> | `7` | `JojaMart` |

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Мусорные_баки" class="wikilink"
title="ru:Модификации:Мусорные баки">ru:Модификации:Мусорные баки</a>
<a href="zh_模组_垃圾桶" class="wikilink"
title="zh:模组:垃圾桶">zh:模组:垃圾桶</a>
