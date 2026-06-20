---
title: "Player"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, player, world, other, advanced, debug-commands, how-to-enter-debug-commands, macros]
---
### Player

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
<td><p><samp>player_changecolor</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_changecolor</code>
&lt;S:feature&gt;, &lt;S:color&gt;</p>
<p>Sets a color for your character's sprite.</p>
<p><em>Example:</em> <code>player_changecolor eyes 255,0,0</code> would
make your character's eyes red.</p></td>
<td><p>|<a href="#player_changecolor" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_changestyle</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_changestyle</code>
&lt;S:target&gt;, &lt;I:style ID&gt;</p>
<p>Sets a style for your character's sprite.</p>
<p><em>Example:</em> <code>player_setstyle swim 1</code> would change
the player into their swim suit.</p></td>
<td><p>|<a href="#player_changestyle" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_sethealth</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_sethealth</code>
&lt;I:amount&gt;</p>
<p>Sets the player's current <a href="health" class="wikilink"
title="health">health</a>.</p>
<p><em>Example:</em> <code>player_sethealth 200</code> would set you to
200 health points.</p></td>
<td><p>|<a href="#player_sethealth" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_setimmunity</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_setimmunity</code>
&lt;I:amount&gt;</p>
<p>Sets the player's total <a href="immunity" class="wikilink"
title="immunity">immunity</a>. This is permanent and is affected by
immunity buffs. For example, if you set immunity 10 while <a
href="Genie_Shoes" class="wikilink" title="Genie Shoes">Genie Shoes</a>
(+6 immunity) are equipped, removing the shoes would set your immunity
to 4 (10 - 6). You can reset immunity to normal by removing everything
that improves immunity, then entering
<code>player_setimmunity 0</code>.</p>
<p><em>Example:</em> <code>player_setimmunity 10</code> would give you
10 immunity points, or a 100% chance of avoiding buff effects.</p></td>
<td><p>|<a href="#player_setimmunity" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_setmaxhealth</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_setmaxhealth</code>
&lt;I:amount&gt;</p>
<p>Sets the player's maximum <a href="health" class="wikilink"
title="health">health</a>. This permanently changes the baseline; for
example, if you set your max health to 500 and then drink <a
href="Skull_Cavern#Secret" class="wikilink"
title="Iridium Snake Milk">Iridium Snake Milk</a>, your max health will
increase to 525.</p>
<p><em>Example:</em> <code>player_setmaxhealth 500</code> would give you
a maximum of 500 health points.</p></td>
<td><p>|<a href="#player_setmaxhealth" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_setmaxstamina</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_setmaxstamina</code>
&lt;I:amount&gt;</p>
<p>Sets the player's maximum <a href="energy" class="wikilink"
title="stamina">stamina</a>. This permanently changes the baseline; for
example, if you set your max stamina to 300 and then collect a <a
href="Stardrop" class="wikilink" title="Stardrop">Stardrop</a>, your max
stamina will increase to 334.</p>
<p><em>Example:</em> <code>player_setmaxstamina 500</code> would give
you a maximum of 500 stamina points.</p></td>
<td><p>|<a href="#player_setmaxstamina" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_setname</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_setname</code>
&lt;S:target&gt;,&lt;S:name&gt;</p>
<p>Sets the name of the current player or their farm, depending on the
&lt;S:target&gt; value (<samp>player</samp> or <samp>farm</samp>).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>player_setname player Malon</code> would change your player
name to Malon.</li>
</ul>
<ul>
<li><code>player_setname farm "Lon Lon"</code> would change your farm
name to Lon Lon Farm.</li>
</ul></td>
<td><p>|<a href="#player_setname" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_setstamina</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_setstamina</code>
&lt;I:amount&gt;</p>
<p>Sets the player's current <a href="energy" class="wikilink"
title="stamina">stamina</a>.</p>
<p><em>Example:</em> <code>player_setstamina 200</code> would give you
200 stamina points.</p></td>
<td><p>|<a href="#player_setstamina" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### World

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
<td><p><samp>hurry_all</samp></p></td>
<td><p>| Immediately warps all NPCs to their scheduled positions. (To
hurry a single NPC, use <a href="#Debug_commands" class="wikilink"
title="debug hurry npc-name"><samp>debug hurry npc-name</samp></a>
instead.)</p></td>
<td><p>|<a href="#hurry_all" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>set_farm_type list</samp></p></td>
<td><p>| Shows a list of farm types you can use with the
<samp>set_farm_type</samp> command.</p></td>
<td><p>|<a href="#set_farm_type_list" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>set_farm_type</samp></p></td>
<td><p>| <em>Syntax</em>: <code>set_farm_type</code> &lt;S:farm
type&gt;</p>
<p>Sets the player's current <a href="Farm_Maps" class="wikilink"
title="farm type">farm type</a>, where &lt;I:farm type&gt; is one of
<samp>0</samp> (Standard), <samp>1</samp> (Riverlands), <samp>2</samp>
(forest), <samp>3</samp> (Hilltop), <samp>4</samp> (Combat),
<samp>5</samp> (Four Corners), <samp>6</samp> (Beach), <samp>7</samp>
(Meadowlands) or a custom farm type ID. You can enter
<code>set_farm_type list</code> for a list of valid farm type IDs.</p>
<p><em>Example:</em> <code>set_farm_type 1</code> will set the farm type
to riverlands.</p></td>
<td><p>|<a href="#set_farm_type" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>world_clear</samp></p></td>
<td><p>| <em>Syntax</em>: <code>world_clear</code>
&lt;S:location&gt;,&lt;S:entity type&gt;</p>
<p>Removes all entities of the given type from a location.</p>
<p><em>Example:</em> <code>world_clear current debris</code> will remove
all debris (sticks, stones, and small plants).</p></td>
<td><p>|<a href="#world_clear" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>world_downminelevel</samp></p></td>
<td><p>| Goes down one mine level. If you're not in the mines, warps you
to the first mine level.</p></td>
<td><p>|<a href="#world_downminelevel" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>world_freezetime</samp></p></td>
<td><p>| <em>Syntax</em>: <code>world_freezetime</code>
&lt;I:action&gt;</p>
<p>Freezes or resumes the time. The [I:action] can be <samp>0</samp>
(resume time) or <samp>1</samp> (freeze time); if omitted, time is
toggled.</p></td>
<td><p>|<a href="#world_freezetime" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>world_setday</samp></p></td>
<td><p>| <em>Syntax</em>: <code>world_setday</code> &lt;I:day&gt;</p>
<p>Sets the day of month.</p>
<p><em>Example:</em> <code>world_setday 30</code> will set the date to
the 30th of the current season.</p></td>
<td><p>|<a href="#world_setday" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>world_setminelevel</samp></p></td>
<td><p>| <em>Syntax</em>: <code>world_setminelevel</code> &lt;I:mine
level&gt;</p>
<p>Warps you to the given mine level. This can be the <a
href="The_Mines" class="wikilink" title="regular mines">regular
mines</a> (levels 1–120), <a href="Skull_Cavern" class="wikilink"
title="Skull Cavern">Skull Cavern</a> (121+), or <a href="Quarry_Mine"
class="wikilink" title="Quarry Mine">Quarry Mine</a> (77377).</p>
<p><em>Example:</em> <code>world_setminelevel 80</code> warps to mine
level 80.</p></td>
<td><p>|<a href="#world_setminelevel" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>world_setseason</samp></p></td>
<td><p>| <em>Syntax</em>: <code>world_setseason</code>
&lt;S:season&gt;</p>
<p>Sets the season (one of <samp>spring</samp>, <samp>summer</samp>,
<samp>fall</samp>, or <samp>winter</samp>).</p>
<p><em>Example:</em> <code>world_setseason spring</code> will set the
season to spring.</p></td>
<td><p>|<a href="#world_setseason" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>world_settime</samp></p></td>
<td><p>| <em>Syntax</em>: <code>world_settime</code> &lt;I:time&gt;</p>
<p>Sets the time of day, using the game's 26-hour time format (from 0600
for 6am at the start of day, to 2600 for 2am at the end of day).</p>
<p><em>Example:</em> <code>world_settime 1430</code> will set time to
2:30pm.</p></td>
<td><p>|<a href="#world_settime" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>world_setyear</samp></p></td>
<td><p>| <em>Syntax</em>: <code>world_setyear</code> &lt;I:year&gt;</p>
<p>Sets the year number.</p>
<p><em>Example:</em> <code>world_setyear 10</code> will set the the game
to the 10th year.</p></td>
<td><p>|<a href="#world_setyear" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Other

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
<td><p><samp>harmony_summary</samp></p></td>
<td><p>| <em>Syntax</em>: <code>harmony_summary</code> [S:search]</p>
<p>Lists the <a href="Modding_Modder_Guide_APIs_Harmony"
class="wikilink" title="Harmony patches">Harmony patches</a> added by
SMAPI and other mods. If [S:search] is given, only patched method names
matching any of the search terms will be listed.</p>
<p><em>Example:</em> <code>harmony_summary MeleeWeapon</code> will list
patches which affect the <samp>MeleeWeapon</samp> class in the game
code.</p></td>
<td><p>|<a href="#harmony_summary" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>help</samp></p></td>
<td><p>| <em>Syntax</em>: <code>help</code> [S:command name]</p>
<p>Provides documentation for console commands. If called without an
argument, shows general help text and a list of available commands. If
called with a command name, shows the documentation for that
command.</p></td>
<td><p>|<a href="#help" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>log_context</samp></p></td>
<td><p>| Enables logging more contextual info like buttons pressed,
menus changed, etc. For example, it can be used to get <a
href="Modding_Player_Guide_Key_Bindings" class="wikilink"
title="key binding codes">key binding codes</a> or to simplify
troubleshooting. This is enabled until you restart the game, or run the
command again to disable it.</p></td>
<td><p>|<a href="#log_context" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>reload_i18n</samp></p></td>
<td><p>| Reload <a href="Modding_Translations" class="wikilink"
title="translation files">translation files</a> for all mods. This is
mainly useful when translating mods. (Note that if a mod caches the
text, it may show the old version until it updates.)</p></td>
<td><p>|<a href="#reload_i18n" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>set_verbose</samp></p></td>
<td><p>| <em>Syntax</em>: <code>set_verbose</code> [enable] [mod
ID]+</p>
<p>Toggles whether more detailed information is written to the SMAPI log
file (and console in developer mode). This may impact performance. This
doesn't affect mods manually set to verbose in the config file.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>set_verbose</code>: toggle verbose logs for SMAPI and all
mods.</li>
</ul>
<ul>
<li><code>set_verbose 1</code>: enable verbose logs for SMAPI and all
mods.</li>
</ul>
<ul>
<li><code>set_verbose 1 SMAPI Pathoschild.ContentPatcher</code>: enable
verbose logs for SMAPI and Content Patcher.</li>
</ul></td>
<td><p>|<a href="#set_verbose" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>show_data_files</samp></p></td>
<td><p>| Opens the folder containing the save and log files.</p></td>
<td><p>|<a href="#show_data_files" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>show_game_files</samp></p></td>
<td><p>| Opens the <a
href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
class="wikilink" title="game folder">game folder</a>.</p></td>
<td><p>|<a href="#show_game_files" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Mods may also add their own commands. For example, Content Patcher adds
the `patch` command, documented
[here](https://github.com/Pathoschild/StardewMods/blob/develop/ContentPatcher/docs/author-guide/troubleshooting.md).

### Advanced

⚠️ These may corrupt or make permanent changes to your save. DO NOT USE
THESE unless you're absolutely sure.

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
<td><p><samp>apply_save_fix</samp></p></td>
<td><p>| <em>Syntax</em>: <code>apply_save_fix</code> &lt;S:fix
ID&gt;</p>
<p>Applies one of the game's save migrations to the currently loaded
save. Parameters:</p>
<p><em>Examples:</em></p>
<ul>
<li><code>apply_save_fix list</code> would show a list of save
fixes.</li>
</ul>
<ul>
<li><code>apply_save_fix AddCampfireKit</code> would add <a
href="Cookout_Kit" class="wikilink" title="Cookout Kit">Cookout Kit</a>
to the player's crafting recipes if they meet the requirements for
it.</li>
</ul></td>
<td><p>|<a href="#apply_save_fix" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>debug</samp></p></td>
<td><p>| <em>Syntax</em>: <code>debug</code> &lt;*:command text&gt;</p>
<p>Executes one of the game's debug commands. See <a
href="#Debug_commands" class="wikilink" title="debug commands"><em>debug
commands</em></a> below for more info.</p></td>
<td><p>|<a href="#debug" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>regenerate_bundles</samp></p></td>
<td><p>| <em>Syntax</em>: <code>regenerate_bundles</code> [S:type]
[*:flags]</p>
<p>Regenerates your community center bundle data. This will
<strong>reset all bundle progress</strong>, and may have unintended
effects if you've already completed bundles. Parameters:</p>
<p><em>Examples:</em></p>
<ul>
<li><code>regenerate_bundles confirm</code> will regenerate bundles
using the save's current settings.</li>
</ul>
<ul>
<li><code>regenerate_bundles remixed ignore_seed confirm</code> will
regenerate using randomized <a href="Remixed_Bundles" class="wikilink"
title="remixed bundles">remixed bundles</a>.</li>
</ul></td>
<td><p>|<a href="#regenerate_bundles" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Debug commands

**ERROR:** **Don't use these commands unless you're aware of the
possible consequences.**These are meant for the game developers, not
players. They may crash your game, permanently corrupt or break your
save, or cause other problems. Using these in a save you care about is
not recommended.

### How to enter debug commands

The game itself has hundreds of hidden debug commands used to test the
game. These <a href="#Console_commands" class="wikilink"
title="require the Console Commands mod">require the Console Commands
mod</a> too, but **every command should be prefixed with `debug`** like
this:

    debug where Robin
    > Robin is at Farm, 21,4

The example above returned output, but many commands don't. If there's
no output, SMAPI will say *Sent debug command to the game, but there was
no output*.

### Macros

Instead of entering each command directly into the SMAPI console, you
can also use the `[[#runmacro|debug runmacro]]` command to a list of
debug commands from a text file. (This doesn't work with the non-debug
commands.) Here's how to use it:

1.  Create a text file in
    <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
    class="wikilink" title="your game folder">your game folder</a> (with
    a `.txt` extension).
2.  Type commands in this file, one command per line. Each command
    should start with a slash character (`/`), but should not include
    `debug`.
3.  To run the macro, type `debug runmacro <filename>` in the SMAPI
    console, replacing `<filename>` with the name of your command file
    with the `.txt` extension.

For example, let's say you have a `quickstart.txt` file with these
commands:

    /backpack 12
    /Money 10000
    /levelup 0 1
    /weapon 5

Entering `debug runmacro quickstart` in the SMAPI console will execute
all the commands, resulting in a backpack upgrade, money set to 10000g,
farming skill set to level 1, and a
<a href="Bone_Sword" class="wikilink" title="Bone Sword">Bone Sword</a>
added to the player's inventory. (Note: `Money` is capitalized in this
example because if it is all lowercase it triggers a
<a href="Secrets#Chat" class="wikilink"
title="special chat response">special chat response</a> instead of
executing the command.)

