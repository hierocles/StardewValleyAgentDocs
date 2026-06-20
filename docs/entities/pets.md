---
title: "Pets"
wiki_source: "Modding:Pets"
permalink: /Modding:Pets/
category: entities
tags: [pets, data-format, basic-info, audio-sprites, events, gifts, behavior, breeds]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents how the game stores and parses data for
<a href="Animals#Cat_or_Dog" class="wikilink" title="pets">pets</a>.
This is an advanced guide for mod developers.

## Data Format

You can create and customize
<a href="Animals#Cat_or_Dog" class="wikilink" title="pets">pets</a> &
pet breeds by editing the `Data/Pets` asset.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  pet (not the pet breed). The vanilla IDs are `Cat` and `Dog`.
- The value is a model with the fields listed below.

### Basic info

| field | effect |
|----|----|
| `DisplayName` | A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the pet type's display name (e.g. "cat" or "dog"). For example, the vanilla adoption events show this when Marnie asks if you want to adopt the cat/dog. |

### Audio & sprites

| field | effect |
|----|----|
| `BarkSound` | The <a href="Modding_Audio" class="wikilink" title="cue ID">cue ID</a> for the pet's occasional 'bark' sound. |
| `ContentSound` | The <a href="Modding_Audio" class="wikilink" title="cue ID">cue ID</a> for the sound which the pet makes when you pet it. |
| `RepeatContentSoundAfter` | *(Optional)* The number of milliseconds until the `ContentSound` is repeated once. This is used by the dog, who pants twice when pet. Defaults to -1 (disabled). |
| `EmoteOffset` | *(Optional)* A pixel offset for the emote drawn above the pet sprite, specified as an object with `X` and `Y` fields. For example, this affects the heart emote shown after petting it. Default none. |

