---
title: "Mod Structure"
wiki_source: "Modding:Modder Guide/APIs/Mod structure"
permalink: /Modding:Modder_Guide/APIs/Mod_structure/
category: smapi
tags: [mod-structure, basic-structure, mod-entry, dependencies]
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

**See <a href="Modding_Modder_Guide_Get_Started" class="wikilink"
title="Modding:Modder Guide">Modding:Modder Guide</a> for an
introduction to creating a SMAPI mod. This is a technical reference page
which assumes you've already followed that guide.**

## Basic structure

A SMAPI mod must have...

1.  a compiled DLL file which contains the code to run as part of the
    mod (see
    <a href="#Mod_entry" class="wikilink" title="mod entry below"><em>mod
    entry</em> below</a>);
2.  a <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
    title="manifest.json file"><samp>manifest.json</samp> file</a> which
    describes the mod.

It may optionally have...

1.  any number of <a href="#Dependencies" class="wikilink"
    title="compiled .dll and .pdb files referenced by the main mod DLL">compiled
    <samp>.dll</samp> and <samp>.pdb</samp> files referenced by the main mod
    DLL</a>;
2.  an <a href="Modding_Modder_Guide_APIs_Translation" class="wikilink"
    title="i18n folder containing translations"><samp>i18n</samp> folder
    containing translations</a>;
3.  any number of custom files used by the mod code (usually in an
    `assets` folder by convention).

## Mod entry

The main mod project must have a subclass of `StardewModdingAPI.Mod`.
The class is often named `ModEntry` by convention, but you can use any
valid C# name. The class must implement an `Entry` method, which SMAPI
will call once the mod is loaded. The `helper` argument provides access
to nearly all <a href="Modding_Modder_Guide_APIs" class="wikilink"
title="SMAPI APIs">SMAPI APIs</a> (available as `this.Helper` in other
methods).

Here's the minimum possible implementation (which does nothing at all):

``` c#
using StardewModdingAPI;

/// <summary>The mod entry point.</summary>
internal sealed class ModEntry : Mod
{
    /// <summary>The mod entry point, called after the mod is first loaded.</summary>
    /// <param name="helper">Provides simplified APIs for writing mods.</param>
    public override void Entry(IModHelper helper)
    {

    }
}
```

The `Entry` method is called very early in the launch process, so some
things aren't initialised yet. You can use events like `GameLaunched`,
`SaveLoaded`, or `DayStarted` to access all features. Here's a quick
summary of using APIs in `Entry`:

| feature | status |
|----|----|
| most SMAPI APIs | ✓ available. That includes <a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="registering event handlers">registering event handlers</a>, <a href="Modding_Modder_Guide_APIs_Config" class="wikilink"
title="reading configuration">reading configuration</a>, <a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="loading assets">loading assets</a>, and <a href="Modding_Modder_Guide_APIs_Integrations#Mod_registry"
class="wikilink" title="fetching mod info">fetching mod info</a>. |
| `helper.ModRegistry.GetApi` | ✖ Not available, since some mods aren't initialised yet. |
| Game fields | ✖ Not reliably available, since mods are loaded early in the process. That includes core fields like `Game1.objectInformation`. |

## Dependencies

Most mods are self-contained and only have one DLL file, but that's not
a hard limit. Here are some common patterns:

- <a href="Modding_Modder_Guide_APIs_Manifest#Dependencies"
  class="wikilink" title="Declare a dependency on another mod">Declare a
  dependency on another mod</a>, and SMAPI will load the other mod
  before yours and show a friendly error if it's not installed. You can
  <a href="Modding_Modder_Guide_APIs_Integrations" class="wikilink"
  title="use a mod-provided API">use a mod-provided API</a> if the mod
  has one, or reference the DLL directly. (If you reference a mod DLL,
  make sure it's *not*
  \[<https://msdn.microsoft.com/en-us/library/t1zz5y8c(v=vs.100>).aspx
  marked 'copy local'\] to avoid issues; SMAPI will load the installed
  version instead.)
- [Create a shared
  project](https://docs.microsoft.com/en-us/xamarin/cross-platform/app-fundamentals/shared-projects)
  and reference it from your mod project. The shared project's code will
  be compiled as part of your mod project (so it'll be one DLL
  containing both projects in the mod folder).
- Reference projects/DLLs and copy their DLLs into your mod folder.
  SMAPI will detect the reference and load the DLLs from your mod folder
  automatically. **Don't do this for referencing a mod** — that can
  cause confusing errors when multiple versions are available (see the
  first option instead).

<a href="es_Modding_Guía_del_Modder_APIs_Mod_structure" class="wikilink"
title="es:Modding:Guía del Modder/APIs/Mod structure">es:Modding:Guía
del Modder/APIs/Mod structure</a>
<a href="ru_Модификации_Руководство_мододела_API_Структура_мода"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Структура мода">ru:Модификации:Руководство
мододела/API/Структура мода</a>
<a href="zh_模组_制作指南_APIs_Mod_structure" class="wikilink"
title="zh:模组:制作指南/APIs/Mod structure">zh:模组:制作指南/APIs/Mod
structure</a>
