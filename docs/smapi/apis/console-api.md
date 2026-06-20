---
title: "Console Api"
wiki_source: "Modding:Modder Guide/APIs/Console"
permalink: /Modding:Modder_Guide/APIs/Console/
category: smapi
tags: [console, intro, add-a-custom-command, see-also]
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

SMAPI can add custom commands to the SMAPI console, which players can
type to do certain actions. These are also available in the in-game chat
for players using the mod.

## Intro

The SMAPI console is the window that opens alongside the game, which
displays messages from SMAPI and mods in a text-only format. Players can
enter commands directly into that window to interact with mods. For
example, you can type `help` to see a list of available commands. Note
that most players aren't comfortable with a command-line interface, so
you should prefer in-game interfaces for player-facing features in most
cases.

<a href="File_smapi-console-window.png" class="wikilink"
title="thumb">thumb</a>

## Add a custom command

Each console command must have:

- A name which the player types to invoke the command.
- A description shown when the player uses the `help` command. This
  should explain what the command does, how to use it, and what
  arguments it accepts. The example below shows the recommended
  convention.
- The method to call when the command is entered.

This code creates a minimal `player_setmoney` command:

``` C#
/// <summary>The main entry point for the mod.</summary>
public class ModEntry : Mod
{
    /*********
    ** Public methods
    *********/
    /// <summary>The mod entry point, called after the mod is first loaded.</summary>
    /// <param name="helper">Provides simplified APIs for writing mods.</param>
    public override void Entry(IModHelper helper)
    {
        helper.ConsoleCommands.Add("player_setmoney", "Sets the player's money.\n\nUsage: player_setmoney <value>\n- value: the integer amount.", this.SetMoney);
    }

    /*********
    ** Private methods
    *********/
    /// <summary>Set the player's money when the 'player_setmoney' command is invoked.</summary>
    /// <param name="command">The name of the command invoked.</param>
    /// <param name="args">The arguments received by the command. Each word after the command name is a separate argument.</param>
    private void SetMoney(string command, string[] args)
    {
        Game1.player.Money = int.Parse(args[0]);
        this.Monitor.Log($"OK, set your money to {args[0]}.", LogLevel.Info);
    }
}
```

Here's how the player would use it:

    help player_setmoney
    > player_setmoney: Sets the player's money.
    >
    > Usage: player_setmoney <value>
    > - value: the integer amount.

    player_setmoney 5000
    > OK, set your money to 5000.

## See also

- <a href="Modding_Modder_Guide_APIs_Integrations" class="wikilink"
  title="Integration APIs">Integration APIs</a>
- <a href="Modding_Modder_Guide_APIs_Logging" class="wikilink"
  title="Logging API">Logging API</a>

<a href="ru_Модификации_Руководство_мододела_API_Консоль"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Консоль">ru:Модификации:Руководство
мододела/API/Консоль</a>
<a href="zh_模组_制作指南_APIs_Console" class="wikilink"
title="zh:模组:制作指南/APIs/Console">zh:模组:制作指南/APIs/Console</a>
