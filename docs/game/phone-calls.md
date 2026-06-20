---
title: "Phone Calls"
wiki_source: "Modding:Phone calls"
permalink: /Modding:Phone_calls/
category: game
tags: [phone-calls, incoming-calls-format, custom-handlers-in-c]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains phone calls. This is an advanced guide for mod
developers.

## Incoming calls format

You can add or customize incoming calls by editing the
`Data/IncomingPhoneCalls` asset.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  incoming call data.
- The value is a model with the fields listed below.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Dialogue</samp></p></td>
<td><p>The dialogue text to show when the player answers the phone. This
can use the full <a href="Modding_Dialogue" class="wikilink"
title="dialogue format">dialogue format</a> (including questions and
different dialogue based on the selected answer).</p></td>
</tr>
<tr>
<td><p><samp>FromNpc</samp></p></td>
<td><p><em>(Optional)</em> The internal name of the NPC making the call.
If specified, that NPC's name and portrait will be shown.</p></td>
</tr>
<tr>
<td><p><samp>FromPortrait</samp></p></td>
<td><p><em>(Optional)</em> The asset name for the portrait spritesheet
to display (like <samp>Portraits/Abigail</samp>). If
<samp>FromNpc</samp> is specified too, this overrides the portrait from
that NPC. If both <samp>FromNpc</samp> and <samp>FromDisplayName</samp>
are null, this portrait will be shown with the display name
"???".</p></td>
</tr>
<tr>
<td><p><samp>FromDisplayName</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the calling NPC's display name. If <samp>FromNpc</samp> is specified
too, this overrides the display name from that NPC.</p></td>
</tr>
<tr>
<td><p><samp>MaxCalls</samp></p></td>
<td><p><em>(Optional)</em> The maximum number of times a player can
receive this phone call, or <samp>-1</samp> for no limit. Default
1.</p></td>
</tr>
<tr>
<td><p><samp>TriggerCondition</samp><br />
<samp>RingCondition</samp></p></td>
<td><p><em>(Optional)</em> If set, a game state query which indicates
whether to trigger this phone call (<samp>TriggerCondition</samp>) or
whether the phone rings when this call is received
(<samp>RingCondition</samp>).</p>
<p>Whether a player receives this call depends on both fields:
<samp>TriggerCondition</samp> is checked on the main player before
sending the call to all players, then <samp>RingCondition</samp> is
checked on each player to determine whether the phone rings for
them.</p></td>
</tr>
<tr>
<td><p><samp>IgnoreBaseChance</samp></p></td>
<td><p><em>(Optional)</em> Whether to ignore the 1% base chance when
checking whether to trigger an incoming call. If true, the game will
check if this call can be received regardless of the base chance.
Default false.</p></td>
</tr>
<tr>
<td><p><samp>SimpleDialogueSplitBy</samp></p></td>
<td><p><em>(Optional, specialized)</em> If set, marks the call as having
a simple dialogue string without an NPC name and portrait, with lines
split into multiple boxes by this substring. For example,
<code>"SimpleDialogueSplitBy": "#"</code> will split
<code>Box A#Box B#Box C</code> into three consecutive dialogue
boxes.</p>
<p>You should omit this in most cases, and use the regular dialogue
format in <samp>Dialogue</samp> to split lines if needed. This is mainly
intended to support some older vanilla phone calls.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

## Custom handlers in C#

C# mods can implement `StardewValley.PhoneCalls.IPhoneHandler` and add
it to `Phone.PhoneHandlers` for full control over both incoming and
outgoing calls:

``` c#
/// <summary>The mod entry point.</summary>
internal sealed class ModEntry : Mod
{
    /// <inheritdoc />
    public override void Entry(IModHelper helper)
    {
        Phone.PhoneHandlers.Add(new CustomPhoneHandler());
    }
}

/// <summary>A custom phone handler.</summary>
internal sealed class CustomPhoneHandler : IPhoneHandler
{
    ...
}
```

See `StardewValley.PhoneCalls.DefaultPhoneHandler` in the
<a href="Modding_Modder_Guide_Get_Started#decompile" class="wikilink"
title="decompiled game code">decompiled game code</a> for an example
implementation.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Телефонные_звонки" class="wikilink"
title="ru:Модификации:Телефонные звонки">ru:Модификации:Телефонные
звонки</a> <a href="zh_模组_电话" class="wikilink"
title="zh:模组:电话">zh:模组:电话</a>
