---
title: "Collections And Quests"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, collections-and-quests]
---
### Collections and quests

#### Cooking and crafting

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>addallcrafting</samp></p></td>
<td><p>| Teaches you all crafting recipes. Basically the same as <a
href="#crafting" class="wikilink" title="crafting">crafting</a>, but
this one does not check if you already know the recipe before adding so
it may output some error messages to the console about duplicate
keys.</p></td>
<td><p>|<a href="#addallcrafting" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>cooking</samp></p></td>
<td><p>| Teaches you all cooking recipes.</p></td>
<td><p>|<a href="#cooking" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>cookingrecipe</samp></p></td>
<td><p>| <em>Syntax</em>: <code>cookingrecipe</code>
&lt;S:recipeName&gt;</p>
<p>Teaches you the specified cooking recipe. Names are case-sensitive
and may contain spaces.</p>
<p><em>Example:</em> <code>debug cookingrecipe Seafoam Pudding</code>
will give you the recipe to cook <a href="Seafoam_Pudding"
class="wikilink" title="Seafoam Pudding">Seafoam Pudding</a>.</p></td>
<td><p>|<a href="#cookingrecipe" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>crafting</samp></p></td>
<td><p>| Teaches you all crafting recipes.</p></td>
<td><p>|<a href="#crafting" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>craftingrecipe</samp><br />
<samp>addCraftingRecipe</samp></p></td>
<td><p>| <em>Syntax</em>: <code>craftingrecipe</code>
&lt;S:recipeName&gt;</p>
<p>Teaches you the specified crafting recipe. Names are case-sensitive
and may contain spaces.</p>
<p><em>Example:</em> <code>debug craftingrecipe Ancient Seeds</code>
will give you the recipe to craft plantable ancient seeds from the
artifact.</p></td>
<td><p>|<a href="#craftingrecipe" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>slimecraft</samp></p></td>
<td><p>| Teaches you the crafting recipes for <a href="Slime_Incubator"
class="wikilink" title="Slime Incubator">Slime Incubator</a> and <a
href="Slime_Egg-Press" class="wikilink" title="Slime Egg-Press">Slime
Egg-Press</a>.</p></td>
<td><p>|<a href="#slimecraft" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Fishing, museum, and secret notes

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearfishcaught</samp></p></td>
<td><p>| Clears all records of which fish you have caught, resetting the
collection. To also change the stat which tracks how many total fish
have been caught, see <a href="#caughtfish" class="wikilink"
title="caughtfish">caughtfish</a>.</p></td>
<td><p>|<a href="#clearfishcaught" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearmuseum</samp></p></td>
<td><p>| Removes all donated items from the museum, emptying the museum
displays and causing all artifacts and minerals to have the <em>Gunther
can tell you more about this...</em> description. Does not affect the
records of which artifacts and minerals have been found (<em>i.e.,</em>
the collection pages).</p></td>
<td><p>|<a href="#clearmuseum" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>deletearch</samp></p></td>
<td><p>| Clears all records of which artifacts and minerals you have
found.<br />
<strong>Warning: Also clears all record of which fish you have caught
and clears all received mail (including hidden progress
flags).</strong></p></td>
<td><p>|<a href="#deletearch" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>museumloot</samp></p></td>
<td><p>| Adds unfound artifacts and minerals to your inventory until it
is full. Items added by this command will now be marked "found" on the
collection pages.</p></td>
<td><p>|<a href="#museumloot" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>newmuseumloot</samp></p></td>
<td><p>| Adds undonated artifacts and minerals to your inventory until
it is full. Items added by this command increment the "Total found"
count on the collection pages.</p></td>
<td><p>|<a href="#newmuseumloot" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>note</samp></p></td>
<td><p>| <em>Syntax</em>: <code>note</code> &lt;I:bookID&gt;</p>
<p>Sets the count of <a href="Lost_Books" class="wikilink"
title="Lost Books">Lost Books</a> recovered to 18, even if you
previously had found more, and brings up a window with the contents of
the specified book. Book IDs above 18 will show the message <em>There's
a book missing here.</em></p></td>
<td><p>|<a href="#note" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>sn</samp><br />
<samp>secretNote</samp></p></td>
<td><p>| <em>Syntax</em>: <code>sn</code> [I:noteID]</p>
<p>Adds specified secret note to your inventory. If no ID is specified,
a random unseen note will be added. See <samp>Data/SecretNotes</samp>
for a list of IDs.</p></td>
<td><p>|<a href="#sn" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Mail

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>allmail</samp></p></td>
<td><p>| Queues every letter defined in <samp>Data/mail</samp> for
delivery tomorrow.</p></td>
<td><p>|<a href="#allmail" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>allmailread</samp></p></td>
<td><p>| Marks every letter defined in <samp>Data/mail</samp> as already
read. They will all be accessible in the letters tab of the collections
menu.</p></td>
<td><p>|<a href="#allmailread" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>broadcastmail</samp></p></td>
<td><p>| <em>Syntax</em>: <code>broadcastmail</code>
&lt;S:mailID&gt;</p>
<p>Queues specified mail for delivery tomorrow for all players. The ID
is case-sensitive; see <samp>Data/mail</samp> for valid IDs in the base
game.</p></td>
<td><p>|<a href="#broadcastmail" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>broadcastmailbox</samp></p></td>
<td><p>| <em>Syntax</em>: <code>broadcastmailbox</code>
&lt;S:mailID&gt;</p>
<p>Immediately adds specified mail to all players' mailboxes. The ID is
case-sensitive; see <samp>Data/mail</samp> for valid IDs in the base
game.</p></td>
<td><p>|<a href="#broadcastmailbox" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearmail</samp></p></td>
<td><p>| Clears records of all received mail <strong>(including hidden
progress flags)</strong>. This also clears the letters tab in the
collections menu.</p></td>
<td><p>|<a href="#clearmail" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>mailfortomorrow</samp><br />
<samp>mft</samp></p></td>
<td><p>| <em>Syntax</em>: <code>mailfortomorrow</code>
&lt;S:mailID&gt;,[noletter]</p>
<p>Queues specified mail for delivery tomorrow. The ID is
case-sensitive, and any zeros in the given ID will be replaced with
underscores. See <samp>Data/mail</samp> for valid IDs (after
replacement) in the base game. Because of the zero replacement, some
letters (<em>e.g.,</em> <samp>quest10</samp>) are inaccessible with this
command; <a href="#broadcastmail" class="wikilink"
title="broadcastmail">broadcastmail</a> may be a useful alternative in
those cases. If the second parameter is present (with any value), the
"noletter" flag is set, which will add the mail to your mail received
list without showing a "new mail" indicator.</p></td>
<td><p>|<a href="#mailfortomorrow" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>seenmail</samp></p></td>
<td><p>| <em>Syntax</em>: <code>seenmail</code>
&lt;S:mailID&gt;,[B:addOrRemove]</p>
<p>Marks specified mail as already received. The ID is case-sensitive;
see <samp>Data/mail</samp> for valid IDs in the base game. You can
remove a mail received (instead of adding it) by setting the second
argument to false, like <samp>seenMail
&lt;code&gt;&lt;id&gt;&lt;/code&gt; false</samp>.</p></td>
<td><p>|<a href="#seenmail" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>showmail</samp></p></td>
<td><p>| <em>Syntax</em>: <code>showmail</code> &lt;S:mailID&gt;</p>
<p>Brings up the letter-reading window with the specified mail. The ID
is case-sensitive; see <samp>Data/mail</samp> for valid IDs in the base
game. If a match cannot be found, a blank window will briefly display
and an ArgumentOutOfRange error will be triggered. Does not set the
letter as received or cause it to show in the letter tab of the
collections menu.</p>
<p><em>Example:</em> <code>debug showmail SeaAmulet</code> will show the
letter Lewis sends about Mermaid's Pendants.</p></td>
<td><p>|<a href="#showmail" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Quests and Special Orders

