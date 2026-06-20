---
title: "Manifest"
wiki_source: "Modding:Modder Guide/APIs/Manifest"
permalink: /Modding:Modder_Guide/APIs/Manifest/
category: smapi
tags: [manifest, basic-examples, fields, basic-fields, minimum-smapi-or-game-version, dependencies, update-checks, specialized-fields]
---
<div style="float: right; border: 2px solid rgb(0, 116, 72); background: #A1DEE2; padding: 0.75em; padding-top: 0.5em; margin: 0 0 2em 2em;">

<span style="font-size: larger;">**Creating SMAPI mods**
<a href="File_SMAPI_mascot.png" class="wikilink" title="25px">25px</a></span>

------------------------------------------------------------------------

- <a href="Modding_Modder_Guide_Get_Started" class="wikilink"
  title="Get started">Get started</a>
- <a href="Modding_Modder_Guide_Game_Fundamentals" class="wikilink"
  title="Game fundamentals">Game fundamentals</a>
- <a href="Modding_Modder_Guide_Test_and_Troubleshoot" class="wikilink"
  title="Test &amp; troubleshoot">Test &amp; troubleshoot</a>
- <a href="Modding_Modder_Guide_Release" class="wikilink"
  title="Release">Release</a>
- <a href="Modding_Modder_Guide_APIs" class="wikilink"
  title="API reference">API reference</a>

  Basic SMAPI APIs:

  - <a href="Modding_Modder_Guide_APIs_Mod_structure" class="wikilink"
    title="Mod structure">Mod structure</a>
  - <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
    title="Manifest">Manifest</a>
  - <a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
    title="Events">Events</a>
  - <a href="Modding_Modder_Guide_APIs_Config" class="wikilink"
    title="Configuration">Configuration</a>
  - <a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
    title="Load &amp; edit content">Load &amp; edit content</a>
  - <a href="Modding_Modder_Guide_APIs_Data" class="wikilink"
    title="Data">Data</a>
  - <a href="Modding_Modder_Guide_APIs_Input" class="wikilink"
    title="Input">Input</a>
  - <a href="Modding_Modder_Guide_APIs_Logging" class="wikilink"
    title="Logging">Logging</a>
  - <a href="Modding_Modder_Guide_APIs_Reflection" class="wikilink"
    title="Reflection">Reflection</a>
  - <a href="Modding_Modder_Guide_APIs_Multiplayer" class="wikilink"
    title="Multiplayer">Multiplayer</a>
  - <a href="Modding_Modder_Guide_APIs_Translation" class="wikilink"
    title="Translation">Translation</a>
  - <a href="Modding_Modder_Guide_APIs_Update_checks" class="wikilink"
    title="Update checks">Update checks</a>
  - <a href="Modding_Modder_Guide_APIs_Utilities" class="wikilink"
    title="Utilities">Utilities</a>

  Advanced SMAPI APIs:

  - <a href="Modding_Modder_Guide_APIs_Content_Packs" class="wikilink"
    title="Content packs">Content packs</a>
  - <a href="Modding_Modder_Guide_APIs_Console" class="wikilink"
    title="Mod console commands">Mod console commands</a>
  - <a href="Modding_Modder_Guide_APIs_Integrations" class="wikilink"
    title="Mod integrations">Mod integrations</a>
  - <a href="Modding_Modder_Guide_APIs_Harmony" class="wikilink"
    title="Harmony patching">Harmony patching</a>
- <a href="Modding_Index#Advanced_topics" class="wikilink"
  title="Specific guides">Specific guides</a>

</div>

←
<span style="font-size: smaller;"><a href="Modding_Index" class="wikilink"
title="Modding:Index">Modding:Index</a></span>
<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

Every SMAPI mod or content pack must have a `manifest.json` file in its
folder. SMAPI uses this to identify and load the mod, perform update
checks, etc. The manifest info is also available to any mod in code
(using `this.ModManifest` for the current mod's manifest, or
<a href="Modding_Modder_Guide_APIs_Integrations#Mod_registry"
class="wikilink" title="mod registry">mod registry</a> for other mods'
manifests).

