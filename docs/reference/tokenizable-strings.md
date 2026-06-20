---
title: "Tokenizable Strings"
wiki_source: "Modding:Tokenizable strings"
permalink: /Modding:Tokenizable_strings/
category: reference
tags: [tokenizable-strings, format, overview, token-format, token-argument-format, tokens, game-data, localization]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents **tokenizable strings**, a built-in way to build
display text which can contain any combination of literal text,
translations, and placeholder values.

## Format

### Overview

You can only use tokenizable strings in data fields that specifically
allow them (which will be indicated in the wiki docs).

A tokenizable string can contain any combination of literal text and
tokens
(<a href="#Tokens" class="wikilink" title="listed below">listed below</a>).
For example:

``` js
"Dialogue": "Welcome to Pierre's! How is [FarmName] doing?"
```

When using <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a>, you can use its tokens
anywhere in the string (including within square brackets); they'll be
expanded before the game parses the string. For example,
`" would love [ArticleFor [SuggestedItem]] [SuggestedItem]!"` would
output something like "*Abigail would love an Apple!*".

### Token format

A *token* is a predefined placeholder which produces text, wrapped in
square brackets. Token names are not case-sensitive, so
`[LocalizedText]` and `[LOCALIZEDTEXT]` are equivalent.

For example, this will show a message like "*Welcome to Pierre's! This
is raw text*":

``` js
"Dialogue": "[LocalizedText Strings\StringsFromCSFiles:ShopMenu.cs.11488] "
```

### Token argument format

A token can optionally have arguments (which can in turn contain
tokens). In the above example, the `LocalizedText` takes one argument
(the translation key to display). Arguments are space-delimited, so you
need to use `EscapedText` to pass an argument containing spaces:

``` js
"Dialogue": "[LocalizedText [EscapedText Strings\BundleNames:Quality Fish]]"
```

## Tokens

Here are the tokens provided by the base game.

### Game data

<table>
<thead>
<tr>
<th><p>token format</p></th>
<th><p>output</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>[DayOfMonth]</samp></p></td>
<td><p>The numeric day of month, like <samp>5</samp> on spring
5.</p></td>
</tr>
<tr>
<td><p><samp>[FarmerUniqueID]</samp></p></td>
<td><p>The target player's unique internal multiplayer ID</p></td>
</tr>
<tr>
<td><p><samp>[FarmName]</samp></p></td>
<td><p>The farm name for the current save (without the injected "Farm"
text).</p></td>
</tr>
<tr>
<td><p><samp>[FarmerStat &lt;key&gt;]</samp></p></td>
<td><p>The value of a <a href="Modding_Stats" class="wikilink"
title="tracked stat">tracked stat</a> for the current player.</p>
<p>For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode js"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;You&#39;ve walked [FarmerStat stepsTaken] steps so far.&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>[Season]</samp></p></td>
<td><p>The current season name, like <em>spring</em>.</p></td>
</tr>
<tr>
<td><p><samp>[SuggestedItem [interval] [sync key]]</samp></p></td>
<td><p><strong>(For shops only.)</strong> The name of a random item
currently available in the shop stock.</p>
<p>The result will be identical for all queries with the same [sync key]
during the given [interval] (one of <samp>tick</samp>, <samp>day</samp>,
<samp>season</samp>, <samp>year</samp>), including between players in
multiplayer mode. If omitted, they default to <samp>day</samp> and the
shop ID respectively.</p></td>
</tr>
</tbody>
</table>

### Localization

