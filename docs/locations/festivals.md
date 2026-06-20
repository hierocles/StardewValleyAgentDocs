---
title: "Festivals"
wiki_source: "Modding:Festival data"
permalink: /Modding:Festival_data/
category: locations
tags: [festival-data, data-file, raw-data, format, year-variants, shop-format, map, spawned-npcs]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and uses festival data. This is
an advanced guide for mod developers.

## Data file

Each festival has a data file located at
`Data/Festivals/<season><day of month>`. The game uses this asset to
determine whether there's a festival today (if the asset exists), where
and when it happens, and NPC placement/dialogue/behavior. The game also
has a data file located at `Data/Festivals/FestivalDates` which contains
the names and dates of festivals. Mod authors who wish to add a custom
festival will need to add an entry to it as well.

### Raw data

The festival data file can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. For example,
here's the raw data from `Data/Festivals/fall27` as of for reference:

### Format

<table>
<thead>
<tr>
<th><p>field key</p></th>
<th><p>explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>name</samp></p></td>
<td><p>The festival name. This is used in display text like the calendar
tooltip or the festival-is-ready message.</p></td>
</tr>
<tr>
<td><p><samp>conditions</samp></p></td>
<td><p>When and where the festival takes place. The format is
<samp>&lt;location&gt;/&lt;start time&gt; &lt;end time&gt;</samp>, where
&lt;location&gt; is the internal location name and the times are
specified in 26-hour format (<em>i.e.,</em> 600 for 6am to 2600 for
2am).</p></td>
</tr>
<tr>
<td><p><samp>mainEvent</samp></p></td>
<td><p>The main event script. This is triggered when the player asks the
festival host (usually Lewis) to begin the festival. This is absent for
events that do not have a prompt or where speaking to Lewis does not
trigger a new scene.</p></td>
</tr>
<tr>
<td><p><samp>shop</samp></p></td>
<td><p>The items the festival shop sells. See <em><a href="#Shop_format"
class="wikilink" title="shop format">shop format</a></em>
below.</p></td>
</tr>
<tr>
<td><p><samp>set-up</samp></p></td>
<td><p>The <a href="Modding_Event_data" class="wikilink"
title="event script">event script</a> that's run when the player first
enters the festival. This includes moving the player to the festival
map.</p></td>
</tr>
<tr>
<td><p><samp>Set-Up_additionalCharacters</samp></p></td>
<td><p>NPCs to spawn when the festival loads. This is specified as four
space-delimited fields in the form <samp>&lt;NPC name&gt; &lt;tile X&gt;
&lt;tile Y&gt; &lt;facing direction&gt;</samp>, repeated for each NPC to
add with a <code>/</code> between each NPC. The &lt;facing
direction&gt;</samp> can be one of <samp>up</samp> or <samp>0</samp>,
<samp>down</samp> or <samp>2</samp>, <samp>left</samp> or
<samp>3</samp>, and <samp>right</samp> or <samp>1</samp>. These are
additional to the NPCs spawned via the <a href="#Map" class="wikilink"
title="map file">map file</a>. For example, this adds Abigail and Leah
side-by-side facing down:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Set-Up_additionalCharacters&quot;</span><span class="op">:</span> <span class="st">&quot;Abigail 15 6 down/Leah 16 6 down&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>startedMessage</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for a custom
festival-started notification message.</p></td>
</tr>
<tr>
<td><p><samp>MainEvent_additionalCharacters</samp>, or<br />
<samp>Main-Event_additionalCharacters</samp> for the <a
href="Festival_of_Ice" class="wikilink" title="Festival of Ice">Festival
of Ice</a></p></td>
<td><p>NPCs to spawn when the festival's <code>mainEvent</code> script
is run. Just like <code>mainEvent</code>, this is absent for events that
do not have a prompt to start a new scene. The format is identical to
<code>Set-Up_additionalCharacters</code>, above.</p></td>
</tr>
<tr>
<td><p><samp>&lt;NPC name&gt;_roommate</samp></p></td>
<td><p>The <a href="Modding_Dialogue#Format" class="wikilink"
title="dialog line">dialog line</a> the named NPC will say when the
player talks to them, if they're roommates with the player. This field
doesn't work on the Flower Dance festival and doesn't support
<samp>#$e#</samp> breaks. If not specified, the <samp>&lt;NPC
name&gt;_spouse</samp> will be used next.</p></td>
</tr>
<tr>
<td><p><samp>&lt;NPC name&gt;_spouse</samp></p></td>
<td><p>The <a href="Modding_Dialogue#Format" class="wikilink"
title="dialog line">dialog line</a> the named NPC will say when the
player talks to them, if they're married to the player. This field
doesn't work on the Flower Dance festival and doesn't support
<samp>#$e#</samp> breaks.</p></td>
</tr>
<tr>
<td><p><samp>&lt;NPC name&gt;</samp></p></td>
<td><p>The <a href="Modding_Dialogue#Format" class="wikilink"
title="dialog line">dialog line</a> the named NPC will say when the
player talks to them, if <samp>&lt;NPC
name&gt;_spouse&lt;/code&gt;</samp> doesn't exist or apply.</p></td>
</tr>
<tr>
<td><p><samp>locationDisplayName</samp></p></td>
<td><p>The location name in the festival-started message (<em>e.g.,</em>
"<em>The Luau has begun on the beach</em>") by default shows the
internal name for non-vanilla festival locations. You can add this field
to set the display name.</p></td>
</tr>
</tbody>
</table>

