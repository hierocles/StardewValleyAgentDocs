---
title: "Track List"
wiki_source: "Modding:Audio"
permalink: /Modding:Audio/
category: game
tags: [audio, track-list, footsteps, music, music-ambient, sound, manage-audio-in-c, playing-sounds]
---
## Track list

These are the raw soundbank IDs for music and sounds exported from the
game data (see the
<a href="Modding_talk_Audio" class="wikilink" title="talk page">talk
page</a> for the export code).

A few notes about the table columns:

- The name is what you'd use in-game (*e.g.,* with the `Music`
  <a href="Modding_Maps" class="wikilink" title="map property">map
  property</a> or the `Game1.changeMusicTrack` method). When a name is
  repeated with different soundbank IDs, the game will choose a random
  sound each time you play it.
- The wavebank indicates whether the audio is from
  `Content/XACT/Wave Bank.xwb` or `Content/XACT/Wave Bank(1.4).xwb`.
  Each wavebank has its own set of soundbank IDs, but names don't
  overlap.
- The soundtrack index is the sound's position in the soundbank. The
  hexadecimal version matches the track's filename if you unpack the
  wavebank using unxwb.
- The description column is filled in manually for the wiki.

See also an [older spreadsheet with more comprehensive
descriptions](https://docs.google.com/spreadsheets/d/1CpDrw23peQiq-C7F2FjYOMePaYe0Rc9BwQsj3h6sjyo).
(Don't copy text from that spreadsheet into this page, since it's not
licensed!)

### Footsteps

<table>
<thead>
<tr>
<th><p>cue ID</p></th>
<th><p>wavebank</p></th>
<th colspan="2"><p>soundbank index</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>dec</p></td>
<td><p>hex</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>Cowboy_Footstep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>269</samp></p></td>
<td data-sort-value="269"><p><samp>0000010d</samp></p></td>
<td><p>Mainly used as the footstep sound for pets, in <a
href="Prairie_King_Arcade_System" class="wikilink"
title="Prairie King">Prairie King</a>, and as a hover sound in various
menus (including the title screen buttons).</p></td>
</tr>
<tr>
<td><p><samp>grassyStep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>22</samp></p></td>
<td data-sort-value="22"><p><samp>00000016</samp></p></td>
<td><p>Mainly used as the player footstep sound on grass tiles, when
adding hay to a silo, when changing a player's hat or hairstyle, and for
rustling bushes in <a href="Marnie#Six_Hearts" class="wikilink"
title="Lewis and Marnie&#39;s six-heart event">Lewis and Marnie's
six-heart event</a>.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>jingleBell</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>433</samp></p></td>
<td data-sort-value="433"><p><samp>000001b1</samp></p></td>
<td rowspan="3"><p>A sleigh bell jingling once. Mainly used as the
player's footstep sound when they wear <a href="Cinderclown_Shoes"
class="wikilink" title="Cinderclown Shoes">Cinderclown
Shoes</a>.</p></td>
</tr>
<tr>
<td><p><samp>434</samp></p></td>
<td data-sort-value="434"><p><samp>000001b2</samp></p></td>
</tr>
<tr>
<td><p><samp>435</samp></p></td>
<td data-sort-value="435"><p><samp>000001b3</samp></p></td>
</tr>
<tr>
<td><p><samp>sandyStep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>16</samp></p></td>
<td data-sort-value="16"><p><samp>00000010</samp></p></td>
<td><p>Mainly used as the player footstep sound on dirt tiles. Also
plays when new clothes are put on the farmer.</p></td>
</tr>
<tr>
<td><p><samp>snowyStep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>340</samp></p></td>
<td data-sort-value="340"><p><samp>00000154</samp></p></td>
<td><p>Mainly used as the player footstep sound on grass tiles in
winter.</p></td>
</tr>
<tr>
<td><p><samp>stoneStep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>23</samp></p></td>
<td data-sort-value="23"><p><samp>00000017</samp></p></td>
<td><p>Mainly used as the player footstep sound on stone tiles. Also
plays when the player selects an inventory slot or places an item in
their inventory.</p></td>
</tr>
<tr>
<td><p><samp>thudStep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>24</samp></p></td>
<td data-sort-value="24"><p><samp>00000018</samp></p></td>
<td><p>Mainly used as a fallback player footstep sound when other sounds
do not apply, particularly in indoors locations.</p></td>
</tr>
<tr>
<td><p><samp>woodyStep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>29</samp></p></td>
<td data-sort-value="29"><p><samp>0000001d</samp></p></td>
<td><p>Mainly used as the player footstep sound on wood tiles.</p></td>
</tr>
</tbody>
</table>

### Music

<table>
<thead>
<tr>
<th><p>cue ID</p></th>
<th><p>wavebank</p></th>
<th colspan="2"><p>soundbank index</p></th>
<th><p>title in <a href="jukebox" class="wikilink"
title="jukebox">jukebox</a> and <a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a></p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>dec</p></td>
<td><p>hex</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>50s</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>45</samp></p></td>
<td data-sort-value="45"><p><samp>0000002d</samp></p></td>
<td><p><em>Pleasant Memory (Penny's Theme)</em></p></td>
<td><p>A peaceful clarinet and marimba track in 3.</p></td>
</tr>
<tr>
<td><p><samp>AbigailFlute</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>279</samp></p></td>
<td data-sort-value="279"><p><samp>00000117</samp></p></td>
<td><p><em>A Stillness in the Rain Solo</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>A Stillness in the Rain (Abigail's Melody)</em> (<a
href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A solo flute melody.</p></td>
</tr>
<tr>
<td><p><samp>AbigailFluteDuet</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>280</samp></p></td>
<td data-sort-value="280"><p><samp>00000118</samp></p></td>
<td><p><em>A Stillness in the Rain Duet</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>A Stillness in the Rain</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>The same melody as in <samp>AbigailFlute</samp>, but accompanied
by a guitar.</p></td>
</tr>
<tr>
<td><p><samp>aerobics</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>55</samp></p></td>
<td data-sort-value="55"><p><samp>00000037</samp></p></td>
<td><p><em>Aerobics Class</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a> only)</p></td>
<td><p>Dance aerobics music that abruptly cuts off. Used in <a
href="Harvey#Six_Hearts" class="wikilink"
title="Harvey&#39;s 6-heart event">Harvey's 6-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>archaeo</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>0</samp></p></td>
<td data-sort-value="0"><p><samp>00000000</samp></p></td>
<td></td>
<td><p>An upbeat banjo tune with heavy bass and a higher-pitched
electric melody. Appears unused.</p></td>
</tr>
<tr>
<td><p><samp>bigDrums</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>172</samp></p></td>
<td data-sort-value="172"><p><samp>000000ac</samp></p></td>
<td></td>
<td><p>Mysterious tambourine, bass drum, and bongos. Used in <a
href="Sebastian#Six_Hearts" class="wikilink"
title="Sebastian&#39;s 6-heart event">Sebastian's 6-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>breezy</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>281</samp></p></td>
<td data-sort-value="281"><p><samp>00000119</samp></p></td>
<td><p><em>Land of Green and Gold</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Land of Green and Gold (Leah's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A happy marimba and harmonica tune in 3.</p></td>
</tr>
<tr>
<td><p><samp>caldera</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>383</samp></p></td>
<td data-sort-value="383"><p><samp>0000017f</samp></p></td>
<td><p><em>Mystery of the Caldera</em></p></td>
<td><p>A mysterious synth track backed by lava bubbling.</p></td>
</tr>
<tr>
<td><p><samp>Cavern</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>65</samp></p></td>
<td data-sort-value="65"><p><samp>00000041</samp></p></td>
<td><p><em>Mines (a Flicker in the Deep)</em></p></td>
<td><p>A soft electric piano track. Plays in <a href="The_Mines"
class="wikilink" title="The Mines">The Mines</a> in levels
1-39.</p></td>
</tr>
<tr>
<td><p><samp>christmasTheme</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>305</samp></p></td>
<td data-sort-value="305"><p><samp>00000131</samp></p></td>
<td><p><em>Winter Festival</em></p></td>
<td><p>A joyful holiday tune with jingling bells. Background music for
the <a href="Feast_of_the_Winter_Star" class="wikilink"
title="Feast of the Winter Star">Feast of the Winter Star</a>.</p></td>
</tr>
<tr>
<td><p><samp>Cloth</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>67</samp></p></td>
<td data-sort-value="67"><p><samp>00000043</samp></p></td>
<td><p><em>Mines (Cloth)</em></p></td>
<td><p>Wistful piano chords with synths in a minor key. Plays in <a
href="The_Mines" class="wikilink" title="The Mines">The Mines</a> in
levels 40-79.</p></td>
</tr>
<tr>
<td><p><samp>CloudCountry</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>190</samp></p></td>
<td data-sort-value="190"><p><samp>000000be</samp></p></td>
<td><p><em>Cloud Country</em></p></td>
<td><p>A happy banjo tune with flute. Used in the character creation
menus.</p></td>
</tr>
<tr>
<td><p><samp>clubloop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>102</samp></p></td>
<td data-sort-value="102"><p><samp>00000066</samp></p></td>
<td></td>
<td><p>Quiet ambient hum interrupted by the occasional sci-fi esque
sound. Background ambiance for the <a href="Casino" class="wikilink"
title="Casino">Casino</a> and <a href="Qi&#39;s_Walnut_Room"
class="wikilink" title="Qi&#39;s Walnut Room">Qi's Walnut
Room</a>.</p></td>
</tr>
<tr>
<td><p><samp>cowboy_boss</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>267</samp></p></td>
<td data-sort-value="267"><p><samp>0000010b</samp></p></td>
<td><p><em>Journey Of The Prairie King (Boss)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Journey of the Prairie King (Final Boss &amp; Ending)</em> (<a
href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A fast and bass-heavy 8-bit boss fight soundtrack. Used as
background music when the player fights <a
href="Journey_of_the_Prairie_King#Bosses" class="wikilink"
title="Fector">Fector</a> in Journey of the Prairie King.</p></td>
</tr>
<tr>
<td><p><samp>cowboy_outlawsong</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>277</samp></p></td>
<td data-sort-value="277"><p><samp>00000115</samp></p></td>
<td><p><em>Journey Of The Prairie King (Outlaw)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Journey of the Prairie King (The Outlaw)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>An 8-bit "wild west"-themed track with whistling. Plays when the
<a href="Journey_of_the_Prairie_King#Bosses" class="wikilink"
title="Cowboy boss">Cowboy boss</a> spawns in Journey of the Prairie
King.</p></td>
</tr>
<tr>
<td><p><samp>Cowboy_OVERWORLD</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>261</samp></p></td>
<td data-sort-value="261"><p><samp>00000105</samp></p></td>
<td><p><em>Journey of the Prairie King (Overworld)</em></p></td>
<td><p>A medium-tempo 8-bit game theme. Used as the default theme for <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>Cowboy_singing</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>262</samp></p></td>
<td data-sort-value="262"><p><samp>00000106</samp></p></td>
<td><p><em>Journey Of The Prairie King (Ending)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Journey of the Prairie King (Final Boss &amp; Ending)</em> (<a
href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A slower 8-bit track with a higher-pitched melody on top of the
bass. Plays when the player completes <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>Cowboy_undead</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>270</samp></p></td>
<td data-sort-value="270"><p><samp>0000010e</samp></p></td>
<td><p><em>Journey Of The Prairie King (Undead)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a> only)</p></td>
<td><p>A short and fast 8-bit game track in a minor key. Plays when the
player picks up a <a
href="Journey_of_the_Prairie_King#Items_Dropped_by_Enemies"
class="wikilink" title="tombstone">tombstone</a> power-up in <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>crane_game</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>12</samp></p></td>
<td data-sort-value="12"><p><samp>0000000c</samp></p></td>
<td><p><em>Crane Game</em></p></td>
<td><p>A slow jazz string bass solo. Used in the <a
href="Movie_Theater#Crane_Game" class="wikilink"
title="Crane Game">Crane Game</a>.</p></td>
</tr>
<tr>
<td><p><samp>crane_game_fast</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>13</samp></p></td>
<td data-sort-value="13"><p><samp>0000000d</samp></p></td>
<td><p><em>Crane Game (It's A Catch!)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Crane Game</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>An upbeat version of <samp>crane_game</samp> that includes piano.
Used in the <a href="Movie_Theater#Crane_Game" class="wikilink"
title="Crane Game">Crane Game</a>.</p></td>
</tr>
<tr>
<td><p><samp>Crystal Bells</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>64</samp></p></td>
<td data-sort-value="64"><p><samp>00000040</samp></p></td>
<td><p><em>Mines (Crystal Bells)</em></p></td>
<td><p>A slow piano melody with electric bass and synths. Plays in <a
href="The_Mines" class="wikilink" title="The Mines">The Mines</a> in
levels 1-39.</p></td>
</tr>
<tr>
<td><p><samp>Cyclops</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>124</samp></p></td>
<td data-sort-value="124"><p><samp>0000007c</samp></p></td>
<td></td>
<td><p>Seems to match <samp>winter2</samp>.</p></td>
</tr>
<tr>
<td><p><samp>desolate</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>40</samp></p></td>
<td data-sort-value="40"><p><samp>00000028</samp></p></td>
<td><p><em>A Sad Story</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>A Sad Song (Alex's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A sad mallet percussion tune.</p></td>
</tr>
<tr>
<td><p><samp>distantBanjo</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>347</samp></p></td>
<td data-sort-value="347"><p><samp>0000015b</samp></p></td>
<td><p><em>Distant Banjo</em></p></td>
<td><p>A happy harmonica and banjo tune.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>EarthMine</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>64</samp></p></td>
<td data-sort-value="64"><p><samp>00000040</samp></p></td>
<td rowspan="3"></td>
<td rowspan="3"><p>Plays one of either <samp>Crystal Bells</samp>,
<samp>Cavern</samp>, or <samp>Secret Gnomes</samp>.</p></td>
</tr>
<tr>
<td><p><samp>65</samp></p></td>
<td data-sort-value="65"><p><samp>00000041</samp></p></td>
</tr>
<tr>
<td><p><samp>66</samp></p></td>
<td data-sort-value="66"><p><samp>00000042</samp></p></td>
</tr>
<tr>
<td><p><samp>echos</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>49</samp></p></td>
<td data-sort-value="49"><p><samp>00000031</samp></p></td>
<td><p><em>Echos</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Echos (Sebastian's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A pensive and slow xylophone solo.</p></td>
</tr>
<tr>
<td><p><samp>elliottPiano</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>295</samp></p></td>
<td data-sort-value="295"><p><samp>00000127</samp></p></td>
<td><p><em>Piano Solo</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Piano Solo (Elliott's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A slow, short, and simple piano solo.</p></td>
</tr>
<tr>
<td><p><samp>EmilyDance</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>357</samp></p></td>
<td data-sort-value="357"><p><samp>00000165</samp></p></td>
<td><p><em>Emily's Dance</em></p></td>
<td><p>A cassette tape being put into a player and then upbeat dance
music with a strong beat and flute/piano melody. Used in <a
href="Emily#Six_Hearts" class="wikilink"
title="Emily&#39;s 6-heart event">Emily's 6-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>EmilyDream</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>358</samp></p></td>
<td data-sort-value="358"><p><samp>00000166</samp></p></td>
<td><p><em>Dreamscape</em></p></td>
<td><p>Ambiance of the wind blowing, a stringed instrument playing, and
"ooo"s. Includes lots of pitch bending. Used in <a
href="Emily#Two_Hearts" class="wikilink"
title="Emily&#39;s 2-heart event">Emily's 2-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>EmilyTheme</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>359</samp></p></td>
<td data-sort-value="359"><p><samp>00000167</samp></p></td>
<td><p><em>Song Of Feathers</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Song of Feathers (Emily's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A medium-tempo happy synth track with a xylophone feature. Used
in several of <a href="Emily" class="wikilink" title="Emily">Emily</a>'s
heart events.</p></td>
</tr>
<tr>
<td><p><samp>end_credits</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>403</samp></p></td>
<td data-sort-value="403"><p><samp>00000193</samp></p></td>
<td><p><em>Stardew Valley Forever</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Summit Celebration</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A happy track with bass and synth melodies. Plays during the <a
href="The_Summit#Cutscene" class="wikilink" title="Summit event">Summit
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>event1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>299</samp></p></td>
<td data-sort-value="299"><p><samp>0000012b</samp></p></td>
<td><p><em>Fun Festival</em></p></td>
<td><p>An upbeat banjo, piano, and bass track. Plays in several
cutscenes, such as the judging at the <a href="Egg_Festival"
class="wikilink" title="Egg Festival">Egg Festival</a>.</p></td>
</tr>
<tr>
<td><p><samp>event2</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>302</samp></p></td>
<td data-sort-value="302"><p><samp>0000012e</samp></p></td>
<td><p><em>Luau Festival</em></p></td>
<td><p>An upbeat yet mysterious xylophone and flute melody. Used during
the <a href="Luau" class="wikilink" title="Luau">Luau</a>.</p></td>
</tr>
<tr>
<td><p><samp>fall1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>121</samp></p></td>
<td data-sort-value="121"><p><samp>00000079</samp></p></td>
<td><p><em>Fall (The Smell of Mushroom)</em></p></td>
<td><p>A soft trumpet, clarinet, harp, and xylophone track. Plays in
various outdoor locations in fall.</p></td>
</tr>
<tr>
<td><p><samp>fall2</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>119</samp></p></td>
<td data-sort-value="119"><p><samp>00000077</samp></p></td>
<td><p><em>Fall (Ghost Synth)</em></p></td>
<td><p>A soft synth and bass track with light drums. Plays in various
outdoor locations in fall.</p></td>
</tr>
<tr>
<td><p><samp>fall3</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>120</samp></p></td>
<td data-sort-value="120"><p><samp>00000078</samp></p></td>
<td><p><em>Fall (Raven's Descent)</em></p></td>
<td><p>A soft flute and xylophone track. Plays in various outdoor
locations in fall.</p></td>
</tr>
<tr>
<td><p><samp>fallFest</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>304</samp></p></td>
<td data-sort-value="304"><p><samp>00000130</samp></p></td>
<td><p><em>Stardew Valley Fair Theme</em></p></td>
<td><p>A medium-tempo banjo and clarinet duet. Used in various
festivals, including the <a href="Stardew_Valley_Fair" class="wikilink"
title="Stardew Valley Fair">Stardew Valley Fair</a>.</p></td>
</tr>
<tr>
<td><p><samp>fieldofficeTentMusic</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>375</samp></p></td>
<td data-sort-value="375"><p><samp>00000177</samp></p></td>
<td><p><em>Professor Snail's Radio</em></p></td>
<td><p>A laid-back electric guitar track with light percussion and some
xylophone fills. Plays in the <a href="Island_Field_Office"
class="wikilink" title="Island Field Office">Island Field
Office</a>.</p></td>
</tr>
<tr>
<td><p><samp>FlowerDance</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>301</samp></p></td>
<td data-sort-value="301"><p><samp>0000012d</samp></p></td>
<td><p><em>Flower Dance</em></p></td>
<td><p>A waltz featuring lots of string pizzicato, flute, and bells.
Plays during the dance scene in the <a href="Flower_Dance"
class="wikilink" title="Flower Dance">Flower Dance</a>.</p></td>
</tr>
<tr>
<td><p><samp>FrogCave</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>387</samp></p></td>
<td data-sort-value="387"><p><samp>00000183</samp></p></td>
<td><p><em>The Gourmand's Cave</em></p></td>
<td><p>A medium-tempo percussive track with drums, clave, and the
occasional frog croak. Plays in <a href="Ginger_Island#Gourmand_Frog"
class="wikilink" title="Gourmand&#39;s Cave">Gourmand's
Cave</a>.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>FrostMine</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>67</samp></p></td>
<td data-sort-value="67"><p><samp>00000043</samp></p></td>
<td rowspan="3"></td>
<td rowspan="3"><p>Plays one of either <samp>Cloth</samp>,
<samp>Icicles</samp>, or <samp>XOR</samp>.</p></td>
</tr>
<tr>
<td><p><samp>68</samp></p></td>
<td data-sort-value="68"><p><samp>00000044</samp></p></td>
</tr>
<tr>
<td><p><samp>69</samp></p></td>
<td data-sort-value="69"><p><samp>00000045</samp></p></td>
</tr>
<tr>
<td><p><samp>Ghost Synth</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>119</samp></p></td>
<td data-sort-value="119"><p><samp>00000077</samp></p></td>
<td></td>
<td><p>Alias for <samp>fall2</samp> that is unused by Vanilla.</p></td>
</tr>
<tr>
<td><p><samp>grandpas_theme</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>336</samp></p></td>
<td data-sort-value="336"><p><samp>00000150</samp></p></td>
<td><p><em>Grandpa's Theme</em></p></td>
<td><p>A soft music box lullaby. Plays in the intro cutscene.</p></td>
</tr>
<tr>
<td><p><samp>gusviolin</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>297</samp></p></td>
<td data-sort-value="297"><p><samp>00000129</samp></p></td>
<td><p><em>Violin Solo</em></p></td>
<td><p>A short, sentimental violin solo. Plays in <a
href="Alex#Ten_Hearts" class="wikilink"
title="Alex&#39;s 10-heart event">Alex's 10-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>harveys_theme_jazz</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>4</samp></p></td>
<td data-sort-value="4"><p><samp>00000004</samp></p></td>
<td><p><em>Grapefruit Sky (Pasta Primavera Mix)</em></p></td>
<td><p>A medium-tempo swing track with piano, drums, and mallet
percussion. Used in <a href="Harvey#Fourteen_Hearts" class="wikilink"
title="Harvey&#39;s 14-heart event">Harvey's 14-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>heavy</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>51</samp></p></td>
<td data-sort-value="51"><p><samp>00000033</samp></p></td>
<td><p><em>Sam's Band (heavy)</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Sam's Band (Heavy Version)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>Loud drums and bass. Used by <a href="Sam#Eight_Hearts"
class="wikilink" title="Sam&#39;s 8-heart event">Sam's 8-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>honkytonky</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>52</samp></p></td>
<td data-sort-value="52"><p><samp>00000034</samp></p></td>
<td><p><em>Sam's Band (Bluegrass)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>)<br />
<em>Sam's Band (Bluegrass Version)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>An uptempo fiddle and banjo tune. Used by <a
href="Sam#Eight_Hearts" class="wikilink"
title="Sam&#39;s 8-heart event">Sam's 8-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>Icicles</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>68</samp></p></td>
<td data-sort-value="68"><p><samp>00000044</samp></p></td>
<td><p><em>Mines (Icicles)</em></p></td>
<td><p>A slower track with synths and some drums. Plays in <a
href="The_Mines" class="wikilink" title="The Mines">The Mines</a> in
levels 40-79.</p></td>
</tr>
<tr>
<td><p><samp>IslandMusic</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>374</samp></p></td>
<td data-sort-value="374"><p><samp>00000176</samp></p></td>
<td><p><em>Ginger Island</em></p></td>
<td><p>A tropical tune featuring steel drums, castanets, güiro, and
flute. Plays on <a href="Ginger_Island" class="wikilink"
title="Ginger Island">Ginger Island</a>.</p></td>
</tr>
<tr>
<td><p><samp>jaunty</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>41</samp></p></td>
<td data-sort-value="41"><p><samp>00000029</samp></p></td>
<td><p><em>Jaunty</em></p></td>
<td><p>A happy flute and harpsichord duet in 3. Used in various heart
events.</p></td>
</tr>
<tr>
<td><p><samp>junimoKart</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>20</samp></p></td>
<td data-sort-value="20"><p><samp>00000014</samp></p></td>
<td><p><em>Junimo Kart (Title Theme)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>JunimoKart (Title Theme)</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>An upbeat synth track. Plays in the title menus of <a
href="Junimo_Kart" class="wikilink" title="Junimo Kart">Junimo
Kart</a>.</p></td>
</tr>
<tr>
<td><p><samp>junimoKart_ghostMusic</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>0</samp></p></td>
<td data-sort-value="0"><p><samp>00000000</samp></p></td>
<td><p><em>Junimo Kart (Ghastly Galleon)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>JunimoKart (Ghastly Galleon)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A slow, spooky track with ghostly "ooo"s. Plays in the <a
href="Junimo_Kart#Ghastly_Galleon" class="wikilink"
title="Ghastly Galleon">Ghastly Galleon</a> levels of
JunimoKart.</p></td>
</tr>
<tr>
<td><p><samp>junimoKart_mushroomMusic</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>21</samp></p></td>
<td data-sort-value="21"><p><samp>00000015</samp></p></td>
<td><p><em>Junimo Kart (Glowshroom Grotto)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>JunimoKart (Glowshroom Grotto)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A slower synth track with a hi-hat beat. Plays in the <a
href="Junimo_Kart#Glowshroom_Grotto" class="wikilink"
title="Glowshroom Grotto">Glowshroom Grotto</a> levels of
JunimoKart.</p></td>
</tr>
<tr>
<td><p><samp>junimoKart_slimeMusic</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>22</samp></p></td>
<td data-sort-value="22"><p><samp>00000016</samp></p></td>
<td><p><em>Junimo Kart (Slomp's Stomp)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>);<br />
<em>JunimoKart (Slomp's Stomp)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>An uptempo track in harmonic minor featuring oboe, a stringed
instrument, güiro, and the occasional slime splat noise. Plays in the <a
href="Junimo_Kart#Slomp&#39;s_Stomp" class="wikilink"
title="Slomp&#39;s Stomp">Slomp's Stomp</a> levels of
JunimoKart.</p></td>
</tr>
<tr>
<td><p><samp>junimoKart_whaleMusic</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>1</samp></p></td>
<td data-sort-value="1"><p><samp>00000001</samp></p></td>
<td><p><em>Junimo Kart (The Gem Sea Giant)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>JunimoKart (The Gem Sea Giant)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A slow, mystical synth track with some pitch bending. Plays in
the <a href="Junimo_Kart#The_Gem_Sea_Giant" class="wikilink"
title="Gem Sea Giant">Gem Sea Giant</a> levels of JunimoKart.</p></td>
</tr>
<tr>
<td><p><samp>junimoStarSong</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>308</samp></p></td>
<td data-sort-value="308"><p><samp>00000134</samp></p></td>
<td><p><em>A Golden Star Is Born</em></p></td>
<td><p>A hopeful synth track. Plays in the <a href="Community_Center"
class="wikilink" title="Community Center">Community Center</a> after
various completion milestones.</p></td>
</tr>
<tr>
<td><p><samp>kindadumbautumn</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>282</samp></p></td>
<td data-sort-value="282"><p><samp>0000011a</samp></p></td>
<td><p><em>Grapefruit Sky</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Grapefruit Sky (Dr. Harvey's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A peaceful guitar and flute duet. Used in several of <a
href="Harvey" class="wikilink" title="Harvey">Harvey</a> and <a
href="Maru" class="wikilink" title="Maru">Maru</a>'s heart
events.</p></td>
</tr>
<tr>
<td rowspan="4"><p><samp>LavaMine</samp></p></td>
<td rowspan="4"><p><samp>Wavebank</samp></p></td>
<td><p><samp>72</samp></p></td>
<td data-sort-value="72"><p><samp>00000048</samp></p></td>
<td rowspan="4"></td>
<td rowspan="4"><p>Plays one of either <samp>Of Dwarves</samp>,
<samp>Near The Planet Core</samp>, <samp>Overcast</samp>, or
<samp>tribal</samp>.</p></td>
</tr>
<tr>
<td><p><samp>73</samp></p></td>
<td data-sort-value="73"><p><samp>00000049</samp></p></td>
</tr>
<tr>
<td><p><samp>198</samp></p></td>
<td data-sort-value="198"><p><samp>000000c6</samp></p></td>
</tr>
<tr>
<td><p><samp>215</samp></p></td>
<td data-sort-value="215"><p><samp>000000d7</samp></p></td>
</tr>
<tr>
<td><p><samp>libraryTheme</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>341</samp></p></td>
<td data-sort-value="341"><p><samp>00000155</samp></p></td>
<td><p><em>Library and Museum</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>The Library and Museum</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A cheerful banjo and flute duet. Plays as background music in the
<a href="Museum" class="wikilink" title="Museum">Museum</a>.</p></td>
</tr>
<tr>
<td><p><samp>MainTheme</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>335</samp></p></td>
<td data-sort-value="335"><p><samp>0000014f</samp></p></td>
<td><p><em>Stardew Valley Overture</em></p></td>
<td><p>A peaceful guitar and flute theme. Plays in the title menus for
the game.</p></td>
</tr>
<tr>
<td><p><samp>Majestic</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>121</samp></p></td>
<td data-sort-value="121"><p><samp>00000079</samp></p></td>
<td></td>
<td><p>Alias for <samp>fall1</samp> that is unused by Vanilla.</p></td>
</tr>
<tr>
<td><p><samp>MarlonsTheme</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>349</samp></p></td>
<td data-sort-value="349"><p><samp>0000015d</samp></p></td>
<td><p><em>Marlon's Theme</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>The Adventure Guild</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A banjo melody accompanied by flute and string bass. Used as
background music for the <a href="Adventurer&#39;s_Guild"
class="wikilink" title="Adventurer&#39;s Guild">Adventurer's
Guild</a>.</p></td>
</tr>
<tr>
<td><p><samp>marnieShop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>180</samp></p></td>
<td data-sort-value="180"><p><samp>000000b4</samp></p></td>
<td><p><em>Country Shop</em></p></td>
<td><p>A happy banjo, violin, and flute melody accompanied by
tambourine. Plays at <a href="Marnie&#39;s_Ranch" class="wikilink"
title="Marnie&#39;s Ranch">Marnie's Ranch</a> and the <a
href="Carpenter&#39;s_Shop" class="wikilink"
title="Carpenter&#39;s Shop">Carpenter's Shop</a>.</p></td>
</tr>
<tr>
<td><p><samp>mermaidSong</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>362</samp></p></td>
<td data-sort-value="362"><p><samp>0000016a</samp></p></td>
<td><p><em>Mermaid</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Mermaid Song</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A slow, mystical synth track with vocals over top. Plays during
the Night Market's <a href="Night_Market#Mermaid_Boat" class="wikilink"
title="mermaid show">mermaid show</a>.</p></td>
</tr>
<tr>
<td><p><samp>moonlightJellies</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>303</samp></p></td>
<td data-sort-value="303"><p><samp>0000012f</samp></p></td>
<td><p><em>Dance of the Moonlight Jellies</em></p></td>
<td><p>A peaceful synth track with the sound of ocean waves in the
background. Plays during the <a href="Dance_of_the_Moonlight_Jellies"
class="wikilink" title="Dance of the Moonlight Jellies">Dance of the
Moonlight Jellies</a>.</p></td>
</tr>
<tr>
<td><p><samp>movie_classic</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>7</samp></p></td>
<td data-sort-value="7"><p><samp>00000007</samp></p></td>
<td><p><em>The Zuzu City Express Theme</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>The Zuzu City Express (Movie Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A peaceful string ballad with quiet mallet percussion. Used in <a
href="Movie_Theater#Movies" class="wikilink"
title="The Zuzu City Express">The Zuzu City Express</a> movie.</p></td>
</tr>
<tr>
<td><p><samp>movie_nature</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>8</samp></p></td>
<td data-sort-value="8"><p><samp>00000008</samp></p></td>
<td><p>Exploring Our Vibrant World<em>(<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
</em>Exploring Our Vibrant World (Movie Theme)''</p></td>
<td><p>A mysterious track with string, marimba, and slow drums. A flute
melody enters midway. Used in the <a href="Movie_Theater#Movies"
class="wikilink"
title="Natural Wonders: Exploring Our Vibrant World">Natural Wonders:
Exploring Our Vibrant World</a> movie.</p></td>
</tr>
<tr>
<td><p><samp>movie_wumbus</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>9</samp></p></td>
<td data-sort-value="9"><p><samp>00000009</samp></p></td>
<td><p><em>Wumbus' Theme</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Wumbus (Movie Theme)</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A midtempo electric piano track with prominent percussion
features. Used the in the <a href="Movie_Theater#Movies"
class="wikilink" title="Wumbus">Wumbus</a> movie.</p></td>
</tr>
<tr>
<td><p><samp>movieTheater</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>10</samp></p></td>
<td data-sort-value="10"><p><samp>0000000a</samp></p></td>
<td><p><em>Movie Theater</em></p></td>
<td><p>An uptempo swing track with electric piano, vibraphone, and
drums. Default music in the <a href="Movie_Theater" class="wikilink"
title="Movie Theater">Movie Theater</a>.</p></td>
</tr>
<tr>
<td><p><samp>movieTheaterAfter</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>11</samp></p></td>
<td data-sort-value="11"><p><samp>0000000b</samp></p></td>
<td><p><em>Movie Theater (Closing Time)</em></p></td>
<td><p>A slower rendititon of <samp>movieTheater</samp> with piano and
clarinet. Plays after a movie ends at the <a href="Movie_Theater"
class="wikilink" title="Movie Theater">Movie Theater</a>.</p></td>
</tr>
<tr>
<td><p><samp>musicboxsong</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>44</samp></p></td>
<td data-sort-value="44"><p><samp>0000002c</samp></p></td>
<td><p><em>Music Box Song</em></p></td>
<td><p>A slow music box and synth melody. Plays in various cutscenes,
such as the <a href="Community_Center#Restoring_the_Community_Center"
class="wikilink" title="Community Center Reopening Ceremony">Community
Center Reopening Ceremony</a> (Pierre's memories).</p></td>
</tr>
<tr>
<td><p><samp>Near The Planet Core</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>72</samp></p></td>
<td data-sort-value="72"><p><samp>00000048</samp></p></td>
<td><p><em>Mines (a Visitor to the Unknown)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Mines (Visitor to the Unknown)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>An uptempo synth, bass, flute, and glockenspiel track with the
occasional wind gust. Plays in <a href="The_Mines" class="wikilink"
title="The Mines">The Mines</a> in levels 80-120.</p></td>
</tr>
<tr>
<td><p><samp>New Snow</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>126</samp></p></td>
<td data-sort-value="126"><p><samp>0000007e</samp></p></td>
<td></td>
<td><p>Alias for <samp>winter1</samp> that is unused by
Vanilla.</p></td>
</tr>
<tr>
<td><p><samp>night_market</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>364</samp></p></td>
<td data-sort-value="364"><p><samp>0000016c</samp></p></td>
<td><p><em>Night Market</em></p></td>
<td><p>A slow track with mallet percussion, strings, flute, and the
sound of ocean waves. Plays during the <a href="Night_Market"
class="wikilink" title="Night Market">Night Market</a>.</p></td>
</tr>
<tr>
<td><p><samp>Of Dwarves</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>73</samp></p></td>
<td data-sort-value="73"><p><samp>00000049</samp></p></td>
<td><p><em>Mines (The Lava Dwellers)</em></p></td>
<td><p>A miidtempo track with synths, lots of hi-hat, and whooshing
sounds. Plays in <a href="The_Mines" class="wikilink"
title="The Mines">The Mines</a> in levels 80-120.</p></td>
</tr>
<tr>
<td><p><samp>Orange</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>122</samp></p></td>
<td data-sort-value="122"><p><samp>0000007a</samp></p></td>
<td></td>
<td><p>Alias for <samp>summer1</samp> that is unused by
Vanilla.</p></td>
</tr>
<tr>
<td><p><samp>Overcast</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>215</samp></p></td>
<td data-sort-value="215"><p><samp>000000d7</samp></p></td>
<td><p><em>Mines (Magical Shoes)</em></p></td>
<td><p>A mysterious synth track backed by drums. Plays in <a
href="The_Mines" class="wikilink" title="The Mines">The Mines</a> in
levels 80-120.</p></td>
</tr>
<tr>
<td><p><samp>Pink Petals</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>93</samp></p></td>
<td data-sort-value="93"><p><samp>0000005d</samp></p></td>
<td></td>
<td><p>Alias for <samp>spring1</samp> that is unused by
Vanilla.</p></td>
</tr>
<tr>
<td><p><samp>PIRATE_THEME</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>390</samp></p></td>
<td data-sort-value="390"><p><samp>00000186</samp></p></td>
<td><p><em>Pirate Theme</em></p></td>
<td><p>A bouncy shanty in a minor key. Plays in Ginger Island's <a
href="Ginger_Island#Pirate_Cove" class="wikilink"
title="Pirate Cove">Pirate Cove</a> when Pirates are visiting.</p></td>
</tr>
<tr>
<td><p><samp>PIRATE_THEME(muffled)</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>390</samp></p></td>
<td data-sort-value="390"><p><samp>00000186</samp></p></td>
<td><p><em>Pirate Theme (Muffled)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a> only)</p></td>
<td><p>A muffled version of <samp>PIRATE_THEME</samp>. Plays in <a
href="Ginger_Island#Island_Southeast" class="wikilink"
title="Ginger Island Southeast">Ginger Island Southeast</a> when Pirates
are visiting.</p></td>
</tr>
<tr>
<td><p><samp>playful</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>278</samp></p></td>
<td data-sort-value="278"><p><samp>00000116</samp></p></td>
<td><p><em>Playful</em></p></td>
<td><p>A happy clarinet and xylophone duet with background strings. Used
in various heart events.</p></td>
</tr>
<tr>
<td><p><samp>Plums</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>120</samp></p></td>
<td data-sort-value="120"><p><samp>00000078</samp></p></td>
<td></td>
<td><p>Alias for <samp>fall3</samp> that is unused by Vanilla.</p></td>
</tr>
<tr>
<td><p><samp>poppy</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>53</samp></p></td>
<td data-sort-value="53"><p><samp>00000035</samp></p></td>
<td><p><em>Sam's Band (poppy)</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Sam's Band (Pop Version)</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td><p>A happy pop song with strong electric guitar, bass, and claps.
Used by <a href="Sam#Eight_Hearts" class="wikilink"
title="Sam&#39;s 8-heart event">Sam's 8-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>raccoonSong</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>436</samp></p></td>
<td data-sort-value="436"><p><samp>000001b4</samp></p></td>
<td><p><em>Raccoon Song</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a> only)</p></td>
<td><p>An eclectic track with a melody full of chirping. Plays after the
player completes all of the requests for the <a href="Giant_Stump"
class="wikilink" title="Raccoon">Raccoon</a>.</p></td>
</tr>
<tr>
<td><p><samp>ragtime</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>46</samp></p></td>
<td data-sort-value="46"><p><samp>0000002e</samp></p></td>
<td><p><em>Pickle Jar Rag</em> (<a href="Jukebox" class="wikilink"
title="Jukebox">Jukebox</a>);<br />
<em>Pickle Jar Rag (Haley's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A piano ragtime track. Used in various heart events such as <a
href="Haley#Four_Hearts" class="wikilink"
title="Haley&#39;s 4-heart event">Haley's 4-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>sad_kid</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>389</samp></p></td>
<td data-sort-value="389"><p><samp>00000185</samp></p></td>
<td><p><em>Leo's Song</em></p></td>
<td><p>A pensieve flute and marimba duet. Plays in various heart events
involving <a href="Leo" class="wikilink" title="Leo">Leo</a>.</p></td>
</tr>
<tr>
<td><p><samp>sadpiano</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>47</samp></p></td>
<td data-sort-value="47"><p><samp>0000002f</samp></p></td>
<td><p><em>A Dark Corner of the Past</em></p></td>
<td><p>A wistful piano solo. Used in various heart events.</p></td>
</tr>
<tr>
<td><p><samp>Saloon1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>350</samp></p></td>
<td data-sort-value="350"><p><samp>0000015e</samp></p></td>
<td><p><em>The Stardrop Saloon</em></p></td>
<td><p>An old-timey ragtime piano solo with the occasional sound of
clinking plates and glasses. Plays in the <a href="Saloon"
class="wikilink" title="Saloon">Saloon</a>.</p></td>
</tr>
<tr>
<td><p><samp>sam_acoustic1</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>2</samp></p></td>
<td data-sort-value="2"><p><samp>00000002</samp></p></td>
<td><p><em>The Happy Junimo Show Theme</em></p></td>
<td><p>A harmonica song with guitar and tambourine accompaniment. Ends
with a guitar solo. Used by <a href="Sam#Fourteen_Hearts"
class="wikilink" title="Sam&#39;s 14-heart event">Sam's 14-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>sam_acoustic2</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>3</samp></p></td>
<td data-sort-value="3"><p><samp>00000003</samp></p></td>
<td><p><em>Sam's Acoustic Noodling</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a> only)</p></td>
<td><p>A short acoustic guitar rendition of <samp>sam_acoustic1</samp>.
Used by <a href="Sam#Fourteen_Hearts" class="wikilink"
title="Sam&#39;s 14-heart event">Sam's 14-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>sampractice</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>50</samp></p></td>
<td data-sort-value="50"><p><samp>00000032</samp></p></td>
<td><p><em>Band Practice</em></p></td>
<td><p>A short clip of an electric guitar practicing over a loop of
drums and claps. Used by <a href="Sam#Two_Hearts" class="wikilink"
title="Sam&#39;s 2-heart event">Sam's 2-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>sappypiano</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>43</samp></p></td>
<td data-sort-value="43"><p><samp>0000002b</samp></p></td>
<td></td>
<td><p>A midtempo track featuring sparkling harp notes, synths, flute,
and drums. It is unknown why the track is titled this way. Unused by
Vanilla.</p></td>
</tr>
<tr>
<td><p><samp>Secret Gnomes</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>66</samp></p></td>
<td data-sort-value="66"><p><samp>00000042</samp></p></td>
<td><p><em>Mines (Star Lumpy)</em></p></td>
<td><p>A mysterious mallet percussion track. Plays in <a
href="The_Mines" class="wikilink" title="The Mines">The Mines</a> in
levels 1-39.</p></td>
</tr>
<tr>
<td><p><samp>SettlingIn</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>192</samp></p></td>
<td data-sort-value="192"><p><samp>000000c0</samp></p></td>
<td><p><em>Settling In</em></p></td>
<td><p>A happy banjo and flute duet with bass. Plays in the event where
the player meets <a href="Robin" class="wikilink"
title="Robin">Robin</a> and <a href="Lewis" class="wikilink"
title="Lewis">Lewis</a> after just moving in.</p></td>
</tr>
<tr>
<td><p><samp>shaneTheme</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>361</samp></p></td>
<td data-sort-value="361"><p><samp>00000169</samp></p></td>
<td><p><em>Shane's Theme</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Frozen Pizza and Eggs (Shane's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A sad xylophone and electric guitar track. Used in various
cutscenes such as <a href="Shane#Four_Hearts" class="wikilink"
title="Shane&#39;s 4-heart event">Shane's 4-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>shimmeringbastion</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>54</samp></p></td>
<td data-sort-value="54"><p><samp>00000036</samp></p></td>
<td><p><em>Sam's Band (Electronic)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Sam's Band (Electronic Version)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>An upbeat synth track with drums. Used by <a
href="Sam#Eight_Hearts" class="wikilink"
title="Sam&#39;s 8-heart event">Sam's 8-heart event</a>.</p></td>
</tr>
<tr>
<td><p><samp>spaceMusic</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>285</samp></p></td>
<td data-sort-value="285"><p><samp>0000011d</samp></p></td>
<td><p><em>Starwatcher</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Starwatcher (Maru's Theme)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td><p>A slow, peaceful synth melody over crickets chirping. Used in
various cutscenes such as <a href="Maru#Fourteen_Hearts"
class="wikilink" title="Maru&#39;s 14-heart event">Maru's 14-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>spirits_eve</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>334</samp></p></td>
<td data-sort-value="334"><p><samp>0000014e</samp></p></td>
<td><p><em>Spirit's Eve Festival</em></p></td>
<td><p>A spooky theme. Plays during <a href="Spirit&#39;s_Eve"
class="wikilink" title="Spirit&#39;s Eve">Spirit's Eve</a>.</p></td>
</tr>
<tr>
<td><p><samp>spring1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>93</samp></p></td>
<td data-sort-value="93"><p><samp>0000005d</samp></p></td>
<td><p><em>Spring (It's a Big World Outside)</em></p></td>
<td><p>A hopeful track featuring strings, clarinet, and flute. Plays in
various outdoor locations in spring.</p></td>
</tr>
<tr>
<td><p><samp>spring2</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>91</samp></p></td>
<td data-sort-value="91"><p><samp>0000005b</samp></p></td>
<td><p><em>Spring (The Valley Comes Alive)</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>spring3</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>92</samp></p></td>
<td data-sort-value="92"><p><samp>0000005c</samp></p></td>
<td><p><em>Spring (Wild Horseradish Jam)</em></p></td>
<td></td>
</tr>
<tr>
<td rowspan="3"><p><samp>springsongs</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>91</samp></p></td>
<td data-sort-value="91"><p><samp>0000005b</samp></p></td>
<td rowspan="3"></td>
<td rowspan="3"></td>
</tr>
<tr>
<td><p><samp>92</samp></p></td>
<td data-sort-value="92"><p><samp>0000005c</samp></p></td>
</tr>
<tr>
<td><p><samp>93</samp></p></td>
<td data-sort-value="93"><p><samp>0000005d</samp></p></td>
</tr>
<tr>
<td><p><samp>springtown</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>94</samp></p></td>
<td data-sort-value="94"><p><samp>0000005e</samp></p></td>
<td><p><em>Pelican Town</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>Stadium_ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>356</samp></p></td>
<td data-sort-value="356"><p><samp>00000164</samp></p></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>starshoot</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>42</samp></p></td>
<td data-sort-value="42"><p><samp>0000002a</samp></p></td>
<td><p><em>Starshoot</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a> only)</p></td>
<td></td>
</tr>
<tr>
<td><p><samp>submarine_song</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>366</samp></p></td>
<td data-sort-value="366"><p><samp>0000016e</samp></p></td>
<td><p><em>Submarine</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Submarine Theme</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td></td>
</tr>
<tr>
<td><p><samp>summer1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>122</samp></p></td>
<td data-sort-value="122"><p><samp>0000007a</samp></p></td>
<td><p><em>Summer (Nature's Crescendo)</em></p></td>
<td><p>A happy track featuring castanets, flute, and bass. Plays in
various outdoor locations in summer.</p></td>
</tr>
<tr>
<td><p><samp>summer2</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>123</samp></p></td>
<td data-sort-value="123"><p><samp>0000007b</samp></p></td>
<td><p><em>Summer (The Sun Can Bend An Orange Sky)</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>summer3</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>115</samp></p></td>
<td data-sort-value="115"><p><samp>00000073</samp></p></td>
<td><p><em>Summer (Tropicala)</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>SunRoom</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>17</samp></p></td>
<td data-sort-value="17"><p><samp>00000011</samp></p></td>
<td><p><em>Alone With Relaxing Tea</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Sun Room (Alone with Relaxing Tea)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td></td>
</tr>
<tr>
<td><p><samp>sweet</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>144</samp></p></td>
<td data-sort-value="144"><p><samp>00000090</samp></p></td>
<td><p><em>Buttercup Melody</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>tickTock</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>300</samp></p></td>
<td data-sort-value="300"><p><samp>0000012c</samp></p></td>
<td><p><em>Festival Game</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>tinymusicbox</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>296</samp></p></td>
<td data-sort-value="296"><p><samp>00000128</samp></p></td>
<td><p><em>Music Box Song</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a> only)</p></td>
<td><p>The <a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>'s <em>Music Box Song</em> is
<samp>musicboxsong</samp>, not this one.</p></td>
</tr>
<tr>
<td><p><samp>title_night</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>127</samp></p></td>
<td data-sort-value="127"><p><samp>0000007f</samp></p></td>
<td><p><em>Load Game Theme</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Load Game</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td></td>
</tr>
<tr>
<td><p><samp>tribal</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>198</samp></p></td>
<td data-sort-value="198"><p><samp>000000c6</samp></p></td>
<td><p><em>Mines (Danger!)</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>Tropical Jam</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>115</samp></p></td>
<td data-sort-value="115"><p><samp>00000073</samp></p></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="2"><p><samp>VolcanoMines</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>382</samp></p></td>
<td data-sort-value="382"><p><samp>0000017e</samp></p></td>
<td rowspan="2"></td>
<td rowspan="2"></td>
</tr>
<tr>
<td><p><samp>384</samp></p></td>
<td data-sort-value="384"><p><samp>00000180</samp></p></td>
</tr>
<tr>
<td><p><samp>VolcanoMines1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>382</samp></p></td>
<td data-sort-value="382"><p><samp>0000017e</samp></p></td>
<td><p><em>Volcano Mines (Molten Jelly)</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>VolcanoMines2</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>384</samp></p></td>
<td data-sort-value="384"><p><samp>00000180</samp></p></td>
<td><p><em>Volcano Mines (Forgotten World)</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>wavy</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>95</samp></p></td>
<td data-sort-value="95"><p><samp>0000005f</samp></p></td>
<td><p><em>Calico Desert</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>wedding</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>104</samp></p></td>
<td data-sort-value="104"><p><samp>00000068</samp></p></td>
<td><p><em>Wedding Theme</em> (<a href="jukebox" class="wikilink"
title="jukebox">jukebox</a>);<br />
<em>Wedding Celebration</em> (<a href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td></td>
</tr>
<tr>
<td><p><samp>winter1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>126</samp></p></td>
<td data-sort-value="126"><p><samp>0000007e</samp></p></td>
<td><p><em>Winter (Nocturne of Ice)</em></p></td>
<td><p>A slow, peaceful track with xylophone and synths. Plays in
various outdoor locations in winter.</p></td>
</tr>
<tr>
<td><p><samp>winter2</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>124</samp></p></td>
<td data-sort-value="124"><p><samp>0000007c</samp></p></td>
<td><p><em>Winter (The Wind Can Be Still)</em></p></td>
<td><p>A slow and peaceful synth track. Plays in various outdoor
locations in winter.</p></td>
</tr>
<tr>
<td><p><samp>winter3</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>125</samp></p></td>
<td data-sort-value="125"><p><samp>0000007d</samp></p></td>
<td><p><em>Winter (Ancient)</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>WizardSong</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>321</samp></p></td>
<td data-sort-value="321"><p><samp>00000141</samp></p></td>
<td><p><em>A Glimpse Of The Other World</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>A Glimpse of the Other World (Wizard's Theme)</em> (<a
href="soundtrack" class="wikilink"
title="soundtrack">soundtrack</a>)</p></td>
<td></td>
</tr>
<tr>
<td><p><samp>woodsTheme</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>216</samp></p></td>
<td data-sort-value="216"><p><samp>000000d8</samp></p></td>
<td><p><em>In the Deep Woods</em></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>XOR</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>69</samp></p></td>
<td data-sort-value="69"><p><samp>00000045</samp></p></td>
<td><p><em>Mines (Marimba Of Frozen Bone)</em> (<a href="jukebox"
class="wikilink" title="jukebox">jukebox</a>);<br />
<em>Mines (Marimba Of Frozen Bones)</em> (<a href="soundtrack"
class="wikilink" title="soundtrack">soundtrack</a>)</p></td>
<td></td>
</tr>
</tbody>
</table>

### Music (ambient)

<table>
<thead>
<tr>
<th><p>cue ID</p></th>
<th><p>wavebank</p></th>
<th colspan="2"><p>soundbank index</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>dec</p></td>
<td><p>hex</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>babblingBrook</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>343</samp></p></td>
<td data-sort-value="343"><p><samp>00000157</samp></p></td>
<td><p>A loop of a stream flowing. Plays when near rivers.</p></td>
</tr>
<tr>
<td><p><samp>bugLevelLoop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>169</samp></p></td>
<td data-sort-value="169"><p><samp>000000a9</samp></p></td>
<td><p>A loop of bug wings periodically clicking and buzzing. Plays when
a <a href="The_Mines#Swarms" class="wikilink" title="swarm">swarm</a>
happens in the mines.</p></td>
</tr>
<tr>
<td><p><samp>communityCenter</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>307</samp></p></td>
<td data-sort-value="307"><p><samp>00000133</samp></p></td>
<td><p>A loop of the wind blowing, wood beams creaking, and the
occasional wind chime. Used as the background audio in the <a
href="Community_Center" class="wikilink"
title="Community Center">Community Center</a> when it is not yet
completed.</p></td>
</tr>
<tr>
<td><p><samp>cracklingFire</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>342</samp></p></td>
<td data-sort-value="342"><p><samp>00000156</samp></p></td>
<td><p>A loop of the sound of fire crackling. Played by fireplace
furniture and the campfire near <a href="Linus" class="wikilink"
title="Linus">Linus</a>' tent.</p></td>
</tr>
<tr>
<td><p><samp>darkCaveLoop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>168</samp></p></td>
<td data-sort-value="168"><p><samp>000000a8</samp></p></td>
<td><p>A constant, fairly quiet low loop of air flowing eerily. Appears
to be unused in vanilla.</p></td>
</tr>
<tr>
<td><p><samp>fall_day_ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>338</samp></p></td>
<td data-sort-value="338"><p><samp>00000152</samp></p></td>
<td><p>A loop of leaves rustling in the wind, ravens cawing, and the
occasional soft wind chime. Used as outdoor ambiance in the
fall.</p></td>
</tr>
<tr>
<td><p><samp>Frost_Ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>200</samp></p></td>
<td data-sort-value="200"><p><samp>000000c8</samp></p></td>
<td><p>A loop of wind gusting and a quiet tinkling noise in the
background. Used as ambiance in the frozen levels of the <a
href="The_Mines#Floors" class="wikilink"
title="mines">mines</a>.</p></td>
</tr>
<tr>
<td><p><samp>heavyEngine</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>344</samp></p></td>
<td data-sort-value="344"><p><samp>00000158</samp></p></td>
<td><p>A loop of an engine rumbling. The sound of the machine outside
the <a href="Blacksmith" class="wikilink"
title="Blacksmith">Blacksmith</a>.</p></td>
</tr>
<tr>
<td><p><samp>Hospital_Ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>283</samp></p></td>
<td data-sort-value="283"><p><samp>0000011b</samp></p></td>
<td><p>A loop of fans whirring and a machine beeping. Used as background
music for many events that take place at <a href="Harvey&#39;s_Clinic"
class="wikilink" title="Harvey&#39;s Clinic">Harvey's
Clinic</a>.</p></td>
</tr>
<tr>
<td><p><samp>jojaOfficeSoundscape</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>337</samp></p></td>
<td data-sort-value="337"><p><samp>00000151</samp></p></td>
<td><p>A loop of fans whirring and keyboards typing. Used in the intro
cutscene for the game.</p></td>
</tr>
<tr>
<td><p><samp>jungle_ambience</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>371</samp></p></td>
<td data-sort-value="371"><p><samp>00000173</samp></p></td>
<td><p>A loop of birds twittering and other rainforest creatures
calling. Used as ambiance for <a href="Ginger_Island#Island_East"
class="wikilink" title="Ginger Island East">Ginger Island
East</a>.</p></td>
</tr>
<tr>
<td><p><samp>Lava_Ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>201</samp></p></td>
<td data-sort-value="201"><p><samp>000000c9</samp></p></td>
<td><p>A loop of the wind blowing, and the occasional low rumble. Used
as ambiance in the lava levels of the <a href="The_Mines#Floors"
class="wikilink" title="mines">mines</a>.</p></td>
</tr>
<tr>
<td><p><samp>movieScreenAmbience</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>6</samp></p></td>
<td data-sort-value="6"><p><samp>00000006</samp></p></td>
<td><p>Begins with people chattering and snacking, which fade out to a
projector starting up. This track does not loop. Used when the player
goes to see a <a href="Movie_Theater" class="wikilink"
title="movie">movie</a>.</p></td>
</tr>
<tr>
<td><p><samp>nightTime</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>224</samp></p></td>
<td data-sort-value="224"><p><samp>000000e0</samp></p></td>
<td><p>A loop of crickets chirping. Used during several overnight events
such as the <a href="Random_Events#The_Crop_Fairy" class="wikilink"
title="crop fairy">crop fairy</a>.</p></td>
</tr>
<tr>
<td><p><samp>ocean</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>175</samp></p></td>
<td data-sort-value="175"><p><samp>000000af</samp></p></td>
<td><p>A loop of the sound of ocean waves. Plays at <a href="the_Beach"
class="wikilink" title="the Beach">the Beach</a>.</p></td>
</tr>
<tr>
<td><p><samp>pool_ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>288</samp></p></td>
<td data-sort-value="288"><p><samp>00000120</samp></p></td>
<td><p>A loop that sounds similar to a faucet running. Used as ambiance
in the <a href="Spa" class="wikilink" title="Spa">Spa</a> pool.</p></td>
</tr>
<tr>
<td><p><samp>rain</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>116</samp></p></td>
<td data-sort-value="116"><p><samp>00000074</samp></p></td>
<td><p>A loop of rain pouring. Used on rainy days.</p></td>
</tr>
<tr>
<td><p><samp>roadnoise</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>189</samp></p></td>
<td data-sort-value="189"><p><samp>000000bd</samp></p></td>
<td><p>Used in the intro cutscene.</p></td>
</tr>
<tr>
<td><p><samp>spring_day_ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>179</samp></p></td>
<td data-sort-value="179"><p><samp>000000b3</samp></p></td>
<td><p>A loop of birds chirping. Used as outdoor ambiance in the spring
during the day.</p></td>
</tr>
<tr>
<td><p><samp>spring_night_ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>345</samp></p></td>
<td data-sort-value="345"><p><samp>00000159</samp></p></td>
<td><p>A loop of crickets chirping. Used as outdoor ambiance at night in
all seasons but winter.</p></td>
</tr>
<tr>
<td><p><samp>summer_day_ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>339</samp></p></td>
<td data-sort-value="339"><p><samp>00000153</samp></p></td>
<td><p>A loop of flies buzzing and birds chirping. Used as outdoor
ambiance in the summer during the day.</p></td>
</tr>
<tr>
<td><p><samp>tropical_island_day_ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>376</samp></p></td>
<td data-sort-value="376"><p><samp>00000178</samp></p></td>
<td><p>A loop of leaves rustling in the wind and rainforest creatures
calling. Used as outdoor ambiance at <a href="Ginger_Island"
class="wikilink" title="Ginger Island">Ginger Island</a> during the
day.</p></td>
</tr>
<tr>
<td><p><samp>Upper_Ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>199</samp></p></td>
<td data-sort-value="199"><p><samp>000000c7</samp></p></td>
<td><p>A loop of the wind blowing and the occasional sound of water
dripping. Used as ambiance in the non-frost/lava levels of the <a
href="The_Mines#Floors" class="wikilink"
title="mines">mines</a></p></td>
</tr>
<tr>
<td><p><samp>Volcano_Ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>377</samp></p></td>
<td data-sort-value="377"><p><samp>00000179</samp></p></td>
<td><p>A loop of fire crackling, lava bubbling, and the wind
occasionally gusting. Used as ambiance in the <a href="Volcano_Dungeon"
class="wikilink" title="Volcano Dungeon">Volcano Dungeon</a>.</p></td>
</tr>
<tr>
<td><p><samp>waterfall</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>427</samp></p></td>
<td data-sort-value="427"><p><samp>000001ab</samp></p></td>
<td><p>A loop of a waterfall rushing. Plays near waterfalls.</p></td>
</tr>
<tr>
<td><p><samp>waterfall_big</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>428</samp></p></td>
<td data-sort-value="428"><p><samp>000001ac</samp></p></td>
<td><p>A loop of a large waterfall rushing. Plays near
waterfalls.</p></td>
</tr>
<tr>
<td><p><samp>wind</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>85</samp></p></td>
<td data-sort-value="85"><p><samp>00000055</samp></p></td>
<td><p>A loop of the wind blowing.</p></td>
</tr>
<tr>
<td><p><samp>winter_day_ambient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>354</samp></p></td>
<td data-sort-value="354"><p><samp>00000162</samp></p></td>
<td><p>A loop of the wind howling and gusting. Used as outdoor ambiance
in the winter during the day.</p></td>
</tr>
</tbody>
</table>

### Sound

<table>
<thead>
<tr>
<th><p>cue ID</p></th>
<th><p>wavebank</p></th>
<th colspan="2"><p>soundbank index</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>dec</p></td>
<td><p>hex</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>achievement</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>103</samp></p></td>
<td data-sort-value="103"><p><samp>00000067</samp></p></td>
<td><p>A bright "success" synth chime with reverb. Plays when the player
gets an <a href="Achievements" class="wikilink"
title="achievement">achievement</a>.</p></td>
</tr>
<tr>
<td><p><samp>axchop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>141</samp></p></td>
<td data-sort-value="141"><p><samp>0000008d</samp></p></td>
<td><p>The hollow sound of an axe hitting wood. Used when various wooden
things are hit with the <a href="Axes" class="wikilink"
title="Axe">Axe</a>.</p></td>
</tr>
<tr>
<td><p><samp>axe</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>1</samp></p></td>
<td data-sort-value="1"><p><samp>00000001</samp></p></td>
<td><p>A higher-pitched version of <samp>axchop</samp>. Plays when
various wooden items such as <a href="Tapper" class="wikilink"
title="Tappers">Tappers</a> are placed.</p></td>
</tr>
<tr>
<td><p><samp>backpackIN</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>133</samp></p></td>
<td data-sort-value="133"><p><samp>00000085</samp></p></td>
<td><p>A low-pitched, descending "whoop" noise. Plays when the player
holds an item in their hand and deposits it in the <a href="Shipping"
class="wikilink" title="Shipping Bin">Shipping Bin</a> without opening
the menu to do so.</p></td>
</tr>
<tr>
<td><p><samp>barrelBreak</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>310</samp></p></td>
<td data-sort-value="310"><p><samp>00000136</samp></p></td>
<td><p>The sound of a wooden crate smashing. Plays when <a
href="The_Mines#Crates_and_Barrels" class="wikilink"
title="Crates and Barrels">Crates and Barrels</a> are broken in the
Mines.</p></td>
</tr>
<tr>
<td><p><samp>batFlap</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>170</samp></p></td>
<td data-sort-value="170"><p><samp>000000aa</samp></p></td>
<td><p>Wings flapping. Used by <a href="bats" class="wikilink"
title="bats">bats</a>, birds, and when weapons block attacks.</p></td>
</tr>
<tr>
<td><p><samp>batScreech</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>171</samp></p></td>
<td data-sort-value="171"><p><samp>000000ab</samp></p></td>
<td><p>A <a href="Bats" class="wikilink" title="bat">bat</a>
screeching.</p></td>
</tr>
<tr>
<td><p><samp>bigDeSelect</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>2</samp></p></td>
<td data-sort-value="2"><p><samp>00000002</samp></p></td>
<td><p>A short, descending click. Plays when menus are closed.</p></td>
</tr>
<tr>
<td><p><samp>bigSelect</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>3</samp></p></td>
<td data-sort-value="3"><p><samp>00000003</samp></p></td>
<td><p>Variation on the <samp>bigDeSelect</samp> sound cue.</p></td>
</tr>
<tr>
<td><p><samp>bob</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>30</samp></p></td>
<td data-sort-value="30"><p><samp>0000001e</samp></p></td>
<td><p>A low "bloop". Plays while <a href="Fishing" class="wikilink"
title="Fishing">Fishing</a> when the rod has been cast but no fish are
on the line.</p></td>
</tr>
<tr>
<td><p><samp>book_read</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>423</samp></p></td>
<td data-sort-value="423"><p><samp>000001a7</samp></p></td>
<td><p>The sound of book pages flipping rapidly. Plays when the player
reads a <a href="Books" class="wikilink" title="Book">Book</a>.</p></td>
</tr>
<tr>
<td rowspan="4"><p><samp>boop</samp></p></td>
<td rowspan="4"><p><samp>Wavebank</samp></p></td>
<td><p><samp>98</samp></p></td>
<td data-sort-value="98"><p><samp>00000062</samp></p></td>
<td rowspan="4"><p>Various electric sci-fi zaps. Plays randomly as
ambiance in the <a href="Casino" class="wikilink"
title="Casino">Casino</a>.</p></td>
</tr>
<tr>
<td><p><samp>99</samp></p></td>
<td data-sort-value="99"><p><samp>00000063</samp></p></td>
</tr>
<tr>
<td><p><samp>100</samp></p></td>
<td data-sort-value="100"><p><samp>00000064</samp></p></td>
</tr>
<tr>
<td><p><samp>101</samp></p></td>
<td data-sort-value="101"><p><samp>00000065</samp></p></td>
</tr>
<tr>
<td><p><samp>boulderBreak</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>238</samp></p></td>
<td data-sort-value="238"><p><samp>000000ee</samp></p></td>
<td><p>The sound of a rock shattering. Plays when <a href="Boulder"
class="wikilink" title="boulders">boulders</a> break.</p></td>
</tr>
<tr>
<td><p><samp>boulderCrack</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>4</samp></p></td>
<td data-sort-value="4"><p><samp>00000004</samp></p></td>
<td><p>A high-pitched "dink" sound. Plays when tools and weapons are <a
href="Forge" class="wikilink" title="forged">forged</a>.</p></td>
</tr>
<tr>
<td><p><samp>breakingGlass</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>284</samp></p></td>
<td data-sort-value="284"><p><samp>0000011c</samp></p></td>
<td><p>The sound of glass shattering. Plays when crystals in the frozen
levels of the <a href="The_Mines#Floors" class="wikilink"
title="mines">mines</a> shatter.</p></td>
</tr>
<tr>
<td><p><samp>breathin</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>84</samp></p></td>
<td data-sort-value="84"><p><samp>00000054</samp></p></td>
<td><p>An ascending "whoop" noise. Plays when dialogue boxes are
opened.</p></td>
</tr>
<tr>
<td><p><samp>breathout</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>83</samp></p></td>
<td data-sort-value="83"><p><samp>00000053</samp></p></td>
<td><p>A descending "whoop" noise. Plays when dialogue boxes are
closed.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>bubbles</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>235</samp></p></td>
<td data-sort-value="235"><p><samp>000000eb</samp></p></td>
<td rowspan="2"><p>A bubbling sound. Played by <a href="Keg"
class="wikilink" title="Kegs">Kegs</a>, <a href="Cask" class="wikilink"
title="Casks">Casks</a>, <a href="Oil_Maker" class="wikilink"
title="Oil Makers">Oil Makers</a>, the <a href="Slime_Egg-Press"
class="wikilink" title="Slime Egg-Press">Slime Egg-Press</a>, and the <a
href="Cauldron" class="wikilink" title="Cauldron">Cauldron</a> furniture
when it is turned on.</p></td>
</tr>
<tr>
<td><p><samp>236</samp></p></td>
<td data-sort-value="236"><p><samp>000000ec</samp></p></td>
</tr>
<tr>
<td><p><samp>busDoorOpen</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>191</samp></p></td>
<td data-sort-value="191"><p><samp>000000bf</samp></p></td>
<td><p>A hissing noise followed by an ascending "whoop". Used in various
cutscenes.</p></td>
</tr>
<tr>
<td><p><samp>busDriveOff</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>309</samp></p></td>
<td data-sort-value="309"><p><samp>00000135</samp></p></td>
<td><p>The sound of a bus engine rumbling that fades out into the
distance. Plays when the <a href="Bus_Stop" class="wikilink"
title="Bus">Bus</a> drives away (such as when the player visits <a
href="The_Desert" class="wikilink" title="The Desert">The
Desert</a>).</p></td>
</tr>
<tr>
<td><p><samp>button_press</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>411</samp></p></td>
<td data-sort-value="411"><p><samp>0000019b</samp></p></td>
<td><p>A mechanical button click. Used by the <a href="Prize_Ticket"
class="wikilink" title="Prize Ticket">Prize Ticket</a> machine
menu.</p></td>
</tr>
<tr>
<td><p><samp>button_tap</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>412</samp></p></td>
<td data-sort-value="412"><p><samp>0000019c</samp></p></td>
<td><p>A quiet mechanical button click. Used by the <a
href="Prize_Ticket" class="wikilink" title="Prize Ticket">Prize
Ticket</a> machine menu.</p></td>
</tr>
<tr>
<td><p><samp>button1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>250</samp></p></td>
<td data-sort-value="250"><p><samp>000000fa</samp></p></td>
<td><p>A high-pitched "click-click" noise. Plays when bobbers are
attached to fishing rods.</p></td>
</tr>
<tr>
<td><p><samp>cacklingWitch</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>323</samp></p></td>
<td data-sort-value="323"><p><samp>00000143</samp></p></td>
<td><p>An cartoony evil witch laugh. Used in the <a
href="Random_Events#The_Witch" class="wikilink" title="Witch">Witch</a>
nighttime event.</p></td>
</tr>
<tr>
<td><p><samp>camel</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>23</samp></p></td>
<td data-sort-value="23"><p><samp>00000017</samp></p></td>
<td><p>A camel bleating. Plays when the player interacts with the <a
href="Desert_Trader" class="wikilink" title="Desert Trader">Desert
Trader</a>'s camel.</p></td>
</tr>
<tr>
<td><p><samp>cameraNoise</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>292</samp></p></td>
<td data-sort-value="292"><p><samp>00000124</samp></p></td>
<td><p>A camera shutter clicking. Plays when screenshots are taken and
when <a href="Haley" class="wikilink" title="Haley">Haley</a> takes
photos in several events.</p></td>
</tr>
<tr>
<td><p><samp>cancel</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>353</samp></p></td>
<td data-sort-value="353"><p><samp>00000161</samp></p></td>
<td><p>A short shaker noise. Used for various cancellation actions or
when the player has insufficient resources to perform an
action.</p></td>
</tr>
<tr>
<td><p><samp>cast</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>246</samp></p></td>
<td data-sort-value="246"><p><samp>000000f6</samp></p></td>
<td><p>A short "shwhip" noise. Used by the <a href="Tools#Fishing_Poles"
class="wikilink" title="Fishing Rod">Fishing Rod</a> when it is
cast.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>cat</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>332</samp></p></td>
<td data-sort-value="332"><p><samp>0000014c</samp></p></td>
<td rowspan="2"><p>A <a href="Animals#Cat_or_Dog" class="wikilink"
title="cat">cat</a> meowing.</p></td>
</tr>
<tr>
<td><p><samp>333</samp></p></td>
<td data-sort-value="333"><p><samp>0000014d</samp></p></td>
</tr>
<tr>
<td><p><samp>cavedrip</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>129</samp></p></td>
<td data-sort-value="129"><p><samp>00000081</samp></p></td>
<td><p>A wet 'dwoop' sound. Used as random background noise in <a
href="The_Mines" class="wikilink" title="the mines">the mines</a> and <a
href="The_Sewers" class="wikilink" title="sewers">sewers</a>, and the
dripping sound for the <a href="Volcano_Dungeon" class="wikilink"
title="volcano dungeon">volcano dungeon</a> entrance pipe.</p></td>
</tr>
<tr>
<td><p><samp>clam_tone</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>363</samp></p></td>
<td data-sort-value="363"><p><samp>0000016b</samp></p></td>
<td><p>A kalimba-esque tone. Used in the "uh" multiplayer emote and the
<a href="Night_Market#Mermaid_Boat" class="wikilink"
title="Mermaid Boat">Mermaid Boat</a>. <a href="Flute_Block"
class="wikilink" title="Flute Blocks">Flute Blocks</a> play this sound
as one of their special sounds.</p></td>
</tr>
<tr>
<td rowspan="6"><p><samp>clank</samp></p></td>
<td rowspan="6"><p><samp>Wavebank</samp></p></td>
<td><p><samp>173</samp></p></td>
<td data-sort-value="173"><p><samp>000000ad</samp></p></td>
<td rowspan="6"><p>A metal-on-metal clanking sound. Plays when <a
href="Metal_Head" class="wikilink" title="Metal Heads">Metal Heads</a>
take damage, as ambient noise when Robin is constructing a farm
building, and when a <a href="Pickaxes" class="wikilink"
title="Pickaxe">Pickaxe</a> is used on boulders that it is not strong
enough to break.</p></td>
</tr>
<tr>
<td><p><samp>203</samp></p></td>
<td data-sort-value="203"><p><samp>000000cb</samp></p></td>
</tr>
<tr>
<td><p><samp>203</samp></p></td>
<td data-sort-value="203"><p><samp>000000cb</samp></p></td>
</tr>
<tr>
<td><p><samp>204</samp></p></td>
<td data-sort-value="204"><p><samp>000000cc</samp></p></td>
</tr>
<tr>
<td><p><samp>205</samp></p></td>
<td data-sort-value="205"><p><samp>000000cd</samp></p></td>
</tr>
<tr>
<td><p><samp>205</samp></p></td>
<td data-sort-value="205"><p><samp>000000cd</samp></p></td>
</tr>
<tr>
<td><p><samp>clubhit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>159</samp></p></td>
<td data-sort-value="159"><p><samp>0000009f</samp></p></td>
<td><p>A low-pitched thud. Used by <a href="Weapons#Club"
class="wikilink" title="Clubs">Clubs</a>.</p></td>
</tr>
<tr>
<td><p><samp>clubSmash</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>174</samp></p></td>
<td data-sort-value="174"><p><samp>000000ae</samp></p></td>
<td><p>A more aggressive and low-pitched thud. Used by <a
href="Weapons#Club" class="wikilink" title="Clubs">Clubs</a> when the
special attack is triggered.</p></td>
</tr>
<tr>
<td><p><samp>clubswipe</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>160</samp></p></td>
<td data-sort-value="160"><p><samp>000000a0</samp></p></td>
<td><p>A low-pitched "swish" noise. Plays when <a href="Weapons#Club"
class="wikilink" title="Clubs">Clubs</a> swing.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>cluck</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>31</samp></p></td>
<td data-sort-value="31"><p><samp>0000001f</samp></p></td>
<td rowspan="3"><p>A <a href="chicken" class="wikilink"
title="chicken">chicken</a> clucking.</p></td>
</tr>
<tr>
<td><p><samp>32</samp></p></td>
<td data-sort-value="32"><p><samp>00000020</samp></p></td>
</tr>
<tr>
<td><p><samp>33</samp></p></td>
<td data-sort-value="33"><p><samp>00000021</samp></p></td>
</tr>
<tr>
<td><p><samp>coin</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>5</samp></p></td>
<td data-sort-value="5"><p><samp>00000005</samp></p></td>
<td><p>A "pop" sound. Plays in a variety of situations, including when
the player picks up objects.</p></td>
</tr>
<tr>
<td><p><samp>coldSpell</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>197</samp></p></td>
<td data-sort-value="197"><p><samp>000000c5</samp></p></td>
<td><p>A high-pitched and rattly "woosh". Unused in vanilla.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>cow</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>80</samp></p></td>
<td data-sort-value="80"><p><samp>00000050</samp></p></td>
<td rowspan="3"><p>A <a href="cow" class="wikilink" title="cow">cow</a>
mooing.</p></td>
</tr>
<tr>
<td><p><samp>81</samp></p></td>
<td data-sort-value="81"><p><samp>00000051</samp></p></td>
</tr>
<tr>
<td><p><samp>82</samp></p></td>
<td data-sort-value="82"><p><samp>00000052</samp></p></td>
</tr>
<tr>
<td><p><samp>cowboy_dead</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>268</samp></p></td>
<td data-sort-value="268"><p><samp>0000010c</samp></p></td>
<td><p>An 8-bit zap noise followed by a disappointed-sounding descending
riff. Plays when the player dies in <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>cowboy_explosion</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>276</samp></p></td>
<td data-sort-value="276"><p><samp>00000114</samp></p></td>
<td><p>An 8-bit explosion sound. Used by <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>cowboy_gopher</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>275</samp></p></td>
<td data-sort-value="275"><p><samp>00000113</samp></p></td>
<td><p>A quick, high-pitched zap. Used by the gopher in <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>cowboy_gunload</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>272</samp></p></td>
<td data-sort-value="272"><p><samp>00000110</samp></p></td>
<td><p>An 8-bit version of a gun loading. Used by <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>Cowboy_gunshot</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>266</samp></p></td>
<td data-sort-value="266"><p><samp>0000010a</samp></p></td>
<td><p>A short, hollow 'tock' sound. Used for woodpeckers pecks, <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie King</a>
guns, <a href="darts" class="wikilink" title="darts">darts</a> impact,
<a href="Slot_Machine" class="wikilink" title="casino slots">casino
slots</a>, and a hover sound in many in-game menus.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>Cowboy_monsterDie</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>264</samp></p></td>
<td data-sort-value="264"><p><samp>00000108</samp></p></td>
<td rowspan="2"><p>An 8-bit death noise. Plays when monsters die in <a
href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>265</samp></p></td>
<td data-sort-value="265"><p><samp>00000109</samp></p></td>
</tr>
<tr>
<td><p><samp>cowboy_monsterhit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>274</samp></p></td>
<td data-sort-value="274"><p><samp>00000112</samp></p></td>
<td><p>A short, hollow "tock" sound. Plays when monsters are damaged in
<a href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>cowboy_powerup</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>271</samp></p></td>
<td data-sort-value="271"><p><samp>0000010f</samp></p></td>
<td><p>An ascending, 8-bit zap. Plays when the player gets a powerup in
<a href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>Cowboy_Secret</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>263</samp></p></td>
<td data-sort-value="263"><p><samp>00000107</samp></p></td>
<td><p>An ascending, 8-bit jingle. Plays when the player holds up
powerups in <a href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>crafting</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>36</samp></p></td>
<td data-sort-value="36"><p><samp>00000024</samp></p></td>
<td><p>A hammer clanking on a nail. Plays when the player tries to
damage a hiding <a href="Rock_Crab" class="wikilink"
title="Rock Crab">Rock Crab</a>.</p></td>
</tr>
<tr>
<td><p><samp>crane</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>14</samp></p></td>
<td data-sort-value="14"><p><samp>0000000e</samp></p></td>
<td><p>A looping buzzing sound. Used by the <a
href="Movie_Theater#Crane_Game" class="wikilink"
title="Crane Game">Crane Game</a>.</p></td>
</tr>
<tr>
<td><p><samp>crickets</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>117</samp></p></td>
<td data-sort-value="117"><p><samp>00000075</samp></p></td>
<td><p>A single chirp. Used as random ambient nighttime noise.</p></td>
</tr>
<tr>
<td><p><samp>cricketsAmbient</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>346</samp></p></td>
<td data-sort-value="346"><p><samp>0000015a</samp></p></td>
<td><p>A loop of crickets chirping. Plays as ambient nighttime
noise.</p></td>
</tr>
<tr>
<td><p><samp>crit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>352</samp></p></td>
<td data-sort-value="352"><p><samp>00000160</samp></p></td>
<td><p>A high-pitched "zing". Plays when the player lands a critical hit
with their weapon.</p></td>
</tr>
<tr>
<td><p><samp>croak</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>138</samp></p></td>
<td data-sort-value="138"><p><samp>0000008a</samp></p></td>
<td><p>A frog croaking once. Used as ambient noise in the rain and in
various cutscenes involving frogs.</p></td>
</tr>
<tr>
<td><p><samp>crow</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>324</samp></p></td>
<td data-sort-value="324"><p><samp>00000144</samp></p></td>
<td><p>A singular <a href="Animals#Crows" class="wikilink"
title="crow">crow</a> caw.</p></td>
</tr>
<tr>
<td><p><samp>crystal</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>143</samp></p></td>
<td data-sort-value="143"><p><samp>0000008f</samp></p></td>
<td><p>A high-pitched 'ding!' sound that resonates for a few seconds.
Used for the <a href="The_Mines" class="wikilink" title="mine">mine</a>
elevator ding, <a href="Ginger_Island#Colored_Crystals_Puzzle"
class="wikilink" title="island crystal puzzle">island crystal
puzzle</a>, in <a href="Modding_Dialogue" class="wikilink"
title="dialogue">dialogue</a> for the <samp>&lt;</samp> character, <a
href="Singing_Stone" class="wikilink" title="Singing Stone">Singing
Stone</a> (with a random pitch), and mine crystals when broken.</p></td>
</tr>
<tr>
<td><p><samp>cursed_mannequin</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>431</samp></p></td>
<td data-sort-value="431"><p><samp>000001af</samp></p></td>
<td><p>A spooky breathing noise. Plays when the <a
href="Cursed_Mannequins" class="wikilink"
title="Cursed Mannequin">Cursed Mannequin</a> "comes to life".</p></td>
</tr>
<tr>
<td><p><samp>cut</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>6</samp></p></td>
<td data-sort-value="6"><p><samp>00000006</samp></p></td>
<td><p>The sound of foliage swiping. Plays when <a href="Weeds"
class="wikilink" title="Weeds">Weeds</a> are cut.</p></td>
</tr>
<tr>
<td><p><samp>daggerswipe</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>163</samp></p></td>
<td data-sort-value="163"><p><samp>000000a3</samp></p></td>
<td><p>A short swiping noise. Plays when the <a href="Weapons#Dagger"
class="wikilink" title="Dagger">Dagger</a> is used for a normal
attack.</p></td>
</tr>
<tr>
<td><p><samp>death</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>70</samp></p></td>
<td data-sort-value="70"><p><samp>00000046</samp></p></td>
<td><p>A descending marimba riff. Plays when the player is knocked to 0
health.</p></td>
</tr>
<tr>
<td><p><samp>debuffHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>151</samp></p></td>
<td data-sort-value="151"><p><samp>00000097</samp></p></td>
<td><p>A "zap" noise. Plays when debuffing projectiles hit the
player.</p></td>
</tr>
<tr>
<td><p><samp>debuffSpell</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>152</samp></p></td>
<td data-sort-value="152"><p><samp>00000098</samp></p></td>
<td><p>A similar "zap" sound to <samp>debuffHit</samp>. Plays when
debuffing projectiles are fired at the player.</p></td>
</tr>
<tr>
<td><p><samp>detector</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>37</samp></p></td>
<td data-sort-value="37"><p><samp>00000025</samp></p></td>
<td><p>A high-pitched sci-fi "boing". Unused by Vanilla.</p></td>
</tr>
<tr>
<td><p><samp>dialogueCharacter</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>7</samp></p></td>
<td data-sort-value="7"><p><samp>00000007</samp></p></td>
<td><p>A short tone. Plays when the dialogue typing animation is running
for dialogue boxes.</p></td>
</tr>
<tr>
<td><p><samp>dialogueCharacterClose</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>8</samp></p></td>
<td data-sort-value="8"><p><samp>00000008</samp></p></td>
<td><p>A short ascending tone. Plays when the last character of the text
in a dialogue box is rendered in the typing animation.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>dirtyHit</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>243</samp></p></td>
<td data-sort-value="243"><p><samp>000000f3</samp></p></td>
<td rowspan="2"><p>The sound of digging in the dirt. Plays when crops
are planted.</p></td>
</tr>
<tr>
<td><p><samp>244</samp></p></td>
<td data-sort-value="244"><p><samp>000000f4</samp></p></td>
</tr>
<tr>
<td><p><samp>discoverMineral</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>208</samp></p></td>
<td data-sort-value="208"><p><samp>000000d0</samp></p></td>
<td><p>A sparkling noise. Plays when the player gets rarer drops from
cracking <a href="Geode" class="wikilink"
title="Geodes">Geodes</a>.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>distantTrain</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>220</samp></p></td>
<td data-sort-value="220"><p><samp>000000dc</samp></p></td>
<td rowspan="2"><p>A train whistle in the distance. Plays when a <a
href="Railroad" class="wikilink" title="Train">Train</a> comes but the
player is not at the Railroad.</p></td>
</tr>
<tr>
<td><p><samp>221</samp></p></td>
<td data-sort-value="221"><p><samp>000000dd</samp></p></td>
</tr>
<tr>
<td><p><samp>dog_bark</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>331</samp></p></td>
<td data-sort-value="331"><p><samp>0000014b</samp></p></td>
<td><p>A <a href="Animals#Cat_or_Dog" class="wikilink"
title="dog">dog</a> barking.</p></td>
</tr>
<tr>
<td><p><samp>dog_pant</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>330</samp></p></td>
<td data-sort-value="330"><p><samp>0000014a</samp></p></td>
<td><p>A <a href="Animals#Cat_or_Dog" class="wikilink"
title="dog">dog</a> panting.</p></td>
</tr>
<tr>
<td><p><samp>dogs</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>228</samp></p></td>
<td data-sort-value="228"><p><samp>000000e4</samp></p></td>
<td><p>Dogs howling and barking. Plays during the <a
href="Random_Events#Wild_animal_attack" class="wikilink"
title="Wild animal attack">Wild animal attack</a> nighttime
event.</p></td>
</tr>
<tr>
<td><p><samp>dogWhining</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>316</samp></p></td>
<td data-sort-value="316"><p><samp>0000013c</samp></p></td>
<td><p>A dog whining and panting. Plays in several events involving <a
href="Dusty" class="wikilink" title="Dusty">Dusty</a>.</p></td>
</tr>
<tr>
<td><p><samp>doorClose</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>9</samp></p></td>
<td data-sort-value="9"><p><samp>00000009</samp></p></td>
<td><p>A door closing. Used by exterior doors throughout the
game.</p></td>
</tr>
<tr>
<td><p><samp>doorCreak</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>319</samp></p></td>
<td data-sort-value="319"><p><samp>0000013f</samp></p></td>
<td><p>The sound of creaky door hinges. Plays when a <a href="Chest"
class="wikilink" title="Chest">Chest</a>, <a href="Shipping"
class="wikilink" title="Shipping Bin">Shipping Bin</a>, or fridge opens.
Also plays when the door of a <a href="Coop" class="wikilink"
title="Coop">Coop</a> or <a href="Barn" class="wikilink"
title="Barn">Barn</a> closes.</p></td>
</tr>
<tr>
<td><p><samp>doorCreakReverse</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>322</samp></p></td>
<td data-sort-value="322"><p><samp>00000142</samp></p></td>
<td><p>The sound of creaky door hinges. Plays when a <a href="Chest"
class="wikilink" title="Chest">Chest</a>, <a href="Shipping"
class="wikilink" title="Shipping Bin">Shipping Bin</a>, or fridge
closes. Also plays when the door of a <a href="Coop" class="wikilink"
title="Coop">Coop</a> or <a href="Barn" class="wikilink"
title="Barn">Barn</a> opens.</p></td>
</tr>
<tr>
<td><p><samp>doorOpen</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>320</samp></p></td>
<td data-sort-value="320"><p><samp>00000140</samp></p></td>
<td><p>The sound of a door opening. Plays when interior doors are
opened.</p></td>
</tr>
<tr>
<td><p><samp>dropItemInWater</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>10</samp></p></td>
<td data-sort-value="10"><p><samp>0000000a</samp></p></td>
<td><p>A "sploosh" noise. Plays when items are dropped in water, farm
animals swim, and fish splash.</p></td>
</tr>
<tr>
<td><p><samp>drumkit0</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>110</samp></p></td>
<td data-sort-value="110"><p><samp>0000006e</samp></p></td>
<td><p>A low-pitched drum hit.</p></td>
</tr>
<tr>
<td><p><samp>drumkit1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>111</samp></p></td>
<td data-sort-value="111"><p><samp>0000006f</samp></p></td>
<td><p>A snare drum hit.</p></td>
</tr>
<tr>
<td><p><samp>drumkit2</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>108</samp></p></td>
<td data-sort-value="108"><p><samp>0000006c</samp></p></td>
<td><p>A hit on a clamped hi-hat.</p></td>
</tr>
<tr>
<td><p><samp>drumkit3</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>107</samp></p></td>
<td data-sort-value="107"><p><samp>0000006b</samp></p></td>
<td><p>A hit on an open hi-hat.</p></td>
</tr>
<tr>
<td><p><samp>drumkit4</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>109</samp></p></td>
<td data-sort-value="109"><p><samp>0000006d</samp></p></td>
<td><p>A low-pitched kick drum hit.</p></td>
</tr>
<tr>
<td><p><samp>drumkit5</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>106</samp></p></td>
<td data-sort-value="106"><p><samp>0000006a</samp></p></td>
<td><p>A higher-pitched bongo drum hit.</p></td>
</tr>
<tr>
<td><p><samp>drumkit6</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>105</samp></p></td>
<td data-sort-value="105"><p><samp>00000069</samp></p></td>
<td><p>The highest-pitched drumkit sound. Reminiscent of a digital
metronome. Plays when checkboxes in the settings menu are
toggled.</p></td>
</tr>
<tr>
<td><p><samp>Duck</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>231</samp></p></td>
<td data-sort-value="231"><p><samp>000000e7</samp></p></td>
<td><p>A <a href="duck" class="wikilink" title="duck">duck</a>
quacking.</p></td>
</tr>
<tr>
<td><p><samp>Duggy</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>60</samp></p></td>
<td data-sort-value="60"><p><samp>0000003c</samp></p></td>
<td><p>Digging sounds. Plays when a <a href="Duggy" class="wikilink"
title="Duggy">Duggy</a> digs up underneath the player.</p></td>
</tr>
<tr>
<td><p><samp>dustMeep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>186</samp></p></td>
<td data-sort-value="186"><p><samp>000000ba</samp></p></td>
<td><p>A high-pitched chirp. Used as an alternate <a href="Junimo"
class="wikilink" title="Junimo">Junimo</a> sound. Also used as ambient
sounds for <a href="Dust_Sprite" class="wikilink"
title="Dust Sprites">Dust Sprites</a> and plays when they die.</p></td>
</tr>
<tr>
<td><p><samp>DwarvishSentry</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>386</samp></p></td>
<td data-sort-value="386"><p><samp>00000182</samp></p></td>
<td><p>A sci-fi "beep-boop" chirp. Plays when a <a
href="Dwarvish_Sentry" class="wikilink" title="Dwarvish Sentry">Dwarvish
Sentry</a> spawns.</p></td>
</tr>
<tr>
<td><p><samp>dwoop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>34</samp></p></td>
<td data-sort-value="34"><p><samp>00000022</samp></p></td>
<td><p>A sound that inflects upwards in pitch, but is a lower pitch than
<samp>dwop</samp>. Plays when farm animals go inside and when furniture
is rotated.</p></td>
</tr>
<tr>
<td><p><samp>dwop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>234</samp></p></td>
<td data-sort-value="234"><p><samp>000000ea</samp></p></td>
<td><p>A sound that inflects upwards in pitch. Plays when the user
clicks on an item in their inventory to lift it up and freely drag it
around, when the trash bear throws an item up into the air, when bobbers
are removed from fishing rods, etc.</p></td>
</tr>
<tr>
<td><p><samp>eat</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>25</samp></p></td>
<td data-sort-value="25"><p><samp>00000019</samp></p></td>
<td><p>A chomping noise. Plays when the player eats food.</p></td>
</tr>
<tr>
<td><p><samp>explosion</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>35</samp></p></td>
<td data-sort-value="35"><p><samp>00000023</samp></p></td>
<td><p>A loud "boom". Plays when bombs explode.</p></td>
</tr>
<tr>
<td><p><samp>fairy_heal</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>421</samp></p></td>
<td data-sort-value="421"><p><samp>000001a5</samp></p></td>
<td><p>A twinkling noise. Plays when the <a href="Fairy_Box"
class="wikilink" title="Fairy Box">Fairy Box</a> trinket heals the
player.</p></td>
</tr>
<tr>
<td><p><samp>fallDown</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>318</samp></p></td>
<td data-sort-value="318"><p><samp>0000013e</samp></p></td>
<td><p>A descending tone. Plays when the player jumps in a shaft in the
<a href="Skull_Cavern" class="wikilink" title="Skull Cavern">Skull
Cavern</a>.</p></td>
</tr>
<tr>
<td><p><samp>fastReel</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>248</samp></p></td>
<td data-sort-value="248"><p><samp>000000f8</samp></p></td>
<td><p>The sound of the fishing rod reeling. Plays when the fishing bar
is behind the fish during the fishing minigame.</p></td>
</tr>
<tr>
<td><p><samp>fireball</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>71</samp></p></td>
<td data-sort-value="71"><p><samp>00000047</samp></p></td>
<td><p>The sound of fire roaring. Plays when interior <a
href="Brick_Fireplace" class="wikilink"
title="Fireplaces">Fireplaces</a> are lit, when monsters fire flaming
projectiles, and when <a href="Butterfly_Powder" class="wikilink"
title="Butterfly Powder">Butterfly Powder</a> is used.</p></td>
</tr>
<tr>
<td><p><samp>firework</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>429</samp></p></td>
<td data-sort-value="429"><p><samp>000001ad</samp></p></td>
<td><p>A firework taking off and then exploding after a few seconds.
Plays when <a href="Fireworks_(Red)" class="wikilink"
title="Fireworks">Fireworks</a> are used.</p></td>
</tr>
<tr>
<td><p><samp>fishBite</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>26</samp></p></td>
<td data-sort-value="26"><p><samp>0000001a</samp></p></td>
<td><p>A warbling noise. This is the default sound that plays when a
fish bites. Players may select this sound as their fish bite sound in
the <a href="Options" class="wikilink" title="options menu">options
menu</a>.</p></td>
</tr>
<tr>
<td><p><samp>fishBite_alternate_0</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>398</samp></p></td>
<td data-sort-value="398"><p><samp>0000018e</samp></p></td>
<td><p>A higher-pitched version of <samp>fishBite</samp>. Players may
select this sound as their fish bite sound in the <a href="Options"
class="wikilink" title="options menu">options menu</a>.</p></td>
</tr>
<tr>
<td><p><samp>fishBite_alternate_1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>397</samp></p></td>
<td data-sort-value="397"><p><samp>0000018d</samp></p></td>
<td><p>A lower-pitched version of <samp>fishBite</samp>. Players may
select this sound as their fish bite sound in the <a href="Options"
class="wikilink" title="options menu">options menu</a>.</p></td>
</tr>
<tr>
<td><p><samp>fishBite_alternate_2</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>396</samp></p></td>
<td data-sort-value="396"><p><samp>0000018c</samp></p></td>
<td><p>A more watery version of <samp>fishBite</samp>. Players may
select this sound as their fish bite sound in the <a href="Options"
class="wikilink" title="options menu">options menu</a>.</p></td>
</tr>
<tr>
<td><p><samp>fishEscape</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>253</samp></p></td>
<td data-sort-value="253"><p><samp>000000fd</samp></p></td>
<td><p>A disappointing echo-y sound. Plays when fish escape during the
fishing minigame.</p></td>
</tr>
<tr>
<td><p><samp>FishHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>251</samp></p></td>
<td data-sort-value="251"><p><samp>000000fb</samp></p></td>
<td><p>A "ding". Plays when the player successfully hooks a fish and the
fishing minigame starts.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>fishingRodBend</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>254</samp></p></td>
<td data-sort-value="254"><p><samp>000000fe</samp></p></td>
<td rowspan="3"><p>A creaking noise. Plays during the fishing minigame
when the player clicks.</p></td>
</tr>
<tr>
<td><p><samp>255</samp></p></td>
<td data-sort-value="255"><p><samp>000000ff</samp></p></td>
</tr>
<tr>
<td><p><samp>256</samp></p></td>
<td data-sort-value="256"><p><samp>00000100</samp></p></td>
</tr>
<tr>
<td><p><samp>fishSlap</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>260</samp></p></td>
<td data-sort-value="260"><p><samp>00000104</samp></p></td>
<td><p>A wet squelching noise. Plays when <a href="Fish_Pond"
class="wikilink" title="Fish Ponds">Fish Ponds</a> are emptied, after
the player catches a fish, and when the <a href="Bait_Maker"
class="wikilink" title="Bait Maker">Bait Maker</a> is
processing.</p></td>
</tr>
<tr>
<td><p><samp>flameSpell</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>150</samp></p></td>
<td data-sort-value="150"><p><samp>00000096</samp></p></td>
<td><p>The sound of fire roaring and a spell casting. Used in several
events, including <a href="Sebastian#Six_Hearts" class="wikilink"
title="Sebastian&#39;s 6-heart event">Sebastian's 6-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>flameSpellHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>149</samp></p></td>
<td data-sort-value="149"><p><samp>00000095</samp></p></td>
<td><p>The sound of a fireball colliding with something. Used in several
events, including <a href="Sebastian#Six_Hearts" class="wikilink"
title="Sebastian&#39;s 6-heart event">Sebastian's 6-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>flute</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>112</samp></p></td>
<td data-sort-value="112"><p><samp>00000070</samp></p></td>
<td><p>A flute playing a single tone. Used by <a href="Flute_Block"
class="wikilink" title="Flute Blocks">Flute Blocks</a>.</p></td>
</tr>
<tr>
<td><p><samp>flybuzzing</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>164</samp></p></td>
<td data-sort-value="164"><p><samp>000000a4</samp></p></td>
<td><p>The sound of insect wings buzzing. Used by flying insects such as
the <a href="Cave_Fly" class="wikilink" title="Cave Fly">Cave
Fly</a>.</p></td>
</tr>
<tr>
<td><p><samp>frog_slap</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>422</samp></p></td>
<td data-sort-value="422"><p><samp>000001a6</samp></p></td>
<td><p>A slimey splat. Plays when the frog from the <a href="Frog_Egg"
class="wikilink" title="Frog Egg">Frog Egg</a> trinket hops.</p></td>
</tr>
<tr>
<td><p><samp>frozen</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>394</samp></p></td>
<td data-sort-value="394"><p><samp>0000018a</samp></p></td>
<td><p>The sound of ice quickly forming. Plays when projectiles from the
<a href="Ice_Rod" class="wikilink" title="Ice Rod">Ice Rod</a> hit
enemies.</p></td>
</tr>
<tr>
<td><p><samp>furnace</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>38</samp></p></td>
<td data-sort-value="38"><p><samp>00000026</samp></p></td>
<td><p>The sound of fire roaring. Plays when a <a href="Furnace"
class="wikilink" title="Furnace">Furnace</a> is processing and a <a
href="Pepper_Rex" class="wikilink" title="Pepper Rex">Pepper Rex</a>
breathes fire.</p></td>
</tr>
<tr>
<td><p><samp>fuse</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>48</samp></p></td>
<td data-sort-value="48"><p><samp>00000030</samp></p></td>
<td><p>A fuse hissing. Plays when <a href="Bomb" class="wikilink"
title="bombs">bombs</a> are placed down before they explode.</p></td>
</tr>
<tr>
<td><p><samp>getNewSpecialItem</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>223</samp></p></td>
<td data-sort-value="223"><p><samp>000000df</samp></p></td>
<td><p>A sparkling jingle. Often used in events when the player learns a
new crafting recipe or receives items.</p></td>
</tr>
<tr>
<td><p><samp>ghost</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>11</samp></p></td>
<td data-sort-value="11"><p><samp>0000000b</samp></p></td>
<td><p>A low moan. Plays when <a href="Ghost" class="wikilink"
title="Ghosts">Ghosts</a> and <a href="Mummy" class="wikilink"
title="Mummies">Mummies</a> die.</p></td>
</tr>
<tr>
<td><p><samp>give_gift</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>348</samp></p></td>
<td data-sort-value="348"><p><samp>0000015c</samp></p></td>
<td><p>A short "confirmation" jingle. Plays when the player gives a gift
to an NPC.</p></td>
</tr>
<tr>
<td><p><samp>glug</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>325</samp></p></td>
<td data-sort-value="325"><p><samp>00000145</samp></p></td>
<td><p>The sound of liquid glugging in a bottle. Used when <a
href="Watering_Cans" class="wikilink" title="Watering Cans">Watering
Cans</a> are filled, in several heart events, and in a farmer drinking
animation.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>goat</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>78</samp></p></td>
<td data-sort-value="78"><p><samp>0000004e</samp></p></td>
<td rowspan="2"><p>A <a href="goat" class="wikilink"
title="goat">goat</a> bleating.</p></td>
</tr>
<tr>
<td><p><samp>79</samp></p></td>
<td data-sort-value="79"><p><samp>0000004f</samp></p></td>
</tr>
<tr>
<td><p><samp>goldenWalnut</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>372</samp></p></td>
<td data-sort-value="372"><p><samp>00000174</samp></p></td>
<td><p>A high-pitched wood block jingle. Plays when the player collects
a <a href="Golden_Walnut" class="wikilink" title="Golden Walnut">Golden
Walnut</a>.</p></td>
</tr>
<tr>
<td><p><samp>gorilla_intro</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>388</samp></p></td>
<td data-sort-value="388"><p><samp>00000184</samp></p></td>
<td><p>An ~10 second song of jungle drums, a gorilla snorting, and
various animal noises. Used when the player offers a banana to the <a
href="Banana#Golden_Walnuts" class="wikilink"
title="Gorilla">Gorilla</a> on Ginger Island.</p></td>
</tr>
<tr>
<td><p><samp>grunt</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>12</samp></p></td>
<td data-sort-value="12"><p><samp>0000000c</samp></p></td>
<td><p>A low-pitched grunt. Used as death sounds for several monsters,
when the player offers a banana to the <a href="Banana#Golden_Walnuts"
class="wikilink" title="Gorilla">Gorilla</a> on Ginger Island, and in <a
href="Emily#Ten_Hearts" class="wikilink"
title="Emily&#39;s 10-heart event">Emily's 10-heart event</a>.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>gulp</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>239</samp></p></td>
<td data-sort-value="239"><p><samp>000000ef</samp></p></td>
<td rowspan="2"><p>Loud drinking sounds. Plays when the player
drinks.</p></td>
</tr>
<tr>
<td><p><samp>240</samp></p></td>
<td data-sort-value="240"><p><samp>000000f0</samp></p></td>
</tr>
<tr>
<td><p><samp>hammer</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>134</samp></p></td>
<td data-sort-value="134"><p><samp>00000086</samp></p></td>
<td><p>The dull thud of metal on rock. Plays when various items are
broken by tools in the game.</p></td>
</tr>
<tr>
<td><p><samp>harvest</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>326</samp></p></td>
<td data-sort-value="326"><p><samp>00000146</samp></p></td>
<td><p>A "pop" noise. Plays when crops are harvested, either by the
player or by <a href="Junimo_Hut" class="wikilink"
title="Junimos">Junimos</a>.</p></td>
</tr>
<tr>
<td><p><samp>healSound</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>196</samp></p></td>
<td data-sort-value="196"><p><samp>000000c4</samp></p></td>
<td><p>An ascending regeneration sound. Used by several events, when the
player regenerates health from the <a href="Forge#Enchantments"
class="wikilink" title="Vampiric enchantment">Vampiric enchantment</a>,
and when a <a href="Shadow_Shaman" class="wikilink"
title="Shadow Shaman">Shadow Shaman</a> heals nearby monsters.</p></td>
</tr>
<tr>
<td><p><samp>hitEnemy</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>56</samp></p></td>
<td data-sort-value="56"><p><samp>00000038</samp></p></td>
<td><p>The sound of a weapon swinging combined with a "hit" sound. Used
in a wide variety of situations, such as when the player deals damage to
an enemy.</p></td>
</tr>
<tr>
<td><p><samp>hoeHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>13</samp></p></td>
<td data-sort-value="13"><p><samp>0000000d</samp></p></td>
<td><p>The sound of digging in the dirt. Plays when dirt is tilled with
a <a href="Hoes" class="wikilink" title="Hoe">Hoe</a>.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>horse_flute</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>395</samp></p></td>
<td data-sort-value="395"><p><samp>0000018b</samp></p></td>
<td rowspan="3"><p>A flute playing a short melody. Plays when the <a
href="Horse_Flute" class="wikilink" title="Horse Flute">Horse Flute</a>
is used.</p></td>
</tr>
<tr>
<td><p><samp>401</samp></p></td>
<td data-sort-value="401"><p><samp>00000191</samp></p></td>
</tr>
<tr>
<td><p><samp>402</samp></p></td>
<td data-sort-value="402"><p><samp>00000192</samp></p></td>
</tr>
<tr>
<td><p><samp>jingle1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>252</samp></p></td>
<td data-sort-value="252"><p><samp>000000fc</samp></p></td>
<td><p>A high-pitched "ding". Used when a fish is caught and when
journal or fish pond quests are completed.</p></td>
</tr>
<tr>
<td><p><samp>junimoKart_coin</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>16</samp></p></td>
<td data-sort-value="16"><p><samp>00000010</samp></p></td>
<td><p>A high-pitched, metallic "ding". Plays when the player collects a
coin in <a href="Junimo_Kart" class="wikilink"
title="Junimo Kart">Junimo Kart</a>.</p></td>
</tr>
<tr>
<td><p><samp>junimoMeep1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>306</samp></p></td>
<td data-sort-value="306"><p><samp>00000132</samp></p></td>
<td><p>A high-pitched chirp. Used by <a href="Junimos" class="wikilink"
title="Junimos">Junimos</a>.</p></td>
</tr>
<tr>
<td><p><samp>keyboardTyping</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>293</samp></p></td>
<td data-sort-value="293"><p><samp>00000125</samp></p></td>
<td><p>An ~8 second loop of a mechanical keyboard clacking. Used in <a
href="Sebastian#Two_Hearts" class="wikilink"
title="Sebastian&#39;s 2-heart event">Sebastian's 2-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>killAnimal</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>233</samp></p></td>
<td data-sort-value="233"><p><samp>000000e9</samp></p></td>
<td><p>The gruesome sound of a whoosh and bones crushing. Used only by
<a href="Sebastian#Six_Hearts" class="wikilink"
title="Sebastian&#39;s 6-heart event">Sebastian's 6-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>leafrustle</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>142</samp></p></td>
<td data-sort-value="142"><p><samp>0000008e</samp></p></td>
<td><p>Leaves rustling. Plays when trees are shaken, critters jump into
bushes, bushes are shaken, and more.</p></td>
</tr>
<tr>
<td><p><samp>machine_bell</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>413</samp></p></td>
<td data-sort-value="413"><p><samp>0000019d</samp></p></td>
<td><p>A bell dinging once. Plays when the player claims a prize in the
<a href="Mayor&#39;s_Manor#Prize_Machine" class="wikilink"
title="Prize Machine">Prize Machine</a>.</p></td>
</tr>
<tr>
<td><p><samp>magic_arrow</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>420</samp></p></td>
<td data-sort-value="420"><p><samp>000001a4</samp></p></td>
<td><p>A quick, quiet "whoosh". Plays when the <a href="Magic_Quiver"
class="wikilink" title="Magic Quiver">Magic Quiver</a> fires an
arrow.</p></td>
</tr>
<tr>
<td><p><samp>magic_arrow_hit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>419</samp></p></td>
<td data-sort-value="419"><p><samp>000001a3</samp></p></td>
<td><p>A high-pitched damage sound. Plays when arrows from the <a
href="Magic_Quiver" class="wikilink" title="Magic Quiver">Magic
Quiver</a> hit an enemy.</p></td>
</tr>
<tr>
<td><p><samp>magma_sprite_die</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>380</samp></p></td>
<td data-sort-value="380"><p><samp>0000017c</samp></p></td>
<td><p>A screech combined with fire roaring. Plays when a <a
href="Magma_Sprite" class="wikilink" title="Magma Sprite">Magma
Sprite</a> dies.</p></td>
</tr>
<tr>
<td><p><samp>magma_sprite_hit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>379</samp></p></td>
<td data-sort-value="379"><p><samp>0000017b</samp></p></td>
<td><p>The sound of fire whooshing. Plays when a <a href="Magma_Sprite"
class="wikilink" title="Magma Sprite">Magma Sprite</a> takes
damage.</p></td>
</tr>
<tr>
<td><p><samp>magma_sprite_spot</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>381</samp></p></td>
<td data-sort-value="381"><p><samp>0000017d</samp></p></td>
<td><p>An airy screech. Plays when a <a href="Magma_Sprite"
class="wikilink" title="Magma Sprite">Magma Sprite</a> spots the player
and begins to attack them.</p></td>
</tr>
<tr>
<td><p><samp>metal_tap</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>203</samp></p></td>
<td data-sort-value="203"><p><samp>000000cb</samp></p></td>
<td><p>A high-pitched metal clank. Plays when the player uses an <a
href="Anvil" class="wikilink" title="Anvil">Anvil</a>.</p></td>
</tr>
<tr>
<td><p><samp>Meteorite</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>225</samp></p></td>
<td data-sort-value="225"><p><samp>000000e1</samp></p></td>
<td><p>A whooshing noise. Plays during the <a
href="Random_Events#Meteorite" class="wikilink"
title="Meteorite">Meteorite</a> nighttime event.</p></td>
</tr>
<tr>
<td><p><samp>Milking</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>230</samp></p></td>
<td data-sort-value="230"><p><samp>000000e6</samp></p></td>
<td><p>The sound of liquid filling up a pail. Plays when the <a
href="Milk_Pail" class="wikilink" title="Milk Pail">Milk Pail</a> is
used.</p></td>
</tr>
<tr>
<td><p><samp>minecartLoop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>188</samp></p></td>
<td data-sort-value="188"><p><samp>000000bc</samp></p></td>
<td><p>A high-pitched loop of a minecart on tracks. Used as a sound
effect in <a href="Junimo_Kart" class="wikilink"
title="Junimo Kart">Junimo Kart</a>.</p></td>
</tr>
<tr>
<td><p><samp>miniharp_note</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>5</samp></p></td>
<td data-sort-value="5"><p><samp>00000005</samp></p></td>
<td><p>A harpsichord tone. Used by the "music" <a
href="Multiplayer_Emotes" class="wikilink"
title="multiplayer emote">multiplayer emote</a> and by <a
href="Flute_Block" class="wikilink" title="Flute Blocks">Flute
Blocks</a> when the player is holding an <a href="Amethyst"
class="wikilink" title="Amethyst">Amethyst</a>.</p></td>
</tr>
<tr>
<td><p><samp>money</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>61</samp></p></td>
<td data-sort-value="61"><p><samp>0000003d</samp></p></td>
<td><p>A single "ding". Plays in various situations, such as when the
game saves.</p></td>
</tr>
<tr>
<td><p><samp>moneyDial</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>237</samp></p></td>
<td data-sort-value="237"><p><samp>000000ed</samp></p></td>
<td><p>A high-pitched sound of coins falling. Plays repeatedly on a new
day when the money from the previous day's shipping is added to the
player's farm.</p></td>
</tr>
<tr>
<td><p><samp>monkey1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>385</samp></p></td>
<td data-sort-value="385"><p><samp>00000181</samp></p></td>
<td><p>A monkey chattering. Used by the monkeys in the <a
href="Volcano_Dungeon#Volcano_Caldera" class="wikilink"
title="Volcano Caldera">Volcano Caldera</a>.</p></td>
</tr>
<tr>
<td><p><samp>monsterdead</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>158</samp></p></td>
<td data-sort-value="158"><p><samp>0000009e</samp></p></td>
<td><p>A "splat" noise. Used as a death sound for various
monsters.</p></td>
</tr>
<tr>
<td><p><samp>moss_cut</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>409</samp></p></td>
<td data-sort-value="409"><p><samp>00000199</samp></p></td>
<td><p>A rustling noise. Plays when <a href="Moss" class="wikilink"
title="Moss">Moss</a> is harvested from a tree.</p></td>
</tr>
<tr>
<td><p><samp>mouseClick</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>294</samp></p></td>
<td data-sort-value="294"><p><samp>00000126</samp></p></td>
<td><p>A computer mouse clicking once. Used in <a
href="Sebastian#Two_Hearts" class="wikilink"
title="Sebastian&#39;s 2-heart event">Sebastian's 2-heart
event</a>.</p></td>
</tr>
<tr>
<td><p><samp>newArtifact</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>211</samp></p></td>
<td data-sort-value="211"><p><samp>000000d3</samp></p></td>
<td><p>A low-pitched "ding". Plays when UI messages such as skill
mastery level-ups appear, items are donated to bundles or the museum,
the <a href="Night_Market" class="wikilink" title="Night Market">Night
Market</a> submarine reaches the ocean floor, breaking open a geode
containing common items at the <a href="Blacksmith" class="wikilink"
title="Blacksmith">Blacksmith</a>, and in other menus throughout the
game.</p></td>
</tr>
<tr>
<td><p><samp>newRecipe</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>214</samp></p></td>
<td data-sort-value="214"><p><samp>000000d6</samp></p></td>
<td><p>The sound of a page turning. Plays when the player learns a new
recipe.</p></td>
</tr>
<tr>
<td><p><samp>newRecord</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>213</samp></p></td>
<td data-sort-value="213"><p><samp>000000d5</samp></p></td>
<td><p>A sparkling jingle. Plays when the player catches a fish of
record size and at night when the player levels up in a skill.</p></td>
</tr>
<tr>
<td><p><samp>objectiveComplete</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>132</samp></p></td>
<td data-sort-value="132"><p><samp>00000084</samp></p></td>
<td><p>A rebounding jingly noise. Plays when a <a href="Weapons"
class="wikilink" title="weapon&#39;s">weapon's</a> secondary attack
cooldown is over.</p></td>
</tr>
<tr>
<td><p><samp>openBox</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>14</samp></p></td>
<td data-sort-value="14"><p><samp>0000000e</samp></p></td>
<td><p>The low-pitched sound of a latch opening. Plays in a variety of
situations, including when <a href="Volcano_Dungeon#Gated_Doors"
class="wikilink" title="Pressure Pads">Pressure Pads</a> are activated
in the Volcano Dungeon, when the player interacts with the <a
href="Telephone" class="wikilink" title="Telephone">Telephone</a>, and
when <a href="Desert_Festival#Skull_Cavern" class="wikilink"
title="Calico Statues">Calico Statues</a> are activated.</p></td>
</tr>
<tr>
<td><p><samp>openChest</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>161</samp></p></td>
<td data-sort-value="161"><p><samp>000000a1</samp></p></td>
<td><p>A click and then the creak of hinges. Plays when a <a
href="Chest" class="wikilink" title="Chest">Chest</a> opens.</p></td>
</tr>
<tr>
<td><p><samp>Ostrich</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>367</samp></p></td>
<td data-sort-value="367"><p><samp>0000016f</samp></p></td>
<td><p>An <a href="ostrich" class="wikilink" title="ostrich">ostrich</a>
cooing.</p></td>
</tr>
<tr>
<td><p><samp>ow</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>63</samp></p></td>
<td data-sort-value="63"><p><samp>0000003f</samp></p></td>
<td><p>Plays when the player takes damage.</p></td>
</tr>
<tr>
<td><p><samp>owl</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>227</samp></p></td>
<td data-sort-value="227"><p><samp>000000e3</samp></p></td>
<td><p>An owl hooting. Plays during the <a
href="Random_Events#Stone_Owl" class="wikilink" title="Stone Owl">Stone
Owl</a> nighttime event.</p></td>
</tr>
<tr>
<td><p><samp>parachute</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>414</samp></p></td>
<td data-sort-value="414"><p><samp>0000019e</samp></p></td>
<td><p>The rustling sound of a parachute. Used in the plane fly-by
cutscene that enables the <a href="Mystery_Box" class="wikilink"
title="Mystery Box">Mystery Box</a> mechanic.</p></td>
</tr>
<tr>
<td><p><samp>parrot</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>360</samp></p></td>
<td data-sort-value="360"><p><samp>00000168</samp></p></td>
<td><p>A parrot squawking. Used by the parrots on <a
href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a>.</p></td>
</tr>
<tr>
<td><p><samp>parrot_flap</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>432</samp></p></td>
<td data-sort-value="432"><p><samp>000001b0</samp></p></td>
<td><p>The sound of parrot wings flapping. Used by the parrots on <a
href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a>.</p></td>
</tr>
<tr>
<td><p><samp>parrot_squawk</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>373</samp></p></td>
<td data-sort-value="373"><p><samp>00000175</samp></p></td>
<td><p>A parrot squawking. Used by the parrots on <a
href="Ginger_Island" class="wikilink" title="Ginger Island">Ginger
Island</a>.</p></td>
</tr>
<tr>
<td><p><samp>parry</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>173</samp></p></td>
<td data-sort-value="173"><p><samp>000000ad</samp></p></td>
<td><p>A "clink" noise. Plays when an attack is successfully
parried.</p></td>
</tr>
<tr>
<td><p><samp>phone</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>113</samp></p></td>
<td data-sort-value="113"><p><samp>00000071</samp></p></td>
<td><p>A phone ringing. Plays when the <a href="Telephone"
class="wikilink" title="Telephone">Telephone</a> rings.</p></td>
</tr>
<tr>
<td><p><samp>Pickup_Coin15</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>273</samp></p></td>
<td data-sort-value="273"><p><samp>00000111</samp></p></td>
<td><p>An electronic metallic "ding". Plays when the player collects
coins in <a href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>pickUpItem</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>15</samp></p></td>
<td data-sort-value="15"><p><samp>0000000f</samp></p></td>
<td><p>A "pop" sound. Plays when forageables are picked up.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>pig</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>130</samp></p></td>
<td data-sort-value="130"><p><samp>00000082</samp></p></td>
<td rowspan="2"><p>A <a href="pig" class="wikilink" title="pig">pig</a>
oinking.</p></td>
</tr>
<tr>
<td><p><samp>131</samp></p></td>
<td data-sort-value="131"><p><samp>00000083</samp></p></td>
</tr>
<tr>
<td><p><samp>planeflyby</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>415</samp></p></td>
<td data-sort-value="415"><p><samp>0000019f</samp></p></td>
<td><p>The whirring of a propellor plane. Used in the plane fly-by
cutscene that enables the <a href="Mystery_Box" class="wikilink"
title="Mystery Box">Mystery Box</a> mechanic.</p></td>
</tr>
<tr>
<td><p><samp>potterySmash</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>147</samp></p></td>
<td data-sort-value="147"><p><samp>00000093</samp></p></td>
<td><p>The sound of pottery shattering. Used in the slingshot minigame
at the <a href="Stardew_Valley_Fair" class="wikilink"
title="Stardew Valley Fair">Stardew Valley Fair</a>.</p></td>
</tr>
<tr>
<td><p><samp>powerup</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>39</samp></p></td>
<td data-sort-value="39"><p><samp>00000027</samp></p></td>
<td><p>An ascending sci-fi powerup noise. Plays when the player uses a
powerup in <a href="Journey_of_the_Prairie_King" class="wikilink"
title="Journey of the Prairie King">Journey of the Prairie
King</a>.</p></td>
</tr>
<tr>
<td><p><samp>pullItemFromWater</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>28</samp></p></td>
<td data-sort-value="28"><p><samp>0000001c</samp></p></td>
<td><p>Water splashing. Plays in various situations, such as when the
player starts/stops <a href="Spa" class="wikilink"
title="swimming">swimming</a>, when fish are caught, and more.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>purchase</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>145</samp></p></td>
<td data-sort-value="145"><p><samp>00000091</samp></p></td>
<td rowspan="3"><p>A few coins clinking together. Plays when items are
sold to shops.</p></td>
</tr>
<tr>
<td><p><samp>146</samp></p></td>
<td data-sort-value="146"><p><samp>00000092</samp></p></td>
</tr>
<tr>
<td><p><samp>241</samp></p></td>
<td data-sort-value="241"><p><samp>000000f1</samp></p></td>
</tr>
<tr>
<td><p><samp>purchaseClick</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>146</samp></p></td>
<td data-sort-value="146"><p><samp>00000092</samp></p></td>
<td><p>A slightly higher-pitched version of <samp>purchase</samp>. Plays
when items are bought from shops.</p></td>
</tr>
<tr>
<td><p><samp>purchaseRepeat</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>241</samp></p></td>
<td data-sort-value="241"><p><samp>000000f1</samp></p></td>
<td><p>A slightly higher-pitched version of <samp>purchase</samp>. Plays
when the player buys multiple items from shops in quick
succession.</p></td>
</tr>
<tr>
<td><p><samp>qi_shop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>399</samp></p></td>
<td data-sort-value="399"><p><samp>0000018f</samp></p></td>
<td><p>A sci-fi jingle. Plays when the player opens the shop in <a
href="Qi&#39;s_Walnut_Room" class="wikilink"
title="Qi&#39;s Walnut Room">Qi's Walnut Room</a>.</p></td>
</tr>
<tr>
<td><p><samp>qi_shop_purchase</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>400</samp></p></td>
<td data-sort-value="400"><p><samp>00000190</samp></p></td>
<td><p>Gems clinking together. Plays when the player purchases from the
shop in <a href="Qi&#39;s_Walnut_Room" class="wikilink"
title="Qi&#39;s Walnut Room">Qi's Walnut Room</a>.</p></td>
</tr>
<tr>
<td><p><samp>questcomplete</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>128</samp></p></td>
<td data-sort-value="128"><p><samp>00000080</samp></p></td>
<td><p>An ascending "success" jingle. Plays when the player completes
quests.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>quickSlosh</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>290</samp></p></td>
<td data-sort-value="290"><p><samp>00000122</samp></p></td>
<td rowspan="2"><p>A more subtle variation of the <samp>slosh</samp>
sound cue.</p></td>
</tr>
<tr>
<td><p><samp>291</samp></p></td>
<td data-sort-value="291"><p><samp>00000123</samp></p></td>
</tr>
<tr>
<td><p><samp>rabbit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>74</samp></p></td>
<td data-sort-value="74"><p><samp>0000004a</samp></p></td>
<td><p>A rustling noise used when <a href="Rabbit" class="wikilink"
title="rabbits">rabbits</a> are pet.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>Raccoon</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>424</samp></p></td>
<td data-sort-value="424"><p><samp>000001a8</samp></p></td>
<td rowspan="2"><p>The chittering of a raccoon. Plays when interacting
with the raccoons in the repaired <a
href="Giant_Stump#Raccoon&#39;s_Requests" class="wikilink"
title="Giant Stump">Giant Stump</a>.</p></td>
</tr>
<tr>
<td><p><samp>425</samp></p></td>
<td data-sort-value="425"><p><samp>000001a9</samp></p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>rainsound</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>135</samp></p></td>
<td data-sort-value="135"><p><samp>00000087</samp></p></td>
<td rowspan="3"><p>Various eerie ambient noises that play on <a
href="Weather" class="wikilink" title="rainy">rainy</a> days.</p></td>
</tr>
<tr>
<td><p><samp>136</samp></p></td>
<td data-sort-value="136"><p><samp>00000088</samp></p></td>
</tr>
<tr>
<td><p><samp>137</samp></p></td>
<td data-sort-value="137"><p><samp>00000089</samp></p></td>
</tr>
<tr>
<td><p><samp>reward</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>212</samp></p></td>
<td data-sort-value="212"><p><samp>000000d4</samp></p></td>
<td><p>A sparkling "success" jingle. Plays in various situations, such
as when the player finds a wallet item.</p></td>
</tr>
<tr>
<td><p><samp>robotBLASTOFF</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>287</samp></p></td>
<td data-sort-value="287"><p><samp>0000011f</samp></p></td>
<td><p>A whooshing rocket launch build-up sound.</p></td>
</tr>
<tr>
<td><p><samp>robotSoundEffects</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>286</samp></p></td>
<td data-sort-value="286"><p><samp>0000011e</samp></p></td>
<td><p>Robotic hissing followed by high-pitched beeps.</p></td>
</tr>
<tr>
<td><p><samp>rockGolemDie</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>166</samp></p></td>
<td data-sort-value="166"><p><samp>000000a6</samp></p></td>
<td><p>A high-pitched squeal. Plays when the player kills a <a
href="Stone_Golem" class="wikilink" title="Stone Golem">Stone
Golem</a>.</p></td>
</tr>
<tr>
<td><p><samp>rockGolemHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>167</samp></p></td>
<td data-sort-value="167"><p><samp>000000a7</samp></p></td>
<td><p>A high-pitched grunt. Plays when the player hits a <a
href="Stone_Golem" class="wikilink" title="Stone Golem">Stone
Golem</a>.</p></td>
</tr>
<tr>
<td><p><samp>rockGolemSpawn</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>165</samp></p></td>
<td data-sort-value="165"><p><samp>000000a5</samp></p></td>
<td><p>The sound of rocks tumbling. Plays when a <a href="Stone_Golem"
class="wikilink" title="Stone Golem">Stone Golem</a> appears.</p></td>
</tr>
<tr>
<td><p><samp>rooster</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>329</samp></p></td>
<td data-sort-value="329"><p><samp>00000149</samp></p></td>
<td><p>A rooster crowing. Plays at the start of each day.</p></td>
</tr>
<tr>
<td><p><samp>scissors</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>229</samp></p></td>
<td data-sort-value="229"><p><samp>000000e5</samp></p></td>
<td><p>Scissors snipping. Plays when <a href="Shears" class="wikilink"
title="Shears">Shears</a> are used.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>seagulls</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>176</samp></p></td>
<td data-sort-value="176"><p><samp>000000b0</samp></p></td>
<td rowspan="3"><p>A <a href="Animals#Seagulls" class="wikilink"
title="seagull">seagull</a> squawking.</p></td>
</tr>
<tr>
<td><p><samp>177</samp></p></td>
<td data-sort-value="177"><p><samp>000000b1</samp></p></td>
</tr>
<tr>
<td><p><samp>178</samp></p></td>
<td data-sort-value="178"><p><samp>000000b2</samp></p></td>
</tr>
<tr>
<td><p><samp>secret1</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>218</samp></p></td>
<td data-sort-value="218"><p><samp>000000da</samp></p></td>
<td><p>A mystical chime. Plays when the player discovers various
secrets, such as finding the sweetest taste for <a
href="Old_Master_Cannoli" class="wikilink"
title="Old Master Cannoli">Old Master Cannoli</a>.</p></td>
</tr>
<tr>
<td><p><samp>seeds</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>17</samp></p></td>
<td data-sort-value="17"><p><samp>00000011</samp></p></td>
<td><p>A hollow squelching noise.</p></td>
</tr>
<tr>
<td><p><samp>select</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>148</samp></p></td>
<td data-sort-value="148"><p><samp>00000094</samp></p></td>
<td><p>A high-pitched hollow rising 'pook!' sound. Used as a
click/select sound in many menus (e.g. clicking a button on the title
screen).</p></td>
</tr>
<tr>
<td><p><samp>sell</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>242</samp></p></td>
<td data-sort-value="242"><p><samp>000000f2</samp></p></td>
<td><p>The clink of a single coin. Plays when the player sells an item
to a vendor.</p></td>
</tr>
<tr>
<td><p><samp>serpentDie</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>315</samp></p></td>
<td data-sort-value="315"><p><samp>0000013b</samp></p></td>
<td><p>A synthesized, echoing scream. Plays when a <a href="serpent"
class="wikilink" title="serpent">serpent</a> dies.</p></td>
</tr>
<tr>
<td><p><samp>serpentHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>314</samp></p></td>
<td data-sort-value="314"><p><samp>0000013a</samp></p></td>
<td><p>A single synthy "thud". Plays when the player attacks a <a
href="serpent" class="wikilink" title="serpent">serpent</a>.</p></td>
</tr>
<tr>
<td><p><samp>sewing_loop</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>15</samp></p></td>
<td data-sort-value="15"><p><samp>0000000f</samp></p></td>
<td><p>A looping mechanical click-clack. Plays when the player processes
items through the <a href="Sewing_Machine" class="wikilink"
title="Sewing Machine">Sewing Machine</a>.</p></td>
</tr>
<tr>
<td><p><samp>shadowDie</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>194</samp></p></td>
<td data-sort-value="194"><p><samp>000000c2</samp></p></td>
<td><p>An airy whooshing. Plays when a <a href="Shadow_Brute"
class="wikilink" title="Shadow Brute">Shadow Brute</a> or <a
href="Shadow_Shaman" class="wikilink" title="Shadow Shaman">Shadow
Shaman</a> dies.</p></td>
</tr>
<tr>
<td><p><samp>shadowHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>195</samp></p></td>
<td data-sort-value="195"><p><samp>000000c3</samp></p></td>
<td><p>A single chewy "thwack". Plays when the player attacks a <a
href="Shadow_Brute" class="wikilink" title="Shadow Brute">Shadow
Brute</a> or <a href="Shadow_Shaman" class="wikilink"
title="Shadow Shaman">Shadow Shaman</a>.</p></td>
</tr>
<tr>
<td><p><samp>shadowpeep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>18</samp></p></td>
<td data-sort-value="18"><p><samp>00000012</samp></p></td>
<td><p>A surprised, whale-like mumble. Heard as intermittent ambient
noise from <a href="Shadow_Brute" class="wikilink"
title="Shadow Brute">Shadow Brutes</a> and <a href="Shadow_Shaman"
class="wikilink" title="Shadow Shaman">Shadow Shamans</a>.</p></td>
</tr>
<tr>
<td><p><samp>sheep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>232</samp></p></td>
<td data-sort-value="232"><p><samp>000000e8</samp></p></td>
<td><p>A <a href="sheep" class="wikilink" title="sheep">sheep</a>
bleating.</p></td>
</tr>
<tr>
<td><p><samp>shiny4</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>19</samp></p></td>
<td data-sort-value="19"><p><samp>00000013</samp></p></td>
<td><p>A quiet "drrt" sound. Plays when using the scroll bar.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>Ship</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>96</samp></p></td>
<td data-sort-value="96"><p><samp>00000060</samp></p></td>
<td rowspan="2"><p>The sound of items dropping into a wooden box. Used
in a variety of situations, including when items are dropped into the <a
href="Shipping" class="wikilink" title="Shipping Bin">Shipping
Bin</a>.</p></td>
</tr>
<tr>
<td><p><samp>97</samp></p></td>
<td data-sort-value="97"><p><samp>00000061</samp></p></td>
</tr>
<tr>
<td><p><samp>shwip</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>317</samp></p></td>
<td data-sort-value="317"><p><samp>0000013d</samp></p></td>
<td><p>A swishy sound. Plays when scrolling through certain menus, such
as the <a href="Jukebox" class="wikilink" title="Jukebox">Jukebox</a>
music selection screen.</p></td>
</tr>
<tr>
<td><p><samp>SinWave</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>245</samp></p></td>
<td data-sort-value="245"><p><samp>000000f5</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>sipTea</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>193</samp></p></td>
<td data-sort-value="193"><p><samp>000000c1</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>skeletonDie</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>183</samp></p></td>
<td data-sort-value="183"><p><samp>000000b7</samp></p></td>
<td><p>The Rattle of bones falling. Used when a <a href="skeleton"
class="wikilink" title="skeleton">skeleton</a> dies.</p></td>
</tr>
<tr>
<td><p><samp>skeletonHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>184</samp></p></td>
<td data-sort-value="184"><p><samp>000000b8</samp></p></td>
<td><p>Bones clanking. Used when the player attacks a <a href="skeleton"
class="wikilink" title="skeleton">skeleton</a>.</p></td>
</tr>
<tr>
<td><p><samp>skeletonStep</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>182</samp></p></td>
<td data-sort-value="182"><p><samp>000000b6</samp></p></td>
<td><p>A single soft bony step. Used when <a href="skeleton"
class="wikilink" title="skeletons">skeletons</a> move.</p></td>
</tr>
<tr>
<td><p><samp>slime</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>57</samp></p></td>
<td data-sort-value="57"><p><samp>00000039</samp></p></td>
<td><p>A "boing" noise. Used when <a href="slimes" class="wikilink"
title="slimes">slimes</a> lunge at the player.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>slimedead</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>59</samp></p></td>
<td data-sort-value="59"><p><samp>0000003b</samp></p></td>
<td rowspan="3"><p>A "splat" sound. Used when <a href="slimes"
class="wikilink" title="slimes">slimes</a> die.</p></td>
</tr>
<tr>
<td><p><samp>156</samp></p></td>
<td data-sort-value="156"><p><samp>0000009c</samp></p></td>
</tr>
<tr>
<td><p><samp>157</samp></p></td>
<td data-sort-value="157"><p><samp>0000009d</samp></p></td>
</tr>
<tr>
<td><p><samp>slimeHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>185</samp></p></td>
<td data-sort-value="185"><p><samp>000000b9</samp></p></td>
<td><p>A wet squelching sound. Used when the player attacks a <a
href="Slimes" class="wikilink" title="slime">slime</a>.</p></td>
</tr>
<tr>
<td><p><samp>slingshot</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>207</samp></p></td>
<td data-sort-value="207"><p><samp>000000cf</samp></p></td>
<td><p>The sound of something being drawn tight. Plays when the <a
href="Slingshot" class="wikilink" title="Slingshot">Slingshot</a> is
drawn back.</p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>slosh</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>289</samp></p></td>
<td data-sort-value="289"><p><samp>00000121</samp></p></td>
<td rowspan="3"><p>Water sloshing. Plays in a variety of situations,
including when a <a href="Tools#Pans" class="wikilink"
title="Pan">Pan</a> is used.</p></td>
</tr>
<tr>
<td><p><samp>290</samp></p></td>
<td data-sort-value="290"><p><samp>00000122</samp></p></td>
</tr>
<tr>
<td><p><samp>291</samp></p></td>
<td data-sort-value="291"><p><samp>00000123</samp></p></td>
</tr>
<tr>
<td><p><samp>slowReel</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>247</samp></p></td>
<td data-sort-value="247"><p><samp>000000f7</samp></p></td>
<td><p>The sound of a fishing rod reeling. Plays when the fishing bar is
no longer behind the fish in the fishing minigame.</p></td>
</tr>
<tr>
<td><p><samp>smallSelect</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>20</samp></p></td>
<td data-sort-value="20"><p><samp>00000014</samp></p></td>
<td><p>A shorter variant of the <samp>select</samp> sound cue. Used as a
click/select sound in many menus (e.g. clicking through to the next
dialogue box).</p></td>
</tr>
<tr>
<td rowspan="5"><p><samp>SpringBirds</samp></p></td>
<td rowspan="5"><p><samp>Wavebank</samp></p></td>
<td><p><samp>86</samp></p></td>
<td data-sort-value="86"><p><samp>00000056</samp></p></td>
<td rowspan="5"><p>A bird chirping. Used as ambient noise.</p></td>
</tr>
<tr>
<td><p><samp>87</samp></p></td>
<td data-sort-value="87"><p><samp>00000057</samp></p></td>
</tr>
<tr>
<td><p><samp>88</samp></p></td>
<td data-sort-value="88"><p><samp>00000058</samp></p></td>
</tr>
<tr>
<td><p><samp>89</samp></p></td>
<td data-sort-value="89"><p><samp>00000059</samp></p></td>
</tr>
<tr>
<td><p><samp>90</samp></p></td>
<td data-sort-value="90"><p><samp>0000005a</samp></p></td>
</tr>
<tr>
<td><p><samp>squid_bubble</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>392</samp></p></td>
<td data-sort-value="392"><p><samp>00000188</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>squid_hit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>393</samp></p></td>
<td data-sort-value="393"><p><samp>00000189</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>squid_move</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>391</samp></p></td>
<td data-sort-value="391"><p><samp>00000187</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>Stadium_cheer</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>355</samp></p></td>
<td data-sort-value="355"><p><samp>00000163</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>stairsdown</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>313</samp></p></td>
<td data-sort-value="313"><p><samp>00000139</samp></p></td>
<td><p>The sound of footsteps descending. Plays when the player descends
ladders.</p></td>
</tr>
<tr>
<td><p><samp>stardrop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>351</samp></p></td>
<td data-sort-value="351"><p><samp>0000015f</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>statue_of_blessings</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>417</samp></p></td>
<td data-sort-value="417"><p><samp>000001a1</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>steam</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>378</samp></p></td>
<td data-sort-value="378"><p><samp>0000017a</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>stone_button</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>418</samp></p></td>
<td data-sort-value="418"><p><samp>000001a2</samp></p></td>
<td></td>
</tr>
<tr>
<td rowspan="2"><p><samp>stoneCrack</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>75</samp></p></td>
<td data-sort-value="75"><p><samp>0000004b</samp></p></td>
<td rowspan="2"></td>
</tr>
<tr>
<td><p><samp>76</samp></p></td>
<td data-sort-value="76"><p><samp>0000004c</samp></p></td>
</tr>
<tr>
<td><p><samp>stumpCrack</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>217</samp></p></td>
<td data-sort-value="217"><p><samp>000000d9</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>submarine_landing</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>365</samp></p></td>
<td data-sort-value="365"><p><samp>0000016d</samp></p></td>
<td></td>
</tr>
<tr>
<td rowspan="2"><p><samp>swordswipe</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>58</samp></p></td>
<td data-sort-value="58"><p><samp>0000003a</samp></p></td>
<td rowspan="2"></td>
</tr>
<tr>
<td><p><samp>162</samp></p></td>
<td data-sort-value="162"><p><samp>000000a2</samp></p></td>
</tr>
<tr>
<td><p><samp>telephone_buttonPush</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>369</samp></p></td>
<td data-sort-value="369"><p><samp>00000171</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>telephone_dialtone</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>370</samp></p></td>
<td data-sort-value="370"><p><samp>00000172</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>telephone_ringingInEar</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>368</samp></p></td>
<td data-sort-value="368"><p><samp>00000170</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>terraria_boneSerpent</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>407</samp></p></td>
<td data-sort-value="407"><p><samp>00000197</samp></p></td>
<td></td>
</tr>
<tr>
<td rowspan="2"><p><samp>terraria_meowmere</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>405</samp></p></td>
<td data-sort-value="405"><p><samp>00000195</samp></p></td>
<td rowspan="2"></td>
</tr>
<tr>
<td><p><samp>406</samp></p></td>
<td data-sort-value="406"><p><samp>00000196</samp></p></td>
</tr>
<tr>
<td><p><samp>terraria_warp</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>404</samp></p></td>
<td data-sort-value="404"><p><samp>00000194</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>throw</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>187</samp></p></td>
<td data-sort-value="187"><p><samp>000000bb</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>throwDownITem</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>21</samp></p></td>
<td data-sort-value="21"><p><samp>00000015</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>thunder</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>114</samp></p></td>
<td data-sort-value="114"><p><samp>00000072</samp></p></td>
<td><p>A loud thunderclap.</p></td>
</tr>
<tr>
<td rowspan="2"><p><samp>thunder_small</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>327</samp></p></td>
<td data-sort-value="327"><p><samp>00000147</samp></p></td>
<td rowspan="2"><p>Thunder rumbling.</p></td>
</tr>
<tr>
<td><p><samp>328</samp></p></td>
<td data-sort-value="328"><p><samp>00000148</samp></p></td>
</tr>
<tr>
<td><p><samp>ticket_machine_whir</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>410</samp></p></td>
<td data-sort-value="410"><p><samp>0000019a</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>tinyWhip</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>249</samp></p></td>
<td data-sort-value="249"><p><samp>000000f9</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>toolCharge</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>62</samp></p></td>
<td data-sort-value="62"><p><samp>0000003e</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>toolSwap</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>27</samp></p></td>
<td data-sort-value="27"><p><samp>0000001b</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>toyPiano</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>181</samp></p></td>
<td data-sort-value="181"><p><samp>000000b5</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>trainLoop</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>222</samp></p></td>
<td data-sort-value="222"><p><samp>000000de</samp></p></td>
<td><p>A loop of a train clacking on the tracks.</p></td>
</tr>
<tr>
<td><p><samp>trainWhistle</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>219</samp></p></td>
<td data-sort-value="219"><p><samp>000000db</samp></p></td>
<td><p>A short train whistle.</p></td>
</tr>
<tr>
<td><p><samp>trashbear</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>25</samp></p></td>
<td data-sort-value="25"><p><samp>00000019</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>trashbear_flute</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>24</samp></p></td>
<td data-sort-value="24"><p><samp>00000018</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>trashcan</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>209</samp></p></td>
<td data-sort-value="209"><p><samp>000000d1</samp></p></td>
<td><p>The sound of wrappers rustling. Plays when the player rustles
through the <a href="Garbage_Can" class="wikilink"
title="Garbage Cans">Garbage Cans</a> around town.</p></td>
</tr>
<tr>
<td><p><samp>trashcanlid</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>210</samp></p></td>
<td data-sort-value="210"><p><samp>000000d2</samp></p></td>
<td><p>The sound of metal hinges creaking. Plays when the player hovers
the <a href="Trash_Cans" class="wikilink" title="Trash Can">Trash
Can</a> in their inventory menu and when the <a href="Bus_Stop"
class="wikilink" title="Bus">Bus</a> door closes before it drives
off.</p></td>
</tr>
<tr>
<td><p><samp>treasure_totem</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>416</samp></p></td>
<td data-sort-value="416"><p><samp>000001a0</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>treecrack</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>140</samp></p></td>
<td data-sort-value="140"><p><samp>0000008c</samp></p></td>
<td><p>A cracking noise. Plays right as the animation of a tree falling
starts.</p></td>
</tr>
<tr>
<td><p><samp>treethud</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>139</samp></p></td>
<td data-sort-value="139"><p><samp>0000008b</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>turtle_pet</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>430</samp></p></td>
<td data-sort-value="430"><p><samp>000001ae</samp></p></td>
<td><p>A low chirping noise. The sound of the <a href="Animals#Turtle"
class="wikilink" title="Turtle">Turtle</a> pet.</p></td>
</tr>
<tr>
<td><p><samp>UFO</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>226</samp></p></td>
<td data-sort-value="226"><p><samp>000000e2</samp></p></td>
<td><p>A sci-fi humming sound. Plays during the <a
href="Random_Events#Strange_Capsule" class="wikilink"
title="Strange Capsule">Strange Capsule</a> nighttime event.</p></td>
</tr>
<tr>
<td><p><samp>wand</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>118</samp></p></td>
<td data-sort-value="118"><p><samp>00000076</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>warrior</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>206</samp></p></td>
<td data-sort-value="206"><p><samp>000000ce</samp></p></td>
<td></td>
</tr>
<tr>
<td rowspan="3"><p><samp>wateringCan</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>153</samp></p></td>
<td data-sort-value="153"><p><samp>00000099</samp></p></td>
<td rowspan="3"><p>Water pouring. Plays when the <a href="Watering_Can"
class="wikilink" title="Watering Can">Watering Can</a> is used.</p></td>
</tr>
<tr>
<td><p><samp>154</samp></p></td>
<td data-sort-value="154"><p><samp>0000009a</samp></p></td>
</tr>
<tr>
<td><p><samp>155</samp></p></td>
<td data-sort-value="155"><p><samp>0000009b</samp></p></td>
</tr>
<tr>
<td rowspan="3"><p><samp>waterSlosh</samp></p></td>
<td rowspan="3"><p><samp>Wavebank</samp></p></td>
<td><p><samp>257</samp></p></td>
<td data-sort-value="257"><p><samp>00000101</samp></p></td>
<td rowspan="3"><p>A sloshing sound. Plays when both water and lava
slosh.</p></td>
</tr>
<tr>
<td><p><samp>258</samp></p></td>
<td data-sort-value="258"><p><samp>00000102</samp></p></td>
</tr>
<tr>
<td><p><samp>259</samp></p></td>
<td data-sort-value="259"><p><samp>00000103</samp></p></td>
</tr>
<tr>
<td><p><samp>weed_cut</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>408</samp></p></td>
<td data-sort-value="408"><p><samp>00000198</samp></p></td>
<td><p>A rustling noise. Plays when weeds are cut down.</p></td>
</tr>
<tr>
<td><p><samp>whistle</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>298</samp></p></td>
<td data-sort-value="298"><p><samp>0000012a</samp></p></td>
<td><p>A sports referee-style whistle. Plays at the end of the fishing
and target minigames at the <a href="Stardew_Valley_Fair"
class="wikilink" title="Stardew Valley Fair">Stardew Valley
Fair</a>.</p></td>
</tr>
<tr>
<td><p><samp>windstorm</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>426</samp></p></td>
<td data-sort-value="426"><p><samp>000001aa</samp></p></td>
<td><p>The sound of the wind howling and then a tree cracking. Plays
during the windstorm nighttime event.</p></td>
</tr>
<tr>
<td><p><samp>woodchipper</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>18</samp></p></td>
<td data-sort-value="18"><p><samp>00000012</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>woodchipper_occasional</samp></p></td>
<td><p><samp>Wavebank(1.4)</samp></p></td>
<td><p><samp>19</samp></p></td>
<td data-sort-value="19"><p><samp>00000013</samp></p></td>
<td></td>
</tr>
<tr>
<td rowspan="2"><p><samp>woodWhack</samp></p></td>
<td rowspan="2"><p><samp>Wavebank</samp></p></td>
<td><p><samp>311</samp></p></td>
<td data-sort-value="311"><p><samp>00000137</samp></p></td>
<td rowspan="2"></td>
</tr>
<tr>
<td><p><samp>312</samp></p></td>
<td data-sort-value="312"><p><samp>00000138</samp></p></td>
</tr>
<tr>
<td><p><samp>woodyHit</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>77</samp></p></td>
<td data-sort-value="77"><p><samp>0000004d</samp></p></td>
<td></td>
</tr>
<tr>
<td><p><samp>yoba</samp></p></td>
<td><p><samp>Wavebank</samp></p></td>
<td><p><samp>202</samp></p></td>
<td data-sort-value="202"><p><samp>000000ca</samp></p></td>
<td><p>A sparkling noise. Plays when the <a
href="Statue_Of_Blessings#Blessing_Of_The_Butterfly" class="wikilink"
title="Prismatic Butterfly">Prismatic Butterfly</a> is found and when <a
href="Fairy_Dust" class="wikilink" title="Fairy Dust">Fairy Dust</a> is
used.</p></td>
</tr>
</tbody>
</table>

## Manage audio in C#

### Playing sounds

The game mostly handles sound effects through the `Game1.sounds` field.
This has low-level methods like `PlayLocal`, `PlayAll`,
`GetVolumeForDistance`, etc.

However, you should rarely call `Game1.sounds` directly. Instead the
game has four main methods for playing a sound effect:

<table>
<thead>
<tr>
<th><p>method</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Game1.playSound</samp></p></td>
<td><p>Play a sound for the current player only, which isn't synced in
multiplayer and isn't affected by location or distance. This is mainly
used for UI and menu sounds.</p>
<p>For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">// for UI elements (e.g. crafting an item)</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>Game1<span class="op">.</span><span class="fu">playSound</span><span class="op">(</span><span class="st">&quot;crafting&quot;</span><span class="op">);</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>GameLocation.localSound</samp><br />
<samp>GameLocation.playSound</samp></p></td>
<td><p>Play a sound for the current player (<samp>localSound</samp>) or
all players (<samp>playSound</samp>) if they're in this location.</p>
<p>You can optionally specify...</p>
<ul>
<li>a tile position (which attenuates volume for each player based on
their distance from the sound's source);</li>
<li>and/or pitch (from 0 to 2400 with intervals of 100 between every
half step, where 1200 is the default pitch).</li>
</ul>
<p>For example:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">// play sound for the current player if they&#39;re anywhere on the farm</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>Game1<span class="op">.</span><span class="fu">getFarm</span><span class="op">().</span><span class="fu">localSound</span><span class="op">(</span><span class="st">&quot;doorCreak&quot;</span><span class="op">);</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="co">// play sound for the current player if they&#39;re on the farm near the mailbox (fading with distance)</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>Farm farm <span class="op">=</span> Game1<span class="op">.</span><span class="fu">getFarm</span><span class="op">();</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>farm<span class="op">.</span><span class="fu">localSound</span><span class="op">(</span><span class="st">&quot;doorCreak&quot;</span><span class="op">,</span> farm<span class="op">.</span><span class="fu">GetMainMailboxPosition</span><span class="op">());</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="co">// play sound for all players on the farm near the mailbox (fading with distance), with a -200 pitch shift</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>Farm farm <span class="op">=</span> Game1<span class="op">.</span><span class="fu">getFarm</span><span class="op">();</span></span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>farm<span class="op">.</span><span class="fu">playSound</span><span class="op">(</span><span class="st">&quot;doorCreak&quot;</span><span class="op">,</span> farm<span class="op">.</span><span class="fu">GetMainMailboxPosition</span><span class="op">(),</span> <span class="dv">1000</span><span class="op">);</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>DelayedAction.playSoundAfterDelay</samp></p></td>
<td><p>Play a sound for the current or all players after a specified
delay in milliseconds. You can optionally specify a location, tile
position, and pitch (which works the same way as the
<samp>GameLocation</samp> methods). You can call this method repeatedly
to play multiple sounds (e.g. for a sequence of sounds with different
delays).</p>
<p>For example:</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="co">// play sound for the current player after 1.5 seconds, no matter where they are</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>DelayedAction<span class="op">.</span><span class="fu">playSoundAfterDelay</span><span class="op">(</span><span class="st">&quot;thunder_small&quot;</span><span class="op">,</span> <span class="dv">1500</span><span class="op">);</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="co">// play sound for all players on the farm after 1.5 seconds, fading with distance from the mailbox</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>Farm farm <span class="op">=</span> Game1<span class="op">.</span><span class="fu">getFarm</span><span class="op">();</span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>DelayedAction<span class="op">.</span><span class="fu">playSoundAfterDelay</span><span class="op">(</span><span class="st">&quot;doorCreak&quot;</span><span class="op">,</span> farm<span class="op">,</span> farm<span class="op">.</span><span class="fu">GetMainMailboxPosition</span><span class="op">());</span></span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a><span class="co">// play sound for the current player only if they&#39;rte on the farm after 1.5 seconds, fading with distance from the mailbox</span></span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a>Farm farm <span class="op">=</span> Game1<span class="op">.</span><span class="fu">getFarm</span><span class="op">();</span></span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a>DelayedAction<span class="op">.</span><span class="fu">playSoundAfterDelay</span><span class="op">(</span><span class="st">&quot;doorCreak&quot;</span><span class="op">,</span> farm<span class="op">,</span> farm<span class="op">.</span><span class="fu">GetMainMailboxPosition</span><span class="op">(),</span> local<span class="op">:</span> <span class="kw">true</span><span class="op">);</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

### Add/Edit Audio

To add or edit audio data in C#, you'll need to use SMAPI Content Events
to <a href="Modding_Modder_Guide_APIs_Content#Edit_a_game_asset"
class="wikilink" title="edit a game asset">edit a game asset</a>. The
expected type for the dictionary should be
`IDictionary<string, AudioCueData>`.

You can then add or edit entries in the loaded content, referencing the
<a href="#Data_format" class="wikilink" title="data format">data
format</a> above.

File paths can be specified by using `Path.Combine`.

Example:

``` c#
List<string> paths = [
    Path.Combine(helper.DirectoryPath, "assets", fileName)
];
```

## See also

- The
  <a href="Soundtrack" class="wikilink" title="Soundtrack">Soundtrack</a>
  page for additional information about where many music tracks are used
  in-game.
- From the modding tutorial wiki:
  - [Content Patcher Snippets for
    Music](https://stardewmodding.wiki.gg/wiki/Content_Patcher_Snippets_for_1.6#Music)
  - [Adding Custom
    Music](https://stardewmodding.wiki.gg/wiki/Tutorial:_Adding_Custom_Music)

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Аудио" class="wikilink"
title="ru:Модификации:Аудио">ru:Модификации:Аудио</a>
<a href="zh_模组_音频" class="wikilink"
title="zh:模组:音频">zh:模组:音频</a>
