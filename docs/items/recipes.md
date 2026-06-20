---
title: "Recipes"
wiki_source: "Modding:Recipe data"
permalink: /Modding:Recipe_data/
category: items
tags: [recipe-data, raw-data, cooking-recipes, crafting-recipes, format, ingredients-and-yield, unlock-conditions, exceptions]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses recipe data for
cooking and crafting. (Tailoring recipes use a different format.) This
is an advanced guide for mod developers.

## Raw data

### Cooking recipes

Cooking recipe data is stored in `Content\Data\CookingRecipes.xnb`,
which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of for reference:

### Crafting recipes

Crafting recipe data is stored in `Content\Data\CraftingRecipes.xnb`,
which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of for reference:

## Format

<table>
<thead>
<tr>
<th colspan="2"><p>Index</p></th>
<th><p>Field</p></th>
<th colspan="2"><p>Example Value</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><small>Cooking</small></p></td>
<td><p><small>Crafting</small></p></td>
<td><p><small>Cooking</small></p></td>
<td><p><small>Crafting</small></p></td>
<td></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><p>Key</p></td>
<td><p>Name</p></td>
<td><p><em>Salad</em></p></td>
<td><p><em>Stone Fence</em></p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><p>0</p></td>
<td><p>Ingredients</p></td>
<td><p><em>20 1 22 1 419 1</em></p></td>
<td><p><em>390 2</em></p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><p>1</p></td>
<td><p>(Unused)</p></td>
<td><p><em>25 5</em></p></td>
<td><p><em>Field</em></p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><p>2</p></td>
<td><p>Yield</p></td>
<td><p><em>196</em></p></td>
<td><p><em>323</em></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>—</p></td>
<td style="text-align: center;"><p>3</p></td>
<td><p>Big craftable?</p></td>
<td><p>—</p></td>
<td><p><em>false</em></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>3</p></td>
<td style="text-align: center;"><p>4</p></td>
<td><p>Unlock conditions</p></td>
<td><p><em>f Emily 3</em></p></td>
<td><p><em>s Farming 2</em></p></td>
</tr>
<tr>
<td style="text-align: center;"><p>4</p></td>
<td style="text-align: center;"><p>5</p></td>
<td><p>Display name<br />
<small>Tokenizable String. Defaults to the display name of the first
product if not given.</small></p></td>
<td><p><em>Ensalada</em></p></td>
<td><p><em>Valla de piedra</em></p></td>
</tr>
</tbody>
</table>

The values in **Index 1** are of different types for cooking and
crafting recipes, but both kinds of value are unused by the game. For
cooking, the field is set to a pair of numbers. For crafting, the field
is set to `Home` or `Field`. The values in this field don't affect
anything, so any pair of numbers can be used, but the field must be
present in the recipe code.

### Ingredients and yield

The **ingredients** are a space-separated list of numbers in pairs. The
first number of each pair is an object index from
<a href="Modding_Objects" class="wikilink"
title="Data/Objects.xnb">Data/Objects.xnb</a>. (Negative numbers refer
to categories, also listed in that article.) The second number of each
pair is the quantity of that object that is required for the recipe.

The **yield** is also a space-separated list of numbers in pairs. The
first number of each pair is an
<a href="Modding_Objects" class="wikilink" title="object">object</a> or
<a href="Modding_Big_craftables" class="wikilink"
title="big craftable">big craftable</a> ID. The second number of each
pair is the quantity of that object (or big craftable) that is created
by the recipe. If there is only one object/craftable yielded, the
quantity is optional and defaults to one.

### Unlock conditions

The **unlock conditions** field supports any one of these condition
types, depending on recipe type:

<table>
<thead>
<tr>
<th><p>Syntax</p></th>
<th><p>Applicability</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>f &lt;NPC&gt; &lt;hearts&gt;</samp></p></td>
<td><p>Cooking</p></td>
<td><p>When the player reaches the given number of hearts of friendship
with the named NPC, a letter with the key
<samp>&lt;NPC&gt;Cooking</samp> will be queued for delivery tomorrow.
That letter then unlocks the recipe with the <a
href="Modding_Mail_data#Value" class="wikilink"
title="%item cookingRecipe %% token"><samp>%item cookingRecipe %%</samp>
token</a>.</p></td>
</tr>
<tr>
<td><p><samp>s &lt;skill&gt; &lt;level&gt;</samp></p></td>
<td><p>both</p></td>
<td><p>When the player reaches the given level of the named skill, the
recipe will be unlocked on the level up menu. The valid skill names are
<code>Farming</code>, <code>Mining</code>, <code>Fishing</code>,
<code>Foraging</code>, <code>Luck</code>, and <code>Combat</code> (but
<code>Luck</code> is unimplemented).</p></td>
</tr>
<tr>
<td><p><samp>default</samp></p></td>
<td><p>both</p></td>
<td><p>This recipe is learned automatically. Any missing default recipes
will be learned on day start. For example, the <a href="Chest"
class="wikilink" title="chest">chest</a> recipe is <samp>"388
50/Home/130/true/default/"</samp>.</p></td>
</tr>
<tr>
<td><p><samp>none</samp><br />
<em>or any other value</em></p></td>
<td><p>both</p></td>
<td><p>The recipe must be unlocked in some other way, such as an event.
(See <a href="#Exceptions" class="wikilink"
title="Exceptions">Exceptions</a> below for starting recipes and other
hard-coded unlocks.)</p></td>
</tr>
</tbody>
</table>

### Exceptions

When the game cannot locate a recipe key in the data, the
<a href="Torch" class="wikilink" title="Torch">Torch</a> recipe is
loaded instead.

The <a href="Fishing#Fishing_Skill" class="wikilink"
title="Trapper profession">Trapper profession</a> is hard-coded to reset
the ingredients for the
<a href="Crab_Pot" class="wikilink" title="Crab Pot">Crab Pot</a> recipe
to 25 <a href="Wood" class="wikilink" title="Wood">Wood</a> and 2
<a href="Copper_Bar" class="wikilink" title="Copper Bar">Copper Bar</a>.

The following recipes are hard-coded to be unlocked from the start of
the game:

- <a href="Chest" class="wikilink" title="Chest">Chest</a>
- <a href="Wood_Fence" class="wikilink" title="Wood Fence">Wood Fence</a>
- <a href="Gate" class="wikilink" title="Gate">Gate</a>
- <a href="Torch" class="wikilink" title="Torch">Torch</a>
- <a href="Campfire" class="wikilink" title="Campfire">Campfire</a>
- <a href="Wood_Path" class="wikilink" title="Wood Path">Wood Path</a>
- <a href="Cobblestone_Path" class="wikilink"
  title="Cobblestone Path">Cobblestone Path</a>
- <a href="Gravel_Path" class="wikilink" title="Gravel Path">Gravel
  Path</a>
- <a href="Wood_Sign" class="wikilink" title="Wood Sign">Wood Sign</a>
- <a href="Stone_Sign" class="wikilink" title="Stone Sign">Stone Sign</a>
- <a href="Fried_Egg" class="wikilink" title="Fried Egg">Fried Egg</a>

The <a href="Cask" class="wikilink" title="Cask">Cask</a> recipe is
hard-coded to unlock when the cellar upgrade is complete.

Recipes that are unlocked during vanilla game events are hard-coded to
be unlocked when those events are skipped.

The recipes unlocked by <a href="The_Queen_of_Sauce" class="wikilink"
title="The Queen of Sauce">The Queen of Sauce</a> TV channel are set in
`Content\Data\TV\CookingChannel.xnb`.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Рецепты" class="wikilink"
title="ru:Модификации:Рецепты">ru:Модификации:Рецепты</a>
<a href="zh_模组_配方数据" class="wikilink"
title="zh:模组:配方数据">zh:模组:配方数据</a>
