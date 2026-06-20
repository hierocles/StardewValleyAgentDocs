---
title: "Update Checks"
wiki_source: "Modding:Modder Guide/APIs/Update checks"
permalink: /Modding:Modder_Guide/APIs/Update_checks/
category: smapi
tags: [update-checks, introduction, enable-update-checks, valid-sites, advanced, beta-versions, update-subkeys, disable-update-checks-locally]
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

Every SMAPI mod or content pack can benefit from automatic update
checks, so the player sees an alert when a new version is available.
This helps ensures players always have the latest version of your mod,
which improves their experience and reduces support requests.

## Introduction

### Enable update checks

You can add *update keys* to
<a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
title="your manifest.json">your <samp>manifest.json</samp></a> to enable
update checks. An update key tells SMAPI where the mod page is. For
example, `Nexus:2400` means :

``` json
"UpdateKeys": [ "Nexus:2400" ]
```

If you have multiple update keys, SMAPI will check them all and show an
alert for the latest version it finds. (If multiple sites have the
latest version, it will link to the earlier one in the list.)

``` javascript
"UpdateKeys": [ "Chucklefish:4250", "Nexus:541", "GitHub:Pathoschild/LookupAnything" ]
```

(SMAPI also fetches mod info from the
<a href="Modding_Mod_compatibility" class="wikilink"
title="mod compatibility list">mod compatibility list</a>, so mods on
that page may get update checks even without update keys. You should
still add update keys to your manifest in case that changes, and to
support mod managers and other tools.)

### Valid sites

Here are the supported mod sites:

<table>
<thead>
<tr>
<th><p>mod site</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a
href="https://community.playstarbound.com/resources/categories/stardew-valley.22/">Chucklefish</a></p></td>
<td><p><strong>(Deprecated)</strong> Make sure you have a mod release
page (with a URL containing <samp>/resources/</samp> instead of
<samp>/thread/</samp>) and it has a <a
href="http://semver.org/">semantic version</a>, then specify the mod ID
(the number in the mod page URL).</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;UpdateKeys&quot;</span><span class="op">:</span> [ <span class="st">&quot;Chucklefish:4250&quot;</span> ]</span></code></pre></div></td>
</tr>
<tr>
<td><p><a
href="https://www.curseforge.com/stardewvalley">CurseForge</a></p></td>
<td><p>Make sure the latest file's display name contains a <a
href="http://semver.org/">semantic version</a> at the end, with a space
before the version and optional file extension. For example, SMAPI will
recognise the version in these display names: <code>1.3.0</code>,
<code>Example Mod 1.10</code>,
<code>Example Mod 1.10.0-prerelease.zip</code>.</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;UpdateKeys&quot;</span><span class="op">:</span> [ <span class="st">&quot;CurseForge:309243&quot;</span> ]</span></code></pre></div></td>
</tr>
<tr>
<td><p><a href="https://github.com/">GitHub</a></p></td>
<td><p>Make sure your <a
href="https://help.github.com/articles/creating-releases/">GitHub
project has at least one release</a> and the latest release's tag is a
<a href="http://semver.org/">semantic version</a>, then specify your
GitHub username and project name.</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;UpdateKeys&quot;</span><span class="op">:</span> [ <span class="st">&quot;GitHub:Pathoschild/LookupAnything&quot;</span> ]</span></code></pre></div>
<p>SMAPI will get the version from the release tag. Note that with the
way GitHub release tags work, they do not support "monorepos", when
multiple mods are on the same repository with different version
numbers.</p></td>
</tr>
<tr>
<td><p><a
href="https://www.moddrop.com/stardew-valley/">ModDrop</a></p></td>
<td><p>Make sure the mod page has a <a
href="http://semver.org/">semantic version</a>, then specify the mod ID
(the number in the mod page URL).</p>
<div class="sourceCode" id="cb4"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;UpdateKeys&quot;</span><span class="op">:</span> [ <span class="st">&quot;ModDrop:123338&quot;</span> ]</span></code></pre></div>
<p>SMAPI will get the version from files under 'Main Versions'.</p></td>
</tr>
<tr>
<td><p><a href="https://www.nexusmods.com/stardewvalley">Nexus
Mods</a></p></td>
<td><p>Make sure the Nexus mod has a <a
href="http://semver.org/">semantic version</a>, then specify the mod ID
(the number in the mod page URL). When creating a new mod on Nexus, the
ID is added to the URL after the first step, before you need to upload
the file.</p>
<div class="sourceCode" id="cb5"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;UpdateKeys&quot;</span><span class="op">:</span> [ <span class="st">&quot;Nexus:541&quot;</span> ]</span></code></pre></div>
<p>SMAPI will get the version from the mod, 'main files' downloads, or
'optional files' downloads (whichever is higher).</p></td>
</tr>
</tbody>
</table>

