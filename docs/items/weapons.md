---
title: "Weapons"
wiki_source: "Modding:Weapons"
permalink: /Modding:Weapons/
category: items
tags: [weapons, overview, data-format, basic-weapon-info, appearance, stats, game-logic, advanced]
---
← <a href="Modding_Items" class="wikilink" title="Items">Items</a>

This page explains how the game stores and parses weapon-type item data.
For items in general, see <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a>.

## Overview

<a href="Weapons" class="wikilink" title="Weapons">Weapons</a> are tools
that can be swung or used by the player to damage monsters.

They have <a href="Modding_Items#Item_types" class="wikilink"
title="item type">item type</a> `(W)` (or `ItemRegistry.type_weapon` in
C# code), their data in `Data/Weapons`, their in-game sprites in
`TileSheets/weapons` by default, and their code in
`StardewValley.Tools.MeleeWeapon` and `StardewValley.Tools.Slingshot`.

## Data format

The weapon data in `Data/Weapons` consists of a string → model lookup,
where...

- The key is the
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="unqualified item ID">unqualified item ID</a>.
- The value is model with the fields listed below.

### Basic weapon info

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
<td><p>The internal weapon name.</p></td>
</tr>
<tr>
<td><p><samp>DisplayName</samp><br />
<samp>Description</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the translated
display name &amp; description.</p></td>
</tr>
<tr>
<td><p><samp>Type</samp></p></td>
<td><p>The weapon type. One of <samp>0</samp> (stabbing sword),
<samp>1</samp> (dagger), <samp>2</samp> (club or hammer), or
<samp>3</samp> (slashing sword).</p></td>
</tr>
</tbody>
</table>

### Appearance

| field | effect |
|----|----|
| `Texture` | The asset name for the spritesheet containing the weapon's sprite. |
| `SpriteIndex` | The index within the `Texture` for the weapon sprite, where 0 is the top-left sprite. |

### Stats

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>MinDamage</samp><br />
<samp>MaxDamage</samp></p></td>
<td><p>The minimum and maximum based damage caused when hitting a
monster with this weapon.</p></td>
</tr>
<tr>
<td><p><samp>Knockback</samp></p></td>
<td><p><em>(Optional)</em> How far the target is pushed when hit, as a
multiplier relative to a base weapon like the <a href="Rusty_Sword"
class="wikilink" title="Rusty Sword">Rusty Sword</a> (e.g.
<samp>1.5</samp> for 150% of Rusty Sword's weight). Default 1.</p></td>
</tr>
<tr>
<td><p><samp>Speed</samp></p></td>
<td><p><em>(Optional)</em> How fast the player can swing the weapon.
Each point of speed is worth 40ms of swing time relative to 0. This
stacks with the <a href="speed" class="wikilink"
title="player&#39;s weapon speed">player's weapon speed</a>. Default
0.</p></td>
</tr>
<tr>
<td><p><samp>Precision</samp></p></td>
<td><p><em>(Optional)</em> Reduces the chance that a strike will miss.
Default 0.</p></td>
</tr>
<tr>
<td><p><samp>Defense</samp></p></td>
<td><p><em>(Optional)</em> Reduces damage received by the player.
Default 0.</p></td>
</tr>
<tr>
<td><p><samp>AreaOfEffect</samp></p></td>
<td><p><em>(Optional)</em> Slightly increases the area of effect.
Default 0.</p></td>
</tr>
<tr>
<td><p><samp>CritChance</samp></p></td>
<td><p><em>(Optional)</em> The chance of a critical hit, as a decimal
value between 0 (never) and 1 (always). Default 0.02.</p></td>
</tr>
<tr>
<td><p><samp>CritMultiplier</samp></p></td>
<td><p><em>(Optional)</em> A multiplier applied to the base damage for a
critical hit. This can be a decimal value. Default 3.</p></td>
</tr>
</tbody>
</table>

### Game logic

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>CanBeLostOnDeath</samp></p></td>
<td><p>Whether the player can <a
href="Adventurer&#39;s_Guild#Item_Recovery_Service" class="wikilink"
title="lose this tool when they die">lose this tool when they die</a>.
Default true.</p></td>
</tr>
<tr>
<td><p><samp>MineBaseLevel</samp><br />
<samp>MineMinLevel</samp></p></td>
<td><p><em>(Optional)</em> The base and minimum mine level, which affect
<a href="#Mine_container_drops" class="wikilink"
title="mine container drops">mine container drops</a>. Both default to
-1, which disables automatic mine drops.</p></td>
</tr>
</tbody>
</table>

### Advanced

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Projectiles</samp></p></td>
<td><p><em>(Optional)</em> The projectiles fired when the weapon is
used, which continue along their path until they hit a monster and cause
damage. A separate projectile is fired for each entry in this list.</p>
<p>This consists of a list of models with these fields (one projectile
will fire for each entry in the list):</p>
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
class="wikilink" title="unique string ID">unique string ID</a> for the
projectile within the current weapon's data.</p></td>
</tr>
<tr>
<td><p><samp>Damage</samp></p></td>
<td><p><em>(Optional)</em> The amount of damage caused when the
projectile hits a monster. Default 10.</p></td>
</tr>
<tr>
<td><p><samp>Explodes</samp></p></td>
<td><p><em>(Optional)</em> Whether the projectile explodes when it
collides with something. Default false.</p></td>
</tr>
<tr>
<td><p><samp>Bounces</samp></p></td>
<td><p><em>(Optional)</em> The number of times the projectile can bounce
off walls before being destroyed. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>MaxDistance</samp></p></td>
<td><p><em>(Optional)</em> The maximum tile distance the projectile can
travel. Default 4.</p></td>
</tr>
<tr>
<td><p><samp>Velocity</samp></p></td>
<td><p><em>(Optional)</em> The speed at which the projectile moves.
Default 10.</p></td>
</tr>
<tr>
<td><p><samp>RotationVelocity</samp></p></td>
<td><p><em>(Optional)</em> The rotation velocity. Default 32.</p></td>
</tr>
<tr>
<td><p><samp>TailLength</samp></p></td>
<td><p><em>(Optional)</em> The length of the tail which trails behind
the main projectile. Default 1.</p></td>
</tr>
<tr>
<td><p><samp>FireSound</samp><br />
<samp>BounceSound</samp><br />
<samp>CollisionSound</samp></p></td>
<td><p><em>(Optional)</em> The sound played when the projectile is
fired, bounces off a wall, or collides with something. All three default
to none.</p></td>
</tr>
<tr>
<td><p><samp>MinAngleOffset</samp><br />
<samp>MaxAngleOffset</samp></p></td>
<td><p><em>(Optional)</em> A random offset applied to the direction of
the project each time it's fired. Both fields default to 0, in which
case it's always shot at the 90° angle matching the player's facing
direction.</p></td>
</tr>
<tr>
<td><p><samp>SpriteIndex</samp></p></td>
<td><p><em>(Optional)</em> The sprite index in the
<samp>TileSheets/Projectiles</samp> asset to draw for this projectile.
Defaults to 11 (a glowing-yellow-ball sprite).</p></td>
</tr>
<tr>
<td><p><samp>Item</samp></p></td>
<td><p><em>(Optional)</em> The item to shoot. If set, this overrides
<samp>SpriteIndex</samp>.</p>
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
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported for ammo items.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p>Note that these are magic projectiles fired when the weapon is used,
they're not aimed directly like <a href="slingshot" class="wikilink"
title="slingshot">slingshot</a> projectiles.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

Weapons have a hardcoded category of -98 (`Object.weaponCategory`).

## Implementation notes

### Slingshots

- The base
  <a href="slingshot" class="wikilink" title="slingshot">slingshot</a>
  has `ParentSheetIndex` 32 in the weapon data, which increases by one
  for each upgrade level (up to 34 in the weapon data, though only 32
  and 33 are obtainable without mods).
- Slingshot damage is <a href="Slingshot#Ammunition" class="wikilink"
  title="calculated dynamically">calculated dynamically</a> regardless
  of the weapon data.

### Mine container drops

When the player breaks a container in
<a href="The_Mines" class="wikilink" title="the mines">the mines</a>,
there's a chance it will drop a weapon. Here's how the weapon to drop is
chosen[^1]:

1.  Match weapons whose <a href="#Game_logic" class="wikilink"
    title="minimum mine level">minimum mine level</a> is less than the
    current mine level.
2.  From that list, match weapons with a probability check based on the
    gap between the
    <a href="#Game_logic" class="wikilink" title="base mine level">base mine
    level</a> and current mine level. The probability is a bell curve
    centered on the base mine level:
    | level difference | probability |
    |------------------|-------------|
    | 0                | 100%        |
    | 5                | 92%         |
    | 10               | 71%         |
    | 15               | 46%         |
    | 20               | 25%         |
    | 25               | 4%          |

    The difference applies in both directions; for example, two weapons
    whose base levels are 5 below and 5 above the current level both
    have a 92% chance. (The probability is calculated with a
    <a href="wikipedia_Gaussian_function" class="wikilink"
    title="Gaussian function">Gaussian function</a>
    `e`<sup>`-(current mine level - base mine level)`<sup>`2`</sup>` / (2 * 12`<sup>`2`</sup>`)`</sup>.)
3.  Find the weapon with the smallest gap between the current and base
    mine levels, and add it to the list. (If the item was also selected
    in step 2, it has two chances to drop.)
4.  From the remaining list of weapons, randomly choose one to drop.

## References

<references />

## See also

- <a href="Modding_Items" class="wikilink"
  title="Modding:Items">Modding:Items</a> for item data in general

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Оружие" class="wikilink"
title="ru:Модификации:Оружие">ru:Модификации:Оружие</a>
<a href="zh_模组_武器" class="wikilink"
title="zh:模组:武器">zh:模组:武器</a>

[^1]: See `Utility.getUncommonItemForThisMineLevel` in the game code.
