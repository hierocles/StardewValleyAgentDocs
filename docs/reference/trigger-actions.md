---
title: "Trigger Actions"
wiki_source: "Modding:Trigger actions"
permalink: /Modding:Trigger_actions/
category: reference
tags: [trigger-actions, overview, introduction, argument-format, actions, built-in-actions, target-player, triggers]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents **trigger actions**, which let content packs perform
an action when something happens. (C# mods should usually use
<a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="SMAPI events">SMAPI events</a> instead.)

## Overview

### Introduction

A *trigger action* consists of two main parts:

- The *trigger* is what causes the action to happen. This can be an
  entry in `Data/TriggerActions`, an event command, etc. See
  <a href="#Triggers" class="wikilink" title="built-in triggers">built-in
  triggers</a>.
- The *action* is a space-delimited string which defines what to do. For
  example, `AddMail Current Robin` adds the `Robin` letter to the
  player's
  <a href="Modding_Mail_data" class="wikilink" title="mailbox">mailbox</a>
  tomorrow. See <a href="#Argument_format" class="wikilink"
  title="argument format">argument format</a> and
  <a href="#Actions" class="wikilink" title="built-in actions">built-in
  actions</a>.

### Argument format

Arguments are space-delimited. For example,
`AddMail Current Abigail_LeoMoved Now` calls the `AddMail` action with
three arguments (player: `Current`, mail ID: `Abigail_LeoMoved`, and
mail type: `Now`).

If you have spaces within an argument, you can surround it with quotes
to keep it together. For example, `AddFriendshipPoints "Mister Qi" 10`
has two arguments (`Mister Qi` and `10`). You can escape inner quotes
with backslashes, like `AddFriendshipPoints "Mister \"Qi\"" 10`.

Remember that quotes and backslashes inside JSON strings need to be
escaped too. For example, `"AddFriendshipPoints \"Mister Qi\" 10"` will
send `AddFriendshipPoints "Mister Qi" 10` to the game code.
Alternatively, you can use single-quotes for the JSON string instead,
like `'AddFriendshipPoints "Mister Qi" 10'`.

## Actions

### Built-in actions