## Advanced

### Beta versions

A *prerelease version* (often called an *alpha* or *beta*) has a
prerelease tag in the version number. For example, `1.0.0-beta.5` is a
prerelease version of an upcoming `1.0.0`.

If you have both prerelease and non-prerelease versions, update checks
depend on the player's installed mod version:

- Stable channel: players with a non-prerelease version installed only
  see update alerts for non-prerelease versions (unless the main mod
  version is prerelease).
- Beta channel: players with a prerelease version see update alerts for
  any newer version, whether prerelease or non-prerelease.

For example, let's say your mod has two current versions: `1.7.0` and
`2.0.0-beta`. A player who has `1.6.0` installed would see an update
alert for `1.7.0`, and a player with `1.6.1-beta` would see an update
alert for `2.0.0-beta`.

### Update subkeys

SMAPI assumes each mod page is about a single mod, so the highest file
version is the latest one. That means having multiple mods on the same
page can cause false update alerts. For example, let's say you have one
Nexus page with two different mods in the downloads: *Geode Crusher*
(version `1.0.5`) and *Diamond Crusher* (version `2.1.0`). If a player
has the latest version of *Geode Crusher* installed, they would always
get update alerts for version `2.1.0` even though that's a different
mod.

You can add an *update subkey* at the end of your normal update key
after `@`:

``` json
"UpdateKeys": [ "Nexus:2400@GeodeCrusher" ]
```

When SMAPI fetches available versions from the page, it will only
consider files that have `@GeodeCrusher` (**including `@`**) somewhere
in the title or description.

Caveats:

- If no files match the subkey, SMAPI will ignore the subkey and perform
  a normal update check.
- For mods on CurseForge, SMAPI won't see subkeys in the file
  description since that's not available through the CurseForge API.
- For mods on GitHub, subkeys don't really do anything since only the
  latest release is fetched.

### Disable update checks locally

SMAPI checks for updates in the background, so disabling update checks
has zero effect on load times.

To disable update checks...

- For SMAPI and all mods: edit the `smapi-internal/config.json` file and
  set `CheckForUpdates` to false. You'll no longer be notified about
  newer versions of SMAPI or installed mods, so this is not recommended.
- For a specific mod: edit the `smapi-internal/config.json` file and add
  the mod ID to the `SuppressUpdateChecks` field.

Note that edits to `smapi-internal/config.json` will be lost when you
update SMAPI. See the instructions at the top of that file to create a
permanent config file.

### Update check algorithm

Here's how SMAPI decides which update alerts to show in the SMAPI
console for a mod:

1.  Collect update keys:
    1.  Get the initial
        <a href="#Introduction" class="wikilink" title="update keys">update
        keys</a> from the mod's
        <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
        title="manifest">manifest</a>.
    2.  Match the mod ID with the
        <a href="Modding_Mod_compatibility" class="wikilink"
        title="mod compatibility list">mod compatibility list</a> and
        `smapi-internal/metadata.json` to add any other update keys that
        aren't in the manifest.
    3.  Apply update key overrides from the mod compatibility list.
