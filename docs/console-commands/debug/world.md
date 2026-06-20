---
title: "World"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, world, other, advanced, debug-commands, how-to-enter-debug-commands, macros, actions-and-queries]
---
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

### Collections and quests

#### Cooking and crafting

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
<td><p><samp>addallcrafting</samp></p></td>
<td><p>| Teaches you all crafting recipes. Basically the same as <a
href="#crafting" class="wikilink" title="crafting">crafting</a>, but
this one does not check if you already know the recipe before adding so
it may output some error messages to the console about duplicate
keys.</p></td>
<td><p>|<a href="#addallcrafting" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>cooking</samp></p></td>
<td><p>| Teaches you all cooking recipes.</p></td>
<td><p>|<a href="#cooking" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>cookingrecipe</samp></p></td>
<td><p>| <em>Syntax</em>: <code>cookingrecipe</code>
&lt;S:recipeName&gt;</p>
<p>Teaches you the specified cooking recipe. Names are case-sensitive
and may contain spaces.</p>
<p><em>Example:</em> <code>debug cookingrecipe Seafoam Pudding</code>
will give you the recipe to cook <a href="Seafoam_Pudding"
class="wikilink" title="Seafoam Pudding">Seafoam Pudding</a>.</p></td>
<td><p>|<a href="#cookingrecipe" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>crafting</samp></p></td>
<td><p>| Teaches you all crafting recipes.</p></td>
<td><p>|<a href="#crafting" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>craftingrecipe</samp><br />
<samp>addCraftingRecipe</samp></p></td>
<td><p>| <em>Syntax</em>: <code>craftingrecipe</code>
&lt;S:recipeName&gt;</p>
<p>Teaches you the specified crafting recipe. Names are case-sensitive
and may contain spaces.</p>
<p><em>Example:</em> <code>debug craftingrecipe Ancient Seeds</code>
will give you the recipe to craft plantable ancient seeds from the
artifact.</p></td>
<td><p>|<a href="#craftingrecipe" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>slimecraft</samp></p></td>
<td><p>| Teaches you the crafting recipes for <a href="Slime_Incubator"
class="wikilink" title="Slime Incubator">Slime Incubator</a> and <a
href="Slime_Egg-Press" class="wikilink" title="Slime Egg-Press">Slime
Egg-Press</a>.</p></td>
<td><p>|<a href="#slimecraft" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Fishing, museum, and secret notes

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
<td><p><samp>clearfishcaught</samp></p></td>
<td><p>| Clears all records of which fish you have caught, resetting the
collection. To also change the stat which tracks how many total fish
have been caught, see <a href="#caughtfish" class="wikilink"
title="caughtfish">caughtfish</a>.</p></td>
<td><p>|<a href="#clearfishcaught" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearmuseum</samp></p></td>
<td><p>| Removes all donated items from the museum, emptying the museum
displays and causing all artifacts and minerals to have the <em>Gunther
can tell you more about this...</em> description. Does not affect the
records of which artifacts and minerals have been found (<em>i.e.,</em>
the collection pages).</p></td>
<td><p>|<a href="#clearmuseum" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>deletearch</samp></p></td>
<td><p>| Clears all records of which artifacts and minerals you have
found.<br />
<strong>Warning: Also clears all record of which fish you have caught
and clears all received mail (including hidden progress
flags).</strong></p></td>
<td><p>|<a href="#deletearch" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>museumloot</samp></p></td>
<td><p>| Adds unfound artifacts and minerals to your inventory until it
is full. Items added by this command will now be marked "found" on the
collection pages.</p></td>
<td><p>|<a href="#museumloot" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>newmuseumloot</samp></p></td>
<td><p>| Adds undonated artifacts and minerals to your inventory until
it is full. Items added by this command increment the "Total found"
count on the collection pages.</p></td>
<td><p>|<a href="#newmuseumloot" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>note</samp></p></td>
<td><p>| <em>Syntax</em>: <code>note</code> &lt;I:bookID&gt;</p>
<p>Sets the count of <a href="Lost_Books" class="wikilink"
title="Lost Books">Lost Books</a> recovered to 18, even if you
previously had found more, and brings up a window with the contents of
the specified book. Book IDs above 18 will show the message <em>There's
a book missing here.</em></p></td>
<td><p>|<a href="#note" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>sn</samp><br />
<samp>secretNote</samp></p></td>
<td><p>| <em>Syntax</em>: <code>sn</code> [I:noteID]</p>
<p>Adds specified secret note to your inventory. If no ID is specified,
a random unseen note will be added. See <samp>Data/SecretNotes</samp>
for a list of IDs.</p></td>
<td><p>|<a href="#sn" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Mail

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
<td><p><samp>allmail</samp></p></td>
<td><p>| Queues every letter defined in <samp>Data/mail</samp> for
delivery tomorrow.</p></td>
<td><p>|<a href="#allmail" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>allmailread</samp></p></td>
<td><p>| Marks every letter defined in <samp>Data/mail</samp> as already
read. They will all be accessible in the letters tab of the collections
menu.</p></td>
<td><p>|<a href="#allmailread" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>broadcastmail</samp></p></td>
<td><p>| <em>Syntax</em>: <code>broadcastmail</code>
&lt;S:mailID&gt;</p>
<p>Queues specified mail for delivery tomorrow for all players. The ID
is case-sensitive; see <samp>Data/mail</samp> for valid IDs in the base
game.</p></td>
<td><p>|<a href="#broadcastmail" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>broadcastmailbox</samp></p></td>
<td><p>| <em>Syntax</em>: <code>broadcastmailbox</code>
&lt;S:mailID&gt;</p>
<p>Immediately adds specified mail to all players' mailboxes. The ID is
case-sensitive; see <samp>Data/mail</samp> for valid IDs in the base
game.</p></td>
<td><p>|<a href="#broadcastmailbox" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearmail</samp></p></td>
<td><p>| Clears records of all received mail <strong>(including hidden
progress flags)</strong>. This also clears the letters tab in the
collections menu.</p></td>
<td><p>|<a href="#clearmail" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>mailfortomorrow</samp><br />
<samp>mft</samp></p></td>
<td><p>| <em>Syntax</em>: <code>mailfortomorrow</code>
&lt;S:mailID&gt;,[noletter]</p>
<p>Queues specified mail for delivery tomorrow. The ID is
case-sensitive, and any zeros in the given ID will be replaced with
underscores. See <samp>Data/mail</samp> for valid IDs (after
replacement) in the base game. Because of the zero replacement, some
letters (<em>e.g.,</em> <samp>quest10</samp>) are inaccessible with this
command; <a href="#broadcastmail" class="wikilink"
title="broadcastmail">broadcastmail</a> may be a useful alternative in
those cases. If the second parameter is present (with any value), the
"noletter" flag is set, which will add the mail to your mail received
list without showing a "new mail" indicator.</p></td>
<td><p>|<a href="#mailfortomorrow" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>seenmail</samp></p></td>
<td><p>| <em>Syntax</em>: <code>seenmail</code>
&lt;S:mailID&gt;,[B:addOrRemove]</p>
<p>Marks specified mail as already received. The ID is case-sensitive;
see <samp>Data/mail</samp> for valid IDs in the base game. You can
remove a mail received (instead of adding it) by setting the second
argument to false, like <samp>seenMail
&lt;code&gt;&lt;id&gt;&lt;/code&gt; false</samp>.</p></td>
<td><p>|<a href="#seenmail" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>showmail</samp></p></td>
<td><p>| <em>Syntax</em>: <code>showmail</code> &lt;S:mailID&gt;</p>
<p>Brings up the letter-reading window with the specified mail. The ID
is case-sensitive; see <samp>Data/mail</samp> for valid IDs in the base
game. If a match cannot be found, a blank window will briefly display
and an ArgumentOutOfRange error will be triggered. Does not set the
letter as received or cause it to show in the letter tab of the
collections menu.</p>
<p><em>Example:</em> <code>debug showmail SeaAmulet</code> will show the
letter Lewis sends about Mermaid's Pendants.</p></td>
<td><p>|<a href="#showmail" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Quests and Special Orders

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
<td><p><samp>clearquests</samp></p></td>
<td><p>| Removes all quests from your journal/quest log.</p></td>
<td><p>|<a href="#clearquests" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>collectquest</samp></p></td>
<td><p>| Starts a new random resource Gathering quest. If used multiple
times on the same game day, the quest will always be the same.</p></td>
<td><p>|<a href="#collectquest" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>completespecialorders</samp><br />
<samp>cso</samp></p></td>
<td><p>| Completes all objectives for all currently active Special
Orders and Qi Challenges. Note that this command does not remove the
associated journal entries.</p></td>
<td><p>|<a href="#completespecialorders" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>completequest</samp></p></td>
<td><p>| <em>Syntax</em>: <code>completequest</code>
&lt;I:questID&gt;</p>
<p>Completes specified quest and removes it from your journal. See
<samp>Data/Quests</samp> for a list of IDs.</p></td>
<td><p>|<a href="#completequest" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>deliveryquest</samp></p></td>
<td><p>| Starts a new random item Delivery quest. If used multiple times
on the same game day, the quest will always be the same.</p></td>
<td><p>|<a href="#deliveryquest" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>getallquests</samp></p></td>
<td><p>| Starts every quest from <samp>Data/Quests</samp> that you don't
already have.</p></td>
<td><p>|<a href="#getallquests" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>ordersboard</samp></p></td>
<td><p>| Shows the <a href="Quests#List_of_Special_Orders"
class="wikilink" title="Special Orders">Special Orders</a> quest
board.</p></td>
<td><p>|<a href="#ordersboard" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>qiboard</samp></p></td>
<td><p>| Shows the <a href="Qi&#39;s_Walnut_Room#Special_Orders_Board"
class="wikilink" title="Qi Challenges">Qi Challenges</a> quest
board.</p></td>
<td><p>|<a href="#qiboard" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>quest</samp></p></td>
<td><p>| <em>Syntax</em>: <code>quest</code> &lt;I:questID&gt;</p>
<p>Starts the specified quest. See <samp>Data/Quests</samp> for a list
of IDs.</p></td>
<td><p>|<a href="#quest" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>quests</samp></p></td>
<td><p>| Starts every quest from <samp>Data/Quests</samp> that you don't
already have as well as a random item Delivery quest and a random Slay
Monster quest.</p></td>
<td><p>|<a href="#quests" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removequest</samp></p></td>
<td><p>| <em>Syntax</em>: <code>removequest</code> &lt;I:questID&gt;</p>
<p>Silently removes specified quest from your journal. See
<samp>Data/Quests</samp> for a list of IDs.</p></td>
<td><p>|<a href="#removequest" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>slayquest</samp></p></td>
<td><p>| Starts a new random Slay Monster quest. If used multiple times
on the same game day, the quest will always be the same.</p></td>
<td><p>|<a href="#slayquest" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>specialorder</samp></p></td>
<td><p>| <em>Syntax</em>: <code>specialorder</code>
&lt;S:questID&gt;</p>
<p>Starts the Special Order (either town or Qi Challenge) with the
specified ID. See <samp>Data/SpecialOrders</samp> for a list of
IDs.</p></td>
<td><p>|<a href="#specialorder" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### NPCs

