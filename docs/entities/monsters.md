---
title: "Monsters"
wiki_source: "Modding:Monster data"
permalink: /Modding:Monster_data/
category: entities
tags: [monster-data, raw-data, format, monster-specific-notes, slime-sprites, monster-ids]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses monster data. This is
an advanced guide for mod developers.

## Raw data

Monster data is stored in `Content\Data\Monsters.xnb`, which can be
<a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of for reference:

## Format

| Index | Field | Example Value |
|----|----|----|
| 0 | health (hit points) | *24* |
| 1 | damage (attack) | *5* |
| 2 | minimum coins to drop *(unimplemented)* | *0* |
| 3 | maximum coins to drop *(unimplemented)* | *0* |
| 4 | whether a "glider" (flying) | *false* |
| 5 | duration of random movements | *1000* |
| 6 | objects to drop | *766 .75 766 .05 153 .1 66 .015 92 .15 96 .005 99 .001* |
| 7 | resilience (defense) | *1* |
| 8 | jitteriness | *.01* |
| 9 | distance threshold for moving towards player | *4* |
| 10 | speed | *2* |
| 11 | chance of attacks missing | *.00* |
| 12 | whether a "mine monster" | *true* |
| 13 | experience gained | *3* |
| 14 | display name | *Green Slime* |
|  |  |  |

Index 4 designates "gliders": monsters that fly above the ground.
Although <a href="Ghost" class="wikilink" title="Ghost">Ghosts</a> are
not listed as gliders in the data, they are overridden to be gliders in
the game code.

Index 6 contains a list of object ID numbers, each followed by the
probability of that object being chosen. Multiple objects can be chosen
from the list. "Extra drop items" in the game code supplement this list
for several monster types.

Index 12 designates "mine monsters": monsters whose stats and drops are
buffed for players who have reached the bottom of the mines. These
include the <a href="Wilderness_Golem" class="wikilink"
title="Wilderness Golem">Wilderness Golem</a> and other monsters that do
not actually occur in the mines. This field is *false* only for
non-monsters that use the monster data file, such as the fireball
projectile launched by the
<a href="Squid_Kid" class="wikilink" title="Squid Kid">Squid Kid</a>.

Note that many of the values stored in the monster data are altered by
the game code under specific circumstances. These include being in
different parts of the mines, having reached the bottom of the mines,
and having a higher combat skill level.

## Monster-specific notes

### Slime sprites

<a href="File_Green_Slime_Notes.png" class="wikilink"
title="right">right</a>

<a href="Slime" class="wikilink" title="Slime">Slime</a> sprites are
entirely modular, with the associated parts spread out across the sprite
sheet. Every slime uses the same grey sprite, coloring it with a tint
mask based on the type of slime, along with a random transparency value.
Row 1 is used for the idle state and normal movement. Rows 2 through 4,
while apparently identical, appear unused in most cases (row 2 appears
sporadically at the end of certain attacks, but further testing is
needed for exact conditions). Row 5 is used for the attack animation.

Area 6 on the sprite sheet contains assets for the "mating ritual"
slimes can go through, as well as their death particles. The mating
particles (going clockwise) are used for seeking a mate, rejecting a
mate, and receiving a rejection.

Area 7 contains the assets for the eyes. Slime eyes are placed
dynamically on their sprite based on their current action. When the
slime is facing down, the eyes are placed directly on top of the sprite;
when facing left, only the right eye is rendered, and moved slightly
left; when facing right, only the left eye is rendered and moved
slightly right; when facing up, the eyes are rendered directly behind
the slime. The eyes, going clockwise, are used for their idle state,
during attacks, during the "evil" state (each slime has a chance to turn
"evil" when first hit, and gains a stat boost), and taking damage.

Area 8 is the antenna attached to "male" slimes. It appears to animate
independently of the slime itself, rocking back and forth somewhat at
random. As with the main sprite, this uses a tint mask to take on the
color of the slime variant.

Area 9 is the antenna attached to "special" slimes, and animates in the
same way as the "male" antenna. However, this one doesn't use the tint
mask, instead using whatever raw color is on the sprite sheet.