Any other entry is
<a href="Modding_Event_data" class="wikilink" title="event data">event
data</a> for a cutscene during the festival. In some cases like the
<a href="Luau" class="wikilink" title="Luau">Luau</a>, these are linked
together when played in the game.

### Year variants

All fields in the festival data allow annual variants. These work by
adding `_y<year variant>` to the end of key, where the \<year variant\>
is an incrementing number starting at 1 with no upper limit. For
example, two entries `set-up_y1` and `set-up_y2` will alternate
(`set-up_y1` in year 1, `set-up_y2` in year 2, `set-up_y1` in year 3,
etc). If year variants are defined for a key, the original key is
ignored (*e.g.,* `set-up` will never be used if `set-up_y*` entries are
defined). **NOTE:**

### Shop format

The shop data for a festival is stored as four space-separated values in
the format `<item type> <item ID> <cost> <count available>`, which is
repeated for each item. Field formats:

| field | explanation |
|----|----|
| \<item type\> | The item type. The valid values are `B` or `Boots` (boots), `BL` or `Blueprint` (blueprint), `BBL`, `BBl` or `BigBlueprint` (big blueprint), `BO` or `BigObject` (bigcraftable object), `F` (furniture), `H` or `Hat` (hat), `O` or `Object` (object), `R` or `Ring` (ring), or `W` or `Weapon` (weapon). |
| `<item id>` | The item's spritesheet index. |
| `<cost>` | The purchase price in gold. For seeds, this is modified based on the <a href="Multiplayer#Profit_margins" class="wikilink"
title="profit margin">profit margin</a>. |
| `<count available>` | How many of that item can be purchased from the shop, or `-1` for unlimited. |

Shop data may also be stored in `Data/Shops` and accessed via a map tile
action, as non-festival shops are.

## Map

Many festivals use a separate
<a href="Modding_Maps" class="wikilink" title="map file">map file</a>
located in the `Maps` folder. The map to use is specified in the
<a href="#Data_file" class="wikilink" title="data file">data file</a>'s
`set-up` field using the `changeToTemporaryMap` command.

### Spawned NPCs

**NOTE:**

NPCs can be added to festivals using map tile indexes on a specific
layer. This is enabled in the
<a href="#Data_file" class="wikilink" title="data file">data file</a>'s
`set-up` field using the `loadActors <layer name>` command. For each
tile which exists on the layer, the tile index is mapped to the NPC's
`FestivalVanillaActorIndex` field in the
<a href="Modding_NPC_data" class="wikilink"
title="Data\Characters asset"><samp>Data\Characters</samp> asset</a>,
with an offset which determines the facing direction (0 = up, 1 = right,
2 = down, or 3 = left).

For example, let's say the layer has a tile with tilesheet index 1. That
matches Abigail's entry (`"FestivalVanillaActorIndex": 0`), with an
offset of 1 so she's facing right. When the festival is loaded, Abigail
will be added to that tile position facing right.

## Hardcoded logic

Several vanilla events have hardcoded scripted logic in the game code.
For example, Lewis judging the farmer's grange display at the
<a href="Stardew_Valley_Fair" class="wikilink"
title="Stardew Valley Fair">Stardew Valley Fair</a> is handled in the
game code, not the content assets documented here.

The <a href="Night_Market" class="wikilink" title="Night Market">Night
Market</a> is also handled differently from other festivals. While there
are separate Night Market maps, the NPC data doesn't exist on these.
Instead, NPCs dynamically enter and leave the festival via schedule
data.

## See also

<a href="Modding_Passive_Festival_data" class="wikilink"
title="Modding:Passive Festival data">Modding:Passive Festival data</a>
for information about passive festivals.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Фестивали" class="wikilink"
title="ru:Модификации:Фестивали">ru:Модификации:Фестивали</a>
<a href="zh_模组_节日数据" class="wikilink"
title="zh:模组:节日数据">zh:模组:节日数据</a>
