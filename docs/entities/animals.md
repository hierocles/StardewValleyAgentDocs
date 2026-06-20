---
title: "Animals"
wiki_source: "Modding:Animal data"
permalink: /Modding:Animal_data/
category: entities
tags: [animal-data, data-format, main-info, animal-shop, hatching, growth, produce, audio-sprite]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how to create and edit in-game
<a href="Animals" class="wikilink" title="farm animals">farm animals</a>.

## Data format

You can add or edit farm animals by editing the `Data/FarmAnimals`
<a href="Modding_Editing_XNB_files" class="wikilink"
title="asset">asset</a>.

This consists of a string → model lookup, where...

- The key is a
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a> for the
  farm animal type.
- The value is a model with the fields listed below.

### Main info

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DisplayName</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the animal type's
display name.</p></td>
</tr>
<tr>
<td><p><samp>House</samp></p></td>
<td><p>The <a href="Modding_Buildings" class="wikilink"
title="building ID">building ID</a> for the main building type that
houses this animal. The animal will also be placeable in buildings whose
<samp>ValidOccupantTypes</samp> field contains this value.</p></td>
</tr>
<tr>
<td><p><samp>Gender</samp></p></td>
<td><p><em>(Optional)</em> The possible genders for the animal type.
Currently this only affects the text shown after purchasing the animal,
like "<em>Great! I'll send little &lt;name&gt; to [his/her] new home
right away</em>". Default <samp>Female</samp>.</p>
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
<td><p><samp>Male</samp><br />
<samp>Female</samp></p></td>
<td><p>Farm animals of this type are always male or always
female.</p></td>
</tr>
<tr>
<td><p><samp>MaleOrFemale</samp></p></td>
<td><p>The gender of each animal is randomized based on its internal
unique ID.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### Animal shop

These fields affect how this farm animal type is shown in
<a href="Marnie&#39;s_Ranch" class="wikilink"
title="Marnie&#39;s animal shop">Marnie's animal shop</a>. Animals are
automatically listed if they have a valid `PurchasePrice` value.

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>PurchasePrice</samp></p></td>
<td><p><em>(Optional if not purchaseable)</em> Half the cost to purchase
the animal (the actual price is double this value), or a negative value
to disable purchasing this animal type. Default -1.</p></td>
</tr>
<tr>
<td><p><samp>ShopTexture</samp></p></td>
<td><p><em>(Optional if not purchaseable)</em> The asset name for the
icon texture to show in shops. Defaults to
<samp>LooseSprites/Cursors</samp> or <samp>LooseSprites/Cursors2</samp>
based on the animal's position within the loaded data (but using the
default isn't recommended if it's purchaseable).</p></td>
</tr>
<tr>
<td><p><samp>ShopSourceRect</samp></p></td>
<td><p><em>(Optional if not purchaseable)</em> The pixel area within the
<samp>ShopTexture</samp> to draw, specified as an object with
<samp>X</samp>, <samp>Y</samp>, <samp>Width</samp>, and
<samp>Height</samp> fields. This should be 32 pixels wide and 16 high.
Ignored if <samp>ShopTexture</samp> isn't set.</p></td>
</tr>
<tr>
<td><p><samp>RequiredBuilding</samp></p></td>
<td><p><em>(Optional)</em> The building that needs to be built on the
farm for this animal to be available to purchase. Buildings that are
upgraded from this building are valid too. Default none.</p></td>
</tr>
<tr>
<td><p><samp>UnlockCondition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether the farm animal is available in the shop menu. Default
always unlocked.</p></td>
</tr>
<tr>
<td><p><samp>ShopDisplayName</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the display name shown in the shop menu. Defaults to the
<samp>DisplayName</samp> field.</p></td>
</tr>
<tr>
<td><p><samp>ShopDescription</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the tooltip description shown in the shop menu. Defaults to
none.</p></td>
</tr>
<tr>
<td><p><samp>ShopMissingBuildingDescription</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> which
overrides <samp>ShopDescription</samp> if the
<samp>RequiredBuilding</samp> isn't built. Defaults to none.</p></td>
</tr>
<tr>
<td><p><samp>AlternatePurchaseTypes</samp></p></td>
<td><p><em>(Optional)</em> The possible variants for this farm animal
(e.g. chickens can be Brown Chicken, Blue Chicken, or White Chicken).
This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ID</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for is
purchase type within the current list.</p></td>
</tr>
<tr>
<td><p><samp>AnimalIDs</samp></p></td>
<td><p>A list of animal IDs to spawn instead of the main <samp>ID</samp>
field. If multiple are listed, one is chosen at random on
purchase.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this variant entry is available. Default always
enabled.</p></td>
</tr>
</tbody>
</table>
<p>If multiple are listed, the first available variant is returned.
Default none.</p></td>
</tr>
</tbody>
</table>

