---
title: "Content Packs Api"
wiki_source: "Modding:Modder Guide/APIs/Content Packs"
permalink: /Modding:Modder_Guide/APIs/Content_Packs/
category: smapi
tags: [content-packs, content-pack-format, content-pack-api, get-owned-content-packs, check-if-a-file-exists, read-a-json-file, write-a-json-file, read-content-asset]
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

A **content pack** is a special type of mod that isn't run by SMAPI
directly, but contains files your own mod can read.

Note that a custom content pack format is not required to provide
integration with content mods; the most common method is to provide a
<a href="Modding_Modder_Guide_APIs_Content#Add_a_new_asset"
class="wikilink" title="custom game asset">custom game asset</a> that
other mods (including Content Patcher packs) can edit. The advantage of
custom assets is that both other C# mods and Content Patcher packs can
edit them via the content pipeline, with the latter benefiting from
convenient features such as tokens, conditional loading and targeted
edits, removing the need to implement similar features in your mod.

See the wiki page for
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="loading and editing content">loading and editing content</a>, as
well as the external tutorial for [making framework
mods](https://stardewmodding.wiki.gg/wiki/Tutorial:_Making_Framework_Mods)
for more info. The rest of this page details instructions for defining
custom content packs formats.

## Content pack format

A content pack is a folder containing a `manifest.json` file which
specifies your mod in its `ContentPackFor` field (see
<a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
title="manifest">manifest</a>). The format beyond that is up to you to
define. For example, requires a `content.json` file, but that's not
validated by SMAPI itself. Instead, SMAPI provides an API you can use to
read any other file you need from the content pack.

See <a href="Modding_Content_packs" class="wikilink"
title="Modding:Content packs">Modding:Content packs</a> for more info
about content packs.

## Content pack API

### Get owned content packs

To get the content packs installed for your mod (including a `Manifest`
field with the content pack's
<a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
title="full manifest info">full manifest info</a>):

``` c#
foreach(IContentPack contentPack in this.Helper.ContentPacks.GetOwned())
{
   this.Monitor.Log($"Reading content pack: {contentPack.Manifest.Name} {contentPack.Manifest.Version} from {contentPack.DirectoryPath}");
}
```

Content packs are listed in load order, so they're already sorted for
dependencies. For example, if content pack B requires A, they'll be
listed in the order A → B.

As a note, this can be done as early as ModEntry, although mods often
choose to perform this step in the GameLoad or SaveLoaded event.

### Check if a file exists

You can check if a file exists in the content pack folder using
`HasFile`. You can specify a relative path like `data/content.json`.

``` c#
if (!contentPack.HasFile("content.json"))
{
   // show 'required file missing' error
}
```

It is often a good idea to alert the player (and modders who may be
using your mod) if the file is missing on deployment.

### Read a JSON file

You can read a JSON file from a content pack folder into
<a href="Modding_Modder_Guide_APIs_Data#Data_model" class="wikilink"
title="a data model">a data model</a> (`YourDataModel` in the example
below) using `ReadJsonFile`. You can specify a relative path like
`data/content.json`. This will return `null` if the file doesn't exist.

``` c#
YourDataModel data = contentPack.ReadJsonFile<YourDataFile>("content.json");
```

### Write a JSON file

You can write a JSON file in a content pack folder using
`WriteJsonFile`, using a
<a href="Modding_Modder_Guide_APIs_Data#Data_model" class="wikilink"
title="data model">data model</a> (`YourDataModel` in the example
below). You can specify a relative path like `data/content.json`
(subdirectories will be created automatically if needed). This will
create the file if it doesn't exist, or overwrite it if it does.

**Note:** this is best used for generated files. Overwriting the
original files isn't recommended, since a bug in your mod which changes
an original file might permanently break the content pack and require
the player to reinstall it.

``` c#
YourDataModel data = new YourDataModel();
contentPack.WriteJsonFile("content.json", data);
```

### Read content asset

You can read
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="a content asset">a content asset</a> from the content pack folder
using `LoadAsset`. You can optionally specify a relative path to read
from a subfolder.

``` c#
Texture2D image = contentPack.ModContent.Load<Texture2D>("image.png");
```

If you need to pass an asset name to game code, you can use the
`GetActualAssetKey` method:

``` c#
tilesheet.ImageSource = contentPack.GetActualAssetKey("image.png");
```

### Get translations

You can read translations from the content pack's `i18n` folder. This is
identical to the
<a href="Modding_Modder_Guide_APIs_Translation" class="wikilink"
title="translation API">translation API</a>, but accessed through
`contentPack.Translations`:

``` c#
string text = contentPack.Translation.Get("item-type.label");
```

### Create a fake content pack

In specialised cases, you can create a temporary content pack for a
given directory path:

``` c#
// create with random manifest data
IContentPack contentPack = this.Helper.ContentPacks.CreateFake(
   directoryPath: Path.Combine(this.Helper.DirectoryPath, "content-pack"),
);

// create with given manifest fields
IContentPack contentPack = this.Helper.ContentPacks.CreateTemporary(
   directoryPath: Path.Combine(this.Helper.DirectoryPath, "content-pack"),
   id: Guid.NewGuid().ToString("N"),
   name: "temporary content pack",
   description: "...",
   author: "...",
   version: new SemanticVersion(1, 0, 0)
);
```

<a href="ru_Модификации_Руководство_мододела_API_Контент-паки"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Контент-паки">ru:Модификации:Руководство
мододела/API/Контент-паки</a>
<a href="zh_模组_制作指南_APIs_Content_Packs" class="wikilink"
title="zh:模组:制作指南/APIs/Content Packs">zh:模组:制作指南/APIs/Content
Packs</a>
