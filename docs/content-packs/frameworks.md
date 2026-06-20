---
title: "Frameworks"
wiki_source: "Modding:Content pack frameworks"
permalink: /Modding:Content_pack_frameworks/
category: content-packs
tags: [content-pack-frameworks, content-patcher, other-popular-frameworks, core-1000-content-packs, popular-400, common-100, specialized-frameworks, see-also]
---
← <a href="Modding_Index" class="wikilink"
title="Modding:Index">Modding:Index</a>

**Content pack frameworks** are SMAPI mods designed to simplify the
process of creating content packs for Stardew Valley. While they aim to
minimize the need for programming experience, some familiarity with
coding concepts can be helpful. Creating mods directly in C# for SMAPI
may offer insight into the way the game works.
<a href="Modding_Content_packs" class="wikilink"
title="Content packs">Content packs</a> are one of the two main ways to
mod Stardew Valley, alongside
<a href="Modding_Modder_Guide_Get_Started" class="wikilink"
title="creating C# mods for SMAPI directly">creating C# mods for SMAPI
directly</a>.

Here's a [list of
software](https://gist.github.com/ishanjalan/c8efb21afa21f74a052293176db107f7)
for pixel art and JSON text editors we recommend. With software like VS
Code and Sublime, you can set up the schema so it checks the formatting
of your JSON file as you write your mod. In that way, it's like a built
in [json validator site](https://smapi.io/json/). More details on
setting up the schema
[here](https://github.com/Pathoschild/SMAPI/blob/stable/docs/technical/web.md#using-a-schema-file-directly).

## Content Patcher

The recommended framework mod to use is , which allows you to change how
Stardew Valley loads its contents, assets, sprites, maps, and even much
of its logic from its
<a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
class="wikilink" title="Content folder"><samp>Content</samp> folder</a>.

The following is a non-exhaustive list of new things you can add to the
game using Content Patcher:

- Items (including cooking, crops, trees, clothing, furniture, and new
  artisan machines that can process inputs)
- Buildings, maps, and locations
- Farm animals and pets
- NPCs, including dialogue, sprites, schedule and events
- Mail, shops, quests, and special orders

With Content Patcher you can also patch existing assets, which includes:

- Retexturing sprites, including (but not limited to) item sprites, NPC
  portraits and map appearance
- Changing NPC behavior, dialogue or even their name
- Modify maps to add new locations or warps

See <a href="Modding_Content_Patcher" class="wikilink"
title="Modding:Content Patcher">Modding:Content Patcher</a> for a
getting started guide.

## Other popular frameworks

While you want to use Content Patcher in most cases, other frameworks
can be useful if you need features that isn't supported by the game
engine itself. These framework mods usually either extend Content
Patcher by adding new assets to the game for content packs to edit (in
which case they don't have their own content pack formats, but instead
rely on Content Patcher's own), or define their own separate formats.

Here is a non-exhaustive list of framework mods used most often to
create content packs. <small>(The parenthesis next to each name is the
<a href="Modding_Content_packs#Conventions" class="wikilink"
title="conventional acronym used in the folder name">conventional
acronym used in the folder name</a> for mods that do not use Content
Patcher.)</small>.

### Core (1000+ content packs)

<table>
<thead>
<tr>
<th><p>mod</p></th>
<th><p>is CP extension</p></th>
<th><p>functionality</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><small>(AT)</small></p></td>
<td><p>no</p></td>
<td><p>Enables texture variation for placeable objects, buildings and
entities. This includes trees, animals, pets, farm buildings, plants,
and more.</p></td>
</tr>
<tr>
<td><p><small>(FS)</small></p></td>
<td><p>no</p></td>
<td><p>Allows for bigger accessories, hairstyles, hats, shirts, sleeves
and pants, as well as animation support and more.</p></td>
</tr>
<tr>
<td><p><small>(JA)</small></p></td>
<td><p>no</p></td>
<td><p>Create specific item types, with support for functionality
specific to each item type (<em>e.g.,</em> specifying
crafting/cooking/recipes or gift tastes for new items). It currently
supports creating objects, big craftables, crops, fruit trees, hats,
weapons, shirts, pants, and boots. Content and images added by Json
Assets can also be edited through Content Patcher.</p>
<p>See for documentation.</p>
<p><strong>Note</strong>: 1.6 adds the ability to add new items natively
via CP, which should be the preferred method.</p></td>
</tr>
</tbody>
</table>

### Popular (400+)

<table>
<thead>
<tr>
<th><p>mod</p></th>
<th><p>is CP extension</p></th>
<th><p>functionality</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><small>(FTM)</small></p></td>
<td><p>no</p></td>
<td><p>Add farm-like spawning logic to any map. That includes spawning
stumps, debris, forage, meteors, monsters, ores, etc.</p></td>
</tr>
<tr>
<td><p><small>(PFM)</small></p></td>
<td><p>no</p></td>
<td><p>Add/change the inputs/outputs/behaviour of any machine in the
game. That includes vanilla machines (<em>e.g.,</em> <a href="Keg"
class="wikilink" title="keg">keg</a>), machines added by other mods, and
adding machine logic to any big craftable. <strong>Note</strong>: 1.6
adds the ability to add new machine rules natively via CP, which should
be the preferred method. PFM still provides several additional features
not found in the base game (though most of them are covered by Extra
Machine Config, an addon framework on top of CP).</p></td>
</tr>
<tr>
<td></td>
<td><p>yes</p></td>
<td><p>A framework providing many features to content pack authors.
Features include:</p>
<ul>
<li>Crafting/cooking recipes that can take ingredients based on context
tags</li>
<li>Extra item data, such as buffs on consumption</li>
<li>Extra trigger actions, map actions and game state queries</li>
<li>Extra yields on crop harvest</li>
<li>Animated textures</li>
<li>Custom spawnables and procedurally generated dungeons.</li>
</ul></td>
</tr>
</tbody>
</table>

### Common (100+)

<table>
<thead>
<tr>
<th><p>mod</p></th>
<th><p>is CP extension</p></th>
<th><p>functionality</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><small>(BAGI)</small></p></td>
<td><p>no</p></td>
<td><p>Add custom icons to artisanal items like <a href="honey"
class="wikilink" title="honey">honey</a> or <a href="wine"
class="wikilink" title="wine">wine</a> based on the item or flower used
to make them.</p>
<p><strong>Note</strong>: The original Nexus version is not updated for
1.6. Use if you want to make 1.6 content packs.</p></td>
</tr>
<tr>
<td><p><small>(FF)</small></p></td>
<td><p>no</p></td>
<td><p>A Framework to make "Furniture Packs" with much more freedom that
what a simple Content Pack allows: with it you can define seats, table
slots, layers, shops, and much more.</p></td>
</tr>
<tr>
<td><p><small>(MFM)</small></p></td>
<td><p>no</p></td>
<td><p>Add new mail with functionality like custom backgrounds,
repeating mail, a wider variety of mail attachments, and support for
multiple attachments. <strong>Note</strong>: 1.6 adds the ability to add
new mail natively via CP, which should be the preferred method. MFM
still provides several additional features not found in the base game
(such as attaching items with higher quality to mail).</p></td>
</tr>
</tbody>
</table>

### Specialized frameworks

These have fewer than 100 content packs, but provide useful
functionality for specific cases.

#### Items

These mods add new functionalities to items, including machines,
furniture, and tools.

| mod | is CP extension | functionality |
|----|----|----|
| <small>(AMF)</small> | no | A framework for creating custom special attacks and enchantments for individual weapons and weapon types. |
| <small>(BC)</small> | yes/no | Create custom recipes more advanced than those supported by the base game including support for controlling availability and ingredients via <a href="Modding_Game_state_queries" class="wikilink"
title="game state queries">game state queries</a>, running <a href="Modding_Trigger_actions" class="wikilink"
title="trigger actions">trigger actions</a> when a player crafts the recipe, and multiple possible ingredients or outputs using <a href="Modding_Item_queries" class="wikilink"
title="item queries and spawn fields">item queries and spawn fields</a>. Create custom crafting stations with a limited selection of recipes, which can optionally be excluded from other crafting menus. These crafting stations can be opened via map tile actions or trigger actions. Allows assigning map tile actions to big craftables, which allows using them with the custom crafting stations feature. |
|  | yes | A core mod providing various useful features. Current feature include custom offset for items displayed on furniture, Custom actions when interacting with furniture, custom item category names, and NPC swimming as part of their schedules. |
|  | yes | Extend crafting recipes to allow crafting furniture, weapons, tools, and anything else. |
|  | yes | Allows custom bushes to be added to the game which work like the tea sapling. |
| <small>(CCS)</small> | no | Add customized crafting stations which opens menus with a limited selection of recipes, without those recipes cluttering up the vanilla crafting menus. The stations can be [big craftables](https://stardewvalleywiki.com/Modding:Big_craftables_data) that are vanilla or added using Json Assets (JA). The stations can also be added via tiledata added to the map. **Note**: This mod is in maintenance mode for 1.6 - Using Better Crafting might be a better idea. |
|  | yes | Adds custom storages (chests, cabinets, etc.) that support capacity at vanilla levels and beyond. |
|  | yes | Adds extra functionalities to machine input/output rules, such as additional fuels/byproducts for specific recipes or copying color and flavor of input to the output. |
|  | yes | Allows furniture items to accept machine rules, notable input-output rules. Essentially allows machine dimensions bigger than 1x2. |
|  | yes | Adds a way for authors to apply a real glow effect to food buffs. |
|  | yes | Gives modders the ability to create custom resources, custom mixed seeds, and interactions between objects in-menu. (1.6) |
|  | yes | Adds the ability to define big craftables that can be placed on trees and water, as well as aquatic crops. |
|  | yes | Framework to allow mod authors to specify a texture color override, including Prismatic and custom prismatic palettes, to their content using custom fields in Content Patcher. Currently supported: farm animals, objects, big craftables, and boots. |
|  | yes | A framework mod for adding custom Secret Notes to the game. Includes the ability to specify complex eligibility conditions or specific locations, use a different item for the note object, specify custom content and formatting (including images and text, or both), and set any trigger actions to be run when a note is first read. |
|  | yes | Framework for making custom trinkets with special abilities and trinket companions via content patcher. Also allows trinkets to be summoned without requiring the slot via <a href="Modding_Trigger_actions" class="wikilink"
title="trigger actions">trigger actions</a>. |

#### Maps and locations

These mods add new functionalities to maps and locations, including
extra tile actions and properties.

| mod | is CP extension | functionality |
|----|----|----|
|  | yes | Allows map makers to add pre-built buildings to their maps and conditionally add/upgrade buildings. |
| <small>(BBM)<small> | yes/no | Allows creating custom bush blooming schedules to support whatever seasons, days, locations, and items you may want. |
|  | yes | Allows custom builder NPCs that can construct buildings like Robin, with either their own list of buildings or shared with Robin. |
|  | yes | Make new locations accessible through <a href="Bus_Stop" class="wikilink" title="bus">bus</a>, <a href="Railroad" class="wikilink" title="train">train</a>, or <a href="Boat" class="wikilink" title="boat">boat</a>, so you don't need to patch paths/warps into existing maps. Has backwards compatibility for and , and adds a new location with randomized tourist/shops which can be populated further by other mods. |
| <small>(CC)</small> | no | Add custom critters to the world, like butterflies and bees. |
| <small>(CFL)</small> | no | A simplified way of adding custom farms. Supports among other things spawning items/wild crops/resource clumps/beach drops and setting fishing rules within your farms context. **Note**: 1.6 adds the ability to add new farm types natively via CP, which should be the preferred method. CFL still provides several additional features not found in the base game. |
|  | yes | Adds miscellaneous new features for other mods to use. Current features include bed placement and kitchens/minifridges outside of a farmhouse, more Content Patcher Tokens, custom Special Order boards, destroyable bushes, multiple fishing zones, change water color. |
|  | yes | Allow map authors to spice up their maps with the new custom tile properties and extra features. Features including spawning fake NPCs, closeup interactions, opening a letter and more. |
|  | yes | Add features for locations, buildings, and furniture. Includes tile data lights on map/building/furniture, various map wide visual effects, simple critter spawning, some fixes for custom farmhouse mods, extended building draw layer definition that also works on furniture, and more. |
|  | yes | Adds new personal FarmHouse rooms. Modders can add room designs. |
| <small>(SF)</small> | yes/no | A framework for adding custom buildings to the game. **Note**: 1.6 adds the ability to add new buildings natively via CP, which should be the preferred method. SF still supports several features not present in the base game, including custom light sources on building exteriors and auxiliary human door. |
|  | yes | Enables custom bundle creation and allow items to be registered as wallet currency. |

#### Miscellaneous

These mods extend game functionality in other ways, or provide
under-the-hood utilities for modders to use.

<table>
<thead>
<tr>
<th><p>mod</p></th>
<th><p>is CP extension</p></th>
<th><p>functionality</p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td><p>yes</p></td>
<td><p>Adds several extra triggers, actions, and game state queries for
Content Patcher mod authors to utilize. See <a
href="https://stardew.button.gay/docs/betas">the documentation</a> for a
full list and instructions.</p></td>
</tr>
<tr>
<td></td>
<td><p>yes</p></td>
<td><p>A framework for adding custom weather types to the game, with
distinct visual and auditory styles. Includes a variety of trigger
actions to simulate weather effects, both beneficial and
harmful.</p></td>
</tr>
<tr>
<td><p><small>(CP-A)</small></p></td>
<td><p>yes/no</p></td>
<td><p>Animate any texture loaded through Content Patcher, including for
textures that can't normally be animated (<em>e.g.,</em> item
sprites).</p>
<p><strong>Note</strong>: It's recommended that you use SpaceCore's
animation feature instead.</p></td>
</tr>
<tr>
<td></td>
<td><p>yes</p></td>
<td><p>Adds some special, custom Content Patcher tokens that lets mods
access the config values, translations, and dynamic tokens from other
mods, including mods that are not made for Content Patcher
specifically.</p></td>
</tr>
<tr>
<td><p><small>(CC)</small></p></td>
<td><p>no</p></td>
<td><p>Allows creating custom entities that can be spawned on maps or
follow the player around. This includes animals in the world or
wandering NPCs.</p></td>
</tr>
<tr>
<td></td>
<td><p>yes</p></td>
<td><p>Extends farm animal data with additional features, such as
multiple harvest types, food other than hay, and multiple choices for
hatching/births.</p></td>
</tr>
<tr>
<td></td>
<td><p>yes</p></td>
<td><p>Revamps the farm animal purchase menu, and adds ways for mod to
create custom animal shops.</p></td>
</tr>
<tr>
<td></td>
<td><p>yes</p></td>
<td><p>Adds custom night-time events, using either configurable pre-made
events, or by making your own with <a href="Modding_Event_data"
class="wikilink" title="event scripting">event scripting</a>.</p></td>
</tr>
<tr>
<td><p><small>(NiTV)</small></p></td>
<td><p>yes/no</p></td>
<td><p>Framework for making catchable animals, creatures, critters and
beasts with varying behaviors and temperaments. Creatures can either
passively spawn according to conditions such as GSQs, or be spawned
actively using <a href="Modding_Trigger_actions" class="wikilink"
title="trigger actions">trigger actions</a>.</p></td>
</tr>
<tr>
<td></td>
<td><p>yes</p></td>
<td><p>A categorized special items &amp; powers tab. For mod authors
working with powers and books, this mod provides the ability to
add/specify tabs for their custom powers, change the "book read" message
for custom books, add books that grant recipes, and extra Game State
Queries, trigger actions and CP tokens.</p></td>
</tr>
</tbody>
</table>

## See also

- <a href="Modding_Index" class="wikilink"
  title="Modding:Index">Modding:Index</a> for different ways to create
  mods, and more detailed documentation.
- [Tutorial: Making Framework
  Mods](https://stardewmodding.wiki.gg/wiki/Tutorial:_Making_Framework_Mods)
  for an external tutorial collecting various instructions and tips on
  making new framework mods.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="pt_Modificações_Frameworks_de_pacotes_de_conteúdo"
class="wikilink"
title="pt:Modificações:Frameworks de pacotes de conteúdo">pt:Modificações:Frameworks
de pacotes de conteúdo</a>
<a href="ru_Модификации_Контент-паки_и_фреймворки" class="wikilink"
title="ru:Модификации:Контент-паки и фреймворки">ru:Модификации:Контент-паки
и фреймворки</a>
<a href="tr_Modlama_İçerik_Paketi_Framework&#39;leri" class="wikilink"
title="tr:Modlama:İçerik Paketi Framework&#39;leri">tr:Modlama:İçerik
Paketi Framework'leri</a>
