---
title: "Content"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, content]
---
### Content

`this.Helper.Events.Content` has events related to assets loaded from
the content pipeline.

<table>
<thead>
<tr>
<th><p>event</p></th>
<th><p>summary</p>
<h4 id="assetrequested">AssetRequested</h4>
<p><em>Group:</em> <code>Content</code></p>
<p>Raised when an asset is being requested from the content pipeline.
The asset isn't necessarily being loaded yet (<em>e.g.</em> the game may
be checking if it exists).</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Name</samp></p></td>
<td><p><samp>IAssetName</samp></p></td>
<td><p>The name of the asset being requested, including the locale code
if any (like the <samp>.fr-FR</samp> in
<samp>Data/Bundles.fr-FR</samp>). This includes utility methods to parse
the value, like <code>e.Name.IsEquivalentTo("Portraits/Abigail")</code>
(which handles any differences in formatting for you).</p></td>
</tr>
<tr>
<td><p><samp>e.NameWithoutLocale</samp></p></td>
<td><p><samp>IAssetName</samp></p></td>
<td><p>Equivalent to <samp>e.Name</samp> but without the locale code (if
any). For example, if <samp>e.Name</samp> is
<samp>Data/Bundles.fr-FR</samp>, this field will contain
<samp>Data/Bundles</samp>.</p></td>
</tr>
<tr>
<td><p><samp>e.LoadFrom(...)</samp></p></td>
<td><p><em><code>method</code></em></p></td>
<td><p>Call this method to provide the initial instance for the asset,
instead of trying to load it from the game's <samp>Content</samp>
folder. For example:</p></td>
</tr>
<tr>
<td><p><samp>e.LoadFromModFile&lt;T&gt;(...)</samp></p></td>
<td><p><em><code>method</code></em></p></td>
<td><p>Call this method to provide the initial instance for the asset by
loading a file from your mod folder. For example:</p></td>
</tr>
<tr>
<td><p><samp>e.Edit(...)</samp></p></td>
<td><p><em><code>method</code></em></p></td>
<td><p>Call this method to apply edits to the asset after it's loaded.
For example:</p></td>
</tr>
</tbody>
</table>
<h4 id="assetsinvalidated">AssetsInvalidated</h4>
<p><em>Group:</em> <code>Content</code></p>
<p>Raised after one or more assets were <a
href="Modding_Modder_Guide_APIs_Content#Cache_invalidation"
class="wikilink" title="invalidated from the content cache">invalidated
from the content cache</a> by a mod, so they'll be reloaded next time
they're requested. If the assets will be reloaded or propagated
automatically, this event is raised before that happens.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Names</samp></p></td>
<td><p><samp>IReadOnlySet&lt;IAssetName&gt;</samp></p></td>
<td><p>The asset names that were invalidated, including the locale code
if any (like the <samp>.fr-FR</samp> in
<samp>Data/Bundles.fr-FR</samp>). These include utility methods to parse
the values, like <code>name.IsEquivalentTo("Portraits/Abigail")</code>
(which handles any differences in formatting for you).</p></td>
</tr>
<tr>
<td><p><samp>e.NamesWithoutLocale</samp></p></td>
<td><p><samp>IReadOnlySet&lt;IAssetName&gt;</samp></p></td>
<td><p>Equivalent to <samp>e.Names</samp> but without the locale code
(if any). For example, if <samp>e.Names</samp> contains
<samp>Data/Bundles.fr-FR</samp>, this field will contain
<samp>Data/Bundles</samp>.</p></td>
</tr>
</tbody>
</table>
<h4 id="assetready">AssetReady</h4>
<p><em>Group:</em> <code>Content</code></p>
<p>Raised after an asset is loaded by the content pipeline, after any
mod edits specified via <a href="#Content.AssetRequested"
class="wikilink" title="AssetRequested"><samp>AssetRequested</samp></a>
have been applied.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Name</samp></p></td>
<td><p><samp>IAssetName</samp></p></td>
<td><p>The name of the asset that was loaded, including the locale code
if any (like the <samp>.fr-FR</samp> in
<samp>Data/Bundles.fr-FR</samp>). This includes utility methods to parse
the value, like <code>e.Name.IsEquivalentTo("Portraits/Abigail")</code>
(which handles any differences in formatting for you).</p></td>
</tr>
<tr>
<td><p><samp>e.NameWithoutLocale</samp></p></td>
<td><p><samp>IAssetName</samp></p></td>
<td><p>Equivalent to <samp>e.Name</samp> but without the locale code (if
any). For example, if <samp>e.Name</samp> is
<samp>Data/Bundles.fr-FR</samp>, this field will contain
<samp>Data/Bundles</samp>.</p></td>
</tr>
</tbody>
</table>
<h4 id="localechanged">LocaleChanged</h4>
<p><em>Group:</em> <code>Content</code></p>
<p>Raised after the game language changes. For non-English players, this
may be raised during startup when the game switches to the previously
selected language.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.OldLanguage</samp></p></td>
<td><p><samp>LanguageCode</samp></p></td>
<td><p>The previous value for the game's language enum. For a custom
language, this is always <samp>LanguageCode.mod</samp>.</p></td>
</tr>
<tr>
<td><p><samp>e.OldLocale</samp></p></td>
<td><p><samp>string</samp></p></td>
<td><p>The previous value for the locale code. This is the locale code
as it appears in asset names, like <samp>fr-FR</samp> in
<samp>Maps/springobjects.fr-FR</samp>. The locale code for English is an
empty string.</p></td>
</tr>
<tr>
<td><p><samp>e.NewLanguage</samp></p></td>
<td><p><samp>LanguageCode</samp></p></td>
<td><p>The new value for the game's language enum. See notes on
<samp>OldLanguage</samp>.</p></td>
</tr>
<tr>
<td><p><samp>e.NewLocale</samp></p></td>
<td><p><samp>string</samp></p></td>
<td><p>The new value for the locale code. See notes on
<samp>OldLocale</samp>.</p></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
