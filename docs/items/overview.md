---
title: "Overview"
wiki_source: "Modding:Items"
permalink: /Modding:Items/
category: items
tags: [items, overview, item-ids, item-types, item-sprites, define-a-custom-item, error-items, common-data]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses item data. This is an
advanced guide for mod developers.

## Overview

### Item IDs

Every item is identified in the game data using a unique item ID. This
has two forms:

- The *unqualified item ID* (`item.ItemId`) is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  item, like `128` (vanilla item) or `Example.ModId_Watermelon` (custom
  item). For legacy reasons, the unqualified ID for vanilla items may
  not be globally unique; for example, Pufferfish (object 128) and
  Mushroom Box (bigcraftable 128) both have item ID `128`.
- The *qualified item ID* (`item.QualifiedItemId`) is a globally unique
  identifier which combines the item's
  <a href="#Item_types" class="wikilink" title="type ID">type ID</a> and
  unqualified item ID, like `(O)128` for
  <a href="Modding_Objects" class="wikilink" title="object">object</a>
  ID 128.

With <a href="Modding_Player_Guide_Getting_Started" class="wikilink"
title="SMAPI installed">SMAPI installed</a>, you can
<a href="Modding_Console_commands#Console_commands" class="wikilink"
title="run the list_items console command">run the
<samp>list_items</samp> console command</a> in-game to search item IDs.

**Note:** mods created before Stardew Valley 1.6 may use the
`item.ParentSheetIndex` field as an item identifier. This is *not* a
valid identifier; multiple items of the same type may have the same
sprite index for different textures.

### Item types

Items are defined by *item type data definitions*, which handle parsing
data of a certain type. For example, the game's `ObjectDataDefinition`
class handles producing <a href="Modding_Objects" class="wikilink"
title="object-type items">object-type items</a> by parsing the
`Data/Objects` asset.

Each definition has a unique ID like `(O)`, which is used to form
globally unique <a href="#Item_IDs" class="wikilink"
title="qualified item IDs">qualified item IDs</a>. In C# code, this is
tracked by the `item.TypeDefinitionId` field, which matches
`ItemRegistry.type_*` constants for vanilla item types.

These are the item types for which custom items can added/edited:

| item type | type identifier | data asset | brief summary |
|----|----|----|----|
| <a href="Modding_Objects" class="wikilink" title="Objects">Objects</a> | `(O)` | `Data/Objects` | The most common item type. Depending on their data, they can be placed in the world, picked up, eaten, sold to shops, etc. |
| <a href="Modding_Big_craftables" class="wikilink"
title="Big craftables">Big craftables</a> | `(BC)` | `Data/BigCraftables` | Items which can be placed in the world and are two tiles tall (instead of one like objects). |
| <a href="Modding_Boots" class="wikilink" title="Boots">Boots</a> | `(B)` | `Data/Boots` | Items which can be equipped in the player's <a href="boots" class="wikilink" title="boots">boots</a> slot. These change the player sprite and may provide buffs. |
| <a href="Modding_Furniture" class="wikilink"
title="Furniture">Furniture</a> | `(F)` | `Data/Furniture` | Decorative items which can be placed in the world. In some cases players can sit on them or place items on them. |
| <a href="Modding_Hats" class="wikilink" title="Hats">Hats</a> | `(H)` | `Data/Hats` | Items which can be equipped in the player's <a href="Hats" class="wikilink" title="hat">hat</a> slot. These change the player sprite. |
| <a href="Modding_Mannequins" class="wikilink"
title="Mannequins">Mannequins</a> | `(M)` | `Data/Mannequins` | Decorative items which can be placed in the world, and used to store and display clothing. |
| <a href="Modding_Pants" class="wikilink" title="Pants">Pants</a> | `(P)` | `Data/Pants` | Items which can be equipped in the player's <a href="Tailoring#Pants" class="wikilink" title="pants">pants</a> slot. These change the player sprite. |
| <a href="Modding_Shirts" class="wikilink" title="Shirts">Shirts</a> | `(S)` | `Data/Shirts` | Items which can be equipped in the player's <a href="Tailoring#Shirts" class="wikilink" title="shirt">shirt</a> slot. These change the player sprite. |
| <a href="Modding_Tools" class="wikilink" title="Tools">Tools</a> | `(T)` | `Data/Tools` | Items that can be swung or used by the player to perform some effect (e.g. dig dirt, chop trees, milk or shear animals, etc). |
| <a href="Modding_Trinkets" class="wikilink"
title="Trinkets">Trinkets</a> | `(TR)` | `Data/Trinkets` | Items that can be equipped in the player's <a href="Trinkets" class="wikilink" title="trinket">trinket</a> slot to enable special effects. |
| <a href="Modding_Wallpaper_and_flooring" class="wikilink"
title="Wallpaper &amp; flooring">Wallpaper &amp; flooring</a> | `(WP)` and `(FL)` | `Data/AdditionalWallpaperFlooring` | Items which can be applied to a decoratable location (e.g. a <a href="farmhouse" class="wikilink" title="farmhouse">farmhouse</a> or <a href="shed" class="wikilink" title="shed">shed</a>) to visually change its floor or wall design. (These are separate from placeable items like <a href="Brick_Floor" class="wikilink" title="brick floor">brick
floor</a>.) |
| <a href="Modding_Weapons" class="wikilink" title="Weapons">Weapons</a> | `(W)` | `Data/Weapons` | Items which can be swung or used by the player to damage monsters. |

