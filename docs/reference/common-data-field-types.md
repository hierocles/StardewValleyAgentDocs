---
title: "Common Data Field Types"
wiki_source: "Modding:Common data field types"
permalink: /Modding:Common_data_field_types/
category: reference
tags: [common-data-field-types, string-formats, unique-string-id, asset-name, color, context-tag, custom-fields, game-state-query]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents common field types which appear in
<a href="Modding_Editing_XNB_files" class="wikilink"
title="the game&#39;s data files">the game's data files</a>.

You normally don't need to read through this page directly; specific
sections are linked from field docs on other pages.

## String formats

These formats can only be used in fields that specifically support them.
The field docs will link to this page if applicable.

### Unique string ID

The game identifies data using unique string IDs. For example, `Town` is
the unique ID for the
<a href="Pelican_Town" class="wikilink" title="Pelican Town">Pelican
Town</a> location; no other location can use that ID. The IDs are used
for a wide range of purposes, from internal game logic to
<a href="Modding_Content_Patcher" class="wikilink"
title="content pack edits">content pack edits</a>.

Best practices for mods:

1.  **Use namespaced IDs prefixed with your
    <a href="Modding_Modder_Guide_APIs_Manifest#Basic_fields"
    class="wikilink" title="mod&#39;s unique ID">mod's unique ID</a>.**
    For example, if your mod ID is `Example.PufferchickMod` and you're
    adding a pufferchick plushy, your item ID would look like
    `Example.PufferchickMod_PufferchickPlushy`. Prefer that *exact*
    format; it's the one expected by the game code and parsed by other
    mods.
2.  **Only use alphanumeric, underscore, and dot characters** in string
    IDs (`a–z A–Z 0–9 _ .`). This is important because they're often
    used in places where some characters have special meaning (like file
    names or <a href="#Game_state_query" class="wikilink"
    title="game state queries">game state queries</a>).