### Events

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>EventOffset</samp></p></td>
<td><p><em>(Optional)</em> The pixel offset for the pet when shown in
events like Marnie's adoption event, specified as an object with
<samp>X</samp> and <samp>Y</samp> fields. Default none.</p></td>
</tr>
<tr>
<td><p><samp>AdoptionEventLocation</samp><br />
<samp>AdoptionEventId</samp></p></td>
<td><p><em>(Optional)</em> If both fields are set, the location and <a
href="Modding_Event_data" class="wikilink" title="event ID">event ID</a>
which lets the player adopt this pet. This forces the event to play
after 20 days if its preconditions haven't been met yet. Default
<samp>Farm</samp> and none respectively.</p></td>
</tr>
<tr>
<td><p><samp>SummitPerfectionEvent</samp></p></td>
<td><p><em>(Optional)</em> How to render the pet during the summit <a
href="perfection" class="wikilink" title="perfection">perfection</a>
slideshow. If this isn't set, the pet won't be shown in the
slideshow.</p>
<p>This consists of a model with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>SourceRect</samp></p></td>
<td><p>The source rectangle within the pet's texture to draw.</p></td>
</tr>
<tr>
<td><p><samp>AnimationLength</samp></p></td>
<td><p>The number of frames to show starting from the
<samp>SourceRect</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Motion</samp></p></td>
<td><p>The motion to apply to the pet sprite.</p></td>
</tr>
<tr>
<td><p><samp>Flipped</samp></p></td>
<td><p><em>(Optional)</em> Whether to flip the pet sprite left-to-right.
Default false.</p></td>
</tr>
<tr>
<td><p><samp>PingPong</samp></p></td>
<td><p><em>(Optional)</em> Whether to apply the 'ping pong' effect to
the pet sprite animation. Default false.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### Gifts

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>GiftChance</samp></p></td>
<td><p><em>(Optional)</em> The random probability each day that the pet
will give the player a gift from the <samp>Gifts</samp> list when they
interact with the pet. Specified as a value between 0 (never) and 1
(always). Default .2 (20% chance).</p></td>
</tr>
<tr>
<td><p><samp>Gifts</samp></p></td>
<td><p><em>(Optional)</em> The list of gifts that this pet can give if
the <samp>GiftChance</samp> is successful. Default none.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry within the list.</p></td>
</tr>
<tr>
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported by pet gifts.</p>
<p>Notes:</p>
<ul>
<li>If <samp>ItemId</samp> or <samp>RandomItemId</samp> is set to an <a
href="Modding_Item_queries" class="wikilink" title="item query">item
query</a> which returns multiple items, one item will be selected at
random.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>MinimumFriendshipThreshold</samp></p></td>
<td><p><em>(Optional)</em> The friendship level that this pet must be at
before it can give this gift. Defaults to 1000 (max
friendship).</p></td>
</tr>
<tr>
<td><p><samp>Weight</samp></p></td>
<td><p><em>(Optional)</em> The option's weight when randomly choosing a
gift, relative to other gifts in the list (e.g. <samp>2</samp> is twice
as likely as <samp>1</samp>). Default 1.</p></td>
</tr>
<tr>
<td><p><samp>QualifiedItemID</samp><br />
<samp>Stack</samp></p></td>
<td><p><strong>Obsolete.</strong> Use <samp>ItemId</samp> and
<samp>MinStack</samp> in the <a
href="Modding_Item_queries#Item_spawn_fields" class="wikilink"
title="item spawn fields">item spawn fields</a> instead.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### Behavior

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for this
entry within the list.</p></td>
</tr>
<tr>
<td><p><samp>MoveSpeed</samp></p></td>
<td><p><em>(Optional)</em> How quickly the pet can move. Default
2.</p></td>
</tr>
<tr>
<td><p><samp>SleepOnBedChance</samp><br />
<samp>SleepNearBedChance</samp><br />
<samp>SleepOnRugChance</samp></p></td>
<td><p><em>(Optional)</em> The percentage chances for the locations
where the pet will sleep each night, as a decimal value between 0
(never) and 1 (always). Each value is checked in the order listed at
left until a match is found. If none of them match, the pet will choose
a random empty spot in the farmhouse; if none was found, it'll sleep
next to its pet bowl outside.</p></td>
</tr>
<tr>
<td><p><samp>Behaviors</samp></p></td>
<td><p>The pet's possible actions and behaviors, defined as the states
in a state machine. Essentially the pet will be in one state at any
given time, which also determines which state they can transition to
next. For example, a cat can transition from <samp>Walk</samp> to
<samp>BeginSitDown</samp>, but it can't skip instantly from
<samp>Walk</samp> to <samp>SitDownLick</samp>.</p>
<p>This consists of a list of models with these fields:</p>
<dl>
<dt>
<p>Required fields:</p>
</dt>
<dd>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>A unique ID for the state. This only needs to be unique within
the pet type (e.g. <samp>Cat</samp> and <samp>Dog</samp> can have
different behaviors with the same ID).</p></td>
</tr>
</tbody>
</table>
</dd>
<dt>
<p>Direction:</p>
</dt>
<dd>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Direction</samp></p></td>
<td><p><em>(Optional)</em> The specific direction to face at the start
of this state (one of <samp>left</samp>, <samp>right</samp>,
<samp>up</samp>, or <samp>down</samp>), unless overridden by
<samp>RandomizeDirection</samp>.</p></td>
</tr>
<tr>
<td><p><samp>RandomizeDirection</samp></p></td>
<td><p><em>(Optional)</em> Whether to point the pet in a random
direction at the start of this state (overriding the
<samp>Direction</samp> if specified). Default false.</p></td>
</tr>
<tr>
<td><p><samp>IsSideBehavior</samp></p></td>
<td><p><em>(Optional)</em> Whether to constrain the pet's facing
direction to left and right while the state is active. Default
false.</p></td>
</tr>
</tbody>
</table>
</dd>
<dt>
<p>Movement:</p>
</dt>
<dd>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>WalkInDirection</samp></p></td>
<td><p><em>(Optional)</em> Whether to walk in the pet's facing
direction. Default false.</p></td>
</tr>
<tr>
<td><p><samp>MoveSpeed</samp></p></td>
<td><p><em>(Optional)</em> Overrides the pet's <samp>MoveSpeed</samp>
field while this state is active. Default -1 (which uses the pet's
<samp>MoveSpeed</samp> value).</p></td>
</tr>
</tbody>
</table>
</dd>
<dt>
<p>Audio:</p>
</dt>
<dd>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>SoundOnStart</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> for the sound to play when the
state starts. If set to <samp>BARK</samp>, the pet's
<samp>BarkSound</samp> (or breed's <samp>BarkOverride</samp>) field is
used. Defaults to none.</p></td>
</tr>
<tr>
<td><p><samp>SoundRange</samp><br />
<samp>SoundRangeFromBorder</samp></p></td>
<td><p><em>(Optional)</em> When set, the <samp>SoundOnStart</samp> is
only audible if the pet is within this many tiles away from the player
(<samp>SoundRange</samp>) or past the border of the screen
(<samp>SoundRangeFromBorder</samp>). Default -1 (no distance
check).</p></td>
</tr>
<tr>
<td><p><samp>SoundIsVoice</samp></p></td>
<td><p><em>(Optional)</em> Whether to mute the <samp>SoundOnStart</samp>
when the 'mute animal sounds' option is set. Default false.</p></td>
</tr>
</tbody>
</table>
</dd>
<dt>
<p>Behavior transitions:</p>
</dt>
<dd>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AnimationEndBehaviorChanges</samp><br />
<samp>TimeoutBehaviorChanges</samp><br />
<samp>PlayerNearbyBehaviorChanges</samp><br />
<samp>RandomBehaviorChanges</samp><br />
<samp>JumpLandBehaviorChanges</samp></p></td>
<td><p><em>(Optional)</em> A list of possible behavior transitions to
start when the criteria are achieved. If multiple transitions are
listed, a random one will be selected. If omitted, it won't affect
behavior transitions.</p>
<p>These are triggered when this behavior's animation finishes
(<samp>AnimationEndBehaviorChanges</samp>), when the set duration ends
(<samp>TimeoutBehaviorChanges</samp>), when the player is within 2 tiles
of the pet (<samp>PlayerNearbyBehaviorChanges</samp>), randomly at the
start of each frame based on the <samp>RandomBehaviorChangeChance</samp>
field (<samp>RandomBehaviorChanges</samp>), and when the pet finishes a
jump (<samp>JumpLandBehaviorChanges</samp>).</p>
<p>These consist of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Behavior</samp><br />
<samp>LeftBehavior</samp><br />
<samp>RightBehavior</samp><br />
<samp>UpBehavior</samp><br />
<samp>DownBehavior</samp></p></td>
<td><p>The ID of the behavior to start. The pet will check for a
behavior field matching its current facing direction first, then try the
<samp>Behavior</samp>. If none are specified, the current behavior will
continue unchanged.</p></td>
</tr>
<tr>
<td><p><samp>OutsideOnly</samp></p></td>
<td><p><em>(Optional)</em> Whether the transition can only happen if the
pet is outside. Default false.</p></td>
</tr>
<tr>
<td><p><samp>Weight</samp></p></td>
<td><p><em>(Optional)</em> The option's weight when randomly choosing a
behavior, relative to other behaviors in the list (e.g. <samp>2</samp>
is twice as likely as <samp>1</samp>). Default 1.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Duration</samp><br />
<samp>MinimumDuration</samp><br />
<samp>MaximumDuration</samp></p></td>
<td><p><em>(Optional)</em> The millisecond duration until the pet
transitions to a behavior in the <samp>TimeoutBehaviorChanges</samp>
field, if set. You must specify either a specific duration, or an
inclusive minimum-to-maximum range in which the game will choose a
random duration. If omitted, the behavior won't have a duration
limit.</p></td>
</tr>
<tr>
<td><p><samp>RandomBehaviorChangeChance</samp></p></td>
<td><p><em>(Optional)</em> The random probability at the start of each
frame that the pet will transition to a behavior in the
<samp>RandomBehaviorChanges</samp> field, if set. Specified as a value
between 0 (never) and 1 (always). Default 0.</p></td>
</tr>
</tbody>
</table>
</dd>
<dt>
<p>Animation and per-frame sounds:</p>
</dt>
<dd>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Animation</samp></p></td>
<td><p><em>(Optional)</em> The animation frames to play while this state
is active. This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Frame</samp></p></td>
<td><p>The frame index in the animation. This should be an incremental
number starting at 0.</p></td>
</tr>
<tr>
<td><p><samp>Duration</samp></p></td>
<td><p>The millisecond duration for which the frame should be kept
on-screen before continuing to the next frame.</p></td>
</tr>
<tr>
<td><p><samp>HitGround</samp></p></td>
<td><p><em>(Optional)</em> Whether to play the footstep sound for the
tile under the pet when the frame starts. Default false.</p></td>
</tr>
<tr>
<td><p><samp>Jump</samp></p></td>
<td><p><em>(Optional)</em> Whether the pet should perform a small hop
when the frame starts, including a 'dwop' sound. Default false.</p></td>
</tr>
<tr>
<td><p><samp>Sound</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> for the sound to play when the
animation starts or loops. If set to <samp>BARK</samp>, the pet's
<samp>BarkSound</samp> (or breed's <samp>BarkOverride</samp>) field is
used. Defaults to none.</p></td>
</tr>
<tr>
<td><p><samp>SoundRange</samp><br />
<samp>SoundRangeFromBorder</samp><br />
<samp>SoundIsVoice</samp></p></td>
<td><p>See description for the equivalent behavior fields, but applies
to the frame's <samp>Sound</samp> field instead.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Shake</samp></p></td>
<td><p><em>(Optional)</em> The millisecond duration for which to shake
the pet when the state starts. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>LoopMode</samp></p></td>
<td><p><em>(Optional)</em> What to do when the last animation frame is
reached while the behavior is still active. The possible values are
<samp>Hold</samp> (keep the last frame visible until the animation
ends), <samp>Loop</samp> (restart from the first frame), or
<samp>None</samp> (equivalent to <samp>Loop</samp>). Default
<samp>None</samp>.</p></td>
</tr>
<tr>
<td><p><samp>AnimationMinimumLoops</samp><br />
<samp>AnimationMaximumLoops</samp></p></td>
<td><p><em>(Optional)</em> The minimum and maximum number of times to
play the animation. Both must be specified to have any effect. The game
will choose an inclusive random value between them. Both default to -1
(don't repeat animation).</p></td>
</tr>
</tbody>
</table>
</dd>
</dl></td>
</tr>
</tbody>
</table>

### Breeds

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Breeds</samp></p></td>
<td><p>The cosmetic breeds which can be selected in the character
customization menu when creating a save. This consists of a list of
models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>The unique ID for the breed within the pet type.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the breed spritesheet for the pet's in-game
sprite. This should be 128 pixels wide, and 256 (cat) or 288 (dog)
pixels high.</p></td>
</tr>
<tr>
<td><p><samp>IconTexture</samp></p></td>
<td><p>The asset name for the breed icon texture, shown on the character
customization screen and in-game menu. This should be a 16x16 pixel
icon.</p></td>
</tr>
<tr>
<td><p><samp>IconSourceRect</samp></p></td>
<td><p>The icon's pixel area within the <samp>IconTexture</samp>,
specified as an object with <samp>X</samp>, <samp>Y</samp>,
<samp>Width</samp>, and <samp>Height</samp> fields.</p></td>
</tr>
<tr>
<td><p><samp>CanBeChosenAtStart</samp></p></td>
<td><p><em>(Optional)</em> Whether this pet can be chosen as a starter
pet during character creation. Default true.</p></td>
</tr>
<tr>
<td><p><samp>CanBeAdoptedFromMarnie</samp></p></td>
<td><p><em>(Optional)</em> Whether this pet can be adopted from Marnie
once she starts offering pets. Default true.</p></td>
</tr>
<tr>
<td><p><samp>AdoptionPrice</samp></p></td>
<td><p><em>(Optional)</em> The gold price to adopt this pet in Marnie's
shop, if it can be adopted. Default .</p></td>
</tr>
<tr>
<td><p><samp>BarkOverride</samp></p></td>
<td><p><em>(Optional)</em> Override the pet's <samp>BarkSound</samp>
field for this breed, if set.</p></td>
</tr>
<tr>
<td><p><samp>VoicePitch</samp></p></td>
<td><p><em>(Optional)</em> The <a href="wikipedia_Pitch_(music)"
class="wikilink" title="pitch">pitch</a> applied to the pet's bark
sound, measured as a decimal value relative to 1. Defaults to
1.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### Advanced

| field | effect |
|----|----|
| `CustomFields` | The <a href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry. |

## Spritesheet layout

### Explanation

Each farm animal's spritesheet must have exactly 4 columns. The sprite
size is expected to be 32x32.

The expected rows are:

1.  move down;
2.  move right;
3.  move up;
4.  move left
5.  unique animations 1;
6.  unique animations 2;
7.  unique animations 3;
8.  sleep and unique animations 4;
9.  unique animations 5

For example, the default layout is:

|                  |                  |                  |                  |
|------------------|------------------|------------------|------------------|
| 0 (move down 1)  | 1 (move down 2)  | 2 (move down 3)  | 3 (move down 4)  |
| 4 (move right 1) | 5 (move right 2) | 6 (move right 3) | 7 (move right 4) |
| 8 (move up 1)    | 9 (move up 2)    | 10 (move up 3)   | 11 (move up 4)   |
| 12 (move left 1) | 13 (move left 2) | 14 (move left 3) | 15 (move left 4) |
| 16 (unique)      | 17 (unique)      | 18 (unique)      | 19 (unique)      |
| 20 (unique)      | 21 (unique)      | 22 (unique)      | 23 (unique)      |
| 24 (unique)      | 25 (unique)      | 26 (unique)      | 27 (unique)      |
| 28 (sleep 1)     | 29 (sleep 2)     | 30 (unique)      | 31 (unique)      |
| 32 (unique)      | 33 (unique)      | 34 (unique)      | 35 (unique)      |

The rows for moving down, right, up, and left will be used when
copy/pasting the Walk behavior from the cat, dog, or turtle. If you
don't use that behavior, you can actually put things that aren't moving
up, down, or left there. However, in the absence of any defined
Behavior, the pet will still use frames 28 and 29 for sleeping, and when
being pushed it will use frames 0, 4, 8, or 12 depending on which
direction the player is pushing from (e.g. if pushing from the left in
order to move right, the pet will face right, using frame 4).

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Питомцы" class="wikilink"
title="ru:Модификации:Питомцы">ru:Модификации:Питомцы</a>
<a href="zh_模组_宠物" class="wikilink"
title="zh:模组:宠物">zh:模组:宠物</a>
