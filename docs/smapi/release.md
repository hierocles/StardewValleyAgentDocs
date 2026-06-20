---
title: "Release"
wiki_source: "Modding:Modder Guide/Release"
permalink: /Modding:Modder_Guide/Release/
category: smapi
tags: [release, prepare-the-release-package, for-smapi-mods, for-content-pack-mods, release-the-mod, using-nexus-mods, using-moddrop, go-open-source]
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

Once you're ready to share your mod, it's time to release it!

## Prepare the release package

### For SMAPI mods

The 'release package' for a SMAPI mod is just a `.zip` file containing a
mod with your compiled files, `manifest.json`, any `i18n` files, etc.
The NuGet package will create it for you automatically.

#### Generate package

1.  Edit your mod's `manifest.json` to increase the version. See
    [semantic version](http://semver.org/) for more information on
    version numbering.
2.  Click *Build \> Rebuild Solution* (Visual Studio) or *Build \>
    Rebuild All* (MonoDevelop) to make sure the project is compiled.
3.  Open your mod project's `bin/Debug` or `bin/Release` folder
    (depending on your build configuration).
4.  There should be a `.zip` file there for your mod version.

That `.zip` file is the release package for your mod, ready to upload.

#### Troubleshoot package

Here's how to fix common issues with the generated `.zip` file.

- The `.zip` file is missing:
  - Make sure you're looking at the right folder (either `bin/Debug` or
    `bin/Release`).
  - Make sure there are no build errors.

<!-- -->

- Some mod files aren't in the package:
  - If it's a mod file: right-click on the file in Visual Studio or
    MonoDevelop, choose *Properties*, and change 'Copy to Output
    Directory' to 'copy if newer'.
  - If it's an assembly reference: right-click on the reference in
    Visual Studio or MonoDevelop, choose *Properties*, and change 'Copy
    Local' or 'Local Copy' to true.

<!-- -->

- Some mod files that shouldn't be in the package are included:
  - If it's a mod file: right-click on the file in Visual Studio or
    MonoDevelop, choose *Properties*, and change 'Copy to Output
    Directory' to 'do not copy'.
  - If it's an assembly reference: right-click on the reference in
    Visual Studio or MonoDevelop, choose *Properties*, and change 'Copy
    Local' or 'Local Copy' to false.

### For content pack mods

The 'release package' for a content pack mod is just a `.zip` file
containing a mod with your files, which must include at least a
`manifest.json` and a `content.json`. See the specific guidelines for
your framework mod that you are using.

#### Create a content pack

1.  Create a folder with the name you want (see
    <a href="Modding_Content_packs#Folder_name" class="wikilink"
    title="folder naming convention">folder naming convention</a>).
2.  Inside the folder:
    - Add a `manifest.json` file with the `ContentPackFor` field (see
      <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
      title="manifest format">manifest format</a>).
    - Add the files needed by the mod that will read it. (See the
      instructions for the mod for which you're creating the content
      pack.)
3.  Launch the game, and make sure your new content pack appears under
    "Loaded X content packs" in the SMAPI console.

#### Release your content pack