When resolving an unqualified item ID like `128`, the game will get the
first item type for which it exists in this order: object, big
craftable, furniture, weapon, boots, hat, mannequin, pants, shirt, tool,
trinket, wallpaper, and floorpaper.

### Item sprites

For each item type, the game has two files in its `Content` folder
(which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>):

- a *data asset* for the text data for its items (names, descriptions,
  prices, etc);
- and a *spritesheet* for the in-game item icons.

Each item has a `ParentSheetIndex` field which is its position in the
item type's spritesheet, starting at 0 in the top-left and incrementing
by one as you move across and then down. For example, hat \#0 is the
first sprite in `Characters/Farmer/hats`.

### Define a custom item

You can define custom items for most vanilla item types using only
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> or
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="SMAPI&#39;s content API">SMAPI's content API</a>.

For example, this content pack adds a new Pufferchick item with a custom
image, custom gift tastes, and a custom crop that produces it. Note that
item references in other data assets like `Data/Crops` and
`Data/NPCGiftTastes` use the item ID.

Most item data assets work just like `Data/Objects`. See also specific
info for <a href="Modding_Fruit_trees" class="wikilink"
title="custom fruit trees">custom fruit trees</a>,
<a href="Modding_Tools" class="wikilink" title="custom tools">custom
tools</a>, and
<a href="Modding_Weapons" class="wikilink" title="melee weapons">melee
weapons</a>.

### Error items

When an item is broken (e.g. due to deleting the mod which adds it),
it's represented in-game as a default
<a href="Error_Item" class="wikilink" title="Error Item">Error Item</a>
with a `🛇` sprite. This keeps the previous item data in case the item
data is re-added.

## Common data

### Quality

Each item has a quality level which (depending on the item type) may
affect its price, health boost, etc. The valid qualities are:

| quality | value | constant             |
|---------|-------|----------------------|
| normal  | `0`   | `Object.lowQuality`  |
| silver  | `1`   | `Object.medQuality`  |
| gold    | `2`   | `Object.highQuality` |
| iridium | `4`   | `Object.bestQuality` |

### Categories

Each item also has a category (represented by a negative integer). In
code, you can get an item's category value from `item.Category`, and its
translated name from `item.getCategoryName()`. Here are the valid
categories:

| value | internal constant | <a href="Modding_Context_tags" class="wikilink"
title="context tag">context tag</a> | English translation | Color | Properties |
|----|----|----|----|----|----|
| -2 | `Object.GemCategory` | `category_gem` | Mineral | `#6E005A` | Affected by <a href="Skills#Mining" class="wikilink"
title="Gemologist">Gemologist</a> profession |
| -4 | `Object.FishCategory` | `category_fish` | Fish | `#00008B` (DarkBlue) | Affected by <a href="Skills#Fishing" class="wikilink" title="Fisher">Fisher</a> and <a href="Skills#Fishing" class="wikilink" title="Angler">Angler</a> professions |
| -5 | `Object.EggCategory` | `category_egg` | Animal Product | `#FF0064` | Affected by <a href="Skills#Farming" class="wikilink" title="Rancher">Rancher</a> profession, can be used in a slingshot |
| -6 | `Object.MilkCategory` | `category_milk` | Animal Product | `#FF0064` | Affected by <a href="Skills#Farming" class="wikilink" title="Rancher">Rancher</a> profession |
| -7 | `Object.CookingCategory` | `category_cooking` | Cooking | `#DC3C00` |  |
| -8 | `Object.CraftingCategory` | `category_crafting` | Crafting \|style="background-color:#943D28;color:#FFF;text-align:center"\>\|`#943D28` | Is Placeable |  |
| -9 | `Object.BigCraftableCategory` | `category_big_craftable` |  |  | Is Placeable |
| -12 | `Object.mineralsCategory` | `category_minerals` | Mineral | `#6E005A` | Affected by <a href="Skills#Mining" class="wikilink"
title="Gemologist">Gemologist</a> profession |
| -14 | `Object.meatCategory` | `category_meat` | Animal Product | `#FF0064` |  |
| -15 | `Object.metalResources` | `category_metal_resources` | Resource | `#406672` |  |
| -16 | `Object.buildingResources` | `category_building_resources` | Resource | `#406672` |  |
| -17 | `Object.sellAtPierres` | `category_sell_at_pierres` |  |  |  |
| -18 | `Object.sellAtPierresAndMarnies` | `category_sell_at_pierres_and_marnies` | Animal Product | `#FF0064` | Affected by <a href="Skills#Farming" class="wikilink" title="Rancher">Rancher</a> profession |
| -19 | `Object.fertilizerCategory` | `category_fertilizer` | Fertilizer | `#708090` (SlateGray) | Is Placeable, is always passable |
| -20 | `Object.junkCategory` | `category_junk` | Trash | `#696969` (DimGray) |  |
| -21 | `Object.baitCategory` | `category_bait` | Bait | `#8B0000` (DarkRed) | Can be attached to a fishing rod |
| -22 | `Object.tackleCategory` | `category_tackle` | Fishing Tackle | `#008B8B` (DarkCyan) | Can be attached to a fishing rod, cannot stack |
| -23 | `Object.sellAtFishShopCategory` | `category_sell_at_fish_shop` |  |  |  |
| -24 | `Object.furnitureCategory` | `category_furniture` | Decor | `#9650BE` |  |
| -25 | `Object.ingredientsCategory` | `category_ingredients` | Cooking |  |  |
| -26 | `Object.artisanGoodsCategory` | `category_artisan_goods` | Artisan Goods | `#009B6F` | Affected by <a href="Skills#Farming" class="wikilink" title="Artisan">Artisan</a> profession |
| -27 | `Object.syrupCategory` | `category_syrup` | Artisan Goods | `#009B6F` | Affected by <a href="Skills#Foraging" class="wikilink" title="Tapper">Tapper</a> profession |
| -28 | `Object.monsterLootCategory` | `category_monster_loot` | Monster Loot | `#320A46` |  |
| -29 | `Object.equipmentCategory` | `category_equipment` |  |  |  |
| -74 | `Object.SeedsCategory` | `category_seeds` | Seed | `#A52A2A` (Brown) | Is Placeable, is always passable |
| -75 | `Object.VegetableCategory` | `category_vegetable` | Vegetable | `#008000` (Green) | Affected by <a href="Skills#Farming" class="wikilink" title="Tiller">Tiller</a> profession, can be used in a slingshot |
| -79 | `Object.FruitsCategory` | `category_fruits` | Fruit | `#FF1493` (DeepPink) | Affected by <a href="Skills#Farming" class="wikilink" title="Tiller">Tiller</a> profession (if not foraged), can be used in a slingshot |
| -80 | `Object.flowersCategory` | `category_flowers` | Flower | `#DB36D3` | Affected by <a href="Skills#Farming" class="wikilink" title="Tiller">Tiller</a> profession |
| -81 | `Object.GreensCategory` | `category_greens` | Forage | `#0A8232` |  |
| -95 | `Object.hatCategory` | `category_hat` |  |  |  |
| -96 | `Object.ringCategory` | `category_ring` |  |  |  |
| -97 | `Object.bootsCategory` | `category_boots` |  |  |  |
| -98 | `Object.weaponCategory` | `category_weapon` |  |  |  |
| -99 | `Object.toolCategory` | `category_tool` |  |  |  |
| -100 | `Object.clothingCategory` | `category_clothing` |  |  |  |
| -101 | `Object.trinketCategory` | `category_trinket` |  |  |  |
| -102 | `Object.booksCategory` |  |  | `#552F1B` |  |
| -103 | `Object.skillBooksCategory` |  |  | `#7A5d27` |  |
| -999 | `Object.litterCategory` | `category_litter` |  |  |  |

### Context tags

