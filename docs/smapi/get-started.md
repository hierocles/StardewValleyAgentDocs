---
title: "Get Started"
wiki_source: "Modding:Modder Guide/Get Started"
permalink: /Modding:Modder_Guide/Get_Started/
category: smapi
tags: [get-started, intro, what-is-a-smapi-mod, why-do-mods-use-smapi, can-i-make-a-mod, can-i-make-a-mod-without-smapi, where-can-i-get-help, learn-c]
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

**If you're making a mod for the first time,** see
<a href="Modding_Index#Creating_mods" class="wikilink"
title="Modding:Index#Creating mods">Modding:Index#Creating mods</a> for
a short description of the differences between C# mods and content
packs. **You can create many mods without C#.**

Do you want to create **SMAPI mods for Stardew Valley with C#?** This
guide is for you!

## Intro

### What is a SMAPI mod?

A SMAPI mod uses the [SMAPI](https://smapi.io/) modding API to extend
the game logic. The mod can respond when something happens in the game
(like when an object is placed in the world), run code periodically
(like once per update tick), change the game's assets and data, etc.
SMAPI mods are written in C# using .NET, and Stardew Valley uses
MonoGame for the game logic (drawing to the screen, user input, etc).

### Why do mods use SMAPI?

SMAPI does a lot for you! For example, SMAPI will...

1.  Load your mod into the game. Code mods aren't possible without SMAPI
    to load them.
2.  Provide APIs and events which let you interact with the game in ways
    you otherwise couldn't. There are simplified APIs for game
    asset/data changes, player configuration, translation, reflection,
    etc. These are covered later in the guide.
3.  Rewrite your mod for crossplatform compatibility when it's loaded.
    That lets you write mod code without worrying about the differences
    between the Linux/Mac/Windows versions of the game.
4.  Rewrite your mod to update it. SMAPI detects and fixes mod code
    broken by a game update in common cases.
5.  Intercept errors. If your mod crashes or causes an error, SMAPI will
    intercept the error, show the error details in the console window,
    and in most cases automatically recover the game. This means your
    mod won't accidentally crash the game, and it makes it much easier
    to troubleshoot errors.
6.  Provide update checks. SMAPI automatically alerts players when a new
    version of your mod is available.
7.  Provide compatibility checks. SMAPI automatically detects when your
    mod is incompatible and disables it before it causes problems, so
    players aren't left with broken games.

### Can I make a mod?

Yes! This guide will help you create a simple mod step-by-step. If you
follow along, you'll have created a mod! Then you'll just need to make
it do what you want.

If you're new to programming: many mod developers start with little or
no programming experience. You can certainly learn along the way if
you're determined, but you should be prepared for a steep learning
curve. Don't be too ambitious at first; it's better to start with a
small mod when you're figuring it out. It's easy to become overwhelmed
at first and give up. The modding community is very welcoming, so don't
be afraid to ask questions!

If you already have programming experience, you should be fine.
Programming experience in C# or Java will make things easier, but it
isn't critical. If you're unfamiliar with C#, you can skim through the
*Learning C#* references below to fill in any gaps.

### Can I make a mod *without SMAPI*?

Yep. Many SMAPI mods support
'<a href="Modding_Content_packs" class="wikilink"
title="content packs">content packs</a>', which let you provide JSON
text files, images, etc which they use. For example, you can
<a href="Modding_Content_Patcher" class="wikilink"
title="use Content Patcher">use Content Patcher</a> to edit the game's
images and data with zero programming needed. The rest of this guide is
about creating a new SMAPI mod; for content packs, see
<a href="Modding_Content_Patcher" class="wikilink"
title="Modding:Content Patcher">Modding:Content Patcher</a> or
<a href="Modding_Content_pack_frameworks" class="wikilink"
title="Modding:Content pack frameworks">Modding:Content pack
frameworks</a> for information on other available frameworks (or the mod
documentation if creating a content pack for a different mod).

### Where can I get help?

<span id="help"></span>The Stardew Valley modding community is very
welcoming. Feel free to ask for help in
<a href="Modding_Community#Discord" class="wikilink"
title="#making-mods on the Stardew Valley Discord">#making-mods on the
Stardew Valley Discord</a>.

## Get started

### Learn C#

Since mods are written in C#, it's a good idea to get acquainted with it
first. You don't need to memorise everything, but a grasp of the basics
(like fields, methods, variables, and classes) will make everything else
much easier.

Some useful resources:

- [*C#
  Quickstarts*](https://docs.microsoft.com/en-us/dotnet/csharp/quick-starts/)
  teaches the basics of C# with interactive examples.
- [*C# Fundamentals for Absolute
  Beginners*](https://mva.microsoft.com/en-us/training-courses/c-fundamentals-for-absolute-beginners-16169)
  is a video guide which will walk you through C#, from the basic
  concepts to event-driven programming (which is what SMAPI mods mostly
  use).
- Already know how to program? Get a quick overview of C# syntax and
  concepts at
  [LearnXinYMinutes.](https://learnxinyminutes.com/docs/csharp/)

A couple of concepts SMAPI uses frequently

- [*Generics*](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics)
- [*Event-based
  programming*](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/events/)
- For serialization, SMAPI usually uses
  [*NewtonSoft*](https://www.newtonsoft.com/json)

### Requirements

Before you start:

1.  Read the
    <a href="Modding_Player_Guide_Getting_Started" class="wikilink"
    title="player guide">player guide</a>. The rest of this guide
    assumes you're already familiar with using mods.
2.  Install Stardew Valley.
3.  Install <a href="Modding_Player_Guide_Getting_Started#Install_SMAPI"
    class="wikilink" title="SMAPI">SMAPI</a>.
4.  Install the [.NET 6
    SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).\
    *You need .NET 6 because it's the version used by the game. On
    Windows, you probably have x64. on macOS, "x64" is for Intel chips
    and "Arm64" is for Apple Silicon chips.*
5.  Install the IDE (*integrated development environment*), which you'll
    use to edit and compile your mod code:
    - Windows: [Visual Studio
      Community](https://visualstudio.microsoft.com/vs/community/)
      (free) or [JetBrains Rider](https://www.jetbrains.com/rider/)
      (free).
    - Linux/macOS: [JetBrains Rider](https://www.jetbrains.com/rider/)
      (free) or [Visual Studio Code](https://code.visualstudio.com/)
      (free).

If you're not familiar with Visual Studio (on Windows),
<a href="Modding_IDE_reference" class="wikilink"
title="Modding:IDE reference">Modding:IDE reference</a> explains how to
do the important stuff you need for this guide.

## Create a basic mod

### Quick start

If you're experienced enough to skip the tutorial, here's a quick
summary of this section:

### Create the project

A SMAPI mod is a compiled library (DLL) with an entry method that gets
called by SMAPI, so let's set that up.

1.  Open Visual Studio or MonoDevelop.
2.  Create a solution with a *Class Library* project (see
    <a href="Modding_IDE_reference#create-project" class="wikilink"
    title="how to create a project">how to create a project</a>). (Don't
    select *Class Library (.NET Framework)*! That's a separate thing
    with a similar name.)
3.  Target .NET 6 (see
    <a href="Modding_IDE_reference#set-target-framework" class="wikilink"
    title="how to change target framework">how to change target
    framework</a>).You may need to [install the
    SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).\
    <small>That's the version installed and used by the game. Newer
    versions may not be installed for players, and SMAPI may not be able
    to load them.
    <a href="#What_does_&quot;target_NET_6.0&quot;_mean?" class="wikilink"
    title="Yes we know it&#39;s EOL">Yes we know it's EOL</a>.</small>
4.  Reference the [`Pathoschild.Stardew.ModBuildConfig` NuGet
    package](https://www.nuget.org/packages/Pathoschild.Stardew.ModBuildConfig)
    (see <a href="Modding_IDE_reference#add-nuget" class="wikilink"
    title="how to add the package">how to add the package</a>).
    - If you are getting an error stating *The type or namespace name
      "StardewModdingAPI" could not be found*, then it's possible that
      your game path is not being detected. You will need to set the
      GamePath property to the game's executable directory. This can be
      done by adding a *GamePath* property to the *PropertyGroup* in
      your *.csproj* settings.
5.  Restart Visual Studio/MonoDevelop after installing the package.

### Add the code

Next let's add some code SMAPI will run.

1.  Delete the `Class1.cs` or `MyClass.cs` file (see
    <a href="Modding_IDE_reference#delete-file" class="wikilink"
    title="how to delete a file">how to delete a file</a>).
2.  Add a C# class file called `ModEntry.cs` to your project (see
    <a href="Modding_IDE_reference#Add_a_file" class="wikilink"
    title="how to add a file">how to add a file</a>).
3.  Put this code in the file (replace `YourProjectName` with the name
    of your project):
    ``` c#
    using System;
    using Microsoft.Xna.Framework;
    using StardewModdingAPI;
    using StardewModdingAPI.Events;
    using StardewModdingAPI.Utilities;
    using StardewValley;

    namespace YourProjectName
    {
        /// <summary>The mod entry point.</summary>
        internal sealed class ModEntry : Mod
        {
            /*********
            ** Public methods
            *********/
            /// <summary>The mod entry point, called after the mod is first loaded.</summary>
            /// <param name="helper">Provides simplified APIs for writing mods.</param>
            public override void Entry(IModHelper helper)
            {
                helper.Events.Input.ButtonPressed += this.OnButtonPressed;
            }

            /*********
            ** Private methods
            *********/
            /// <summary>Raised after the player presses a button on the keyboard, controller, or mouse.</summary>
            /// <param name="sender">The event sender.</param>
            /// <param name="e">The event data.</param>
            private void OnButtonPressed(object? sender, ButtonPressedEventArgs e)
            {
                // ignore if player hasn't loaded a save yet
                if (!Context.IsWorldReady)
                    return;

                // print button presses to the console window
                this.Monitor.Log($"{Game1.player.Name} pressed {e.Button}.", LogLevel.Debug);
            }
        }
    }
    ```

Here's a breakdown of what that code is doing:

1.  `using X;` (see [using
    directive](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive))
    makes classes in that namespace available in your code.
2.  `namespace YourProjectName` (see [namespace
    keyword](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/namespace))
    defines the scope for your mod code. Don't worry about this when
    you're starting out, Visual Studio or MonoDevelop will add it
    automatically when you add a file.
3.  `public class ModEntry : Mod` (see [class
    keyword](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/class))
    creates your mod's main class, and subclasses SMAPI's `Mod` class.
    SMAPI will detect your `Mod` subclass automatically, and `Mod` gives
    you access to SMAPI's APIs.
4.  `public override void Entry(IModHelper helper)` is the method SMAPI
    will call when your mod is loaded into the game. The `helper`
    provides convenient access to many of SMAPI's APIs.
5.  `helper.Events.Input.ButtonPressed += this.OnButtonPressed;` adds an
    'event handler' (*i.e.,* a method to call) when the button-pressed
    event happens. In other words, when a button is pressed (the
    `helper.Events.Input.ButtonPressed` event), SMAPI will call your
    `this.OnButtonPressed` method. See
    <a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
    title="events in the SMAPI reference">events in the SMAPI reference</a>
    for more info.

Note: if you get compile errors along the lines of "Feature XX is not
available in C# \<number\>. Please use language version \<number\> or
greater", add `<LangVersion>Latest</LangVersion>` to your `.csproj`.

### Add your manifest

The mod manifest tells SMAPI about your mod.

1.  Add a file named `manifest.json` to your project.
2.  Paste this code into the file:
    ``` json
    {
      "Name": "<your project name>",
      "Author": "<your name>",
      "Version": "1.0.0",
      "Description": "<One or two sentences about the mod>",
      "UniqueID": "<your name>.<your project name>",
      "EntryDll": "<your project name>.dll",
      "MinimumApiVersion": "4.0.0",
      "UpdateKeys": []
    }
    ```
3.  Replace the `<...>` placeholders with the correct info. Don't leave
    any `<>` symbols!

This will be listed in the console output when the game is launching.
For more info, see the
<a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
title="manifest docs">manifest docs</a>.

### Try your mod

1.  Build the project.\
    <small>If you did the
    *<a href="#Create_the_project" class="wikilink"
    title="create the project">create the project</a>* steps correctly,
    this will automatically add your mod to the game's `Mods`
    folder.</small>
2.  Run the game through SMAPI.

The mod so far will just send a message to the console window whenever
you press a key in the game.

**Changing console text color**

The default text-colors in the console may be set in a way that makes
them unreadable. To change text color:

- **Steam**: Open Steam and right-click the game in your library. Click
  "Browse local files" under "Manage" and then open the `config.json`
  file in your "/Stardew Valley/smapi-internal/" folder, search for
  "ConsoleColors" and then edit the "Trace" and "Debug" colors so that
  they become visible within your console.

<!-- -->

- **Linux**: The default path on linux is
  `~/.local/share/Steam/steamapps/common/Stardew Valley/smapi-internal/config.json`,
  unless you have installed your game on a different drive/outside the
  standard steam library folder.

<!-- -->

- **Windows**: The default path on Windows should be "C:\Program files
  (x86)\Steam\steamapps\common\Stardew
  Valley\smapi-internal\config.json", unless you have installed your
  game on a different drive/outside the standard steam library folder.

### Troubleshoot

If the tutorial mod doesn't work...

1.  Review the above steps to make sure you didn't skip something.
2.  Check for error messages which may explain why it's not working:
    - In Visual Studio, click *Build \> Rebuild Solution* and check the
      *Output* pane or *Error* list.
    - In MonoDevelop, click *Build \> Rebuild All* and wait until it's
      done. Then click the "Build: XX errors, XX warnings" bar at the
      top, and check the *XX Errors* and *Build Output* tabs.
3.  If one of the errors (not necessarily the first one) says the
    package can't find your game folder, see <a
    href="Modding_Modder_Guide_Test_and_Troubleshoot#Visual_Studio_can&#39;t_find_the_game_SMAPI_MonoGame_DLLs"
    class="wikilink"
    title="Visual Studio can&#39;t find the game/SMAPI/MonoGame DLLs"><em>Visual
    Studio can't find the game/SMAPI/MonoGame DLLs</em></a>.
4.  See the
    <a href="Modding_Modder_Guide_Test_and_Troubleshoot" class="wikilink"
    title="troubleshooting guide">troubleshooting guide</a>.
5.  If all else fails, come ask for help in the
    <a href="Modding_Community#Discord" class="wikilink"
    title="#making-mods in the Stardew Valley Discord">#making-mods in the
    Stardew Valley Discord</a>. :)

## FAQs

### Where's the SMAPI documentation?

This is just the 'getting started' tutorial. For more documentation, see
the <a href="Modding_Modder_Guide_APIs" class="wikilink"
title="SMAPI reference">SMAPI reference</a> and the
<a href="Modding_Index" class="wikilink"
title="topics listed on the index page">topics listed on the index
page</a>.

### Can I look at other mods' code?

Yep, nearly 70% of SMAPI mods have public source code. To find their
code:

1.  Open the [mod compatibility page](https://smapi.io/mods/).
2.  Click "show advanced info" under the search box.
3.  Look in the "code" column for links.

### How do I make my mod work crossplatform?

SMAPI will automatically adjust your mod so it works on Linux, MacOS,
and Windows. However, there are a few things you should do to avoid
problems:

1.  Use the [crossplatform build
    config](https://smapi.io/package/readme) package to automatically
    set up your project references. This makes crossplatform
    compatibility easier and lets your code compile on any platform. (If
    you followed the above guide, you already have this.)
2.  Use `System.IO.Path.Combine` to build file paths, don't hardcode
    path separators since they won't work on all platforms.
    ``` c#
    // ✘ Don't do this! It won't work on SteamDeck/Linux/Mac.
    string path = this.Helper.DirectoryPath + "\\assets\\image.png";

    // ✓ This is OK
    string path = Path.Combine(this.Helper.DirectoryPath, "assets", "image.png");
    ```
3.  Use `this.Helper.DirectoryPath`, don't try to determine the mod path
    yourself.
    ``` c#
    // ✘ Don't do this! It will crash if SMAPI rewrites the assembly (''e.g.,'' to update or crossplatform it).
    string modFolder = Assembly.GetCallingAssembly().Location;

    // ✓ This is OK
    string modFolder = this.Helper.DirectoryPath;
    ```
4.  An *asset name* identifies an asset you can load through a content
    API like `Game1.content.Load<T>("asset name")`. This is *not* a file
    path, and the asset name format doesn't always match the file path
    format. When comparing asset names, make sure you use
    `PathUtilities.NormalizeAssetName("some/path")` instead of path
    helpers.
    ``` c#
    // ✘ Don't do this! It won't work on Windows.
    bool isAbigail = (asset.Name == Path.Combine("Characters", "Abigail"));
    bool isAbigail2 = (asset.Name == PathUtilities.NormalizePath("Characters", "Abigail"));

    // ✓ This is OK
    bool isAbigail = (asset.Name == PathUtilities.NormalizeAssetName("Characters", "Abigail"));
    ```

    Note that there's no need to normalize asset names you pass into
    SMAPI APIs, which normalize them automatically (though it doesn't
    hurt to do it anyway):

    ``` c#
    // ✓ This is OK
    helper.Content.Load<Texture2D>("Characters/Abigail");
    helper.Content.Load<Texture2D>(@"Characters\\Abigail");
    ```

### How do I decompile the game code?<span id="decompile"></span>

It's often useful to see how the game code works. The game code is
compiled into `StardewValley.dll` (*i.e.,* converted to a
machine-readable format), but you can decompile it get a mostly-readable
approximation of the original code. (This might not be fully functional
due to decompiler limitations, but you'll be able to see what it's
doing.)

To decompile the game code...

:# First-time setup:

:## Install for Windows (get the "ILSpy_binaries" file under assets), or
[Avalonia ILSpy](https://github.com/icsharpcode/AvaloniaILSpy/releases)
for Linux and macOS.

:## Open ILSpy.

:## Click *View \> Options*, scroll to the "Other" section at the
bottom, and enable "Always qualify member references".

:# Open `Stardew Valley.dll` in ILSpy.

:# Make sure *C#* is selected in the language drop-down (not IL, IL with
C#, or ReadyToRun).

:# Right-click on *Stardew Valley* and choose *Save Code* to create a
decompiled project you can open in Visual Studio.

:## If you're using Avalonia ILSpy, make sure to add the `.csproj` file
extension to the filename in the save dialog, like so:
`Stardew-Valley.csproj` (Otherwise, the project won't decompile
properly.)

You can also use [ilspycmd](https://www.nuget.org/packages/ilspycmd) to
decompile from the command line:

:# Install ilspycmd

:## `dotnet tool install --global ilspycmd`

:# Run ilspycmd (using your local game paths). This will decompile both
the main dll and the game data dll to one project.

:##
`ilspycmd -p --nested-directories -r <game path> -o <output folder> "<game path>/Stardew Valley.dll" "<game path>/StardewValley.GameData.dll"`.

To unpack the XNB data/image/map files, see
<a href="Modding_Editing_XNB_files" class="wikilink"
title="Modding:Editing XNB files">Modding:Editing XNB files</a>.

### What does "target NET 6.0" mean?

There are multiple different things here.

- target version: this is the version of .NET your binary is compiled
  against. You have to target net 6.0 for stardew (and in general, you
  can at maximum use the version of .NET the person loading you uses.)
- sdk version: this is the version of the .NET you installed. You can
  target any version less than your sdk version. If I have net 7.0
  installed with VS 2022, I can still target net 6.0.
- C# version - guess what? the language is versioned separately from the
  .NET version (although there is a correspondence) and you can pick
  your language version with `<langversion>` in the .csproj.

<a href="es_Modding_Guía_del_Modder_Introducción" class="wikilink"
title="es:Modding:Guía del Modder/Introducción">es:Modding:Guía del
Modder/Introducción</a>
<a href="fr_Modding_Guide_du_Moddeur_Commencer" class="wikilink"
title="fr:Modding:Guide du Moddeur/Commencer">fr:Modding:Guide du
Moddeur/Commencer</a>
<a href="pt_Modificações_Guia_do_Modder_Começando" class="wikilink"
title="pt:Modificações:Guia do Modder/Começando">pt:Modificações:Guia do
Modder/Começando</a>
<a href="ru_Модификации_Руководство_мододела_Приступая_к_работе"
class="wikilink"
title="ru:Модификации:Руководство мододела/Приступая к работе">ru:Модификации:Руководство
мододела/Приступая к работе</a>
<a href="tr_Modlama_Mod_Rehberi_Başlangıç_Kılavuzu" class="wikilink"
title="tr:Modlama:Mod Rehberi/Başlangıç Kılavuzu">tr:Modlama:Mod
Rehberi/Başlangıç Kılavuzu</a>
<a href="zh_模组_创建_SMAPI_模组" class="wikilink"
title="zh:模组:创建 SMAPI 模组">zh:模组:创建 SMAPI 模组</a>