2.  Get the possible updates:
    1.  Collect versions from every matched update key (see
        <a href="#Valid_sites" class="wikilink" title="valid sites"><em>valid
        sites</em></a> for which versions are used).
    2.  Filter the list of versions to...
        - the main mod version;
        - the optional prerelease version if the player has a beta
          version of SMAPI, *or* they have an older prerelease mod
          version installed, *or* the installed version failed to load;
        - the unofficial version from the mod compatibility list;
        - and the unofficial version for the beta, if using a prerelease
          version of SMAPI.
3.  Recommend the highest version from the filtered list (if newer than
    the installed version).

If multiple mod pages have the recommended update, SMAPI links to the
first match in this order:

1.  pages listed in the mod manifest's update keys (in the order
    listed);
2.  the default update key from SMAPI's `smapi-internal/metadata.json`;
3.  update keys from the mod compatibility list (in the order Nexus,
    ModDrop, CurseForge, and Chucklefish);
4.  update key overrides from the mod compatibility list.

### Custom update manifest

**This is highly specialized** and supports specific edge cases (like
mods which only exist in a shared GitHub repository or custom website).
Most mods should use normal update keys instead.

An *update manifest* is a JSON file hosted on a website, which the SMAPI
servers can download to get info about mods which aren't available on a
more usual site like Nexus. For example, this manifest shows info about
a mod which is only hosted on a custom website:

``` js
{
    "Format": "4.0.0",
    "Mods": {
        "ExampleMod": {
            "Name": "Example Mod",
            "ModPageUrl": "https://example.org/mods/example-mod",
            "Versions": [
                { "Version": "1.0.0" }
            ]
        }
    }
}
```

Here are the expected fields (all required unless noted otherwise):

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Format</samp></p></td>
<td><p>The version of the manifest format (currently
<samp>4.0.0</samp>). This is used to parse older manifests correctly if
later versions of SMAPI change the format.</p></td>
</tr>
<tr>
<td><p><samp>Mods</samp></p></td>
<td><p>The mods for which info is provided. Any number of mods can be
listed.</p>
<p>This consists of a string → model lookup, where...</p>
<ul>
<li>The key is the update subkey (see details below the table).</li>
<li>The value is a model with the fields listed below.</li>
</ul>
<p>Each mod has these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p>The human-readable display name for the mod.</p></td>
</tr>
<tr>
<td><p><samp>ModPageUrl</samp></p></td>
<td><p>The URL of the page from which the player can download
updates.</p></td>
</tr>
<tr>
<td><p><samp>Versions</samp></p></td>
<td><p>The versions available to download. Any number of versions can be
listed, and they'll be compared to the player's installed version using
the <a href="#Update_check_algorithm" class="wikilink"
title="usual update check algorithm">usual update check
algorithm</a>.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Version</samp></p></td>
<td><p>The semantic version number.</p></td>
</tr>
<tr>
<td><p><samp>ModPageUrl</samp></p></td>
<td><p><em>(Optional)</em> The URL of the page from which the player can
download this update, if different from the <samp>ModPageUrl</samp> for
the mod itself.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

To use the manifest, a mod must add an
<a href="#Enable_update_checks" class="wikilink"
title="update key">update key</a> in the form
`UpdateManifest:<full URL to json file>@<mod key>`. If the example above
was hosted at `<nowiki>https://example.org/mod-updates.json</nowiki>`,
then its update key would look like this:

``` js
"UpdateKeys": [ "UpdateManifest:https://example.org/mod-updates.json@ExampleMod" ]
```

<a href="ru_Модификации_Руководство_мододела_API_Проверка_обновлений"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Проверка обновлений">ru:Модификации:Руководство
мододела/API/Проверка обновлений</a>
<a href="zh_模组_制作指南_APIs_Update_checks" class="wikilink"
title="zh:模组:制作指南/APIs/Update checks">zh:模组:制作指南/APIs/Update
checks</a>