<table>
<thead>
<tr>
<th><p>command</p></th>
<th><p>description</p></th>
<th><p> </p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearquests</samp></p></td>
<td><p>| Removes all quests from your journal/quest log.</p></td>
<td><p>|<a href="#clearquests" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>collectquest</samp></p></td>
<td><p>| Starts a new random resource Gathering quest. If used multiple
times on the same game day, the quest will always be the same.</p></td>
<td><p>|<a href="#collectquest" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>completespecialorders</samp><br />
<samp>cso</samp></p></td>
<td><p>| Completes all objectives for all currently active Special
Orders and Qi Challenges. Note that this command does not remove the
associated journal entries.</p></td>
<td><p>|<a href="#completespecialorders" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>completequest</samp></p></td>
<td><p>| <em>Syntax</em>: <code>completequest</code>
&lt;I:questID&gt;</p>
<p>Completes specified quest and removes it from your journal. See
<samp>Data/Quests</samp> for a list of IDs.</p></td>
<td><p>|<a href="#completequest" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>deliveryquest</samp></p></td>
<td><p>| Starts a new random item Delivery quest. If used multiple times
on the same game day, the quest will always be the same.</p></td>
<td><p>|<a href="#deliveryquest" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>getallquests</samp></p></td>
<td><p>| Starts every quest from <samp>Data/Quests</samp> that you don't
already have.</p></td>
<td><p>|<a href="#getallquests" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>ordersboard</samp></p></td>
<td><p>| Shows the <a href="Quests#List_of_Special_Orders"
class="wikilink" title="Special Orders">Special Orders</a> quest
board.</p></td>
<td><p>|<a href="#ordersboard" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>qiboard</samp></p></td>
<td><p>| Shows the <a href="Qi&#39;s_Walnut_Room#Special_Orders_Board"
class="wikilink" title="Qi Challenges">Qi Challenges</a> quest
board.</p></td>
<td><p>|<a href="#qiboard" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>quest</samp></p></td>
<td><p>| <em>Syntax</em>: <code>quest</code> &lt;I:questID&gt;</p>
<p>Starts the specified quest. See <samp>Data/Quests</samp> for a list
of IDs.</p></td>
<td><p>|<a href="#quest" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>quests</samp></p></td>
<td><p>| Starts every quest from <samp>Data/Quests</samp> that you don't
already have as well as a random item Delivery quest and a random Slay
Monster quest.</p></td>
<td><p>|<a href="#quests" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>removequest</samp></p></td>
<td><p>| <em>Syntax</em>: <code>removequest</code> &lt;I:questID&gt;</p>
<p>Silently removes specified quest from your journal. See
<samp>Data/Quests</samp> for a list of IDs.</p></td>
<td><p>|<a href="#removequest" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>slayquest</samp></p></td>
<td><p>| Starts a new random Slay Monster quest. If used multiple times
on the same game day, the quest will always be the same.</p></td>
<td><p>|<a href="#slayquest" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>specialorder</samp></p></td>
<td><p>| <em>Syntax</em>: <code>specialorder</code>
&lt;S:questID&gt;</p>
<p>Starts the Special Order (either town or Qi Challenge) with the
specified ID. See <samp>Data/SpecialOrders</samp> for a list of
IDs.</p></td>
<td><p>|<a href="#specialorder" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
