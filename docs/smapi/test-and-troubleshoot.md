---
title: "Test And Troubleshoot"
wiki_source: "Modding:Modder Guide/Test and Troubleshoot"
permalink: /Modding:Modder_Guide/Test_and_Troubleshoot/
category: smapi
tags: [test-and-troubleshoot, test-the-mod, basic-testing, testing-in-multiplayer, testing-on-all-platforms, fix-common-build-warnings, this-implicitly-converts, fieldname-is-a-net-field]
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

This page helps you test your mods and solve common issues. **For issues
*using* mods, see
<a href="Modding_Player_Guide_Troubleshooting" class="wikilink"
title="Modding:Player Guide/Troubleshooting">Modding:Player
Guide/Troubleshooting</a>.**

## Test the mod

### Basic testing

Testing is pretty straightforward for most mods:

1.  Click *Build \> Rebuild Solution* (Visual Studio) or *Build \>
    Rebuild All* (MonoDevelop).
2.  Make sure there are no build errors and the mod gets copied to your
    `Mods` folder.
3.  Try the mod in-game.
4.  Make sure there are no errors or warnings for your mod in the SMAPI
    console.

In general, if a mod works on one platform it'll work fine on the
others.

### Testing in multiplayer

You can test mods in multiplayer on the same computer, by launching two
instances of the game:

1.  Prepare player one:
    1.  Launch SMAPI like usual.
    2.  From the title screen: click *co-op*, then *host*.
    3.  Start a new save slot (unless you've already created one). Make
        sure to set 'starting cabins' to at least one (you'll need one
        cabin per extra player).
2.  Prepare player two:
    1.  Launch SMAPI again. (This will automatically create a separate
        log file.)
    2.  From the title screen: click *co-op*, then *join LAN game*.
    3.  Leave the 'Enter IP...' box empty and click OK.

### Testing on all platforms

For complex mods, you may need to test your mod on all platforms. The
game is mostly the same on Linux/Mac, so you only need to test your mod
twice: once on Windows, and again on Linux or Mac. You can do that by
testing one version on your computer, and the other in a virtual
machine.

<dl>

<dt>

If your main computer is Windows 10 or 11:

</dt>

<dd>

1.  [Install Windows Subsystem for Linux
    (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install).
2.  Install the required software in WSL:

<!-- -->

1.  [Install
    Steam](https://linuxconfig.org/how-to-install-steam-on-ubuntu-20-04-focal-fossa-linux).
2.  Launch `export TERM=xterm && steam`, then install & launch Stardew
    Valley through its UI. This will also install its dependencies.
3.  *(optional)* Download and install your preferred IDE, if you plan to
    compile the code on Linux. For the [latest standalone Rider
    version](https://www.jetbrains.com/help/rider/Installation_guide.html#prerequisites)
    (not free):
    ``` sh
    wget "<download url here>" -O rider-install.tar.gz
    sudo tar -xzvf rider-install.tar.gz -C /opt
    ln -s "/opt/JetBrains Rider-<version>/bin/rider.sh"
    ./rider.sh
    ```
4.  <a href="Modding_Installing_SMAPI_on_Linux" class="wikilink"
    title="Install SMAPI">Install SMAPI</a>.

</li>

<li>

To launch the game, launch `steam` and run the game through its UI.

</li>

</ol>

</li>

</ul>

</dd>

</dl>

If your main computer is Windows 8 or earlier
1.  Install [VirtualBox](https://www.virtualbox.org/).
2.  Create a [ZorinOS Core](https://zorinos.com/) VM in VirtualBox.
    - *See [this setup
      guide](https://extr3metech.wordpress.com/2013/09/05/installing-zorin-os-7-in-virtual-box-screenshots)
      for more details. The ZorinOS installer might be a bit different
      than shown, but should be pretty intuitive.*
    - *If you don't see any options for 64-bit OSes in VirtualBox, see
      [how to enable them](https://superuser.com/a/866963).*
    - *When creating the virtual disk, at least 20GB is recommended.*
3.  [Download the Steam installer](https://store.steampowered.com/about)
    in the VM and run it.
4.  Launch Steam to finish installation. If nothing happens, see [these
    extra
    steps](https://askubuntu.com/questions/771032/steam-not-opening-in-ubuntu-16-04-lts)
    to fix it.
5.  Install Stardew Valley through Steam.
6.  <a href="Modding_Player_Guide_Getting_Started#Install_SMAPI"
    class="wikilink" title="Install SMAPI">Install SMAPI</a>.
7.  *(optional)* Install
    [`mono-complete`](https://www.mono-project.com/) and
    [MonoDevelop](http://www.monodevelop.com/download/) in your VM. This
    is only needed if you want to compile separately for Linux/Mac. When
    installing `.deb` files, use the instructions for [the Ubuntu
    version shown
    here](https://zorinos.com/help/install-apps/#deb-files). If you run
    into errors, may Linux have mercy on your soul.
8.  *(optional)* For unlocking Mac OS only: [Virtual Machine Unlocker
    2.1.1](https://www.insanelymac.com/forum/files/file/838-unlocker/)
    for VmWare Workstation 11/12/14, VmWare Player 7/12/14, or Fusion
    7/8/10. **This is needed to boot Mac OS on a virtual Machine**

<!-- -->

If your main computer is Linux or macOS
1.  Install [VirtualBox](https://www.virtualbox.org/).
2.  [Create a VM with
    Windows](http://www.macworld.co.uk/how-to/mac-software/run-windows-10-on-your-mac-using-virtualbox-3621650/).
3.  Install Stardew Valley in your VM.
4.  <a href="Modding_Player_Guide_Getting_Started#Install_SMAPI"
    class="wikilink" title="Install SMAPI">Install SMAPI</a>.
5.  *(optional)* Install [Visual Studio
    Community](https://visualstudio.microsoft.com/vs/community/) in your
    VM. This is only needed if you want to compile separately for
    Windows.

## Fix common build warnings

After building your project, you can see build warnings via *Visual
Studio \> View \> Error List* or *MonoDevelop \> View \> Pads \>
Errors*. Here are some common ones.

### This implicitly converts...

Sample warning: "*This implicitly converts '{0}' from Net{1} to {2}, but
Net{1} has unintuitive implicit conversion rules. Consider comparing
against the actual value instead to avoid bugs. See
<https://smapi.io/buildmsg/avoid-implicit-net-field-cast> for details.*"

Your code is referencing a
<a href="Modding_Modder_Guide_Game_Fundamentals#Net_fields"
class="wikilink" title="net field">net field</a>, which can cause subtle
bugs. This field has an equivalent non-net property, like
`monster.Health` (`int`) instead of `monster.health` (`NetBool`). Change
your code to use the suggested property instead.

### FieldName is a Net\* field...

Sample warning: "*'{0}' is a Net{1} field; consider using the {2}
property instead. See <https://smapi.io/buildmsg/avoid-net-field> for
details.*"

Your code is referencing a
<a href="Modding_Modder_Guide_Game_Fundamentals#Net_fields"
class="wikilink" title="net field">net field</a>, which can cause subtle
bugs. You should access the underlying value instead:

- For a reference type (*i.e.,* one that can contain `null`), you can
  use the `.Value` property (or `.FieldDict` for a `NetDictionary`):
  ``` c#
  if (building.indoors.Value == null)
  ```

  Or convert the value before comparison:

  ``` c#
  GameLocation indoors = building.indoors.Value;
  if(indoors == null)
     // ...
  ```
- For a value type (*i.e.,* one that can't contain `null`), check if the
  parent is null (if needed) and compare with `.Value`:
  ``` c#
  if (item != null && item.category.Value == 0)
  ```

### The FieldName field is obsolete...

Sample warning: "*The 'Character.friendships' field is obsolete and
should be replaced with 'friendshipData'. See
<https://smapi.io/buildmsg/avoid-obsolete-field> for details.*"

You're referencing a field which should no longer be used. Use the
suggested field name instead to fix it.

### An instance of analyzer ... cannot be created

Update to the latest [Visual
Studio](https://visualstudio.microsoft.com/vs/community/); the NuGet
package uses a recent feature that isn't available in older versions.

### Feature 'global using directive' is not available in C# 9.0

Go to your solution's project file (the .csproj file) and change the
\<ImplicitUsings\> property from "enable" to "disable".

## Other issues

### Can't target .NET 6

If the target framework list has options starting with...

- *.NET Framework*: you created the wrong type of project. Make sure you
  create a .NET 6 project for your mod instead. (The naming is a bit
  confusing.)
- *.NET Core*, *.NET Standard*, or *.NET 6+*: use .NET 6 for
  compatibility with the game. If you don't have that option, you can
  install the [.NET 6
  SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) to add
  it.

### Visual Studio can't find the game/SMAPI/MonoGame DLLs

<span id="Visual_Studio_can.27t_find_the_game.2FSMAPI.2FXNA_DLLs">
</span> Common solutions:

- Restart Visual Studio.
- Make sure the game and SMAPI are correctly installed and work fine.
- Check for an error like "*Failed to find game install path*". If it's
  present, you need to [specify your game
  path](https://smapi.io/package/custom-game-path).
- Make sure you created a .NET 6 project, **not** .NET Framework. (See
  <a href="Modding_IDE_reference#Set_the_target_framework"
  class="wikilink" title="how to set the target framework">how to set the
  target framework</a>; if you see options starting with .NET Framework,
  delete the project and create a .NET 6 project instead.)
- Make sure you target .NET 6 (see
  <a href="Modding_IDE_reference#Set_the_target_framework"
  class="wikilink" title="how to">how to</a>).

If those didn't fix it:

1.  Click *Build \> Rebuild Solution* (Visual Studio) or *Build \>
    Rebuild All* (MonoDevelop).
2.  Check the *Output* pane or error list (Visual Studio), or the
    *Errors* pad (MonoDevelop).
3.  If you don't see anything relevant, post the *Output* text to
    [hastebin](https://hastebin.com),
    <a href="#Ask_for_help" class="wikilink"
    title="ask for help on Discord">ask for help on Discord</a>, and
    include a link to your hastebin.

## Ask for help

See <a href="Modding_Help" class="wikilink"
title="Modding:Help">Modding:Help</a> for how to get help!

<a href="es_Modding_Guía_del_Modder_Prueba_y_solución_de_problemas"
class="wikilink"
title="es:Modding:Guía del Modder/Prueba y solución de problemas">es:Modding:Guía
del Modder/Prueba y solución de problemas</a>
<a href="pt_Modificações_Guia_do_Modder_Teste_e_Solução_de_Problemas"
class="wikilink"
title="pt:Modificações:Guia do Modder/Teste e Solução de Problemas">pt:Modificações:Guia
do Modder/Teste e Solução de Problemas</a>
<a href="ru_Модификации_Руководство_мододела_Тестирование_и_отладка"
class="wikilink"
title="ru:Модификации:Руководство мододела/Тестирование и отладка">ru:Модификации:Руководство
мододела/Тестирование и отладка</a>
<a href="zh_模组_制作指南_测试和疑难解答" class="wikilink"
title="zh:模组:制作指南/测试和疑难解答">zh:模组:制作指南/测试和疑难解答</a>