1.  Add an <a href="Modding_Modder_Guide_APIs_Manifest#Update_checks"
    class="wikilink" title="update key">update key</a> to your manifest
    (if you haven't already).
2.  Update the `Version` field in the manifest. (Increase it for each
    release! SMAPI will use it for update and compatibility checks.) See
    [semantic version](http://semver.org/) for more information on
    version numbering.
3.  Create a `.zip` file containing the content pack's folder.
4.  Upload that file to your chosen release site. See below guide to
    sites.

## Release the mod

### Using Nexus Mods

#### Create a mod page

If you haven't already, create a mod page on [Nexus
Mods](http://www.nexusmods.com/stardewvalley). Ideally your mod
description should...

- explain what the mod does and how to use it;
- provide clear install steps;
- explain which version of the game it works with;
- say whether it works in multiplayer (and list any multiplayer
  limitations);
- link to release notes, source code, discussion thread, etc if
  applicable.

Here's a recommended template for the mod description:

1.  Click the "\[BBCODE\]" button above the mod description on Nexus.
    This will switch to raw text mode.
2.  Paste this template in:
        This mod adds pineapples everywhere in the game. Replace this line with a few sentences explaining your mod.

        [size=5]Install[/size]
        [list=1]
        [*][url=https://smapi.io]Install the latest version of SMAPI[/url].
        [*]Download this mod and unzip it into [font=Courier New]Stardew Valley/Mods[/font].
        [*]Run the game using SMAPI.
        [/list]

        [size=5]How to use[/size]
        Provide a few sentences explaining how to use your mod. For example, the default buttons to press, where to find a menu, etc. You can remove this section if it's self-evident.

        [size=5]Compatibility[/size]
        [list]
        [*]Works with Stardew Valley 1.5.6 on Linux/macOS/Windows.
        [*]Works in single player, multiplayer, and split-screen mode. If there are multiplayer limitations, explain them here.
        [/list]

        [size=5]See also[/size]
        Add links below for your mod, and remove any that don't apply. Don't forget to remove this sentence.

        [list]
        [*]Official discussion thread
        [*]Release notes
        [*]Source code
        [/list]
3.  Click the "\[BBCODE\]" button to switch back to the formatted view.
4.  Edit the template for your mod.

#### Add update keys to your manifest

Update keys tell SMAPI where your mod is released, so it can let players
know when a new version is available. This requires your mod ID, which
is available as soon as you create the mod page (before uploading the
mod files). See the
<a href="Modding_Modder_Guide_APIs_Manifest#Update_checks"
class="wikilink" title="update check docs">update check docs</a> for
more info.

#### Upload the mod release

<a href="File_Modding_-_Nexus_new-file_screen.png" class="wikilink"
title="thumb">thumb</a>

To upload a file to Nexus:

1.  From your mod page, go to *Manage \> Files*.
2.  Fill in the form:
    - 'File name' should have the mod name and version (like
      `PineapplesEverywhere 1.0`).
    - 'File version' field should match the version in your
      `manifest.json`! If it doesn't, players may get incorrect update
      alerts.
    - Tick the "this is the latest version" checkbox so players get
      update alerts.
    - 'File description' is up to you. You can mention the minimum SMAPI
      version (if any), what changed, link to release notes, etc.
3.  Upload the `.zip` file
    <a href="#Prepare_the_release_package" class="wikilink"
    title="you prepared above">you prepared above</a>.

### Using ModDrop

ModDrop used to be an alternative location to host your mods. However,
**as of February 2026 ModDrop appears to be unmoderated and potentially
unsafe**. Mod Developers should, however, monitor ModDrop for stolen
rereleases of their mods.

#### Release via webpage

1.  Go to [*ModDrop*](https://www.moddrop.com/stardew-valley/) and
    choose `Upload Your Mod`.
2.  Confirm that the mod is yours to publish to proceed.
3.  Choose `Upload a File from Your Computer`.
4.  Choose a name for your mod and upload the `.zip` file
    <a href="#Prepare_the_release_package" class="wikilink"
    title="you prepared above">you prepared above</a>. Page will display
    a green check next to the mod name if that name is available to use.
5.  Choose the name of the mod file you want to display, the version
    number, release status (alpha, beta, release), add a description
    (<a href="Modding_Modder_Guide_Release#Create_a_mod_page"
    class="wikilink" title="see the Nexus description tips">see the Nexus
    description tips</a>), and optionally add patch notes or notes for
    yourself.
6.  Upload an image for your mod.
7.  You'll now have a chance to create a more detailed mod page,
    including links to other pages where your mod can be found. You may
    also add more files, images, videos, and notices to be displayed to
    users. You can also choose a category for your mod. If you are
    uploading on someone else's behalf (with permission), there is also
    a section to provide credit.
8.  Confirm again that you have permission to upload the mod to publish.
    You may cancel out of this page and resume at a later time.

#### Release via app

1.  Open [*ModDrop app*](https://www.moddrop.com/app/) and click on your
    username (top right corner). Choose `Forge`.
2.  Choose `Publish a new mod`.
3.  Follow the same steps as listed above for the site.

#### Sync Nexus mods to ModDrop

1.  Open [*ModDrop app*](https://www.moddrop.com/app/) and click on your
    username (top right corner). Choose `Forge`.
2.  Choose `Sync my mods from another site`.
3.  Follow the prompts to add your Nexus API key.
4.  Choose `Find new mods to sync` and follow the prompts.
5.  Confirm that the mod is yours to publish and that ModDrop is allowed
    to sync updates from your Nexus account.
6.  You will receive a confirmation that the request is complete.
    ModDrop reviews all submissions, so it may take some time for your
    mod to appear on the app/site.

#### Add update keys to your manifest

Update keys tell SMAPI where your mod is released, so it can let players
know when a new version is available. This requires your mod ID, which
can be found after creating the mod page. See the
<a href="Modding_Modder_Guide_APIs_Manifest#Update_checks"
class="wikilink" title="update check docs">update check docs</a> for
more info.

## Go open-source

Making your mods open-source is highly recommended; see
<a href="Modding_Open_source" class="wikilink"
title="Modding:Open source">Modding:Open source</a> for more info.

<a href="es_Modding_Guía_del_Modder_Lanzamiento" class="wikilink"
title="es:Modding:Guía del Modder/Lanzamiento">es:Modding:Guía del
Modder/Lanzamiento</a>
<a href="ru_Модификации_Руководство_мододела_Публикация"
class="wikilink"
title="ru:Модификации:Руководство мододела/Публикация">ru:Модификации:Руководство
мододела/Публикация</a> <a href="zh_模组_制作指南_发布" class="wikilink"
title="zh:模组:制作指南/发布">zh:模组:制作指南/发布</a>
