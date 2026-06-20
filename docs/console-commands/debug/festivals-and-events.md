---
title: "Festivals And Events"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, festivals-and-events]
---
### Festivals and events

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>endevent</samp></p></td>
<td><p>| Immediately end the current event or festival, applying the
event's skip logic (if any). The event is marked seen, but you can
rewatch it using the <samp>eventById</samp> command if needed.</p></td>
<td><p>|<a href="#endevent" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>event</samp></p></td>
<td><p>| <em>Syntax</em>: <code>event</code>
&lt;S:locationName&gt;,&lt;I:index&gt;,[S:clearEventsSeen]</p>
<p>Starts the specified event in the specified location. The location
name is a fuzzy match, but the second parameter is an index rather than
an ID. This is basically a zero-based count of the item definitions in
the appropriate data file, and since these definitions can be altered by
mods this a difficult command to use. Because of this and the warning
below, <a href="#ebi" class="wikilink" title="ebi">ebi</a> is often the
better choice.<br />
<strong>Warning: The third parameter is default to true so this will
clear the eventsSeen list unless a third parameter is
specified.</strong></p></td>
<td><p>|<a href="#event" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>eventbyid</samp><br />
<samp>ebi</samp></p></td>
<td><p>| <em>Syntax</em>: <code>eventbyid</code> &lt;I:eventID&gt;</p>
<p>Starts the specified event. This does take an event ID; events which
have prerequisites of other events might not start if those
prerequisites have not been seen.</p>
<p><em>Example:</em> <code>debug ebi 992559</code> would trigger the
event where Emily visits the farm and gives you access to her sewing
machine.</p></td>
<td><p>|<a href="#eventbyid" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>eventover</samp></p></td>
<td><p>| Ends (and restarts) the current event. Seems to be essentially
equivalent to <a href="#ee" class="wikilink" title="ee">ee</a>.</p></td>
<td><p>|<a href="#eventover" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>eventseen</samp><br />
<samp>seenevent</samp></p></td>
<td><p>| <em>Syntax</em>: <code>eventseen</code>
&lt;I:eventID&gt;,[B:seeOrForget]</p>
<p>Marks specifid event as seen by your farmer. Useful for enabling
access to event-dependent areas or events. You can forget an event
(instead of adding it) by setting the second argument to false, like
<samp>seenEvent &lt;code&gt;&lt;id&gt;&lt;/code&gt;
false</samp>.</p></td>
<td><p>|<a href="#eventseen" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>festival</samp></p></td>
<td><p>| <em>Syntax</em>: <code>festival</code> &lt;S:festivalID&gt;</p>
<p>Starts the specified festival ID. The season, day, and time will be
set to match the starting time, and you will be warped to the correct
location. Valid IDs are listed below.</p></td>
<td><p>|<a href="#festival" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>festivalscore</samp></p></td>
<td><p>| <em>Syntax</em>: <code>festivalscore</code> &lt;I:value&gt;</p>
<p>Adds the specified value to the festival score. The festival score
has different meanings depending on which festival is active and
includes the egg count at the Egg Hunt, number of fish caught at the Ice
Festival, and star token count at the fall Fair.</p></td>
<td><p>|<a href="#festivalscore" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>runtestevent</samp><br />
<samp>rte</samp></p></td>
<td><p>| Runs an event from the file <code>test_event.txt</code> in the
root game folder. The first line of the file should specify the location
where the event takes place, and the rest of the file should be the same
as a normal event script except that line breaks will be treated as
<code>/</code> delimiters.<br />
<strong>Note: this file must use CRLF (Windows-style) line breaks, or it
will fail to parse.</strong> If you are on Mac or Linux, make sure you
convert when saving (any text editor should be able to do
this).</p></td>
<td><p>|<a href="#runtestevent" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setFarmEvent</samp><br />
<samp>sfe</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setFarmEvent</code>
&lt;S:eventID&gt;</p>
<p>Queue an <a href="Random_Events#Farm_events" class="wikilink"
title="overnight farm event">overnight farm event</a> if one doesn't
plan naturally instead. The &lt;event id&gt; can be one of...</p></td>
<td><p>|<a href="#setFarmEvent" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
