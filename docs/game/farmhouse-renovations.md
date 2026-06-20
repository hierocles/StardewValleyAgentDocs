---
title: "Farmhouse Renovations"
wiki_source: "Modding:Farmhouse Renovations"
permalink: /Modding:Farmhouse_Renovations/
category: game
tags: [farmhouse-renovations]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how to create custom farmhouse renovations. This is
an advanced guide for mod developers.

You can add custom <a href="Farmhouse#Upgrades" class="wikilink"
title="farmhouse renovations">farmhouse renovations</a> that will be
applied automatically when the specified
<a href="Modding_Mail_data#Mail_flags" class="wikilink"
title="mail flag">mail flag</a> is set. This is based on a new map
property in the farmhouse map:

<table>
<thead>
<tr>
<th><p>valid in</p></th>
<th><p>map property</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>farmhouse</p></td>
<td><p><samp>AdditionalRenovations &lt;renovation&gt;+</samp></p></td>
<td><p>A comma-separated list of renovations to apply, each in the form
<samp>&lt;map patch ID&gt; &lt;required mail flag&gt; &lt;map asset if
active&gt; &lt;map asset if inactive&gt; [area rectangle]</samp>.
Fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>map patch ID</samp></p></td>
<td><p>A unique ID for the patch being applied. This is usually similar
to the renovation name, but can be any unique value. If a renovation
applies multiple map patches, each one must have unique ID.</p></td>
</tr>
<tr>
<td><p><samp>required mail flag</samp></p></td>
<td><p>The <a href="Modding_Mail_data#Mail_flags" class="wikilink"
title="mail flag">mail flag</a> that is checked on the house's owner to
decide whether the patch should be applied.</p></td>
</tr>
<tr>
<td><p><samp>map asset if active</samp></p></td>
<td><p>The asset name for the map applied when the mail flag is set,
relative to the <samp>Maps</samp> folder.</p></td>
</tr>
<tr>
<td><p><samp>map asset if inactive</samp></p></td>
<td><p>The asset name for the map applied when the mail flag is not set,
relative to the <samp>Maps</samp> folder.</p></td>
</tr>
<tr>
<td><p><samp>area rectangle</samp></p></td>
<td><p><em>(Optional)</em> The tile area in the map to patch, specified
as <samp>&lt;X&gt; &lt;Y&gt; &lt;width&gt; &lt;height&gt;</samp>. If
&lt;X&gt; isn't set, this defaults to the top-left corner of the map. If
it is, you must specify all four values.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

For example, this Content Patcher pack would add a renovation to the
fully-upgraded farmhouse based on a custom
`ExampleAuthor_PineapplesEverywhere_HasRenovation` flag. Note that
`TextOperations` is used to avoid overwriting any renovations added by
another mod, and is automatically replaced by Content Patcher to avoid
conflicts with other mods.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Ремонт_фермерского_дома" class="wikilink"
title="ru:Модификации:Ремонт фермерского дома">ru:Модификации:Ремонт
фермерского дома</a> <a href="zh_模组_农舍升级" class="wikilink"
title="zh:模组:农舍升级">zh:模组:农舍升级</a>
