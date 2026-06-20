---
title: "Npcs"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, npcs]
---
### NPCs

#### Children

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
<td><p><samp>child</samp><br />
<samp>kid</samp></p></td>
<td><p>| If you have children, advances the age of the first child to
the next stage. Otherwise, spawns a new child named "Baby" with gender
and skin tone randomly chosen; the child will start at stage 3
(crawling) and may initially spawn out of bounds. You do not need to be
married or have an upgraded house to use this command.</p></td>
<td><p>|<a href="#child" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>child2</samp></p></td>
<td><p>| If you have multiple children, advances the age of the second
child to the next stage. Otherwise, spawns a new child named "Baby2"
with gender and skin tone randomly chosen; the child will start at stage
3 (crawling) and may initially spawn out of bounds. You do not need to
be married or have an upgraded house to use this command.</p></td>
<td><p>|<a href="#child2" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearchildren</samp></p></td>
<td><p>| Removes all your children.</p></td>
<td><p>|<a href="#clearchildren" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pregnant</samp></p></td>
<td><p>| Sets a new baby to be born/adopted the next day. You may need
to be already married (and have a house with a nursery) for this to
work.</p></td>
<td><p>|<a href="#pregnant" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Spawning and removal

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
<td><p><samp>addkent</samp></p></td>
<td><p>| Spawns <a href="Kent" class="wikilink" title="Kent">Kent</a> if
after year 1.</p></td>
<td><p>|<a href="#addkent" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>characterinfo</samp></p></td>
<td><p>| Displays a global message listing how many NPCs are in the
current location.</p></td>
<td><p>|<a href="#characterinfo" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clearcharacters</samp></p></td>
<td><p>| Removes all NPCs who are in the current location.</p></td>
<td><p>|<a href="#clearcharacters" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clone</samp></p></td>
<td><p>| <em>Syntax</em>: <code>clone</code> &lt;S:npcName&gt;</p>
<p>Clones specified NPC and places the copy in the current location.
Name is a fuzzy match.<br />
<strong>Warning: cloning <samp>farmer</samp> will crash the
game.</strong></p></td>
<td><p>|<a href="#clone" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>killall</samp></p></td>
<td><p>| <em>Syntax</em>: <code>killall</code> &lt;S:npcName&gt;</p>
<p>Removes all NPCs except for the specified character. Name is an exact
match, and they are only spared from removal if they are in the current
location. Will also remove NPCs inside constructed buildings.</p></td>
<td><p>|<a href="#killall" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>killnpc</samp><br />
<samp>removenpc</samp></p></td>
<td><p>| <em>Syntax</em>: <code>killnpc</code> &lt;S:npcName&gt;</p>
<p>Removes specified NPC from the game, checking all game locations and
buildings. Name is an exact match. Command will output a message to the
console stating whether or not the NPC was found and removed.</p></td>
<td><p>|<a href="#killnpc" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Relationships

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
<td><p><samp>dating</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dating</code> &lt;S:npcName&gt;</p>
<p>Sets your relationship status with specified NPC to
<samp>Dating</samp>; <em>i.e.,</em> marks them as having been given a
bouquet. Name is an exact match.</p></td>
<td><p>|<a href="#dating" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>divorce</samp></p></td>
<td><p>| Queues your farmer to divorce their spouse overnight. The
spouse room may not be fully removed until you have slept and/or
returned to title.</p></td>
<td><p>|<a href="#divorce" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>engaged</samp></p></td>
<td><p>| <em>Syntax</em>: <code>engaged</code> &lt;S:npcName&gt;</p>
<p>Increases your friendship with specified NPC by 2500 points (10
hearts) and sets relationship status to <samp>Engaged</samp> with a
wedding for the next day. Name is an exact match.</p></td>
<td><p>|<a href="#engaged" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>friendall</samp></p></td>
<td><p>| <em>Syntax</em>: <code>friendall</code> [I:value]</p>
<p>Increases <a href="friendship" class="wikilink"
title="friendship">friendship</a> with all socializable NPCs by the
specified amount. If no amount is given, the increase will be 2500
points (10 hearts). All normal point caps are in place, so a bachelor
you aren't dating will not increase past 8 hearts. Previously unmet NPCs
will also be marked as met and have friendship increased with the
following exceptions:</p></td>
<td><p>|<a href="#friendall" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>friendship</samp><br />
<samp>friend</samp></p></td>
<td><p>| <em>Syntax</em>: <code>friendship</code>
&lt;S:npcName&gt;,&lt;I:value&gt;</p>
<p>Sets friendship with specified NPC to specified value. This is a
fuzzy match, and they will be marked as met if previously
unmet.</p></td>
<td><p>|<a href="#friendship" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>invitemovie</samp></p></td>
<td><p>| <em>Syntax</em>: <code>invitemovie</code> &lt;S:npcName&gt;</p>
<p>Invites specified NPC to see a movie today. This is a fuzzy match and
you will still need your own ticket to enter the theatre.</p></td>
<td><p>|<a href="#invitemovie" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>makeex</samp></p></td>
<td><p>| <em>Syntax</em>: <code>makeex</code> &lt;S:npcName&gt;</p>
<p>Sets your relationship status with specified NPC to
<samp>Divorced</samp>, removing any marriage or bouquet flag and listing
them as <em>ex-husband</em> or <em>ex-wife.</em> Name is an exact
match.</p></td>
<td><p>|<a href="#makeex" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>marry</samp></p></td>
<td><p>| <em>Syntax</em>: <code>marry</code> &lt;S:npcName&gt;</p>
<p>Increases your friendship with the specified NPC by 2500 points (10
hearts), and sets your relationship status to <samp>Married</samp> with
an anniversary of today. Name is a fuzzy match.</p></td>
<td><p>|<a href="#marry" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>wedding</samp></p></td>
<td><p>| <em>Syntax</em>: <code>wedding</code> &lt;S:npcName&gt;</p>
<p>Sets the specified NPC as your spouse and queues a wedding for today.
Name is an exact match. If the specified NPC is not normally
marriageable, the wedding will still occur but they will be invisible on
the wedding day.</p></td>
<td><p>|<a href="#wedding" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Dialogue

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
<td><p><samp>clearactivedialogueevents</samp></p></td>
<td><p>| Clears all active <a
href="Modding_Dialogue#Conversation_topics" class="wikilink"
title="conversation topics">conversation topics</a>.</p></td>
<td><p>|<a href="#clearactivedialogueevents" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>db</samp><br />
<samp>speakto</samp></p></td>
<td><p>| <em>Syntax</em>: <code>db</code> &lt;S:npcName&gt;</p>
<p>Shows a dialogue box with the current dialogue for the specified NPC.
Name is a fuzzy match and will default to Pierre if not supplied. This
does count as having spoken to that NPC today, and if they don't have
any more dialogue right now, the message <em>Stack empty</em> will be
output to the console.</p></td>
<td><p>|<a href="#db" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dialogue</samp><br />
<samp>adddialogue</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dialogue</code>
&lt;S:npcName&gt;,&lt;S:dialogueString&gt;</p>
<p>Sets the dialogue for the specified character to the specified
string. Name is a fuzzy match, and NPC names containing spaces should be
quoted (e.g.
<code>debug dialogue "Some NPC" Some dialogue text$h</code>. The
dialogue string should start with a zero and everything after will be
parsed. It can include tokens such as <samp>@</samp> for the farmer name
and portrait commands; see <a href="Modding_Dialogue#Format"
class="wikilink" title="Dialogue">Dialogue</a> for format specifics.</p>
<p><em>Example:</em>
<code>debug dialogue Abi 0Hi @! Modding is fun!$h</code> would set <a
href="Abigail" class="wikilink" title="Abigail&#39;s">Abigail's</a> next
dialogue to be <em>Hi (FarmerName)! Modding is fun!</em> with her happy
portrait.</p></td>
<td><p>|<a href="#dialogue" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>loaddialogue</samp></p></td>
<td><p>| <em>Syntax</em>: <code>loaddialogue</code>
&lt;S:npcName&gt;,&lt;S:dialogueKey&gt;</p>
<p>Sets the dialogue for the specified character using the specified
asset key. Name is a fuzzy match. Key format appears to be
<samp>file:key</samp> but exact specifics are unknown. Curly braces in
the key (<samp>{</samp>, <samp>}</samp>) will be converted to angle
brackets (<samp>&lt;</samp>, <samp>&gt;</samp>).</p></td>
<td><p>|<a href="#loaddialogue" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>phone</samp></p></td>
<td><p>| Brings up the <a href="Telephone" class="wikilink"
title="Telephone">Telephone</a> menu.</p></td>
<td><p>|<a href="#phone" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>question</samp></p></td>
<td><p>| <em>Syntax</em>: <code>question</code>
&lt;I:questionID&gt;,[B:answerOrForget]</p>
<p>Marks the specified dialogue question as answered. You can forget a
selected answer (instead of adding it) by setting the second argument to
false, like <samp>question &lt;code&gt;&lt;id&gt;&lt;/code&gt;
false</samp>.</p></td>
<td><p>|<a href="#question" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>showtextabovehead</samp><br />
<samp>sb</samp></p></td>
<td><p>| <em>Syntax</em>: <code>showtextabovehead</code>
&lt;S:npcName&gt;</p>
<p>Shows a speech bubble saying <em>"Hello! This is a test"</em> above
the specified NPC's head. Name is a fuzzy match.</p></td>
<td><p>|<a href="#showtextabovehead" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>speech</samp></p></td>
<td><p>| <em>Syntax</em>: <code>speech</code>
&lt;S:npcName&gt;,&lt;S:text&gt;</p>
<p>Displays a dialogue box for the specified character saying the
specified string. Name is a fuzzy match and names with spaces should be
in double quotes. All text after the NPC name is part of the text to
display. The text can include tokens such as <samp>@</samp> for the
farmer name and portrait commands; see <a href="Modding_Dialogue#Format"
class="wikilink" title="Dialogue">Dialogue</a> for format specifics.
Useful for testing dialogue changes.</p>
<p><em>Example:</em>
<code>debug speech Abi 0Hi @! Modding is fun!$h</code> would open a
dialogue box of <a href="Abigail" class="wikilink"
title="Abigail">Abigail</a> saying <em>Hi (FarmerName)! Modding is
fun!</em> with her happy portrait.</p></td>
<td><p>|<a href="#speech" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Movement and warping

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
<td><p><samp>facedirection</samp><br />
<samp>face</samp><br />
<samp>fd</samp></p></td>
<td><p>| <em>Syntax</em>: <code>facedirection</code>
&lt;S:npcName&gt;,&lt;I:direction&gt;</p>
<p>Sets specified character to face the specified direction. Name is a
fuzzy match and also accepts <samp>farmer</samp>. See <a
href="Modding_Event_data#Directions" class="wikilink"
title="Event data">Event data</a> for the valid directions.</p></td>
<td><p>|<a href="#facedirection" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>faceplayer</samp></p></td>
<td><p>| <em>Syntax</em>: <code>faceplayer</code> &lt;S:npcName&gt;</p>
<p>Sets specified character to face towards the player. Name is a fuzzy
match.</p></td>
<td><p>|<a href="#faceplayer" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>hurry</samp></p></td>
<td><p>| <em>Syntax</em>: <code>hurry</code> &lt;S:npcName&gt;</p>
<p>Warps specified character to the endpoint of their current schedule
entry. Name is a fuzzy match.</p>
<p><em>Example:</em> <code>debug hurry pam</code> would cause <a
href="Pam" class="wikilink" title="Pam">Pam</a> to immediately warp to
the bus if entered during her morning walk after the bus has been
repaired.</p></td>
<td><p>|<a href="#hurry" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>jump</samp></p></td>
<td><p>| <em>Syntax</em>: <code>jump</code>
&lt;S:npcName&gt;,[F:velocity]</p>
<p>Makes specified character jump with the specified velocity. Name is a
fuzzy match and also accepts <samp>farmer</samp>. Velocity is a float
and defaults to 8.0 if not supplied, which results in a jump of about
half the height of the player character.</p></td>
<td><p>|<a href="#jump" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpcharacter</samp><br />
<samp>wc</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpcharacter</code>
&lt;S:npcName&gt;,&lt;I:X&gt;,&lt;I:Y&gt;,[I:facingDirection]</p>
<p>Warps specified character to the given coordinates on the current
map. Name is a fuzzy match. See <a href="Modding_Event_data#Directions"
class="wikilink" title="Event data">Event data</a> for the valid
directions; the default is <samp>2</samp>. Note: if you do not include
enough parameters, an error message will be printed to the console which
incorrectly states the default facing direction is
<samp>1</samp>.</p></td>
<td><p>|<a href="#warpcharacter" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpcharacterto</samp><br />
<samp>wct</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpcharacterto</code>
&lt;S:npcName&gt;,&lt;S:locationName&gt;,&lt;I:X&gt;,&lt;I:Y&gt;,[I:facingDirection]</p>
<p>Warps specified character to the given coordinates on the specified
map. Character name is a fuzzy match, but location is exact. See <a
href="Modding_Event_data#Directions" class="wikilink"
title="Event data">Event data</a> for the valid directions; the default
is <samp>2</samp>. Note: if you do not include enough parameters, an
error message will be printed to the console which incorrectly states
the default facing direction is <samp>1</samp>.</p>
<p><em>Example:</em> <code>debug wct robin Farm 69 16</code> would warp
<a href="Robin" class="wikilink" title="Robin">Robin</a> to just right
of the mailbox on the Farm map, facing downwards.</p></td>
<td><p>|<a href="#warpcharacterto" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpcharactertome</samp><br />
<samp>wctm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpcharactertome</code>
&lt;S:npcName&gt;</p>
<p>Warps the specified character directly to you; name is a fuzzy
match.</p></td>
<td><p>|<a href="#warpcharactertome" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>whereis</samp><br />
<samp>where</samp></p></td>
<td><p>| <em>Syntax</em>: <code>whereis</code> &lt;S:npcName&gt;</p>
<p>Outputs the location and coordinates of the specified character to
the SMAPI console. Name is a fuzzy match, so the command will return all
matching NPCs.</p></td>
<td><p>|<a href="#whereis" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Farm animals

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
<td><p><samp>animal</samp></p></td>
<td><p>| <em>Syntax</em>: <code>animal</code> &lt;S:type&gt;</p>
<p>Adds a new baby animal of the specified type to the Farm. The animal
will have a random name and be assigned to the correct type of building
(if there is room). Type is a case-sensitive match with spaces allowed.
Valid types for the base game are listed below.</p></td>
<td><p>|<a href="#animal" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>animalinfo</samp></p></td>
<td><p>| Displays a global message with the count of the total number of
farm animals.</p></td>
<td><p>|<a href="#animalinfo" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>befriendanimals</samp></p></td>
<td><p>| <em>Syntax</em>: <code>befriendanimals</code> [I:amount]</p>
<p>Sets friendship of all animals who live (and are currently present)
in the current location to the given amount. Default is 1000
(max).</p></td>
<td><p>|<a href="#befriendanimals" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>displaceanimals</samp></p></td>
<td><p>| Goes through all buildings that can contain animals. For each
animal in each building, tries to move the animal outside the building.
Finally, clears the building of all animals that live there.</p></td>
<td><p>|<a href="#displaceanimals" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fixanimals</samp></p></td>
<td><p>| Goes through all buildings that can contain animals and removes
entries for animals which no longer live in that building.</p></td>
<td><p>|<a href="#fixanimals" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>growanimals</samp></p></td>
<td><p>| Sets all animals who live in the current location to day 1 of
adulthood, unless they are already adults. May cause each of them to eat
hay.</p></td>
<td><p>|<a href="#growanimals" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pauseanimals</samp></p></td>
<td><p>| Pauses all farm animals in the current location indefinitely.
Exiting and re-entering may cause them to be randomly moved to a new
spot, but they will remain paused.</p></td>
<td><p>|<a href="#pauseanimals" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>unpauseanimals</samp></p></td>
<td><p>| Unpauses all farm animals in the current location.</p></td>
<td><p>|<a href="#unpauseanimals" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>warpanimaltome</samp><br />
<samp>watm</samp></p></td>
<td><p>| <em>Syntax</em>: <code>warpanimaltome</code>
&lt;S:animalName&gt;</p>
<p>Warps the specified farm animal to you; name is a case-insensitive
fuzzy search but will only work in a location that allows
animals.</p></td>
<td><p>|<a href="#warpanimaltome" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Pets, horses, and monsters

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
<td><p><samp>befriendpets</samp></p></td>
<td><p>| Gives the player 1000 friendship points with all pets.</p></td>
<td><p>|<a href="#befriendpets" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>cat</samp></p></td>
<td><p>| <em>Syntax</em>: <code>cat</code>
&lt;I:X&gt;,&lt;I:Y&gt;,[I:breed]</p>
<p>Spawns a new <a href="Animals#Cat_or_Dog" class="wikilink"
title="Cat">Cat</a> at the given coordinates of the current location.
Breed can be <samp>0</samp>, <samp>1</samp>, <samp>2</samp>,
<samp>3</samp>, <samp>4</samp>, or the <samp>Id</samp> of a <a
href="Modding_Pets#Breeds" class="wikilink" title="custom breed">custom
breed</a> added by a mod, and determines which texture to use. This is
an additional pet and does not replace any current pet(s).</p></td>
<td><p>|<a href="#cat" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>changepet</samp></p></td>
<td><p>| <em>Syntax</em>: <code>changepet</code>
&lt;S:petName&gt;,&lt;S:type&gt;,[S:breedId]</p>
<p>Changes the type and breed of an existing pet on the farm with name
<samp>petName</samp>. <samp>type</samp> should match an ID in
<samp>Data/Pets</samp>. Defaults to the first pet breed if none is
specified.</p></td>
<td><p>|<a href="#changepet" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>createdino</samp></p></td>
<td><p>| Spawns a <a href="Pepper_Rex" class="wikilink"
title="Pepper Rex">Pepper Rex</a> just to the right of your
farmer.</p></td>
<td><p>|<a href="#createdino" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dog</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dog</code>
&lt;I:X&gt;,&lt;I:Y&gt;,[I:breed]</p>
<p>Spawns a new <a href="Animals#Cat_or_Dog" class="wikilink"
title="Dog">Dog</a> at the given coordinates of the current location.
Breed can be <samp>0</samp>, <samp>1</samp>, <samp>2</samp>,
<samp>3</samp>, <samp>4</samp>, or the <samp>Id</samp> of a <a
href="Modding_Pets#Breeds" class="wikilink" title="custom breed">custom
breed</a> added by a mod and determines which texture to use. This is an
additional pet and does not replace any current pet(s).</p></td>
<td><p>|<a href="#dog" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>horse</samp></p></td>
<td><p>| <em>Syntax</em>: <code>horse</code> &lt;I:X&gt;,&lt;I:Y&gt;</p>
<p>Spawns a new <a href="Animals#Horse" class="wikilink"
title="Horse">Horse</a> at the given coordinates of the current
location. Horse may disappear after dismounting if there is no stable
for it.</p></td>
<td><p>|<a href="#horse" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>killallhorses</samp></p></td>
<td><p>| Removes all horses from all locations.</p></td>
<td><p>|<a href="#killallhorses" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>monster</samp></p></td>
<td><p>| <em>Syntax</em>: <code>monster</code>
&lt;S:type&gt;,&lt;I:X&gt;,&lt;I:Y&gt;,[I:facingDirection]</p>
<p>Spawns a monster of the specified type at the given coordinates of
the current location. Only certain monster types seem to work. Known
valid types include <samp>Bat</samp>, <samp>DinoMonster</samp>,
<samp>DustSpirit</samp>, <samp>Fly</samp>, <samp>Ghost</samp>,
<samp>GreenSlime</samp>, <samp>Grub</samp>, <samp>LavaCrab</samp>,
<samp>Mummy</samp>, <samp>RockCrab</samp>, <samp>RockGolem</samp>,
<samp>Serpent</samp>, <samp>ShadowBrute</samp>,
<samp>ShadowShaman</samp>, <samp>Skeleton</samp>, and
<samp>SquidKid</samp>. <samp>Duggy</samp> may also work depending on the
terrain.</p></td>
<td><p>|<a href="#monster" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>owl</samp></p></td>
<td><p>| Spawns an Owl in the current location.</p></td>
<td><p>|<a href="#owl" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pettofarm</samp></p></td>
<td><p>| If it is not raining, warps your pet to the pet bowl location
on the Farm (Tech note: Location is initially set by checking for tile
1938 on Building layer). If it is raining, warps pet to the FarmHouse.
Only works for host in multiplayer.</p></td>
<td><p>|<a href="#pettofarm" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>setpreferredpet</samp></p></td>
<td><p>| <em>Syntax</em>: <code>setpreferredpet</code>
&lt;S:type&gt;,[S:breedId]</p>
<p>Sets the player's preferred pet type and breed. <samp>type</samp>
should match an ID in <samp>Data/Pets</samp>. Defaults to the first pet
breed if none is specified.</p></td>
<td><p>|<a href="#setpreferredpet" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>togglecatperson</samp></p></td>
<td><p>| Toggles your farmer's chosen pet preference between cat and
dog. If you already have a pet, the inventory graphic will switch but
the pet themselves will not be affected.</p></td>
<td><p>|<a href="#togglecatperson" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