### Actions and queries

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
<td><p><samp>action</samp></p></td>
<td><p>| <em>Syntax</em>: <code>action</code> &lt;S:action&gt;</p>
<p>Run a <a href="Modding_Trigger_actions" class="wikilink"
title="trigger action string">trigger action string</a>.</p>
<p><em>Example:</em> <code>action AddMoney 500</code> will add 500 g to
the current player.</p></td>
<td><p>|<a href="#action" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>gamequery</samp><br />
<samp>gq</samp></p></td>
<td><p>| <em>Syntax</em>: <code>gamequery</code> &lt;S:query&gt;</p>
<p>Check whether the given <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> matches
in the current context.</p>
<p><em>Example:</em></p></td>
<td><p>|<a href="#gamequery" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>itemquery</samp><br />
<samp>iq</samp></p></td>
<td><p>| <em>Syntax</em>: <code>itemquery</code> &lt;S:query&gt;</p>
<p>Open a shop menu with all the items matching an <a
href="Modding_Item_queries" class="wikilink" title="item query">item
query</a> (all items free).</p>
<p><em>Examples:</em></p>
<ul>
<li><samp>debug iq ALL_ITEMS</samp> shows all items</li>
</ul>
<ul>
<li><samp>debug iq ALL_ITEMS (W)</samp> shows all weapons</li>
</ul>
<ul>
<li><samp>debug iq (O)128</samp> shows a pufferfish (object 128)</li>
</ul>
<ul>
<li><samp>debug iq FLAVORED_ITEM Wine (O)128</samp> shows Pufferfish
Wine.</li>
</ul></td>
<td><p>|<a href="#itemquery" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>search</samp></p></td>
<td><p>| <em>Syntax</em>: <code>search</code> [S:term]</p>
<p>List all debug commands that match the given search term (or all
debug commands if the search term is omitted).</p>
<p><em>Example:</em></p></td>
<td><p>|<a href="#search" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>tokens</samp></p></td>
<td><p>| <em>Syntax</em>: <code>tokens</code>
&lt;S:tokenizedString&gt;</p>
<p>Parses a <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> and prints its
output.</p>
<p><em>Example:</em></p></td>
<td><p>|<a href="#tokens" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Items and inventory

