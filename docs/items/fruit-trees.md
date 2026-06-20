---
title: "Fruit Trees"
wiki_source: "Modding:Fruit trees"
permalink: /Modding:Fruit_trees/
category: items
tags: [fruit-trees, raw-data]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses fruit tree data. This
is an advanced guide for mod developers.

## Raw data

Fruit tree data is stored in `Content\Data\FruitTrees.xnb`, which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of for reference:

#### Data format

The `Data/FruitTrees` asset consists of a string → model lookup,
where...

- The key is the unqualified item it for the sapling item in
  `Data/Objects`.
- The value is a model with the fields listed below.

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
title="tokenizable string">tokenizable string</a> for the tree's display
name. This should return a display name without 'tree' (like
<samp>Cherry</samp> for a cherry tree). This is used in UI messages like
"<em>Your &lt;display name&gt; tree wasn't able to grow last
night</em>".</p></td>
</tr>
<tr>
<td><p><samp>Seasons</samp></p></td>
<td><p>The seasons in which the fruit tree bears fruit. This consists of
an array of season names (any combination of <samp>spring</samp>,
<samp>summer</samp>, <samp>fall</samp>, or <samp>winter</samp>).</p>
<p><strong>Note:</strong> the previous '<samp>island</samp>' season
value is no longer valid. Using <samp>summer</samp> is equivalent to how
it worked before (since we now have <a href="#Custom_location_contexts"
class="wikilink" title="per-location seasons">per-location
seasons</a>).</p></td>
</tr>
<tr>
<td><p><samp>Fruit</samp></p></td>
<td><p>The fruit items to add to the tree each day while the tree is
in-season. The first matching fruit (if any) is selected each day.</p>
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
generic item fields supported for fruit items.</p>
<p>Notes:</p>
<ul>
<li>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</li>
<li>Season conditions are ignored in non-seasonal locations like the <a
href="greenhouse" class="wikilink" title="greenhouse">greenhouse</a> and
<a href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a>.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> If set, the group only applies if the tree's
location is in this season. This is ignored in non-seasonal locations
like the <a href="greenhouse" class="wikilink"
title="greenhouse">greenhouse</a> and <a href="Ginger_Island"
class="wikilink" title="Ginger Island">Ginger Island</a>.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that this entry is selected,
as a value between 0 (never drops) and 1 (always drops). Default 1 (100%
chance).</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture under the game's
<samp>Content</samp> folder. Use <samp>\</samp> (or <samp>\\</samp> in
JSON) to separate name segments if needed. For example, vanilla fruit
trees use <samp>TileSheets\fruitTrees</samp>.</p></td>
</tr>
<tr>
<td><p><samp>TextureSpriteRow</samp></p></td>
<td><p>The tree's row index in the <samp>Texture</samp> spritesheet
(e.g. 0 for the first tree, 1 for the second tree, etc).</p></td>
</tr>
<tr>
<td><p><samp>PlantableLocationRules</samp></p></td>
<td><p><em>(Optional)</em> The rules to decide which locations you can
plant the sapling in, if applicable. The first matching rule is used.
This can override location checks (e.g. crops being limited to the
farm), but not built-in requirements like crops needing dirt.</p>
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
entry within the list.</p></td>
</tr>
<tr>
<td><p><samp>Result</samp></p></td>
<td><p>Indicates whether the sapling can be planted in a location if
this entry is selected. The possible values are:</p>
<ul>
<li><samp>Default</samp>: the sapling can be planted if the location
normally allows it. This can be used to stop processing further rules,
and/or set a custom <samp>DeniedMessage</samp>.</li>
<li><samp>Allow</samp>: the sapling can be planted here, regardless of
whether the location normally allows it.</li>
<li><samp>Deny</samp>: the sapling can't be planted here, regardless of
whether the location normally allows it.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this entry applies. Default true.</p></td>
</tr>
<tr>
<td><p><samp>PlantedIn</samp></p></td>
<td><p><em>(Optional)</em> The planting context to apply this rule for.
The possible values are <samp>Ground</samp> (planted directly in the
ground), <samp>GardenPot</samp> (planted in a <a href="Garden_Pot"
class="wikilink" title="garden pot">garden pot</a>), or
<samp>Any</samp>. Default <samp>Any</samp>.</p>
<p>Note that saplings can't be planted in garden pots.</p></td>
</tr>
<tr>
<td><p><samp>DeniedMessage</samp></p></td>
<td><p><em>(Optional)</em> If this rule prevents planting the sapling,
the tokenizable string to show to the player (or <samp>null</samp> to
default to the normal behavior for the context). This also applies when
the <samp>Result</samp> is <samp>Default</samp>, if that causes the
planting to be denied.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

For example, this content pack adds a custom fruit tree, including
<a href="Modding_Objects" class="wikilink" title="custom objects">custom
objects</a> for the sapling and fruit:

The fruit trees can then be added to the game by giving the player a
sapling item in the usual ways (e.g. from
<a href="#Custom_shops" class="wikilink" title="a shop">a shop</a>).

#### Fruit items

For C# mods, the `fruitsOnTree` field (number of fruit on the tree) has
been replaced by `fruit` (list of fruit items).

#### Spawning fruit trees

Custom trees can be added to the game in two ways:

- Spawn them on
  <a href="Modding_Maps" class="wikilink" title="map tiles">map tiles</a>
  when the location is created, using the new
  `SpawnTree: fruit <tree ID> [growth stage on location created] [growth stage on day-update regrowth]`
  tile property. This must be added on the `Paths` layer, which must
  also have tile index 34 from the `paths` tilesheet.
- Or give the player a seed item in the usual ways (e.g. from
  <a href="#Custom_shops" class="wikilink" title="a shop">a shop</a>,
  <a href="Modding_Mail_data" class="wikilink" title="mail letter">mail
  letter</a>, etc).

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Плодовые_деревья" class="wikilink"
title="ru:Модификации:Плодовые деревья">ru:Модификации:Плодовые
деревья</a> <a href="zh_模组_果树数据" class="wikilink"
title="zh:模组:果树数据">zh:模组:果树数据</a>
