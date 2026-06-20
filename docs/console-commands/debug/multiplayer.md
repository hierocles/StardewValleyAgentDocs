---
title: "Multiplayer"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, multiplayer]
---
### Multiplayer

#### General multiplayer

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
<td><p><samp>addotherfarmer</samp></p></td>
<td><p>| Creates an additional new male farmer with randomized name and
appearance which spawns 1 tile to the left of your farmer. Unsure of
what situation this can be used in.</p></td>
<td><p>|<a href="#addotherfarmer" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>nethost</samp></p></td>
<td><p>| Starts a new LAN server. Details unknown.</p></td>
<td><p>|<a href="#nethost" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>netjoin</samp></p></td>
<td><p>| <em>Syntax</em>: <code>netjoin</code> &lt;IP&gt;</p>
<p>Connect to a given IP address.</p></td>
<td><p>|<a href="#netjoin" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>split</samp></p></td>
<td><p>| <em>Syntax</em>: <code>split</code> [I:playerIndex]</p>
<p>Adds another split-screen multiplayer instance for the specified
player index or starts split-screen mode otherwise.</p></td>
<td><p>|<a href="#split" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>validatenetfields</samp></p></td>
<td><p>| Enables net field validation.</p></td>
<td><p>|<a href="#validatenetfields" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Logging

| command | description |   |
|----|----|----|
|  |  |  |
| `logbandwidth` | \| Toggles bandwidth logging on and off. Can be used on either host or client. | \|<a href="#logbandwidth" class="wikilink" title="#">#</a> |
|  |  |  |
| `logFile` | \| Begin writing debug messages to a log file at `%appdata%/StardewValley/ErrorLogs/game-latest.txt` to simplify troubleshooting. You can also enter `/logtext` into the in-game chatbox to enable it. This does nothing if SMAPI is installed, since the debug messages are already saved to SMAPI's log. | \|<a href="#logFile" class="wikilink" title="#">#</a> |
|  |  |  |
| `logSounds` | \| Log info about each sound effect played to the SMAPI console window. | \|<a href="#logSounds" class="wikilink" title="#">#</a> |
|  |  |  |
| `netclear` | \| Clears network message log. | \|<a href="#netclear" class="wikilink" title="#">#</a> |
|  |  |  |
| `netdump` | \| Outputs network message log to a file. | \|<a href="#netdump" class="wikilink" title="#">#</a> |
|  |  |  |
| `netlog` | \| Toggles network message logging on and off. | \|<a href="#netlog" class="wikilink" title="#">#</a> |
|  |  |  |

#### Player relationships

| command | description |   |
|----|----|----|
|  |  |  |
| `dateplayer` | \| Checks all other farmers and sets the first one found as dating the player. | \|<a href="#dateplayer" class="wikilink" title="#">#</a> |
|  |  |  |
| `engageplayer` | \| Checks all other farmers and sets the first one found as engaged to the player with a wedding date of the next game day. | \|<a href="#engageplayer" class="wikilink" title="#">#</a> |
|  |  |  |
| `testwedding` | \| Immediately play the <a href="Marriage#The_Wedding" class="wikilink"
title="wedding">wedding</a> event. This requires the player to be married first - to test specific NPCs, `debug marry` the NPC followed by this command. | \|<a href="#testwedding" class="wikilink" title="#">#</a> |
|  |  |  |
| `marryplayer` | \| Checks all online farmers and sets the first one found as married to the player with a wedding date of the current game day. | \|<a href="#marryplayer" class="wikilink" title="#">#</a> |
|  |  |  |

#### Shared/split money

| command | description |   |
|----|----|----|
|  |  |  |
| `changewallet` | \| Sets the game to toggle between shared or split money overnight. Host only. | \|<a href="#changewallet" class="wikilink" title="#">#</a> |
|  |  |  |
| `mergewallets` | \| Immediately switches to shared money, merging all player wallets. Host only. | \|<a href="#mergewallets" class="wikilink" title="#">#</a> |
|  |  |  |
| `separatewallets` | \| Immediately switches to split money, separating all player wallets. Host only. | \|<a href="#separatewallets" class="wikilink" title="#">#</a> |
|  |  |  |