## Basic examples

Here's the basic format (see below for details on each field):

<table>
<thead>
<tr>
<th><p>For a SMAPI mod</p></th>
<th><p>For a content pack</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>{</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Name&quot;</span><span class="op">:</span> <span class="st">&quot;Your Project Name&quot;</span><span class="op">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Author&quot;</span><span class="op">:</span> <span class="st">&quot;your name&quot;</span><span class="op">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Version&quot;</span><span class="op">:</span> <span class="st">&quot;1.0.0&quot;</span><span class="op">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Description&quot;</span><span class="op">:</span> <span class="st">&quot;One or two sentences about the mod.&quot;</span><span class="op">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;UniqueID&quot;</span><span class="op">:</span> <span class="st">&quot;YourName.YourProjectName&quot;</span><span class="op">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;EntryDll&quot;</span><span class="op">:</span> <span class="st">&quot;YourDllFileName.dll&quot;</span><span class="op">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;UpdateKeys&quot;</span><span class="op">:</span> []</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>{</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Name&quot;</span><span class="op">:</span> <span class="st">&quot;Your Project Name&quot;</span><span class="op">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Author&quot;</span><span class="op">:</span> <span class="st">&quot;your name&quot;</span><span class="op">,</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Version&quot;</span><span class="op">:</span> <span class="st">&quot;1.0.0&quot;</span><span class="op">,</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;Description&quot;</span><span class="op">:</span> <span class="st">&quot;One or two sentences about the mod.&quot;</span><span class="op">,</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;UniqueID&quot;</span><span class="op">:</span> <span class="st">&quot;YourName.YourProjectName&quot;</span><span class="op">,</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;UpdateKeys&quot;</span><span class="op">:</span> []<span class="op">,</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;ContentPackFor&quot;</span><span class="op">:</span> {</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;UniqueID&quot;</span><span class="op">:</span> <span class="st">&quot;Pathoschild.ContentPatcher&quot;</span></span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Fields

### Basic fields

All mods should specify the following fields.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p>The mod name. SMAPI uses this in player messages, logs, and
errors. Example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Name&quot;</span><span class="op">:</span> <span class="st">&quot;Lookup Anything&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Author</samp></p></td>
<td><p>The name of the person who created the mod. Ideally this should
include the username used to publish mods. Example:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Author&quot;</span><span class="op">:</span> <span class="st">&quot;Pathoschild&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Version</samp></p></td>
<td><p>The mod's <a href="http://semver.org/">semantic version</a>. Make
sure you update this for each release! SMAPI uses this for update
checks, mod dependencies, and compatibility blacklists (if the mod
breaks in a future version of the game). For example:</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Version&quot;</span><span class="op">:</span> <span class="st">&quot;1.0.0&quot;</span></span></code></pre></div>
<p>If you set the <code>&lt;Version&gt;</code> in your
<samp>.csproj</samp> project file, you can use the exact text
<samp>%ProjectVersion%</samp> in the manifest file to set the same
version automatically:</p>
<div class="sourceCode" id="cb4"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Version&quot;</span><span class="op">:</span> <span class="st">&quot;%ProjectVersion%&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Description</samp></p></td>
<td><p>A short explanation of what your mod does (one or two sentences),
shown in the SMAPI log. Example:</p>
<div class="sourceCode" id="cb5"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Description&quot;</span><span class="op">:</span> <span class="st">&quot;View metadata about anything by pressing a button.&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>UniqueID</samp></p></td>
<td><p>A unique identifier for your mod. The recommended format is
<samp>&lt;your name&gt;.&lt;mod name&gt;</samp>, with no spaces or
special characters. SMAPI uses this for update checks, mod dependencies,
and compatibility blacklists (if the mod breaks in a future version of
the game). When another mod needs to reference this mod, it uses the
unique ID. For this reason, once you've published your mod, do not
change this unique ID in future versions of the same mod. Example:</p>
<div class="sourceCode" id="cb6"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;UniqueID&quot;</span><span class="op">:</span> <span class="st">&quot;Pathoschild.LookupAnything&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>EntryDll</samp> <strong>or</strong>
<samp>ContentPackFor</samp></p></td>
<td><p>All mods must specify either <samp>EntryDll</samp> (for a SMAPI
mod) or <samp>ContentPackFor</samp> (for a <a
href="Modding_Content_packs" class="wikilink"
title="content pack">content pack</a>). These are mutually exclusive —
you can't specify both.</p>
<p>For a SMAPI mod, <samp>EntryDll</samp> is the mod's compiled DLL
filename in its mod folder. Example:</p>
<div class="sourceCode" id="cb7"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;EntryDll&quot;</span><span class="op">:</span> <span class="st">&quot;LookupAnything.dll&quot;</span></span></code></pre></div>
<p>For a content pack, <samp>ContentPackFor</samp> specifies which mod
can read it. The <samp>MinimumVersion</samp> is optional. Example:</p>
<div class="sourceCode" id="cb8"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ContentPackFor&quot;</span><span class="op">:</span> {</span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a>   <span class="st">&quot;UniqueID&quot;</span><span class="op">:</span> <span class="st">&quot;Pathoschild.ContentPatcher&quot;</span><span class="op">,</span></span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a>   <span class="st">&quot;MinimumVersion&quot;</span><span class="op">:</span> <span class="st">&quot;1.0.0&quot;</span></span>
<span id="cb8-4"><a href="#cb8-4" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
</tbody>
</table>

### Minimum SMAPI or game version

The `MinimumApiVersion` and `MinimumGameVersion` field sets the minimum
version of SMAPI or Stardew Valley needed to use this mod. If a player
tries to use the mod with an older version, they'll see a friendly
message saying they need to update it.

For example:

``` javascript
"MinimumApiVersion": "4.0.0"
```

### Dependencies

The `Dependencies` field specifies other mods required to use this mod.
If a player tries to use the mod and the dependencies aren't installed,
the mod won't be loaded and they'll see a friendly message saying they
need to install those. For example:

``` javascript
"Dependencies": [
   {
      "UniqueID": "SMAPI.ConsoleCommands",
      "MinimumVersion": "3.8.0" // optional. If specified, older versions won't meet the requirement.
   }
]
```

You can mark a dependency as optional. It will be loaded first if it's
installed, otherwise it'll be ignored.

``` javascript
"Dependencies": [
   {
      "UniqueID": "SMAPI.ConsoleCommands",
      "IsRequired": false
   }
]
```

### Update checks

SMAPI can detect new versions of your mod and alert the user with a link
to your mod page. You can enable this by setting the `UpdateKeys` field
in your `manifest.json`, which tells SMAPI where to check.

See <a href="Modding_Modder_Guide_APIs_Update_checks" class="wikilink"
title="update checks"><em>update checks</em></a> for more information.

## Specialized fields

**⚠️ Most mods shouldn't need to use these fields.**

### Anything else

Any other fields will be stored in the `IManifest.ExtraFields`
dictionary, which is available through the
<a href="Modding_Modder_Guide_APIs_Integrations#Mod_registry"
class="wikilink" title="mod registry">mod registry</a>. Extra fields are
ignored by SMAPI, but may be useful for extended metadata intended for
other mods.

<a href="es_Modding_Guía_del_Modder_APIs_Manifest" class="wikilink"
title="es:Modding:Guía del Modder/APIs/Manifest">es:Modding:Guía del
Modder/APIs/Manifest</a>
<a href="ru_Модификации_Руководство_мододела_API_Манифест"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Манифест">ru:Модификации:Руководство
мододела/API/Манифест</a>
<a href="tr_Modlama_Mod_Rehberi_API&#39;ler_Manifest" class="wikilink"
title="tr:Modlama:Mod Rehberi/API&#39;ler/Manifest">tr:Modlama:Mod
Rehberi/API'ler/Manifest</a>
<a href="zh_模组_制作指南_APIs_Manifest" class="wikilink"
title="zh:模组:制作指南/APIs/Manifest">zh:模组:制作指南/APIs/Manifest</a>
