---
title: "Bundles"
wiki_source: "Modding:Bundles"
permalink: /Modding:Bundles/
category: game
tags: [bundles, raw-data, format, reward-limitation]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

## Raw data

Bundle data is stored in `Content\Data\Bundles.xnb`, which can be
<a href="Modding_Editing_XNB_files#Getting_started" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of for reference:

## Format

All bundles share the same format, which cannot be re-ordered. Each
field is explained below.

Key format:

| index | syntax | description |
|----|----|----|
| 0 | room ID | The room of the Community Center that the bundle is located in. This can be `Pantry`, `Crafts Room`, `Fish Tank`, `Boiler Room`, `Vault`, and `Bulletin Board`. |
| 1 | sprite index | The bundle's sprite in the `LooseSprites/JunimoNote` spritesheet, starting from zero in the top-left corner of the sprite area. Some index numbers will cause a menu crash if used, for unknown reasons. |

Value format:

<table>
<thead>
<tr>
<th><p>index</p></th>
<th><p>syntax</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0</p></td>
<td><p>bundle name</p></td>
<td><p>The internal name for the bundle.</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>reward</p></td>
<td><p>Format: <samp>&lt;item type&gt; &lt;item ID&gt;
&lt;count&gt;</samp></p>
<p>The reward given when the bundle is completed. Arguments:</p>
<ul>
<li>&lt;item type&gt;: one of <samp>O</samp> (<a href="Modding_Objects"
class="wikilink" title="object">object</a>), <samp>BO</samp> (<a
href="Modding_Big_craftables" class="wikilink" title="big craftable">big
craftable</a>), <samp>F</samp> (<a href="Modding_Furniture"
class="wikilink" title="furniture">furniture</a>), <samp>H</samp> (<a
href="Modding_Hats" class="wikilink" title="hat">hat</a>),
<samp>C</samp> (<a href="Modding_Pants" class="wikilink"
title="pants">pants</a> or <a href="Modding_Shirts" class="wikilink"
title="shirt">shirt</a>), or <samp>R</samp> (ring-type <a
href="Modding_Objects" class="wikilink" title="object">object</a>).</li>
<li>&lt;item ID&gt;: the <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="unqualified item ID">unqualified item ID</a>.</li>
<li>&lt;count&gt;: the stack size of the produced item, if applicable
for its type. Some types (e.g. big craftables or rings) aren't stackable
so this field will be ignored.</li>
</ul>
<p>A bundle can only produce one item stack. For example, a bundle can
provide 15 apples as a reward, but it can't provide two different
items.</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>requirements</p></td>
<td><p>Format: <samp>[&lt;item ID&gt; &lt;count&gt; &lt;min
quality&gt;]+</samp></p>
<p>The <a href="Modding_Objects" class="wikilink"
title="object">object</a>-type items required to complete the bundle.
You can list one to twelve items (more than twelve will crash the bundle
menu).</p>
<p>Arguments:</p>
<ul>
<li>&lt;item ID&gt;: the <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="unqualified item ID">unqualified item ID</a> for the <a
href="Modding_Objects" class="wikilink" title="object">object</a>-type
item.</li>
<li>&lt;count&gt;: the number of the item required.</li>
<li>&lt;min quality&gt;: The minimum <a href="Modding_Items#Quality"
class="wikilink" title="item quality">item quality</a> (numeric form)
that must be provided. Note that some items can't have iridium quality
by default.</li>
</ul></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>color</p></td>
<td><p>The index of the bundle color in the
<samp>LooseSprites/JunimoNote</samp> spritesheet, starting from the
top-left corner of the color icons area. This can be one of these
values:</p>
<table>
<thead>
<tr>
<th><p>index</p></th>
<th><p>icon (incomplete)</p></th>
<th><p>icon (complete)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>0</samp></p></td>
<td><p>green</p></td>
<td><p>green</p></td>
</tr>
<tr>
<td><p><samp>1</samp></p></td>
<td><p>purple</p></td>
<td><p>purple</p></td>
</tr>
<tr>
<td><p><samp>2</samp></p></td>
<td><p>orange</p></td>
<td><p>organge</p></td>
</tr>
<tr>
<td><p><samp>3</samp></p></td>
<td><p>yellow</p></td>
<td><p>pink</p></td>
</tr>
<tr>
<td><p><samp>4</samp></p></td>
<td><p>red</p></td>
<td><p>flower<br />
<small>(yellow center with red &amp; green leaves)</small></p></td>
</tr>
<tr>
<td><p><samp>5</samp></p></td>
<td><p>blue</p></td>
<td><p>blue</p></td>
</tr>
<tr>
<td><p><samp>6</samp></p></td>
<td><p>teal</p></td>
<td><p>teal</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>item count</p></td>
<td><p>The number of distinct items needed to complete the bundle, or
blank to match the number of required items. This can be a value between
1 and 12 (higher numbers will break the UI layout).</p>
<p>For example, if you have six entries in the 'requirements' field and
set this to 4, the player needs to fill the bundle with any four of the
six required items.</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>override texture and sprite index</p></td>
<td><p>If not blank, the texture and sprite index to use as the icon
instead of automatically from <code>LooseSprites/JunimoNote</code>,
specified in the form of
<code>&lt;texture asset name&gt;:&lt;sprite index&gt;</code>.</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>display name</p></td>
<td><p>The translated display name for this bundle (this is also shown
in English).</p></td>
</tr>
</tbody>
</table>

## Reward limitation

Bundles can only reward one big object (auto-grabber, crystalarium,
lightning rod, etc.) at a time. If you attempt to make it reward
multiple big objects by changing the quantity, it will only reward one
and ignore the others.

Bundles can also only reward one type of object at a time. Thus, it is
possible to make a bundle reward 5 iridium sprinklers, but it is not
possible to make a bundle reward 2 iridium sprinklers and 3 quality
sprinklers.

Either way, it is not possible to reward multiple objects by editing
bundles.xnb. Doing so would require modding the game code itself, and
that particular mod does not exist yet.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Datos_de_lotes" class="wikilink"
title="es:Modding:Datos de lotes">es:Modding:Datos de lotes</a>
<a href="ru_Модификации_Пакеты" class="wikilink"
title="ru:Модификации:Пакеты">ru:Модификации:Пакеты</a>
<a href="zh_模组_收集包数据" class="wikilink"
title="zh:模组:收集包数据">zh:模组:收集包数据</a>
