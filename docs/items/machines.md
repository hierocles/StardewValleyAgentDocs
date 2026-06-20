---
title: "Machines"
wiki_source: "Modding:Machines"
permalink: /Modding:Machines/
category: items
tags: [machines, definitions, data-format, item-processing-rules, behavior-tweaks, audio-visuals, player-interaction-messages, advanced-logic]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how to add/edit machines in the game data. This is an
advanced guide for modders.

## Definitions

A "machine" is a placeable object which takes input and/or produces
output based on the rules in `Data/Machines`. A machine doesn't need to
do both (e.g.
<a href="Solar_Panel" class="wikilink" title="solar panels">solar
panels</a> produce output without accepting input), and it's not
necessarily something players would intuitively consider a machine (e.g.
<a href="incubator" class="wikilink" title="incubator">incubators</a>
and
<a href="Mushroom_Log" class="wikilink" title="mushroom logs">mushroom
logs</a> are machines).

## Data format

You can add/edit machine logic by editing the `Data/Machines`
<a href="Modding_Editing_XNB_files" class="wikilink"
title="asset">asset</a>.

This consists of a string → model lookup, where...

- The key is the
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="qualified item ID"><strong>qualified</strong> item ID</a> for
  the item which acts as a machine (like `(BC)127` for
  <a href="The_Cave" class="wikilink" title="mushroom boxes">mushroom
  boxes</a>).
- The value is a model with the fields listed below.

