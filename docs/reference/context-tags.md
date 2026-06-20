---
title: "Context Tags"
wiki_source: "Modding:Context tags"
permalink: /Modding:Context_tags/
category: reference
tags: [context-tags, format, list-of-context-tags, added-automatically, colors, item-behavior, machine-processing, informational]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains *context tags*, arbitrary data label attached to
items. These can produce various effects in-game, or may be
informational only.

## Format

Context tags generally contain only alphanumeric, underscore, and
parentheses characters like `category_gem` or `item_apple`. They're
usually case-insensitive, but custom tags should be lowercase to be
safe.

Many context tags are generated automatically based on the item data
(like the item quality), and others are defined in an asset like
`Data/Objects`.

## List of context tags

Here's an *incomplete* list of context tags added or used in the base
game. Mods can add custom context tags, which aren't listed here.

### Added automatically

These are added for all items:

<table>
<thead>
<tr>
<th><p>context tag</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>category_&lt;category&gt;</samp></p></td>
<td><p>Added automatically based on the item category. See the 'context
tag' column in the <a href="Modding_Items#Categories" class="wikilink"
title="item category list">item category list</a> for possible
values.</p></td>
</tr>
<tr>
<td><p><samp>fish_&lt;metadata&gt;</samp></p></td>
<td><p>Added automatically for a fish item based on <a
href="Modding_Fish_data" class="wikilink"
title="its metadata in Data/Fish">its metadata in
<samp>Data/Fish</samp></a>.</p>
<p>For <a href="Crab_Pot" class="wikilink" title="crab pot">crab pot</a>
fish (<em>i.e.</em> those with type <samp>trap</samp>):</p>
<table>
<thead>
<tr>
<th><p>context tag</p></th>
<th><p>notes</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>fish_trap_location_&lt;water type&gt;</samp></p></td>
<td><p>Based on field 4 ('location'). For example,
<samp>fish_trap_location_ocean</samp>.</p></td>
</tr>
</tbody>
</table>
<p>For fishing rod fish (<em>i.e.</em> those whose type is <em>not</em>
<samp>trap</samp>):</p>
<table>
<thead>
<tr>
<th><p>context tag</p></th>
<th><p>notes</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>fish_difficulty_&lt;difficulty&gt;</samp></p></td>
<td><p>Based on field 1 ('chance to dart'), where &lt;difficulty&gt; is
one of <samp>easy</samp> (0–33), <samp>medium</samp> (34–66),
<samp>hard</samp> (67–100), or <samp>extremely_hard</samp> (101+). For
example, <samp>fish_difficulty_hard</samp>.</p></td>
</tr>
<tr>
<td><p><samp>fish_motion_&lt;motion&gt;</samp></p></td>
<td><p>Based on field 2 ('darting randomness'). For example,
<samp>fish_motion_floater</samp>.</p></td>
</tr>
<tr>
<td><p><samp>fish_favor_weather_&lt;weather&gt;</samp></p></td>
<td><p>Based on field 7 ('weather'). For example,
<samp>fish_favor_weather_sunny</samp>.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>id_&lt;type&gt;_&lt;identifier&gt;</samp></p></td>
<td><p>Added automatically as an alternative ID. The &lt;type&gt; is one
of <samp>B</samp> (boots), <samp>BBL</samp> (big craftable recipe),
<samp>BL</samp> (object recipe), <samp>BO</samp> (big craftable),
<samp>C</samp> (clothing), <samp>F</samp> (furniture), <samp>H</samp>
(hat), <samp>O</samp> (object), <samp>R</samp> (ring), <samp>W</samp>
(melee weapon), else blank. The &lt;identifier&gt; is the item's parent
sheet index. For example, <a href="pufferfish" class="wikilink"
title="pufferfish">pufferfish</a> has value <samp>id_o_128</samp>
(object #128).</p></td>
</tr>
<tr>
<td><p><samp>item_&lt;name&gt;</samp></p></td>
<td><p>Added automatically based on the item name. The name is trimmed,
lowercase, with spaces replaced with underscores, and with single quotes
removed. For example, <a href="&#39;1000_Years_From_Now&#39;"
class="wikilink" title="&#39;1000 Years From Now&#39;">'1000 Years From
Now'</a> has context tag <samp>item_1000_years_from_now</samp>.</p></td>
</tr>
</tbody>
</table>

These are added for <a href="Modding_Objects" class="wikilink"
title="object-type">object-type</a> items:

<table>
<thead>
<tr>
<th><p>context tag</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>item_type_&lt;type&gt;</samp></p></td>
<td><p>Added automatically based on the <samp>Type</samp> field in
<samp>Data/Objects</samp>. The tag is checked in a few places
(<em>e.g.</em> the <a href="museum" class="wikilink"
title="museum">museum</a> to check if an item is an artifact or
mineral).</p></td>
</tr>
<tr>
<td><p><samp>jelly_item</samp><br />
<samp>juice_item</samp><br />
<samp>pickle_item</samp><br />
<samp>wine_item</samp></p></td>
<td><p>For items produced by the <a href="keg" class="wikilink"
title="keg">keg</a> or <a href="Preserves_Jar" class="wikilink"
title="preserves jar">preserves jar</a>, the preserved item
type.</p></td>
</tr>
<tr>
<td><p><samp>preserve_sheet_index_&lt;id&gt;</samp></p></td>
<td><p>For items produced by the <a href="keg" class="wikilink"
title="keg">keg</a> or <a href="Preserves_Jar" class="wikilink"
title="preserves jar">preserves jar</a>, the parent sheet index for the
original item that was produced. For example, blueberry <a href="wine"
class="wikilink" title="wine">wine</a> has
<samp>preserve_sheet_index_258</samp>, where 258 is the <a
href="blueberry" class="wikilink" title="blueberry">blueberry</a> item's
index.</p></td>
</tr>
<tr>
<td><p><samp>quality_none</samp><br />
<samp>quality_silver</samp><br />
<samp>quality_gold</samp><br />
<samp>quality_iridium</samp></p></td>
<td><p>Added automatically based on the item quality.</p></td>
</tr>
<tr>
<td><p><samp>quality_qi</samp></p></td>
<td><p>Added automatically for items cooked while the <a href="Quests"
class="wikilink" title="Qi&#39;s Cuisine special order"><em>Qi's
Cuisine</em> special order</a> is active.</p></td>
</tr>
</tbody>
</table>

### Colors

`color_*` tags are used by a number of game functions, including when
the player
<a href="Dyeing#Dye_Pots" class="wikilink" title="dyes clothing">dyes
clothing</a> at <a href="2_Willow_Lane" class="wikilink"
title="Emily&#39;s house">Emily's house</a>, when tinting certain
machine products such as
<a href="Wine" class="wikilink" title="Wine">Wine</a> and
<a href="Pickles" class="wikilink" title="Pickles">Pickles</a>, and when
displaying the <a href="Books" class="wikilink" title="Book">Book</a>
reading animation. For tinting purposes, each tag has a specific RGB
value that is used, except when using Emily's Dye Pots, in which case
they are grouped into one of the following categories.

| dye pot | context tags |
|----|----|
| red | `color_red`, `color_salmon`, `color_dark_red`, `color_pink` |
| orange | `color_orange`, `color_dark_orange`, `color_dark_brown`, `color_brown`, `color_copper` |
| yellow | `color_yellow`, `color_dark_yellow`, `color_gold`, `color_sand` |
| green | `color_green`, `color_dark_green`, `color_lime`, `color_yellow_green`, `color_jade`, `color_sea_green` |
| blue | `color_blue`, `color_dark_blue`, `color_dark_cyan`, `color_light_cyan`, `color_cyan`, `color_aquamarine` |
| purple | `color_purple`, `color_dark_purple`, `color_dark_pink`, `color_pale_violet_red`, `color_poppyseed`, `color_iridium` |
| no color | `color_black`, `color_gray`, `color_dark_gray`, `color_white`, `color_iron`, `color_prismatic` |

### Item behavior

<table>
<thead>
<tr>
<th><p>context tag</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>campfire_item</samp></p></td>
<td><p>Marks the item as a <a href="campfire" class="wikilink"
title="campfire">campfire</a>. If the item also has the
<samp>torch_item</samp> context tag, when it's placed in the world and
turned on...</p>
<ul>
<li>Campfire flames are drawn over it;</li>
<li>If the item is <a href="Modding_Big_craftables" class="wikilink"
title="big craftable">big craftable</a>, light is emitted from its
center instead of the top.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>crow_scare</samp></p></td>
<td><p>Whether this item acts as a <a href="scarecrow" class="wikilink"
title="scarecrow">scarecrow</a>. Only applies to <a
href="Modding_Big_craftables" class="wikilink"
title="big craftables">big craftables</a>.</p></td>
</tr>
<tr>
<td><p><samp>crow_scare_radius_&lt;radius&gt;</samp></p></td>
<td><p>If this item is a scarecrow, the circular radius it covers. If
the scarecrow doesn't have this context tag, its radius defaults to 17
if its internal name begins with <samp>Deluxe</samp> else 9.</p></td>
</tr>
<tr>
<td><p><samp>museum_donatable</samp><br />
<samp>not_museum_donatable</samp></p></td>
<td><p>Set whether the item can be donated to the <a href="museum"
class="wikilink" title="museum">museum</a>, overriding the vanilla
logic.</p></td>
</tr>
<tr>
<td><p><samp>not_giftable</samp></p></td>
<td><p>Prevents players from gifting this item to NPCs, who'll ignore
the item entirely (e.g. as if you were holding a tool).</p>
<p>This only affects gift-giving, it doesn't affect non-gift logic like
quest goals or special order objectives. If the NPC also has a
<samp>reject_*</samp> dialogue for the item, the dialogue takes
priority.</p></td>
</tr>
<tr>
<td><p><samp>not_placeable</samp><br />
<samp>placeable</samp></p></td>
<td><p>Sets whether the item can be placed on the ground.</p></td>
</tr>
<tr>
<td><p><samp>prevent_loss_on_death</samp></p></td>
<td><p>Indicates the item can't be <a
href="Adventurer&#39;s_Guild#Item_Recovery_Service" class="wikilink"
title="lost when the player dies">lost when the player
dies</a>.</p></td>
</tr>
<tr>
<td><p><samp>propose_roommate_&lt;NPC name&gt;</samp></p></td>
<td><p>Triggers a roommate proposal when given to the named NPC. The NPC
name must be lowercase with underscores instead of spaces (e.g.,
<samp>propose_roommate_dwarf</samp>).</p></td>
</tr>
<tr>
<td><p><samp>sign_item</samp></p></td>
<td><p>Marks the item as a <a href="Crafting#Signs" class="wikilink"
title="sign">sign</a>, which lets player display items on it or place it
on a <a href="Fish_Pond" class="wikilink" title="fish pond">fish
pond</a> to show the fish count.</p></td>
</tr>
<tr>
<td><p><samp>torch_item</samp></p></td>
<td><p>Marks the item as a <a href="torch" class="wikilink"
title="torch">torch</a>, which lets the player turn it on/off to emit
light. See also <samp>campfire_item</samp>.</p></td>
</tr>
</tbody>
</table>

### Machine processing

<table>
<thead>
<tr>
<th><p>context tag</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>crystalarium_banned</samp></p></td>
<td><p>When applied to a gem or mineral item, prevents players from
placing it in a <a href="crystalarium" class="wikilink"
title="crystalarium">crystalarium</a>.</p></td>
</tr>
<tr>
<td><p><samp>fish_pond_ignore</samp></p></td>
<td><p>Prevents players from adding this fish to <a href="Fish_Pond"
class="wikilink" title="fish ponds">fish ponds</a>, even if it would
otherwise match an entry in <samp>Data/FishPondData</samp>.</p></td>
</tr>
<tr>
<td><p><samp>geode_crusher_ignored</samp></p></td>
<td><p>Prevents breaking this item open in a <a href="Geode_Crusher"
class="wikilink" title="geode crusher">geode crusher</a>, even if the
item has geode fields in <a href="Modding_Objects" class="wikilink"
title="Data/Objects"><samp>Data/Objects</samp></a>.</p></td>
</tr>
<tr>
<td><p><samp>keg_juice</samp><br />
<samp>keg_wine</samp></p></td>
<td><p>Allows processing the item in a <a href="keg" class="wikilink"
title="keg">keg</a> to produce a juice or wine variant.</p></td>
</tr>
<tr>
<td><p><samp>preserves_jelly</samp><br />
<samp>preserves_pickle</samp></p></td>
<td><p>Allows processing the item in a <a href="Preserves_Jar"
class="wikilink" title="preserves jar">preserves jar</a> to produce a
jelly or pickled variant.</p></td>
</tr>
<tr>
<td><p><samp>seedmaker_banned</samp></p></td>
<td><p>When applied to a seed item, prevents players from placing it in
a <a href="Seed_Maker" class="wikilink" title="seed maker">seed
maker</a>.</p></td>
</tr>
<tr>
<td><p><samp>tapper_item</samp></p></td>
<td><p>Marks the item as a <a href="tapper" class="wikilink"
title="tapper">tapper</a> or <a href="Heavy_Tapper" class="wikilink"
title="heavy tapper">heavy tapper</a>.</p></td>
</tr>
<tr>
<td><p><samp>tapper_multiplier_&lt;multiplier&gt;</samp></p></td>
<td><p>The multiplier applied to the tapper production speed. For
example, <samp>2</samp> will make items take half their base time
(<em>i.e.</em> each item will finish in <sup>base time</sup>/<sub>speed
multiplier</sub>). Defaults to 1 if omitted.</p></td>
</tr>
</tbody>
</table>

### Informational

These tags have no effect on the game logic, they just provide metadata
about the item.

<table>
<thead>
<tr>
<th><p>context tag</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>fish_legendary</samp><br />
<samp>fish_legendary_family</samp></p></td>
<td><p>Marks the fish as a <a href="Fish#Legendary_Fish"
class="wikilink" title="legendary fish">legendary fish</a> or <a
href="Quests#Extended_Family" class="wikilink"
title="legendary fish family">legendary fish family</a>. These are
purely informational; the legendary fish behavior is determined by data
fields like <samp>CatchLimit</samp> or <samp>IsBossFish</samp> in <a
href="Modding_Location_data" class="wikilink"
title="Data/Locations"><samp>Data/Locations</samp></a>.</p></td>
</tr>
<tr>
<td><p><samp>geode</samp></p></td>
<td><p><em>(Added automatically)</em> Marks the item as a <a
href="Minerals#Geodes" class="wikilink" title="geode">geode</a> item,
which can be broken open at <a href="Blacksmith" class="wikilink"
title="Clint&#39;s blacksmith shop">Clint's blacksmith shop</a> or using
a <a href="Geode_Crusher" class="wikilink" title="geode crusher">geode
crusher</a>. This is added automatically if the geode fields are present
in <a href="Modding_Objects" class="wikilink"
title="Data/Objects"><samp>Data/Objects</samp></a>.</p></td>
</tr>
<tr>
<td><p><samp>id_&lt;item id&gt;</samp></p></td>
<td><p><em>(Added automatically)</em> The <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified item ID">qualified item ID</a>, like
<samp>id_(o)128</samp>. This can be used to match or exclude an item by
ID using context tags. Any spaces in the ID are replaced with
underscores, and single quotes are removed.</p></td>
</tr>
<tr>
<td><p><samp>is_machine</samp></p></td>
<td><p><em>(Added automatically)</em> Indicates the item has <a
href="Modding_Machines" class="wikilink" title="machine logic">machine
logic</a>. This is added automatically based on
<samp>Data/Machines</samp>.</p></td>
</tr>
<tr>
<td><p><samp>machine_input</samp></p></td>
<td><p><em>(Added automatically)</em> Whether the item is a machine
which accepts items from the player. This is added automatically based
on the machine's fields in <samp>Data/Machines</samp>:</p>
<ul>
<li>if <samp>HasInput</samp> is true;</li>
<li><em>or</em> if any output rules have an
<samp>ItemPlacedInMachine</samp> trigger.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>machine_output</samp></p></td>
<td><p><em>(Added automatically)</em> Whether the item is a machine
which produces items for the player to collect. This is added
automatically based on the machine's fields in
<samp>Data/Machines</samp>:</p>
<ul>
<li>if <samp>HasOutput</samp> is true;</li>
<li><em>or</em> if it has any output rules.</li>
</ul></td>
</tr>
</tbody>
</table>

### Others

The `debug listtags` <a href="Modding_Console_commands" class="wikilink"
title="console command">console command</a> lists all the tags of the
item being held.

## Usage in data

Some game data references context tags in a generic way. For example,
you can add custom tags to an item, then reference them in the fish pond
data.

For example:

| game data | effects |
|----|----|
| <a href="Modding_Fish_ponds" class="wikilink" title="fish ponds">fish
ponds</a> | In `Data/FishPondData`, used to match fish that can be placed in the pond (see <a href="Modding_Fish_ponds#RequiredTags" class="wikilink"
title="RequiredTags in the fish pond data"><samp>RequiredTags</samp> in
the fish pond data</a>). |
| <a href="Modding_Special_orders" class="wikilink"
title="special orders">special orders</a> | In `Data/SpecialOrders`, used to match items that meet the quest objectives (see <a href="Modding_Special_orders#Context_tags" class="wikilink"
title="AcceptedContextTags in the special order data"><samp>AcceptedContextTags</samp>
in the special order data</a>). |
| tailoring | In `Data/TailoringRecipes`, used to match items that are needed for a recipe. |
| <a href="Modding_Gift_taste_data" class="wikilink"
title="gift tastes">gift tastes</a> | In `Data/NPCGiftTastes`, used to set character likes and dislike for every item using the context tag. |

## For C# mods

### ItemContextTagManager class

For C# mods, the `ItemContextTagManager` class simplifies working with
item context tags and reduces repeated code.

This provides a few utility methods:

<table>
<thead>
<tr>
<th><p>method</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>GetBaseContextTags(id)</code></p></td>
<td><p>Get the base context tags for an item based on its raw data in
<samp>Data/Objects</samp> or <samp>Data/BigCraftables</samp>. This
doesn't include dynamic tags added that are based on instance info (like
quality), which you can get using
<code>item.GetContextTags()</code>.</p></td>
</tr>
<tr>
<td><p><code>DoesTagQueryMatch(query, tags)</code></p></td>
<td><p>Get whether a context tag query matches the given tags. For
example,
<code>ItemContextTagManager.DoesTagQueryMatch("bone_item, !fossil_item", item.GetContextTags())</code>
returns true if the item is a bone item but not a fossil (like the <a
href="Bone_Flute" class="wikilink" title="Bone Flute">Bone
Flute</a>).</p></td>
</tr>
<tr>
<td><p><code>DoAllTagsMatch(requiredTags, actualTags)</code><br />
<code>DoAnyTagsMatch(requiredTags, actualTags)</code></p></td>
<td><p>Get whether every (<samp>DoAllTagsMatch</samp>) or at least one
(<samp>DoAnyTagsMatch&lt;/samp) required tag matches the actual item
tags. This supports negated required tags like
&lt;samp&gt;"!fossil_item"</samp> too.</p></td>
</tr>
<tr>
<td><p><code>DoesTagMatch(requiredTag, actualTags)</code></p></td>
<td><p>Get whether a single tag matches the actual item tags. This
supports negated required tags like <samp>"!fossil_item"</samp>
too.</p></td>
</tr>
<tr>
<td><p><code>SanitizeContextTag(tag)</code></p></td>
<td><p><em>(Specialized)</em> Replace characters that may appear in item
names so they're valid in context tags. For example,
<code>SanitizeContextTag("Sam's Boombox")</code> returns
<samp>sams_boombox</samp>.</p></td>
</tr>
</tbody>
</table>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="zh_模组_上下文标签" class="wikilink"
title="zh:模组:上下文标签">zh:模组:上下文标签</a>
