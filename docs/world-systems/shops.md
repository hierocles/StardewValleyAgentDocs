---
title: "Shops"
wiki_source: "Modding:Shops"
permalink: /Modding:Shops/
category: world-systems
tags: [shops, data, format, examples, vanilla-shop-ids, open-a-custom-shop]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how to edit shop data.

## Data

### Format

You can create and change shops by editing the `Data/Shops` asset. This
consists of a string → model lookup, where the key is a
<a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for the
shop, and the value is a model with these fields.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td data-valign="top"><p><samp>Items</samp></p></td>
<td><p>The items to add to the shop inventory. This consists of a list
of values with these fields:</p>
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
generic item fields supported by shop items.</p>
<p>Notes:</p>
<ul>
<li>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, all of
them will be added to the shop.</li>
<li>The <samp>MinStack</samp> and <samp>MaxStack</samp> fields apply to
the item after it's purchased, and have no effect on the price or
<samp>Stock</samp> limit.</li>
<li>If the player found <a href="Pierre&#39;s_Missing_Stocklist"
class="wikilink" title="Pierre&#39;s Missing Stocklist">Pierre's Missing
Stocklist</a>, season conditions in the <samp>Condition</samp> field are
ignored in <a href="Pierre&#39;s_General_Store" class="wikilink"
title="Pierre&#39;s General Store">Pierre's General Store</a>.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Price</samp></p></td>
<td><p><em>(Optional)</em> The gold price to purchase the item from the
shop. Defaults to the item's normal price, or zero if
<samp>TradeItemId</samp> is specified.</p></td>
</tr>
<tr>
<td><p><samp>TradeItemId</samp><br />
<samp>TradeItemAmount</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_items"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a> and amount which must be traded to purchase this
item. Defaults to no item and 1 respectively.</p>
<p>If both <samp>Price</samp> and <samp>TradeItemId</samp> are
specified, the player will have to provide both to get the
item.</p></td>
</tr>
<tr>
<td><p><samp>ApplyProfitMargins</samp></p></td>
<td><p><em>(Optional)</em> Whether to multiply the price by the
difficulty modifier, which reduces the price for higher <a
href="options" class="wikilink" title="profit margins">profit
margins</a>. This can be <samp>true</samp> (always apply it),
<samp>false</samp> (never apply it), or <samp>null</samp> (apply for
certain items like saplings). This is applied before any quantity
modifiers. Default <samp>null</samp>.</p></td>
</tr>
<tr>
<td><p><samp>IgnoreShopPriceModifiers</samp></p></td>
<td><p><em>(Optional)</em> Whether to ignore the shop's
<samp>PriceModifiers</samp> field for this item. This has no effect on
the item's equivalent field. Default false.</p></td>
</tr>
<tr>
<td><p><samp>AvailableStockModifiers</samp><br />
<samp>PriceModifiers</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="Quantity modifiers">Quantity modifiers</a>
applied to the <samp>AvailableStock</samp> or <samp>Price</samp>
values.</p>
<p>Notes:</p>
<ul>
<li>The price modifiers stack with the <samp>PriceModifiers</samp> field
on the shop (unless <samp>IgnoreStorePriceModifiers</samp> is
true).</li>
</ul></td>
</tr>
<tr>
<td><p><samp>AvailableStockModifierMode</samp><br />
<samp>PriceModifierMode</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="quantity modifier modes">quantity modifier
modes</a> which indicate what to do if multiple modifiers in the
<samp>AvailableStockModifiers</samp> or <samp>PriceModifiers</samp>
field apply at the same time. Default <samp>Stack</samp>.</p></td>
</tr>
<tr>
<td><p><samp>AvoidRepeat</samp></p></td>
<td><p><em>(Optional)</em> Whether to avoid adding this item to the shop
if it would duplicate one that was already added. If the item ID is
randomized, this will choose a value that hasn't already been added to
the shop if possible. Default false.</p></td>
</tr>
<tr>
<td><p><samp>UseObjectDataPrice</samp></p></td>
<td><p><em>(Optional)</em> If this data produces an object and
<samp>Price</samp> is omitted, whether to use the raw price in
<samp>Data/Objects</samp> instead of the calculated sell-to-player
price.</p></td>
</tr>
<tr>
<td><p><samp>AvailableStock</samp></p></td>
<td><p><em>(Optional)</em> The maximum number of the item which can be
purchased in one day. Default unlimited.</p></td>
</tr>
<tr>
<td data-valign="top"><p><samp>AvailableStockLimit</samp></p></td>
<td><p><em>(Optional)</em> If <samp>Stock</samp> is set, how the limit
is applied in multiplayer. This has no effect on recipes.</p>
<p>The possible values are:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Global</samp></p></td>
<td><p>The limit is shared by every player in the world. For example, if
the <samp>Stock</samp> was <samp>1</samp> and a player bought it, no
other players could buy one.</p></td>
</tr>
<tr>
<td><p><samp>Player</samp></p></td>
<td><p>The limit applies to each player separately. For example, if the
<samp>Stock</samp> was <samp>1</samp>, each player could buy
one.</p></td>
</tr>
<tr>
<td><p><samp>None</samp></p></td>
<td><p>The limit applies to the current instance of the shop menu. If
you exit and reopen the menu, the item will reappear with the same
stock. This is mainly used for items that are added
conditionally.</p></td>
</tr>
</tbody>
</table>
<p>Default <samp>Global</samp>.</p></td>
</tr>
<tr>
<td><p><samp>PerItemCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether an item produced from the other fields should be added
(e.g. to filter results from item queries like <samp>ALL_ITEMS</samp>).
Defaults to always added.</p></td>
</tr>
<tr>
<td><p><samp>ActionsOnPurchase</samp></p></td>
<td><p><em>(Optional)</em> A list of <a href="Modding_Trigger_actions"
class="wikilink" title="actions">actions</a> to run when the player
purchases this item. These are run once per purchase click. Default
none.</p>
<p>For example, this can be used to start a <a
href="Modding_Dialogue#Conversation_topics" class="wikilink"
title="conversation topic">conversation topic</a> when it's
purchased:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ActionsOnPurchase&quot;</span><span class="er">:</span> <span class="ot">[</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;AddConversationTopic _PurchasedItem 5&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span></span></code></pre></div></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>SalableItemTags</samp></p></td>
<td><p><em>(Optional)</em> A list of <a href="Modding_Context_tags"
class="wikilink" title="context tags">context tags</a> for items which
the player can sell to to this shop. Default none.</p></td>
</tr>
<tr>
<td data-valign="top"><p><samp>Owners</samp></p></td>
<td><p><em>(Optional)</em> The 'owner' data to apply when the shop is
opened. This affects the portrait and dialogue shown, and whether the
shop is closed. This field is checked <em>after</em> conditions
specified in the <a href="Modding_Maps#Action" class="wikilink"
title="Action OpenShop tile property"><samp>Action OpenShop</samp> tile
property</a>.</p>
<p>The behavior depends on whether <samp>Owners</samp> is set:</p>
<ul>
<li>If omitted, the shop is opened regardless of whether an NPC is
present, and no portrait or dialogue is shown.</li>
<li>If it's specified, this consists of an <em>ordered</em> list. When
the player opens the shop, the first matching entry is applied. When
searching for an NPC, each entry checks either the [owner tile area]
from the <a href="Modding_Maps#Action" class="wikilink"
title="Action OpenShop tile property"><samp>Action OpenShop</samp> tile
property</a> (if set), else the whole location. If no entries are
matched, the shop isn't opened.</li>
</ul>
<p>For example, let's say a shop has these owners:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode js"><code class="sourceCode javascript"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Owners&quot;</span><span class="op">:</span> [</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Name&quot;</span><span class="op">:</span> <span class="st">&quot;AnyOrNone&quot;</span><span class="op">,</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;ClosedMessage&quot;</span><span class="op">:</span> <span class="st">&quot;The shop opens from 1pm to 2pm.&quot;</span><span class="op">,</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Condition&quot;</span><span class="op">:</span> <span class="st">&quot;!TIME 1300 1400&quot;</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    }<span class="op">,</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    {</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Name&quot;</span><span class="op">:</span> <span class="st">&quot;Any&quot;</span><span class="op">,</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Dialogues&quot;</span><span class="op">:</span> [ <span class="st">&quot;Hi there!&quot;</span> ]</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    }<span class="op">,</span></span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>    {</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Name&quot;</span><span class="op">:</span> <span class="st">&quot;Abigail&quot;</span><span class="op">,</span></span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;Dialogues&quot;</span><span class="op">:</span> [ <span class="st">&quot;This entry is never selected.&quot;</span> ]</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>    }<span class="op">,</span></span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>]</span></code></pre></div>
<p>Here's what happens when the player clicks the shop:</p>
<ol>
<li>If it's not 1pm to 2pm, the first entry matches. The
<samp>ClosedMessage</samp> shows a matching dialogue box and the shop
isn't opened.</li>
<li>Else if any NPC is present, the second entry applies. The third
entry is always ignored, since Abigail would match the
<code>"Name": "Any"</code> check.</li>
<li>Else the shop isn't opened.</li>
</ol>
<p>Each model in the list can specify these fields:</p>
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
<td><p>One of...</p>
<ul>
<li>the internal name for the NPC who must be in range to use this
entry;</li>
<li><samp>AnyOrNone</samp> to use this entry regardless of whether any
NPC is within the shop area;</li>
<li><samp>Any</samp> to use this entry if <em>any</em> NPC is within the
shop area;</li>
<li><samp>None</samp> to use this entry if <em>no</em> NPC is within the
shop area.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p><em>(Optional)</em> An ID for this entry within the shop. This
only needs to be unique within the current shop's owner list. Defaults
to the <samp>Name</samp> value.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this owner entry is available. If omitted, it's always
available.</p></td>
</tr>
<tr>
<td><p><samp>Portrait</samp></p></td>
<td><p><em>(Optional)</em> One of...</p>
<ul>
<li>the internal name of the NPC whose portrait to show;</li>
<li>the asset name of the texture to display;</li>
<li>or an empty string (or other value which doesn't match an NPC or
texture asset name) to disable the portrait.</li>
</ul>
<p>Defaults to the portrait for the NPC matching the <samp>Name</samp>
field (if any).</p>
<p>If drawn, it'll use the 64x64 pixel area in the top-left corner of
the texture. Note : it is possible that name of "none" prevents any
portrait to be used.</p></td>
</tr>
<tr>
<td><p><samp>Dialogues</samp></p></td>
<td><p><em>(Optional)</em> A list of possible dialogue lines the shop
will display for this Owner. The first entry with a matching condition
will be chosen. Each entry consists of a model with these fields:</p>
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
dialogue within the current list.</p></td>
</tr>
<tr>
<td><p><samp>Dialogue</samp></p></td>
<td><p>The dialogue text to show, as a <a
href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a>. The resulting text is
parsed using the <a href="Modding_Dialogue" class="wikilink"
title="dialogue format">dialogue format</a>.</p>
<p>You can use an empty string (like <code>"Dialogue": ""</code>) to
remove the little dialogue box.</p></td>
</tr>
<tr>
<td><p><samp>RandomDialogue</samp></p></td>
<td><p><em>(Optional)</em> A list of dialogue lines to randomly choose
from, using the same format as <samp>Dialogue</samp>. If set,
<samp>Dialogue</samp> is optional and ignored. Each entry in the list
has an equal probability of being chosen every time the shop is opened
(see <samp>RandomizeDialogueOnOpen</samp> below for how to change this
to randomize daily). For example:</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RandomDialogue&quot;</span><span class="er">:</span> <span class="ot">[</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;[LocalizedText Strings</span><span class="er">\S</span><span class="st">tringsFromCSFiles:ShopMenu.cs.11469]&quot;</span><span class="ot">,</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;[LocalizedText Strings</span><span class="er">\S</span><span class="st">tringsFromCSFiles:ShopMenu.cs.11470]&quot;</span><span class="ot">,</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;[LocalizedText Strings</span><span class="er">\S</span><span class="st">tringsFromCSFiles:ShopMenu.cs.11471]&quot;</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the dialogue should be available. If omitted, the
dialogue is always available.</p></td>
</tr>
</tbody>
</table>
<p>This can be set to an empty list (<code>"Dialogues": []</code>) to
disable the dialogue text entirely. If omitted, defaults to a generic
"<em>Have a look at my wares</em>" text.</p></td>
</tr>
<tr>
<td><p><samp>RandomizeDialogueOnOpen</samp></p></td>
<td><p><em>(Optional)</em> If a <samp>Dialogues</samp> entry is using
<samp>RandomDialogue</samp>, whether to re-randomize which line is
selected each time the shop is opened (<samp>true</samp>) or once per
day (<samp>false</samp>). Default <samp>true</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ClosedMessage</samp></p></td>
<td><p><em>(Optional)</em> If set, a <a
href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for a 'shop is
closed'-style message to display when this entry is selected.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>This only applies if the <samp>Owners</samp> list is checked (i.e.
the <a href="#Open_a_custom_shop" class="wikilink"
title="Action OpenShop conditions"><samp>Action OpenShop</samp>
conditions</a> match). If you want to customize the message shown for
the shop opening hours, remove the conditions from <samp>Action
OpenShop</samp> and set them on this entry instead.</li>
<li>If the selected entry sets this field, the shop is closed regardless
of any other fields or whether the shop owner is present. When you set
the <samp>Name</samp> field, that affects whether this entry is selected
(i.e. whether the shop is closed).</li>
</ul></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>Currency</samp></p></td>
<td><p><em>(Optional)</em> The currency in which all items in the shop
should be priced. The valid values are 0 (money), 1 (star tokens), 2 (Qi
coins), and 4 (Qi gems). Default 0. For item trading, see
<samp>TradeItemId</samp> for each item.</p></td>
</tr>
<tr>
<td><p><samp>ApplyProfitMargins</samp></p></td>
<td><p><em>(Optional)</em> The default value for
<samp>ApplyProfitMargins</samp> under <samp>Items</samp>, if set. This
can be <samp>true</samp> (always apply it), <samp>false</samp> (never
apply it), or <samp>null</samp> (apply for certain items like saplings).
This is applied before any quantity modifiers. Default
<samp>null</samp>.</p></td>
</tr>
<tr>
<td><p><samp>StackSizeVisibility</samp></p></td>
<td><p><em>(Optional)</em> How to draw stack size numbers in the shop
list by default. If omitted, the default shop logic is applied (usually
equivalent to <samp>Show</samp>).</p>
<p>The possible values are:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Hide</samp></p></td>
<td><p>Always hide the stack size.</p></td>
</tr>
<tr>
<td><p><samp>Show</samp></p></td>
<td><p>Always draw the stack size.</p></td>
</tr>
<tr>
<td><p><samp>ShowIfMultiple</samp></p></td>
<td><p>Draw the stack size if it's more than one.</p></td>
</tr>
</tbody>
</table>
<p>This is ignored in some special cases (e.g. recipes can't have a
stack size).</p></td>
</tr>
<tr>
<td><p><samp>OpenSound</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_audio"
class="wikilink" title="audio cue ID">audio cue ID</a> to play when the
shop menu is opened. Defaults to <samp>dwop</samp>.</p></td>
</tr>
<tr>
<td><p><samp>PurchaseSound</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_audio"
class="wikilink" title="audio cue ID">audio cue ID</a> to play when an
item is purchased normally. Defaults to
<samp>purchaseClick</samp>.</p></td>
</tr>
<tr>
<td><p><samp>purchaseRepeatSound</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_audio"
class="wikilink" title="audio cue ID">audio cue ID</a> to play when
accumulating a stack to purchase (e.g. by holding right-click on PC).
Defaults to <samp>purchaseRepeat</samp>.</p></td>
</tr>
<tr>
<td><p><samp>PriceModifiers</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="Quantity modifiers">Quantity modifiers</a>
applied to the sell price for items in this shop. See also
<samp>PriceModifiers</samp> under <samp>Items</samp>.</p></td>
</tr>
<tr>
<td><p><samp>PriceModifierMode</samp></p></td>
<td><p><em>(Optional)</em> A <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Quantity_modifiers"
class="wikilink" title="quantity modifier mode">quantity modifier
mode</a> which indicates what to do if multiple modifiers in the
<samp>PriceModifiers</samp> field apply at the same time. This only
affects that specific field, it won't affect price modifiers under
<samp>Items</samp>. Default <samp>Stack</samp>.</p></td>
</tr>
<tr>
<td data-valign="top"><p><samp>VisualTheme</samp></p></td>
<td><p><em>(Optional)</em> The visual theme to apply to the shop UI, or
omit to use the default theme. The first matching theme is applied. All
fields are optional and will fallback to the default theme.</p>
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
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this theme should be applied. Defaults to always
true.</p></td>
</tr>
<tr>
<td><p><samp>WindowBorderTexture</samp><br />
<samp>WindowBorderSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the shop window border. Defaults to
<samp>LooseSprites\Cursors</samp> at (384, 373) with size
18×18.</p></td>
</tr>
<tr>
<td><p><samp>PortraitBackgroundTexture</samp><br />
<samp>PortraitBackgroundSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the NPC portrait background. Defaults to
<samp>LooseSprites\Cursors</samp> at (603, 414) with size
74×74.</p></td>
</tr>
<tr>
<td><p><samp>DialogueBackgroundTexture</samp><br />
<samp>DialogueBackgroundSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the NPC dialogue background. Defaults to
<samp>Maps\MenuTiles</samp> at (0, 256) with size 60×60.</p></td>
</tr>
<tr>
<td><p><samp>DialogueColor</samp><br />
<samp>DialogueShadowColor</samp></p></td>
<td><p><em>(Optional)</em> The sprite text color for the dialogue text.
See <a href="Modding_Migrate_to_Stardew_Valley_1.6#Color_fields"
class="wikilink" title="color format">color format</a>. Defaults to the
game's standard text color.</p></td>
</tr>
<tr>
<td><p><samp>ItemRowBackgroundTexture</samp><br />
<samp>ItemRowBackgroundSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the item row background in the shop inventory. Defaults
to <samp>LooseSprites\Cursors</samp> at (384, 396) with size
15×15.</p></td>
</tr>
<tr>
<td><p><samp>ItemRowBackgroundHoverColor</samp></p></td>
<td><p><em>(Optional)</em> The color tint to apply to the item row
background in the shop inventory when the cursor is hovering over it, or
<samp>White</samp> for no tint. See <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Color_fields"
class="wikilink" title="color format">color format</a>. Defaults to
<samp>Wheat</samp>.</p></td>
</tr>
<tr>
<td><p><samp>ItemRowTextColor</samp></p></td>
<td><p><em>(Optional)</em> The sprite text color for the item text. See
<a href="Modding_Migrate_to_Stardew_Valley_1.6#Color_fields"
class="wikilink" title="color format">color format</a>. Defaults to the
game's standard text color.</p></td>
</tr>
<tr>
<td><p><samp>ItemIconBackgroundTexture</samp><br />
<samp>ItemIconBackgroundSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the background behind the item icons. Defaults to
<samp>LooseSprites\Cursors</samp> at (296, 363) with size
18×18.</p></td>
</tr>
<tr>
<td><p><samp>ScrollUpTexture</samp><br />
<samp>ScrollUpSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the up arrow icon above the scrollbar. Defaults to
<samp>LooseSprites\Cursors</samp> at (421, 459) with size
11×12.</p></td>
</tr>
<tr>
<td><p><samp>ScrollDownTexture</samp><br />
<samp>ScrollDownSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the down arrow icon beneath the scrollbar. Defaults to
<samp>LooseSprites\Cursors</samp> at (421, 472) with size
11×12.</p></td>
</tr>
<tr>
<td><p><samp>ScrollBarFrontTexture</samp><br />
<samp>ScrollBarFrontSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the sliding scrollbar foreground. Defaults to
<samp>LooseSprites\Cursors</samp> at (435, 463) with size 6×10.</p></td>
</tr>
<tr>
<td><p><samp>ScrollBarBackTexture</samp><br />
<samp>ScrollBarBackSourceRect</samp></p></td>
<td><p><em>(Optional)</em> The texture asset name, and the pixel area
within it, for the scrollbar background. Defaults to
<samp>LooseSprites\Cursors</samp> at (403, 383) with size 6×6.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a
href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_data_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

### Examples

You can add or replace entire shops. For example, this content pack adds
a shop that sells ice cream in summer, and pufferfish all year:

You can also add, replace, edit, or reorder items in a specific shop by
targeting the shop's `Items` field. For example, this removes Trout Soup
(item \#219) and adds Pufferfish above bait (item \#685):

### Vanilla shop IDs

The base game's shops are defined in `Data/Shops` too (except a few
special cases like <a href="_Category_Dressers" class="wikilink"
title="dressers">dressers</a> and home renovations).

See `Data/Shops` for a full list, but here are the main shop IDs for
convenience:

<table>
<thead>
<tr>
<th><p>shop</p></th>
<th><p>ID</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="Abandoned_House" class="wikilink"
title="Abandoned house shop">Abandoned house shop</a></p></td>
<td><p><samp>HatMouse</samp></p></td>
</tr>
<tr>
<td><p><a href="Adventurer&#39;s_Guild" class="wikilink"
title="Adventurer&#39;s Guild">Adventurer's Guild</a></p></td>
<td><p><samp>AdventureShop</samp> (regular shop)<br />
<samp>AdventureGuildRecovery</samp> (item recovery service)</p></td>
</tr>
<tr>
<td><p><a href="Bookseller" class="wikilink"
title="Bookseller">Bookseller</a></p></td>
<td><p><samp>Bookseller</samp> (regular shop)<br />
<samp>BooksellerTrade</samp> (book trades)</p></td>
</tr>
<tr>
<td><p><a href="Casino" class="wikilink"
title="Casino">Casino</a></p></td>
<td><p><samp>Casino</samp></p></td>
</tr>
<tr>
<td><p><a href="Blacksmith" class="wikilink"
title="Clint&#39;s blacksmith shop">Clint's blacksmith shop</a></p></td>
<td><p><samp>Blacksmith</samp> (regular shop)<br />
<samp>ClintUpgrade</samp> (tool upgrades)</p></td>
</tr>
<tr>
<td><p><a href="Desert_Trader" class="wikilink"
title="Desert trader">Desert trader</a></p></td>
<td><p><samp>DesertTrade</samp></p></td>
</tr>
<tr>
<td><p><a href="Dwarf#Shop" class="wikilink"
title="Dwarf&#39;s shop">Dwarf's shop</a></p></td>
<td><p><samp>Dwarf</samp></p></td>
</tr>
<tr>
<td><p><a href="Harvey&#39;s_Clinic" class="wikilink"
title="Harvey&#39;s clinic">Harvey's clinic</a></p></td>
<td><p><samp>Hospital</samp></p></td>
</tr>
<tr>
<td><p><a href="Ice_Cream_Stand" class="wikilink"
title="Ice-cream stand">Ice-cream stand</a></p></td>
<td><p><samp>IceCreamStand</samp></p></td>
</tr>
<tr>
<td><p><a href="Ginger_Island#Beach_Resort" class="wikilink"
title="Island resort">Island resort</a></p></td>
<td><p><samp>ResortBar</samp></p></td>
</tr>
<tr>
<td><p><a href="Island_Trader" class="wikilink"
title="Island trader">Island trader</a></p></td>
<td><p><samp>IslandTrade</samp></p></td>
</tr>
<tr>
<td><p><a href="Joja_Mart" class="wikilink" title="Joja Mart">Joja
Mart</a></p></td>
<td><p><samp>Joja</samp></p></td>
</tr>
<tr>
<td><p><a href="Krobus" class="wikilink"
title="Krobus&#39; shop">Krobus' shop</a></p></td>
<td><p><samp>ShadowShop</samp></p></td>
</tr>
<tr>
<td><p><a href="Marnie&#39;s_Ranch" class="wikilink"
title="Marnie&#39;s ranch">Marnie's ranch</a></p></td>
<td><p><samp>AnimalShop</samp></p></td>
</tr>
<tr>
<td><p><a href="Pierre&#39;s_General_Store" class="wikilink"
title="Pierre&#39;s general store">Pierre's general store</a></p></td>
<td><p><samp>SeedShop</samp></p></td>
</tr>
<tr>
<td><p><a href="Qi&#39;s_Walnut_Room" class="wikilink"
title="Qi&#39;s gem shop">Qi's gem shop</a></p></td>
<td><p><samp>QiGemShop<samp></p></td>
</tr>
<tr>
<td><p><a href="Giant_Stump#Raccoon_Wife&#39;s_Shop" class="wikilink"
title="Raccoon Wife&#39;s Shop">Raccoon Wife's Shop</a></p></td>
<td><p><samp>Raccoon</samp></p></td>
</tr>
<tr>
<td><p><a href="Carpenter&#39;s_Shop" class="wikilink"
title="Robin&#39;s carpenter shop">Robin's carpenter shop</a></p></td>
<td><p><samp>Carpenter</samp></p></td>
</tr>
<tr>
<td><p><a href="Saloon" class="wikilink"
title="Stardrop Saloon">Stardrop Saloon</a></p></td>
<td><p><samp>Saloon</samp></p></td>
</tr>
<tr>
<td><p><a href="Oasis" class="wikilink"
title="Sandy&#39;s Oasis shop">Sandy's Oasis shop</a></p></td>
<td><p><samp>Sandy</samp></p></td>
</tr>
<tr>
<td><p><a href="Traveling_Cart" class="wikilink"
title="Traveling cart">Traveling cart</a></p></td>
<td><p><samp>Traveler</samp></p></td>
</tr>
<tr>
<td><p><a href="Volcano_Dungeon#Shop" class="wikilink"
title="Volcano dwarf shop">Volcano dwarf shop</a></p></td>
<td><p><samp>VolcanoShop</samp></p></td>
</tr>
<tr>
<td><p><a href="Fish_Shop" class="wikilink"
title="Willy&#39;s fish shop">Willy's fish shop</a></p></td>
<td><p><samp>FishShop</samp></p></td>
</tr>
</tbody>
</table>

And the main festival shops:

<table>
<thead>
<tr>
<th><p>festival shop</p></th>
<th><p>ID</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="Dance_of_the_Moonlight_Jellies" class="wikilink"
title="Dance of the Moonlight Jellies">Dance of the Moonlight
Jellies</a></p></td>
<td><p><samp>Festival_DanceOfTheMoonlightJellies_Pierre</samp></p></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><p><a href="Desert_Festival#Calico_Egg_Merchant" class="wikilink"
title="Desert Festival (egg merchant)">Desert Festival (egg
merchant)</a></p></td>
<td><p><samp>DesertFestival_EggShop</samp></p></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><p><a href="Desert_Festival#Villager_Shops" class="wikilink"
title="Desert Festival (villager shops)">Desert Festival (villager
shops)</a></p></td>
<td><p><samp>DesertFestival_&lt;name&gt;</samp><br />
(e.g. <samp>DesertFestival_Abigail)</samp></p></td>
</tr>
<tr>
<td><p><a href="Egg_Festival" class="wikilink" title="Egg Festival">Egg
Festival</a></p></td>
<td><p><samp>Festival_EggFestival_Pierre</samp></p></td>
</tr>
<tr>
<td><p><a href="Festival_of_Ice" class="wikilink"
title="Festival of Ice">Festival of Ice</a></p></td>
<td><p><samp>Festival_FestivalOfIce_TravelingMerchant</samp></p></td>
</tr>
<tr>
<td><p><a href="Feast_of_the_Winter_Star" class="wikilink"
title="Feast of the Winter Star">Feast of the Winter Star</a></p></td>
<td><p><samp>Festival_FeastOfTheWinterStar_Pierre</samp></p></td>
</tr>
<tr>
<td><p><a href="Flower_Dance" class="wikilink"
title="Flower Dance">Flower Dance</a></p></td>
<td><p><samp>Festival_FlowerDance_Pierre</samp></p></td>
</tr>
<tr>
<td><p><a href="Luau" class="wikilink" title="Luau">Luau</a></p></td>
<td><p><samp>Festival_Luau_Pierre</samp></p></td>
</tr>
<tr>
<td><p><a href="Night_Market#Decoration_Boat" class="wikilink"
title="Night Market (decoration boat)">Night Market (decoration
boat)</a></p></td>
<td><p><samp>Festival_NightMarket_DecorationBoat</samp></p></td>
</tr>
<tr>
<td><p><a href="Night_Market#Magic_Shop_Boat" class="wikilink"
title="Night Market (magic boat)">Night Market (magic boat)</a></p></td>
<td><p><samp>Festival_NightMarket_MagicBoat_Day1</samp><br />
<samp>Festival_NightMarket_MagicBoat_Day2</samp><br />
<samp>Festival_NightMarket_MagicBoat_Day3</samp></p></td>
</tr>
<tr>
<td><p><a href="Spirit&#39;s_Eve" class="wikilink"
title="Spirit&#39;s Eve">Spirit's Eve</a></p></td>
<td><p><samp>Festival_SpiritsEve_Pierre</samp></p></td>
</tr>
<tr>
<td><p><a href="Stardew_Valley_Fair" class="wikilink"
title="Stardew Valley Fair">Stardew Valley Fair</a></p></td>
<td><p><samp>Festival_StardewValleyFair_StarTokens</samp></p></td>
</tr>
</tbody>
</table>

And several 'shops' for the catalogues:

| item | ID |
|----|----|
| <a href="Catalogue" class="wikilink" title="Catalogue">Catalogue</a> | `Catalogue` |
| <a href="Furniture_Catalogue" class="wikilink"
title="Furniture Catalogue">Furniture Catalogue</a> | `Furniture Catalogue` |
| <a href="Joja_Furniture_Catalogue" class="wikilink"
title="Joja Furniture Catalogue">Joja Furniture Catalogue</a> | `JojaFurnitureCatalogue` |
| <a href="Junimo_Catalogue" class="wikilink"
title="Junimo Catalogue">Junimo Catalogue</a> | `JunimoFurnitureCatalogue` |
| <a href="Retro_Catalogue" class="wikilink" title="Retro Catalogue">Retro
Catalogue</a> | `RetroFurnitureCatalogue` |
| <a href="Trash_Catalogue" class="wikilink" title="Trash Catalogue">Trash
Catalogue</a> | `TrashFurnitureCatalogue` |
| <a href="Wizard_Catalogue" class="wikilink"
title="Wizard Catalogue">Wizard Catalogue</a> | `WizardFurnitureCatalogue` |

## Open a custom shop

You can place an <a href="Modding_Maps#Action" class="wikilink"
title="Action OpenShop tile property"><samp>Action OpenShop</samp> tile
property</a> on the map, which will open the given shop ID when the
player clicks it.

In C# code, you can get the inventory for a custom shop using
`Utility.GetShopStock("shop id here")`, open a shop menu using
`Utility.TryOpenShopMenu("shop id", …)`, and add temporary items to an
open menu using `shopMenu.AddForSale(…)`. The ID of the opened shop is
stored in the shop menu's `ShopId` field.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Магазины" class="wikilink"
title="ru:Модификации:Магазины">ru:Модификации:Магазины</a>
<a href="zh_模组_商店" class="wikilink"
title="zh:模组:商店">zh:模组:商店</a>