A *context tag* is an arbitrary data label like `category_gem` or
`item_apple` attached to items. These provide metadata about items
(*e.g.* their color, quality, category, general groupings like alcohol
or fish, etc), and may affect game logic (*e.g.* machine processing).

See <a href="Modding_Context_tags" class="wikilink"
title="Modding:Context tags">Modding:Context tags</a> for more info.

## Specific item types

For docs about each item type (e.g. objects or weapons), see the
<a href="#Item_types" class="wikilink" title="item types"><em>item
types</em></a> table above.

## For C# mods

### Identify items

You can uniquely identify items by checking their
<a href="#Item_IDs" class="wikilink" title="item ID">item ID</a> fields.
For example:

``` c#
bool isPufferfish = item.QualifiedItemId == "(O)128";
```

The `ItemRegistry` class also provides methods to work with items. For
example:

``` c#
// check if item would be matched by a qualified or unqualified item ID
bool isPufferfish = ItemRegistry.HasItemId(item, "128");

// qualify an item ID if needed
string pufferfishQualifiedId = ItemRegistry.QualifyItemId("128"); // returns "(O)128"
```

Note that flavored items like
<a href="Jellies_and_Pickles" class="wikilink"
title="jellies">jellies</a> and
<a href="wine" class="wikilink" title="wine">wine</a> don't have their
own ID. For example, Blueberry Wine and Wine are both `(O)348`. You can
get the flavor item ID from the `preservedParentSheetIndex` field; for
example, Blueberry Wine will have the item ID for blueberry. (Despite
the name, it contains the item's ID rather than its `ParentSheetIndex`).

### Create item instances

The `ItemRegistry.Create` method is the main way to construct items. For
example:

``` c#
Item pufferfish = ItemRegistry.Create("(O)128"); // can optionally specify count and quality
```

If the ID doesn't match a real item, the `ItemRegistry` will return an
<a href="Error_Item" class="wikilink" title="Error Item">Error Item</a>
by default. You can override that by setting `allowNull: true` when
calling the method.

You can also get a specific value type instead of `Item` if needed. This
will throw a descriptive exception if the type isn't compatible (e.g.
you try to convert furniture to boots).

``` c#
Boots boots = ItemRegistry.Create<Boots>("(B)505"); // Rubber Boots
```

When creating an item manually instead, make sure to pass its `ItemId`
(*not* `QualifiedItemId`) to the constructor. For example:

``` c#
Item pufferfish = new Object("128", 1);
```

### Work with item metadata

The `ItemRegistry` class provides several methods for working with item
metadata. Some useful methods include:

<table>
<thead>
<tr>
<th><p>method</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ItemRegistry.Create</samp></p></td>
<td><p><a href="#Create_item_instances" class="wikilink"
title="Create an item instance">Create an item instance</a>.</p></td>
</tr>
<tr>
<td><p><samp>ItemRegistry.Exists</samp></p></td>
<td><p>Get whether a qualified or unqualified item ID matches an
existing item. For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="dt">bool</span> pufferfishExists <span class="op">=</span> ItemRegistry<span class="op">.</span><span class="fu">Exists</span><span class="op">(</span><span class="st">&quot;(O)128&quot;</span><span class="op">);</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>ItemRegistry.IsQualifiedId</samp></p></td>
<td><p>Get whether the given item ID is qualified with the type prefix
(like <samp>(O)128</samp> instead of <samp>128</samp>).</p></td>
</tr>
<tr>
<td><p><samp>ItemRegistry.QualifyItemId</samp></p></td>
<td><p>Get the unique qualified item ID given an unqualified or
qualified one. For example:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="dt">string</span> qualifiedId <span class="op">=</span> ItemRegistry<span class="op">.</span><span class="fu">QualifyItemId</span><span class="op">(</span><span class="st">&quot;128&quot;</span><span class="op">);</span> <span class="co">// returns (O)128</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>ItemRegistry.GetMetadata</samp></p></td>
<td><p>Get high-level info about an item:</p>
<div class="sourceCode" id="cb3"><pre class="sourceCode c#"><code class="sourceCode cs"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="co">// get info about Rubber Boots</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>ItemMetadata metadata <span class="op">=</span> ItemRegistry<span class="op">.</span><span class="fu">GetMetadata</span><span class="op">(</span><span class="st">&quot;(B)505&quot;</span><span class="op">);</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="co">// get item ID info</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>$<span class="st">&quot;The item has unqualified ID {metadata.LocalId}, qualified ID {metadata.QualifiedId}, and is defined by the {metadata.TypeIdentifier} item data definition.&quot;</span><span class="op">;</span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a><span class="co">// does the item exist in the data files?</span></span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a><span class="dt">bool</span> exists <span class="op">=</span> metadata<span class="op">.</span><span class="fu">Exists</span><span class="op">();</span></span></code></pre></div>
<p>And get common parsed item data:</p>
<div class="sourceCode" id="cb4"><pre class="sourceCode c#"><code class="sourceCode cs"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="co">// get parsed info</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>ParsedItemData data <span class="op">=</span> metadata<span class="op">.</span><span class="fu">GetParsedData</span><span class="op">();</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>$<span class="st">&quot;The internal name is {data.InternalName}, translated name {data.DisplayName}, description {data.Description}, etc.&quot;</span><span class="op">;</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a><span class="co">// draw an item sprite</span></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>Texture2D texture <span class="op">=</span> data<span class="op">.</span><span class="fu">GetTexture</span><span class="op">();</span></span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>Rectangle sourceRect <span class="op">=</span> data<span class="op">.</span><span class="fu">GetSourceRect</span><span class="op">();</span></span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a>spriteBatch<span class="op">.</span><span class="fu">Draw</span><span class="op">(</span>texture<span class="op">,</span> Vector2<span class="op">.</span><span class="fu">Zero</span><span class="op">,</span> sourceRect<span class="op">,</span> Color<span class="op">.</span><span class="fu">White</span><span class="op">);</span></span></code></pre></div>
<p>And create an item:</p>
<div class="sourceCode" id="cb5"><pre class="sourceCode c#"><code class="sourceCode cs"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a>Item item <span class="op">=</span> metadata<span class="op">.</span><span class="fu">CreateItem</span><span class="op">();</span></span></code></pre></div>
<p>And get the type definition (note that this is very specialized, and
you should usually use <samp>ItemRegistry</samp> instead to benefit from
its caching and optimizations):</p>
<div class="sourceCode" id="cb6"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a>IItemDataDefinition typeDefinition <span class="op">=</span> info<span class="op">.</span><span class="fu">GetTypeDefinition</span><span class="op">();</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>ItemRegistry.ResolveMetadata</samp></p></td>
<td><p>Equivalent to <samp>ItemRegistry.GetMetadata</samp>, except that
it'll return null if the item doesn't exist.</p></td>
</tr>
<tr>
<td><p><samp>ItemRegistry.GetData</samp></p></td>
<td><p>Get the parsed data about an item, or <samp>null</samp> if the
item doesn't exist. This is a shortcut for
<code>ItemRegistry.ResolveMetadata(id)?.GetParsedData()</code>; see the
previous method for info on the parsed data.</p></td>
</tr>
<tr>
<td><p><samp>ItemRegistry.GetDataOrErrorItem</samp></p></td>
<td><p>Equivalent to <samp>ItemRegistry.GetData</samp>, except that
it'll return info for an <a href="Error_Item" class="wikilink"
title="Error Item">Error Item</a> if the item doesn't exist (e.g. for
drawing in inventory).</p></td>
</tr>
<tr>
<td><p><samp>ItemRegistry.GetErrorItemName</samp></p></td>
<td><p>Get a translated <em>Error Item</em> label.</p></td>
</tr>
</tbody>
</table>

### Define custom item types

You can implement `IItemDataDefinition` for your own item type, and call
`ItemRegistry.AddTypeDefinition` to register it. This provides all the
logic needed by the game to handle the item type: where to get item
data, how to draw them, etc.

**This is extremely specialized**, and multiplayer compatibility is
unknown. Most mods should add custom items within the existing types
instead.

## See also

- For specific item types, see the
  <a href="#Item_types" class="wikilink" title="item types"><em>item
  types</em></a> table above.
- <a href="Modding_Index" class="wikilink"
  title="Modding:Index">Modding:Index</a> for related content like
  <a href="Modding_Crop_data" class="wikilink" title="crops">crops</a>,
  <a href="Modding_Fish_data" class="wikilink" title="fish">fish</a>,
  <a href="Modding_Gift_taste_data" class="wikilink"
  title="gift tastes">gift tastes</a>, and
  <a href="Modding_Recipe_data" class="wikilink"
  title="recipes">recipes</a>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Предметы" class="wikilink"
title="ru:Модификации:Предметы">ru:Модификации:Предметы</a>
<a href="zh_模组_物品数据" class="wikilink"
title="zh:模组:物品数据">zh:模组:物品数据</a>