#### General item search and spawning

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
<td><p><samp>createDebris</samp></p></td>
<td><p>| <em>Syntax</em>: <code>createDebris</code> &lt;I:item
ID&gt;</p>
<p>Spawns an item with the given <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a> on the ground at your feet.</p>
<p><em>Example:</em> <code>debug createDebris 24</code> would spawn a <a
href="parsnip" class="wikilink" title="parsnip">parsnip</a>.</p></td>
<td><p>|<a href="#createDebris" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>doesItemExist</samp></p></td>
<td><p>| <em>Syntax</em>: <code>doesItemExist</code> &lt;S:item
ID&gt;</p>
<p>Searches the entire world (including other players' inventories) to
see if the <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a> exists anywhere. If you search with the name of
the item, make sure that it's Capitalized for each word in the item's
name, between "quotation mark" and there's no space between the words. A
global message saying <em>Yes</em> or <em>No</em> will be displayed, but
there's no indication of where the item is located if it is found. See
the <samp>whereIsItem</samp> command for more detailed output.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug doesItemExist 24</code> or
<code>debug doesItemExist (O)24</code> or
<code>debug doesItemExist "Parsnip"</code> will search for
parsnips.</li>
</ul>
<ul>
<li><code>debug doesItemExist "river jelly"</code> would respond with
"No" but <code>debug doesItemExist "RiverJelly"</code> would search for
River Jelly and respond with "Yes"</li>
</ul></td>
<td><p>|<a href="#doesItemExist" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>furniture</samp><br />
<samp>ff</samp></p></td>
<td><p>| <em>Syntax</em>: <code>furniture</code> [item ID]</p>
<p>Adds a <a href="Modding_Furniture" class="wikilink"
title="furniture">furniture</a>-type item to your inventory based on its
<a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="unqualified item ID">unqualified item ID</a>. If the item ID is
omitted, a random furniture with ID 0–1612 will be added.</p>
<p><em>Example:</em> <code>debug furniture 704</code> would give you an
<a href="Oak_Dresser" class="wikilink" title="Oak Dresser">Oak
Dresser</a>.</p></td>
<td><p>|<a href="#furniture" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fuzzyItemNamed</samp><br />
<samp>fin</samp><br />
<samp>f</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fuzzyItemNamed</code> &lt;S:name
search&gt;,[I:amount],[I:quality]</p>
<p>Adds the specified item to your inventory based on a fuzzy search for
&lt;item name&gt; across all item types. Only the first matching item
will be spawned. The item name can be quoted to include spaces. The
optional parameters are for stack size (default 1) and <a
href="Modding_Items#Quality" class="wikilink"
title="quality">quality</a> (default 0).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug fuzzyItemNamed sturg 5 4</code> would give you a stack
of five iridium-quality <a href="sturgeon" class="wikilink"
title="sturgeon">sturgeon</a>.</li>
</ul>
<ul>
<li><code>debug fin "galaxy sword"</code> would give you a <a
href="Galaxy_Sword" class="wikilink" title="Galaxy Sword">Galaxy
Sword</a>.</li>
</ul>
<ul>
<li><code>debug f grief</code> would give you a <a
href="Tailoring#Shirts" class="wikilink"
title="&quot;Good Grief&quot; shirt">"Good Grief" shirt</a>.</li>
</ul></td>
<td><p>|<a href="#fuzzyItemNamed" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>getIndex</samp></p></td>
<td><p>| <em>Syntax</em>: <code>getIndex</code> &lt;S:name
search&gt;</p>
<p>Shows the display name and <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified item ID">qualified item ID</a> for the item matching
the fuzzy search (see <code>fuzzyItemNamed</code> for search
syntax).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug getIndex prisma</code> would output <em>Prismatic
Shard's qualified ID is (O)74</em>.</li>
</ul>
<ul>
<li><code>debug getIndex grief</code> would output <em>"Good Grief"
Shirt's qualified ID is (S)1008</em>.</li>
</ul></td>
<td><p>|<a href="#getIndex" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>holdItem</samp></p></td>
<td><p>| Plays the animation where the player holds an item up above
their head. Uses the player's current item.</p></td>
<td><p>|<a href="#holdItem" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>item</samp><br />
<samp>i</samp></p></td>
<td><p>| <em>Syntax</em>: <code>item</code> &lt;S:item
ID&gt;,[I:amount],[I:quality]</p>
<p>Adds an item to your inventory based on its <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a>. The optional parameters are for stack size (default 1) and <a
href="Modding_Items#Quality" class="wikilink"
title="quality">quality</a> (default 0).</p>
<p><em>Example:</em> <code>debug item 74</code> or
<code>debug item (O)74</code> would give you a <a href="Prismatic_Shard"
class="wikilink" title="prismatic shard">prismatic shard</a>.</p></td>
<td><p>|<a href="#item" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>itemNamed</samp><br />
<samp>in</samp></p></td>
<td><p>| <em>Syntax</em>: <code>itemNamed</code> &lt;S:item
name&gt;,[I:amount],[I:quality]</p>
<p>Adds <a href="Modding_Objects" class="wikilink"
title="object">object</a>-type items whose internal names exactly equals
the &lt;item name&gt; (case-insensitive) to your inventory. The optional
parameters are for stack size (default 1) and <a
href="Modding_Items#Quality" class="wikilink"
title="quality">quality</a> (default 0).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug itemNamed "miner's treat"</code> would give you <a
href="Miner&#39;s_Treat" class="wikilink"
title="miner&#39;s treat">miner's treat</a>.</li>
</ul>
<ul>
<li><code>debug in "strange doll" 3</code> would give you 3 of each of
the strange doll <a href="artifacts" class="wikilink"
title="artifacts">artifacts</a>.</li>
</ul></td>
<td><p>|<a href="#itemNamed" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>lookup</samp><br />
<samp>lu</samp></p></td>
<td><p>| <em>Syntax</em>: <code>lookup</code> &lt;S:name search&gt;</p>
<p>Outputs the <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="unqualified item ID">unqualified item ID</a> of
each <a href="Modding_Objects" class="wikilink"
title="object">object</a>-type item whose internal name contains the
&lt;name search&gt; (case-insensitive).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug lookup diamond</code> would output <em>Diamond
72</em>.</li>
</ul>
<ul>
<li><code>debug lu strange doll</code> would output <em>Strange Doll
126</em> and <em>Strange Doll 127</em>.</li>
</ul></td>
<td><p>|<a href="#lookup" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>qualifiedId</samp></p></td>
<td><p>| Shows the held item's display name and <a href="#Custom_items"
class="wikilink" title="qualified item ID">qualified item
ID</a>.</p></td>
<td><p>|<a href="#qualifiedId" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>tv</samp></p></td>
<td><p>| Adds a <a href="Budget_TV" class="wikilink"
title="budget TV">budget TV</a> or <a href="Plasma_TV" class="wikilink"
title="plasma TV">plasma TV</a> to your inventory (each has an equal
random chance).</p></td>
<td><p>|<a href="#tv" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>wallpaper</samp><br />
<samp>wp</samp></p></td>
<td><p>| <em>Syntax</em>: <code>wallpaper</code> [I:item ID]</p>
<p>Adds a floorpaper or wallpaper item to the inventory. If a numeric
wallpaper/flooring ID is specified, spawns that one; otherwise it
randomly chooses one from floor IDs 0–39 or wallpaper IDs
0–111.</p></td>
<td><p>|<a href="#wallpaper" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>whereIsItem</samp><br />
<samp>whereItem</samp></p></td>
<td><p>| <em>Syntax</em>: <code>whereIsItem</code> &lt;S:item ID&gt;</p>
<p>Searches the entire world (including other players' inventories) for
items matching the <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a>, and lists all matches.</p>
<p><em>Example:</em></p></td>
<td><p>|<a href="#whereIsItem" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Backpack and inventory

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
<td><p><samp>backpack</samp></p></td>
<td><p>| <em>Syntax</em>: <code>backpack</code> &lt;I:amount&gt;</p>
<p>Increases your inventory space by the specified amount; capped at 36
slots.</p></td>
<td><p>|<a href="#backpack" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clear</samp><br />
<samp>ci</samp></p></td>
<td><p>| Removes all items currently in your inventory.</p></td>
<td><p>|<a href="#clear" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fillbackpack</samp><br />
<samp>fillbp</samp><br />
<samp>fill</samp><br />
<samp>fbp</samp></p></td>
<td><p>| Fills all empty spaces in your inventory with random Objects.
Any objects spawned by this command will not be marked as found on the
collections tab.</p></td>
<td><p>|<a href="#fillbackpack" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>sl</samp><br />
<samp>shiftToolbarLeft</samp></p></td>
<td><p>| Shifts inventory rows down, looping previous bottom row to top;
similar to using Control-Tab with default keyboard controls. Will work
with larger-than-normal inventories.</p></td>
<td><p>|<a href="#sl" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>sr</samp><br />
<samp>shiftToolbarRight</samp></p></td>
<td><p>| Shifts inventory rows up, looping previous top row to bottom;
similar to using Tab with default keyboard controls. Will work with
larger-than-normal inventories.</p></td>
<td><p>|<a href="#sr" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Clothing and tailoring

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
<td><p><samp>dye</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dye</code> &lt;S:itemType&gt;,
&lt;S:color&gt;, &lt;F:strength&gt;</p>
<p>Dyes the specified (currently equipped) item the specified color.
Item type can be <samp>shirt</samp> or <samp>pants</samp> and valid
colors are <samp>black</samp>, <samp>blue</samp>, <samp>green</samp>,
<samp>red</samp>, <samp>white</samp>, and <samp>yellow</samp>. Strength
is a float between 0 and 1 inclusive; the higher the number, the more
vibrant the color. The dye will mix with the current color so it is
sometimes necessary to "reset" the item by dyeing first with white
strength 1.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug dye shirt red 0.33</code> would dye your current shirt a
shade of pink.</li>
</ul>
<ul>
<li><code>debug dye pants blue 1</code> would dye your current pants
bright blue.</li>
</ul></td>
<td><p>|<a href="#dye" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dyeAll</samp></p></td>
<td><p>| Seems to be intended to bring up a character customization menu
with HSV sliders for both shirt and pants, but it does not function
because all entered commands are forced to lower case. The two
individual commands <a href="#dyepants" class="wikilink"
title="dyepants">dyepants</a> and <a href="#dyeshirt" class="wikilink"
title="dyeshirt">dyeshirt</a> can be used instead.</p></td>
<td><p>|<a href="#dyeAll" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dyemenu</samp></p></td>
<td><p>| Brings up the same <a href="Dyeing#Dye_Pots" class="wikilink"
title="dyeing menu">dyeing menu</a> you get by interacting with the dye
pots in Emily's house. Filling all six pots with appropriate items will
bring up a character customization menu with HSV sliders for dyeing both
your currently-equipped shirt and pants.</p></td>
<td><p>|<a href="#dyemenu" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dyepants</samp></p></td>
<td><p>| Brings up a character customization menu with HSV sliders for
dyeing your currently-equipped pants.</p></td>
<td><p>|<a href="#dyepants" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dyeshirt</samp></p></td>
<td><p>| Brings up a character customization menu with HSV sliders for
dyeing your currently-equipped shirt.</p></td>
<td><p>|<a href="#dyeshirt" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>hat</samp></p></td>
<td><p>| <em>Syntax</em>: <code>hat</code> &lt;I:itemID&gt;</p>
<p>Gives and automatically equips the specified <a href="Hats"
class="wikilink" title="hat">hat</a> to your farmer; any currently
equipped hat will be destroyed. See <a href="Modding_Hats"
class="wikilink" title="hat data">hat data</a> for a list of base game
IDs.</p>
<p><em>Example:</em> <code>debug hat 3</code> would give you a <a
href="Sombrero" class="wikilink" title="Sombrero">Sombrero</a> and
automatically equip it.</p></td>
<td><p>|<a href="#hat" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>shirt</samp></p></td>
<td><p>| <em>Syntax</em>: <code>shirt</code> &lt;I:itemID&gt;</p>
<p>Gives and automatically equips the specified <a href="Shirts"
class="wikilink" title="shirt">shirt</a> to your farmer; any currently
equipped shirt will be destroyed.</p></td>
<td><p>|<a href="#shirt" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>tailor</samp></p></td>
<td><p>| Brings up the same <a href="Tailoring" class="wikilink"
title="tailoring menu">tailoring menu</a> you get by interacting with
the sewing machine in Emily's house.</p></td>
<td><p>|<a href="#tailor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>tailorrecipelisttool</samp><br />
<samp>trlt</samp></p></td>
<td><p>| Brings up a special menu listing most Objects, what color they
will dye an item, and what clothing item they can make when used in the
sewing machine. The menu can be scrolled with the mouse wheel, hovering
the mouse over the object will show the tooltip for the clothing it
makes, and clicking on the object will add the clothing it makes to your
inventory.</p></td>
<td><p>|<a href="#tailorrecipelisttool" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Tools and weapons

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
<td><p><samp>bobber</samp></p></td>
<td><p>| <em>Syntax</em>: <code>bobber</code> &lt;I:type&gt;</p>
<p>Changes the player's fishing rod <a href="Fish_Shop#Bobber_Machine"
class="wikilink" title="bobber style">bobber style</a>. Valid styles
begin at 0.</p></td>
<td><p>|<a href="#bobber" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fish</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fish</code> &lt;S:whichFish&gt;</p>
<p>Starts the fishing minigame with the specified fish. The player must
be holding a fishing rod. Can lead to the farmer getting stuck on
fishing animation frames.</p></td>
<td><p>|<a href="#fish" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>forge</samp></p></td>
<td><p>| Shows the <a href="Forge" class="wikilink"
title="Forge">Forge</a> menu.</p></td>
<td><p>|<a href="#forge" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pole</samp></p></td>
<td><p>| <em>Syntax</em>: <code>pole</code> [I:type]</p>
<p>Adds a <a href="Tools#Fishing_Poles" class="wikilink"
title="Fishing Pole">Fishing Pole</a> of the specified type to your
inventory. Valid types are 0 (Bamboo Pole; the default), 1 (Training
Rod), 2 (Fiberglass Rod), or 3 (Iridium Rod).</p></td>
<td><p>|<a href="#pole" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>trashcan</samp></p></td>
<td><p>| <em>Syntax</em>: <code>trashcan</code> &lt;I:level&gt;</p>
<p>Changes the upgrade level of your inventory <a href="Trash_Cans"
class="wikilink" title="Trash Can">Trash Can</a>. Upgrade levels are 0
(basic), 1 (copper), 2 (steel), 3 (gold), or 4 (iridium). The can sprite
may not fully update until the inventory is closed and
reopened.</p></td>
<td><p>|<a href="#trashcan" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Wallet items

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
<td><p><samp>clearspecials</samp></p></td>
<td><p>| Removes most special items from your <a href="Wallet"
class="wikilink" title="Wallet">Wallet</a>. The Rusty Key, Skull Key,
Special Charm, Dark Talisman, Magic Ink, Club Card, Dwarven Translation
Guide, and Magnifying Glass will all be removed, but Bear's Knowledge
and Spring Onion Mastery will remain.</p></td>
<td><p>|<a href="#clearspecials" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>darktalisman</samp></p></td>
<td><p>| Adds the <a href="Dark_Talisman" class="wikilink"
title="Dark Talisman">Dark Talisman</a> to (and removes the <a
href="Magic_Ink" class="wikilink" title="Magic Ink">Magic Ink</a> from)
your wallet; also removes the magic artifact blocking access to the <a
href="Witch&#39;s_Swamp" class="wikilink"
title="Witch&#39;s Swamp">Witch's Swamp</a>.<br />
<strong>Warning: This command will also clear all received mail and
hidden mail flags.</strong></p></td>
<td><p>|<a href="#darktalisman" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skullkey</samp></p></td>
<td><p>| Adds the <a href="Skull_Key" class="wikilink"
title="Skull Key">Skull Key</a> to your wallet.</p></td>
<td><p>|<a href="#skullkey" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>specialitem</samp></p></td>
<td><p>| <em>Syntax</em>: <code>specialitem</code> &lt;I:itemID&gt;</p>
<p>Adds the specified special item to your wallet. Which ID values are
useful is currently unknown.</p></td>
<td><p>|<a href="#specialitem" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>specials</samp></p></td>
<td><p>| Adds all special items to your wallet, including Bear's
Knowledge and Spring Onion Mastery. The associated events for these two
are also marked as seen.</p></td>
<td><p>|<a href="#specials" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>townkey</samp></p></td>
<td><p>| Adds the <a href="Key_To_The_Town" class="wikilink"
title="Key To The Town">Key To The Town</a> to your wallet.</p></td>
<td><p>|<a href="#townkey" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Miscellaneous items

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
<td><p><samp>fillbin</samp><br />
<samp>fb</samp></p></td>
<td><p>| Adds a Parsnip, Fire Quartz, LargeMouth Bass, Wild Horseradish,
and Wood to the shipping bin.</p></td>
<td><p>|<a href="#fillbin" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>listtags</samp></p></td>
<td><p>| Outputs all object context tags associated with the
currently-held item to the console.</p>
<p><em>Example:</em> <code>debug listtags</code> while holding an <a
href="Acorn" class="wikilink" title="Acorn">Acorn</a> would output
<em>Tags on Acorn: id_o_309 color_brown tree_seed_item item_acorn
category_seeds</em>.</p></td>
<td><p>|<a href="#listtags" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>makeinedible</samp></p></td>
<td><p>| Makes the currently-held item inedible by setting its edibility
value to -300; does not affect other instances of the same
item.</p></td>
<td><p>|<a href="#makeinedible" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skullgear</samp></p></td>
<td><p>| Sets your current backpack size to 36 slots, equips a Savage
Ring and Iridium Band, equips Space Boots, and clears inventory except
for an Iridium Pickaxe, a Galaxy Sword, a stack of 20 Spicy Eels, and a
stack of 20 Mega Bombs. Also sets your maximum health to 75 and gives
you the Fighter profession. Any previously equipped boots and rings and
all previous inventory items are lost.</p></td>
<td><p>|<a href="#skullgear" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Player

#### Appearance

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
<td><p><samp>copyoutfit</samp></p></td>
<td><p>| Copies all elements of the player's outfit in XML format to the
desktop clipboard and prints the same XML to the console.</p></td>
<td><p>|<a href="#copyoutfit" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>customizemenu</samp><br />
<samp>customize</samp><br />
<samp>cmenu</samp></p></td>
<td><p>| Opens the full character customization menu seen at the start
of a new game which includes gender options and player/farm names.
Changing the player name will cause the save file to change as
well.</p></td>
<td><p>|<a href="#customizemenu" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>haircolor</samp></p></td>
<td><p>| <em>Syntax</em>: <code>haircolor</code>
&lt;I:R&gt;,&lt;I:G&gt;,&lt;I:B&gt;</p>
<p>Sets the player's hair color to the specified RGB values. Each has a
range of 0-255.</p></td>
<td><p>|<a href="#haircolor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>hairstyle</samp></p></td>
<td><p>| <em>Syntax</em>: <code>hairstyle</code> &lt;I:ID&gt;</p>
<p>Sets the player's hair style to the specified ID. Note that these IDs
are one less than the values shown in the character customization menu
and have a range of 0-55 in the base game.</p></td>
<td><p>|<a href="#hairstyle" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pants</samp></p></td>
<td><p>| <em>Syntax</em>: <code>pants</code>
&lt;I:R&gt;,&lt;I:G&gt;,&lt;I:B&gt;</p>
<p>Sets the player's pants color to the specified RGB values. Each has a
range of 0-255. This no longer has a noticeable effect since pants are
now a clothing item; the <a href="#dyepants" class="wikilink"
title="dyepants">dyepants</a> command should be used instead.</p></td>
<td><p>|<a href="#pants" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>shirtcolor</samp></p></td>
<td><p>| <em>Syntax</em>: <code>shirtcolor</code> &lt;I:ID&gt;</p>
<p>Sets the player's shirt choice to the specified ID. This no longer
has a noticeable effect since shirts are now a clothing item; the <a
href="#clothes" class="wikilink" title="clothes">clothes</a> or <a
href="#dyeshirt" class="wikilink" title="dyeshirt">dyeshirt</a> commands
should be used instead.</p></td>
<td><p>|<a href="#shirtcolor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skincolor</samp></p></td>
<td><p>| <em>Syntax</em>: <code>skincolor</code> &lt;I:ID&gt;</p>
<p>Sets the player's skin color to the specified ID. Note that these IDs
are one less than the values shown in the character customization menu
and have a range of 0-23 in the base game.</p></td>
<td><p>|<a href="#skincolor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Health, stamina, buffs, and currency

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
<td><p><samp>buff</samp></p></td>
<td><p>| <em>Syntax</em>: <code>buff</code> &lt;I:buffID&gt;</p>
<p>Adds the specified buff to the player. Useful ID values are listed
below. Also see the <a href="#speed" class="wikilink"
title="speed">speed</a> command.</p></td>
<td><p>|<a href="#buff" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearbuffs</samp></p></td>
<td><p>| Removes all active buffs (both positive and negative.)</p></td>
<td><p>|<a href="#clearbuffs" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>die</samp></p></td>
<td><p>| Sets your <a href="health" class="wikilink"
title="health">health</a> to zero, resulting in passing out and
awakening in the <a href="Harvey&#39;s_Clinic" class="wikilink"
title="Clinic">Clinic</a>.</p></td>
<td><p>|<a href="#die" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>energize</samp></p></td>
<td><p>| <em>Syntax</em>: <code>energize</code> [I:amount]</p>
<p>Sets your <a href="energy" class="wikilink" title="energy">energy</a>
to the specified amount. If no amount is specified, it will be set to
maximum.</p></td>
<td><p>|<a href="#energize" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>exhaust</samp></p></td>
<td><p>| Sets your <a href="energy" class="wikilink"
title="energy">energy</a> to -15, resulting in passing out and ending
the day.</p></td>
<td><p>|<a href="#exhaust" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>gem</samp></p></td>
<td><p>| <em>Syntax</em>: <code>gem</code> &lt;I:amount&gt;</p>
<p>Gives you the specified number of <a href="Qi_Gem" class="wikilink"
title="Qi Gems">Qi Gems</a>.</p></td>
<td><p>|<a href="#gem" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>gold</samp></p></td>
<td><p>| Gives you one million (1,000,000) <a href="gold"
class="wikilink" title="gold">gold</a>.</p></td>
<td><p>|<a href="#gold" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>heal</samp></p></td>
<td><p>| Sets your <a href="health" class="wikilink"
title="health">health</a> to maximum.</p></td>
<td><p>|<a href="#heal" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>invincible</samp><br />
<samp>inv</samp><br />
<samp>gm</samp></p></td>
<td><p>| Toggles invincibility. When on, you will not take any
damage.</p></td>
<td><p>|<a href="#invincible" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>money</samp></p></td>
<td><p>| <em>Syntax</em>: <code>money</code> &lt;I:amount&gt;</p>
<p>Sets your money to the specified amount. To use in a <a
href="#Macros_for_multiple_commands" class="wikilink"
title="macro">macro</a>, make sure one or more of the letters in the
command is capitalized.</p></td>
<td><p>|<a href="#money" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>testnut</samp></p></td>
<td><p>| Spawns a <a href="Golden_Walnut" class="wikilink"
title="Golden Walnut">Golden Walnut</a> at the upper left corner of the
current map which will immediately start moving towards a player for
collection.</p></td>
<td><p>|<a href="#testnut" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>walnut</samp></p></td>
<td><p>| <em>Syntax</em>: <code>walnut</code> &lt;I:amount&gt;</p>
<p>Gives your team the specified number of Golden Walnuts.</p></td>
<td><p>|<a href="#walnut" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Movement and warping

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
<td><p><samp>canmove</samp><br />
<samp>cm</samp><br />
<samp>c</samp></p></td>
<td><p>| Attempts to force-enable player movement by resetting
animations and dismounting the horse. Sometimes useful when the player
becomes "stuck."</p></td>
<td><p>|<a href="#canmove" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>farmerdayupdate</samp></p></td>
<td><p>| <em>Syntax</em>: <code>farmerdayupdate</code> [I:timeOfDay]</p>
<p>Updates the farmer for a new day (<samp>Farmer::dayupdate</samp>) as
if they went to sleep at the current time of day. If
<samp>timeOfDay</samp> is specified, it then re-updates the farmer as if
they went to sleep at time <samp>0</samp> (inclusive) all the way up
through time <samp>timeOfDay - 1</samp> (exclusive).</p></td>
<td><p>|<a href="#farmerdayupdate" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>minelevel</samp></p></td>
<td><p>| <em>Syntax</em>: <code>minelevel</code> &lt;I:level&gt;
[I:layout]</p>
<p>Warps you to the specified level of the <a href="The_Mines"
class="wikilink" title="Mines">Mines</a> using the specified layout in
<samp>Content/Maps/Mines</samp>. Use level 77377 to warp to the <a
href="Quarry_Mine" class="wikilink" title="Quarry Mine">Quarry Mine</a>,
and to warp to a level in the <a href="Skull_Cavern" class="wikilink"
title="Skull Cavern">Skull Cavern</a>, add 120 to your target level.</p>
<p><em>Example:</em> <code>debug mineLevel 101 47</code> warps to mine
level 101 using layout 47.</p></td>
<td><p>|<a href="#minelevel" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>printplayerpos</samp><br />
<samp>ppp</samp></p></td>
<td><p>| Prints the player's current position in both tile and pixel
coordinates to the console.</p></td>
<td><p>|<a href="#printplayerpos" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>speed</samp></p></td>
<td><p>| <em>Syntax</em>: <code>speed</code>
&lt;I:value&gt;,[I:duration]</p>
<p>Gives the player a speed buff of the specified amount for the
specified duration. The duration is interpreted as in-game minutes and
defaults to 30; multiplying this value by 0.7 will convert to real-time
seconds. This buff has a unique source of "Debug Speed" and will stack
with both food and drink speed buffs.</p>
<p><em>Example:</em> <code>debug speed 5 600</code> will give you a +5
speed buff which lasts for 7 minutes (10 game hours).</p></td>
<td><p>|<a href="#speed" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>volcano</samp></p></td>
<td><p>| <em>Syntax</em>: <code>volcano</code> &lt;I:level&gt;</p>
<p>Warps you to the specified level of the <a href="Volcano_Dungeon"
class="wikilink" title="Volcano Dungeon">Volcano Dungeon</a>.</p></td>
<td><p>|<a href="#volcano" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warp</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warp</code>
&lt;S:locationName&gt;,[I:X],[I:Y]</p>
<p>Warps you to the <a href="Modding_Location_data#Location_names"
class="wikilink" title="specified location">specified location</a> at
the given coordinates. The location name is a fuzzy match, and if the
coordinates are not supplied the game has a list of hardcoded defaults
it will use for many locations (see
<samp>Utility.getDefaultWarpLocation()</samp> for details.)</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug warp forest 33 99</code> will warp you near Hat Mouse's
shop in the forest.</li>
</ul>
<ul>
<li><code>debug warp sci</code> will warp you to Robin's House
(internally <samp>ScienceHouse</samp>) just in front of where Robin
tends the shop.</li>
</ul></td>
<td><p>|<a href="#warp" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warphome</samp><br />
<samp>wh</samp></p></td>
<td><p>| Warps you directly to your bed in your
farmhouse/cabin.</p></td>
<td><p>|<a href="#warphome" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpshop</samp><br />
<samp>ws</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpshop</code> &lt;S:npcName&gt;</p>
<p>Warps you to the shop run by the specified NPC; if necessary will
also warp the NPC to the shop location. NPC names are case-insensitive
and can be one of the following: <samp>pierre</samp>,
<samp>robin</samp>, <samp>krobus</samp>, <samp>sandy</samp>,
<samp>marnie</samp>, <samp>clint</samp>, <samp>gus</samp>,
<samp>willy</samp>, <samp>pam</samp>, <samp>dwarf</samp>, and
<samp>wizard</samp>. The <samp>wizard</samp> option will also add Magic
Ink to your wallet and mark the event where the ink is returned as
already seen.</p>
<p><em>Example:</em> <code>debug warpshop marnie</code> will warp both
you and Marnie to her animal shop.</p></td>
<td><p>|<a href="#warpshop" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warptocharacter</samp><br />
<samp>wtc</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warptocharacter</code>
&lt;S:npcName&gt;</p>
<p>Warps you to the specified character, wherever they are. This is a
fuzzy match.</p></td>
<td><p>|<a href="#warptocharacter" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warptoplayer</samp><br />
<samp>wtp</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warptoplayer</code>
&lt;S:playerName&gt;</p>
<p>Warps you to the specified player, wherever they are. The match is
case-insensitive and names with spaces should be surrounded by double
quotes.</p></td>
<td><p>|<a href="#warptoplayer" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Skills and XP

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
<td><p><samp>experience</samp></p></td>
<td><p>| <em>Syntax</em>: <code>experience</code>
&lt;I:skillID&gt;,&lt;I:xpAmount&gt;</p>
<p>Adds the specified amount of experience to the specified skill. Valid
skill IDs are 0 (Farming), 1 (Fishing), 2 (Foraging), 3 (Mining), 4
(Combat), and 5 (Luck).</p></td>
<td><p>|<a href="#experience" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fishing</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fishing</code> &lt;I:level&gt;</p>
<p>Sets your fishing skill to the specified level. This does not unlock
crafting recipes or allow profession choice, nor does it change the
underlying experience amount. However it does count in terms of
unlocking what Willy sells and enabling legendary fish to be
hooked.</p></td>
<td><p>|<a href="#fishing" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>levelup</samp></p></td>
<td><p>| <em>Syntax</em>: <code>levelup</code>
&lt;I:skillID&gt;,&lt;I:level&gt;</p>
<p>Shows the appropriate levelup window for the specified skill and
level. This unlocks any associated crafting recipes and (if applicable)
lets you choose a profession, but does not actually change the skill
level or underlying experience amount. Valid skill IDs are 0 (Farming),
1 (Fishing), 2 (Foraging), 3 (Mining), 4 (Combat), and 5
(Luck).</p></td>
<td><p>|<a href="#levelup" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>profession</samp></p></td>
<td><p>| <em>Syntax</em>: <code>profession</code> &lt;I:ID&gt;</p>
<p>Gives you the specified profession. Note that this just hard adds the
profession, it's not a way to switch skill trees. Valid profession IDs
from the base game are shown below.</p></td>
<td><p>|<a href="#profession" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>showexperience</samp></p></td>
<td><p>| <em>Syntax</em>: <code>showexperience</code>
&lt;I:skillID&gt;</p>
<p>Outputs your total experience amount for the specified skill in the
SMAPI console. Valid skill IDs are 0 (Farming), 1 (Fishing), 2
(Foraging), 3 (Mining), 4 (Combat), and 5 (Luck).</p></td>
<td><p>|<a href="#showexperience" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Statistics and achievements

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
<td><p><samp>achieve</samp></p></td>
<td><p>| <em>Syntax</em>: <code>achieve</code>
&lt;S:steamAchieveID&gt;</p>
<p>Awards the specified Steam achievement. Steam achievements which
correspond to in-game achievements use the same numeric ID as listed in
<a href="Modding_Achievement_data" class="wikilink"
title="Achievement data">Achievement data</a> with one exception: the ID
for <em>Greenhorn</em> is <samp>a0</samp> instead of just
<samp>0</samp>. Steam-only achievements have a much longer string ID;
these are listed below.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug achieve 17</code> will award the Steam achievement for
<em>Gourmet Chef</em>.</li>
</ul>
<ul>
<li><code>debug achieve Achievement_Stardrop</code> will award the Steam
achievement for <em>Mystery of the Stardrops</em>.</li>
</ul></td>
<td><p>|<a href="#achieve" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>achievement</samp></p></td>
<td><p>| <em>Syntax</em>: <code>achievement</code>
&lt;I:achieveID&gt;</p>
<p>Awards the specified in-game achievement. See <a
href="Modding_Achievement_data" class="wikilink"
title="Achievement data">Achievement data</a> for a list of IDs. This
will also award the associated Steam achievement if you don't have
it.</p></td>
<td><p>|<a href="#achievement" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>catchallfish</samp></p></td>
<td><p>| Marks every fish in the game as having been caught by the
player. All fish will be marked as having size 9.</p></td>
<td><p>|<a href="#catchallfish" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>caughtfish</samp><br />
<samp>fishcaught</samp></p></td>
<td><p>| <em>Syntax</em>: <code>caughtfish</code> &lt;I:value&gt;</p>
<p>Sets the <samp>FishCaught</samp> stat to the specified
amount.</p></td>
<td><p>|<a href="#caughtfish" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>daysplayed</samp><br />
<samp>dap</samp></p></td>
<td><p>| Shows a global message with the current value of the
<samp>daysPlayed</samp> stat.</p></td>
<td><p>|<a href="#daysplayed" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dp</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dp</code> &lt;I:value&gt;</p>
<p>Sets the <samp>daysPlayed</samp> stat to the specified
amount.</p></td>
<td><p>|<a href="#dp" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>getStat</samp></p></td>
<td><p>| <em>Syntax</em>: <code>getStat</code> &lt;S:stat key&gt;</p>
<p>Shows a <a href="Modding_Stats" class="wikilink"
title="stat&#39;s value">stat's value</a> in the console.</p></td>
<td><p>|<a href="#getStat" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>killmonsterstat</samp><br />
<samp>kms</samp></p></td>
<td><p>| <em>Syntax</em>: <code>killmonsterstat</code>
&lt;S:monsterName&gt;,&lt;I:value&gt;</p>
<p>Sets the kill stats for the specified monster to the specified value.
The monster name should be the same as the keys in
<samp>Data/Monsters</samp> and names with spaces should be in double
quotes; it is case-sensitive. The command will output a buggy response
to the console due to referencing the wrong string key, but the stats
are correctly set.</p>
<p><em>Example:</em> <code>debug kms "Dust Spirit" 499</code> will set
the monster kill stats for <a href="Dust_Sprite" class="wikilink"
title="Dust Sprites">Dust Sprites</a> to 499 and output <em>Drink Dust
Spirit?</em></p></td>
<td><p>|<a href="#killmonsterstat" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>mineinfo</samp></p></td>
<td><p>| Outputs two mine-related stats to the SMAPI Console:
<samp>MineShaft.lowestLevelReached</samp> and
<samp>player.deepestMineLevel</samp></p></td>
<td><p>|<a href="#mineinfo" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>perfection</samp></p></td>
<td><p>| <strong>May be broken.</strong> Makes a variety of changes to
qualify for <a href="Perfection" class="wikilink"
title="Perfection">Perfection</a>. These include maxing all friendships,
marking all fish as caught, awarding and marking complete all cooking
and crafting recipes, marking all items as shipped, setting the flags
for all stardrops, setting all skill levels to 10, awarding 500 kills
for all monsters, forcibly placing all 4 obelisks and the gold clock in
the upper left corner of the farm, and giving 130 walnuts.</p></td>
<td><p>|<a href="#perfection" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>resetachievements</samp></p></td>
<td><p>| Resets the Steam achievements.</p></td>
<td><p>|<a href="#resetachievements" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setStat</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setStat</code> &lt;S:stat
key&gt;,&lt;I:value&gt;</p>
<p>Sets a <a href="Modding_Stats" class="wikilink"
title="stat&#39;s value">stat's value</a> to the given positive
integer.</p>
<p><em>Example:</em> <code>debug setstat StepsTaken 99999</code> would
set the <em>Number of Steps Taken</em> stat to 99999.</p></td>
<td><p>|<a href="#setStat" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
