---
title: "Fish"
wiki_source: "Modding:Fish data"
permalink: /Modding:Fish_data/
category: locations
tags: [fish-data, data-format, fish, aquarium-fish, spawning-fish, references]
---
← <a href="Modding_Index" class="wikilink"
title="Modding:Index">Modding:Index</a>

This page explains how the game stores and parses
<a href="fish" class="wikilink" title="fish">fish</a> data. This is an
advanced guide for mod developers.

## Data format

### Fish

You can edit fish data by editing the `Data/Fish` data asset.

This consists of a string → string lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  fish.
- The value is a slash-deliminated string with the fields listed below:

The value consists of two different formats: one for
<a href="Crab_pot" class="wikilink" title="crab pot">crab pot</a> fish
and one for fish that can be caught with the
<a href="Tools#Fishing_Poles" class="wikilink"
title="fishing rod">fishing rod</a>.

If the value of the field at index 1 is `trap`, the fish can only be
caught using a
<a href="Crab_Pot" class="wikilink" title="crab pot">crab pot</a>, and
it uses this format:

<table>
<thead>
<tr>
<th><p>index</p></th>
<th><p>syntax</p></th>
<th><p>example</p></th>
<th><p>content</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0</p></td>
<td><p>&lt;name&gt;</p></td>
<td><p><code>Lobster</code></p></td>
<td><p>The fish name.</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>&lt;type&gt;</p></td>
<td><p><code>trap</code></p></td>
<td><p>Must be <code>trap</code> to indicate a crab pot catch.</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>&lt;chance&gt;</p></td>
<td><p><code>.05</code></p></td>
<td><p>The percentage chance that this fish will be caught as a value
between 0 and 1. Only applies if a fish listed earlier in the file isn't
selected first.</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td></td>
<td><p><code>688 .45 689 .35 690 .35</code></p></td>
<td><p>Unused.</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>&lt;location&gt;</p></td>
<td><p><code>ocean</code></p></td>
<td><p>The type of water body where the fish can be caught. The vanilla
values are <code>freshwater</code> or <code>ocean</code>; mods may add
their own region.</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>&lt;min size&gt;</p></td>
<td><p><code>2</code></p></td>
<td rowspan="2"><p>The minimum and maximum size of the caught fish in
inches for fishing stats. In non-English languages, this is converted to
centimetres by multiplying by 2.54.</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>&lt;max size&gt;</p></td>
<td><p><code>20</code></p></td>
</tr>
</tbody>
</table>

Otherwise it's a fish that can be caught while fishing and uses this
format:

<table>
<thead>
<tr>
<th><p>index</p></th>
<th><p>syntax</p></th>
<th><p>example</p></th>
<th><p>content</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0</p></td>
<td><p>&lt;name&gt;</p></td>
<td><p><code>Pufferfish</code></p></td>
<td><p>The fish name.</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>&lt;chance to dart&gt;</p></td>
<td><p><code>80</code></p></td>
<td><p>How often the fish darts in the fishing minigame; between 15 (<a
href="carp" class="wikilink" title="carp">carp</a>) and 100 (<a
href="glacierfish" class="wikilink"
title="glacierfish">glacierfish</a>).</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>&lt;darting randomness&gt;</p></td>
<td><p><code>floater</code></p></td>
<td><p>How the bobber behaves during the fishing minigame; one of
<code>mixed</code>, <code>smooth</code>, <code>floater</code>,
<code>sinker</code>, or <code>dart</code>.</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>&lt;min size&gt;</p></td>
<td><p><code>1</code></p></td>
<td rowspan="2"><p>The minimum and maximum size of the caught fish in
inches for fishing stats. In non-English languages, this is converted to
centimetres by multiplying by 2.54.</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>&lt;max size&gt;</p></td>
<td><p><code>36</code></p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>[&lt;min time&gt; &lt;max time&gt;]+</p></td>
<td><p><code>1200 1600</code></p></td>
<td><p>The time of day when the fish can spawn. The min time is
inclusive, max time is exclusive. May specify multiple ranges.</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>[&lt;season&gt;]+</p></td>
<td><p><code>summer</code></p></td>
<td><p>Unused; seasons are taken from <samp>Data/Locations</samp>
instead.</p></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p>&lt;weather&gt;</p></td>
<td><p><code>sunny</code></p></td>
<td><p>The weather when the fish can spawn; one of <code>sunny</code>,
<code>rainy</code>, or <code>both</code>.</p></td>
</tr>
<tr>
<td><p>8</p></td>
<td><p>&lt;locations&gt;</p></td>
<td><p><code>690 .4 685 .1</code></p></td>
<td><p>Unused; locations are taken from <samp>Data/Locations</samp>
instead.</p></td>
</tr>
<tr>
<td><p>9</p></td>
<td><p>&lt;max depth&gt;</p></td>
<td><p><code>4</code></p></td>
<td><p>The minimum number of tiles from land that the player must cast
their rod such that the chance for catching this fish is not decreased.
If the player casts closer to land than this minimum, they will accrue a
penalty of <samp>(depth multiplier * chance)</samp> percentage points
for each tile below this minimum.<a href="#fn1" class="footnote-ref"
id="fnref1" role="doc-noteref"><sup>1</sup></a></p></td>
</tr>
<tr>
<td><p>10</p></td>
<td><p>&lt;chance&gt;</p></td>
<td><p><code>.3</code></p></td>
<td><p>The base chance for catching this fish once it has already been
determined as one of the possible fish to catch at a tile. After
applying buffs from <a href="Skills" class="wikilink"
title="fishing level">fishing level</a> and the <a href="Training_Rod"
class="wikilink" title="Training Rod">Training Rod</a>, this value is
clamped to <samp>0.9</samp> before applying other buffs such as from the
<a href="Curiosity_Lure" class="wikilink"
title="Curiosity Lure">Curiosity Lure</a> and <a href="Targeted_Bait"
class="wikilink" title="Targeted Bait">Targeted Bait</a>.<a href="#fn2"
class="footnote-ref" id="fnref2"
role="doc-noteref"><sup>2</sup></a></p></td>
</tr>
<tr>
<td><p>11</p></td>
<td><p>&lt;depth multiplier&gt;</p></td>
<td><p><code>.5</code></p></td>
<td><p>A multiplier used when penalizing the player for not casting
their rod at least <samp>max depth</samp> tiles from land.<a href="#fn3"
class="footnote-ref" id="fnref3"
role="doc-noteref"><sup>3</sup></a></p></td>
</tr>
<tr>
<td><p>12</p></td>
<td><p>&lt;fishing level&gt;</p></td>
<td><p><code>0</code></p></td>
<td><p>The minimum <a href="skills" class="wikilink"
title="fishing level">fishing level</a> needed for this fish to
appear.</p></td>
</tr>
<tr>
<td><p>13</p></td>
<td><p>&lt;first-catch tutorial eligible&gt;</p></td>
<td><p><code>true</code></p></td>
<td><p>Indicates whether the fish can be selected for the first-catch
tutorial.</p></td>
</tr>
</tbody>
</table>
<section id="footnotes" class="footnotes footnotes-end-of-document"
role="doc-endnotes">
<hr />
<ol>
<li id="fn1">See <samp>GameLocation::CheckGenericFishRequirements</samp>
in the game code<a href="#fnref1" class="footnote-back"
role="doc-backlink">↩︎</a></li>
<li id="fn2"></li>
<li id="fn3"></li>
</ol>
</section>

### Aquarium fish

Fish in
<a href="Fish_Tank" class="wikilink" title="fish tank">fish tanks</a>
can be edited via the `Data/AquariumFish` asset.

This consists of a string → string lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  aquarium fish, which must match the non-qualified item ID of the item
  being deposited into the tank.
- The value is a slash-deliminated string with the fields listed below:

<table>
<thead>
<tr>
<th><p>index</p></th>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0</p></td>
<td><p>sprite index</p></td>
<td><p>The index of the sprite in the
<samp>LooseSprites/AquariumFish</samp> spritesheet, starting at 0 for
the top-left sprite. The fish sprites are 24x24px.</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>type</p></td>
<td><p>The fish type, which influences their behavior. Possible
values:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>notes</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>eel</samp></p></td>
<td><p>These fish have a clamped minimum velocity greater than 0,
regardless of their behavior in <samp>Data/Fish</samp>.</p></td>
</tr>
<tr>
<td><p><samp>cephalopod</samp></samp></p></td>
<td><p>These fish have no minimum velocity. They favor moving downward
in the tank rather than upward.</p></td>
</tr>
<tr>
<td><p><samp>crawl</samp></p></td>
<td><p>These fish always stay at the bottom of the tank. They move
horizontally along the tank bottom. These fish have no minimum
velocity.</p></td>
</tr>
<tr>
<td><p><samp>ground</samp></p></td>
<td><p>These fish always stay near the bottom of the tank. They are
closer to the glass than all other fish types. They move horizontally
and vertically, but favor moving downward towards the tank bottom. These
fish have no minimum velocity.</p></td>
</tr>
<tr>
<td><p><samp>fish</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>front_crawl</samp></p></td>
<td><p>Used for crawling fish whose sprites extend past the floor. They
are closer to the glass than all other fish (besides <samp>ground</samp>
fish). Otherwise, it has identical behavior to
<samp>crawl</samp>.</p></td>
</tr>
<tr>
<td><p><samp>static</samp></p></td>
<td><p>These fish always stay at the bottom of the tank. They do not
move within the tank.</p></td>
</tr>
<tr>
<td><p><samp>float</samp></p></td>
<td></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>2<br />
3–5</p></td>
<td><p>idle animation<br />
dart animation</p></td>
<td><p>The animation used by the fish when it's idling (2) or darting
(3–5). This is specified as a list of space-delimited frames, where each
frame is the sprite index in the <samp>LooseSprites/AquariumFish</samp>
spritesheet to display. Each frame is displayed for 125ms. For example,
<a href="Stingray" class="wikilink" title="Stingray">Stingrays</a> have
their idle animation set to <samp>70 70 70 71 71 72</samp>.</p>
<p>The dart animation is split into three fields: start (3), hold (4),
and end (5).</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>texture</p></td>
<td><p>The asset name for the texture containing the fish's sprite.
Defaults to <samp>LooseSprites/AquariumFish</samp>.</p></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p>hat position</p></td>
<td><p>The pixel position of the hat on the sprite, specified as an
object with <samp>X</samp> and <samp>Y</samp> values. Custom fish in
aquariums can wear <a href="hats" class="wikilink"
title="hats">hats</a>, just like vanilla <a href="Sea_Urchin"
class="wikilink" title="sea urchins">sea urchins</a>.</p></td>
</tr>
</tbody>
</table>

## Spawning Fish

Fish spawn data is stored in `Data/Locations`. Fish can be added to a
location by editing the `Fish` field in the location's data entry.
Distinct fishing areas can be defined within the same location (for
example, a pond and a river within the same location that have different
fish spawn chances) by editing the `FishAreas` field. These fishing
areas can then be referenced by ID in the `Fish` field. See
<a href="Modding_Location_data" class="wikilink"
title="Modding:Location data">Modding:Location data</a> for more
information.

## References

<references />

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="de_Modding_Fisch_Daten" class="wikilink"
title="de:Modding:Fisch Daten">de:Modding:Fisch Daten</a>
<a href="es_Modding_Datos_de_pescado" class="wikilink"
title="es:Modding:Datos de pescado">es:Modding:Datos de pescado</a>
<a href="pt_Modificações_Dados_de_Peixes" class="wikilink"
title="pt:Modificações:Dados de Peixes">pt:Modificações:Dados de
Peixes</a> <a href="ru_Модификации_Рыболовство" class="wikilink"
title="ru:Модификации:Рыболовство">ru:Модификации:Рыболовство</a>
<a href="zh_模组_鱼类数据" class="wikilink"
title="zh:模组:鱼类数据">zh:模组:鱼类数据</a>