### Item processing rules

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>OutputRules</samp></p></td>
<td><p>The output produced by this machine. If multiple output rules can
be produced, the first available one is selected. This consists of a
list of models with these fields:</p>
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
rule within the current machine (it doesn't need to be unique between
machines).</p></td>
</tr>
<tr>
<td><p><samp>Triggers</samp></p></td>
<td><p>When to apply this output rule. This can list any number of
triggers; the output will apply if any of them match.</p>
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
trigger within the current rule.</p></td>
</tr>
<tr>
<td><p><samp>Trigger</samp></p></td>
<td><p><em>(Optional)</em> When this output rule applies. Defaults to
<samp>ItemPlacedInMachine</samp>. The possible values are...</p>
<ul>
<li><samp>ItemPlacedInMachine</samp>: apply this rule when an item is
placed into the machine. This is the most common machine behavior.</li>
<li><samp>OutputCollected</samp>: apply this rule when the machine's
previous output is collected. An output-collected rule won't require or
consume the input items, and the input item will be the previous output.
For example, this is used to reload the <a href="crystalarium"
class="wikilink" title="crystalarium">crystalarium</a>.</li>
<li><samp>MachinePutDown</samp>: apply this rule when the machine is put
down. For example, this is used to start the <a href="Worm_Bin"
class="wikilink" title="worm bin">worm bin</a>.</li>
<li><samp>DayUpdate</samp>: apply this rule when a new day starts, if it
isn't already processing output. For example, this is used for the <a
href="Soda_Machine" class="wikilink" title="soda machine">soda
machine</a>.</li>
</ul>
<p>You can specify multiple values, like
<code>"Trigger": "DayUpdate, MachinePutDown, OutputCollected"</code>.</p></td>
</tr>
<tr>
<td><p><samp>RequiredItemId</samp></p></td>
<td><p><em>(Optional)</em> The qualified or unqualified item ID for the
item to match, if the trigger is <samp>ItemPlacedInMachine</samp> or
<samp>OutputCollected</samp>. Defaults to allowing any item ID.</p></td>
</tr>
<tr>
<td><p><samp>RequiredTags</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Context_tags"
class="wikilink" title="context tags">context tags</a> to match against
input items, if the trigger is <samp>ItemPlacedInMachine</samp> or
<samp>OutputCollected</samp>. An item must have all of the listed tags
to select this rule. You can negate a tag with <samp>!</samp> (like
<code>"RequiredTags": [ "bone_item", "!fossil_item" ]</code> for bone
items that aren't fossils).</p></td>
</tr>
<tr>
<td><p><samp>RequiredCount</samp></p></td>
<td><p><em>(Optional)</em> The required stack size for the input item,
if the trigger is <samp>ItemPlacedInMachine</samp> or
<samp>OutputCollected</samp>. Default 1.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this trigger should be checked. Item-only tokens are
valid for this check if the trigger is <samp>ItemPlacedInMachine</samp>
or <samp>OutputCollected</samp>. Defaults to always true.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>OutputItem</samp></p></td>
<td><p>The items produced by this machine. If multiple output entries
match, one will be selected randomly unless you specify
<samp>UseFirstValidOutput</samp>. This consists of a list of models with
these fields:</p>
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
generic item fields supported by machine output.</p>
<p>Notes:</p>
<ul>
<li>If <samp>ItemId</samp> or <samp>RandomItemId</samp> is set to an <a
href="Modding_Item_queries" class="wikilink" title="item query">item
query</a> which returns multiple items, one item will be selected at
random.</li>
<li>The <samp>ItemId</samp> and <samp>RandomItemId</samp> can optionally
contain special tokens, which will be replaced before the item ID is
parsed. For example, you can use
<code>FLAVORED_ITEM Wine DROP_IN_ID</code> to create a wine for whatever
item was placed in the machine.
<table>
<thead>
<tr>
<th><p>token</p></th>
<th><p>replaced with</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DROP_IN_ID</samp></p></td>
<td><p>The qualified item ID for the item placed in the
machine.</p></td>
</tr>
<tr>
<td><p><samp>DROP_IN_PRESERVE</samp></p></td>
<td><p>If the item placed into the machine is a flavored item like Apple
Juice or Tuna Roe, the <em>unqualified</em> item ID for the flavor item
(e.g. the apple in Apple Wine). Otherwise <samp>0</samp>.</p></td>
</tr>
<tr>
<td><p><samp>NEARBY_FLOWER_ID</samp></p></td>
<td><p>The item ID for a flower within 5 tiles of the machine, or
<samp>-1</samp> if no flower is found. For example, <a href="Bee_House"
class="wikilink" title="bee houses">bee houses</a> produce
<code>FLAVORED_ITEM Honey NEARBY_FLOWER_ID</code>.</p></td>
</tr>
</tbody>
</table></li>
<li>The <samp>ObjectInternalName</samp> can optionally contain
<samp>{0}</samp>, which will be replaced with the input item's internal
name. This is used to prevent flavored items from stacking
(<em>e.g.</em> apple <a href="wine" class="wikilink"
title="wine">wine</a> and blueberry wine).</li>
<li>The <samp>Condition</samp> field will check the <em>input</em> (not
output) item for item-related conditions.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>PreserveType</samp></p></td>
<td><p><em>(Optional)</em> The produced item's preserved item type, if
applicable. This sets the equivalent flag on the output item. The valid
values are <samp>Jelly</samp>, <samp>Juice</samp>, <samp>Pickle</samp>,
<samp>Roe</samp> or <samp>AgedRoe</samp>, and <samp>Wine</samp>.
Defaults to none.</p></td>
</tr>
<tr>
<td><p><samp>PreserveId</samp></p></td>
<td><p><em>(Optional)</em> The produced item's preserved unqualified
item ID, if applicable. For example, <a href="Wine" class="wikilink"
title="blueberry wine">blueberry wine</a> has its preserved item ID set
to the <a href="blueberry" class="wikilink"
title="blueberry">blueberry</a> ID. This can be set to
<samp>DROP_IN</samp> to use the input item's ID, or
<samp>DROP_IN_PRESERVE</samp> to use the input item's flavor, if it's a
flavored item. Default none.</p></td>
</tr>
<tr>
<td><p><samp>CopyColor</samp></p></td>
<td><p><em>(Optional)</em> Whether to inherit the color of the input
item. If the input is a <samp>ColoredObject</samp> the output will
inherit its exact color; otherwise it will use the <a href="Dyeing"
class="wikilink" title="dye color">dye color</a> from the input item's
context tags. Default false.</p></td>
</tr>
<tr>
<td><p><samp>CopyPrice</samp></p></td>
<td><p><em>(Optional)</em> Whether to inherit the base price of the
input item (before <samp>PriceModifiers</samp> are applied). This is
ignored if the input or output aren't both object
(<samp>(O)</samp>)-type.</p></td>
</tr>
<tr>
<td><p><samp>CopyQuality</samp></p></td>
<td><p><em>(Optional)</em> Whether to inherit the quality of the input
item (before <samp>QualityModifiers</samp> are applied).</p></td>
</tr>
<tr>
<td><p><samp>PriceModifiers</samp><br />
<samp>PriceModifiers</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="Quantity modifiers">Quantity modifiers</a>
applied to the output item's price. Default none.</p></td>
</tr>
<tr>
<td><p><samp>IncrementMachineParentSheetIndex</samp></p></td>
<td><p><em>(Optional)</em> An amount by which to increment the machine's
spritesheet index while it's processing this output. This stacks with
the <samp>ShowNextIndexWhenLoaded</samp> or
<samp>ShowNextIndexWhileWorking</samp> field. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>OutputMethod</samp></p></td>
<td><p><em>(Optional, specialized)</em> A C# method which decides which
item to produce. If set, the <samp>ItemId</samp> field is optional and
ignored.</p>
<p>This must be specified in the form <samp>&lt;full type name&gt;:
&lt;method name&gt;</samp> (like <samp>StardewValley.Object, Stardew
Valley: OutputSolarPanel</samp>). The method must be static and match
the game's <samp>MachineOutputDelegate</samp> method signature:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;summary&gt;</span><span class="co">Get the output item to produce.</span><span class="kw">&lt;/summary&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;param</span><span class="ot"> name=</span><span class="dt">&quot;machine&quot;</span><span class="kw">&gt;</span><span class="co">The machine instance for which to produce output.</span><span class="kw">&lt;/param&gt;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;param</span><span class="ot"> name=</span><span class="dt">&quot;inputItem&quot;</span><span class="kw">&gt;</span><span class="co">The item being dropped into the machine, if applicable.</span><span class="kw">&lt;/param&gt;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;param</span><span class="ot"> name=</span><span class="dt">&quot;probe&quot;</span><span class="kw">&gt;</span><span class="co">Whether the machine is only checking whether the input is valid. If so, the input/machine shouldn&#39;t be changed and no animations/sounds should play.</span><span class="kw">&lt;/param&gt;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;param</span><span class="ot"> name=</span><span class="dt">&quot;outputData&quot;</span><span class="kw">&gt;</span><span class="co">The item output data from </span><span class="kw">&lt;c&gt;</span><span class="co">Data/Machines</span><span class="kw">&lt;/c&gt;</span><span class="co"> for which output is being created, if applicable.</span><span class="kw">&lt;/param&gt;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;param</span><span class="ot"> name=</span><span class="dt">&quot;overrideMinutesUntilReady&quot;</span><span class="kw">&gt;</span><span class="co">The in-game minutes until the item will be ready to collect, if set. This overrides the equivalent fields in the machine data if set.</span><span class="kw">&lt;/param&gt;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;returns&gt;</span><span class="co">Returns the item to produce, or </span><span class="kw">&lt;c&gt;</span><span class="co">null</span><span class="kw">&lt;/c&gt;</span><span class="co"> if none should be produced.</span><span class="kw">&lt;/returns&gt;</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="kw">public</span> <span class="kw">static</span> Item <span class="fu">GetOutput</span><span class="op">(</span>Object machine<span class="op">,</span> Item inputItem<span class="op">,</span> <span class="dt">bool</span> probe<span class="op">,</span> MachineItemOutput outputData<span class="op">,</span> Farmer player<span class="op">,</span> <span class="kw">out</span> <span class="dt">int</span><span class="op">?</span> overrideMinutesUntilReady<span class="op">)</span></span></code></pre></div>
<p>If this method returns null, the machine won't output
anything.</p></td>
</tr>
<tr>
<td><p><samp>CustomData</samp></p></td>
<td><p>Machine-specific data provided to the machine logic, if
applicable.</p>
<p>For example, the cask uses this to set the aging rate for each
item:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;OutputItem&quot;</span><span class="op">:</span> {</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;OutputMethod&quot;</span><span class="op">:</span> <span class="st">&quot;StardewValley.Objects.Cask, Stardew Valley: OutputCask&quot;</span><span class="op">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;CustomData&quot;</span><span class="op">:</span> {</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;AgingMultiplier&quot;</span><span class="op">:</span> <span class="dv">4</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>UseFirstValidOutput</samp></p></td>
<td><p><em>(Optional)</em> If multiple <samp>OutputItem</samp> entries
match, whether to use the first match instead of choosing one randomly.
Default false.</p></td>
</tr>
<tr>
<td><p><samp>MinutesUntilReady</samp><br />
<samp>DaysUntilReady</samp></p></td>
<td><p><em>(Optional)</em> The number of in-game minutes or days until
the output is ready to collect. If both days and minutes are specified,
days are used. If none are specified, the item will be ready
instantly.</p></td>
</tr>
<tr>
<td><p><samp>InvalidCountMessage</samp></p></td>
<td><p><em>(Optional)</em> If set, overrides the machine's main
<samp>InvalidCountMessage</samp> field.</p></td>
</tr>
<tr>
<td><p><samp>RecalculateOnCollect</samp></p></td>
<td><p><em>(Optional)</em> Whether to regenerate the output right before
the player collects it, similar to <a href="Bee_House" class="wikilink"
title="bee houses">bee houses</a>. If the new item is null, the original
output is returned instead.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>AdditionalConsumedItems</samp></p></td>
<td><p><em>(Optional)</em> A list of extra items required before
<samp>OutputRules</samp> will be checked. If specified, every listed
item must be present in the player, <a href="hopper" class="wikilink"
title="hopper">hopper</a>, or chest inventory (depending how the machine
is being loaded).</p>
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
<td><p><samp>ItemId</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a> for the required item.</p></td>
</tr>
<tr>
<td><p><samp>RequiredCount</samp></p></td>
<td><p><em>(Optional)</em> The required stack size for the item matching
<samp>ItemId</samp>. Default 1.</p></td>
</tr>
<tr>
<td><p><samp>InvalidCountMessage</samp></p></td>
<td><p><em>(Optional)</em> If set, overrides the machine's main
<samp>InvalidCountMessage</samp> field.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>AllowFairyDust</samp></p></td>
<td><p><em>(Optional)</em> Whether the player can add <a
href="Fairy_Dust" class="wikilink" title="fairy dust">fairy dust</a> to
speed up the machine. Default true.</p></td>
</tr>
<tr>
<td><p><samp>ReadyTimeModifiers</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="Quantity modifiers">Quantity modifiers</a>
applied to the produced item's processing time. The modifier conditions
can use item-only tokens, which will check the <em>input</em> (not
output) item.</p></td>
</tr>
<tr>
<td><p><samp>ReadyTimeModifierMode</samp></p></td>
<td><p><em>(Optional)</em> A <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="quantity modifier mode">quantity modifier
mode</a> which indicates what to do if multiple modifiers apply at the
same time. Default <samp>Stack</samp>.</p></td>
</tr>
</tbody>
</table>

### Behavior tweaks

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>OnlyCompleteOvernight</samp></p></td>
<td><p><em>(Optional)</em> Whether the machine should only produce
output overnight. If enabled and it finishes processing during the day,
it'll pause until its next day update. Default false.</p></td>
</tr>
<tr>
<td><p><samp>PreventTimePass</samp></p></td>
<td><p><em>(Optional)</em> A list of cases when the machine should be
paused, so the timer on any item being produced doesn't decrement.
Possible values:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Outside</samp><br />
<samp>Inside</samp></p></td>
<td><p>Pause when placed in an outside or inside location. For example,
<a href="Bee_House" class="wikilink" title="bee houses">bee houses</a>
don't work inside.</p></td>
</tr>
<tr>
<td><p><samp>Spring</samp><br />
<samp>Summer</samp><br />
<samp>Fall</samp><br />
<samp>Winter</samp></p></td>
<td><p>Pause in the given season. For example, <a href="Bee_House"
class="wikilink" title="bee houses">bee houses</a> don't work in
winter.</p></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>Sun</samp><br />
<samp>Rain</samp></p></td>
<td><p>Pause on days with the given weather.</p></td>
</tr>
<tr>
<td><p><samp>Always</samp></p></td>
<td><p>Always pause the machine. This is used in specialized cases where
the timer is handled by <a href="#Advanced_logic" class="wikilink"
title="advanced machine logic">advanced machine logic</a>.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>AllowLoadWhenFull</samp></p></td>
<td><p><em>(Optional)</em> Whether the player can drop a new item into
the machine before it's done processing the last one (like the <a
href="crystalarium" class="wikilink"
title="crystalarium">crystalarium</a>). The previous item will be lost.
Default false.</p></td>
</tr>
<tr>
<td><p><samp>ClearContentsOvernightCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the machine should be emptied overnight, so any
current output will be lost. Defaults to always false.</p></td>
</tr>
</tbody>
</table>

### Audio & visuals

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>LoadEffects</samp><br />
<samp>WorkingEffects</samp></p></td>
<td><p><em>(Optional)</em> The cosmetic effects shown when an item is
loaded into the machine (for <samp>LoadEffects</samp>), or while it's
processing the item (for <samp>WorkingEffects</samp>, based on the
<samp>WorkingEffectChance</samp> probability). Both default to none.
These consist of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this effect should be played. For item queries, you
can check the input item (<samp>Input&lt;/samp) or output item
(&lt;samp&gt;Target</samp>). Defaults to always true.</p></td>
</tr>
<tr>
<td><p><samp>Sounds</samp></p></td>
<td><p><em>(Optional)</em> The audio to play. This consists of a list of
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
<td><p>The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> to play.</p></td>
</tr>
<tr>
<td><p><samp>Delay</samp></p></td>
<td><p><em>(Optional)</em> The number of milliseconds until the sound
should play. Default 0.</p></td>
</tr>
</tbody>
</table>
<p>Defaults to no sound.</p></td>
</tr>
<tr>
<td><p><samp>ShakeDuration</samp></p></td>
<td><p><em>(Optional)</em> A duration in milliseconds during which the
machine sprite should shake. Default none.</p></td>
</tr>
<tr>
<td><p><samp>Frames</samp></p></td>
<td><p><em>(Optional)</em> The animation to apply to the machine sprite,
specified as a list of offsets relative to the base sprite index.
Default none.</p></td>
</tr>
<tr>
<td><p><samp>Interval</samp></p></td>
<td><p><em>(Optional)</em> The number of milliseconds for which each
frame in <samp>Frames</samp> is kept on-screen. Default 100.</p></td>
</tr>
<tr>
<td><p><samp>TemporarySprites</samp></p></td>
<td><p><em>(Optional)</em> The temporary animated sprites to show. This
consists of a list of models with these fields:</p>
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
rule within the current machine (it doesn't need to be unique between
machines).</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p>The asset name for the texture (under the game's
<samp>Content</samp> folder) for the animated sprite.</p></td>
</tr>
<tr>
<td><p><samp>SourceRect</samp></p></td>
<td><p>The pixel area for the first animated frame within the
<samp>Texture</samp>, specified as an object with <samp>X</samp>,
<samp>Y</samp>, <samp>Width</samp>, and <samp>Height</samp>
fields.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether to add this temporary sprite.</p></td>
</tr>
<tr>
<td><p><samp>PositionOffset</samp></p></td>
<td><p><em>(Optional)</em> A pixel offset applied to the sprite,
relative to the top-left corner of the machine's collision box,
specified as an object with <samp>X</samp> and <samp>Y</samp> fields.
Defaults to (0, 0).</p></td>
</tr>
<tr>
<td><p><samp>Color</samp></p></td>
<td><p><em>(Optional)</em> A tint color to apply to the sprite. See <a
href="Modding_Common_data_field_types#Color" class="wikilink"
title="color format">color format</a>. Default <samp>White</samp> (no
tint).</p></td>
</tr>
<tr>
<td><p><samp>AlphaFade</samp><br />
<samp>Loops</samp><br />
<samp>Rotation</samp><br />
<samp>RotationChange</samp><br />
<samp>ScaleChange</samp><br />
<samp>SortOffset</samp></p></td>
<td><p><em>(Optional)</em> See equivalent fields in the <a
href="Modding_Event_data" class="wikilink"
title="temporaryAnimatedSprite event command"><samp>temporaryAnimatedSprite</samp>
event command</a>. Default 0.</p></td>
</tr>
<tr>
<td><p><samp>Frames</samp><br />
<samp>Scale</samp></p></td>
<td><p><em>(Optional)</em> See equivalent fields in the <a
href="Modding_Event_data" class="wikilink"
title="temporaryAnimatedSprite event command"><samp>temporaryAnimatedSprite</samp>
event command</a>. Default 1.</p></td>
</tr>
<tr>
<td><p><samp>Interval</samp></p></td>
<td><p><em>(Optional)</em> See equivalent fields in the <a
href="Modding_Event_data" class="wikilink"
title="temporaryAnimatedSprite event command"><samp>temporaryAnimatedSprite</samp>
event command</a>. Default 100.</p></td>
</tr>
<tr>
<td><p><samp>Flicker</samp><br />
<samp>Flip</samp></p></td>
<td><p><em>(Optional)</em> See equivalent fields in the <a
href="Modding_Event_data" class="wikilink"
title="temporaryAnimatedSprite event command"><samp>temporaryAnimatedSprite</samp>
event command</a>. Default false.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>WorkingEffectChance</samp></p></td>
<td><p><em>(Optional)</em> The percentage chance to apply
<samp>WorkingEffects</samp> each time the day starts or the in-game
clock changes, as a value between 0 (never) and 1 (always). Default
0.33.</p></td>
</tr>
<tr>
<td><p><samp>LightWhileWorking</samp></p></td>
<td><p><em>(Optional)</em> The light emitted by the machine while it's
processing an item. Default none.</p>
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
<td><p><samp>Radius</samp></p></td>
<td><p><em>(Optional)</em> The size of the area covered by the light
effect, as a multiplier of the default radius (like <samp>1.5</samp> for
an area 50% wider than the default). Default 1.</p></td>
</tr>
<tr>
<td><p><samp>Color</samp></p></td>
<td><p><em>(Optional)</em> A tint color to apply to the light. See <a
href="Modding_Common_data_field_types#Color" class="wikilink"
title="color format">color format</a>. Default <samp>White</samp> (no
tint).</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>WobbleWhileWorking</samp></p></td>
<td><p><em>(Optional)</em> Whether the machine sprite should bulge in
&amp; out while it's processing an item. Default false.</p></td>
</tr>
<tr>
<td><p><samp>ShowNextIndexWhileWorking</samp><br />
<samp>ShowNextIndexWhenReady</samp></p></td>
<td><p><em>(Optional)</em> Whether to show the next sprite in the
machine's spritesheet while it's processing an item
(<samp>ShowNextIndexWhileWorking</samp>) or ready
(<samp>ShowNextIndexWhenReady</samp>). Default false.</p></td>
</tr>
</tbody>
</table>

### Player interaction messages

These only apply when the player interacts with a chest directly,
instead of using a
<a href="hopper" class="wikilink" title="hopper">hopper</a> or mod like
.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>InvalidItemMessage</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the message shown in a toaster notification if the player tries to input
an item that isn't accepted by the machine.</p></td>
</tr>
<tr>
<td><p><samp>InvalidItemMessageCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether <samp>InvalidItemMessage</samp> should be shown. This
can use item-related queries like <samp>ITEM_TYPE</samp>. Defaults to
always true.</p></td>
</tr>
<tr>
<td><p><samp>InvalidCountMessage</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the message shown in a toaster notification if the input inventory
doesn't contain this item, unless overridden by
<samp>InvalidCountMessage</samp> under <samp>OutputRules</samp>.</p>
<p>This can use extra custom tokens:</p>
<ul>
<li><samp>[ItemCount]</samp>: the number of remaining items needed. For
example, if you're holding three and need five, <samp>[ItemCount]</samp>
will be replaced with <samp>2</samp>.</li>
</ul></td>
</tr>
</tbody>
</table>

### Advanced logic

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>InteractMethod</samp></p></td>
<td><p><em>(Optional)</em> A C# method invoked when the player interacts
with the machine when it doesn't have output ready to harvest.</p>
<p>This must be specified in the form <samp>&lt;full type name&gt;:
&lt;method name&gt;</samp> (like <samp>StardewValley.Object, Stardew
Valley: SomeInteractMethod</samp>). The method must be static and match
the game's <samp>MachineInteractDelegate</samp> method signature:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;summary&gt;</span><span class="co">The method signature for a custom </span><span class="kw">&lt;see</span><span class="ot"> cref=</span><span class="dt">&quot;MachineData.InteractMethod&quot;</span><span class="kw">/&gt;</span><span class="co"> method.</span><span class="kw">&lt;/summary&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;param</span><span class="ot"> name=</span><span class="dt">&quot;machine&quot;</span><span class="kw">&gt;</span><span class="co">The machine instance for which to produce output.</span><span class="kw">&lt;/param&gt;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;param</span><span class="ot"> name=</span><span class="dt">&quot;location&quot;</span><span class="kw">&gt;</span><span class="co">The location containing the machine.</span><span class="kw">&lt;/param&gt;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;param</span><span class="ot"> name=</span><span class="dt">&quot;player&quot;</span><span class="kw">&gt;</span><span class="co">The player using the machine.</span><span class="kw">&lt;/param&gt;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co">/// </span><span class="kw">&lt;returns&gt;</span><span class="co">Returns whether the interaction was handled.</span><span class="kw">&lt;/returns&gt;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="kw">public</span> <span class="kw">static</span> <span class="dt">bool</span> <span class="fu">InteractWithMachine</span><span class="op">(</span>Object machine<span class="op">,</span> GameLocation location<span class="op">,</span> Farmer player<span class="op">);</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>HasInput</samp><br />
<samp>HasOutput</samp></p></td>
<td><p><em>(Optional)</em> Whether to force adding the
<samp>machine_input</samp> or <samp>machine_output</samp> <a
href="Modding_Context_tags" class="wikilink"
title="context tags">context tags</a> respectively. This isn't needed
for most machines, since they'll be set based on the
<samp>OutputRules</samp> field. Default false.</p></td>
</tr>
<tr>
<td><p><samp>IsIncubator</samp></p></td>
<td><p><em>(Optional)</em> Whether this machine acts as an incubator
when placed in a building, so players can incubate eggs in it. Default
false.</p>
<p>This is used by the <a href="incubator" class="wikilink"
title="incubator">incubator</a> and <a href="Ostrich_Incubator"
class="wikilink" title="ostrich incubator">ostrich incubator</a>. The
game logic assumes there's only one such machine in each building, so
this generally shouldn't be used by custom machines that can be built in
a vanilla <a href="barn" class="wikilink" title="barn">barn</a> or <a
href="coop" class="wikilink" title="coop">coop</a>.</p></td>
</tr>
<tr>
<td><p><samp>StatsToIncrementWhenLoaded</samp><br />
<samp>StatsToIncrementWhenHarvested</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Stats" class="wikilink"
title="tracked stats">tracked stats</a> to increment when an item is
placed in the machine (<samp>StatsToIncrementWhenLoaded</samp>) or when
the processed output is collected
(<samp>StatsToIncrementWhenHarvested</samp>). Default none. This
consists of a list of models with these fields:</p>
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
entry within the current list.</p></td>
</tr>
<tr>
<td><p><samp>StatName</samp></p></td>
<td><p>The <a href="Modding_Stats" class="wikilink"
title="stat key">stat key</a> (case-insensitive).</p></td>
</tr>
<tr>
<td><p><samp>RequiredItemId</samp></p></td>
<td><p><em>(Optional)</em> If set, only increment the stat if the main
input item has this qualified or unqualified item ID.</p></td>
</tr>
<tr>
<td><p><samp>RequiredTags</samp></p></td>
<td><p><em>(Optional)</em> If set, only increment the stat if the main
input item has <em>all</em> of these <a href="Modding_Context_tags"
class="wikilink" title="context tags">context tags</a>. You can negate a
tag with <samp>!</samp> (like
<code>"RequiredTags": [ "bone_item", "!fossil_item" ]</code> for bone
items that aren't fossils).</p></td>
</tr>
</tbody>
</table>
<p>This can be used to increment both built-in stats (like
<samp>GeodesCracked</samp> for the <a href="Geode_Crusher"
class="wikilink" title="geode crusher">geode crusher</a>) and custom
stats. Using a <a
href="Modding_Common_data_field_types#Unique_string_ID" class="wikilink"
title="unique string ID">unique string ID</a> is strongly recommended
for custom stats to avoid conflicts.</p></td>
</tr>
<tr>
<td><p><samp>ExperienceGainOnHarvest</samp></p></td>
<td><p><em>(Optional)</em> Experience points to grant on harvesting from
this machine. For example, set to <code>"Farming 7 Fishing 5"</code> to
grant 7 Farming and 5 Fishing xp.</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

## For C# mods

### Interacting with machines

Stardew Valley 1.6 adds two `Object` fields for reference:

| field | effect |
|----|----|
| `lastOutputRuleId` | If this is a machine, the output rule ID for the rule being processed by the machine (if any). |
| `lastInputItem` | If this is a machine, the item that was dropped into the machine to start the current output (if any). |

And a few methods for processing items:

| field | effect |
|----|----|
| `IsMachineWorking()` | Get whether the machine is currently processing an item. |
| `ShouldTimePassForMachine(location)` | Get whether the machine should be updated in the given location. For example, this will return false for <a href="Solar_Panel" class="wikilink" title="solar panels">solar
panels</a> placed indoors, or outdoors on a cloudy day. |
| `GetMachineData()` | Get the underlying machine data from `Data/Machines`. |
| `PlaceInMachine(…)` | Try to place an item in the machine using the rules from `Data/Machines`. This returns a boolean which indicates whether the machine was successfully started. |
| `OutputMachine(…)` | Try to set the machine output given the input item and an optional output rule to apply. Most code should call `PlaceInMachine` instead. |

A lot of the generic machine logic is also handled by a new
`MachineDataUtility` class, which lets C# mods interact with machine
data more directly. For example, you can check which output a machine
would produce without actually updating the machine.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Автоматы" class="wikilink"
title="ru:Модификации:Автоматы">ru:Модификации:Автоматы</a>
<a href="zh_模组_机器" class="wikilink"
title="zh:模组:机器">zh:模组:机器</a>
