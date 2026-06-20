---
title: "Logging"
wiki_source: "Modding:Modder Guide/APIs/Logging"
permalink: /Modding:Modder_Guide/APIs/Logging/
category: smapi
tags: [logging, overview, log-levels, log-once, verbose-logging, faqs, where-is-the-log-file-created]
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

The monitor API, available through `this.Monitor` in your mod class,
mainly lets you write messages to the console window and log file.

## Logging

### Overview

You can log messages by calling `this.Monitor.Log` with a string message
and a log level. These messages will appear in the SMAPI console and log
file.

For example, this code:

``` c#
this.Monitor.Log("a trace message", LogLevel.Trace);
this.Monitor.Log("a debug message", LogLevel.Debug);
this.Monitor.Log("an info message", LogLevel.Info);
this.Monitor.Log("a warning message", LogLevel.Warn);
this.Monitor.Log("an error message", LogLevel.Error);
```

...will produce log entries with a timestamp, log level, mod name, and
message:

<div style="font-family: monospace;">

<span style="color:#666;">\[18:00:00 TRACE NameOfMod\] a trace
message</span>\
<span style="color:#666;">\[18:00:00 DEBUG NameOfMod\] a debug
message</span>\
<span style="color:black;">\[18:00:00 INFO NameOfMod\] an info
message</span>\
<span style="color:darkorange;">\[18:00:00 WARN NameOfMod\] a warning
message</span>\
<span style="color:red;">\[18:00:00 ERROR NameOfMod\] an error
message</span>

</div>

The text won't appear in color in the log file, but will appear in color
in SMAPI console window as the game runs.

### Log levels

The log level is *semantic*, meaning that the level itself conveys
information (a `Trace` message means something different from an `Error`
message). You should use the log level that's closest to your message's
purpose:

| level | purpose |
|----|----|
| `Trace` | Tracing info intended for developers, usually low-level troubleshooting details that are useful when someone sends you their error log. Trace messages won't appear in the console window by default (unless you have the "SMAPI for developers" version), though they're always written to the log file. |
| `Debug` | Troubleshooting details that may be relevant to the player. |
| `Info` | Info relevant to the player. This should be used judiciously. |
| `Warn` | Potential problems that the player should be aware of. This should be used rarely. |
| `Error` | A message indicating something went wrong. |
| `Alert` | Important information to highlight for the player when player action is needed (*e.g.,* new version available). This is mainly meant for SMAPI itself, and should almost never be used by mods. |

### Log once

The `LogOnce` method lets you log a message just
<a href="#Overview" class="wikilink" title="like the above">like the
above</a>, but only once per game launch. For example, you can use it to
show a compatibility warning for an API call:

``` c#
this.Monitor.LogOnce("Some Mod Name used the deprecated X API.", LogLevel.Warn);
```

### Verbose logging

You can have messages appear in the log (and console in the *for
developers* version) only if SMAPI's verbose logging option is enabled.
This is meant for diagnostic information that's sometimes needed to
troubleshoot, but doesn't need to be logged in most cases.

There are two ways to use it:

``` c#
// log a TRACE message if verbose logging is enabled
this.Monitor.VerboseLog("This will only appear if verbose logging is enabled.");

// check the verbose option
if (this.Monitor.IsVerbose)
   this.Monitor("This will only appear if verbose logging is enabled.", LogLevel.Trace);
```

Players can enable verbose logging by adding your mod ID to the
`VerboseLogging` field in the
`smapi-internal/StardewModdingAPI.config.json` (or
`smapi-internal/config.user.json` file. For example, this enables it for
SMAPI and Content Patcher:

``` js
"VerboseLogging": [ "SMAPI", "Pathoschild.ContentPatcher" ],
```

## FAQs

### Where is the log file created?

It's output to the game's `ErrorLogs` data folder. See
[smapi.io/log](https://smapi.io/log/) for help finding the log file, and
you can also upload your log there to see what it looks like. The log
file is always created (even if there are no errors) and it's written
continuously (so you don't need to exit the game to see the log so far).

<a href="ru_Модификации_Руководство_мододела_API_Журнал"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Журнал">ru:Модификации:Руководство
мододела/API/Журнал</a>
<a href="zh_模组_制作指南_APIs_Logging" class="wikilink"
title="zh:模组:制作指南/APIs/Logging">zh:模组:制作指南/APIs/Logging</a>
