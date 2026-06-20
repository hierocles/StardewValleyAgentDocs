---
title: "Jukebox Tracks"
wiki_source: "Modding:Jukebox tracks"
permalink: /Modding:Jukebox_tracks/
category: game
tags: [jukebox-tracks, format]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page describes how the game stores and parses
<a href="The_Stardrop_Saloon#Jukebox" class="wikilink"
title="jukebox">jukebox</a> tracks. This is an advanced guide for mod
developers.

## Format

<a href="The_Stardrop_Saloon#Jukebox" class="wikilink"
title="Jukebox">Jukebox</a> audio tracks can be changed by editing the
`Data/JukeboxTracks` data asset.

This consists of a string → model lookup, where...

- The key is the
  <a href="Modding_Audio" class="wikilink" title="audio cue ID">audio cue
  ID</a> to play (case-sensitive).
- The value is a model with the fields listed below.

If the player has heard a music track not listed in
`Data/JukeboxTracks`, it's automatically available with the title set to
the cue name. To disable a track, add an entry with
`"Available": false`.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Name</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the music track's in-game title. Defaults to the ID.</p></td>
</tr>
<tr>
<td><p><samp>Available</samp></p></td>
<td><p><em>(Optional)</em> Whether the track should be shown in the
jukebox menu. This can be <samp>true</samp> (always shown),
<samp>false</samp> (never shown), or <samp>null</samp> (show if the
player has heard it before). Default <samp>null</samp>.</p>
<p>Tracks with <samp>"Available": true</samp> are listed first in the
jukebox menu.</p></td>
</tr>
<tr>
<td><p><samp>AlternativeTrackIds</samp></p></td>
<td><p><em>(Optional)</em> A list of other cue names for this audio
track (not case-sensitive). If the player has heard any of these track
IDs, this entry is available in the menu. Default none.</p>
<p>For example, this can be used when renaming a track to keep it
unlocked for existing players:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;_TrackName&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Name&quot;</span><span class="fu">:</span> <span class="st">&quot;&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;AlternativeTrackIds&quot;</span><span class="fu">:</span> <span class="ot">[</span> <span class="st">&quot;OldTrackName&quot;</span> <span class="ot">]</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Музыкальный_автомат" class="wikilink"
title="ru:Модификации:Музыкальный автомат">ru:Модификации:Музыкальный
автомат</a> <a href="zh_模组_点唱机音乐" class="wikilink"
title="zh:模组:点唱机音乐">zh:模组:点唱机音乐</a>