### Hatching

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>EggItemIds</samp></p></td>
<td><p><em>(Optional)</em> A list of the <a href="Modding_Objects"
class="wikilink" title="object IDs">object IDs</a> that can be placed in
the <a href="incubator" class="wikilink" title="incubator">incubator</a>
or <a href="Ostrich_Incubator" class="wikilink"
title="ostrich incubator">ostrich incubator</a> to hatch this animal. If
the animal's <samp>House</samp> field doesn't match the current
building, the entry will be ignored. Default none.</p></td>
</tr>
<tr>
<td><p><samp>IncubationTime</samp></p></td>
<td><p><em>(Optional)</em> How long eggs incubate before they hatch.
Default 9000 minutes.</p></td>
</tr>
<tr>
<td><p><samp>IncubatorParentSheetOffset</samp></p></td>
<td><p><em>(Optional)</em> An offset applied to the incubator's sprite
index when it's holding an egg. Default 1.</p>
<p>The vanilla values are:</p>
<table>
<thead>
<tr>
<th><p>offset</p></th>
<th><p><a href="incubator" class="wikilink"
title="incubator">incubator</a></p></th>
<th><p><a href="Ostrich_Incubator" class="wikilink"
title="ostrich incubator">ostrich incubator</a></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0</p></td>
<td><p>empty incubator</p></td>
<td><p>empty incubator</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>small white egg</p></td>
<td><p>large brown egg</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>small brown egg</p></td>
<td><p><em>invalid</em> (will show <a href="Junimo_Chest"
class="wikilink" title="Junimo chest">Junimo chest</a> sprite)</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>BirthText</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Tokenizable_strings"
class="wikilink" title="tokenizable string">tokenizable string</a> for
the message shown when entering the building after the egg hatched.
Defaults to the text "<samp>???</samp>".</p></td>
</tr>
</tbody>
</table>

### Growth

| field | effect |
|----|----|
| `DaysToMature` | *(Optional)* The number of days until a freshly purchased/born animal becomes an adult and begins producing items. Default 1. |
| `CanGetPregnant` | *(Optional)* Whether an animal can <a href="Animals#Animal_Births" class="wikilink"
title="produce a child">produce a child</a> (regardless of gender). Default false. |

### Produce

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ProduceItemIds</samp><br />
<samp>DeluxeProduceItemIds</samp></p></td>
<td><p><em>(Optional)</em> The items produced by the animal when it's an
adult. The <samp>DeluxeProduceItemIds</samp> field only applies if the
<samp>Deluxe*</samp> fields match. Both default to none.</p>
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
<td><p>The <a href="Modding_Objects" class="wikilink"
title="unqualified object ID"><em>unqualified</em> object ID</a> of the
item to produce.</p></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this item can be produced now. Defaults to always
true.</p></td>
</tr>
<tr>
<td><p><samp>MinimumFriendship</samp></p></td>
<td><p><em>(Optional)</em> The minimum friendship points with the animal
needed to produce this item. Default 0.</p></td>
</tr>
</tbody>
</table>
<p>If multiple items can be produced, one is chosen at random (with
deluxe items taking priority if applicable).</p></td>
</tr>
<tr>
<td><p><samp>DaysToProduce</samp></p></td>
<td><p><em>(Optional)</em> The number of days between item productions.
For example, setting <samp>1</samp> will produce an item every day.
Default 1.</p></td>
</tr>
<tr>
<td><p><samp>ProduceOnMature</samp></p></td>
<td><p><em>(Optional)</em> Whether an item is produced on the day the
animal becomes an adult. Default false.</p></td>
</tr>
<tr>
<td><p><samp>FriendshipForFasterProduce</samp></p></td>
<td><p><em>(Optional)</em> The minimum friendship points needed to
reduce the <samp>DaysToProduce</samp> by one. Defaults to no reduction
based on friendship.</p></td>
</tr>
<tr>
<td><p><samp>DeluxeProduceMinimumFriendship</samp></p></td>
<td><p><em>(Optional)</em> The minimum friendship points needed to
produce the <samp>DeluxeProduceItemId</samp>. Default 200.</p></td>
</tr>
<tr>
<td><p><samp>DeluxeProduceCareDivisor</samp><br />
<samp>DeluxeProduceLuckMultiplier</samp></p></td>
<td><p><em>(Optional)</em> <a
href="Modding_Common_data_field_types#Quantity_modifiers"
class="wikilink" title="Quantity modifiers">Quantity modifiers</a> which
change the probability of producing the
<samp>DeluxeProduceItemId</samp>, based on this formula:</p>
<pre><code>if happiness &gt; 200:
   happiness_modifier = happiness * 1.5
