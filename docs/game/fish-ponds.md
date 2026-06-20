---
title: "Fish Ponds"
wiki_source: "Modding:Fish ponds"
permalink: /Modding:Fish_ponds/
category: game
tags: [fish-ponds, format]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses
<a href="Fish_Pond" class="wikilink" title="Fish Pond">Fish Pond</a>
data. This is an advanced guide for mod developers.

## Format

The fish pond data in `Data/FishPondData` consists of a list of elements
with these fields.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry.</p></td>
</tr>
<tr>
<td><p><samp>RequiredTags</samp></p></td>
<td><p>The <a href="Modding_Context_tags" class="wikilink"
title="context tags">context tags</a> for fish which should use this
entry. A tag can be prefixed with <code>!</code> to require that the
fish <em>not</em> have that tag.</p>
<p>For example,
<code>["fish_ocean", "fish_crab_pot", "!fish_carnivorous"]</code> will
match ocean fish that can be caught in <a href="Crab_Pot"
class="wikilink" title="crab pots">crab pots</a> and aren't
carnivorous.</p>
<p>The first matching entry based on the <samp>Precedence</samp> field
is used. If no other entries match, <samp>Data/FishPondData</samp> has a
default entry with the required tags <code>category_fish</code> as a
catch-all for any fish without their own entry.</p></td>
</tr>
<tr>
<td><p><samp>ProducedItems</samp></p></td>
<td><p>The items that can be produced by the selected fish.</p>
<p>When a fish pond is ready to produce output (based on a hardcoded
<code>(15 + 8 * population of pond)%</code> chance), it checks each
entry in the list and takes the first one that matches. If no entry
matches, no output is produced.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry.</p></td>
</tr>
<tr>
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported by fish pond rewards.</p>
<p>Notes:</p>
<ul>
<li>If <samp>ItemId</samp> or <samp>RandomItemId</samp> is set to an <a
href="Modding_Item_queries" class="wikilink" title="item query">item
query</a> which returns multiple items, one item will be selected at
random.</li>
<li>If <samp>ItemId</samp> and <samp>RandomItemId</samp> is set to the
exact string <code>(O)812</code> (<a href="roe" class="wikilink"
title="roe">roe</a>), it will produce roe for the current fish.</li>
<li>For the <samp>Condition</samp> field, the input item matches the
fish living in the pond.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>RequiredPopulation</samp></p></td>
<td><p><em>(Optional)</em> The minimum number of fish in the pond
required to produce this item. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that this item will be
produced, as a value between 0 (never) and 1 (always). This is applied
<em>after</em> the base chance of producing any item above. Default
1.</p></td>
</tr>
<tr>
<td><p><samp>MinQuantity</samp><br />
<samp>MaxQuantity</samp></p></td>
<td><p><em>(Deprecated)</em> Use
<samp>MinStack</samp>/<samp>MaxStack</samp> from the item spawn fields
instead.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>PopulationGates</samp></p></td>
<td><p>The rules which decide when the fish pond population can grow (up
to a hardcoded limit of 10 fish), and the quests that must be completed
to do so. If omitted, the population can grow to 10 fish with no
quests.</p>
<p>This consists of a number → item IDs lookup, where:</p>
<ul>
<li>The key is the population number at which this gate applies.</li>
<li>The value is a list of possible quest items that may be requested by
the fish at random to complete the gate. Each item is represented by 1–3
space-delimited values: the item ID, minimum quantity, and maximum
quantity. If both min and max quantity are specified, a random number in
that range is used. If only the min quantity is specified, that exact
number is used. If neither are specified, the fish will request
one.</li>
</ul>
<p>For example, consider this population gate:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;6&quot;</span><span class="er">:</span> <span class="ot">[</span> <span class="st">&quot;422 2 3&quot;</span><span class="ot">,</span> <span class="st">&quot;60 2&quot;</span><span class="ot">,</span> <span class="st">&quot;749 2 3&quot;</span><span class="ot">,</span> <span class="st">&quot;116&quot;</span> <span class="ot">]</span></span></code></pre></div>
<p>This means that before the population grows to 6, the fish will
randomly ask for one of these:</p>
<ul>
<li>2–3 <a href="Purple_Mushroom" class="wikilink"
title="purple mushrooms">purple mushrooms</a> (item ID 422);</li>
<li>2 <a href="emerald" class="wikilink" title="emerald">emeralds</a>
(item ID 60);</li>
<li>2–3 <a href="Omni_Geode" class="wikilink" title="omni geodes">omni
geodes</a> (item ID 749);</li>
<li>or 1 <a href="Dried_Starfish" class="wikilink"
title="dried starfish">dried starfish</a>.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>MaxPopulation</samp></p></td>
<td><p><em>(Optional)</em> The maximum number of fish that can live in
this pond, whether added manually or through population growth. This
can't exceed the hardcoded maximum of 10. If omitted, defaults to the
maximum based on <samp>PopulationGates</samp>.</p></td>
</tr>
<tr>
<td><p><samp>BaseMinProduceChance</samp><br />
<samp>BaseMaxProduceChance</samp></p></td>
<td><p>The daily chance that this fish pond checks for output on a given
day, as a value between 0 (never) and 1 (always). The actual probability
is lerped between the min and max value based on the fish pond's
population (i.e. the probability increases within that range as the
population grows). This only affects whether it checks for output;
output is only produced if one of the <samp>ProducedItems</samp> passes
its checks too.</p></td>
</tr>
<tr>
<td><p><samp>Precedence</samp></p></td>
<td><p><em>(Optional)</em> The order in which this entry should be
checked, where 0 is the default value used by most entries. Entries with
the same precedence are checked in the order listed. Default 0.</p>
<p>For consistency, vanilla entries use these values:</p>
<table>
<thead>
<tr>
<th><p>precedence</p></th>
<th><p>used for</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0<br />
<small>(default value)</small></p></td>
<td><p>specific fish</p></td>
</tr>
<tr>
<td><p>100</p></td>
<td><p>custom groups (e.g. desert fish)</p></td>
</tr>
<tr>
<td><p>500</p></td>
<td><p>broad fish type (e.g. ocean fish)</p></td>
</tr>
<tr>
<td><p>1000</p></td>
<td><p>fallback (e.g. fish category)</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>SpawnTime</samp></p></td>
<td><p><em>(Optional)</em> The number of days needed to raise the
population by one if there's enough room in the fish pond.</p>
<p>If omitted, the game chooses a value based on the base fish price: 1
day (0–30g), 2 days (31–80g), 3 days (81–120g), 4 days (121–250g), or 5
days (250g+).</p></td>
</tr>
<tr>
<td><p><samp>WaterColor</samp></p></td>
<td><p><em>(Optional)</em> The color tint to apply to the water when
this entry applies. If multiple are specified, the first matching entry
is applied. If none match, the default water color is used.</p>
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
entry.</p></td>
</tr>
<tr>
<td><p><samp>Color</samp></p></td>
<td><p><em>(Optional)</em> The water color to apply. This can be <a
href="Modding_Common_data_field_types#Color" class="wikilink"
title="a standard color value">a standard color value</a>, or
<samp>CopyFromInput</samp> (to use the item color from the fish item
data). Default none.</p></td>
</tr>
<tr>
<td><p><samp>MinPopulation</samp></p></td>
<td><p><em>(Optional)</em> The minimum number of fish in the pond before
this color applies. Default 1.</p></td>
</tr>
<tr>
<td><p><samp>MinUnlockedPopulationGate</samp></p></td>
<td><p><em>(Optional)</em> The minimum population for the last
population gate that was unlocked, or 0 for any value. Default
0.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry should be applied. Defaults to always
true.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Рыбный_пруд" class="wikilink"
title="ru:Модификации:Рыбный пруд">ru:Модификации:Рыбный пруд</a>
<a href="zh_模组_鱼塘数据" class="wikilink"
title="zh:模组:鱼塘数据">zh:模组:鱼塘数据</a>
