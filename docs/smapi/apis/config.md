---
title: "Config"
wiki_source: "Modding:Modder Guide/APIs/Config"
permalink: /Modding:Modder_Guide/APIs/Config/
category: smapi
tags: [config, config-model, creating-a-config-model, default-values, using-the-config-file, keybind-settings]
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

You can let users configure your mod through a standard `config.json`
file. SMAPI will automatically create the file and take care of reading,
normalising, and updating it.

## Config model

### Creating a config model

The *config model* is a C# class you create, with properties
representing the settings you want to store. It can contain almost
anything from a few boolean fields to a complex object graph (though you
should try to keep things simple for players). Here's a simple config
model:

``` c#
public sealed class ModConfig
{
   public bool ExampleBoolean { get; set; }
   public int ExampleNumber { get; set; }
}
```

That model would be saved to `config.json` with this content:

``` json
{
   "ExampleBoolean": false,
   "ExampleNumber": 0
}
```

These properties must be public.

### Default values

You can set default values in your data model:

``` c#
public sealed class ModConfig
{
   public bool ExampleBoolean { get; set; } = true;
   public int ExampleNumber { get; set; } = 5;
}
```

...or set defaults with a constructor:

``` c#
public sealed class ModConfig
{
   public bool ExampleBoolean { get; set; }
   public int ExampleNumber { get; set; }

   public ModConfig()
   {
      this.ExampleBoolean = true;
      this.ExampleNumber = 5;
   }
}
```

## Using the config file

To read the `config.json` (SMAPI will create it automatically):

1.  Create your
    <a href="#Config_model" class="wikilink" title="config model">config
    model</a>.
2.  Access the config values in your `ModEntry` class:
    ``` c#
    /// <summary>The main entry point for the mod.</summary>
    internal sealed class ModEntry : Mod
    {
        /*********
        ** Properties
        *********/
        /// <summary>The mod configuration from the player.</summary>
        private ModConfig Config;

        /*********
        ** Public methods
        *********/
        /// <summary>The mod entry point, called after the mod is first loaded.</summary>
        /// <param name="helper">Provides simplified APIs for writing mods.</param>
        public override void Entry(IModHelper helper)
        {
            this.Config = this.Helper.ReadConfig<ModConfig>();
            bool exampleBool = this.Config.ExampleBoolean;
        }
    }
    ```

That's it! When the player launches the game, SMAPI will create the
`config.json` file automatically if it doesn't exist yet, using the
default config options you provided in your model. If you need to save
some changes, you can use `this.Helper.WriteConfig(this.Config)`.

Note that `ReadConfig` will raise an exception if the user does not
provide a valid JSON.

## Keybind settings



You can use SMAPI's
<a href="Modding_Modder_Guide_APIs_Input#KeybindList" class="wikilink"
title="KeybindList"><samp>KeybindList</samp></a> in your model to let
users configure keybinds. This automatically supports multi-key or
alternative bindings (*e.g.,* to support split-screen mode):

``` c#
class ModConfig
{
   public KeybindList ToggleKey { get; set; } = KeybindList.Parse("LeftShift + F2, LeftTrigger");
}
```

The value is automatically written/parsed in the `config.json` file as a
string:

``` json
{
   "ToggleKey": "LeftShift + F2, LeftTrigger"
}
```

<a href="ru_Модификации_Руководство_мододела_API_Конфигурация"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Конфигурация">ru:Модификации:Руководство
мододела/API/Конфигурация</a>
<a href="zh_模组_制作指南_APIs_Config" class="wikilink"
title="zh:模组:制作指南/APIs/Config">zh:模组:制作指南/APIs/Config</a>