else if happiness &gt; 100:
   happiness_modifier = 0
else
   happiness_modifier = happiness - 100
&#10;((friendship + happiness_modifier) / DeluxeProduceCareDivisor) + (daily_luck * DeluxeProduceLuckMultiplier)</code></pre>
<p>Specifically:</p>
<ul>
<li><samp>DeluxeProduceCareDivisor</samp> reduces the bonus from
friendship and happiness, so a lower value <em>increases</em> the
probability of producing the deluxe item. Default 1200.</li>
<li><samp>DeluxeProduceLuckMultiplier</samp> increases the effect of <a
href="Luck" class="wikilink" title="daily luck">daily luck</a>. Default
0.</li>
</ul>
<p>For example, given a friendship of 102 and happiness of 150, the
probability with the default field values will be
<code>((102 + 0) / 1200) + (daily_luck * 0) = (102 / 1200) = 0.085</code>
or 8.5%.</p>
<p>See <a href="Animals#Produce" class="wikilink"
title="Animal Produce">Animal Produce</a> for more info on the
calculation.</p></td>
</tr>
<tr>
<td><p><samp>HarvestType</samp></p></td>
<td><p><em>(Optional)</em> How produced items are collected from the
animal. The valid values are:</p>
<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>DropOvernight</samp></p></td>
<td><p>The item is placed on the ground in the animal's home building
overnight.</p></td>
</tr>
<tr>
<td><p><samp>HarvestWithTool</samp></p></td>
<td><p>The item is collected from the animal directly based on the
<samp>HarvestTool</samp> field.</p></td>
</tr>
<tr>
<td><p><samp>DigUp</samp></p></td>
<td><p>The farm animal will dig it up randomly throughout the day. This
applies the same logic as <a href="Pig#Produce" class="wikilink"
title="pigs finding truffles">pigs finding truffles</a>, but for the
current item to produce via <samp>ProduceItemIds</samp> and
<samp>DeluxeProduceItemIds</samp>.</p></td>
</tr>
</tbody>
</table>
<p>Default <samp>DropOvernight</samp>.</p></td>
</tr>
<tr>
<td><p><samp>HarvestTool</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Tools" class="wikilink"
title="tool ID">tool ID</a> with which produced items can be collected
from the animal, if the <samp>HarvestType</samp> is set to
<samp>HarvestWithTool</samp>. The values recognized by the vanilla tools
are <samp>Milk Pail</samp> and <samp>Shears</samp>. Default
none.</p></td>
</tr>
<tr>
<td><p><samp>CanEatGoldenCrackers</samp></p></td>
<td><p><em>(Optional)</em> Whether players can feed this animal a golden
cracker to double its normal output. Default true.</p></td>
</tr>
</tbody>
</table>

