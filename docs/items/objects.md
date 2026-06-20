---
title: "Objects"
wiki_source: "Modding:Objects"
permalink: /Modding:Objects/
category: items
tags: [objects, overview, data-format, basic-info, appearance, edibility, geodes-artifact-spots, context-tags-exclusions]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses object-type item data.
For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

Objects are the default type for items in inventories or in the world.
Depending on their data, they can be placed, picked up, eaten, sold to
shops, etc.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(O)` (or `ItemRegistry.type_object` in
C# code), their data in `Data/Objects`, their icon sprites in
`Maps/springobjects` or `TileSheets/Objects_2` by default, and their
code in `StardewValley.Object`. See
<a href="Modding_Objects_Object_sprites" class="wikilink"
title="a table of sprites and their corresponding indexes">a table of
sprites and their corresponding indexes</a>.

## Data format

The object data in `Data/Objects` consists of a string → model lookup,
where...

- The key is the unqualified
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="item ID">item ID</a>.
- The value is a model with the fields listed below.

### Basic info

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p>The internal item name.</p></td>
</tr>
<tr>
<td><p><samp>DisplayName</samp><br />
<samp>Description</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the item's in-game
display name and description.</p></td>
</tr>
<tr>
<td><p><samp>Type</samp></p></td>
<td><p>The item's general type, like Arch (artifact) or Minerals. The
vanilla types are: <samp>Basic</samp>, <samp>Arch</samp> (artifact),
<samp>Litter</samp> (e.g. debris), <samp>Minerals</samp>,
<samp>Quest</samp>, <samp>Crafting</samp>, <samp>Fish</samp>,
<samp>Cooking</samp>, <samp>Seeds</samp>, <samp>Ring</samp>,
<samp>interactive</samp>, and some placeholder values like
<samp>asdf</samp>.</p>
<p><strong>Caution:</strong> adding custom items with the
<samp>Arch</samp> type is inadvisable as it often leads to <a
href="Artifact_Spot" class="wikilink" title="artifact spot">artifact
spots</a> becoming broken and not giving any items.</p>
<p><strong>Note:</strong> The "Type" affects whether an item shows up in
the collections menu. For example, items with <samp>Type: Cooking</samp>
will show up as silhouettes in the cooked items collection menu, items
with <samp>Type: Minerals</samp> will show up as silhouettes in the
mineral collection menu, etc. However, the <a
href="Modding_Items#Categories" class="wikilink"
title="Category">Category</a> of the item must also be the correct
number or the item will not count toward Perfection/Achievements. For
example, if an item has Type: Cooking, it must also be "Category": -7 in
order to count toward the "Gourmet Chef" achievement and
Perfection.</p></td>
</tr>
<tr>
<td><p><samp>Category</samp></p></td>
<td><p>The <a href="Modding_Items#Categories" class="wikilink"
title="item category">item category</a>.</p></td>
</tr>
<tr>
<td><p><samp>Price</samp></p></td>
<td><p><em>(Optional)</em> The price when sold by the player. This is
not the price when bought from a shop. Default 0.</p></td>
</tr>
</tbody>
</table>

### Appearance

| field | purpose |
|----|----|
| `Texture` | The asset name for the texture containing the item's sprite. Defaults to `Maps/springobjects`. |
| `SpriteIndex` | The sprite's index within the `Texture`, where 0 is the top-left sprite. |
| `ColorOverlayFromNextIndex` | *(Optional)* When drawn as a colored object, whether to apply the color to the next sprite in the spritesheet and draw that over the main sprite. If false, the color is applied to the main sprite instead. Default false. |

### Edibility

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Edibility</samp></p></td>
<td><p><em>(Optional)</em> A numeric value that determines how much
energy (edibility × 2.5) and health (edibility × 1.125) is restored when
this item is eaten. An item with an edibility of -300 can't be eaten,
values from -299 to -1 reduce health and energy, and zero can be eaten
but doesn't change health/energy. Default -300.</p></td>
</tr>
<tr>
<td><p><samp>IsDrink</samp></p></td>
<td><p><em>(Optional)</em> Whether to drink the item instead of eating
it. Default false.</p></td>
</tr>
<tr>
<td><p><samp>Buffs</samp></p></td>
<td><p><em>(Optional)</em> The buffs to apply to the player when this
item is eaten, if any. Default none.</p>
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
entry within the list.</p></td>
</tr>
<tr>
<td><p><samp>Duration</samp></p></td>
<td><p><em>(Optional if <samp>BuffId</samp> is set)</em> The buff
duration measured in in-game minutes. This can be set to <samp>-2</samp>
for a buff that should last for the rest of the day.</p></td>
</tr>
<tr>
<td><p><samp>BuffId</samp></p></td>
<td><p><em>(Optional)</em> The unique ID of a buff from
<samp>Data/Buffs</samp> to apply, or <samp>null</samp> to ignore
<samp>Data/Buffs</samp> and set the ID to <samp>food</samp> or
<samp>drink</samp> depending on the item's <samp>IsDrink</samp>
field.</p>
<p>If a buff from <samp>Data/Buffs</samp> is applied and you also
specify other fields, here's how the buff data is combined:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>result</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Duration</samp><br />
<samp>IconTexture</samp><br />
<samp>IconSpriteIndex</samp><br />
<samp>GlowColor</samp></p></td>
<td><p>If specified, the value in <samp>Data/Objects</samp> is used
instead of the one in <samp>Data/Buffs</samp>. If omitted, defaults to
the value from <samp>Data/Buffs</samp>.</p></td>
</tr>
<tr>
<td><p><samp>CustomAttributes</samp></p></td>
<td><p>The values from both entries are combined (e.g. +1 speed in
<samp>Data/Objects</samp> and +1 speed in <samp>Data/Buffs</samp>
results in +2 speed).</p></td>
</tr>
<tr>
<td><p><samp>IsDebuff</samp></p></td>
<td><p>The value in <samp>Data/Objects</samp> is used.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>IsDebuff</samp></p></td>
<td><p><em>(Optional)</em> Whether this buff counts as a debuff, so its
duration should be halved when wearing a Sturdy Ring. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>IconTexture</samp></p></td>
<td><p><em>(Optional)</em> The asset name for the icon texture to load.
This must contain one or more 16x16 icons in a grid of any size. If
omitted, the game will draw a default icon based on the
<samp>BuffId</samp> and <samp>CustomAttributes</samp> fields.</p></td>
</tr>
<tr>
<td><p><samp>IconSpriteIndex</samp></p></td>
<td><p><em>(Optional)</em> The buff's icon index within the
<samp>IconTexture</samp>, where 0 is the top-left icon. Default
0.</p></td>
</tr>
<tr>
<td><p><samp>GlowColor</samp></p></td>
<td><p><em>(Optional)</em> The glow color to apply to the player. See <a
href="Modding_Common_data_field_types#Color" class="wikilink"
title="color format">color format</a>. Default none.</p></td>
</tr>
<tr>
<td><p><samp>CustomAttributes</samp></p></td>
<td><p>The custom buff attributes to apply, if any.</p>
<p>This consists of a model with any combination of these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>CombatLevel</samp><br />
<samp>FarmingLevel</samp><br />
<samp>FishingLevel</samp><br />
<samp>ForagingLevel</samp><br />
<samp>LuckLevel</samp><br />
<samp>MiningLevel</samp><br />
<samp>CombatLevel</samp></p></td>
<td><p><em>(Optional)</em> An amount applied to the matching <a
href="Skills" class="wikilink" title="skill level">skill level</a> while
the buff is active. This can be negative for a debuff. Default
0.</p></td>
</tr>
<tr>
<td><p><samp>Attack</samp><br />
<samp>AttackMultiplier</samp><br />
<samp>CriticalChanceMultiplier</samp><br />
<samp>CriticalPowerMultiplier</samp><br />
<samp>Defense</samp><br />
<samp>Immunity</samp><br />
<samp>KnockbackMultiplier</samp><br />
<samp>MagneticRadius</samp><br />
<samp>MaxStamina</samp><br />
<samp>Speed</samp><br />
<samp>WeaponPrecisionMultiplier</samp><br />
<samp>WeaponSpeedMultiplier</samp></p></td>
<td><p><em>(Optional)</em> An amount applied to the player's <a
href="attack" class="wikilink" title="attack">attack</a>, <a
href="Crit._Chance" class="wikilink" title="critical chance">critical
chance</a> and <a href="Crit._Power" class="wikilink"
title="critical power">critical power</a>, <a href="defense"
class="wikilink" title="defense">defense</a>, <a href="immunity"
class="wikilink" title="immunity">immunity</a>, knockback (i.e. <a
href="weight" class="wikilink" title="weight">weight</a>), <a
href="Magnetism" class="wikilink" title="magnetic radius">magnetic
radius</a>, maximum <a href="Energy" class="wikilink"
title="stamina">stamina</a>, <a href="speed" class="wikilink"
title="speed">speed</a>, or weapon precision/<a href="speed"
class="wikilink" title="speed">speed</a> while the buff is active. This
can be negative for a debuff. Default 0.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### Geodes & artifact spots

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>GeodeDrops</samp><br />
<samp>&lt;samp&gt;GeodeDropsDefaultItems</samp></p></td>
<td><p><em>(Optional)</em> The items that can be dropped when breaking
open this item as a <a href="Minerals#Geodes" class="wikilink"
title="geode">geode</a>. Specifying either or both fields automatically
enables geode behavior for this item.</p>
<p>You can specify one or both fields:</p>
<ul>
<li><samp>GeodeDrops</samp> can be set to the specific items to drop.
Default none. This consists of a list of models with these fields:
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported by geode drops.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Chance</samp></p></td>
<td><p><em>(Optional)</em> The probability that the item will be dropped
if the other fields match, as a decimal value between 0 (never) and 1
(always). Default 1.</p></td>
</tr>
<tr>
<td><p><samp>SetFlagOnPickup</samp></p></td>
<td><p><em>(Optional)</em> The mail flag to set for the current player
when this drop is picked up.</p></td>
</tr>
<tr>
<td><p><samp>Precedence</samp></p></td>
<td><p><em>(Optional)</em> The order in which this entry should be
checked, where lower values are checked first. This can be a negative
value. Geode drops with the same precedence are checked in the order
listed. Default 0.</p>
<p>For consistency, vanilla drops mostly use these values:</p>
<ul>
<li><samp>-1000</samp>: special overrides like the <a
href="Golden_Helmet" class="wikilink" title="golden helmet">golden
helmet</a>;</li>
<li><samp>0</samp>: normal items.</li>
</ul></td>
</tr>
</tbody>
</table></li>
<li><samp>GeodeDropsDefaultItems</samp> chooses a predefined list of
possible geode drops like <a href="clay" class="wikilink"
title="clay">clay</a>, <a href="coal" class="wikilink"
title="coal">coal</a>, <a href="Copper_Ore" class="wikilink"
title="copper">copper</a>, <a href="Iridium_Ore" class="wikilink"
title="iridium">iridium</a>, etc. Default false.</li>
</ul>
<p>If both fields are specified, each geode will choose between them
with an equal 50% chance. If <samp>GeodeDrops</samp> is specified but no
entries match, the geode will use the
<samp>GeodeDropsDefaultItems</samp> regardless of whether it's
true.</p></td>
</tr>
<tr>
<td><p><samp>ArtifactSpotChances</samp></p></td>
<td><p><em>(Optional)</em> If this is an artifact (i.e. the
<samp>Type</samp> field is <samp>Arch</samp>), the chance that it can be
found by digging <a href="Artifact_Spot" class="wikilink"
title="artifact spots">artifact spots</a> in each location.</p>
<p>This consists of a string → model lookup, where:</p>
<ul>
<li>the key is the internal location name;</li>
<li>the value is the probability the item will spawn if checked, as a
decimal value between 0 (never) and 1 (always).</li>
</ul></td>
</tr>
</tbody>
</table>

### Context tags & exclusions

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ContextTags</samp></p></td>
<td><p><em>(Optional)</em> The custom <a href="Modding_Context_tags"
class="wikilink" title="context tags">context tags</a> to add for this
item (in addition to the tags added automatically based on the other
object data). This is formatted as a list; for example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ContextTags&quot;</span><span class="er">:</span> <span class="ot">[</span> <span class="st">&quot;color_yellow&quot;</span><span class="ot">,</span> <span class="st">&quot;fish_ocean&quot;</span><span class="ot">,</span> <span class="st">&quot;fish_upright&quot;</span><span class="ot">,</span> <span class="st">&quot;season_summer&quot;</span> <span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>CanBeGivenAsGift</samp></p></td>
<td><p><em>(Optional)</em> Whether this item can be gifted to NPCs.
Default true.</p></td>
</tr>
<tr>
<td><p><samp>CanBeTrashed</samp></p></td>
<td><p><em>(Optional)</em> Whether this item can be trashed from the
player's inventory. Also affects whether the item can be shipped but not
whether it can be sold to shops. Default true.</p></td>
</tr>
<tr>
<td><p><samp>ExcludeFromRandomSale</samp></p></td>
<td><p><em>(Optional)</em> Whether to exclude this item from shops when
selecting random items to sell. Default false.</p></td>
</tr>
<tr>
<td><p><samp>ExcludeFromFishingCollection</samp><br />
<samp>ExcludeFromShippingCollection</samp></p></td>
<td><p><em>(Optional)</em> Whether to exclude this item from the
fishing/shipping collection and their respective effect on the <a
href="perfection" class="wikilink" title="perfection score">perfection
score</a>. Default false, in which case the normal requirements apply
(e.g., artifacts are always excluded from the shipping
collection).</p></td>
</tr>
</tbody>
</table>

### Advanced

| field | purpose |
|----|----|
| `CustomFields` | *(Optional)* The <a href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry. |

## Unobtainable items

The spritesheet and data have items that can't normally be found in the
player inventory (like twigs and lumber), and some sprites have no
corresponding item data. There are also multiple entries for *weeds* and
*stone* corresponding to different sprites, but the player can only
normally obtain one *stone* item (index 390) and no *weeds* items.

## For C# mods

Object-type items are represented by the `StardewValley.Object` type.

This provides many methods to simplify common logic. Some notable
examples:

| method | effect |
|----|----|
| `Object.GetRadiusForScarecrow()` | The tile radius that Object protects as a scarecrow. Default behavior: Checks for the value in the `crow_scare_radius_<radius>` <a href="Modding_Context_tags" class="wikilink"
title="context tag">context tag</a> if applicable, then defaults to 17 if the internal name contains "Deluxe" and 9 otherwise. Can be patched to support custom scarecrows. |
| `Object.IsBar()` | Whether the item is a <a href="Copper_Bar" class="wikilink" title="copper bar">copper bar</a>, <a href="Iron_Bar" class="wikilink" title="iron bar">iron bar</a>, <a href="Gold_Bar" class="wikilink" title="gold bar">gold bar</a>, <a href="Iridium_Bar" class="wikilink" title="iridium bar">iridium
bar</a>, or <a href="Radioactive_Bar" class="wikilink"
title="radioactive bar">radioactive bar</a>. |
| `Object.IsBreakableStone()` | Whether the item is a stone debris item which can be broken by a pickaxe. |
| `Object.IsFence()` | Whether the item is a <a href="Crafting#Fences" class="wikilink" title="fence">fence</a>. |
| `Object.IsFruitTreeSapling()` | Whether the item is a <a href="Fruit_Trees" class="wikilink" title="fruit tree">fruit tree</a> sapling. This checks the `Data\fruitTrees` keys, so it works with custom fruit trees too. |
| `Object.IsHeldOverHead()` | Whether the player is shown holding up the item when it's selected in their toolbar. Default true (except for furniture). |
| `Object.IsIncubator()` | Whether the item can incubate <a href="Animals" class="wikilink" title="farm animal">farm animal</a> eggs when placed in a building. |
| `Object.IsScarecrow()` | Whether the item is a scarecrow. Default: `true` if the object has the `crow_scare` <a href="Modding_Context_tags" class="wikilink"
title="context tag">context tag</a>. Otherwise, returns whether the object's internal name contains "arecrow". Can be patched to support custom scarecrows. |
| `Object.IsTapper()` | Whether the item is a <a href="Tapper" class="wikilink" title="tapper">tapper</a> or <a href="Heavy_Tapper" class="wikilink" title="heavy tapper">heavy
tapper</a>. |
| `Object.IsTeaSapling()` | Whether the item is a <a href="Tea_Sapling" class="wikilink" title="tea sapling">tea
sapling</a>. |
| `Object.IsTwig()` | Whether the item is a twig debris item. |
| `Object.IsWeeds()` | Whether the item is a weed debris item. |

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Объекты" class="wikilink"
title="ru:Модификации:Объекты">ru:Модификации:Объекты</a>
<a href="zh_模组_物体" class="wikilink"
title="zh:模组:物体">zh:模组:物体</a>