These are the built-in actions which can be used by any
<a href="#Triggers" class="wikilink" title="trigger">trigger</a>. (Other
custom actions may be <a href="#For_C#_mod_authors" class="wikilink"
title="added by C# mods">added by C# mods</a>.)

<table>
<thead>
<tr>
<th><p>action</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>AddBuff &lt;buff ID&gt; [milliseconds
duration]</samp><br />
<samp>RemoveBuff &lt;buff ID&gt;</samp></p></td>
<td><p>Apply or remove a buff ID for the current player. For
<samp>AddBuff</samp>, duration defaults to the buff's default duration
if not specified; this value can be <samp>-2</samp> to make the buff
last the entire day.</p></td>
</tr>
<tr>
<td><p><samp>AddConversationTopic &lt;topic ID&gt;
[days]</samp></p></td>
<td><p>Start a <a href="Modding_Dialogue#Conversation_topics"
class="wikilink" title="conversation topic">conversation topic</a> for
the given number of [days] (default 4). If the topic is already active,
this resets its duration to the given number.</p></td>
</tr>
<tr>
<td><p><samp>RemoveConversationTopic &lt;topic ID&gt;</samp></p></td>
<td><p>End a <a href="Modding_Dialogue#Conversation_topics"
class="wikilink" title="conversation topic">conversation topic</a>, if
it's active.</p></td>
</tr>
<tr>
<td><p><samp>AddFriendshipPoints &lt;NPC name&gt;
&lt;count&gt;</samp></p></td>
<td><p>Add &lt;count&gt; <a href="Friendship" class="wikilink"
title="friendship points">friendship points</a> between the current
player and specified NPC. The &lt;count&gt; can be negative to reduce
friendship points.</p></td>
</tr>
<tr>
<td><p><samp>AddItem &lt;item ID&gt; [count] [quality]</samp></p></td>
<td><p>Add an item by its <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_items"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a> to the current player's inventory, with an
optional count (default 1) and <a href="Modding_Items#Quality"
class="wikilink" title="quality">quality</a> (default 0).</p></td>
</tr>
<tr>
<td><p><samp>RemoveItem &lt;item ID&gt; [count]</samp></p></td>
<td><p>Deduct items by <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_items"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a> from the current player's inventory, up to a max
combined stack size of [count] (default 1).</p></td>
</tr>
<tr>
<td><p><samp>AddMail &lt;player&gt; &lt;mail ID&gt; [type]</samp><br />
<samp>RemoveMail &lt;player&gt; &lt;mail ID&gt; [type]</samp></p></td>
<td><p>Add or remove a <a href="Modding_Mail_data" class="wikilink"
title="mail flag or letter">mail flag or letter</a> for the <a
href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a>.</p>
<p>The &lt;type&gt; must be one of:</p>
<table>
<thead>
<tr>
<th><p>type</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>now</samp></p></td>
<td><p>In the player's mailbox now.</p></td>
</tr>
<tr>
<td><p><samp>tomorrow</samp></p></td>
<td><p>In the player's list of mail arriving in the mailbox
tomorrow.</p></td>
</tr>
<tr>
<td><p><samp>received</samp></p></td>
<td><p>In the player's list of received mail (bypassing the
mailbox).</p></td>
</tr>
<tr>
<td><p><samp>all</samp></p></td>
<td><p>Add or remove it everywhere (mailbox, tomorrow's mailbox, and
received mail).</p></td>
</tr>
</tbody>
</table>
<p>If omitted, the &lt;type&gt; defaults to <samp>tomorrow</samp> for
<samp>AddMail</samp> and <samp>all</samp> for
<samp>RemoveMail</samp>.</p></td>
</tr>
<tr>
<td><p><samp>AddMoney &lt;amount&gt;</samp></p></td>
<td><p>Add the given &lt;amount&gt; of money for the current player. The
&lt;amount&gt; can be negative to deduct money.</p></td>
</tr>
<tr>
<td><p><samp>AddQuest &lt;quest ID&gt;</samp><br />
<samp>RemoveQuest &lt;quest ID&gt;</samp></p></td>
<td><p>Add or remove a <a href="Modding_Quest_data" class="wikilink"
title="quest">quest</a> for the current player.</p></td>
</tr>
<tr>
<td><p><samp>AddSpecialOrder &lt;order ID&gt;</samp><br />
<samp>RemoveSpecialOrder &lt;order ID&gt;</samp></p></td>
<td><p>Add or remove a <a href="Modding_Special_orders" class="wikilink"
title="special order">special order</a>.</p></td>
</tr>
<tr>
<td><p><samp>If &lt;query&gt; ## &lt;action if true&gt;</samp><br />
<samp>If &lt;query&gt; ## &lt;action if true&gt; ## &lt;action if
false&gt;</samp></p></td>
<td><p>Check a <a href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> and perform an action
based on the result.</p>
<p>For example, this only sends a mail if the player doesn't have it in
their received, mailbox, or queued-for-tomorrow mail:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ActionsOnPurchase&quot;</span><span class="er">:</span> <span class="ot">[</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;If !PLAYER_HAS_MAIL Current SomeFlag ## AddMail Current SomeFlag&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>IncrementStat &lt;stat key&gt; [amount]</samp></p></td>
<td><p>Increment a <a href="Modding_Stats" class="wikilink"
title="stat value">stat value</a> by the given amount (default 1) for
the current player. The amount can be negative to decrement it, but
can't be reduced below 0.</p></td>
</tr>
<tr>
<td><p><samp>MarkActionApplied &lt;player&gt; &lt;answer ID&gt;
[applied]</samp></p></td>
<td><p>Mark a <samp>Data/TriggerActions</samp> entry as applied or
non-applied for the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a>, depending on
[applied] (default <samp>true</samp>). This can be used to skip or
re-run an entry, since <samp>Data/TriggerActions</samp> entries are only
applied once by default.</p>
<p>Note that an entry can't use this to mark <em>itself</em> unapplied;
see <a href="#Make_Data_TriggerActions_repeat" class="wikilink"
title="Make Data/TriggerActions repeat"><em>Make
<samp>Data/TriggerActions</samp> repeat</em></a> if you want to do
that.</p></td>
</tr>
<tr>
<td><p><samp>MarkCookingRecipeKnown &lt;player&gt; &lt;recipe ID&gt;
[known]</samp><br />
<samp>MarkCraftingRecipeKnown &lt;player&gt; &lt;recipe key&gt;
[known]</samp></p></td>
<td><p>Set whether <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a> know a <a
href="Modding_Recipe_data" class="wikilink"
title="cooking or crafting recipe">cooking or crafting recipe</a>,
depending on [known] (default <samp>true</samp>).</p>
<p>Note that forgetting a recipe will also reset its
times-cooked/crafted counter to zero.</p></td>
</tr>
<tr>
<td><p><samp>MarkEventSeen &lt;player&gt; &lt;event ID&gt;
[seen]</samp></p></td>
<td><p>Mark <a href="Modding_Event_data" class="wikilink"
title="an event">an event</a> as seen or unseen for the <a
href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a>, depending on [seen]
(default <samp>true</samp>).</p></td>
</tr>
<tr>
<td><p><samp>MarkQuestionAnswered &lt;player&gt; &lt;answer ID&gt;
[answered]</samp></p></td>
<td><p>Mark <a href="Modding_Dialogue#Response_IDs" class="wikilink"
title="a dialogue answer">a dialogue answer</a> as selected or
non-selected for the <a href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a>, depending on
[answered] (default <samp>true</samp>).</p></td>
</tr>
<tr>
<td><p><samp>MarkSongHeard &lt;player&gt; &lt;song ID&gt;
[heard]</samp></p></td>
<td><p>Mark a song track's cue name heard or non-heard for the <a
href="#Target_player" class="wikilink"
title="specified player(s)">specified player(s)</a>, depending on
[heard] (default <samp>true</samp>). This affects whether the song
appears in the <a href="jukebox" class="wikilink"
title="jukebox">jukebox</a> selection.</p></td>
</tr>
<tr>
<td><p><samp>Null</samp></p></td>
<td><p><em>(Specialized)</em> Does nothing. This is used internally;
there's generally no benefit to using it yourself.</p></td>
</tr>
<tr>
<td><p><samp>RemoveTemporaryAnimatedSprites</samp></p></td>
<td><p>Remove all temporary animated sprites in the current location.
For example, this can be used in the <a href="Modding_Event_data"
class="wikilink" title="event">event</a> <samp>setSkipActions</samp>
command to clean up the event's temporary sprites.</p></td>
</tr>
<tr>
<td><p><samp>SetNpcInvisible &lt;NPC name&gt; &lt;day
duration&gt;</samp></p></td>
<td><p>Hide an NPC so they disappear and can't be interacted with for
the given number of days. This is used when NPCs go away for a while
(e.g. <a href="Elliott#Fourteen_Hearts" class="wikilink"
title="Elliott&#39;s 14-heart event">Elliott's 14-heart event</a>).</p>
<p><strong>TODO: can you call this from the farmhand? Atra doesn't think
so.</strong></p></td>
</tr>
<tr>
<td><p><samp>SetNpcVisible &lt;NPC name&gt;</samp></p></td>
<td><p>End the NPC's invisibility, if applicable.</p>
<p><strong>TODO: check to see if can be called from farmhand. Will
probably make the NPC visible again, but the daysUntilNotInvisible is
NOT synced.</strong></p></td>
</tr>
</tbody>
</table>

### Target player

Some conditions have a \<player\> argument. This can be one of...

| value | result |
|----|----|
| `All` | Apply the action to all players (regardless of whether they're online). |
| `Current` | Apply to the local player. |
| `Host` | Apply to the main player. |

## Triggers

### `Data/TriggerActions`

`Data/TriggerActions` is a data asset which lets you dynamically perform
actions when the conditions are met.

For example, consider this
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> patch:

You can read that like: "*When the player is going to sleep, if Leo has
moved to the valley, then
<a href="Modding_Mail_data" class="wikilink" title="send a letter">send
a letter</a> and start
<a href="Modding_Dialogue#Conversation_topics" class="wikilink"
title="a conversation topic">a conversation topic</a>*".

Each entry in `Data/TriggerActions` only runs once by default, though
you can use the `MarkActionApplied` action to re-enable one.

`Data/TriggerActions` consists of a list of models with these fields:

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
trigger action.</p></td>
</tr>
<tr>
<td><p><samp>Trigger</samp></p></td>
<td><p>When to apply the trigger action. This must be one or more of
these values (space-delimited):</p>
<table>
<thead>
<tr>
<th><p>trigger</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DayStarted</samp></p></td>
<td><p>Raised when the player starts a day, after either sleeping or
loading. This happens before SMAPI's <samp>DayStarted</samp>
<em>and</em> <samp>SaveLoaded</samp> events.</p></td>
</tr>
<tr>
<td><p><samp>DayEnding</samp></p></td>
<td><p>Raised when the player is going to sleep. This happens
immediately before the game changes the date, sets up the new day, and
saves.</p></td>
</tr>
<tr>
<td><p><samp>LocationChanged</samp></p></td>
<td><p>Raised when the player arrives in a location.</p></td>
</tr>
<tr>
<td><p><em>other</em></p></td>
<td><p>Other custom triggers may be <a href="#For_C#_mod_authors"
class="wikilink" title="added by C# mods">added by C# mods</a>.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Actions</samp></p></td>
<td><p><em>(Optional)</em> The actions to perform, as a list of strings
matching the <a href="#Actions" class="wikilink"
title="action format">action format</a>.</p></td>
</tr>
<tr>
<td><p><samp>Action</samp></p></td>
<td><p><em>(Optional)</em> A single action to perform, matching the <a
href="#Actions" class="wikilink" title="action format">action
format</a>.</p>
<p>This is just a shortcut for <samp>Actions</samp> with one action.
Technically you can use both together, but usually you should just pick
one property to set.</p></td>
</tr>
<tr>
<td><p><samp>HostOnly</samp></p></td>
<td><p><em>(Optional)</em> Whether this trigger action can only run for
the main player. If true, the action will be ignored for farmhands in <a
href="multiplayer" class="wikilink"
title="multiplayer">multiplayer</a>.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this action can be applied currently. Defaults to
always true.</p></td>
</tr>
<tr>
<td><p><samp>MarkActionApplied</samp></p></td>
<td><p><em>(Optional)</em> Whether to mark the action applied when it's
applied. Default true.</p>
<ul>
<li>If true: the action is added to the player's
<samp>triggerActionsRun</samp> list, <a
href="Modding_Game_state_queries" class="wikilink"
title="queries">queries</a> like
<samp>PLAYER_HAS_RUN_TRIGGER_ACTION</samp> will return true, and the
action won't run again (unless you use the
<samp>MarkActionApplied</samp> action to mark it unapplied).</li>
<li>If false: the action can repeat immediately when the same trigger is
raised, and <a href="Modding_Game_state_queries" class="wikilink"
title="queries">queries</a> like
<samp>PLAYER_HAS_RUN_TRIGGER_ACTION</samp> will return false for
it.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>SkipPermanentlyCondition</samp></p></td>
<td><p><em>(Optional)</em> If set, a <a
href="Modding_Game_state_queries" class="wikilink"
title="game state query">game state query</a> which indicates that the
action should be marked applied when this condition matches. This
happens before <samp>Condition</samp>, <samp>Action</samp>, and
<samp>Actions</samp> are applied.</p>
<p>This mainly allows optimizing cases where the action will never be
applied, to avoid parsing the <samp>Condition</samp> each time.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_data_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

### Elsewhere

You can also run an action directly from...

- A <a href="Modding_Dialogue" class="wikilink"
  title="dialogue string">dialogue string</a> using the `$action`
  command. For example:
  ``` json
  "Mon": "Hi there! Here's 10g and a parsnip, don't spend it all at once.#$action AddMoney 10#$action AddItem (O)24"
  ```
- An
  <a href="Modding_Event_data" class="wikilink" title="event script">event
  script</a> using the `action` command. For example:
  ``` json
  "_Event": "continue/64 15/farmer 64 16 2 Abigail 64 18 0/pause 1500/speak Abigail \"Hi. Here's 10g and a parsnip.\"/action AddMoney 10/action AddItem (O)24/pause 500/end"
  ```

  See also the `setSkipActions` command.
- A
  <a href="Modding_Mail_data" class="wikilink" title="mail letter">mail
  letter</a> using the `%action` command. For example:
  ``` json
  "_Letter": "Hey there!^Here's 10g and a parsnip. Take care!^   -Abigail%action AddMoney 10%% %action Additem (O)24%%[#]A gift from Abigail"
  ```
- The <a href="Modding_Console_commands" class="wikilink"
  title="SMAPI console window">SMAPI console window</a> using the
  `debug action` console command. For example:
      > debug action "AddMoney 10"

      Applied action 'AddMoney 10'.

## For C# mod authors

### Using trigger actions in C# data

Trigger actions are mainly meant for
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher packs">Content Patcher packs</a>. C# mod can use
<a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="SMAPI&#39;s events">SMAPI's events</a> instead, which are much
more flexible and efficient (unless you want to let content packs edit
your trigger actions).

### Extensibility

C# mods can use the `StardewValley.Triggers.TriggerActionManager` class
to interact with trigger actions.

For example, you can...

- Add and raise a new trigger type:
  ``` c#
  // register custom trigger type
  TriggerActionManager.RegisterTrigger("Some.ModId_OnItemReceived");

  // run actions in Data/TriggerActions for the custom trigger
  TriggerActionManager.Raise("Some.ModId_OnItemReceived", new[] { item, index }); // trigger can pass optional trigger arguments
  ```
- Or add a new action:
  ``` c#
  TriggerActionManager.RegisterAction("Some.ModId_PlaySound", this.PlaySound);

  ...

  /// <inheritdoc cref="TriggerActionDelegate" />
  public static bool PlaySound(string[] args, TriggerActionContext context, out string error)
  {
      // get args
      if (!ArgUtility.TryGet(args, 1, out string soundId, out error, allowBlank: false))
          return false;

      // apply
      Game1.playSound(soundId);
      return true;
  }
  ```
- Or run an action string:
  ``` c#
  // NOTE: this is just an example of how to run an action. This is meant to support actions specified in data or content
  // packs. If you want to send mail (or perform other actions) in C#, it's better to call the C# APIs directly instead.
  string action = "AddMail Current Robin Now";
  if (!TriggerActionManager.TryRunAction(action, out string error, out Exception ex))
      Game1.log.Error($"Failed running action '{action}': {error}", ex);
  ```

To avoid conflicts, custom trigger names should be
<a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string IDs">unique string IDs</a>.

## FAQs

### Trigger actions vs map actions

*Actions* can refer to two different systems:

- *Trigger actions* (this page) let you perform generic background tasks
  that can be done anytime, like sending a letter or starting a quest.
  These can be triggered automatically based on conditions, or via
  commands in dialogue, events, etc.
- *<a href="Modding_Maps" class="wikilink" title="Map actions">Map
  actions</a>* refer to the `Action` and `TouchAction` map properties,
  which do something when you walk on or interact with a map tile. These
  can perform a wide array of map- and interaction-specific things like
  showing a message box, changing the map, opening shop menus, etc.
  These only work in maps, and generally don't make sense in other
  contexts.

Aside from the similar names, they're not interchangeable and there's
fairly little overlap.

### Make `Data/TriggerActions` repeat

By default, each entry in `Data/TriggerActions` is only applied once per
player.

There are two main ways to repeat actions:

- To make it repeatable immediately, set `"MarkActionApplied": false` on
  the `Data/TriggerActions` entry.

<li>

To enable repeating at a different time, you can use the
`MarkActionApplied` action to forget that it was applied.

For example, this patch will set alternating 'work' or 'weekend' mail
flags depending on the day of week:

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Триггерные_действия" class="wikilink"
title="ru:Модификации:Триггерные действия">ru:Модификации:Триггерные
действия</a> <a href="zh_模组_触发动作" class="wikilink"
title="zh:模组:触发动作">zh:模组:触发动作</a>
