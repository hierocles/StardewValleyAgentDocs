---
title: "Overview"
wiki_source: "Modding:Content packs"
permalink: /Modding:Content_packs/
category: content-packs
tags: [content-packs, for-players, for-modders, create-a-content-pack, release-your-content-pack, consume-a-content-pack, conventions, folder-name]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

A **content pack** is a collection of files loaded by a specific
<a href="Modding_Content_pack_frameworks" class="wikilink"
title="content pack framework">content pack framework</a> (essentially a
sub-mod). Content packs can contain any files, but usually consist of
JSON files and images.

## For players

If you want to use a content pack, install it just like a SMAPI mod (see
<a href="Modding_Player_Guide_Getting_Started" class="wikilink"
title="player guide">player guide</a>). Make sure you install the mod it
needs too.

## For modders

### Create a content pack

1.  Decide which
    <a href="Modding_Content_pack_frameworks" class="wikilink"
    title="content pack framework">content pack framework</a> you'll use
    (each framework defines the particular files you need).
2.  <a href="Modding_Player_Guide_Getting_Started#Getting_started"
    class="wikilink" title="Install SMAPI">Install SMAPI</a>.
3.  Create the generic content pack format (identical for all
    frameworks):
    1.  Open your game's `Mods` folder (located in
        <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
        class="wikilink" title="your game folder">your game folder</a>).
    2.  Add a subfolder with the name you want (see
        <a href="#Folder_name" class="wikilink"
        title="folder naming convention">folder naming convention</a>).
    3.  In the subfolder, add a `manifest.json` file with the
        `ContentPackFor` field (see
        <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
        title="manifest examples and format">manifest examples and format</a>).
4.  Add the files needed by the content pack framework (see its mod page
    for details).
5.  Launch the game, and make sure your new content pack appears under
    "Loaded X content packs" in the SMAPI console.

### Release your content pack

1.  Add an <a href="Modding_Modder_Guide_APIs_Manifest#Update_checks"
    class="wikilink" title="update key">update key</a> to your manifest
    (if you haven't already).
2.  Update the `Version` field in the manifest. (Increase it for each
    release! SMAPI will use it for update and compatibility checks.)
3.  Create a `.zip` file containing the content pack's folder.
4.  Upload that file to [Nexus
    Mods](http://www.nexusmods.com/stardewvalley).

In your mod description, providing clear install steps will help reduce
support questions. Example BBCode:

    [size=5]Install[/size]
    [list=1]
    [*][url=https://smapi.io]Install the latest version of SMAPI[/url].
    [*][url=<url of required mod>]Install <name of required mod>[/url].
    [*]Download this mod and unzip it into [font=Courier New]Stardew Valley/Mods[/font].
    [*]Run the game using SMAPI.
    [/list]

### Consume a content pack

If you're writing a SMAPI mod which will read content packs, see
<a href="Modding_Modder_Guide_APIs_Content_Packs" class="wikilink"
title="Modding:Modder Guide/APIs/Content Packs">Modding:Modder
Guide/APIs/Content Packs</a>.

## Conventions

These are recommended practices, but they're not required.

### Folder name

The folder name should use
<a href="wikipedia_Camel_case" class="wikilink"
title="upper camel case">upper camel case</a>, with an acroynm prefix in
square brackets showing which mod it's for. For example, a folder named
`[CP] SampleName` is a content pack for Content Patcher.

See <a href="Modding_Content_pack_frameworks" class="wikilink"
title="Modding:Content pack frameworks">Modding:Content pack
frameworks</a> for the common acronyms.

### Folder structure

The folder should contain your `manifest.json`, the `content.json` (or
the correct json for your framework), and an `assets` folder that
contains any other files your mod uses. This may include `.png` files,
other `.json` files, and even or `.tmx/.tbin` files, among others. The
assets folder may use further subfolders if you wish, though it is not
required.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="pt_Modificações_Pacotes_de_conteúdo" class="wikilink"
title="pt:Modificações:Pacotes de conteúdo">pt:Modificações:Pacotes de
conteúdo</a> <a href="ru_Модификации_Контент-паки" class="wikilink"
title="ru:Модификации:Контент-паки">ru:Модификации:Контент-паки</a>
<a href="zh_模组_内容包" class="wikilink"
title="zh:模组:内容包">zh:模组:内容包</a>
