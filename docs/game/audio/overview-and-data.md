---
title: "Overview And Data"
wiki_source: "Modding:Audio"
permalink: /Modding:Audio/
category: game
tags: [audio, overview, audio-data, data-format, category-list, audio-file-format, example, review-audio]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how to use and edit the game's music tracks and sound
effects (called *cues*). This is an advanced guide for modders.

## Overview

'Audio' covers both sound effects (like the *boop* sound when clicking a
button) and music tracks. An audio track or sound effect is called a
*cue*, which may have multiple audio files to randomize which one plays
each time the cue starts.

The game loads its initial cues from the `Content/XACT` folder (which
can't be edited directly), and then adds/edits cues based on the
<a href="#Audio_data" class="wikilink" title="audio data">audio data</a>
(which can be edited through Content Patcher or SMAPI).

Sound effects are played by
<a href="#Track_list" class="wikilink" title="audio cue ID">audio cue
ID</a>, while music is selected using this priority list:

1.  specific
    <a href="#Track_list" class="wikilink" title="audio cue IDs">audio cue
    IDs</a> in some cases (e.g. `MainTheme` on the title screen);
2.  music data in <a href="Modding_Location_data" class="wikilink"
    title="Data/Locations"><samp>Data/Locations</samp></a>;
3.  the `Music`
    <a href="Modding_Maps" class="wikilink" title="map property">map
    property</a> (deprecated);
4.  music data in `Data/LocationContexts`.

## Audio data

You can add or edit cues by editing the `Data/AudioChanges` asset. New
cues are added to the game's soundbank, so they can be used anywhere
normal audio can be used (e.g. the `Music`
<a href="Modding_Maps" class="wikilink" title="map property">map
property</a>).

### Data format

The `Data/AudioChanges` asset consists of a string → model lookup, where
the key matches the `ID`, and the value is a model with the fields
below.

Entries in this asset describe an **override** applied to the soundbank.
The override is applied permanently for the current game session, even
if the asset is edited to remove it. Overriding a cue will reset all
values to the ones specified.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ID</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for the
audio cue, used when playing the sound in-game.</p></td>
</tr>
<tr>
<td><p><samp>FilePaths</samp></p></td>
<td><p>A list of absolute file paths (not asset names) from which to
load the audio. Each file can be <samp>.ogg</samp> or <samp>.wav</samp>.
If you list multiple paths, a random one will be chosen each time it's
played.</p></td>
</tr>
<tr>
<td><p><samp>Category</samp></p></td>
<td><p>The <a href="#Category_list" class="wikilink"
title="audio category">audio category</a>, which determines which volume
slider in the game options applies. This should be one of
<samp>Default</samp>, <samp>Music</samp>, <samp>Sound</samp>,
<samp>Ambient</samp>, or <samp>Footsteps</samp> (see <a
href="#Category_list" class="wikilink"
title="a description of each category">a description of each
category</a>). Defaults to <samp>Default</samp>.</p></td>
</tr>
<tr>
<td><p><samp>StreamedVorbis</samp></p></td>
<td><p>Whether the audio should be streamed from disk when it's played,
instead of being loaded into memory ahead of time. This is only possible
for <a href="wikipedia_Vorbis" class="wikilink" title="Ogg Vorbis">Ogg
Vorbis</a> (<samp>.ogg</samp>) files, which otherwise will be
decompressed in-memory on load. Default false.</p>
<p>This is a tradeoff between memory usage and performance, so you
should consider which value is best for each audio cue:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>true</samp></p></td>
<td><p>Reduces memory usage when the audio cue isn't active, but
increases performance impact when it's played. Playing the audio
multiple times will multiply the memory and performance impact while
they're active, since each play will stream a new instance. Recommended
for longer audio cues (like music or ambient noise), or cues that are
rarely used in a specific scenario (e.g. a sound that only plays once in
an event).</p></td>
</tr>
<tr>
<td><p><samp>false</samp></p></td>
<td><p>Increases memory usage (since it's fully loaded into memory), but
reduces performance impact when it's played. It can be played any number
of times without affecting memory or performance (it'll just play the
cached audio). Recommended for sound effects, or short audio cues that
are played occasionally.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Looped</samp></p></td>
<td><p>Whether the audio cue loops continuously until stopped. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>UseReverb</samp></p></td>
<td><p>Whether to apply a <a href="wikipedia_Reverberation"
class="wikilink" title="reverb">reverb</a> effect to the audio. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="#Custom_data_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry.</p></td>
</tr>
</tbody>
</table>

### Category list

Each audio cue is assigned to one of five categories, which affects
which volume slider in the game options applies to it:

| internal ID | name | description |
|----|----|----|
| 1 | `Default` | This is an unused category, and should generally be avoided. |
| 2 | `Music` | For music tracks, to be regulated with the in-game music volume option. |
| 3 | `Sound` | For sound effects, to be regulated with the in-game sound volume option. |
| 4 | `Ambient` | For ambient background sounds, like wind, rain or machine whirring, that can play in the background of a scene. |
| 5 | `Footsteps` | For step sounds, such as player or horse footsteps. |

### Audio file format

The game only supports `.ogg` and `.wav` formats. If you have `.mp3`
files you'd like to use in-game, you can convert the audio file to
`.wav` or `.ogg` with audio software such as
[Audacity](https://www.audacityteam.org/). For smaller-sized sounds such
as sound effects, you can use a `.wav` file, but for audio such as music
that has a large file size, use a compressed `.ogg` file.

Make sure the file size of your music is relatively small (preferably
around 2-4MB). The bigger the file, the longer the game will freeze for
when loading your newly added song. To reduce the size of your song, you
can convert it to `.ogg` and add compression to the sound file. The more
compression your audio has, the smaller the file will be, but the
quality will diminish noticeably if you compress the audio too much.

If you're patching many sounds at once, keep the file size of your mod
in mind, because the more sounds you include, the longer it will take
for people to download your mod.

If your audio is in mono and not stereo, it may sound quieter or muffled
compared to other audio. You should convert your audio to stereo if you
want to avoid this.

### Example

This <a href="Modding_Content_Patcher" class="wikilink"
title="content pack">content pack</a> adds a new music cue to the game,
and plays it when the player enters the bus stop:

## Review audio

### Unpack audio files

The base game's audio is stored in the `Content/XACT` folder in the form
of soundbanks, which store all of the game's sounds and music. The two
soundbank files available are `Wave Bank(1.4).xwb` and `Wave Bank.xwb`.

Audio files can be extracted and browsed with an XWB extractor:

| tool name | platforms supported | notes |
|----|----|----|
|  | Windows, macOS | Extracts an XWB soundbank into .wav files and hex codes. A straightforward open and extract utility. |
| [VGMStream](https://www.vgmstream.org/downloads) plugin for [foobar2000](https://www.foobar2000.org/) sound player | Windows | Views XWB soundbanks with integer codes and many in-game codes included in filenames, and has a very convenient file browser. (For some reason, it increments audio IDs by 1, and each audio cue is looped.) |
| [XACTTool](https://shrinefox.com/browse?post=xacttool) | Windows | Extracts an XWB soundbank into .wav files and integer codes. Can also manipulate soundbanks. Command-line only. |

See the
<a href="#Track_list" class="wikilink" title="full track list">full
track list</a> below.

### Identify audio in-game

- For music tracks, you can install the mod (see the mod description for
  info on adding the music ID to the message). A HUD message will be
  shown in-game when music starts.
- For sound effects, you can enter `debug logSounds` in the SMAPI
  console window. This will log info for each sound played in-game,
  including positional data if applicable. See
  <a href="Modding_Console_commands" class="wikilink"
  title="console commands">console commands</a> for more info.