<table>
<thead>
<tr>
<th><p>token format</p></th>
<th><p>output</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>[ArticleFor &lt;word&gt;]</samp></p></td>
<td><p>The grammatical article (<em>a</em> or <em>an</em>) for the given
word when playing in English, else blank. For example,
<code>[ArticleFor apple] apple</code> will output <em>an
apple</em>.</p></td>
</tr>
<tr>
<td><p><samp>[AchievementName &lt;id&gt;]</samp></p></td>
<td><p>The translated display name for an achievement from <a
href="Modding_Achievement_data" class="wikilink"
title="Data/Achievements"><samp>Data/Achievements</samp></a>. For
example, <samp>[AchievementName 5]</samp> will output <em>A Complete
Collection</em> in English.</p></td>
</tr>
<tr>
<td><p><samp>[CharacterName &lt;name&gt;]</samp></p></td>
<td><p>The translated display name for an NPC, given their internal
name.</p></td>
</tr>
<tr>
<td><p><samp>[GenderedText &lt;male text&gt; &lt;female text&gt; [other
text]]</samp></p></td>
<td><p>Depending on the target player's gender, show either the male,
female, or other text. If the text contains spaces, you'll need to
escape them using <samp>EscapedText</samp>. If the player's gender is
neither male nor female, the game will try to user the other text; if
not provided, it will fall back on the female text.</p></td>
</tr>
<tr>
<td><p><samp>[ItemName &lt;id&gt; [fallback text]]</samp></p></td>
<td><p>The translated display name for an item based on its qualified or
unqualified item ID. For example, <samp>[ItemName (O)128]</samp> will
output <em>Pufferfish</em> in English.</p>
<p>If the item doesn't exist, it'll output [fallback text] if specified,
else <em>Error Item (&lt;id&gt;)</em>.</p></td>
</tr>
<tr>
<td><p><samp>[ItemNameWithFlavor &lt;flavor type&gt; &lt;flavor
ID&gt;]</samp></p></td>
<td><p>The translated display name for a flavored item name,
where...</p>
<ul>
<li>&lt;flavor type&gt; is one of <samp>AgedRoe</samp>,
<samp>Bait</samp>, <samp>DriedFruit</samp>, <samp>DriedMushroom</samp>,
<samp>Honey</samp>, <samp>Jelly</samp>, <samp>Juice</samp>,
<samp>Pickle</samp>, <samp>Roe</samp>, <samp>SmokedFish</samp>, or
<samp>Wine</samp>;</li>
<li>&lt;flavor ID&gt; is the <a
href="Modding_Common_data_field_types#Item_ID" class="wikilink"
title="qualified or qualified item ID">qualified or qualified item
ID</a> for the flavor (e.g. the blueberry in blueberry wine).</li>
</ul></td>
</tr>
<tr>
<td><p><samp>[LocalizedText &lt;string key&gt;]</samp><br />
<samp>[LocalizedText &lt;string key&gt; &lt;token
values&gt;+]</samp></p></td>
<td><p>Translation text loaded from the given <a
href="Modding_Common_data_field_types#Translation_keys" class="wikilink"
title="translation key">translation key</a>. If the translation has
placeholder tokens like <samp>{0}</samp>, you can add the values after
the string key.</p></td>
</tr>
<tr>
<td><p><samp>[LocationName &lt;location ID&gt;]</samp></p></td>
<td><p>The translated display name for a location given its ID <a
href="Modding_location_data" class="wikilink"
title="in Data/Locations">in <samp>Data/Locations</samp></a>.</p></td>
</tr>
<tr>
<td><p><samp>[MovieName &lt;id&gt;]</samp></p></td>
<td><p>The translated display name for a movie from <a
href="Modding_Movie_theater_data" class="wikilink"
title="Data/Movies"><samp>Data/Movies</samp></a>. For example,
<samp>[MovieName spring_movie_0]</samp> will output <em>The Brave Little
Sapling</em> in English.</p></td>
</tr>
<tr>
<td><p><samp>[PositiveAdjective]</samp></p></td>
<td><p>A random adjective from the <samp>Strings\Lexicon</samp> data
asset's <samp>RandomPositiveAdjective_PlaceOrEvent</samp>
entry.</p></td>
</tr>
<tr>
<td><p><samp>[SpecialOrderName &lt;id&gt;]</samp></p></td>
<td><p>The translated display name for a special order from <a
href="Modding_Special_orders" class="wikilink"
title="Data/SpecialOrders"><samp>Data/SpecialOrders</samp></a>. If the
special order is currently active, it'll show the same name shown in the
quest log. For example, <samp>[SpecialOrder Caroline]</samp> will output
<em>Island Ingredients</em> in English.</p></td>
</tr>
<tr>
<td><p><samp>[SpouseFarmerText &lt;spouse is farmer text&gt; &lt;spouse
is NPC text&gt;</samp></p></td>
<td><p>Show a different text depending on whether the target player's
spouse is a player or NPC. If the text contains spaces, you'll need to
escape them using <samp>EscapedText</samp>.</p></td>
</tr>
<tr>
<td><p><samp>[SpouseGenderedText &lt;male text&gt; &lt;female text&gt;
[other text]]</samp></p></td>
<td><p>Equivalent to <samp>GenderedText</samp>, but based on the gender
of the player's spouse (NPC or another player) instead.</p></td>
</tr>
<tr>
<td><p><samp>[ToolName &lt;id&gt; [upgrade level]]</samp></p></td>
<td><p>The translated display name for a tool, including its upgrade
level if specified. For example, <samp>[ToolName (T)IridiumAxe]</samp>
will output <em>Iridium Axe</em> in English.</p></td>
</tr>
</tbody>
</table>

### String manipulation

<table>
<thead>
<tr>
<th><p>token format</p></th>
<th><p>output</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>[CapitalizeFirstLetter &lt;text&gt;]</samp></p></td>
<td><p>The input text, with the first letter capitalized.</p></td>
</tr>
<tr>
<td><p><samp>[EscapedText]</samp><br />
<samp>[EscapedText &lt;text&gt;]</samp></p></td>
<td><p>Marks a snippet of text as a single argument, so it can be safely
passed into another token's space-delimited arguments even if it's empty
or contains spaces.</p>
<p>For example, the <samp>SpouseFarmerText</samp> expects two arguments
separated by spaces. This passes an empty string for the first one, and
text containing spaces for the second:</p>
<pre><code>[SpouseFarmerText [EscapedText] [EscapedText spouse 28 63 2]]</code></pre></td>
</tr>
<tr>
<td><p><samp>[NumberWithSeparators &lt;number&gt;]</samp></p></td>
<td><p>Format a number with thousands separators based on the current
language. For example, <samp>[NumberWithSeparators 5000000]</samp> will
output <em>5,000,000</em> in English.</p></td>
</tr>
</tbody>
</table>

## Extensibility for C# mods

- C# mods can define custom tokens by calling
  `TokenParser.RegisterParser("tokenName", ...)`. To avoid conflicts,
  custom token names should apply the
  <a href="Modding_Common_data_field_types#Unique_string_ID"
  class="wikilink" title="unique string ID">unique string ID</a>
  conventions.
- The `TokenStringBuilder` class provides methods for creating token
  strings. For example, `TokenStringBuilder.ItemNameFor(item)` will
  produce a string like `[ItemName (O)128]` or
  `[ItemNameWithFlavor SmokedFish (O)128]`.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Строки_с_токенами" class="wikilink"
title="ru:Модификации:Строки с токенами">ru:Модификации:Строки с
токенами</a> <a href="zh_模组_模板字符串" class="wikilink"
title="zh:模组:模板字符串">zh:模组:模板字符串</a>