### Audio & Sprite

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Sound</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Audio" class="wikilink"
title="audio cue ID">audio cue ID</a> for the sound produced by the
animal (e.g. when pet). Default none.</p></td>
</tr>
<tr>
<td><p><samp>BabySound</samp></p></td>
<td><p><em>(Optional)</em> Overrides <samp>Sound</samp> field when the
animal is a baby. Has no effect if <samp>Sound</samp> isn't specified.
Default none.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p><em>(Optional)</em> The asset name for the animal's spritesheet.
Defaults to <samp>Animals/&lt;ID&gt;</samp> (like
<samp>Animals/Goat</samp> for a <a href="goat" class="wikilink"
title="goat">goat</a>). This asset must exist even if you use
<samp>Skins</samp> below, since the default appearance is automatically
an available skin. See <a href="#Spritesheet_layout" class="wikilink"
title="spritesheet layout">spritesheet layout</a>.</p></td>
</tr>
<tr>
<td><p><samp>HarvestedTexture</samp></p></td>
<td><p><em>(Optional)</em> Overrides <samp>Texture</samp> if the animal
doesn't currently have an item ready to collect (like the <a
href="sheep" class="wikilink" title="sheep">sheep</a>'s sheared sprite).
Default none.</p></td>
</tr>
<tr>
<td><p><samp>BabyTexture</samp></p></td>
<td><p><em>(Optional)</em> Overrides <samp>Texture</samp> and
<samp>HarvestedTexture</samp> when the animal is a baby. Default
none.</p></td>
</tr>
<tr>
<td><p><samp>UseFlippedRightForLeft</samp></p></td>
<td><p><em>(Optional)</em> When the animal is facing left, whether to
use a flipped version of their right-facing sprite. See <a
href="#Spritesheet_layout" class="wikilink"
title="spritesheet layout">spritesheet layout</a> for more info. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>SpriteWidth</samp><br />
<samp>SpriteHeight</samp></p></td>
<td><p><em>(Optional)</em> The pixel height &amp; width of the animal's
sprite (before the in-game pixel zoom). Both default to 16.</p></td>
</tr>
<tr>
<td><p><samp>EmoteOffset</samp></p></td>
<td><p><em>(Optional)</em> A pixel offset to apply to emotes from the
farm animal, specified as an object with <samp>X</samp> and
<samp>Y</samp>. Default zero.</p></td>
</tr>
<tr>
<td><p><samp>SwimOffset</samp></p></td>
<td><p><em>(Optional)</em> A pixel offset to apply to the farm animal's
sprite while it's swimming, specified as an object with <samp>X</samp>
and <samp>Y</samp>. Default <samp>"X": 0, "Y": 112</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Skins</samp></p></td>
<td><p><em>(Optional)</em> A list of alternate appearances. If
specified, a skin is chosen at random when the animal is purchased or
hatched based on the <samp>Weight</samp> field. The default appearance
(e.g. using <samp>Texture</samp>) is automatically an available skin
with a weight of 1.</p>
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
<td><p><samp>ID</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for the
skin within the current list.</p></td>
</tr>
<tr>
<td><p><samp>Weight</samp></p></td>
<td><p><em>(Optional)</em> A multiplier for the probability to choose
this skin when an animal is purchased. For example, <samp>2.0</samp>
will double the chance this skin is selected relative to the other
skins. Default <samp>1.0</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Texture</samp><br />
<samp>HarvestedTexture</samp><br />
<samp>BabyTexture</samp></p></td>
<td><p><em>(Optional)</em> Overrides the equivalent main field when this
skin is selected. Defaults to the main field's value.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>SleepFrame</samp></p></td>
<td><p><em>(Optional)</em> The sprite index in the texture to display
when sleeping. Default 12.</p></td>
</tr>
<tr>
<td><p><samp>UseDoubleUniqueAnimationFrames</samp></p></td>
<td><p><em>(Optional)</em> Whether the texture has two frames for the
randomized 'unique' animation instead of one. See <a
href="#Spritesheet_layout" class="wikilink"
title="spritesheet layout">spritesheet layout</a> for more info. Default
false.</p>
<p>The unique animation sprite indexes are:</p>
<ul>
<li>If false: 13 (down), 14 (right), 12 (left if
<samp>UseFlippedRightForLeft</samp> is false), and 15 (up).</li>
<li>If true: 16 (down), 18 (right), 22 (left), and 20 (up).</li>
</ul></td>
</tr>
<tr>
<td><p><samp>ShadowWhenBaby</samp><br />
<samp>ShadowWhenBabySwims</samp><br />
<samp>ShadowWhenAdult</samp><br />
<samp>ShadowWhenAdultSwims</samp><br />
<samp>Shadow</samp></p></td>
<td><p><em>(Optional)</em> The shadow to draw under the farm animal.</p>
<p>The fields are checked in this order, and the first existing one
which matches the animal is used:</p>
<ol>
<li><samp>ShadowWhenBabySwims</samp> or
<samp>ShadowWhenAdultSwims</samp> when the animal is swimming;</li>
<li><samp>ShadowWhenBaby</samp> or <samp>ShadowWhenAdult</samp> in
general;</li>
<li>else <samp>Shadow</samp>.</li>
</ol>
<p>These consist of a model with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Visible</samp></p></td>
<td><p><em>(Optional)</em> Whether the shadow should be drawn. Default
true.</p></td>
</tr>
<tr>
<td><p><samp>Offset</samp></p></td>
<td><p><em>(Optional)</em> A pixel offset applied to the shadow
position, specified as an object with <samp>X</samp> and <samp>Y</samp>
fields. Default zero.</p></td>
</tr>
<tr>
<td><p><samp>Scale</samp></p></td>
<td><p><em>(Optional)</em> The scale at which to draw the shadow.
Default 2.5 (swimming baby), 3 (baby), 3.5 (swimming adult), or 4
(adult).</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### Player profession effects

