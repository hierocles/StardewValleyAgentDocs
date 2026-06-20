---
title: "Game Loop"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, game-loop]
---
### Game loop

`this.Helper.Events.GameLoop` has events linked to the game's update
loop. The update loop runs roughly ≈60 times/second to run game logic
like state changes, action handling, etc. These are often useful, but
you should consider semantic events like `Input` where applicable.

<table>
<thead>
<tr>
<th><p>event</p></th>
<th><p>summary</p>
<h4 id="gamelaunched">GameLaunched</h4>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised after the game is launched, right before the first update
tick. This happens once per game session (unrelated to loading saves).
All mods are loaded and initialised at this point, so this is a good
time to set up mod integrations.</p>
<h4 id="updateticking">UpdateTicking</h4>
<p><em>Also known as:</em> <code>UpdateTicked</code></p>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised before/after the game state is updated (≈60 times per
second).</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Ticks</samp></p></td>
<td><p><samp>int</samp></p></td>
<td><p>The number of ticks elapsed since the game started, including the
current tick.</p></td>
</tr>
<tr>
<td><p><samp>e.IsOneSecond</samp></p></td>
<td><p><samp>bool</samp></p></td>
<td><p>Whether <samp>e.TicksElapsed</samp> is a multiple of 60, which
happens approximately once per second.</p></td>
</tr>
<tr>
<td><p><samp>e.IsMultipleOf(int number)</samp></p></td>
<td><p><em><code>method</code></em><code> returns </code><samp>bool</samp></p></td>
<td><p>Whether <samp>e.TicksElapsed</samp> is a multiple of the given
number. This is mainly useful if you want to run logic intermittently
(<em>e.g.,</em> <code>e.IsMultipleOf(30)</code> for every
half-second).</p></td>
</tr>
</tbody>
</table>
<h4 id="onesecondupdateticking">OneSecondUpdateTicking</h4>
<p><em>Also known as:</em> <code>OneSecondUpdateTicked</code></p>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised before/after the game state is updated, once per second.
EventArgs subtype is OneSecondUpdateTickedEventArgs</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.Ticks</samp></p></td>
<td><p><samp>int</samp></p></td>
<td><p>The number of ticks elapsed since the game started, including the
current tick.</p></td>
</tr>
</tbody>
</table>
<h4 id="savecreating">SaveCreating</h4>
<p><em>Also known as:</em> <code>SaveCreated</code></p>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised before/after the game creates the save file (after the
new-game intro). The save won't be written until all mods have finished
handling this event. This is a somewhat specialised event, since the
world isn't fully initialised at this point; in most cases you should
use <a href="#GameLoop.DayStarted" class="wikilink"
title="DayStarted"><samp>DayStarted</samp></a>, <a
href="#GameLoop.Saving" class="wikilink"
title="Saving"><samp>Saving</samp></a>, or <a href="#GameLoop.Saved"
class="wikilink" title="Saved"><samp>Saved</samp></a> instead.</p>
<h4 id="saving">Saving</h4>
<p><em>Also known as:</em> <code>Saved</code></p>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised before/after the game writes data to save file (except <a
href="#GameLoop.SaveCreating" class="wikilink"
title="the initial save creation">the initial save creation</a>). The
save won't be written until all mods have finished handling this event.
This is also raised for farmhands in multiplayer.</p>
<h4 id="saveloaded">SaveLoaded</h4>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised after loading a save (including the first day after creating a
new save), or connecting to a multiplayer world. This happens right
before <samp>DayStarted</samp>, but after the game's own day-start
initialization process; at this point the save file is read and
<samp>[[Modding_Modder_Guide_APIs_Utilities#Context|Context.IsWorldReady]]</samp>
is true.</p>
<h4 id="daystarted">DayStarted</h4>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised after a new in-game day starts, or after connecting to a
multiplayer world. Everything has already been initialised at this
point. (To run code before the game sets up the day, see <a
href="#GameLoop.DayEnding" class="wikilink"
title="DayEnding"><samp>DayEnding</samp></a> instead.)</p>
<h4 id="dayending">DayEnding</h4>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised before the game ends the current day. This happens before it
starts setting up the next day and before <a href="#GameLoop.Saving"
class="wikilink" title="Saving"><samp>Saving</samp></a>.</p>
<h4 id="timechanged">TimeChanged</h4>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised after the in-game clock time changes, which happens in
intervals of ten in-game minutes.</p>
<p><em>Event arguments:</em></p>
<table>
<thead>
<tr>
<th><p>Argument</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>e.OldTime</samp></p></td>
<td><p><samp>int</samp></p></td>
<td><p>The previous time of day in 24-hour notation (like 1600 for 4pm).
The clock time resets when the player sleeps, so 2am (before sleeping)
is 2600.</p></td>
</tr>
<tr>
<td><p><samp>e.NewTime</samp></p></td>
<td><p><samp>int</samp></p></td>
<td><p>The current time of day in 24-hour notation (like 1600 for 4pm).
The clock time resets when the player sleeps, so 2am (before sleeping)
is 2600.</p></td>
</tr>
</tbody>
</table>
<h4 id="returnedtotitle">ReturnedToTitle</h4>
<p><em>Group:</em> <code>GameLoop</code></p>
<p>Raised after the game returns to the title screen.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
