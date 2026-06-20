---
title: "Specialised"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, specialised]
---
### Specialised

`this.Helper.Events.Specialised` has events for specialised edge cases.
These shouldn't be used by most mods.

<table>
<thead>
<tr>
<th><p>event</p></th>
<th><p>summary</p>
<h4 id="loadstagechanged">LoadStageChanged</h4>
<p><em>Group:</em> <code>Specialised</code></p>
<p>Raised when the low-level stage in the game's loading process has
changed, for mods which need to run code at specific points in the
loading process. The available stages or when they happen might change
without warning in future versions (<em>e.g.,</em> due to changes in the
game's load process), so <strong>mods using this event are more likely
to break or have bugs</strong>. Most mods should use the <a
href="#Game_loop" class="wikilink" title="game loop events">game loop
events</a> instead.</p>
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
<td><p><samp>e.NewStage</samp></p></td>
<td><p><samp>LoadStage</samp></p></td>
<td><p>The new load stage. The possible values are...</p></td>
</tr>
<tr>
<td><p><samp>e.OldStage</samp></p></td>
<td><p><samp>LoadStage</samp></p></td>
<td><p>The previous load stage. See comments for
<samp>e.NewStage</samp>.</p></td>
</tr>
</tbody>
</table>
<h4 id="unvalidatedupdateticking">UnvalidatedUpdateTicking</h4>
<p><em>Also known as:</em> <code>UnvalidatedUpdateTicked</code></p>
<p><em>Group:</em> <code>Specialised</code></p>
<p>Raised before/after the game updates its state (≈60 times per
second), regardless of normal SMAPI validation. This event is not
thread-safe and may be invoked while game logic is running
asynchronously. Changes to game state in this method may crash the game
or corrupt an in-progress save. <strong>Do not use this event unless
you're fully aware of the context in which your code will be run. Using
this event will trigger a warning in the SMAPI console.</strong></p>
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
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
