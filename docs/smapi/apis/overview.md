---
title: "Overview"
wiki_source: "Modding:Modder Guide/APIs"
permalink: /Modding:Modder_Guide/APIs/
category: smapi
tags: [apis, basic-apis, advanced-apis]
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

SMAPI provides a number of APIs for mods to use. Click a section on the
right or below for more details.

## Basic APIs

| page | summary |
|----|----|
| <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
title="Manifest">Manifest</a> | A file needed for every mod or content pack which describes the mod, lists dependencies, enables update checks, etc. |
| <a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="Events">Events</a> | Respond when something happens in the game (*e.g.,* when a save is loaded), and often include details about what happened. |
| <a href="Modding_Modder_Guide_APIs_Config" class="wikilink"
title="Configuration">Configuration</a> | Let players edit a `config.json` file to configure your mod. |
| <a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="Content">Content</a> | Load images/maps/data, and edit or replace the game's images/maps/data. |
| <a href="Modding_Modder_Guide_APIs_Data" class="wikilink"
title="Data">Data</a> | Store arbitrary data and retrieve it later. |
| <a href="Modding_Modder_Guide_APIs_Input" class="wikilink"
title="Input">Input</a> | Check and suppress keyboard, controller, and mouse state. |
| <a href="Modding_Modder_Guide_APIs_Logging" class="wikilink"
title="Logging">Logging</a> | Write messages to the SMAPI console and log. |
| <a href="Modding_Modder_Guide_APIs_Reflection" class="wikilink"
title="Reflection">Reflection</a> | Access fields, properties, or methods which are normally inaccessible. |
| <a href="Modding_Modder_Guide_APIs_Multiplayer" class="wikilink"
title="Multiplayer">Multiplayer</a> | Provides methods for supporting multiplayer. |
| <a href="Modding_Modder_Guide_APIs_Translation" class="wikilink"
title="Translation">Translation</a> | Translate your mod text into any game language. |
| <a href="Modding_Modder_Guide_APIs_Utilities" class="wikilink"
title="Utilities">Utilities</a> | Use constants, contextual information, date logic, and semantic versions. |

## Advanced APIs

| page | summary |
|----|----|
| <a href="Modding_Modder_Guide_APIs_Content_Packs" class="wikilink"
title="Content packs">Content packs</a> | Let other modders provide files for your mod to read, which players can install like any other mod. |
| <a href="Modding_Modder_Guide_APIs_Console" class="wikilink"
title="Console commands">Console commands</a> | Add custom commands to the SMAPI console. |
| <a href="Modding_Modder_Guide_APIs_Integrations" class="wikilink"
title="Mod integrations">Mod integrations</a> | Get information about loaded mods, and integrate with mods using mod-provided APIs. |
| <a href="Modding_Modder_Guide_APIs_Harmony" class="wikilink"
title="Harmony patching">Harmony patching</a> | Harmony lets you patch or replace methods, effectively rewriting the game code. |

<a href="es_Modding_Guía_del_Modder_APIs" class="wikilink"
title="es:Modding:Guía del Modder/APIs">es:Modding:Guía del
Modder/APIs</a>
<a href="ru_Модификации_Руководство_мододела_API" class="wikilink"
title="ru:Модификации:Руководство мододела/API">ru:Модификации:Руководство
мододела/API</a>
<a href="tr_Modlama_Mod_Rehberi_API&#39;ler" class="wikilink"
title="tr:Modlama:Mod Rehberi/API&#39;ler">tr:Modlama:Mod
Rehberi/API'ler</a> <a href="zh_模组_制作指南_APIs" class="wikilink"
title="zh:模组:制作指南/APIs">zh:模组:制作指南/APIs</a>