| field | effect |
|----|----|
| `ProfessionForFasterProduce` | *(Optional)* The internal ID of a <a href="Skills" class="wikilink" title="profession">profession</a> which reduces the `DaysToProduce` by one. Default none. |
| `ProfessionForHappinessBoost` | *(Optional)* The internal ID of a <a href="Skills" class="wikilink" title="profession">profession</a> which makes it easier to befriend this animal. Default none. |
| `ProfessionForQualityBoost` | *(Optional)* The internal ID of a <a href="Skills" class="wikilink" title="profession">profession</a> which increases the chance of higher-quality produce. Default none. |

### Behavior

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>CanSwim</samp></p></td>
<td><p><em>(Optional)</em> Whether animals on the farm can swim in water
once they've been pet. Default false.</p></td>
</tr>
<tr>
<td><p><samp>BabiesFollowAdults</samp></p></td>
<td><p><em>(Optional)</em> Whether baby animals can follow nearby
adults. Default false.</p></td>
</tr>
<tr>
<td><p><samp>GrassEatAmount</samp></p></td>
<td><p><em>(Optional)</em> The amount of grass eaten by this animal each
day. Setting it to <samp>0</samp> will disable the farm animal's hunger.
Default 2.</p></td>
</tr>
<tr>
<td><p><samp>HappinessDrain</samp></p></td>
<td><p><em>(Optional)</em> An amount which affects the daily reduction
in happiness if the animal wasn't pet, or didn't have a heater in
winter. Default none.</p></td>
</tr>
<tr>
<td><p><samp>SellPrice</samp></p></td>
<td><p><em>(Optional)</em> The price when <a
href="Animals#Selling_Animals" class="wikilink"
title="the player sells the animal">the player sells the animal</a>,
before it's adjusted for the animal's friendship towards the player.
Default 0.</p>
<p>The actual sell price will be this value multiplied by a number
between 0.3 (zero friendship) and 1.3 (max friendship).</p></td>
</tr>
<tr>
<td><p><samp>CustomFields</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Custom_fields"
class="wikilink" title="custom fields">custom fields</a> for this
entry.</p></td>
</tr>
</tbody>
</table>

