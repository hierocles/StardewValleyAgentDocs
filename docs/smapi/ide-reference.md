---
title: "Ide Reference"
wiki_source: "Modding:IDE reference"
permalink: /Modding:IDE_reference/
category: smapi
tags: [ide-reference, before-you-start, create-a-mod-project, windows-visual-studio-2019-2022, windows-mac-linux-rider-2024-x-x, linux-monodevelop, macos-visual-studio-2019-for-mac, macos-visual-studio-for-mac]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page is a quick reference for how to use Visual Studio 2017 or
MonoDevelop/Visual Studio for Mac when creating or editing a SMAPI mod.
See <a href="Modding_Modder_Guide_Get_Started" class="wikilink"
title="Modding:Modder Guide">Modding:Modder Guide</a> for the main
guide.

## Before you start

- You should install [Visual Studio
  Community](https://visualstudio.microsoft.com/vs/community/)
  (Windows), [MonoDevelop](http://www.monodevelop.com/) (Linux), or
  [Visual Studio for Mac](https://visualstudio.microsoft.com/vs/mac/)
  (Mac).
- Reviewing [*C# Fundamentals for Absolute
  Beginners*](https://mva.microsoft.com/en-us/training-courses/c-fundamentals-for-absolute-beginners-16169)
  is strongly recommended if you're new to programming C#.
- Here are some basic terms to remember:
  | term | definition |
  |----|----|
  | IDE | The program used to edit, run, and compile your code (short for *Integrated Development Environment*). The main IDEs are Visual Studio on Windows, and MonoDevelop/Visual Studio for Mac on Linux/Mac. |
  | DLL | The file with a `.dll` extension which contains your compiled code (short for *Dynamic Link Library*). This is the file that SMAPI reads when loading your mod. |
  | project | A collection of source code + configuration + resources (like images) you edit in the IDE. Each project is compiled into its own DLL. |
  | solution | A collection of projects with some global settings. The solution itself isn't compiled, but it enables some convenient features (like letting projects easily reference each other). |

## Create a mod project

<span id="create-project"></span> Before you can write your mod code,
you need to create a solution and project to contain it.

### Windows (Visual Studio 2019/2022)

1.  Open Visual Studio 2019/2022.
2.  Click *Create a new project* from the start screen.\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(Visual_Studio_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - create project (Visual Studio 1).png"><span>File:Modding</span>
    - IDE reference - create project (Visual Studio 1).png</a>
3.  Filter by "C#" and "Library", then choose *Class Library* and click
    *Next*. Make sure you **don't** choose *Class Library (.NET
    Framework)* which won't work.\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(Visual_Studio_2).png"
    class="wikilink" title="589px">589px</a>
4.  In the *configure your new project* window:
    1.  Enter a descriptive mod name. By convention, the name should be
        one word with mixed caps (like "PineapplesEverywhere").
    2.  Make sure "Place solution and project in the same directory" is
        *not* checked.
    3.  Click "Create" to to create the project.

    <a
    href="File_Modding_-_IDE_reference_-_create_project_(Visual_Studio_3).png"
    class="wikilink" title="800px">800px</a>
5.  Next, select NET 6.0 and click "Create" to create the project. For
    VS 2022, this will be on the next page.\
    <a href="File_Screenshot_2021-12-16_140835.png" class="wikilink"
    title="File:Screenshot 2021-12-16 140835.png"><span>File:Screenshot</span>
    2021-12-16 140835.png</a>

### Windows/Mac/Linux (Rider 2024.x.x)

1.  Open Rider.
2.  Click *New Solution* from the project selection window. Rider may
    open to your previously opened project instead. If this is the case,
    click on *File*, and *New Solution*.\
    <a href="File_Rider_IDE_Guide_-_1.png" class="wikilink"
    title="800px">800px</a>
3.  Click *Class Library* in the left pane.\
    <a href="File_Rider_IDE_Guide_-_2.png" class="wikilink"
    title="800px">800px</a>
4.  Click where it says *from \<SDK version\>*.\
    <a href="File_Rider_IDE_Guide_-_3.png" class="wikilink"
    title="800px">800px</a>
5.  Select *SDK 6.0* so you can create a *.NET 6.0* project.\
    <a href="File_Rider_IDE_Guide_-_4.png" class="wikilink"
    title="800px">800px</a>
6.  Select *net6.0* in the dropdown to the right of *Target framework*.\
    <a href="File_Rider_IDE_Guide_-_6.png" class="wikilink"
    title="800px">800px</a>
7.  Click the *Create* button.\
    <a href="File_Rider_IDE_Guide_-_7.png" class="wikilink"
    title="800px">800px</a>

### Linux (MonoDevelop)

1.  Open MonoDevelop.
2.  Click *File » New Solution* from the menu bar:\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(MonoDevelop_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - create project (MonoDevelop 1).png"><span>File:Modding</span>
    - IDE reference - create project (MonoDevelop 1).png</a>
3.  In the 'New Project' window, choose *.NET » Library* and click
    *Next*:\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(MonoDevelop_2).png"
    class="wikilink"
    title="File:Modding - IDE reference - create project (MonoDevelop 2).png"><span>File:Modding</span>
    - IDE reference - create project (MonoDevelop 2).png</a>
4.  Enter a descriptive mod name. By convention, the name should be one
    word with mixed caps (like "PineapplesEverywhere"):\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(MonoDevelop_3).png"
    class="wikilink"
    title="File:Modding - IDE reference - create project (MonoDevelop 3).png"><span>File:Modding</span>
    - IDE reference - create project (MonoDevelop 3).png</a>
5.  Make sure "create a project directory within the solution directory"
    is checked, and click *Create*:\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(MonoDevelop_4).png"
    class="wikilink"
    title="File:Modding - IDE reference - create project (MonoDevelop 4).png"><span>File:Modding</span>
    - IDE reference - create project (MonoDevelop 4).png</a>

### MacOS (Visual Studio 2019 for Mac)

1.  Install the .NET 6.0 SDK if you haven't already (check
    <a href="Modding_Modder_Guide_Get_Started#Requirements" class="wikilink"
    title="here">here</a> for your system).\
    <a href="File_1a_NET_website.png" class="wikilink"
    title="600px">600px</a>
2.  Open Visual Studio for Mac.
3.  Click *File » New Solution* from the menu bar:\
    <a href="File_VS_Mac_1_newsolution.png" class="wikilink"
    title="600px">600px</a>
4.  Select the correct type of class library:\
    <a href="File_VS_Mac_2_createlibrary.png" class="wikilink"
    title="600px">600px</a>
5.  Set it to target **.NET 6.0.**:\
    <a href="File_VS_Mac_3_setframework.png" class="wikilink"
    title="600px">600px</a>
6.  Enter a descriptive mod name for the project. By convention, the
    name should be one word with mixed caps (like
    "PineapplesEverywhere"):\
    <a href="File_VS_Mac_4_nameproject.png" class="wikilink"
    title="600px">600px</a>

### MacOS (Visual Studio for Mac)

1.  Open Visual Studio for Mac.
2.  Click *File » New Solution* from the menu bar:\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(Visual_Studio_for_Mac_1).png"
    class="wikilink" title="200px">200px</a>
3.  In the 'New Project' window, choose *.NET » Library* and click
    *Next*:\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(Visual_Studio_for_Mac_2).png"
    class="wikilink" title="750px">750px</a>
4.  Enter a descriptive mod name. By convention, the name should be one
    word with mixed caps (like "PineapplesEverywhere"):\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(Visual_Studio_for_Mac_3).png"
    class="wikilink" title="750px">750px</a>
5.  Make sure "create a project directory within the solution directory"
    is checked, and click *Create*:\
    <a
    href="File_Modding_-_IDE_reference_-_create_project_(Visual_Studio_for_Mac_4).png"
    class="wikilink" title="750px">750px</a>

## Set the target framework

<span id="set-target-framework"></span> The 'target framework' is the
version of .NET your code uses, which affects the version needed to run
your mod. The recommended target framework is .NET 6.0, which is the
version SMAPI itself targets. **Please find the subsection below for
your OS** (Windows/Mac).

### In Windows Visual Studio 2019/2022

**NOTE: Visual Studio 2017 MAY no longer be compatible with creating
mods!** If you followed
<a href="Modding_Modder_Guide_Get_Started" class="wikilink"
title="Modding:Modder_Guide/Get_Started">Modding:Modder_Guide/Get_Started</a>
and receive errors, from the code that page instructed be copy and
pasted, with regards to `helper.Events` in the
`Entry(IModhelper helper)` method and `ButtonPressedEventArgs` from the
`Entry(IModHelper helper)` method, try the project-creation and
code-copy/paste process again with Visual Studio 2019/2022 instead.

1.  Open the Solution Explorer pane. If it's not visible, click *View »
    Solution Explorer* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(Visual_Studio).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (Visual Studio).png"><span>File:Modding</span>
    - IDE reference - show solution pane (Visual Studio).png</a>
2.  From the Solution Explorer, right-click on the project and choose
    *Properties*:\
    <a
    href="File_Modding_-_IDE_reference_-_change_target_framework_(Visual_Studio_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - change target framework (Visual Studio 1).png"><span>File:Modding</span>
    - IDE reference - change target framework (Visual Studio 1).png</a>
3.  On the *Application* tab, change the *Target Framework* dropdown to
    *.NET 6.0*:\
    <a
    href="File_Modding_-_IDE_reference_-_change_target_framework_(Visual_Studio_2).png"
    class="wikilink" title="800px">800px</a>
4.  A dialogue may appear asking you to confirm the change. Click 'Yes'
    to confirm:\
    <a
    href="File_Modding_-_IDE_reference_-_change_target_framework_(Visual_Studio_3).png"
    class="wikilink"
    title="File:Modding - IDE reference - change target framework (Visual Studio 3).png"><span>File:Modding</span>
    - IDE reference - change target framework (Visual Studio 3).png</a>

### In Visual Studio 2019 for Mac

If you followed the instructions above to set up your project, your
framework should already be set to .NET 6.0. However, if you picked the
wrong class library or you just want to check, you can follow these
steps to look at the .csproj file, which is basically equivalent to
setting it manually. (If you're checking that it worked, don't replace
the .csproj, just check it refers to .NET 6.0.)

Unfortunately there doesn't appear to be a way to change the target
framework using the GUI. However, it is very easy to follow the 1.5.5
migration guide steps:

1.  Open the .csproj file for editing:\
    <a href="File_VS_Mac_7_editcsproj.png" class="wikilink"
    title="600px">600px</a>
2.  Replace your mod's `.csproj` file with this (where `EXAMLE_MOD_NAME`
    is your solution's name):

``` xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <AssemblyName>EXAMPLE_MOD_NAME</AssemblyName>
    <RootNamespace>EXAMPLE_MOD_NAME</RootNamespace>
    <Version>1.0.0</Version>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Pathoschild.Stardew.ModBuildConfig" Version="4.0.0" />
  </ItemGroup>
</Project>
```

1.  If the mod uses
    <a href="Modding_Modder_Guide_APIs_Harmony" class="wikilink"
    title="Harmony">Harmony</a>, add
    `<EnableHarmony>true</EnableHarmony>` to the property group.

### In MonoDevelop/Visual Studio for Mac

**This section is out of date for Stardew Valley 1.5.5. It appears you
cannot change the .NET framework in this way with Visual Studio 2019 and
Stardew Valley 1.5.5.**

1.  Open the Solution pad. If it's not visible, click *View » Pads »
    Solution* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(MonoDevelop).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (MonoDevelop).png"><span>File:Modding</span>
    - IDE reference - show solution pane (MonoDevelop).png</a>
2.  From the Solution pad, right-click on the project and choose
    *Options*:\
    <a
    href="File_Modding_-_IDE_reference_-_change_target_framework_(MonoDevelop_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - change target framework (MonoDevelop 1).png"><span>File:Modding</span>
    - IDE reference - change target framework (MonoDevelop 1).png</a>
3.  On the *Build » General* tab, change the *Target Framework* dropdown
    to *Mono / .NET 6.0*:\
    <a
    href="File_Modding_-_IDE_reference_-_change_target_framework_(MonoDevelop_2).png"
    class="wikilink"
    title="File:Modding - IDE reference - change target framework (MonoDevelop 2).png"><span>File:Modding</span>
    - IDE reference - change target framework (MonoDevelop 2).png</a>

## Add a file

<span id="add-file"></span>

### In Visual Studio 2017

1.  Open the Solution Explorer pane. If it's not visible, click *View »
    Solution Explorer* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(Visual_Studio).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (Visual Studio).png"><span>File:Modding</span>
    - IDE reference - show solution pane (Visual Studio).png</a>
2.  From the Solution Explorer pane, right-click on the project and
    choose *Add » New Item*:\
    <a
    href="File_Modding_-_IDE_reference_-_create_file_(Visual_Studio_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - create file (Visual Studio 1).png"><span>File:Modding</span>
    - IDE reference - create file (Visual Studio 1).png</a>
3.  From the 'Add New Item' window, choose the file type (usually
    *Visual C# Item » Class*):\
    <a
    href="File_Modding_-_IDE_reference_-_create_file_(Visual_Studio_2).png"
    class="wikilink"
    title="File:Modding - IDE reference - create file (Visual Studio 2).png"><span>File:Modding</span>
    - IDE reference - create file (Visual Studio 2).png</a>
4.  Enter a descriptive file name and click *Add*:\
    <a
    href="File_Modding_-_IDE_reference_-_create_file_(Visual_Studio_3).png"
    class="wikilink"
    title="File:Modding - IDE reference - create file (Visual Studio 3).png"><span>File:Modding</span>
    - IDE reference - create file (Visual Studio 3).png</a>

### In MonoDevelop/Visual Studio for Mac

1.  Open the Solution pad. If it's not visible, click *View » Pads »
    Solution* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(MonoDevelop).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (MonoDevelop).png"><span>File:Modding</span>
    - IDE reference - show solution pane (MonoDevelop).png</a>
2.  From the Solution pad, right-click on the project to delete and
    choose *Add » New File*:\
    <a href="File_Modding_-_IDE_reference_-_create_file_(MonoDevelop_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - create file (MonoDevelop 1).png"><span>File:Modding</span>
    - IDE reference - create file (MonoDevelop 1).png</a>
3.  From the 'New File' window, choose the file type (usually *General »
    Empty Class*):\
    <a href="File_Modding_-_IDE_reference_-_create_file_(MonoDevelop_2).png"
    class="wikilink"
    title="File:Modding - IDE reference - create file (MonoDevelop 2).png"><span>File:Modding</span>
    - IDE reference - create file (MonoDevelop 2).png</a>
4.  Enter a descriptive file name and click *New*:\
    <a href="File_Modding_-_IDE_reference_-_create_file_(MonoDevelop_3).png"
    class="wikilink"
    title="File:Modding - IDE reference - create file (MonoDevelop 3).png"><span>File:Modding</span>
    - IDE reference - create file (MonoDevelop 3).png</a>

## Delete a file

<span id="delete-file"></span>

### In Visual Studio 2017

1.  Open the Solution Explorer pane. If it's not visible, click *View »
    Solution Explorer* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(Visual_Studio).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (Visual Studio).png"><span>File:Modding</span>
    - IDE reference - show solution pane (Visual Studio).png</a>
2.  From the Solution Explorer pane, right-click on the file to delete
    and choose *Delete*:\
    <a href="File_Modding_-_IDE_reference_-_delete_file_(Visual_Studio).png"
    class="wikilink"
    title="File:Modding - IDE reference - delete file (Visual Studio).png"><span>File:Modding</span>
    - IDE reference - delete file (Visual Studio).png</a>

### In MonoDevelop/Visual Studio for Mac

1.  Open the Solution pad. If it's not visible, click *View » Pads »
    Solution* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(MonoDevelop).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (MonoDevelop).png"><span>File:Modding</span>
    - IDE reference - show solution pane (MonoDevelop).png</a>
2.  From the Solution pad, right-click on the file to delete and choose
    *Remove*:\
    <a href="File_Modding_-_IDE_reference_-_delete_file_(MonoDevelop).png"
    class="wikilink"
    title="File:Modding - IDE reference - delete file (MonoDevelop).png"><span>File:Modding</span>
    - IDE reference - delete file (MonoDevelop).png</a>

## Add a NuGet package

<span id="add-nuget"></span>

### In Visual Studio Code

1.  As of August 31, 2024, Visual Studio is now retired for Mac. You may
    be using Visual Studio Code to edit your game files now. As of right
    now, the built-in Nuget Package Manager with the C# Dev Kit does not
    work with SDK 6.0. You can download another extension called "Nuget
    Package Manager GUI" by aliasadidev and the flow will be similar to
    the process below for Visual Studio 2019. If you do not want to
    download this, you can use the Terminal below.
2.  With your Project open, open a new Terminal in Visual Studio Code.
3.  Type in
    `dotnet add <YOUR_MOD_NAME_HERE> package Pathoschild.Stardew.ModBuildConfig`
    to the terminal and press enter. Change `<YOUR_MOD_NAME_HERE>` to
    the name of your Mod.
4.  You should get a bunch of log messages like in the picture below.



<a href="File_Nuget_package_cli.png" class="wikilink"
title="thumb">thumb</a>

### In Visual Studio 2019/2022

1.  Click *Tools » NuGet Package Manager » Manage NuGet Packages for
    Solution* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_add_NuGet_package_(Visual_Studio_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - add NuGet package (Visual Studio 1).png"><span>File:Modding</span>
    - IDE reference - add NuGet package (Visual Studio 1).png</a>
2.  Note: if the nuget package manager is missing, you can add it as a
    package source with the following steps:
    <https://stackoverflow.com/questions/37293242/nuget-package-manager-no-packages-found-even-though-the-package-exists>
3.  On the *Browse* tab, search for the package and click on the result
    to display some options:\
    <a
    href="File_Modding_-_IDE_reference_-_add_NuGet_package_(Visual_Studio_2).png"
    class="wikilink"
    title="File:Modding - IDE reference - add NuGet package (Visual Studio 2).png"><span>File:Modding</span>
    - IDE reference - add NuGet package (Visual Studio 2).png</a>
4.  In the options, check the box next to your project and click
    *Install*:\
    <a
    href="File_Modding_-_IDE_reference_-_add_NuGet_package_(Visual_Studio_3).png"
    class="wikilink"
    title="File:Modding - IDE reference - add NuGet package (Visual Studio 3).png"><span>File:Modding</span>
    - IDE reference - add NuGet package (Visual Studio 3).png</a>
5.  If a 'Review Changes' dialogue appears, click *OK*:\
    <a
    href="File_Modding_-_IDE_reference_-_add_NuGet_package_(Visual_Studio_4).png"
    class="wikilink"
    title="File:Modding - IDE reference - add NuGet package (Visual Studio 4).png"><span>File:Modding</span>
    - IDE reference - add NuGet package (Visual Studio 4).png</a>

### In Visual Studio 2019 for Mac

1.  Click *Project » Manage NuGet Packages...* from the menu:\
    <a href="File_VS_Mac_5_managenuget.png" class="wikilink"
    title="600px">600px</a>
2.  Search for the package, click on the result, and click *Add
    Package*:\
    <a href="File_VS_Mac_6_addnuget.png" class="wikilink"
    title="600px">600px</a>
3.  Quit and relaunch Visual Studio.

### In MonoDevelop/Visual Studio for Mac

1.  Click *Project » Add NuGet Packages* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_add_NuGet_package_(MonoDevelop_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - add NuGet package (MonoDevelop 1).png"><span>File:Modding</span>
    - IDE reference - add NuGet package (MonoDevelop 1).png</a>
2.  Search for the package, click on the result, and click *Add
    Package*:\
    <a
    href="File_Modding_-_IDE_reference_-_add_NuGet_package_(MonoDevelop_2).png"
    class="wikilink"
    title="File:Modding - IDE reference - add NuGet package (MonoDevelop 2).png"><span>File:Modding</span>
    - IDE reference - add NuGet package (MonoDevelop 2).png</a>

## Edit project file (`.csproj`)

<span id="edit-project"></span>

Sometimes you may want to edit the project file directly (mainly to
configure build steps). The project is a `.csproj` file, and can be
edited from within the IDE.

### In Visual Studio 2017

1.  Open the Solution Explorer pane. If it's not visible, click *View »
    Solution Explorer* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(Visual_Studio).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (Visual Studio).png"><span>File:Modding</span>
    - IDE reference - show solution pane (Visual Studio).png</a>
2.  From the Solution Explorer pane, right-click on the project and
    choose *Unload*:\
    <a
    href="File_Modding_-_IDE_reference_-_edit_project_(Visual_Studio_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - edit project (Visual Studio 1).png"><span>File:Modding</span>
    - IDE reference - edit project (Visual Studio 1).png</a>
3.  Right-click on the project again and choose *Edit \<project
    name\>.csproj*:\
    <a
    href="File_Modding_-_IDE_reference_-_edit_project_(Visual_Studio_2).png"
    class="wikilink"
    title="File:Modding - IDE reference - edit project (Visual Studio 2).png"><span>File:Modding</span>
    - IDE reference - edit project (Visual Studio 2).png</a>
4.  Make your changes in the editor that appears and save.
5.  When you're done, right-click on the project again and choose
    *Reload Project*:\
    <a
    href="File_Modding_-_IDE_reference_-_edit_project_(Visual_Studio_3).png"
    class="wikilink"
    title="File:Modding - IDE reference - edit project (Visual Studio 3).png"><span>File:Modding</span>
    - IDE reference - edit project (Visual Studio 3).png</a>

### In MonoDevelop/Visual Studio for Mac

1.  Open the Solution pad. If it's not visible, click *View » Pads »
    Solution* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(MonoDevelop).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (MonoDevelop).png"><span>File:Modding</span>
    - IDE reference - show solution pane (MonoDevelop).png</a>
2.  From the Solution pad, right-click on the project and choose *Tools
    » Edit File*:\
    <a href="File_Modding_-_IDE_reference_-_edit_project_(MonoDevelop).png"
    class="wikilink"
    title="File:Modding - IDE reference - edit project (MonoDevelop).png"><span>File:Modding</span>
    - IDE reference - edit project (MonoDevelop).png</a>
3.  Make your changes in the editor that appears and save.

## Find compiled files

<span id="build-output"></span>

### In Visual Studio 2017

1.  Open the Solution Explorer pane. If it's not visible, click *View »
    Solution Explorer* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(Visual_Studio).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (Visual Studio).png"><span>File:Modding</span>
    - IDE reference - show solution pane (Visual Studio).png</a>
2.  From the Solution Explorer pane, right-click on the project and
    choose *Open Folder in File Explorer*:\
    <a
    href="File_Modding_-_IDE_reference_-_view_build_output_(Visual_Studio).png"
    class="wikilink"
    title="File:Modding - IDE reference - view build output (Visual Studio).png"><span>File:Modding</span>
    - IDE reference - view build output (Visual Studio).png</a>
3.  Navigate to `bin\Debug` (or `bin\Release` if you switched to release
    build configuration).

### In MonoDevelop/Visual Studio for Mac

1.  Open the Solution pad. If it's not visible, click *View » Pads »
    Solution* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(MonoDevelop).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (MonoDevelop).png"><span>File:Modding</span>
    - IDE reference - show solution pane (MonoDevelop).png</a>
2.  From the Solution pad, right-click on the project and choose *Open
    Containing Folder*:\
    <a
    href="File_Modding_-_IDE_reference_-_view_build_output_(MonoDevelop).png"
    class="wikilink"
    title="File:Modding - IDE reference - view build output (MonoDevelop).png"><span>File:Modding</span>
    - IDE reference - view build output (MonoDevelop).png</a>
3.  Navigate to `bin/Debug` (or `bin/Release` if you switched to release
    build configuration).

## Add a reference to another DLL

<span id="add-reference"></span>

### In Visual Studio 2017

1.  Open the Solution Explorer pane. If it's not visible, click *View »
    Solution Explorer* from the menu:\
    <a
    href="File_Modding_-_IDE_reference_-_show_solution_pane_(Visual_Studio).png"
    class="wikilink"
    title="File:Modding - IDE reference - show solution pane (Visual Studio).png"><span>File:Modding</span>
    - IDE reference - show solution pane (Visual Studio).png</a>
2.  From the Solution Explorer pane, right-click on *References* and
    choose *Add Reference...*:\
    <a
    href="File_Modding_-_IDE_reference_-_add_reference_(Visual_Studio_1).png"
    class="wikilink"
    title="File:Modding - IDE reference - add reference (Visual Studio 1).png"><span>File:Modding</span>
    - IDE reference - add reference (Visual Studio 1).png</a>
3.  From the 'Reference Manager' window, choose *Browse* in the left
    side, then click *Browse..* at the bottom:\
    <a
    href="File_Modding_-_IDE_reference_-_add_reference_(Visual_Studio_2).png"
    class="wikilink"
    title="File:Modding - IDE reference - add reference (Visual Studio 2).png"><span>File:Modding</span>
    - IDE reference - add reference (Visual Studio 2).png</a>
4.  Find the DLL you want to reference, select it, and click *Add*:\
    <a
    href="File_Modding_-_IDE_reference_-_add_reference_(Visual_Studio_3).png"
    class="wikilink"
    title="File:Modding - IDE reference - add reference (Visual Studio 3).png"><span>File:Modding</span>
    - IDE reference - add reference (Visual Studio 3).png</a>
5.  From the 'Reference Manager' window, click *OK*:\
    <a
    href="File_Modding_-_IDE_reference_-_add_reference_(Visual_Studio_4).png"
    class="wikilink"
    title="File:Modding - IDE reference - add reference (Visual Studio 4).png"><span>File:Modding</span>
    - IDE reference - add reference (Visual Studio 4).png</a>

### In Rider

When opening a project for the first time, you must add a reference to
StardewModdingAPI.dll for code completion to work.

1.  In the Explorer panel, select the *Solution* view
2.  Under the project, right-click on *Dependencies* and choose
    *Reference...*
3.  In the Add Reference window, click *Add From...* at the bottom
4.  Find the DLL you want to reference, select it, and click *OK*

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Referencia_IDE" class="wikilink"
title="es:Modding:Referencia IDE">es:Modding:Referencia IDE</a>
<a href="ru_Модификации_Настройка_среды_разработки" class="wikilink"
title="ru:Модификации:Настройка среды разработки">ru:Модификации:Настройка
среды разработки</a> <a href="zh_模组_IDE_参考" class="wikilink"
title="zh:模组:IDE 参考">zh:模组:IDE 参考</a>
