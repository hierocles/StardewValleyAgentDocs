---
title: "Schedules"
wiki_source: "Modding:Schedule data"
permalink: /Modding:Schedule_data/
category: npcs
tags: [schedule-data, raw-data, schedule-key, special-schedules, marriage-schedules, normal-schedules, schedule-script, format]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses NPC schedule data,
which determines where NPCs go and what they do when they get there.
This is an advanced guide for mod developers.

## Raw data

Schedule data is stored in `Content/Characters/schedules/*.xnb` files
(one per character), which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data for Abigail as of for reference:

## Schedule key

Each schedule has a key which is used to decide when it applies. The key
must be one of the exact formats below (it's not dynamic). If multiple
schedules apply, the first match in the order listed here is used.

Notes:

- Schedule keys are not case-sensitive.
- The game's logic for schedule keys is in `NPC::TryLoadSchedule()`.

### Special schedules

These are checked first, regardless of marriage status.

| syntax | summary |
|----|----|
| `GreenRain` | Applies on <a href="Weather#Green_Rain" class="wikilink" title="green rain">green
rain</a> days in year 1. |

### Marriage schedules

These apply if the NPC is married to a player (not necessarily the main
player). **Married NPCs don't use any other schedule keys.** If the
marriage keys don't match, they won't have a schedule for that day.

<table>
<thead>
<tr>
<th><p>syntax</p></th>
<th><p>summary</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>marriage_&lt;festival ID&gt;_&lt;festival
day&gt;</samp><br />
<samp>marriage_&lt;festival ID&gt;</samp></p></td>
<td><p>Applies when a passive festival like the <a href="Night_Market"
class="wikilink" title="Night Market">Night Market</a> is active. The
&lt;festival ID&gt; is the key from <samp>Data/PassiveFestivals</samp>,
and &lt;festival day&gt; is the number of days since the passive
festival started (where the first day is 1).</p></td>
</tr>
<tr>
<td><p><samp>marriage_&lt;season&gt;_&lt;day of
month&gt;</samp></p></td>
<td><p>Applies on the given date.<br />
<small>Example: <samp>marriage_spring_26</samp></small></p></td>
</tr>
<tr>
<td><p><samp>marriageJob</samp></p></td>
<td><p>Used by Harvey on Tuesday/Thursday, Maru on Tuesday/Thursday,
Penny on Tuesday/Wednesday/Friday. No other NPC can use
<samp>marriageJob</samp> without C# to change the game code.</p></td>
</tr>
<tr>
<td><p><samp>marriage_&lt;day of week&gt;</samp></p></td>
<td><p>Applies on the given day of week when not raining.<br />
<small>Example: <samp>marriage_Mon</samp></small></p></td>
</tr>
</tbody>
</table>

### Normal schedules

These schedules apply to any non-marriage NPC. If none of these keys
match, they won't have a schedule for that day.

<table>
<thead>
<tr>
<th><p>syntax</p></th>
<th><p>summary</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>&lt;festival ID&gt;_&lt;festival day&gt;</samp><br />
<samp>&lt;festival ID&gt;</samp></p></td>
<td><p>Applies when a passive festival like the <a href="Night_Market"
class="wikilink" title="Night Market">Night Market</a> is active. The
&lt;festival ID&gt; is the key from <samp>Data/PassiveFestivals</samp>,
and &lt;festival day&gt; is the number of days since the passive
festival started (where the first day is 1).</p></td>
</tr>
<tr>
<td><p><samp>&lt;season&gt;_&lt;day of month&gt;</samp></p></td>
<td><p>Applies on the given date.<br />
<small>Example: <samp>spring_15</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;day of month&gt;_&lt;hearts&gt;</samp></p></td>
<td><p>Applies on the given day of month if <em>any</em> player has at
least that many <a href="friendship" class="wikilink"
title="hearts">hearts</a> with the NPC. If multiple schedules apply, the
one with the highest heart number is used.<br />
<small>Example: <samp>11_6</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;day of month&gt;</samp></p></td>
<td><p>Applies on the given day of month.<br />
<small>Example: <samp>16</samp></small></p></td>
</tr>
<tr>
<td><p><samp>bus</samp></p></td>
<td><p>For <a href="Pam" class="wikilink" title="Pam">Pam</a> only,
applies if the bus is repaired.</p></td>
</tr>
<tr>
<td><p><samp>rain2</samp></p></td>
<td><p>50% chance of applying on rainy days.</p></td>
</tr>
<tr>
<td><p><samp>rain</samp></p></td>
<td><p>Applies on rainy days.</p></td>
</tr>
<tr>
<td><p><samp>&lt;season&gt;_&lt;day of
week&gt;_&lt;hearts&gt;</samp></p></td>
<td><p>Applies in the given season and day of week, if <em>any</em>
player has at least that many <a href="friendship" class="wikilink"
title="hearts">hearts</a> with the NPC. If multiple schedules apply, the
one with the highest heart number is used.<br />
<small>Example: <samp>spring_Mon_6</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;season&gt;_&lt;day of week&gt;</samp></p></td>
<td><p>Applies in the given season and day of week.<br />
<small>Example: <samp>spring_Mon</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;day of week&gt;_&lt;hearts&gt;</samp></p></td>
<td><p>Applies on the given day of week, if <em>any</em> player has at
least that many <a href="friendship" class="wikilink"
title="hearts">hearts</a> with the NPC. If multiple schedules apply, the
one with the highest heart number is used.<br />
<small>Example: <samp>Mon_6</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;day of week&gt;</samp></p></td>
<td><p>Applies in the given day of week.<br />
<small>Example: <samp>Mon</samp></small></p></td>
</tr>
<tr>
<td><p><samp>&lt;season&gt;</samp></p></td>
<td><p>Applies in the given season.<br />
<small>Example: <samp>spring</samp></small></p></td>
</tr>
<tr>
<td><p><samp>spring_&lt;day of week&gt;</samp></p></td>
<td><p>Applies (in any season) on the given day of week.<br />
<small>Example: <samp>spring_Mon</samp></small></p></td>
</tr>
<tr>
<td><p><samp>spring</samp></p></td>
<td><p>Always applies. This schedule is also used as a default in some
cases.<br />
DO NOT REMOVE THIS ENTRY. THAT WILL BREAK THE GAME.</p></td>
</tr>
<tr>
<td><p><samp>default</samp></p></td>
<td><p>Also used as a default sometimes. It's okay for this one to not
exist, spring will be used instead.</p></td>
</tr>
</tbody>
</table>

## Schedule script

### Format

Each schedule entry has a
<a href="#Schedule_key" class="wikilink" title="key">key</a>, and a
value containing an arbitrary number of the slash-delimited commands
listed below.

These can be on a single line like this:

``` js
"Wed": "1000 ArchaeologyHouse 11 9 0/1800 Town 47 87 0/2200 SeedShop 1 9 3 abigail_sleep"
```

Or you can add whitespace before or after commands for readability:

``` js
"Wed": "
    1000 ArchaeologyHouse 11 9 0/
    1800 Town 47 87 0/
    2200 SeedShop 1 9 3 abigail_sleep
"
```

### Initial commands

A script may have one initial command as the first field in the script,
before the first `/` character. The `GOTO` command can also appear in
the next two fields after `MAIL`, or the next field after `NOT`.

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>GOTO &lt;key&gt;</samp></p></td>
<td><p>(Note: this line only applies if <samp>GOTO</samp> is the first
command. If it's not, see <samp>GOTO</samp> below.)<br />
End the current script and load the schedule with the given key instead.
The key does not need to be one of the standard keys and can be any
arbitrary string. If the key is "season", the current season name is
used instead. If the schedule doesn't exist or can't be parsed, the
<samp>spring</samp> schedule will be used instead.<br />
<small>Example: <samp>GOTO spring</samp></small></p></td>
</tr>
<tr>
<td><p><samp>NOT friendship &lt;npc name&gt;
&lt;hearts&gt;</samp></p></td>
<td><p>End the current script if <em>any</em> player <em>does</em> have
at least that many <a href="friendship" class="wikilink"
title="hearts">hearts</a> with any of the named NPCs (can list
multiple). If the script is ended, the <samp>spring</samp> schedule is
used instead.<br />
<small>Example: <samp>NOT friendship Sebastian 6 Abigail 3</samp>
(script ends if any player has 6+ hearts with Sebastian and/or 3+ hearts
with Abigail).</small></p></td>
</tr>
<tr>
<td><p><samp>NOT</samp></p></td>
<td><p>Command ignored if the next word is not
<samp>friendship</samp>.</p></td>
</tr>
<tr>
<td><p><samp>MAIL &lt;letter ID&gt;</samp></p></td>
<td><p>Runs the next command if the player did <em>not</em> receive the
given letter ID or world state ID (see <samp>HasFlag</samp> in the <a
href="https://github.com/Pathoschild/StardewMods/tree/develop/ContentPatcher">Content
Patcher documentation</a>); else continues from the command after
that.<br />
<small>Example: <samp>MAIL ccVault/GOTO spring/GOTO summer</samp> (runs
<samp>GOTO summer</samp> if the bus is repaired, or <samp>GOTO
spring</samp> if it isn't; not limited to <samp>GOTO</samp>
commands).</small></p></td>
</tr>
<tr>
<td><p><samp>GOTO &lt;key&gt;</samp></p></td>
<td><p>(Note: this line only applies if <samp>GOTO</samp> is after
<samp>NOT</samp> or <samp>MAIL</samp>. If it's not, see
<samp>GOTO</samp> above.)<br />
End the current script and load the schedule with the given key instead.
If the key is "season", the current season name is used instead. If the
key is "NO_SCHEDULE", the NPC has no schedule for the day. If the
schedule doesn't exist or can't be parsed, the game crashes (or shows an
error if playing with SMAPI).<br />
<small>Example: <samp>GOTO NO_SCHEDULE</samp></small></p></td>
</tr>
</tbody>
</table>

### Schedule points

The rest of the schedule script consists of slash-delimited entries,
each containing space-separated fields which specify a start time,
destination, and what to do when the NPC reaches it:


`<time> [location] <tileX> <tileY> [facingDirection] [animation] [dialogue]`

If the `location` field is omitted, the rest of the fields are parsed as
normal. The other optional fields must be in sequential order (*e.g.,*
you can skip `animation` and `dialogue`, but you can't skip
`facingDirection` and then specify `animation` and `dialogue`). The
exception is `dialogue`. The `dialogue` can be specified without the
`animation`.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>time</samp></p></td>
<td><p>The time at which the schedule event begins, in military time (24
hour format, no colon). The time may be preceded with the single
character '<samp>a</samp>' to indicate that the event should end (that
is, the NPC should arrive at the destination) at the given time. In this
case, the game will calculate when the event needs to begin. However,
the event will never begin before the time specified for the previous
event.</p>
<p>In the unmodified game, this is only used to synchronise Emily's and
Sandy's schedules on Fall 15.</p></td>
</tr>
<tr>
<td><p><samp>location</samp></p></td>
<td><p><em>(optional)</em> The location name the NPC should walk
towards. If omitted, defaults to the previous map, or if it's the first,
it defaults to the <a href="Bus_Stop" class="wikilink"
title="bus stop">bus stop</a> (if married to a player) or their default
location.</p>
<p><strong>Note:</strong> the game has special logic for unlockable
locations. If this is JojaMart/Railroad and it's not available yet, the
game gets the replacement destination from the first entry in the
<samp>&lt;location&gt;_Replacement</samp> schedule if available;
otherwise it switches to the <samp>default</samp> schedule if available,
else <samp>spring</samp>. If this is CommunityCenter and it's not
available yet, the game switches to the <samp>default</samp> schedule if
available, else <samp>spring</samp>.</p>
<p><strong>Note also:</strong> if the location is <code>bed</code>, the
game will ignore the remaining parameters from this schedule point and
attempt to load a "home" destination (map and coordinates): the warp out
of <code>BusStop</code> back to the <code>Farm</code> for married NPCs,
or for unmarried ones, the last schedule entry from the
<code>default</code> or <code>spring</code> schedule (or the NPC's
default location, if neither schedule can be loaded or parsed
correctly). The NPC's <a href="Modding_NPC_data#Sleep_animation"
class="wikilink" title="sleeping animation">sleeping animation</a>
(<code>&lt;lowercase name&gt;_sleep</code>) from
<code>Data/animationDescriptions</code> will be set to play on arrival
if it is defined.</p></td>
</tr>
<tr>
<td><p><samp>tileX</samp><br />
<samp>tileY</samp></p></td>
<td><p>The X and Y <a
href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
title="tile coordinates">tile coordinates</a> the NPC should walk
towards.</p></td>
</tr>
<tr>
<td><p><samp>facingDirection</samp></p></td>
<td><p><em>(optional)</em> The direction to face after reaching the
destination. The possible values are 0 (up), 1 (right), 2 (down), and 3
(left). Defaults to down.</p></td>
</tr>
<tr>
<td><p><samp>animation</samp></p></td>
<td><p><em>(optional)</em> The animation to play when the NPC reaches
the destination. This must be a key that appears in the
<samp>Content/Data/animationDescriptions.xnb</samp> file. Each key entry
has three required parts: entry frames/repeat frames/leaving frames. The
numbers on them refer to the <a
href="Modding_NPC_data#Overworld_sprites" class="wikilink"
title="overworld sprite frame">overworld sprite frame</a>. The entry
frames will play after arriving at the schedule point. Then the repeat
frames will loop until the end of schedule time. Finally, the leaving
frames will play before moving on to the next schedule point. Note that
each frame is around 120ms so duplicates of frame is used to get desired
looking animation.<br />
<br />
The full format is <samp>entry frames/repeat frames/leaving
frames/message key/laying_down/offset X Y</samp>. If a message key is
given, the NPC will repeat that message if you talk to them while they
are performing the animation. <samp>offset X Y</samp> lets you offset
their sprite (in pixels). <samp>laying_down</samp> will hide the shadow.
If you want to use offset or laying_down without a message, leave that
spot empty. The order of <samp>offset</samp> and
<samp>laying_down</samp> do not matter and either can be used without
the other.<br />
Example offset/laying down without message: <samp>"haley_beach_towel":
"20 20 21 21 21 21 21/22/21 21 20//laying_down/offset 0 16"</samp><br />
Example offset without message or laying_down:
<samp>"haley_beach_towel": "20 20 21 21 21 21 21/22/21 21 20//offset 0
16"</samp> (note there are now only 5 fields, not 6).<br />
<br />
Additionally, there are a few special animations. <samp>sleep</samp>
anywhere in an animation name causes the NPC to go to sleep (which,
among other things, prevents players from gifting or talking to the NPC
while the animation is active.) The specific animation
<samp>NPCName_sleep</samp> (with the NPCName fully lowercased)
automatically used by spouses when they turn in for the night, and by
NPCs coming home from Ginger Island. <samp>square_X_Y_facing</samp>
causes NPCs to make random movements in a rectangle of at most X by Y
(it can be less), centered at the schedule point. They will occasionally
pause and face the <samp>facing</samp> direction.
<samp>change_beach</samp> and <samp>change_normal</samp> cause NPCs to
change into and out of their beach outfits, and is used by Ginger Island
resort schedules.</p></td>
</tr>
<tr>
<td><p><samp>dialogue</samp></p></td>
<td><p><em>(optional)</em> The dialogue the NPC should use when they
reach their destination. This must be an <a
href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="asset name">asset name</a> and entry key in this exact format
(including quotes): <samp>"assetName:key"</samp>. Any slashes in the
asset name should be double backslashes (<samp>\\</samp>). The format of
the entry key doesn't matter, it just needs to match one in the
file.</p>
<p>For example, <samp>"Strings\\schedules\\Abigail:Sun.000"</samp> means
"open the file at <samp>Strings\schedules\Abigail.xnb</samp> and get the
text of the <samp>Sun.000</samp> key".</p>
<p><small>Tip: If you want schedule dialogue in marriage schedules,
include the exact string <samp>marriage</samp> somewhere in the key,
that will only show it to the npc's spouse.</small></p></td>
</tr>
</tbody>
</table>

For example, consider this schedule entry in Abigail's schedule:

    1300 Town 47 87 0 \"Strings\\schedules\\Abigail:marriage_Mon.001\"

At 13:00 (1pm), Abigail will begin walking to tile (47, 87) in the Town
location. When she reaches it, she'll face direction 0 (up) and say
"*Hey, @. I like to relax here... it's so peaceful.*"

## Limitations

- When an NPC is added to an existing save, they generally don't follow
  their schedule correctly until you've slept once in-game (which
  triggers their first day update).
- Using a time of 600 (when the day starts) for an event may not work.
  Try using 610 if you want an event early in the morning and the NPC
  doesn't move if you use 600.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Datos_de_horarios" class="wikilink"
title="es:Modding:Datos de horarios">es:Modding:Datos de horarios</a>
<a href="ru_Модификации_Расписание" class="wikilink"
title="ru:Модификации:Расписание">ru:Модификации:Расписание</a>
<a href="zh_模组_行程数据" class="wikilink"
title="zh:模组:行程数据">zh:模组:行程数据</a>