### Other

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ShowInSummitCredits</samp></p></td>
<td><p><em>(Optional)</em> Whether to show the farm animal in the credit
scene on <a href="The_Summit" class="wikilink" title="the summit">the
summit</a> after the player achieves <a href="perfection"
class="wikilink" title="perfection">perfection</a>. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>StatToIncrementOnProduce</samp></p></td>
<td><p><em>(Optional)</em> The <a href="Modding_Stats" class="wikilink"
title="tracked stats">tracked stats</a> to increment when the animal
produces an item. Default none. This consists of a list of models with
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
<td><p><samp>ID</samp></p></td>
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
<td><p><em>(Optional)</em> The qualified or unqualified <a
href="Modding_Objects" class="wikilink" title="object ID">object ID</a>
that the animal must produce to increment the stat listed in
<samp>StatName</samp>. If both this field and <samp>RequiredTags</samp>
are omitted the stat will increase every time the animal produces any
item.</p></td>
</tr>
<tr>
<td><p><samp>RequiredTags</samp></p></td>
<td><p><em>(Optional)</em> A comma-delimited list of <a
href="Modding_Context_tags" class="wikilink"
title="context tags">context tags</a> required on the item produced. The
stat is only incremented if the item has <em>all</em> of these. You can
negate a tag with <samp>!</samp> (like
<code>bone_item, !fossil_item</code> for bone items that aren't
fossils). Defaults to always enabled.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>UpDownPetHitboxTileSize</samp><br />
<samp>LeftRightPetHitboxTileSize</samp></p></td>
<td><p><em>(Optional)</em> The animal sprite's <a
href="Modding_Modder_Guide_Game_Fundamentals#Tiles" class="wikilink"
title="tile">tile</a> size in the world when the player is clicking to
pet them, specified in the form <samp>&lt;width&gt;,
&lt;height&gt;</samp>. The <samp>UpDownPetHitboxTileSize</samp> applies
when the animal is facing up or down, and
<samp>LeftRightPetHitboxTileSize</samp> applies when facing left or
right. The values can be fractional (<em>e.g.</em> cows have a width of
1.75). Both default to a 1×1 tile.</p></td>
</tr>
<tr>
<td><p><samp>BabyUpDownPetHitboxTileSize</samp><br />
<samp>BabyLeftRightPetHitboxTileSize</samp></p></td>
<td><p><em>(Optional)</em> Overrides
<samp>UpDownPetHitboxTileSize</samp> and
<samp>LeftRightPetHitboxTileSize</samp> respectively before the animal
is an adult. Both default to 1×1 tile.</p></td>
</tr>
</tbody>
</table>

## Spritesheet layout

Each farm animal's spritesheet must have exactly 4 columns, and at least
5–7 rows (depending on the data fields). The sprite size depends on the
<a href="#Audio_.26_Sprite" class="wikilink"
title="SpriteWidth and SpriteHeight"><samp>SpriteWidth</samp> and
<samp>SpriteHeight</samp></a> fields; for example, the default sprite
width of 16 pixels means the spritesheet must be exactly 4 × 16 = 64
pixels wide.

The expected rows are:

1.  move down;
2.  move right;
3.  move up;
4.  move left (**only** if `UseFlippedRightForLeft` is false);
5.  unique animations 1;
6.  unique animations 2 (**only** if `UseDoubleUniqueAnimationFrames` is
    true);
7.  eat.

For example, the default layout (with `UseFlippedRightForLeft` and
`UseDoubleUniqueAnimationFrames` both false) is:

|                  |                  |                   |                  |
|------------------|------------------|-------------------|------------------|
| 0 (move down 1)  | 1 (move down 2)  | 2 (move down 3)   | 3 (move down 4)  |
| 4 (move right 1) | 5 (move right 2) | 6 (move right 3)  | 7 (move right 4) |
| 8 (move up)      | 9 (move up)      | 10 (move up)      | 11 (move up)     |
| 12 (*unused*)    | 13 (unique down) | 14 (unique right) | 15 (unique up)   |
| 16 (eat 1)       | 17 (eat 1)       | 18 (eat 1)        | 19 (eat 1)       |

When both are true, that becomes:

|  |  |  |  |
|----|----|----|----|
| 0 (move down 1) | 1 (move down 2) | 2 (move down 3) | 3 (move down 4) |
| 4 (move right 1) | 5 (move right 2) | 6 (move right 3) | 7 (move right 4) |
| 8 (move up) | 9 (move up) | 10 (move up) | 11 (move up) |
| 12 (move left) | 13 (move left) | 14 (move left) | 15 (move left) |
| 16 (unique down 1) | 17 (unique down 2) | 18 (unique right 1) | 19 (unique right 2) |
| 20 (unique up 1) | 21 (unique up 2) | 22 (unique left 1) | 23 (unique left 2) |
| 24 (eat 1) | 25 (eat 1) | 26 (eat 1) | 27 (eat 1) |

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Животные" class="wikilink"
title="ru:Модификации:Животные">ru:Модификации:Животные</a>
<a href="zh_模组_动物数据" class="wikilink"
title="zh:模组:动物数据">zh:模组:动物数据</a>
