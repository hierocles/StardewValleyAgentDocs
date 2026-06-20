---
title: "Fences"
wiki_source: "Modding:Fences"
permalink: /Modding:Fences/
category: game
tags: [fences, data-format]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents how the game stores and parses fence data. This is
an advanced guide for mod developers.

## Data format

You can add or customize
<a href="Crafting#Fences" class="wikilink" title="fences">fences</a> by
editing the `Data/Fences` asset.

This consists of a string → model lookup, where the key is the
<a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="unqualified item ID">unqualified item ID</a> of the fence object,
and the value is a model with these fields:

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Health</samp></p></td>
<td><p>The health points for a fence when it's first placed, which
affects how quickly it degrades. A fence loses
<sup>1</sup>/<sub>1440</sub> points per in-game minute (roughly 0.04
points per hour or 0.5 points for a 12-hour day).</p>
<p>Repairing a fence sets its max health to <em>2 × (base_health +
repair_health_adjustment)</em>, where <samp>base_health</samp> is this
field's value and <samp>repair_health_adjustment</samp> is a random
value between <samp>RepairHealthAdjustmentMinimum</samp> and
<samp>RepairHealthAdjustmentMaximum</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture (under the game's
<samp>Content</samp> folder) when the fence is placed. Use
<samp>\</samp> (or <samp>\\</samp> in JSON) to separate name segments if
needed. For example, the vanilla fences use individual tilesheets like
<samp>LooseSprites\Fence1</samp> (wood fence).</p></td>
</tr>
<tr>
<td><p><samp>RemovalToolIds</samp><br />
<samp>RemovalToolTypes</samp></p></td>
<td><p>A list of tool IDs (matching the keys in
<samp>Data\ToolData</samp>) or C# full type names which can be used to
break the fence.</p>
<p>For example, this will let the player break the fence with an iridium
axe and any pickaxe:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RemovalToolIds&quot;</span><span class="er">:</span> <span class="ot">[</span><span class="st">&quot;IridiumAxe&quot;</span><span class="ot">]</span><span class="er">,</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RemovalToolTypes&quot;</span><span class="er">:</span> <span class="ot">[</span><span class="st">&quot;StardewValley.Tools.Pickaxe&quot;</span><span class="ot">]</span></span></code></pre></div>
<p>A tool must match <samp>RemovalToolIds</samp> <em>or</em>
<samp>RemovalToolTypes</samp> to be a valid removal tool. If both lists
are null or empty, all tools can remove the fence.</p></td>
</tr>
<tr>
<td><p><samp>PlacementSound</samp></p></td>
<td><p>The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> played when the fence is placed or
repaired (e.g. <samp>axe</samp> used by <a href="Wood_Fence"
class="wikilink" title="Wood Fence">Wood Fence</a>).</p></td>
</tr>
<tr>
<td><p><samp>RemovalSound</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> played when the fence is broken or
picked up by the player. Defaults to the same sound as
<samp>PlacementSound</samp>.</p></td>
</tr>
<tr>
<td><p><samp>RemovalDebrisType</samp></p></td>
<td><p><em>(Optional)</em> The type of cosmetic debris particles to
'splash' from the tile when the fence is broken with a tool. The defined
values are 0 (copper), 2 (iron), 4 (coal), 6 (gold), 8 (coins), 10
(iridium), 12 (wood), 14 (stone), 32 (big stone), and 34 (big wood).
Default 14 (stone).</p></td>
</tr>
<tr>
<td><p><samp>RepairHealthAdjustmentMinimum</samp><br />
<samp>RepairHealthAdjustmentMaximum</samp></p></td>
<td><p><em>(Optional)</em> A random amount added to the
<samp>Health</samp> when a fence is repaired by a player. See the
<samp>Health</samp> field description. Both default to 0.</p></td>
</tr>
<tr>
<td><p><samp>HeldObjectDrawOffset</samp></p></td>
<td><p><em>(Optional)</em> When an item like a <a href="torch"
class="wikilink" title="torch">torch</a> is placed on the fence, the
pixel offset to apply to its draw position. Specified as a string in the
form <samp>"&lt;x&gt;, &lt;y&gt;"</samp>. Defaults to <samp>"0,
-20"</samp> if omitted.</p></td>
</tr>
<tr>
<td><p><samp>LeftEndHeldObjectDrawX</samp><br />
<samp>RightEndHeldObjectDrawX</samp></p></td>
<td><p><em>(Optional)</em> The X pixel offset to apply when the fence is
oriented horizontally, with only one connected fence on the right (for
<samp>LeftEndHeldObjectDrawX</samp>) or left (for
<samp>RightEndHeldObjectDrawX</samp>). This fully replaces the X value
specified by <samp>HeldObjectDrawOffset</samp> when it's applied.
Default 0.</p></td>
</tr>
</tbody>
</table>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Заборы" class="wikilink"
title="ru:Модификации:Заборы">ru:Модификации:Заборы</a>
<a href="zh_模组_围栏" class="wikilink"
title="zh:模组:围栏">zh:模组:围栏</a>
