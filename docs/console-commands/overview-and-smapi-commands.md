---
title: "Overview And Smapi Commands"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, format-used-on-this-page, how-to-enter-console-commands, items-money, player, world, other, advanced]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

**WARNING:** **Console commands aren't meant for general use. Be very
careful using them.** They can have permanent side-effects on your save
data, break your save, or have other unintended effects. If you don't
understand the command, don't use it on a save you care about.'''

SMAPI provides access to hundreds of console commands with a wide
variety of effects, ranging from useful tools to cheats to specialized
test commands. These are documented on this page.

## Format used on this page

To avoid repeating text, this page uses a few conventions to convey
common information:

- Required parameters are listed in angle brackets, and optional
  parameters are listed in square brackets. For example, `speed`
  \<I:value\> \[I:duration\] means the command requires an integer value
  parameter and has an optional integer duration parameter. Details such
  as default values should be listed in the description.
- The command names are case-insensitive, but their parameters might be
  case-sensitive.
- If a command description says that a parameter uses "fuzzy" match,
  that means that it can match on a case-insensitive partial name. For
  example, `abi` would match Abigail if it's fuzzy.

## Console commands

### How to enter console commands

You can enter console commands directly into the SMAPI console window.
You can type `help` to get a list of console commands (including
commands added by other mods).

### Items & money

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
<td><p><samp>list_items</samp></p></td>
<td><p>| <em>Syntax</em>: <code>list_items</code> [S:search text]</p>
<p>Shows a list of every item in the game (including those added by
mods). The optional search text limits results to those which have all
of the search words somewhere in their ID + type + name.</p></td>
<td><p>|<a href="#list_items" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_add name</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_add name</code> &lt;S:item
name&gt;, [I:count], [I:quality]</p>
<p>Adds an item to your inventory based on its name.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>player_add name "Galaxy Sword"</code> will create a Galaxy
Sword.</li>
</ul>
<ul>
<li><code>player_add name "Stir Fry" 10 4</code> will create 10
iridium-quality <a href="Stir_Fry" class="wikilink"
title="stir fry">stir fry</a> dishes.</li>
</ul></td>
<td><p>|<a href="#player_add_name" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_add</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_add</code> &lt;I:item ID&gt;,
[I:count], [I:quality]</p>
<p>Adds an item to your inventory based on its item ID.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>player_add (O)246</code> will create a <a href="Wheat_Flour"
class="wikilink" title="wheat flour">wheat flour</a> item.</li>
</ul>
<ul>
<li><code>player_add (O)128 10 4</code> would create 10 iridium-quality
<a href="pufferfish" class="wikilink"
title="pufferfish">pufferfish</a>.</li>
</ul></td>
<td><p>|<a href="#player_add" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>player_setmoney</samp></p></td>
<td><p>| <em>Syntax</em>: <code>player_setmoney</code>
&lt;I:amount&gt;</p>
<p>Changes the player's total money to the given amount of gold.</p>
<p><em>Example:</em> <code>player_setmoney 5000</code> will change your
total money to 5000g.</p></td>
<td><p>|<a href="#player_setmoney" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

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
