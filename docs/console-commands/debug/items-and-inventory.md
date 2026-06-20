---
title: "Items And Inventory"
wiki_source: "Modding:Console commands"
permalink: /Modding:Console_commands/
category: console-commands
tags: [console-commands, items-and-inventory]
---
### Items and inventory

#### General item search and spawning

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
<td><p><samp>createDebris</samp></p></td>
<td><p>| <em>Syntax</em>: <code>createDebris</code> &lt;I:item
ID&gt;</p>
<p>Spawns an item with the given <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a> on the ground at your feet.</p>
<p><em>Example:</em> <code>debug createDebris 24</code> would spawn a <a
href="parsnip" class="wikilink" title="parsnip">parsnip</a>.</p></td>
<td><p>|<a href="#createDebris" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>doesItemExist</samp></p></td>
<td><p>| <em>Syntax</em>: <code>doesItemExist</code> &lt;S:item
ID&gt;</p>
<p>Searches the entire world (including other players' inventories) to
see if the <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a> exists anywhere. If you search with the name of
the item, make sure that it's Capitalized for each word in the item's
name, between "quotation mark" and there's no space between the words. A
global message saying <em>Yes</em> or <em>No</em> will be displayed, but
there's no indication of where the item is located if it is found. See
the <samp>whereIsItem</samp> command for more detailed output.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug doesItemExist 24</code> or
<code>debug doesItemExist (O)24</code> or
<code>debug doesItemExist "Parsnip"</code> will search for
parsnips.</li>
</ul>
<ul>
<li><code>debug doesItemExist "river jelly"</code> would respond with
"No" but <code>debug doesItemExist "RiverJelly"</code> would search for
River Jelly and respond with "Yes"</li>
</ul></td>
<td><p>|<a href="#doesItemExist" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>furniture</samp><br />
<samp>ff</samp></p></td>
<td><p>| <em>Syntax</em>: <code>furniture</code> [item ID]</p>
<p>Adds a <a href="Modding_Furniture" class="wikilink"
title="furniture">furniture</a>-type item to your inventory based on its
<a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="unqualified item ID">unqualified item ID</a>. If the item ID is
omitted, a random furniture with ID 0–1612 will be added.</p>
<p><em>Example:</em> <code>debug furniture 704</code> would give you an
<a href="Oak_Dresser" class="wikilink" title="Oak Dresser">Oak
Dresser</a>.</p></td>
<td><p>|<a href="#furniture" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fuzzyItemNamed</samp><br />
<samp>fin</samp><br />
<samp>f</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fuzzyItemNamed</code> &lt;S:name
search&gt;,[I:amount],[I:quality]</p>
<p>Adds the specified item to your inventory based on a fuzzy search for
&lt;item name&gt; across all item types. Only the first matching item
will be spawned. The item name can be quoted to include spaces. The
optional parameters are for stack size (default 1) and <a
href="Modding_Items#Quality" class="wikilink"
title="quality">quality</a> (default 0).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug fuzzyItemNamed sturg 5 4</code> would give you a stack
of five iridium-quality <a href="sturgeon" class="wikilink"
title="sturgeon">sturgeon</a>.</li>
</ul>
<ul>
<li><code>debug fin "galaxy sword"</code> would give you a <a
href="Galaxy_Sword" class="wikilink" title="Galaxy Sword">Galaxy
Sword</a>.</li>
</ul>
<ul>
<li><code>debug f grief</code> would give you a <a
href="Tailoring#Shirts" class="wikilink"
title="&quot;Good Grief&quot; shirt">"Good Grief" shirt</a>.</li>
</ul></td>
<td><p>|<a href="#fuzzyItemNamed" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>getIndex</samp></p></td>
<td><p>| <em>Syntax</em>: <code>getIndex</code> &lt;S:name
search&gt;</p>
<p>Shows the display name and <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified item ID">qualified item ID</a> for the item matching
the fuzzy search (see <code>fuzzyItemNamed</code> for search
syntax).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug getIndex prisma</code> would output <em>Prismatic
Shard's qualified ID is (O)74</em>.</li>
</ul>
<ul>
<li><code>debug getIndex grief</code> would output <em>"Good Grief"
Shirt's qualified ID is (S)1008</em>.</li>
</ul></td>
<td><p>|<a href="#getIndex" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>holdItem</samp></p></td>
<td><p>| Plays the animation where the player holds an item up above
their head. Uses the player's current item.</p></td>
<td><p>|<a href="#holdItem" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>item</samp><br />
<samp>i</samp></p></td>
<td><p>| <em>Syntax</em>: <code>item</code> &lt;S:item
ID&gt;,[I:amount],[I:quality]</p>
<p>Adds an item to your inventory based on its <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or unqualified item ID">qualified or unqualified item
ID</a>. The optional parameters are for stack size (default 1) and <a
href="Modding_Items#Quality" class="wikilink"
title="quality">quality</a> (default 0).</p>
<p><em>Example:</em> <code>debug item 74</code> or
<code>debug item (O)74</code> would give you a <a href="Prismatic_Shard"
class="wikilink" title="prismatic shard">prismatic shard</a>.</p></td>
<td><p>|<a href="#item" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>itemNamed</samp><br />
<samp>in</samp></p></td>
<td><p>| <em>Syntax</em>: <code>itemNamed</code> &lt;S:item
name&gt;,[I:amount],[I:quality]</p>
<p>Adds <a href="Modding_Objects" class="wikilink"
title="object">object</a>-type items whose internal names exactly equals
the &lt;item name&gt; (case-insensitive) to your inventory. The optional
parameters are for stack size (default 1) and <a
href="Modding_Items#Quality" class="wikilink"
title="quality">quality</a> (default 0).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug itemNamed "miner's treat"</code> would give you <a
href="Miner&#39;s_Treat" class="wikilink"
title="miner&#39;s treat">miner's treat</a>.</li>
</ul>
<ul>
<li><code>debug in "strange doll" 3</code> would give you 3 of each of
the strange doll <a href="artifacts" class="wikilink"
title="artifacts">artifacts</a>.</li>
</ul></td>
<td><p>|<a href="#itemNamed" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>lookup</samp><br />
<samp>lu</samp></p></td>
<td><p>| <em>Syntax</em>: <code>lookup</code> &lt;S:name search&gt;</p>
<p>Outputs the <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="unqualified item ID">unqualified item ID</a> of
each <a href="Modding_Objects" class="wikilink"
title="object">object</a>-type item whose internal name contains the
&lt;name search&gt; (case-insensitive).</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug lookup diamond</code> would output <em>Diamond
72</em>.</li>
</ul>
<ul>
<li><code>debug lu strange doll</code> would output <em>Strange Doll
126</em> and <em>Strange Doll 127</em>.</li>
</ul></td>
<td><p>|<a href="#lookup" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>qualifiedId</samp></p></td>
<td><p>| Shows the held item's display name and <a href="#Custom_items"
class="wikilink" title="qualified item ID">qualified item
ID</a>.</p></td>
<td><p>|<a href="#qualifiedId" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>tv</samp></p></td>
<td><p>| Adds a <a href="Budget_TV" class="wikilink"
title="budget TV">budget TV</a> or <a href="Plasma_TV" class="wikilink"
title="plasma TV">plasma TV</a> to your inventory (each has an equal
random chance).</p></td>
<td><p>|<a href="#tv" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>wallpaper</samp><br />
<samp>wp</samp></p></td>
<td><p>| <em>Syntax</em>: <code>wallpaper</code> [I:item ID]</p>
<p>Adds a floorpaper or wallpaper item to the inventory. If a numeric
wallpaper/flooring ID is specified, spawns that one; otherwise it
randomly chooses one from floor IDs 0–39 or wallpaper IDs
0–111.</p></td>
<td><p>|<a href="#wallpaper" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>whereIsItem</samp><br />
<samp>whereItem</samp></p></td>
<td><p>| <em>Syntax</em>: <code>whereIsItem</code> &lt;S:item ID&gt;</p>
<p>Searches the entire world (including other players' inventories) for
items matching the <a href="Modding_Common_data_field_types#Item_ID"
class="wikilink" title="qualified or unqualified item ID">qualified or
unqualified item ID</a>, and lists all matches.</p>
<p><em>Example:</em></p></td>
<td><p>|<a href="#whereIsItem" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Backpack and inventory

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
<td><p><samp>backpack</samp></p></td>
<td><p>| <em>Syntax</em>: <code>backpack</code> &lt;I:amount&gt;</p>
<p>Increases your inventory space by the specified amount; capped at 36
slots.</p></td>
<td><p>|<a href="#backpack" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>clear</samp><br />
<samp>ci</samp></p></td>
<td><p>| Removes all items currently in your inventory.</p></td>
<td><p>|<a href="#clear" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fillbackpack</samp><br />
<samp>fillbp</samp><br />
<samp>fill</samp><br />
<samp>fbp</samp></p></td>
<td><p>| Fills all empty spaces in your inventory with random Objects.
Any objects spawned by this command will not be marked as found on the
collections tab.</p></td>
<td><p>|<a href="#fillbackpack" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>sl</samp><br />
<samp>shiftToolbarLeft</samp></p></td>
<td><p>| Shifts inventory rows down, looping previous bottom row to top;
similar to using Control-Tab with default keyboard controls. Will work
with larger-than-normal inventories.</p></td>
<td><p>|<a href="#sl" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>sr</samp><br />
<samp>shiftToolbarRight</samp></p></td>
<td><p>| Shifts inventory rows up, looping previous top row to bottom;
similar to using Tab with default keyboard controls. Will work with
larger-than-normal inventories.</p></td>
<td><p>|<a href="#sr" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Clothing and tailoring

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
<td><p><samp>dye</samp></p></td>
<td><p>| <em>Syntax</em>: <code>dye</code> &lt;S:itemType&gt;,
&lt;S:color&gt;, &lt;F:strength&gt;</p>
<p>Dyes the specified (currently equipped) item the specified color.
Item type can be <samp>shirt</samp> or <samp>pants</samp> and valid
colors are <samp>black</samp>, <samp>blue</samp>, <samp>green</samp>,
<samp>red</samp>, <samp>white</samp>, and <samp>yellow</samp>. Strength
is a float between 0 and 1 inclusive; the higher the number, the more
vibrant the color. The dye will mix with the current color so it is
sometimes necessary to "reset" the item by dyeing first with white
strength 1.</p>
<p><em>Examples:</em></p>
<ul>
<li><code>debug dye shirt red 0.33</code> would dye your current shirt a
shade of pink.</li>
</ul>
<ul>
<li><code>debug dye pants blue 1</code> would dye your current pants
bright blue.</li>
</ul></td>
<td><p>|<a href="#dye" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dyeAll</samp></p></td>
<td><p>| Seems to be intended to bring up a character customization menu
with HSV sliders for both shirt and pants, but it does not function
because all entered commands are forced to lower case. The two
individual commands <a href="#dyepants" class="wikilink"
title="dyepants">dyepants</a> and <a href="#dyeshirt" class="wikilink"
title="dyeshirt">dyeshirt</a> can be used instead.</p></td>
<td><p>|<a href="#dyeAll" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dyemenu</samp></p></td>
<td><p>| Brings up the same <a href="Dyeing#Dye_Pots" class="wikilink"
title="dyeing menu">dyeing menu</a> you get by interacting with the dye
pots in Emily's house. Filling all six pots with appropriate items will
bring up a character customization menu with HSV sliders for dyeing both
your currently-equipped shirt and pants.</p></td>
<td><p>|<a href="#dyemenu" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dyepants</samp></p></td>
<td><p>| Brings up a character customization menu with HSV sliders for
dyeing your currently-equipped pants.</p></td>
<td><p>|<a href="#dyepants" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>dyeshirt</samp></p></td>
<td><p>| Brings up a character customization menu with HSV sliders for
dyeing your currently-equipped shirt.</p></td>
<td><p>|<a href="#dyeshirt" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>hat</samp></p></td>
<td><p>| <em>Syntax</em>: <code>hat</code> &lt;I:itemID&gt;</p>
<p>Gives and automatically equips the specified <a href="Hats"
class="wikilink" title="hat">hat</a> to your farmer; any currently
equipped hat will be destroyed. See <a href="Modding_Hats"
class="wikilink" title="hat data">hat data</a> for a list of base game
IDs.</p>
<p><em>Example:</em> <code>debug hat 3</code> would give you a <a
href="Sombrero" class="wikilink" title="Sombrero">Sombrero</a> and
automatically equip it.</p></td>
<td><p>|<a href="#hat" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>shirt</samp></p></td>
<td><p>| <em>Syntax</em>: <code>shirt</code> &lt;I:itemID&gt;</p>
<p>Gives and automatically equips the specified <a href="Shirts"
class="wikilink" title="shirt">shirt</a> to your farmer; any currently
equipped shirt will be destroyed.</p></td>
<td><p>|<a href="#shirt" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>tailor</samp></p></td>
<td><p>| Brings up the same <a href="Tailoring" class="wikilink"
title="tailoring menu">tailoring menu</a> you get by interacting with
the sewing machine in Emily's house.</p></td>
<td><p>|<a href="#tailor" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>tailorrecipelisttool</samp><br />
<samp>trlt</samp></p></td>
<td><p>| Brings up a special menu listing most Objects, what color they
will dye an item, and what clothing item they can make when used in the
sewing machine. The menu can be scrolled with the mouse wheel, hovering
the mouse over the object will show the tooltip for the clothing it
makes, and clicking on the object will add the clothing it makes to your
inventory.</p></td>
<td><p>|<a href="#tailorrecipelisttool" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Tools and weapons

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
<td><p><samp>bobber</samp></p></td>
<td><p>| <em>Syntax</em>: <code>bobber</code> &lt;I:type&gt;</p>
<p>Changes the player's fishing rod <a href="Fish_Shop#Bobber_Machine"
class="wikilink" title="bobber style">bobber style</a>. Valid styles
begin at 0.</p></td>
<td><p>|<a href="#bobber" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>fish</samp></p></td>
<td><p>| <em>Syntax</em>: <code>fish</code> &lt;S:whichFish&gt;</p>
<p>Starts the fishing minigame with the specified fish. The player must
be holding a fishing rod. Can lead to the farmer getting stuck on
fishing animation frames.</p></td>
<td><p>|<a href="#fish" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>forge</samp></p></td>
<td><p>| Shows the <a href="Forge" class="wikilink"
title="Forge">Forge</a> menu.</p></td>
<td><p>|<a href="#forge" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>pole</samp></p></td>
<td><p>| <em>Syntax</em>: <code>pole</code> [I:type]</p>
<p>Adds a <a href="Tools#Fishing_Poles" class="wikilink"
title="Fishing Pole">Fishing Pole</a> of the specified type to your
inventory. Valid types are 0 (Bamboo Pole; the default), 1 (Training
Rod), 2 (Fiberglass Rod), or 3 (Iridium Rod).</p></td>
<td><p>|<a href="#pole" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>trashcan</samp></p></td>
<td><p>| <em>Syntax</em>: <code>trashcan</code> &lt;I:level&gt;</p>
<p>Changes the upgrade level of your inventory <a href="Trash_Cans"
class="wikilink" title="Trash Can">Trash Can</a>. Upgrade levels are 0
(basic), 1 (copper), 2 (steel), 3 (gold), or 4 (iridium). The can sprite
may not fully update until the inventory is closed and
reopened.</p></td>
<td><p>|<a href="#trashcan" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Wallet items

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
<td><p><samp>clearspecials</samp></p></td>
<td><p>| Removes most special items from your <a href="Wallet"
class="wikilink" title="Wallet">Wallet</a>. The Rusty Key, Skull Key,
Special Charm, Dark Talisman, Magic Ink, Club Card, Dwarven Translation
Guide, and Magnifying Glass will all be removed, but Bear's Knowledge
and Spring Onion Mastery will remain.</p></td>
<td><p>|<a href="#clearspecials" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>darktalisman</samp></p></td>
<td><p>| Adds the <a href="Dark_Talisman" class="wikilink"
title="Dark Talisman">Dark Talisman</a> to (and removes the <a
href="Magic_Ink" class="wikilink" title="Magic Ink">Magic Ink</a> from)
your wallet; also removes the magic artifact blocking access to the <a
href="Witch&#39;s_Swamp" class="wikilink"
title="Witch&#39;s Swamp">Witch's Swamp</a>.<br />
<strong>Warning: This command will also clear all received mail and
hidden mail flags.</strong></p></td>
<td><p>|<a href="#darktalisman" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skullkey</samp></p></td>
<td><p>| Adds the <a href="Skull_Key" class="wikilink"
title="Skull Key">Skull Key</a> to your wallet.</p></td>
<td><p>|<a href="#skullkey" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>specialitem</samp></p></td>
<td><p>| <em>Syntax</em>: <code>specialitem</code> &lt;I:itemID&gt;</p>
<p>Adds the specified special item to your wallet. Which ID values are
useful is currently unknown.</p></td>
<td><p>|<a href="#specialitem" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>specials</samp></p></td>
<td><p>| Adds all special items to your wallet, including Bear's
Knowledge and Spring Onion Mastery. The associated events for these two
are also marked as seen.</p></td>
<td><p>|<a href="#specials" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>townkey</samp></p></td>
<td><p>| Adds the <a href="Key_To_The_Town" class="wikilink"
title="Key To The Town">Key To The Town</a> to your wallet.</p></td>
<td><p>|<a href="#townkey" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Miscellaneous items

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
<td><p><samp>fillbin</samp><br />
<samp>fb</samp></p></td>
<td><p>| Adds a Parsnip, Fire Quartz, LargeMouth Bass, Wild Horseradish,
and Wood to the shipping bin.</p></td>
<td><p>|<a href="#fillbin" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>listtags</samp></p></td>
<td><p>| Outputs all object context tags associated with the
currently-held item to the console.</p>
<p><em>Example:</em> <code>debug listtags</code> while holding an <a
href="Acorn" class="wikilink" title="Acorn">Acorn</a> would output
<em>Tags on Acorn: id_o_309 color_brown tree_seed_item item_acorn
category_seeds</em>.</p></td>
<td><p>|<a href="#listtags" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>makeinedible</samp></p></td>
<td><p>| Makes the currently-held item inedible by setting its edibility
value to -300; does not affect other instances of the same
item.</p></td>
<td><p>|<a href="#makeinedible" class="wikilink"
title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><p><samp>skullgear</samp></p></td>
<td><p>| Sets your current backpack size to 36 slots, equips a Savage
Ring and Iridium Band, equips Space Boots, and clears inventory except
for an Iridium Pickaxe, a Galaxy Sword, a stack of 20 Spicy Eels, and a
stack of 20 Mega Bombs. Also sets your maximum health to 75 and gives
you the Fighter profession. Any previously equipped boots and rings and
all previous inventory items are lost.</p></td>
<td><p>|<a href="#skullgear" class="wikilink" title="#">#</a></p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
