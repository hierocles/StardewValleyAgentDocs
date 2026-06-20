---
title: "Audio And Visual"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, audio-and-visual-effects]
---
### Audio and visual effects

#### Animations

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
<td><p><samp>animationpreviewtool</samp><br />
<samp>apt</samp></p></td>
<td><p>| Opens a menu allowing you to preview different farmer
animations and change some appearance options. Useful for event modding.
A note that this <em>Only</em> works on the farmer. <strong>Warning:
previewing the "passOutTired" animation will make your farmer pass out
as if it's 2 am and start a new day.</strong></p></td>
<td><p>|<a href="#animationpreviewtool" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>busdriveback</samp></p></td>
<td><p>| Plays the animation of the bus returning from the desert. Must
be done on the Bus Stop map.</p></td>
<td><p>|<a href="#busdriveback" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>busdriveoff</samp></p></td>
<td><p>| Plays the animation of the bus leaving the Bus Stop and driving
to the desert. Will warp the player to the desert. Must be done on the
Bus Stop map.</p></td>
<td><p>|<a href="#busdriveoff" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>createsplash</samp></p></td>
<td><p>| Creates a fish "bubble" spot in front of the player. Seems
inconsistent.</p></td>
<td><p>|<a href="#createsplash" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>framebyframe</samp><br />
<samp>fbf</samp></p></td>
<td><p>| Turns on "frame-by-frame" mode which pauses the game and allows
you to advance time/animations one frame at a time by hitting the
<samp>G</samp> key. Hit <samp>Escape</samp> key to exit.</p></td>
<td><p>|<a href="#framebyframe" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>frameoffset</samp><br />
<samp>fo</samp></p></td>
<td><p>| <em>Syntax</em>: <code>frameoffset</code>
&lt;I:frameID&gt;,&lt;S:X&gt;,&lt;S:Y&gt;,&lt;S:??&gt;</p>
<p>Sets frame offset for specified frame and specified X &amp; Y values.
The X and Y can be made negative to flip the direction. Details unknown;
reference <samp>FarmerRenderer.featureXOffsetPerFrame()</samp> and
<samp>FarmerRenderer.featureYOffsetPerFrame()</samp>.</p></td>
<td><p>|<a href="#frameoffset" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setframe</samp><br />
<samp>sf</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setframe</code> &lt;I:frameID&gt;</p>
<p>Sets farmer sprite to the given animation frame. Probably best used
in conjunction with <a href="#framebyframe" class="wikilink"
title="frame-by-frame mode">frame-by-frame mode</a>.</p></td>
<td><p>|<a href="#setframe" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>sprinkle</samp></p></td>
<td><p>| Shows an animation of a sprinkle effect around the farmer.
(It's the animation used while fairy-dusting a machine).</p></td>
<td><p>|<a href="#sprinkle" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>toss</samp></p></td>
<td><p>| Shows an animation of a spinning vial/beaker which rises and
then falls. Likely used in one of Maru's heart events.</p></td>
<td><p>|<a href="#toss" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Camera, lighting, and effects

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
<td><p><samp>ambientlight</samp><br />
<samp>al</samp></p></td>
<td><p>| <em>Syntax</em>: <code>ambientlight</code>
&lt;I:R&gt;,&lt;I:G&gt;,&lt;I:B&gt;</p>
<p>Sets the ambient light of the current location to the inverse of the
specified RGB values. This is a temporary change and the light will
revert if the location is reset or re-entered. Ex. inputting <samp>255 0
0</samp> will set the lighting to aqua blue, <samp>0 255 255,</samp>
rather than red.</p></td>
<td><p>|<a href="#ambientlight" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>panmode</samp><br />
<samp>pm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>panmode</code> [options]</p>
<p>Turns on panmode. During panmode the screen can be panned with
movement keys or mouse movements and <samp>debug panmode</samp> or
<samp>debug exit</samp> will turn panmode off. You can also clear with
&lt;sampe&gt;debug panMode clear</samp> or set a time with <samp>debug
panMode {time}</samp>. <strong>Warning: Do not enter the backroom of
Willy's shop while in this state as it will crash your
game.</strong></p></td>
<td><p>|<a href="#panmode" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>tls</samp><br />
<samp>toggleLightingScale</samp></p></td>
<td><p>| Toggles between scaled and unscaled lighting.</p></td>
<td><p>|<a href="#tls" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>viewport</samp></p></td>
<td><p>| <em>Syntax</em>: <code>viewport</code>
&lt;I:X&gt;,&lt;I:Y&gt;</p>
<p>Sets the viewport to the given values measured in tiles. Details
unknown.</p></td>
<td><p>|<a href="#viewport" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>uiscale</samp><br />
<samp>us</samp></p></td>
<td><p>| <em>Syntax</em>: <code>uiscale</code> &lt;I:value&gt;</p>
<p>Sets the UI Scale level to the specified value. This is an integer
interpreted as the scale percent. Can be used to go beyond the normal
limits of 75 - 125 percent.</p>
<p><em>Example:</em> <code>debug us 60</code> would set the UI scale
level to 60%.</p></td>
<td><p>|<a href="#uiscale" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>zoomlevel</samp><br />
<samp>zl</samp></p></td>
<td><p>| <em>Syntax</em>: <code>zoomlevel</code> &lt;I:value&gt;</p>
<p>Sets the game zoom level to the specified value. This is an integer
interpreted as the zoom percent. Can be used to go beyond the normal
limits of 75 - 125 percent.</p>
<p><em>Example:</em> <code>debug zl 60</code> would set the zoom level
to 60%.</p></td>
<td><p>|<a href="#zoomlevel" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Audio

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
<td><p><samp>playmusic</samp></p></td>
<td><p>| <em>Syntax</em>: <code>playmusic</code> &lt;s:cueID&gt;</p>
<p>Stops any current music and starts the specified <a
href="Modding_Audio#Track_list" class="wikilink"
title="music track cue ID">music track cue ID</a>. If the cue ID has a
space, you can quote the ID like <code>playMusic "Crystal Bells"</code>.
Tracks played this way will be added to the <a href="Jukebox"
class="wikilink" title="Jukebox">Jukebox</a> list if applicable.</p>
<p><em>Example:</em> <code>debug playmusic spring2</code> would play the
track <em>Spring (The Valley Comes Alive)</em>.</p></td>
<td><p>|<a href="#playmusic" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>playsound</samp><br />
<samp>ps</samp></p></td>
<td><p>| <em>Syntax</em>: <code>playsound</code>
&lt;s:cueID&gt;,&lt;I:pitch&gt;</p>
<p>Playes the specified <a href="Modding_Audio#Track_list"
class="wikilink" title="sound effect cue ID">sound effect cue ID</a>.
The pitch argument is optional and can take values from 1 (low pitch) to
2400 (high pitch) inclusively.</p>
<p><em>Example:</em> <code>debug ps purchase</code> would make the coin
clink sound heard when buying and selling items.</p></td>
<td><p>|<a href="#playsound" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
