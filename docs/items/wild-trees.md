---
title: "Wild Trees"
wiki_source: "Modding:Wild trees"
permalink: /Modding:Wild_trees/
category: items
tags: [wild-trees, data-format]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents the in-game data format for
<a href="Trees" class="wikilink" title="wild trees">wild trees</a>. This
is an advanced guide for mod developers.

## Data format

You now create/edit
<a href="Trees" class="wikilink" title="wild trees">wild trees</a> by
editing the `Data/WildTrees` asset.

This consists of a string → model lookup, where...

- The asset key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  tree type. The vanilla tree IDs are `1` (oak), `2` (maple), `3`
  (pine), `6` (desert palm), `7` (mushroom), `8` (mahogany), `9` (island
  palm), `10` (green tree 1), `11` (green tree 2), `12` (giant
  fiddlehead), and `13` (mystic).
- The asset value is a model with the fields listed below.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Textures</samp></p></td>
<td><p>The texture to use as the tree's spritesheet in-game. If multiple
textures are listed, the first matching one is used.</p>
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
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the tree's spritesheet.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> If set, the specific season when this texture
should apply. For more complex conditions, see
<samp>Condition</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this texture should be applied for a tree. Defaults to
always enabled.</p>
<p>This is checked when the tree is created, a new day starts, or its
texture is reloaded by a mod. More frequent conditions (like time of
day) won't work as expected unless a mod manually triggers a tree
update.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>SeedItemId</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified item ID">qualified item ID</a> for the seed item. If
omitted, the tree can't be planted and <samp>SeedOnShakeChance</samp>
will be ignored.</p></td>
</tr>
<tr>
<td><p><samp>SeedPlantable</samp></p></td>
<td><p><em>(Optional)</em> Whether the seed can be planted by the
player. If this is false, it can only be spawned automatically via map
properties. Default true.</p></td>
</tr>
<tr>
<td><p><samp>GrowthChance</samp></p></td>
<td><p><em>(Optional)</em> The probability each day that the tree will
grow to the next stage without <a href="Tree_Fertilizer"
class="wikilink" title="tree fertilizer">tree fertilizer</a>, as a value
from 0 (will never grow) to 1 (will grow every day). Defaults to 0.2
(20% chance).</p></td>
</tr>
<tr>
<td><p><samp>FertilizedGrowthChance</samp></p></td>
<td><p><em>(Optional)</em> Equivalent to <samp>GrowthChance</samp>, but
with <a href="Tree_Fertilizer" class="wikilink"
title="tree fertilizer">tree fertilizer</a>. Defaults to 1 (100%
chance).</p></td>
</tr>
<tr>
<td><p><samp>SeedSpreadChance</samp></p></td>
<td><p><em>(Optional)</em> The probability each day that the tree will
plant a seed on a nearby tile, as a value from 0 (never) to 1 (always).
This only applied in locations where trees plant seeds (e.g. farms in
vanilla). Default 0.15 (15% chance).</p></td>
</tr>
<tr>
<td><p><samp>SeedOnShakeChance</samp></p></td>
<td><p><em>(Optional)</em> The probability each day that the tree will
produce a seed that will drop when the tree is shaken, as a value from 0
(never) to 1 (always). Default 0.05 (5% chance).</p></td>
</tr>
<tr>
<td><p><samp>SeedOnChopChance</samp></p></td>
<td><p><em>(Optional)</em> The probability that a seed will drop when
the player chops down the tree, as a value from 0 (never) to 1 (always).
Default 0.75 (75% chance).</p></td>
</tr>
<tr>
<td><p><samp>DropWoodOnChop</samp></p></td>
<td><p><em>(Optional)</em> Whether to drop <a href="wood"
class="wikilink" title="wood">wood</a> when the player chops down the
tree. Default true.</p></td>
</tr>
<tr>
<td><p><samp>DropHardwoodOnLumberChop</samp></p></td>
<td><p><em>(Optional)</em> Whether to drop <a href="hardwood"
class="wikilink" title="hardwood">hardwood</a> when the player chops
down the tree, if they have the <a href="Skills#Foraging"
class="wikilink" title="Lumberjack profession">Lumberjack
profession</a>. Default true.</p></td>
</tr>
<tr>
<td><p><samp>IsLeafy</samp></p></td>
<td><p><em>(Optional)</em> Whether shaking or chopping the tree causes
cosmetic leaves to drop from tree and produces a leaf rustle sound. When
a leaf drops, the game will use one of the four leaf sprites in the
tree's spritesheet in the slot left of the stump sprite. Default
true.</p></td>
</tr>
<tr>
<td><p><samp>IsLeafyInWinter</samp></p></td>
<td><p><em>(Optional)</em> Whether <samp>IsLeafy</samp> also applies in
winter. Default false.</p></td>
</tr>
<tr>
<td><p><samp>GrowsInWinter</samp></p></td>
<td><p><em>(Optional)</em> Whether the tree can grow in winter (subject
to <samp>GrowthChance</samp> or <samp>FertilizedGrowthChance</samp>).
Default false.</p></td>
</tr>
<tr>
<td><p><samp>IsStumpDuringWinter</samp></p></td>
<td><p><em>(Optional)</em> Whether the tree is reduced to a stump in
winter and regrows in spring, like the vanilla <a
href="Trees#Mushroom_Tree" class="wikilink"
title="mushroom tree">mushroom tree</a>. Default false.</p></td>
</tr>
<tr>
<td><p><samp>AllowWoodpeckers</samp></p></td>
<td><p><em>(Optional)</em> Whether woodpeckers can spawn on the tree.
Default true.</p></td>
</tr>
<tr>
<td><p><samp>UseAlternateSpriteWhenNotShaken</samp><br />
<samp>UseAlternateSpriteWhenSeedReady</samp></p></td>
<td><p><em>(Optional)</em> Whether to render a different tree sprite
when the player hasn't shaken it on that day
(<samp>UseAlternateSpriteWhenNotShaken</samp>) or it has a seed ready
(<samp>UseAlternateSpriteWhenSeedReady</samp>). If either field is true,
the tree spritesheet must be double-width with the alternate textures on
the right. If both are true, the same alternate sprites are used for
both. Default false.</p></td>
</tr>
<tr>
<td><p><samp>DebrisColor</samp></p></td>
<td><p><em>(Optional)</em> The color of the cosmetic wood chips when
chopping the tree. This can be...</p>
<ul>
<li>a <a href="Modding_Common_data_field_types#Color" class="wikilink"
title="standard color format">standard color format</a>;</li>
<li>or one of <samp>12</samp> (brown/woody), <samp>100001</samp>
(white), <samp>100001</samp> (light green), <samp>100002</samp> (light
blue), <samp>100003</samp> (red), <samp>100004</samp> (yellow),
<samp>100005</samp> (black), <samp>100006</samp> (gray), or
<samp>100007</samp> (charcoal / dim gray).</li>
</ul>
<p>Defaults to <samp>12</samp> (brown/woody).</p></td>
</tr>
<tr>
<td><p><samp>SeedDropItems</samp></p></td>
<td><p><em>(Optional)</em> When a seed is dropped subject to
<samp>SeedOnShakeChance</samp>, the item to drop instead of the item
specified by <samp>SeedItemId</samp>. If this is empty or none match,
the <samp>SeedItemId</samp> will be dropped instead.</p>
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
generic item fields supported for chop drops.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> If set, the item only applies if the tree's
location is in this season.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that the item will drop, as a
value between 0 (never drops) and 1 (always drops). Default 1 (100%
chance).</p></td>
</tr>
<tr>
<td><p><samp>ContinueOnDrop</samp></p></td>
<td><p><em>(Optional)</em> If this item is dropped, whether to continue
as if it hadn't been dropped for the remaining drop candidates. Default
false.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>ChopItems</samp></p></td>
<td><p><em>(Optional)</em> The additional items to drop when the tree is
chopped down. All matching items are dropped.</p>
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
generic item fields supported for chop drops.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> If set, the item only applies if the tree's
location is in this season.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that the item will drop, as a
value between 0 (never drops) and 1 (always drops). Default 1 (100%
chance).</p></td>
</tr>
<tr>
<td><p><samp>MinSize</samp><br />
<samp>MaxSize</samp></p></td>
<td><p><em>(Optional)</em> The minimum and/or maximum growth stage for
the tree at which this item is produced. The possible values are
<samp>Seed</samp>, <samp>Sprout</samp>, <samp>Sapling</samp>,
<samp>Bush</samp>, and <samp>Tree</samp>. Both default to no
limit.</p></td>
</tr>
<tr>
<td><p><samp>ForStump</samp></p></td>
<td><p><em>(Optional)</em> Whether the item is only produced if the tree
is a stump (<samp>true</samp>), not a stump (<samp>false</samp>), or
both (<samp>null</samp>). Defaults to <samp>false</samp> (non-stumps
only).</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>ShakeItems</samp></p></td>
<td><p>The items produced by shaking the tree when it's fully grown.
This only applies the first time the tree is shaken each day. All
matching items are dropped.</p>
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
generic item fields supported for shake items.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> If set, the item only applies if the tree's
location is in this season.</p></td>
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
<td><p><samp>TapItems</samp></p></td>
<td><p>The items produced by <a href="Tapper" class="wikilink"
title="tapping">tapping</a> the tree. If multiple items can be produced,
the first available one is selected.</p>
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
generic item fields supported for tapper items.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Season</samp></p></td>
<td><p><em>(Optional)</em> If set, the item only applies if the tree's
location is in this season.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that this entry is selected,
as a value between 0 (never drops) and 1 (always drops). Default 1 (100%
chance).</p></td>
</tr>
<tr>
<td><p><samp>DaysUntilReady</samp></p></td>
<td><p>The number of days before the tapper is ready to empty.</p></td>
</tr>
<tr>
<td><p><samp>PreviousItemId</samp></p></td>
<td><p><em>(Optional)</em> If set, the item only applies if the previous
item produced by the tapper matches one of the given <a
href="#Custom_items" class="wikilink"
title="qualified item IDs">qualified item IDs</a>. If an entry is null
or an empty string, it matches when there's no previous item.</p>
<p>For example: <code>"PreviousItemId": [ null ]</code> only applies
when a tapper is first added to the tree, and
<code>"PreviousItemsId": [ "(O)420" ]</code> applies if the player just
collected a <a href="Red_Mushroom" class="wikilink"
title="red mushroom">red mushroom</a> (object #420) from it.</p></td>
</tr>
<tr>
<td><p><samp>DaysUntilReadyModifiers</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Common_data_field_types#Quantity_modifiers"
class="wikilink" title="Quantity modifiers">Quantity modifiers</a>
applied to the <samp>DaysUntilReady</samp> value. Default none.</p></td>
</tr>
<tr>
<td><p><samp>DaysUntilReadyModifiersMode</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Common_data_field_types#Quantity_modifiers"
class="wikilink" title="Quantity modifier modes">Quantity modifier
modes</a> which indicate what to do if multiple modifiers in the
<samp>DaysUntilReadyModifiersMode</samp> field apply at the same time.
Default <samp>Stack</samp>.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>PlantableLocationRules</samp></p></td>
<td><p><em>(Optional)</em> The rules to decide which locations you can
plant the seed in, if applicable. The first matching rule is used. This
can override location checks (e.g. crops being limited to the farm), but
not built-in requirements like crops needing dirt.</p>
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
<td><p>Indicates whether the seed can be planted in a location if this
entry is selected. The possible values are:</p>
<ul>
<li><samp>Default</samp>: the seed can be planted if the location
normally allows it. This can be used to stop processing further rules,
and/or set a custom <samp>DeniedMessage</samp>.</li>
<li><samp>Allow</samp>: the seed can be planted here, regardless of
whether the location normally allows it.</li>
<li><samp>Deny</samp>: the seed can't be planted here, regardless of
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
<p>Note that trees can't be planted in garden pots.</p></td>
</tr>
<tr>
<td><p><samp>DeniedMessage</samp></p></td>
<td><p><em>(Optional)</em> If this rule prevents planting the seed, the
tokenizable string to show to the player (or <samp>null</samp> to
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
<tr>
<td><p><samp>GrowsMoss</samp></p></td>
<td><p>Whether the tree grows moss in warm seasons. If field is true,
the tree spritesheet must be triple-width with the mossy textures for
the upper tree and stump on the far right.</p></td>
</tr>
</tbody>
</table>

#### Spawning wild trees

Custom trees can be added to the game in two ways:

- Spawn them on
  <a href="Modding_Maps" class="wikilink" title="map tiles">map tiles</a>
  when the location is created, using the new
  `SpawnTree: wild <tree ID> [growth stage on location created] [growth stage on day-update regrowth]`
  tile property. This must be added on the `Paths` layer, which must
  also have tile index 34 from the `paths` tilesheet.
- Or give the player a seed item in the usual ways (e.g. from
  <a href="Modding_Shops" class="wikilink" title="a shop">a shop</a>,
  <a href="Modding_Mail_data" class="wikilink" title="mail letter">mail
  letter</a>, etc).

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Дикорастущие_деревья" class="wikilink"
title="ru:Модификации:Дикорастущие деревья">ru:Модификации:Дикорастущие
деревья</a> <a href="zh_模组_野树" class="wikilink"
title="zh:模组:野树">zh:模组:野树</a>
