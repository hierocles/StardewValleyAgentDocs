---
title: "Crops"
wiki_source: "Modding:Crop data"
permalink: /Modding:Crop_data/
category: items
tags: [crop-data, raw-data, format, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses crops data. This is an
advanced guide for mod developers.

## Raw data

Crop data is stored in `Data\Crops.xnb`, which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's a portion
of the raw data as of for reference:

## Format

The asset `Data\Crops` consists of a string → model lookup, where...

- The key is the unqualified
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="item ID">item ID</a> for the seed item.
- The value is model with the fields listed below.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Growth</p></td>
</tr>
<tr>
<td><p><samp>Seasons</samp></p></td>
<td><p>The seasons in which this crop can grow (any combination of
<samp>spring</samp>, <samp>summer</samp>, <samp>fall</samp>, and
<samp>winter</samp>).</p></td>
</tr>
<tr>
<td><p><samp>DaysInPhase</samp></p></td>
<td><p>The number of days in each visual step of growth before the crop
is harvestable. Each step corresponds to a sprite in the crop's row (see
<samp>SpriteIndex</samp>).</p>
<p>For example, a crop with <code>"DaysInPhase": [ 1, 1, 1, 1 ]</code>
will grow from seed to harvestable in 4 days, moving to the next sprite
in the row each day.</p></td>
</tr>
<tr>
<td><p><samp>RegrowDays</samp></p></td>
<td><p><em>(Optional)</em> The number of days before the crop regrows
after harvesting, or -1 if it can't regrow. The crop will keep the
full-grown sprite (i.e. the last phase in <samp>DaysInPhase</samp>)
during this time. Default -1.</p></td>
</tr>
<tr>
<td><p><samp>IsRaised</samp></p></td>
<td><p><em>(Optional)</em> Whether this is a raised crop on a trellis
that can't be walked through. Default false.</p></td>
</tr>
<tr>
<td><p><samp>IsPaddyCrop</samp></p></td>
<td><p><em>(Optional)</em> Whether this crop can be planted near water
for a unique paddy dirt texture, faster growth time, and auto-watering.
For example, <a href="Rice_Shoot" class="wikilink" title="rice">rice</a>
and <a href="Taro_Root" class="wikilink" title="taro">taro</a> are paddy
crops. Default false.</p></td>
</tr>
<tr>
<td><p><samp>NeedsWatering</samp></p></td>
<td><p><em>(Optional)</em> Whether this crop needs to be watered to grow
(e.g. <a href="Fiber_Seeds" class="wikilink" title="fiber seeds">fiber
seeds</a> don't). Default true.</p></td>
</tr>
<tr>
<td colspan="2"><p>Harvest</p></td>
</tr>
<tr>
<td><p><samp>HarvestItemId</samp></p></td>
<td><p>The item ID produced when this crop is harvested.</p></td>
</tr>
<tr>
<td><p><samp>HarvestMethod</samp></p></td>
<td><p><em>(Optional)</em> How the crop can be harvested. This can be
<samp>Grab</samp> (crop is harvested by hand) or <samp>Scythe</samp>
(harvested with a <a href="scythe" class="wikilink"
title="scythe">scythe</a>). Default <samp>Grab</samp>.</p></td>
</tr>
<tr>
<td><p><samp>HarvestMinStack</samp><br />
<samp>HarvestMaxStack</samp></p></td>
<td><p><em>(Optional)</em> The minimum and maximum number of
<samp>HarvestItemId</samp> to produce (before
<samp>HarvestMaxIncreasePerFarmingLevel</samp> and
<samp>ExtraHarvestChance</samp> are applied). A value within this range
(inclusive) will be randomly chosen each time the crop is harvested. The
minimum defaults to 1, and the maximum defaults to the minimum.</p></td>
</tr>
<tr>
<td><p><samp>HarvestMinQuality</samp><br />
<samp>HarvestMaxQuality</samp></p></td>
<td><p><em>(Optional)</em> If set, the minimum and maximum quality of
the harvest crop. These fields set a constraint that's applied after the
quality is calculated normally, they don't affect the initial quality
logic.</p></td>
</tr>
<tr>
<td><p><samp>HarvestMaxIncreasePerFarmingLevel</samp></p></td>
<td><p><em>(Optional)</em> The number of extra harvests to produce per
farming level. This is rounded down to the nearest integer and added to
<samp>HarvestMaxStack</samp>. Defaults to 0.</p>
<p>For example, a value of 0.2 is equivalent to +1 max at level 5 and +2
at level 10.</p></td>
</tr>
<tr>
<td><p><samp>ExtraHarvestChance</samp></p></td>
<td><p><em>(Optional)</em> The probability that harvesting the crop will
produce extra harvest items, as a value between 0 (never) and 0.9
(nearly always). This is repeatedly rolled until it fails, then the
number of successful rolls is added to the produced count. For example,
<a href="tomato" class="wikilink" title="tomato">tomatoes</a> use 0.05.
Default 0. This is <a
href="https://www.desmos.com/calculator/ok9c2tw6o5">a geometric series
with expected value</a> of <samp>1/(1-ExtraHarvestChance) - 1</samp>, so
it will grow faster than you expect it should. For example, with a value
of <samp>0.9</samp>, this field has an expected value of nine additional
crops.</p></td>
</tr>
<tr>
<td colspan="2"><p>Appearance</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture (under the game's
<samp>Content</samp> folder) containing the crop sprite. For example,
the vanilla crops use <samp>TileSheets\crops</samp>.</p></td>
</tr>
<tr>
<td><p><samp>SpriteIndex</samp></p></td>
<td><p><em>(Optional)</em> The index of this crop in the
<samp>Texture</samp>, one crop per row, where 0 is the top row. Default
0.</p></td>
</tr>
<tr>
<td><p><samp>TintColors</samp></p></td>
<td><p><em>(Optional)</em> The colors with which to tint the sprite when
drawn (e.g. for colored flowers). A random color from the list will be
chosen for each crop. See <a
href="Modding_Common_data_field_types#Color" class="wikilink"
title="color format">color format</a>. Default none.</p></td>
</tr>
<tr>
<td colspan="2"><p>Achievements</p></td>
</tr>
<tr>
<td><p><samp>CountForMonoculture</samp></p></td>
<td><p><em>(Optional)</em> Whether the player can ship 300 of this
crop's harvest item to unlock the monoculture <a href="achievements"
class="wikilink" title="achievement">achievement</a>. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>CountForPolyculture</samp></p></td>
<td><p><em>(Optional)</em> Whether the player must ship 15 of this
crop's harvest item (along with any other required crops) to unlock the
polyculture <a href="achievements" class="wikilink"
title="achievement">achievement</a>. Default false.</p></td>
</tr>
<tr>
<td colspan="2"><p>Advanced</p></td>
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
The possible values are <samp>Ground</samp> (planted directly in dirt),
<samp>GardenPot</samp> (planted in a <a href="Garden_Pot"
class="wikilink" title="garden pot">garden pot</a>), or
<samp>Any</samp>. Default <samp>Any</samp>.</p></td>
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
</tbody>
</table>

For example, this adds a custom cucumber crop (assuming you've already
added
<a href="Modding_Objects" class="wikilink" title="custom objects">custom
objects</a> for cucumber seeds and cucumber):

## See also

- <a href="Modding_Giant_crops" class="wikilink"
  title="Modding:Giant crops">Modding:Giant crops</a> for information
  about giant crops.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="fr_Modding_Données_des_récoltes" class="wikilink"
title="fr:Modding:Données des récoltes">fr:Modding:Données des
récoltes</a> <a href="ru_Модификации_Культуры" class="wikilink"
title="ru:Модификации:Культуры">ru:Модификации:Культуры</a>
<a href="zh_模组_农作物数据" class="wikilink"
title="zh:模组:农作物数据">zh:模组:农作物数据</a>
