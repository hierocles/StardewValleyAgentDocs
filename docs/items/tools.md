---
title: "Tools"
wiki_source: "Modding:Tools"
permalink: /Modding:Tools/
category: items
tags: [tools, overview, data-format, basic-data, appearance, upgrades, game-logic, extensibility]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses tool-type item data.
For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

<a href="Tools" class="wikilink" title="Tools">Tools</a> are items that
can be swung or used by the player to perform some effect (e.g. dig
dirt, chop trees, etc).

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(T)` (or `ItemRegistry.type_tool` in C#
code), their data in `Data/Tools`, their in-game sprites in
`TileSheets/Tools` and translations in `Strings/Tools` by default, and
their code in `StardewValley.Tool` and various subclasses like
`StardewValley.Tools.Axe`.

## Data format

The tool data in `Data/Tools` consists of a string → model lookup,
where...

- The key is the
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="unqualified item ID">unqualified item ID</a>.
- The value is a model with the fields listed below.

### Basic data

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ClassName</samp></p></td>
<td><p>The name of the C# class to construct within the
<code>StardewValley.Tools</code> namespace. The class must be a subclass
of <samp>StardewValley.Tool</samp>, and have a constructor with no
arguments. For example, given a value of <samp>Axe</samp>, the game will
create <code>StardewValley.Tools.Axe</code> instances.</p>
<p>The main values are:</p>
<ul>
<li>main tools (<samp>Axe</samp>, <samp>FishingRod</samp>,
<samp>Hoe</samp>, <samp>MeleeWeapon</samp>, <samp>MilkPail</samp>,
<samp>Pan</samp>, <samp>Pickaxe</samp>, <samp>Shears</samp>,
<samp>Wand</samp>, and <samp>WateringCan</samp>);</li>
<li>a special <samp>GenericTool</samp> type which applies the
<samp>Data/Tools</samp> data and only has generic logic, so C# mods can
patch in their own logic;</li>
<li>and two tools cut from the game which may not work correctly
(<samp>Lantern</samp> and <samp>Raft</samp>).</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p>The internal name to set for the tool item.</p></td>
</tr>
<tr>
<td><p><samp>DisplayName</samp><br />
<samp>Description</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the tool's in-game
display name and description.</p></td>
</tr>
<tr>
<td><p><samp>AttachmentSlots</samp></p></td>
<td><p><em>(Optional)</em> The number of attachment slots to enable on
the tool. Note that only <samp>FishingRod</samp> tools have the code to
render and use attachment slots. Default <samp>-1</samp>, which keeps
the default value set by the tool class.</p></td>
</tr>
<tr>
<td><p><samp>SalePrice</samp></p></td>
<td><p><em>(Optional)</em> The default price when the item is sold to
the player in a shop. Defaults to <samp>-1</samp>, in which case you
should set the price manually in shops.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

### Appearance

Note that drawing the tool correctly in the world (ie, while the player
is trying to use it) will likely require custom code.

| field | purpose |
|----|----|
| `Texture` | The asset name for the texture containing the tool's sprite. |
| `SpriteIndex` | The tool's sprite index within the `Texture`, where 0 is the top row. |
| `MenuSpriteIndex` | *(Optional)* The sprite index within the `Texture` for the item icon. Defaults to `SpriteIndex`. |

### Upgrades

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>UpgradeLevel</samp></p></td>
<td><p><em>(Optional)</em> The tool upgrade level. Default
<samp>-1</samp>, which keeps the default value set by the tool
class.</p></td>
</tr>
<tr>
<td><p><samp>ConventionalUpgradeFrom</samp></p></td>
<td><p><em>(Optional)</em> If set, prepends an upgrade for the given
tool ID to the <samp>UpgradeFrom</samp> field. This applies these rules
(based on the <samp>UpgradeLevel</samp> field, not the upgrade level of
the specified tool ID):</p>
<table>
<thead>
<tr>
<th><p>upgrade level</p></th>
<th><p>price</p></th>
<th><p>items needed</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>1</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p>2</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p>3</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p>4</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>For example, Iridium Axe specifies this value:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ConventionalUpgradeFrom&quot;</span><span class="op">:</span> <span class="st">&quot;(T)GoldAxe&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>UpgradeFrom</samp></p></td>
<td><p><em>(Optional)</em> The requirements to buy this tool from
Clint's <a href="Blacksmith#Upgrade_Tools" class="wikilink"
title="blacksmith tool upgrade shop">blacksmith tool upgrade shop</a>.
If you specify multiple entries, the first one which matches will be
applied.</p>
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
<td><p><samp>Price</samp></p></td>
<td><p><em>(Optional)</em> The gold price to buy the upgrade. Defaults
to 0.</p></td>
</tr>
<tr>
<td><p><samp>RequireToolId</samp></p></td>
<td><p><em>(Optional)</em> If set, the <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a> for the tool that must be in the player's inventory for the
upgrade to appear. The tool will be destroyed when the upgrade is
purchased.</p></td>
</tr>
<tr>
<td><p><samp>TradeItemId</samp></p></td>
<td><p><em>(Optional)</em> If set, the <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a> for an extra item that must be traded to upgrade the tool. (For
example, many vanilla tools need metal bars.)</p></td>
</tr>
<tr>
<td><p><samp>TradeItemAmount</samp></p></td>
<td><p><em>(Optional)</em> The number of <samp>TradeItemId</samp>
required. Defaults to 1.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this upgrade is available. Defaults to always
true.</p></td>
</tr>
</tbody>
</table>
<p>For example, these are equivalent to the Steel Axe's upgrade
settings:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode js"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;UpgradeFrom&quot;</span><span class="op">:</span> [</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;RequireToolId&quot;</span><span class="op">:</span> <span class="st">&quot;(T)CopperAxe&quot;</span><span class="op">,</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Price&quot;</span><span class="op">:</span> <span class="dv">5000</span><span class="op">,</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;TradeItemId&quot;</span><span class="op">:</span> <span class="st">&quot;(O)335&quot;</span><span class="op">,</span> <span class="co">// Iron Bar</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;TradeItemAmount&quot;</span><span class="op">:</span> <span class="dv">5</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>]</span></code></pre></div>
<p>If you want the tool to always be available, you can just omit the
conditions. For example:</p>
<div class="sourceCode" id="cb3"><pre class="sourceCode js"><code class="sourceCode javascript"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;UpgradeFrom&quot;</span><span class="op">:</span> [</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>    {</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Price&quot;</span><span class="op">:</span> <span class="dv">5000</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>]</span></code></pre></div>
<p>Note that Clint needs a few days to smith the new tool. If you want
to sell the tool directly, <a href="Modding_Shops" class="wikilink"
title="add it to a regular shop">add it to a regular shop</a>
instead.</p></td>
</tr>
</tbody>
</table>

### Game logic

| field | purpose |
|----|----|
| `CanBeLostOnDeath` | Whether the player can <a href="Adventurer&#39;s_Guild#Item_Recovery_Service" class="wikilink"
title="lose this tool when they die">lose this tool when they die</a>. Default false. |

### Extensibility

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ModData</samp></p></td>
<td><p><em>(Optional)</em> The mod data values to set when the tool is
created, accessible in C# code via the <samp>tool.modData</samp>
dictionary. For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ModData&quot;</span><span class="op">:</span> {</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;PowerLevel&quot;</span><span class="op">:</span> <span class="dv">9000</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>SetProperties</samp></p></td>
<td><p><em>(Optional)</em> Set the value of arbitrary properties on the
tool class. For example, this would disable the tool animation and
require no stamina:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;SetProperties&quot;</span><span class="op">:</span> {</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;InstantUse&quot;</span><span class="op">:</span> <span class="kw">true</span><span class="op">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;IsEfficient&quot;</span><span class="op">:</span> <span class="kw">true</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
</tbody>
</table>

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Инструменты" class="wikilink"
title="ru:Модификации:Инструменты">ru:Модификации:Инструменты</a>
<a href="zh_模组_工具" class="wikilink"
title="zh:模组:工具">zh:模组:工具</a>