3.  **Insert the mod ID automatically** to avoid typos and inconsistent
    capitalization (so it's compatible with mods which parse it):
    - In a <a href="Modding_Content_Patcher" class="wikilink"
      title="Content Patcher pack">Content Patcher pack</a>, use
      `_PufferchickPlushy`. (Type the exact string ; it's a token
      recognized by Content Patcher.)
    - In a C# mod, use
      `$"{this.ModManifest.UniqueID}_PufferchickPlushy"`.

You're strongly encouraged to use this exact format to maintain good mod
compatibility, eliminate ID conflicts, and make it easy (for both
troubleshooters and mod code) to identify which mod added custom
content.

### Asset name

An *asset name* uniquely identifies a
<a href="Modding_Editing_XNB_files" class="wikilink"
title="game asset">game asset</a>. These usually match files in the
game's `Content` folder, but mods can add custom assets using
<a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> or the
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="C# content API">C# content API</a>.

For example, `Portraits/Abigail` contains
<a href="Abigail" class="wikilink" title="Abigail">Abigail</a>'s
portraits.

Asset names **do not** include the `Content/` prefix, file extension, or
locale code. For example, the `Content/Data/Achievements.de-DE.xnb` file
has asset name `Data/Achievements`.

### Color

Data assets can define colors using a standard format. For example:

``` js
"DebrisColor": "White"
```

The supported color formats are:

<table>
<thead>
<tr>
<th><p>format</p></th>
<th><p>example</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>A <a
href="https://learn.microsoft.com/en-us/dotnet/api/system.drawing.color?view=netframework-4.8.1#properties"><samp>Color</samp>
property name</a>.</p></td>
<td><p><samp>ForestGreen</samp></p></td>
</tr>
<tr>
<td><p>A <a
href="https://en.wikipedia.org/wiki/Web_colors#Hex_triplet">hexadecimal
color code</a>. The optional alpha is a value between <samp>00</samp>
(transparent) and <samp>FF</samp> (opaque).</p></td>
<td><p><samp>#228B22</samp><br />
<samp>#228B22FF</samp></p></td>
</tr>
<tr>
<td><p>An <a
href="https://en.wikipedia.org/wiki/RGB_color_model#Numeric_representations">8-bit
RGB color code</a>. The optional alpha is a value between <samp>0</samp>
(transparent) and <samp>255</samp> (opaque).</p></td>
<td><p><samp>34 139 34</samp><br />
<samp>34 139 34 255</samp></p></td>
</tr>
</tbody>
</table>

C# mods can parse a color like `Utility.StringToColor("White")`.

### Context tag

A *context tag* is an arbitrary data label attached to items. The game
auto-generates some context tags, while others can be added through the
item data.

These can produce various effects in-game, be queried in various asset
fields or using the `ITEM_CONTEXT_TAG`
<a href="#Game_state_query" class="wikilink"
title="game state query">game state query</a>, or may be informational
only.

See <a href="Modding_Context_tags" class="wikilink"
title="Modding:Context tags">Modding:Context tags</a> for more info.

### Custom fields

Many data assets have a `CustomFields` field. This is ignored by the
game, but can be read by mod frameworks to enable custom features.

For example, a content pack can
<a href="Modding_Crop_data" class="wikilink" title="add a crop">add a
crop</a> with custom fields:

``` js
"CustomFields": {
    "Example.FrameworkMod/WetTexture": ""
}
```

And then a C# mod could handle the custom field if it's set:

``` c#
CropData data = crop.GetData();
if (data != null && data.CustomFields.TryGetValue("Example.FrameworkMod/WetTexture", out string textureName))
{
    // do magic
}
```

### Game state query

A *game state query* defines a condition using a special command syntax.
For example, this checks if today is spring or summer:

``` js
"Condition": "SEASON Spring Summer"
```

See <a href="Modding_Game_state_queries" class="wikilink"
title="Modding:Game state queries">Modding:Game state queries</a> for
more info.

### Item ID

Every item is identified by two strings:

- An *unqualified item ID* (`item.ItemId`) is a
  <a href="#Unique_string_ID" class="wikilink"
  title="unique string ID">unique string ID</a> for the item. This
  should generally be unique, but older vanilla items have non-unique
  numeric IDs for legacy reasons.
- A *qualified item ID* (`item.QualifiedItemId`) prefixes the
  unqualified ID with the type identifier to guarantee uniqueness.

For example,
<a href="pufferfish" class="wikilink" title="pufferfish">pufferfish</a>
has two item IDs: `128` (unqualified) and `(O)128` (qualified).

See <a href="Modding_Items" class="wikilink"
title="Modding:Items">Modding:Items</a> for more info.

### Item query

An *item query* creates any number of items dynamically using either an
<a href="#Item_ID" class="wikilink" title="item ID">item ID</a> or a
special command syntax. For example, you can select random
<a href="House_Plant" class="wikilink" title="house plants">house
plants</a>:

``` js
"ItemId": "RANDOM_ITEMS (F) 1376 1390"
```

See <a href="Modding_Item_queries" class="wikilink"
title="Modding:Item queries">Modding:Item queries</a> for more info.

### Tokenizable string

A *tokenizable string* is text which can contain special tokens. For
example, this shows a message like "It's a beautiful spring day":

``` js
"Message": "It's a beautiful [Season] day"
```

See <a href="Modding_Tokenizable_strings" class="wikilink"
title="Modding:Tokenizable strings">Modding:Tokenizable strings</a> for
more info.

### Translation key

A *translation key* uniquely identifies where to find translatable text,
in the form `<asset name>:<key>`. For example,
`Strings\\StringsFromCSFiles:spring` will look for a `spring` key in the
`Strings\StringsFromCSFiles` asset file in the content folder.

This is often used in game code (*e.g.* via `Game1.content.LoadString`)
and in data assets (*e.g.* via the `LocalizedText`
<a href="#Tokenizable_string" class="wikilink"
title="tokenizable string">tokenizable string</a> token).

### Trigger action

A *trigger action* performs an action when something happens, with
support for a wide range of actions (like sending mail, changing
friendship, starting a quest, etc).

For example, you can give the player an item from dialogue:

``` js
"Message": "Hi there! Here's a pufferfish.#%action AddItem (O)128"
```

See <a href="Modding_Trigger_actions" class="wikilink"
title="Modding:Trigger actions">Modding:Trigger actions</a> for more
info.

## Data structures

### Item spawn fields

*Item spawn fields* are a common set of fields used to create items
using <a href="#Item_query" class="wikilink" title="item queries">item
queries</a> in many data assets.

For example, you can create an iridium-quality strawberry juice:

``` js
"ItemId": "FLAVORED_ITEM Juice (O)400",
"Quality": 4
```

See <a href="Modding_Item_queries#Item_spawn_fields" class="wikilink"
title="Modding:Item queries#Item spawn fields">Modding:Item queries#Item
spawn fields</a> for more info.

### Mod data

`modData` dictionary fields store custom data about instances. These are
synchronized in multiplayer, persisted in the save file, and accessible
from both C# and <a href="#Game_state_query" class="wikilink"
title="game state queries">game state queries</a> like
`PLAYER_MOD_DATA`.

When you split an item stack, the new stack copies the previous one's
mod data; when merged into another stack, the merged items adopt the
target stack's mod data. Otherwise mod data has no effect on item
split/merge logic (*e.g.* you can still merge items with different mod
data).

In C#, these are available on these types: `Character` (including
monsters, NPCs, and players), `GameLocation`, `Item`, `Projectile`,
`Quest`, and `TerrainFeature`.

