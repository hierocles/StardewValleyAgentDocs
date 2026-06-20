---
title: "Overview"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, faqs, what-are-events, how-do-i-use-them, how-do-events-fit-into-the-game, what-if-a-mod-changes-what-the-event-was-raised-for]
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

SMAPI provides several C# events which let your mod respond when
something happens (like when the player places an object) or run code
periodically (like once per update tick).

## FAQs

### What are events?

Events let you run code when something happens. You can add any number
of *event handlers* (methods to call) when an *event* (what happened) is
raised. You can think of events and handlers as a *when..then*
statement:

    WHEN the save is loaded,   <-- event
    THEN run my code           <-- event handler

See [*Events* in the C# programming
guide](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/events/)
for more info.

### How do I use them?

Event handlers are usually added in your `Entry` method, though you can
add and remove them anytime. For example, let's say you want to print a
message when each day starts. First you would choose the appropriate
event from the list below
(`[[#GameLoop.DayStarted|GameLoop.DayStarted]]`), then add an event
handler, and do something in your method code:

``` c#
/// <summary>The main entry point for the mod.</summary>
internal sealed class ModEntry : Mod
{
    /**********
    ** Public methods
    *********/
    /// <summary>The mod entry point, called after the mod is first loaded.</summary>
    /// <param name="helper">Provides simplified APIs for writing mods.</param>
    public override void Entry(IModHelper helper)
    {
        // event += method to call
        helper.Events.GameLoop.DayStarted += this.OnDayStarted;
    }

    /// <summary>The method called after a new day starts.</summary>
    /// <param name="sender">The event sender.</param>
    /// <param name="e">The event arguments.</param>
    private void OnDayStarted(object? sender, DayStartedEventArgs e)
    {
       this.Monitor.Log("A new day dawns!", LogLevel.Info);
    }
}
```

Tip: you don't need to memorise the method arguments. In Visual Studio,
type `helper.Events.GameLoop.SaveLoaded +=` and press to auto-create a
method. (There doesn't seem to be an equivalent feature in MonoDevelop.)

`sender` is part of the C# event pattern, and is unused by SMAPI.

### How do events fit into the game?

Events are raised on each game tick (when the game updates its state and
renders to the screen), which is 60 times per second. An event may be
raised multiple times (*e.g.,* if the player pressed two keys
simultaneously), but most events won't be raised 60 times per second
(*e.g.,* players are unlikely to be pressing 60 buttons per second).

Your event handlers are run *synchronously*: the game is paused and no
other mod's code will run simultaneously, so there's no risk of
conflicting changes. Since code runs very quickly, players won't notice
any delay unless your code is unusually slow. That said, when using
frequent events like `UpdateTicked` or `Rendered`, you should cache
expensive operations (like loading an asset) instead of repeating them
in each tick to avoid impacting performance.

### What if a mod changes what the event was raised for?

Events are raised based on a snapshot of the game state. That's usually
*but not necessarily* the current game state.

For example, consider this case:

1.  The `GameMenu` opens.
2.  SMAPI raises the `MenuChanged` event, which mods A and B listen to.
3.  Mod A receives the event and closes the menu.
4.  Mod B receives the event.

Each mod is still handling the `MenuChanged` event for the opened menu,
even though the first mod closed it. SMAPI will raise a new
`MenuChanged` event for the closed menu on the next tick.

This rarely affects mods, but it's something to keep in mind if you need
the current state (*e.g.,* check `Game1.activeClickableMenu` instead of
`e.NewMenu`).