## Monster IDs

Each monster type has a unique ID (stored in the `Name` field) which can
be used to spawn it (e.g. via
<a href="Modding_Console_commands" class="wikilink"
title="console commands">console commands</a>), and is used to track
kills for the <a href="Adventurer&#39;s_Guild" class="wikilink"
title="Adventurer&#39;s Guild">Adventurer's Guild</a> monster
eradication goals. These are the IDs for vanilla monsters:

| monster | ID |
|----|----|
| <a href="Bats" class="wikilink" title="Bat">Bat</a> | `Bat` |
| <a href="Slimes" class="wikilink" title="Big Slime">Big Slime</a> | `BigSlime` |
| <a href="Blue_Squid" class="wikilink" title="Blue Squid">Blue Squid</a> | `Blue Squid` |
| <a href="Bug" class="wikilink" title="Bug">Bug</a> | `Bug` |
| <a href="Cave_Fly" class="wikilink" title="Cave Fly">Cave Fly</a> | `Fly` |
| <a href="Duggy" class="wikilink" title="Duggy">Duggy</a> | `Duggy` |
| <a href="Dust_Sprite" class="wikilink" title="Dust Sprite">Dust
Sprite</a> | `Dust Spirit` |
| <a href="Dwarvish_Sentry" class="wikilink"
title="Dwarvish Sentry">Dwarvish Sentry</a> | `Dwarvish Sentry` |
| <a href="Ghost" class="wikilink" title="Ghost">Ghost</a> | `Ghost` |
| <a href="Grub" class="wikilink" title="Grub">Grub</a> | `Grub` |
| <a href="Lava_Crab" class="wikilink" title="Lava Crab">Lava Crab</a> | `Lava Crab` |
| <a href="Lava_Lurk" class="wikilink" title="Lava Lurk">Lava Lurk</a> | `Lava Lurk` |
| <a href="Metal_Head" class="wikilink" title="Metal Head">Metal Head</a> | `Metal Head` |
| <a href="Mummy" class="wikilink" title="Mummy">Mummy</a> | `Mummy` |
| <a href="Pepper_Rex" class="wikilink" title="Pepper Rex">Pepper Rex</a> | `Pepper Rex` |
| <a href="Rock_Crab" class="wikilink" title="Rock Crab">Rock Crab</a> | `Rock Crab` |
| <a href="Serpent" class="wikilink" title="Serpent">Serpent</a> | `Serpent` |
| <a href="Shadow_Brute" class="wikilink" title="Shadow Brute">Shadow
Brute</a> | `Shadow Brute` |
| <a href="Shadow_Shaman" class="wikilink" title="Shadow Shaman">Shadow
Shaman</a> | `Shadow Shaman` |
| <a href="Shadow_Sniper" class="wikilink" title="Shadow Sniper">Shadow
Sniper</a> | `Shadow Sniper` |
| <a href="Slimes" class="wikilink" title="Slime">Slime</a> | `Green Slime` |
| <a href="Spider" class="wikilink" title="Spider">Spider</a> | `Spider` |
| Spiker | `Spiker` |
| <a href="Squid_Kid" class="wikilink" title="Squid Kid">Squid Kid</a> | `Squid Kid` |
| <a href="Stone_Golem" class="wikilink" title="Stone Golem">Stone
Golem</a> | `Stone Golem` |
| <a href="Wilderness_Golem" class="wikilink"
title="Wilderness Golem">Wilderness Golem</a> | `Wilderness Golem` |

Note that many other monsters are variants of the above (*e.g.*
<a href="Haunted_Skull" class="wikilink" title="Haunted Skull">Haunted
Skull</a> is a variant of
<a href="Bats" class="wikilink" title="Bat">Bat</a>), and have the same
ID.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Монстры" class="wikilink"
title="ru:Модификации:Монстры">ru:Модификации:Монстры</a>
<a href="zh_模组_怪物数据" class="wikilink"
title="zh:模组:怪物数据">zh:模组:怪物数据</a>