To avoid mod conflicts, mod data keys should be
<a href="#Unique_string_ID" class="wikilink"
title="unique string IDs">unique string IDs</a>:

``` C#
item.modData[$"{this.ModManifest.UniqueID}/item-age"] = "30";
```

### Point

A point represents an integer coordinate or size, usually measured in
pixels or tiles. This is formatted as an object with an X/Y position.
For example:

``` js
"Position": {
    "X": 0,
    "Y": 0
}
```

### Quantity modifiers

*Quantity modifiers* apply dynamic changes to a numeric field in a data
asset like <a href="Modding_Shops" class="wikilink"
title="Data/Shops"><samp>Data/Shops</samp></a> or
<a href="Modding_Machines" class="wikilink"
title="Data/Machines"><samp>Data/Machines</samp></a>. For example, you
can multiply a shop item's price or increase a machine output's quality.
You can specify any number of modifiers for the same field.

#### Modifier format

These consist of a list of models with these fields:

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
modifier within the current list.</p></td>
</tr>
<tr>
<td><p><samp>Modification</samp></p></td>
<td><p>The type of change to apply. The possible values are
<samp>Add</samp>, <samp>Subtract</samp>, <samp>Multiply</samp>,
<samp>Divide</samp>, and <samp>Set</samp>.</p></td>
</tr>
<tr>
<td><p><samp>Amount</samp></p></td>
<td><p><em>(Optional if <samp>RandomAmount</samp> specified)</em> The
operand applied to the target value (e.g. the multiplier if used with
<samp>Multiply</samp>).</p></td>
</tr>
<tr>
<td><p><samp>RandomAmount</samp></p></td>
<td><p><em>(Optional)</em> A list of possible amounts to randomly choose
from. If set, <samp>Amount</samp> is optional and ignored. Each entry in
the list has an equal probability of being chosen, and the choice is
persisted for the current day. For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;RandomAmount&quot;</span><span class="op">:</span> [ <span class="dv">1</span><span class="op">,</span> <span class="dv">2</span><span class="op">,</span> <span class="fl">3.5</span><span class="op">,</span> <span class="dv">4</span> ]</span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Condition</samp></p></td>
<td><p><em>(Optional)</em> A <a href="Modding_Game_state_queries"
class="wikilink" title="game state query">game state query</a> which
indicates whether this change should be applied. Defaults to always
true.</p></td>
</tr>
</tbody>
</table>

#### Modifier mode

Quality modifier fields are often accompanied by a *mode* field (like
`PriceModifiers` and `PriceModifierMode`), which indicate what to do
when multiple modifiers apply to the same value. Available modes:

| value | effect |
|----|----|
| `Stack` | Apply each modifier to the result of the previous one. For example, two modifiers which double a value will quadruple it. |
| `Minimum` | Apply the modifier which results in the lowest value. |
| `Maximum` | Apply the modifier which results in the highest value. |

#### Examples

For example, this will double the price of a shop item in `Data/Shops`:

``` js
"PriceModifiers": [
    {
        "Modification": "Multiply",
        "Amount": 2.0
    }
]
```

This will set the price to a random value between 100–1000, *or* 3–5
times the item's normal sell price, whichever is higher (like the
<a href="Traveling_Cart" class="wikilink"
title="Traveling Cart">Traveling Cart</a>):

``` js
"PriceModifierMode": "Maximum",
"PriceModifiers": [
    {
        "Modification": "Set",
        "RandomAmount": [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ]
    },
    {
        "Modification": "Multiply",
        "RandomAmount": [ 3, 4, 5 ]
    }
]
```

### Rectangle

A rectangle represents a square area, usually measured in pixels or
tiles. This is formatted as an object with an X/Y position (for the
top-left corner) and width/height size, where all values are integers.
For example:

``` js
"Rectangle": {
    "X": 0,
    "Y": 0,
    "Width": 16,
    "Height": 32
}
```

### Vector2

A Vector2 represents a non-integer coordinate or size, usually measured
in pixels or tiles. This is formatted as an object with an X/Y position.
For example:

``` js
"Position": {
    "X": 10.5,
    "Y": 12.0
}
```

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Типы_распространенных_полей_данных"
class="wikilink"
title="ru:Модификации:Типы распространенных полей данных">ru:Модификации:Типы
распространенных полей данных</a>
<a href="zh_模组_公共数据字段" class="wikilink"
title="zh:模组:公共数据字段">zh:模组:公共数据字段</a>
