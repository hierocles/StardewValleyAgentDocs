---
title: "Advanced"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, advanced, change-monitoring, custom-priority]
---
## Advanced

### Change monitoring

You may want to handle a change that doesn't have its own event (*e.g.,*
an NPC's heart event ends, a letter is added to the mailbox, etc). You
can usually do that by handling a general event like
<a href="#GameLoop.UpdateTicked" class="wikilink"
title="UpdateTicked"><samp>UpdateTicked</samp></a>, and detecting when
the value(s) you're watching changed. For example, here's a complete mod
which logs a message when an in-game event ends:

``` c#
/// <summary>The main entry point for the mod.</summary>
internal sealed class ModEntry : Mod
{
    /*********
    ** Fields
    *********/
    /// <summary>The in-game event detected on the last update tick.</summary>
    private Event LastEvent;

    /*********
    ** Public methods
    *********/
    /// <summary>The mod entry point, called after the mod is first loaded.</summary>
    /// <param name="helper">Provides simplified APIs for writing mods.</param>
    public override void Entry(IModHelper helper)
    {
        helper.Events.GameLoop.UpdateTicked += this.OnUpdateTicked;
    }

    /*********
    ** Private methods
    *********/
    /// <summary>The method invoked when the game updates its state.</summary>
    /// <param name="sender">The event sender.</param>
    /// <param name="e">The event arguments.</param>
    private void OnUpdateTicked(object sender, EventArgs e)
    {
        if (this.LastEvent != null && Game1.CurrentEvent == null)
            this.Monitor.Log($"Event {this.LastEvent.id} just ended!");

        this.LastEvent = Game1.CurrentEvent;
    }
}
```

### Custom priority

SMAPI calls event handlers in the same order they're registered by
default, so the first event handler registered is the first to receive
the event each time. This isn't always predictable, since it depends on
mod load order and when each mod registers their handlers. This order is
also an implementation detail, so it's not guaranteed.

If you need more control over the order, you can specify an event
priority using the `[EventPriority]` attribute: `Low` (after most
handlers), `Default`, `High` (before most handlers), or a custom value
(*e.g.,* `High + 1` is higher priority than `High`). **You should only
do this if strictly needed**; depending on event handler order between
mods is fragile (*e.g.,* the other mod might change its priority too).

``` c#
/// <summary>The main entry point for the mod.</summary>
internal sealed class ModEntry : Mod
{
    /*********
    ** Public methods
    *********/
    /// <summary>The mod entry point, called after the mod is first loaded.</summary>
    /// <param name="helper">Provides simplified APIs for writing mods.</param>
    public override void Entry(IModHelper helper)
    {
        helper.Events.GameLoop.UpdateTicked += this.OnUpdateTicked;
    }

    /*********
    ** Private methods
    *********/
    /// <summary>The method invoked when the game updates its state.</summary>
    /// <param name="sender">The event sender.</param>
    /// <param name="e">The event arguments.</param>
    [EventPriority(EventPriority.High)]
    private void OnUpdateTicked(object sender, EventArgs e)
    {
        this.Monitor.Log("Update!");
    }
}
```

<a href="ru_Модификации_Руководство_мододела_API_События"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/События">ru:Модификации:Руководство
мододела/API/События</a>
<a href="zh_模组_制作指南_APIs_Events" class="wikilink"
title="zh:模组:制作指南/APIs/Events">zh:模组:制作指南/APIs/Events</a>