#### Children

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
<td><p><samp>child</samp><br />
<samp>kid</samp></p></td>
<td><p>| If you have children, advances the age of the first child to
the next stage. Otherwise, spawns a new child named "Baby" with gender
and skin tone randomly chosen; the child will start at stage 3
(crawling) and may initially spawn out of bounds. You do not need to be
married or have an upgraded house to use this command.</p></td>
<td><p>|<a href="#child" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>child2</samp></p></td>
<td><p>| If you have multiple children, advances the age of the second
child to the next stage. Otherwise, spawns a new child named "Baby2"
with gender and skin tone randomly chosen; the child will start at stage
3 (crawling) and may initially spawn out of bounds. You do not need to
be married or have an upgraded house to use this command.</p></td>
<td><p>|<a href="#child2" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearchildren</samp></p></td>
<td><p>| Removes all your children.</p></td>
<td><p>|<a href="#clearchildren" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pregnant</samp></p></td>
<td><p>| Sets a new baby to be born/adopted the next day. You may need
to be already married (and have a house with a nursery) for this to
work.</p></td>
<td><p>|<a href="#pregnant" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Spawning and removal

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
<td><p><samp>addkent</samp></p></td>
<td><p>| Spawns <a href="Kent" class="wikilink" title="Kent">Kent</a> if
after year 1.</p></td>
<td><p>|<a href="#addkent" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>characterinfo</samp></p></td>
<td><p>| Displays a global message listing how many NPCs are in the
current location.</p></td>
<td><p>|<a href="#characterinfo" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearcharacters</samp></p></td>
<td><p>| Removes all NPCs who are in the current location.</p></td>
<td><p>|<a href="#clearcharacters" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clone</samp></p></td>
<td><p>| <em>Syntax</em>: <code>clone</code> &lt;S:npcName&gt;</p>
<p>Clones specified NPC and places the copy in the current location.
Name is a fuzzy match.<br />
<strong>Warning: cloning <samp>farmer</samp> will crash the
game.</strong></p></td>
<td><p>|<a href="#clone" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>killall</samp></p></td>
<td><p>| <em>Syntax</em>: <code>killall</code> &lt;S:npcName&gt;</p>
<p>Removes all NPCs except for the specified character. Name is an exact
match, and they are only spared from removal if they are in the current
location. Will also remove NPCs inside constructed buildings.</p></td>
<td><p>|<a href="#killall" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>killnpc</samp><br />
<samp>removenpc</samp></p></td>
<td><p>| <em>Syntax</em>: <code>killnpc</code> &lt;S:npcName&gt;</p>
<p>Removes specified NPC from the game, checking all game locations and
buildings. Name is an exact match. Command will output a message to the
console stating whether or not the NPC was found and removed.</p></td>
<td><p>|<a href="#killnpc" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Relationships

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
<td><p><samp>dating</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dating</code> &lt;S:npcName&gt;</p>
<p>Sets your relationship status with specified NPC to
<samp>Dating</samp>; <em>i.e.,</em> marks them as having been given a
bouquet. Name is an exact match.</p></td>
<td><p>|<a href="#dating" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>divorce</samp></p></td>
<td><p>| Queues your farmer to divorce their spouse overnight. The
spouse room may not be fully removed until you have slept and/or
returned to title.</p></td>
<td><p>|<a href="#divorce" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>engaged</samp></p></td>
<td><p>| <em>Syntax</em>: <code>engaged</code> &lt;S:npcName&gt;</p>
<p>Increases your friendship with specified NPC by 2500 points (10
hearts) and sets relationship status to <samp>Engaged</samp> with a
wedding for the next day. Name is an exact match.</p></td>
<td><p>|<a href="#engaged" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>friendall</samp></p></td>
<td><p>| <em>Syntax</em>: <code>friendall</code> [I:value]</p>
<p>Increases <a href="friendship" class="wikilink"
title="friendship">friendship</a> with all socializable NPCs by the
specified amount. If no amount is given, the increase will be 2500
points (10 hearts). All normal point caps are in place, so a bachelor
you aren't dating will not increase past 8 hearts. Previously unmet NPCs
will also be marked as met and have friendship increased with the
following exceptions:</p></td>
<td><p>|<a href="#friendall" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>friendship</samp><br />
<samp>friend</samp></p></td>
<td><p>| <em>Syntax</em>: <code>friendship</code>
&lt;S:npcName&gt;,&lt;I:value&gt;</p>
<p>Sets friendship with specified NPC to specified value. This is a
fuzzy match, and they will be marked as met if previously
unmet.</p></td>
<td><p>|<a href="#friendship" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>invitemovie</samp></p></td>
<td><p>| <em>Syntax</em>: <code>invitemovie</code> &lt;S:npcName&gt;</p>
<p>Invites specified NPC to see a movie today. This is a fuzzy match and
you will still need your own ticket to enter the theatre.</p></td>
<td><p>|<a href="#invitemovie" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>makeex</samp></p></td>
<td><p>| <em>Syntax</em>: <code>makeex</code> &lt;S:npcName&gt;</p>
<p>Sets your relationship status with specified NPC to
<samp>Divorced</samp>, removing any marriage or bouquet flag and listing
them as <em>ex-husband</em> or <em>ex-wife.</em> Name is an exact
match.</p></td>
<td><p>|<a href="#makeex" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>marry</samp></p></td>
<td><p>| <em>Syntax</em>: <code>marry</code> &lt;S:npcName&gt;</p>
<p>Increases your friendship with the specified NPC by 2500 points (10
hearts), and sets your relationship status to <samp>Married</samp> with
an anniversary of today. Name is a fuzzy match.</p></td>
<td><p>|<a href="#marry" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>wedding</samp></p></td>
<td><p>| <em>Syntax</em>: <code>wedding</code> &lt;S:npcName&gt;</p>
<p>Sets the specified NPC as your spouse and queues a wedding for today.
Name is an exact match. If the specified NPC is not normally
marriageable, the wedding will still occur but they will be invisible on
the wedding day.</p></td>
<td><p>|<a href="#wedding" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Dialogue

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
<td><p><samp>clearactivedialogueevents</samp></p></td>
<td><p>| Clears all active <a
href="Modding_Dialogue#Conversation_topics" class="wikilink"
title="conversation topics">conversation topics</a>.</p></td>
<td><p>|<a href="#clearactivedialogueevents" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>db</samp><br />
<samp>speakto</samp></p></td>
<td><p>| <em>Syntax</em>: <code>db</code> &lt;S:npcName&gt;</p>
<p>Shows a dialogue box with the current dialogue for the specified NPC.
Name is a fuzzy match and will default to Pierre if not supplied. This
does count as having spoken to that NPC today, and if they don't have
any more dialogue right now, the message <em>Stack empty</em> will be
output to the console.</p></td>
<td><p>|<a href="#db" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dialogue</samp><br />
<samp>adddialogue</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dialogue</code>
&lt;S:npcName&gt;,&lt;S:dialogueString&gt;</p>
<p>Sets the dialogue for the specified character to the specified
string. Name is a fuzzy match, and NPC names containing spaces should be
quoted (e.g.
<code>debug dialogue "Some NPC" Some dialogue text$h</code>. The
dialogue string should start with a zero and everything after will be
parsed. It can include tokens such as <samp>@</samp> for the farmer name
and portrait commands; see <a href="Modding_Dialogue#Format"
class="wikilink" title="Dialogue">Dialogue</a> for format specifics.</p>
<p><em>Example:</em>
<code>debug dialogue Abi 0Hi @! Modding is fun!$h</code> would set <a
href="Abigail" class="wikilink" title="Abigail&#39;s">Abigail's</a> next
dialogue to be <em>Hi (FarmerName)! Modding is fun!</em> with her happy
portrait.</p></td>
<td><p>|<a href="#dialogue" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>loaddialogue</samp></p></td>
<td><p>| <em>Syntax</em>: <code>loaddialogue</code>
&lt;S:npcName&gt;,&lt;S:dialogueKey&gt;</p>
<p>Sets the dialogue for the specified character using the specified
asset key. Name is a fuzzy match. Key format appears to be
<samp>file:key</samp> but exact specifics are unknown. Curly braces in
the key (<samp>{</samp>, <samp>}</samp>) will be converted to angle
brackets (<samp>&lt;</samp>, <samp>&gt;</samp>).</p></td>
<td><p>|<a href="#loaddialogue" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>phone</samp></p></td>
<td><p>| Brings up the <a href="Telephone" class="wikilink"
title="Telephone">Telephone</a> menu.</p></td>
<td><p>|<a href="#phone" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>question</samp></p></td>
<td><p>| <em>Syntax</em>: <code>question</code>
&lt;I:questionID&gt;,[B:answerOrForget]</p>
<p>Marks the specified dialogue question as answered. You can forget a
selected answer (instead of adding it) by setting the second argument to
false, like <samp>question &lt;code&gt;&lt;id&gt;&lt;/code&gt;
false</samp>.</p></td>
<td><p>|<a href="#question" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>showtextabovehead</samp><br />
<samp>sb</samp></p></td>
<td><p>| <em>Syntax</em>: <code>showtextabovehead</code>
&lt;S:npcName&gt;</p>
<p>Shows a speech bubble saying <em>"Hello! This is a test"</em> above
the specified NPC's head. Name is a fuzzy match.</p></td>
<td><p>|<a href="#showtextabovehead" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>speech</samp></p></td>
<td><p>| <em>Syntax</em>: <code>speech</code>
&lt;S:npcName&gt;,&lt;S:text&gt;</p>
<p>Displays a dialogue box for the specified character saying the
specified string. Name is a fuzzy match and names with spaces should be
in double quotes. All text after the NPC name is part of the text to
display. The text can include tokens such as <samp>@</samp> for the
farmer name and portrait commands; see <a href="Modding_Dialogue#Format"
class="wikilink" title="Dialogue">Dialogue</a> for format specifics.
Useful for testing dialogue changes.</p>
<p><em>Example:</em>
<code>debug speech Abi 0Hi @! Modding is fun!$h</code> would open a
dialogue box of <a href="Abigail" class="wikilink"
title="Abigail">Abigail</a> saying <em>Hi (FarmerName)! Modding is
fun!</em> with her happy portrait.</p></td>
<td><p>|<a href="#speech" class="wikilink" title="#">#</a></p></td>
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
<td><p><samp>facedirection</samp><br />
<samp>face</samp><br />
<samp>fd</samp></p></td>
<td><p>| <em>Syntax</em>: <code>facedirection</code>
&lt;S:npcName&gt;,&lt;I:direction&gt;</p>
<p>Sets specified character to face the specified direction. Name is a
fuzzy match and also accepts <samp>farmer</samp>. See <a
href="Modding_Event_data#Directions" class="wikilink"
title="Event data">Event data</a> for the valid directions.</p></td>
<td><p>|<a href="#facedirection" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>faceplayer</samp></p></td>
<td><p>| <em>Syntax</em>: <code>faceplayer</code> &lt;S:npcName&gt;</p>
<p>Sets specified character to face towards the player. Name is a fuzzy
match.</p></td>
<td><p>|<a href="#faceplayer" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>hurry</samp></p></td>
<td><p>| <em>Syntax</em>: <code>hurry</code> &lt;S:npcName&gt;</p>
<p>Warps specified character to the endpoint of their current schedule
entry. Name is a fuzzy match.</p>
<p><em>Example:</em> <code>debug hurry pam</code> would cause <a
href="Pam" class="wikilink" title="Pam">Pam</a> to immediately warp to
the bus if entered during her morning walk after the bus has been
repaired.</p></td>
<td><p>|<a href="#hurry" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>jump</samp></p></td>
<td><p>| <em>Syntax</em>: <code>jump</code>
&lt;S:npcName&gt;,[F:velocity]</p>
<p>Makes specified character jump with the specified velocity. Name is a
fuzzy match and also accepts <samp>farmer</samp>. Velocity is a float
and defaults to 8.0 if not supplied, which results in a jump of about
half the height of the player character.</p></td>
<td><p>|<a href="#jump" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpcharacter</samp><br />
<samp>wc</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpcharacter</code>
&lt;S:npcName&gt;,&lt;I:X&gt;,&lt;I:Y&gt;,[I:facingDirection]</p>
<p>Warps specified character to the given coordinates on the current
map. Name is a fuzzy match. See <a href="Modding_Event_data#Directions"
class="wikilink" title="Event data">Event data</a> for the valid
directions; the default is <samp>2</samp>. Note: if you do not include
enough parameters, an error message will be printed to the console which
incorrectly states the default facing direction is
<samp>1</samp>.</p></td>
<td><p>|<a href="#warpcharacter" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpcharacterto</samp><br />
<samp>wct</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpcharacterto</code>
&lt;S:npcName&gt;,&lt;S:locationName&gt;,&lt;I:X&gt;,&lt;I:Y&gt;,[I:facingDirection]</p>
<p>Warps specified character to the given coordinates on the specified
map. Character name is a fuzzy match, but location is exact. See <a
href="Modding_Event_data#Directions" class="wikilink"
title="Event data">Event data</a> for the valid directions; the default
is <samp>2</samp>. Note: if you do not include enough parameters, an
error message will be printed to the console which incorrectly states
the default facing direction is <samp>1</samp>.</p>
<p><em>Example:</em> <code>debug wct robin Farm 69 16</code> would warp
<a href="Robin" class="wikilink" title="Robin">Robin</a> to just right
of the mailbox on the Farm map, facing downwards.</p></td>
<td><p>|<a href="#warpcharacterto" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpcharactertome</samp><br />
<samp>wctm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpcharactertome</code>
&lt;S:npcName&gt;</p>
<p>Warps the specified character directly to you; name is a fuzzy
match.</p></td>
<td><p>|<a href="#warpcharactertome" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>whereis</samp><br />
<samp>where</samp></p></td>
<td><p>| <em>Syntax</em>: <code>whereis</code> &lt;S:npcName&gt;</p>
<p>Outputs the location and coordinates of the specified character to
the SMAPI console. Name is a fuzzy match, so the command will return all
matching NPCs.</p></td>
<td><p>|<a href="#whereis" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Farm animals

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
<td><p><samp>animal</samp></p></td>
<td><p>| <em>Syntax</em>: <code>animal</code> &lt;S:type&gt;</p>
<p>Adds a new baby animal of the specified type to the Farm. The animal
will have a random name and be assigned to the correct type of building
(if there is room). Type is a case-sensitive match with spaces allowed.
Valid types for the base game are listed below.</p></td>
<td><p>|<a href="#animal" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>animalinfo</samp></p></td>
<td><p>| Displays a global message with the count of the total number of
farm animals.</p></td>
<td><p>|<a href="#animalinfo" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>befriendanimals</samp></p></td>
<td><p>| <em>Syntax</em>: <code>befriendanimals</code> [I:amount]</p>
<p>Sets friendship of all animals who live (and are currently present)
in the current location to the given amount. Default is 1000
(max).</p></td>
<td><p>|<a href="#befriendanimals" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>displaceanimals</samp></p></td>
<td><p>| Goes through all buildings that can contain animals. For each
animal in each building, tries to move the animal outside the building.
Finally, clears the building of all animals that live there.</p></td>
<td><p>|<a href="#displaceanimals" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fixanimals</samp></p></td>
<td><p>| Goes through all buildings that can contain animals and removes
entries for animals which no longer live in that building.</p></td>
<td><p>|<a href="#fixanimals" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>growanimals</samp></p></td>
<td><p>| Sets all animals who live in the current location to day 1 of
adulthood, unless they are already adults. May cause each of them to eat
hay.</p></td>
<td><p>|<a href="#growanimals" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pauseanimals</samp></p></td>
<td><p>| Pauses all farm animals in the current location indefinitely.
Exiting and re-entering may cause them to be randomly moved to a new
spot, but they will remain paused.</p></td>
<td><p>|<a href="#pauseanimals" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>unpauseanimals</samp></p></td>
<td><p>| Unpauses all farm animals in the current location.</p></td>
<td><p>|<a href="#unpauseanimals" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpanimaltome</samp><br />
<samp>watm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpanimaltome</code>
&lt;S:animalName&gt;</p>
<p>Warps the specified farm animal to you; name is a case-insensitive
fuzzy search but will only work in a location that allows
animals.</p></td>
<td><p>|<a href="#warpanimaltome" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Pets, horses, and monsters

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
<td><p><samp>befriendpets</samp></p></td>
<td><p>| Gives the player 1000 friendship points with all pets.</p></td>
<td><p>|<a href="#befriendpets" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>cat</samp></p></td>
<td><p>| <em>Syntax</em>: <code>cat</code>
&lt;I:X&gt;,&lt;I:Y&gt;,[I:breed]</p>
<p>Spawns a new <a href="Animals#Cat_or_Dog" class="wikilink"
title="Cat">Cat</a> at the given coordinates of the current location.
Breed can be <samp>0</samp>, <samp>1</samp>, <samp>2</samp>,
<samp>3</samp>, <samp>4</samp>, or the <samp>Id</samp> of a <a
href="Modding_Pets#Breeds" class="wikilink" title="custom breed">custom
breed</a> added by a mod, and determines which texture to use. This is
an additional pet and does not replace any current pet(s).</p></td>
<td><p>|<a href="#cat" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>changepet</samp></p></td>
<td><p>| <em>Syntax</em>: <code>changepet</code>
&lt;S:petName&gt;,&lt;S:type&gt;,[S:breedId]</p>
<p>Changes the type and breed of an existing pet on the farm with name
<samp>petName</samp>. <samp>type</samp> should match an ID in
<samp>Data/Pets</samp>. Defaults to the first pet breed if none is
specified.</p></td>
<td><p>|<a href="#changepet" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>createdino</samp></p></td>
<td><p>| Spawns a <a href="Pepper_Rex" class="wikilink"
title="Pepper Rex">Pepper Rex</a> just to the right of your
farmer.</p></td>
<td><p>|<a href="#createdino" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dog</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dog</code>
&lt;I:X&gt;,&lt;I:Y&gt;,[I:breed]</p>
<p>Spawns a new <a href="Animals#Cat_or_Dog" class="wikilink"
title="Dog">Dog</a> at the given coordinates of the current location.
Breed can be <samp>0</samp>, <samp>1</samp>, <samp>2</samp>,
<samp>3</samp>, <samp>4</samp>, or the <samp>Id</samp> of a <a
href="Modding_Pets#Breeds" class="wikilink" title="custom breed">custom
breed</a> added by a mod and determines which texture to use. This is an
additional pet and does not replace any current pet(s).</p></td>
<td><p>|<a href="#dog" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>horse</samp></p></td>
<td><p>| <em>Syntax</em>: <code>horse</code> &lt;I:X&gt;,&lt;I:Y&gt;</p>
<p>Spawns a new <a href="Animals#Horse" class="wikilink"
title="Horse">Horse</a> at the given coordinates of the current
location. Horse may disappear after dismounting if there is no stable
for it.</p></td>
<td><p>|<a href="#horse" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>killallhorses</samp></p></td>
<td><p>| Removes all horses from all locations.</p></td>
<td><p>|<a href="#killallhorses" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>monster</samp></p></td>
<td><p>| <em>Syntax</em>: <code>monster</code>
&lt;S:type&gt;,&lt;I:X&gt;,&lt;I:Y&gt;,[I:facingDirection]</p>
<p>Spawns a monster of the specified type at the given coordinates of
the current location. Only certain monster types seem to work. Known
valid types include <samp>Bat</samp>, <samp>DinoMonster</samp>,
<samp>DustSpirit</samp>, <samp>Fly</samp>, <samp>Ghost</samp>,
<samp>GreenSlime</samp>, <samp>Grub</samp>, <samp>LavaCrab</samp>,
<samp>Mummy</samp>, <samp>RockCrab</samp>, <samp>RockGolem</samp>,
<samp>Serpent</samp>, <samp>ShadowBrute</samp>,
<samp>ShadowShaman</samp>, <samp>Skeleton</samp>, and
<samp>SquidKid</samp>. <samp>Duggy</samp> may also work depending on the
terrain.</p></td>
<td><p>|<a href="#monster" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>owl</samp></p></td>
<td><p>| Spawns an Owl in the current location.</p></td>
<td><p>|<a href="#owl" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pettofarm</samp></p></td>
<td><p>| If it is not raining, warps your pet to the pet bowl location
on the Farm (Tech note: Location is initially set by checking for tile
1938 on Building layer). If it is raining, warps pet to the FarmHouse.
Only works for host in multiplayer.</p></td>
<td><p>|<a href="#pettofarm" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setpreferredpet</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setpreferredpet</code>
&lt;S:type&gt;,[S:breedId]</p>
<p>Sets the player's preferred pet type and breed. <samp>type</samp>
should match an ID in <samp>Data/Pets</samp>. Defaults to the first pet
breed if none is specified.</p></td>
<td><p>|<a href="#setpreferredpet" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>togglecatperson</samp></p></td>
<td><p>| Toggles your farmer's chosen pet preference between cat and
dog. If you already have a pet, the inventory graphic will switch but
the pet themselves will not be affected.</p></td>
<td><p>|<a href="#togglecatperson" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

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

### Minigames and cutscenes

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
<td><p><samp>boatjourney</samp></p></td>
<td><p>| Plays the extended cutscene of the first boat trip to <a
href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a>. The player will be warped to the Island Docks when the
cutscene ends.</p></td>
<td><p>|<a href="#boatjourney" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>crane</samp></p></td>
<td><p>| Starts the <a href="Movie_Theater#Crane_Game" class="wikilink"
title="Crane Game">Crane Game</a> minigame from the Movie Theater
populated with prizes based on which movie is (or would be) showing for
the current month.</p></td>
<td><p>|<a href="#crane" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>darts</samp></p></td>
<td><p>| Starts the <a href="Darts" class="wikilink"
title="Darts">Darts</a> minigame from the <a
href="Ginger_Island#Pirate_Cove" class="wikilink"
title="Pirate Cove">Pirate Cove</a>.</p></td>
<td><p>|<a href="#darts" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fish</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fish</code> &lt;I:fishID&gt;</p>
<p>Starts the fishing minigame with the specified fish hooked and a
treasure chest available. You must have a fishing line already cast into
the water before entering the command in order to actually receive the
fish after completing the minigame. Additional "hits" may trigger during
the game, and none of the fishing pole animations will play. See <a
href="Modding_Objects" class="wikilink" title="object data">object
data</a> for a list of valid IDs; non-fish objects can be used and
caught.</p></td>
<td><p>|<a href="#fish" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>minegame</samp></p></td>
<td><p>| <em>Syntax</em>: <code>minegame</code> [S:mode]</p>
<p>Starts the <a href="Junimo_Kart" class="wikilink"
title="Junimo Kart">Junimo Kart</a> minigame. If the second argument is
<samp>infinite</samp> the game will play <em>Endless</em> mode; if it is
anything else (or missing), the game will play <em>Progress</em>
mode.</p></td>
<td><p>|<a href="#minegame" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>minigame</samp></p></td>
<td><p>| <em>Syntax</em>: <code>minigame</code> &lt;S:which&gt;</p>
<p>Starts the specified minigame or cutscene. Valid choices are listed
below.</p></td>
<td><p>|<a href="#minigame" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>movieSchedule</samp></p></td>
<td><p>| <em>Syntax</em>: <code>movieSchedule</code> [I:year]</p>
<p>Lists the movies that will play in the given year (default this
year), with the dates they'll play.</p></td>
<td><p>|<a href="#movieSchedule" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>test</samp></p></td>
<td><p>| Starts the <em>Test</em> minigame. This brings up a window
showing a variety of flooring textures; left-click closes the
window.</p></td>
<td><p>|<a href="#test" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Shops

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
<td><p><samp>exportShops</samp></p></td>
<td><p>| Export a summary of what's in every shop in the game, taking
into account their current conditions. This is saved to a file on disk,
and the file path shown in the console.</p></td>
<td><p>|<a href="#exportShops" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>shop</samp></p></td>
<td><p>| <em>Syntax</em>: <code>shop</code>
&lt;shopID&gt;,[ownerName]</p>
<p>Open a <a href="Modding_Shops" class="wikilink"
title="shop defined in Data/Shops">shop defined in
<samp>Data/Shops</samp></a>, regardless of whether one of the owners is
nearby. Specifying [ownerName] will use that NPC, otherwise the command
will find the closest valid NPC if possible (else open with no
NPC).</p></td>
<td><p>|<a href="#shop" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Locations

#### Terrain, trees, and crops

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
<td><p><samp>artifactSpots</samp></p></td>
<td><p>| Spawn an <a href="Artifact_Spot" class="wikilink"
title="artifact spot">artifact spot</a> in each empty tile around the
player.</p></td>
<td><p>|<a href="#artifactSpots" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearfarm</samp></p></td>
<td><p>| Removes nearly everything from the Farm map such as grass,
trees, debris, paths, and placed objects (including working machines and
filled chests.)</p></td>
<td><p>|<a href="#clearfarm" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dayupdate</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dayupdate</code> [I:number]</p>
<p>Runs the DayUpdate for the current location the specified number of
times. If the number of updates is not specified, it will default to 1.
This simulates days passing for some things such as grass and fruit
trees growing or fish reproducing in ponds. Other things may not
progress the full amount; for example crop growth only advances one day
because sprinklers will not be triggered and the <a href="#growcrops"
class="wikilink" title="growcrops">growcrops</a> command should be used
for that instead.</p></td>
<td><p>|<a href="#dayupdate" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fruittrees</samp></p></td>
<td><p>| Adds a month of growth to all fruit trees in the current
location, causing even newly-planted saplings to instantly
mature.</p></td>
<td><p>|<a href="#fruittrees" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>grass</samp></p></td>
<td><p>| Spawns long grass on all available tiles in the current
location.</p></td>
<td><p>|<a href="#grass" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>growcrops</samp></p></td>
<td><p>| <em>Syntax</em>: <code>growcrops</code> &lt;I:number&gt;</p>
<p>Grows all crops in the current location the specified number of
days.</p></td>
<td><p>|<a href="#growcrops" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>growgrass</samp></p></td>
<td><p>| <em>Syntax</em>: <code>growgrass</code> &lt;I:number&gt;</p>
<p>Grows long grass the specified number of times in the current
location. This will cause already-placed grass to spread but will not
necessarily create grass in clear areas.</p></td>
<td><p>|<a href="#growgrass" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>growwildtrees</samp></p></td>
<td><p>| Grows all wild trees (such as Oak) in the current location to
maturity. This command may be broken as it can de-age fully grown trees,
even ones with existing tappers.</p></td>
<td><p>|<a href="#growwildtrees" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>localinfo</samp></p></td>
<td><p>| Outputs counts of grass, trees, other terrain features,
objects, and temporary sprites for the current location. May be
broken.</p></td>
<td><p>|<a href="#localinfo" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>mushroomtrees</samp></p></td>
<td><p>| Turns all wild trees in the current location into mushroom
trees.</p></td>
<td><p>|<a href="#mushroomtrees" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>r</samp><br />
<samp>resetForPlayerEntry</samp></p></td>
<td><p>| Resets current location which essentially simulates the player
leaving and reentering. Most noticeable effect is the restarting of
music tracks.</p></td>
<td><p>|<a href="#r" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removedebris</samp></p></td>
<td><p>| Removes all dropped items from the current location.</p></td>
<td><p>|<a href="#removedebris" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removedirt</samp></p></td>
<td><p>| Removes (<em>i.e.,</em> untills) all tilled dirt in the current
location.<br />
<strong>Warning: this includes removing any currently-planted crops
(including fully-grown ones).</strong></p></td>
<td><p>|<a href="#removedirt" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removelargetf</samp><br />
<samp>removeLargeTerrainFeature</samp></p></td>
<td><p>| Removes all large terrain features (such as bushes) from the
current location.</p></td>
<td><p>|<a href="#removelargetf" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removeterrainfeatures</samp><br />
<samp>removetf</samp></p></td>
<td><p>| Removes all (small) terrain features such as grass and tilled
dirt from the current location.<br />
<strong>Warning: this includes removing any currently-planted crops
(including fully-grown ones).</strong></p></td>
<td><p>|<a href="#removeterrainfeatures" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>spawnweeds</samp></p></td>
<td><p>| <em>Syntax</em>: <code>spawnweeds</code> &lt;I:number&gt;</p>
<p>Spawns weeds the specified number of times. This will cause
already-placed weeds to spread but will not necessarily create new weeds
in clear areas.</p></td>
<td><p>|<a href="#spawnweeds" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>spreaddirt</samp></p></td>
<td><p>| Tills all unoccupied diggable tiles in the current
location.</p></td>
<td><p>|<a href="#spreaddirt" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>spreadseeds</samp></p></td>
<td><p>| <em>Syntax</em>: <code>spreadseeds</code> &lt;I:seedID&gt;</p>
<p>Plants specified seed in all tilled dirt in the current location. The
argument is the <a href="Modding_Objects" class="wikilink"
title="object ID">object ID</a> for the seed item. Out of season crops
can be planted this way but will not survive outside of the
greenhouse.<br />
<strong>Warning: this will replace any currently-planted crops
(including fully-grown ones) with the new seeds.</strong></p>
<p><em>Example:</em> <code>debug spreadseeds 472</code> would plant <a
href="Parsnip" class="wikilink" title="parsnips">parsnips</a> on all
hoed dirt tiles.</p></td>
<td><p>|<a href="#spreadseeds" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>water</samp></p></td>
<td><p>| Waters all tilled soil on the current map.</p></td>
<td><p>|<a href="#water" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>watercolor</samp></p></td>
<td><p>| <em>Syntax</em>: <code>watercolor</code>
&lt;I:R&gt;,&lt;I:G&gt;,&lt;I:B&gt;</p>
<p>Tints the water color for the current location. The parameters are
red, green, and blue components and the actual RGBA color used will be
(R/2, G/2, B/2, 127). This affects fishing ponds as well as lakes,
rivers, etc., but the effect is temporary and the color will reset to
normal if you leave and re-enter the map.</p></td>
<td><p>|<a href="#watercolor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>whereore</samp></p></td>
<td><p>| Outputs (to the SMAPI console) the coordinates of any "shiny
spots" suitable for panning on the current map. Will output <samp>{X:0
Y:0}</samp> if there are no active panning spots.</p></td>
<td><p>|<a href="#whereore" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Objects and lights

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
<td><p><samp>clearfurniture</samp></p></td>
<td><p>| Removes all furniture from the current location. Can be used in
a farmhouse/cabin, or outside the farmhouse as well.</p></td>
<td><p>|<a href="#clearfurniture" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearlightglows</samp></p></td>
<td><p>| Removes all light glows from the current location.</p></td>
<td><p>|<a href="#clearlightglows" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fencedecay</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fencedecay</code> &lt;I:amount&gt;</p>
<p>Ages all fences in the current location the specified amount of
days.</p>
<p><em>Example:</em> <code>debug fencedecay 60</code> would age all
fences by 60 days which would break any basic Wood Fences (their base
health is 54-58 days).</p></td>
<td><p>|<a href="#fencedecay" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fillwithobject</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fillwithobject</code>
&lt;I:itemID&gt;,[S:isBigCraftable]</p>
<p>Places the specified item on all open tiles in the current location.
The first argument is the <a href="Modding_Objects" class="wikilink"
title="object">object</a> or <a href="Modding_Big_craftables"
class="wikilink" title="big craftable">big craftable</a> ID. If the
second argument is "<samp>true</samp>", the ID will be interpreted as a
craftable, but if it is anything else (or missing) the ID will be
interpreted as an object. Note that many objects spawned this way cannot
be easily removed.</p>
<p><em>Example:</em> <code>debug fillwithobject 13 true</code> would
fill the map with <a href="Furnace" class="wikilink"
title="furnaces">furnaces</a>.</p></td>
<td><p>|<a href="#fillwithobject" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>readyforharvest</samp><br />
<samp>rfh</samp></p></td>
<td><p>| <em>Syntax</em>: <code>readyforharvest</code>
&lt;I:X&gt;,&lt;I:Y&gt;</p>
<p>Sets the machine at the specified coordinates to finish processing at
the next clock update. If used to target a rock in the mine, quarry,
etc. the rock's health will be reduced such that it only needs 1 more
hit to break. A mod such as <a
href="https://www.nexusmods.com/stardewvalley/mods/679">Debug Mode</a>
may be useful for getting coordinates.</p></td>
<td><p>|<a href="#readyforharvest" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>listLights</samp></p></td>
<td><p>| Show debug info about all currently active light
sources.</p></td>
<td><p>|<a href="#listLights" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removefurniture</samp></p></td>
<td><p>| Removes all furniture from the current location. Similar to <a
href="#clearfurniture" class="wikilink"
title="clearfurniture">clearfurniture</a> but will also work in other
decoratable locations such as sheds.</p></td>
<td><p>|<a href="#removefurniture" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removelights</samp></p></td>
<td><p>| Removes all light sources from the current location. This is
temporary and they will be restored if the location is reset or
re-entered.</p></td>
<td><p>|<a href="#removelights" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removeobjects</samp></p></td>
<td><p>| Removes all placed objects from the current location. This
includes things like fences, machines, and chests, but does not include
flooring or long grass.</p></td>
<td><p>|<a href="#removeobjects" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Farm buildings

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
<td><p><samp>build</samp></p></td>
<td><p>| <em>Syntax</em>: <code>build</code>
&lt;S:Name&gt;,[I:X],[I:Y]</p>
<p>Builds the specified building at the given coordinates. Names are
case-insensitive, and will list fuzzy matches if an exact match isn't
found. If the name includes spaces, quote them (e.g. <samp>"Junimo
Hut"</samp>). If the coordinates are not specified, it will build just
to the right of your farmer. While higher-level farm buildings such as
Deluxe Barns can be immediately built this way, the incubator will be
missing from Big or Deluxe Coops.</p>
<p><em>Example:</em> <code>debug build "Stone Cabin"</code> would build
a new Stone Cabin next to the player.</p></td>
<td><p>|<a href="#build" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>buildcoop</samp><br />
<samp>bc</samp></p></td>
<td><p>| <em>Syntax</em>: <code>buildcoop</code>
&lt;I:X&gt;,&lt;I:Y&gt;</p>
<p>Tries to build a new coop at the specified position in the current
location. Finishes construction instantly.</p></td>
<td><p>|<a href="#buildcoop" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>finishallbuilds</samp><br />
<samp>fab</samp></p></td>
<td><p>| Finishes all buildings under construction. Only the host player
can use this command in multiplayer.</p></td>
<td><p>|<a href="#finishallbuilds" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>forcebuild</samp></p></td>
<td><p>| <em>Syntax</em>: <code>forcebuild</code>
&lt;S:Name&gt;,[I:X],[I:Y]</p>
<p>Equivalent to <samp>build</samp>, but disables all safety checks so
you can build in a location that wouldn't normally allow buildings,
build on top of farm animals or placed objects, etc.</p>
<p><em>Example:</em> <code>debug build "Stone Cabin"</code> would build
a new Stone Cabin next to the player.</p></td>
<td><p>|<a href="#forcebuild" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>movebuilding</samp></p></td>
<td><p>| <em>Syntax</em>: <code>movebuilding</code>
&lt;I:sourceX&gt;,&lt;I:sourceY&gt;,&lt;I:destX&gt;,&lt;I:destY&gt;</p>
<p>Moves building in the current location from specified source
coordinates to specified destination coordinates. The coordinates are
the upper-left corner of the building's footprint. The <a
href="https://www.nexusmods.com/stardewvalley/mods/541">Lookup
Anything</a> mod is one of the easier ways to get the source coordinates
of a building; they are listed under <samp>tileX</samp> and
<samp>tileY</samp> in the debug info (needs
<samp>ShowDataMiningFields</samp> enabled.)</p></td>
<td><p>|<a href="#movebuilding" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>paintBuilding</samp><br />
<samp>bpm</samp></p></td>
<td><p>| Gets the building the player is standing in front of and opens
a paint menu for that building if it can be painted. If the player is
not standing in front of a building, defaults to the main
farmhouse.</p></td>
<td><p>|<a href="#paintBuilding" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removebuildings</samp></p></td>
<td><p>| Destroys all farm buildings. Animals within any of the
buildings will also be removed, but animals which are outside will not
be.</p></td>
<td><p>|<a href="#removebuildings" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skinbuilding</samp><br />
<samp>bsm</samp></p></td>
<td><p>| If the player is standing right under a building, open a menu
to change the building appearance.</p></td>
<td><p>|<a href="#skinbuilding" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>spawncoopsandbarns</samp></p></td>
<td><p>| <em>Syntax</em>: <code>spawncoopsandbarns</code>
&lt;I:number&gt;</p>
<p>Spawns the specified number of buildings. The game will randomly
choose either a Deluxe Barn full of cows or a Deluxe Coop full of
chickens for each (equal chance). Their locaions are also randomly
chosen and the game will try 20 times to find a spot for each before
giving up. The coops created by this command will not have
incubators.</p></td>
<td><p>|<a href="#spawncoopsandbarns" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Farmhouse

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
<td><p><samp>crib</samp></p></td>
<td><p>| <em>Syntax</em>: <code>crib</code> &lt;I:mapID&gt;</p>
<p>Sets the current crib style to the specified value. In the base game,
valid values are <samp>0</samp> (no crib) or <samp>1</samp> (default
crib). Additional styles may be possible through modding as the ID is
appended to the map filename. For example, crib style 1 is specified by
the file <samp>Maps/FarmHouse_Crib_1</samp>.</p></td>
<td><p>|<a href="#crib" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>floor</samp></p></td>
<td><p>| <em>Syntax</em>: <code>floor</code> [I:textureID]</p>
<p>Sets all floors of your farmhouse to the specified texture. Valid
texture numbers are <samp>0 - 55</samp>; see <a href="Flooring"
class="wikilink" title="Flooring">Flooring</a> for previews but note
that the IDs used by the game are 1 less than the numbers used for the
wiki filenames. If no texture is specified, the game will use the next
ID after the current floor texture without checking for overflow which
can create bugged textures.</p>
<p><em>Example:</em> <code>debug floor 22</code> would set all flooring
in the house to the white and grey checkerboard style.</p></td>
<td><p>|<a href="#floor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>houseupgrade</samp><br />
<samp>house</samp><br />
<samp>hu</samp></p></td>
<td><p>| <em>Syntax</em>: <code>houseupgrade</code>
&lt;I:upgradeLevel&gt;</p>
<p>Sets upgrade level of your farmhouse/cabin to the specified value.
Valid values are <samp>0 - 3</samp>. Furniture and placed items will not
be automatically moved and may wind up out of bounds. If done while the
player is inside the house, warp points may not immediately
update.</p></td>
<td><p>|<a href="#houseupgrade" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>logWallAndFloorWarnings</samp></p></td>
<td><p>| Enable debug logs when applying wallpaper and flooring to a
farmhouse (or other decoratable location) to help troubleshoot cases
where they don't work with a custom map. You'd usually enable this
before loading the save.</p></td>
<td><p>|<a href="#logWallAndFloorWarnings" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>renovate</samp></p></td>
<td><p>| Opens the <a href="Carpenter&#39;s_Shop#House_Renovations"
class="wikilink" title="farmhouse renovation">farmhouse renovation</a>
menu.</p></td>
<td><p>|<a href="#renovate" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>thishouseupgrade</samp><br />
<samp>thishouse</samp><br />
<samp>thu</samp></p></td>
<td><p>| <em>Syntax</em>: <code>thishouseupgrade</code>
&lt;I:upgradeLevel&gt;</p>
<p>Equivalent to <samp>houseupgrade</samp>, but can be used to upgrade
another player's house by running it from inside or just south of its
exterior.</p></td>
<td><p>|<a href="#thishouseupgrade" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>upgradehouse</samp></p></td>
<td><p>| Increases the upgrade level of your farmhouse/cabin to the next
level (max 3). Furniture and placed items will not be automatically
moved and may wind up out of bounds. If done while the player is inside
the house, warp points may not immediately update.</p></td>
<td><p>|<a href="#upgradehouse" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>wall</samp><br />
<samp>w</samp></p></td>
<td><p>| <em>Syntax</em>: <code>wall</code> [I:textureID]</p>
<p>Sets all walls of your farmhouse to the specified texture. Valid
texture numbers are <samp>0 - 111</samp>; see <a href="Wallpaper"
class="wikilink" title="Wallpaper">Wallpaper</a> for previews but note
that the IDs used by the game are 1 less than the numbers used for the
wiki filenames. If no texture is specified, the game will use the next
ID after the current wallpaper texture without checking for overflow
which can create bugged textures.</p>
<p><em>Example:</em> <code>debug wall 21</code> would set all wallpaper
in the house to the Joja style.</p></td>
<td><p>|<a href="#wall" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Special farm setups

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
<td><p><samp>farmmap</samp></p></td>
<td><p>| <em>Syntax</em>: <code>farmmap</code> [I:mapID]</p>
<p>Removes the current farm map and farmhouse from the game and creates
a new farm of the specified type. The farm will be named after the type
(<em>e.g.,</em> "Standard Farm"). Valid types are: <samp>0</samp>
(Standard), <samp>1</samp> (Riverland), <samp>2</samp> (Forest),
<samp>3</samp> (Hilltop), <samp>4</samp> (Wilderness), <samp>5</samp>
(Four Corners), <samp>6</samp> (Beach), and <samp>7</samp>
(Meadowlands)</p></td>
<td><p>|<a href="#farmmap" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setupbigfarm</samp></p></td>
<td><p>| Clears the farm and then does the following:</p></td>
<td><p>|<a href="#setupbigfarm" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setupfarm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setupfarm</code> [S:clearMore]</p>
<p>Removes all farm buildings and completely clears large areas of the
current farm. After this, the following things are done:</p></td>
<td><p>|<a href="#setupfarm" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setupfishpondfarm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setupfishpondfarm</code>
[I:population]</p>
<p>Clears farm and then builds up to 96 fish ponds randomly filled with
various types of fish. The population of each of the ponds will be set
to the specified value and defaults to 10. The ponds are built in a
large 12 x 8 grid but will not be placed in a spot blocked by other
buildings, animals, or map features.</p></td>
<td><p>|<a href="#setupfishpondfarm" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Community center and bundles

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
<td><p><samp>addjunimo</samp><br />
<samp>aj</samp><br />
<samp>j</samp></p></td>
<td><p>| <em>Syntax</em>: <code>addjunimo</code>
&lt;I:X&gt;,&lt;I:Y&gt;,&lt;I:area&gt;</p>
<p>Adds a junimo at the specified coordinates and assigned to the given
Community Center area. Valid areas are <samp>0</samp> (Pantry),
<samp>1</samp> (Crafts Room), <samp>2</samp> (Fish Tank), <samp>3</samp>
(Boiler Room), <samp>4</samp> (Vault), or <samp>5</samp> (Bulletin
Board).</p></td>
<td><p>|<a href="#addjunimo" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>allbundles</samp></p></td>
<td><p>| Marks all bundles complete.</p></td>
<td><p>|<a href="#allbundles" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>bundle</samp></p></td>
<td><p>| <em>Syntax</em>: <code>bundle</code> &lt;I:ID&gt;</p>
<p>Marks the specified bundle as complete. Valid IDs are listed
below.</p></td>
<td><p>|<a href="#bundle" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>ccload</samp></p></td>
<td><p>| <em>Syntax</em>: <code>ccload</code> &lt;I:area&gt;</p>
<p>Removes the junimo note from and restores the specified area. Valid
areas are <samp>0</samp> (Pantry), <samp>1</samp> (Crafts Room),
<samp>2</samp> (Fish Tank), <samp>3</samp> (Boiler Room), <samp>4</samp>
(Vault), or <samp>5</samp> (Bulletin Board).</p></td>
<td><p>|<a href="#ccload" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>ccloadcutscene</samp></p></td>
<td><p>| <em>Syntax</em>: <code>ccloadcutscene</code> &lt;I:area&gt;</p>
<p>Plays the full restoration cutscene for the specified area including
junimo dance and star retrieval. Valid areas are <samp>0</samp>
(Pantry), <samp>1</samp> (Crafts Room), <samp>2</samp> (Fish Tank),
<samp>3</samp> (Boiler Room), <samp>4</samp> (Vault), or <samp>5</samp>
(Bulletin Board).</p></td>
<td><p>|<a href="#ccloadcutscene" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>completecc</samp></p></td>
<td><p>| Adds all of the appropriate flags for Community Center
completion and restores all areas.</p></td>
<td><p>|<a href="#completecc" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>completejoja</samp></p></td>
<td><p>| Adds all of the appropriate flags for Joja membership and
Community Development purchases.</p></td>
<td><p>|<a href="#completejoja" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>junimogoodbye</samp></p></td>
<td><p>| Plays the animation where 6 junimos wave goodbye in front of
the hut in the Community Center and then that corner of the Community
Center gets restored.</p></td>
<td><p>|<a href="#junimogoodbye" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>junimonote</samp><br />
<samp>jn</samp></p></td>
<td><p>| <em>Syntax</em>: <code>junimonote</code> &lt;I:area&gt;</p>
<p>Adds a junimo note (bundle scroll) for the specified area. Valid
areas are <samp>0</samp> (Pantry), <samp>1</samp> (Crafts Room),
<samp>2</samp> (Fish Tank), <samp>3</samp> (Boiler Room), <samp>4</samp>
(Vault), or <samp>5</samp> (Bulletin Board).</p></td>
<td><p>|<a href="#junimonote" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>junimostar</samp></p></td>
<td><p>| Causes a junimo to run to the hut and retrieve a star which is
then placed on the plaque above the fireplace. Must be done in the
Community Center.</p></td>
<td><p>|<a href="#junimostar" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>plaque</samp></p></td>
<td><p>| Adds a star to the plaque above the Community Center
fireplace.</p></td>
<td><p>|<a href="#plaque" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>resetjunimonotes</samp></p></td>
<td><p>| Resets all bundles.</p></td>
<td><p>|<a href="#resetjunimonotes" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>shufflebundles</samp></p></td>
<td><p>| Regenerates bundles using remixed bundle logic and without a
specific random seed.</p></td>
<td><p>|<a href="#shufflebundles" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Other location-specific functions

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
<td><p><samp>activatecalicostatue</samp></p></td>
<td><p>| Spawns and activates a new Calico Statue from the <a
href="Desert_Festival#Skull_Cavern" class="wikilink"
title="Desert Festival">Desert Festival</a> at point (8, 8) on the
player's current mines level. If the player is in the regular mines
instead of the Skull Cavern, the statue will not visually spawn but some
animations and effects will still occur.</p></td>
<td><p>|<a href="#activatecalicostatue" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>beachbridge</samp></p></td>
<td><p>| Toggles the state of the beach bridge between fixed and not
fixed.</p></td>
<td><p>|<a href="#beachbridge" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>ladder</samp><br />
<samp>shaft</samp></p></td>
<td><p>| <em>Syntax</em>: <code>ladder</code> [I:X],[I:Y]</p>
<p>Creates a ladder or mineshaft at the specified coordinates. If no
coordinates are given, it will spawn 1 tile north of the player. In the
regular mines, both versions of the command will create a ladder. In the
Skull Caverns, <samp>ladder</samp> will randomly spawn either a ladder
or mineshaft while <samp>shaft</samp> will always spawn a
mineshaft.</p></td>
<td><p>|<a href="#ladder" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>minedifficulty</samp><br />
<samp>md</samp></p></td>
<td><p>| <em>Syntax</em>: <code>minedifficulty</code>
[I:difficultyLevel]</p>
<p>Sets the difficulty of the mines to the specified level. In the base
game, normal difficulty is <samp>0</samp> and the harder difficulty
corresponding to the "Danger in the Deep" quest or <a
href="The_Mines#Shrine_of_Challenge" class="wikilink"
title="Shrine of Challenge">Shrine of Challenge</a> activation is
<samp>1</samp>. Higher numbers can be used. If no difficulty level is
specified, command will simply print the current difficulty level to the
console.</p></td>
<td><p>|<a href="#minedifficulty" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>movie</samp></p></td>
<td><p>| <em>Syntax</em>: <code>movie</code>
[S:movieID],[S:inviteNpcName]</p>
<p>Starts a movie. The movie ID defaults to today's movie, and the NPC
name can be omitted to watch the movie without an invitee. Note that
this command can create a group with up to 3 guests instead of just the
single guest allowed in normal play. Valid vanilla movie IDs are listed
below.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug movie</code> would show <em>It Howls in the Rain</em>
with random NPC guests.</li>
</ul>
<ul>
<li><code>debug movie spring_movie_1</code> would show <em>Natural
Wonders</em> with random NPC guests.</li>
</ul>
<ul>
<li><code>debug movie summer_movie_0 Abi</code> would show <em>Journey
of the Prairie King</em> with Abigail and possibly 1 or 2 additional
random NPC guests.</li>
</ul></td>
<td><p>|<a href="#movie" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pgb</samp><br />
<samp>printGemBirds</samp></p></td>
<td><p>| Prints the <a href="Ginger_Island#Gem_Birds" class="wikilink"
title="Gem Bird Puzzle">Gem Bird Puzzle</a> solution to the
console.</p></td>
<td><p>|<a href="#pgb" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>resetmines</samp></p></td>
<td><p>| Resets "permanent mine changes" such as coal carts and treasure
chests. Does not affect mines level progress or monster eradication
goals.</p></td>
<td><p>|<a href="#resetmines" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>returneddonations</samp></p></td>
<td><p>| Opens the "returned donations" menu of the Lost and Found box
from the <a href="Mayor&#39;s_Manor" class="wikilink"
title="Mayor&#39;s Manor">Mayor's Manor</a>.</p></td>
<td><p>|<a href="#returneddonations" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skullcavedifficulty</samp><br />
<samp>scd</samp></p></td>
<td><p>| <em>Syntax</em>: <code>skullcavedifficulty</code>
[I:difficultyLevel]</p>
<p>Sets the difficulty of the Skull Cavern to the specified level. In
the base game, normal difficulty is <samp>0</samp> and the harder
difficulty corresponding to the "Skull Cavern Invasion" quest is
<samp>1</samp>. Higher numbers can be used. If no difficulty level is
specified, command will simply print the current difficulty level to the
console.</p>
<p><em>Example:</em> <code>debug scd 1</code> would activate hard mode
Skull Cavern outside of the "Skull Cavern Invasion" quest.</p></td>
<td><p>|<a href="#skullcavedifficulty" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>train</samp></p></td>
<td><p>| Causes a train to spawn at the Railroad.</p></td>
<td><p>|<a href="#train" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### World

#### Date and time

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
<td><p><samp>addhour</samp></p></td>
<td><p>| Increases time by 1 hour.</p></td>
<td><p>|<a href="#addhour" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>addminute</samp></p></td>
<td><p>| Increases time by 10 minutes.</p></td>
<td><p>|<a href="#addminute" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>day</samp></p></td>
<td><p>| <em>Syntax</em>: <code>day</code> &lt;I:value&gt;</p>
<p>Changes day of the month to the specified value; stays in current
season and adjusts <samp>daysPlayed</samp> statistic
appropriately.</p></td>
<td><p>|<a href="#day" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pausetime</samp></p></td>
<td><p>| Toggles game pause state. This is different from the normal
chat <samp>/pause</samp> command in that the player still has free
movement during the pause.</p></td>
<td><p>|<a href="#pausetime" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>season</samp></p></td>
<td><p>| <em>Syntax</em>: <code>season</code> &lt;S:name&gt;</p>
<p>Sets season to the specified value. The season name is
case-insensitive; valid names are <samp>spring</samp>,
<samp>summer</samp>, <samp>fall</samp>, and
<samp>winter</samp>.</p></td>
<td><p>|<a href="#season" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>sleep</samp><br />
<samp>newday</samp><br />
<samp>nd</samp></p></td>
<td><p>| Forces end of day.</p></td>
<td><p>|<a href="#sleep" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>time</samp></p></td>
<td><p>| <em>Syntax</em>: <code>time</code> &lt;I:value&gt;</p>
<p>Sets current time to the specified value. This is essentially 24-hour
time without a colon, although the stardew clock keeps running until
2600. See examples.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug time 2040</code> would set the time to 20:40 or
8:40pm.</li>
</ul>
<ul>
<li><code>debug time 2550</code> would set the time to 1:50am.</li>
</ul></td>
<td><p>|<a href="#time" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>year</samp></p></td>
<td><p>| <em>Syntax</em>: <code>year</code> &lt;I:value&gt;</p>
<p>Sets the current year to the specified value.</p></td>
<td><p>|<a href="#year" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Weather and world state

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
<td><p><samp>debrisweather</samp></p></td>
<td><p>| Toggles "debris" weather (<em>i.e.,</em> windy weather with
floating leaves) on and off. Does not change the weather icon on the
HUD.</p></td>
<td><p>|<a href="#debrisweather" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>greenrain</samp></p></td>
<td><p>| Toggles green rain weather on and off. Will turn off
debris/windy weather. Does not change the weather icon on the
HUD.</p></td>
<td><p>|<a href="#greenrain" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>morepollen</samp></p></td>
<td><p>| <em>Syntax</em>: <code>morepollen</code> &lt;I:amount&gt;</p>
<p>Increases the amount of leaves flying around if in debris/windy
weather.</p></td>
<td><p>|<a href="#morepollen" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>rain</samp></p></td>
<td><p>| Toggles rainy weather on and off. Will turn off debris/windy
weather. Does not change the weather icon on the HUD.</p></td>
<td><p>|<a href="#rain" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>resetworldstate</samp></p></td>
<td><p>| Clears all world state IDs which track map changes such as
whether the beach bridge is fixed, whether Trash Bear has done his thing
and various small changes from heart events.<br />
<strong>Warning: Also clears records of found artifacts and minerals,
fish caught, events seen, and mail received (including hidden progress
flags.)</strong></p></td>
<td><p>|<a href="#resetworldstate" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
