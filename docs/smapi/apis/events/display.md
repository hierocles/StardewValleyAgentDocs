---
title: "Display"
wiki_source: "Modding:Modder Guide/APIs/Events"
permalink: /Modding:Modder_Guide/APIs/Events/
category: smapi
tags: [events, display]
---
### Display

`this.Helper.Events.Display` has events linked to UI and drawing to the
screen.

<table>
<thead>
<tr>
<th><p>event</p></th>
<th><p>summary</p>
<h4 id="menuchanged">MenuChanged</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>Raised after a game menu is opened, closed, or replaced.</p>
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
<td><p><samp>e.NewMenu</samp></p></td>
<td><p><samp>IClickableMenu</samp></p></td>
<td><p>The new menu instance (or <samp>null</samp> if none).</p></td>
</tr>
<tr>
<td><p><samp>e.OldMenu</samp></p></td>
<td><p><samp>IClickableMenu</samp></p></td>
<td><p>The old menu instance (or <samp>null</samp> if none).</p></td>
</tr>
</tbody>
</table>
<h4 id="rendering">Rendering</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>Raised before the game draws anything to the screen in a draw tick,
as soon as the sprite batch is opened. The sprite batch may be closed
and reopened multiple times after this event is called, but it's only
raised once per draw tick. This event isn't useful for drawing to the
screen, since the game will draw over it.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
</tbody>
</table>
<h4 id="rendered">Rendered</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>Raised after the game draws to the sprite batch in a draw tick, just
before the final sprite batch is rendered to the screen. Since the game
may open/close the sprite batch multiple times in a draw tick, the
sprite batch may not contain everything being drawn and some things may
already be rendered to the screen. Content drawn to the sprite batch at
this point will be drawn over all vanilla content (including menus, HUD,
and cursor).</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
</tbody>
</table>
<h4 id="renderingworld">RenderingWorld</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>Raised before the game world is drawn to the screen. This event isn't
useful for drawing to the screen, since the game will draw over it.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
</tbody>
</table>
<h4 id="renderedworld">RenderedWorld</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>Raised after the game world is drawn to the sprite batch, before it's
rendered to the screen. Content drawn to the sprite batch at this point
will be drawn over the world, but under any active menu, HUD elements,
or cursor.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
</tbody>
</table>
<h4 id="renderingactivemenu">RenderingActiveMenu</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>When a menu is open (<samp>Game1.activeClickableMenu != null</samp>),
raised before that menu is drawn to the screen. This includes the game's
internal menus like the title screen. Content drawn to the sprite batch
at this point will appear under the menu.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
</tbody>
</table>
<h4 id="renderedactivemenu">RenderedActiveMenu</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>When a menu is open (<samp>Game1.activeClickableMenu != null</samp>),
raised after that menu is drawn to the sprite batch but before it's
rendered to the screen. Content drawn to the sprite batch at this point
will appear over the menu and menu cursor.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
</tbody>
</table>
<h4 id="renderinghud">RenderingHud</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>Raised before drawing the HUD (item toolbar, clock, etc) to the
screen. The vanilla HUD may be hidden at this point (<em>e.g.,</em>
because a menu is open). Content drawn to the sprite batch at this point
will appear under the HUD.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
</tbody>
</table>
<h4 id="renderedhud">RenderedHud</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>Raised after drawing the HUD (item toolbar, clock, etc) to the sprite
batch, but before it's rendered to the screen. The vanilla HUD may be
hidden at this point (<em>e.g.,</em> because a menu is open). Content
drawn to the sprite batch at this point will appear over the HUD.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
</tbody>
</table>
<h4 id="windowresized">WindowResized</h4>
<p><em>Group:</em> <code>Display</code></p>
<p>Raised after the game window is resized.</p>
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
<td><p><samp>e.OldSize</samp></p></td>
<td><p><samp>Point</samp></p></td>
<td><p>The previous window width (<samp>e.OldSize.X</samp>) and height
(<samp>e.OldSize.Y</samp>).</p></td>
</tr>
<tr>
<td><p><samp>e.NewSize</samp></p></td>
<td><p><samp>Point</samp></p></td>
<td><p>The new window width (<samp>e.NewSize.X</samp>) and height
(<samp>e.NewSize.Y</samp>).</p></td>
</tr>
</tbody>
</table>
<h4 id="renderingstep">RenderingStep</h4>
<p><em>Group:</em> <code>Display</code></p>
<p><em>(Specialized)</em> Raised before the game draws a specific step
in the rendering cycle. This gives more granular control over render
logic, but is more vulnerable to changes in game updates. Consider using
one of the other render events if possible.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
<tr>
<td><p><samp>e.Step</samp></p></td>
<td><p><samp>RenderSteps</samp></p></td>
<td><p>The step being rendered in the draw cycle.</p></td>
</tr>
</tbody>
</table>
<h4 id="renderedstep">RenderedStep</h4>
<p><em>Group:</em> <code>Display</code></p>
<p><em>(Specialized)</em> Raised after the game draws a specific step in
the rendering cycle. This gives more granular control over render logic,
but is more vulnerable to changes in game updates. Consider using one of
the other render events if possible.</p>
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
<td><p><samp>e.SpriteBatch</samp></p></td>
<td><p><samp>SpriteBatch</samp></p></td>
<td><p>The sprite batch being drawn. Add anything you want to appear
on-screen to this sprite batch.</p></td>
</tr>
<tr>
<td><p><samp>e.Step</samp></p></td>
<td><p><samp>RenderSteps</samp></p></td>
<td><p>The step being rendered in the draw cycle.</p></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
