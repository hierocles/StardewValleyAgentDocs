---
title: "Buffs"
wiki_source: "Modding:Buffs"
permalink: /Modding:Buffs/
category: game
tags: [buffs, data-format, for-c-mod-authors]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents custom buffs.

## Data format

You can define custom buffs by editing the `Data/Buffs` asset. You can
then use the buff from other places like `Data/Object`'s `Buff` field or
the C# `Buff` constructor.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  buff.
- The value is a model with the fields listed below.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DisplayName</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the buff
name.</p></td>
</tr>
<tr>
<td><p><samp>Description</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the buff name. Default none.</p></td>
</tr>
<tr>
<td><p><samp>IsDebuff</samp></p></td>
<td><p><em>(Optional)</em> &gt;Whether this buff counts as a debuff, so
its duration should be halved when wearing a <a href="Sturdy_Ring"
class="wikilink" title="sturdy ring">sturdy ring</a>. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>GlowColor</samp></p></td>
<td><p><em>(Optional)</em> The glow color to apply to the player. See <a
href="Modding_Common_data_field_types#Color" class="wikilink"
title="Modding:Common data field types#Color">Modding:Common data field
types#Color</a>. Default none.</p></td>
</tr>
<tr>
<td><p><samp>Duration</samp></p></td>
<td><p>The duration in milliseconds for which the buff should be active.
This can be set to value <samp>-2</samp> for a buff that should last for
the rest of the day.</p></td>
</tr>
<tr>
<td><p><samp>MaxDuration</samp></p></td>
<td><p><em>(Optional)</em> The maximum buff duration in milliseconds. If
specified and larger than <samp>Duration</samp>, a random value between
<samp>Duration</samp> and <samp>MaxDuration</samp> will be selected for
each buff. Default none.</p></td>
</tr>
<tr>
<td><p><samp>IconTexture</samp></p></td>
<td><p>The asset name for the texture containing the buff's
sprite.</p></td>
</tr>
<tr>
<td><p><samp>IconSpriteIndex</samp></p></td>
<td><p><em>(Optional)</em> The sprite index for the buff icon within the
<samp>IconTexture</samp>. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>Effects</samp></p></td>
<td><p><em>(Optional)</em> The buff attributes to apply. Default
none.</p>
<p>This consists of a model with any combination of these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>FarmingLevel</samp><br />
<samp>FishingLevel</samp><br />
<samp>ForagingLevel</samp><br />
<samp>LuckLevel</samp><br />
<samp>MiningLevel</samp><br />
<samp>CombatLevel</samp></p></td>
<td><p><em>(Optional)</em> An amount applied to the matching <a
href="Skills" class="wikilink" title="skill level">skill level</a> while
the buff is active. This can be negative for a debuff. Default
0.</p></td>
</tr>
<tr>
<td><p><samp>Attack</samp><br />
<samp>Defense</samp><br />
<samp>MagneticRadius</samp><br />
<samp>MaxStamina</samp><br />
<samp>Speed</samp><br />
<samp>Immunity</samp><br />
<samp>KnockbackMultiplier</samp><br />
<samp>WeaponSpeedMultiplier</samp><br />
<samp>AttackMultiplier</samp><br />
<samp>CriticalChanceMultiplier</samp><br />
<samp>CriticalPowerMultiplier</samp><br />
<samp>WeaponPrecisionMultiplier</samp></p></td>
<td><p><em>(Optional)</em> An amount applied to the player's <a
href="attack" class="wikilink" title="attack">attack</a>, <a
href="defense" class="wikilink" title="defense">defense</a>, <a
href="Magnetism" class="wikilink" title="magnetic radius">magnetic
radius</a>, maximum <a href="Energy" class="wikilink"
title="stamina">stamina</a>, <a href="speed" class="wikilink"
title="speed">speed</a>, <a href="immunity" class="wikilink"
title="immunity">immunity</a>, <a href="weight" class="wikilink"
title="weight">weight</a> multiplier, <a href="speed" class="wikilink"
title="weapon speed">weapon speed</a> multipler, <a href="attack"
class="wikilink" title="attack">attack</a> multiplier, <a
href="Crit._Chance" class="wikilink" title="crit chance">crit chance</a>
multiplier, <a href="Crit._Power" class="wikilink"
title="crit power">crit power</a> multiplier, or weapon percision
multiplier while the buff is active. This can be negative for a debuff.
Default 0.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>ActionsOnApply</samp></p></td>
<td><p><em>(Optional)</em> Run any number of <a
href="Modding_Trigger_actions" class="wikilink"
title="trigger action strings">trigger action strings</a> when the buff
is applied to the current player. For example, this increments a player
stat:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ActionsOnApply&quot;</span><span class="op">:</span> [</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;IncrementStat _NumberEaten 1&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>]</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Custom_fields" class="wikilink"
title="custom fields">custom fields</a> for this entry.</p></td>
</tr>
</tbody>
</table>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

## For C# mod authors

1.6 rewrites buffs to work more consistently and be more extensible:

- Buff logic is unified into `Game1.player.buffs`, which is the single
  source of truth for buff data. This replaces the previous
  `player.added*` and `player.appliedBuffs` fields, `BuffsDisplay`
  logic, enchantment stat bonuses, and boots/ring attribute changes on
  (un)equip.
- This also removes limitations on buff types (e.g. buffs can add weapon
  bonuses and weapons can add attribute buffs) and buffable equipment
  (e.g. equipped tools can have buffs too).
- Buff effects are now fully recalculated when they change, to fix a
  range of longstanding bugs like attribute drift and double-debuffs.
  Just like before, the buffs are managed locally; only the buff IDs and
  aggregate attribute effects are synced.

**For C# mods:**

- Each buff now has a unique string ID. You can apply a new buff with
  the same ID to replace it (so you no longer need to manually find and
  remove previous instances of the buff).
- The buff duration can now be set to `Buff.ENDLESS` to remove the
  duration. It'll last all day until the player sleeps.
- You can add standard buff effects to any equipment by overriding
  `Item.AddEquipmentEffects`, or add custom behaviour/buffs by
  overriding `Item.onEquip` and `Item.onUnequip`.
- You can add custom food or drink buffs by overriding
  `Item.GetFoodOrDrinkBuffs()`.
- The `Buff` constructor now supports a custom icon texture, sprite
  index, display name, description, and millisecond duration to fully
  support custom buffs.
- You can change how buff attributes are displayed (or add new
  attributes) by extending the `BuffsDisplay.displayAttributes` list.
- You can have invisible buffs by setting `buff.visible = false`.

For example, here's how to add a custom buff which adds +3 speed:

``` c#
Buff buff = new Buff(
    id: "Example.ModId_ZoomZoom",
    displayName: "Zoom Zoom", // can optionally specify description text too
    iconTexture: this.Helper.ModContent.Load<Texture2D>("assets/zoom.png"),
    iconSheetIndex: 0,
    duration: 30_000, // 30 seconds
    effects: new BuffEffects()
    {
        Speed = { 10 } // shortcut for buff.Speed.Value = 10
    }
);
Game1.player.applyBuff(buff);
```

You can also implement your own custom effects in code by checking if
the buff is active, like
`Game1.player.hasBuff("Example.ModId_ZoomZoom")`.

<a href="ru_Модификации_Бонусы" class="wikilink"
title="ru:Модификации:Бонусы">ru:Модификации:Бонусы</a>
<a href="zh_模组_效果" class="wikilink"
title="zh:模组:效果">zh:模组:效果</a>
