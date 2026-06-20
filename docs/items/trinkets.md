---
title: "Trinkets"
wiki_source: "Modding:Trinkets"
permalink: /Modding:Trinkets/
category: items
tags: [trinkets, overview, data-format, see-also]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses trinket-type item
data. For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

<a href="Trinkets" class="wikilink" title="Trinkets">Trinkets</a> are
items that can be equipped in the player's trinket slot to enable
special effects.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(TR)` (or `ItemRegistry.type_trinket`
in C# code), their data in `Data/Trinkets`, their vanilla icon sprites
in `TileSheets\Objects_2`, and their code in
`StardewValley.Objects.Trinkets.Trinket`.

## Data format

The trinket data in `Data/Trinkets` consists of a string → model lookup,
where...

- The key is the
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="unqualified item ID">unqualified item ID</a> and internal name.
- The value is a model with the fields listed below.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DisplayName</samp><br />
<samp>Description</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the item's in-game
display name and description.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Asset_name"
class="wikilink" title="asset name">asset name</a> for the texture
containing the item's sprite.</p></td>
</tr>
<tr>
<td><p><samp>SheetIndex</samp></p></td>
<td><p>The sprite's index within the <samp>Texture</samp>, where 0 is
the top-left sprite.</p></td>
</tr>
<tr>
<td><p><samp>TrinketEffectClass</samp></p></td>
<td><p>The C# <samp>TrinketEffect</samp> subclass which implements the
trinket behavior. This can safely be a mod class, since it's not written
to the save file.</p>
<p>This should be the full assembly-qualified name in the form
<code>namespace.class, assembly</code>. For example:
<code>StardewValley.Objects.Trinkets.CompanionTrinketEffect, StardewValley</code>.</p></td>
</tr>
<tr>
<td><p><samp>DropsNaturally</samp></p></td>
<td><p><em>(Optional)</em> Whether this trinket can be spawned randomly
(e.g. in mine treasure chests). Default true.</p></td>
</tr>
<tr>
<td><p><samp>CanBeReforged</samp></p></td>
<td><p><em>(Optional)</em> Whether players can re-roll this trinket's
stats using an anvil. This assumes that the
<samp>TrinketEffectClass</samp> implements the
<samp>GenerateRandomStats</samp> method. Default true.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry.</p></td>
</tr>
<tr>
<td><p><samp>ModData</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Mod_data" class="wikilink"
title="mod data fields">mod data fields</a> to add to created trinket
instances. Default none.</p>
<p>For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ModData&quot;</span><span class="op">:</span> {</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Example.ModId_FieldName&quot;</span><span class="op">:</span> <span class="st">&quot;some custom data&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
</tbody>
</table>

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Брелоки" class="wikilink"
title="ru:Модификации:Брелоки">ru:Модификации:Брелоки</a>
<a href="zh_模组_饰品" class="wikilink"
title="zh:模组:饰品">zh:模组:饰品</a>
