---
title: "Custom Languages"
wiki_source: "Modding:Custom languages"
permalink: /Modding:Custom_languages/
category: game
tags: [custom-languages, add-a-custom-language, data-format, example, add-a-custom-font, font-files, limitations, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how to create custom languages in Stardew Valley
1.5.5+. This is an advanced guide for modders.

To translate text into an existing language, see
<a href="Modding_Translations" class="wikilink"
title="Modding:Translations">Modding:Translations</a> instead.

## Add a custom language

### Data format

You can add custom languages by editing the `Data/AdditionalLanguages`
asset. Each entry consists of an object with these fields:

<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>ID</samp></p></td>
<td><p>A <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> for your
language. This isn't shown in-game.</p></td>
</tr>
<tr>
<td><p><samp>LanguageCode</samp></p></td>
<td><p>The language code for this localization. This should ideally be
an <a href="wikipedia_List_of_ISO_639-1_codes" class="wikilink"
title="ISO 639-1 code">ISO 639-1 code</a>, with only letters and
hyphens. You should avoid commas for compatibility with Content Patcher
packs checking the <samp>&lt;nowiki&gt;&lt;/nowiki&gt;</samp>
token.</p></td>
</tr>
<tr>
<td><p><samp>ButtonTexture</samp></p></td>
<td><p>The asset name for a 174x78 pixel texture containing the button
of the language for language selection menu. The top half of the sprite
is the default state, while the bottom half is the hover state.</p></td>
</tr>
<tr>
<td><p><samp>TimeFormat</samp></p></td>
<td><p>A string which describes the in-game time format, with tokens
replaced by in-game values. For example,
<code>[HOURS_12]:[MINUTES] [AM_PM]</code> would show
<code>12:00 PM</code> at noon.</p>
<p>The valid tokens are:</p>
<ul>
<li><code>[HOURS_12]</code>: hours in 12-hour format, where midnight and
noon are both "12".</li>
<li><code>[HOURS_12_0]</code>: hours in 12-hour format, where midnight
and noon are both "0".</li>
<li><code>[HOURS_24]</code>: hours in 24-hour format, where midnight is
"0" and noon is "12".</li>
<li><code>[HOURS_24_00]</code>: hours in 24-hour format with
zero-padding, where midnight is "00" and noon is "12".</li>
<li><code>[MINUTES]</code>: minutes with zero-padding.</li>
<li><code>[AM_PM]</code>: the localized text for "am" or "pm" (taken
from <code>Strings\\StringsFromCSFiles:DayTimeMoneyBox.cs.10370</code>
and <code>DayTimeMoneyBox.cs.10371</code> respectively). The game shows
"pm" between noon and 11:59pm inclusively; it shows "am" otherwise.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>ClockTimeFormat</samp></p></td>
<td><p>A string which describes the in-game time format. Equivalent to
<samp>TimeFormat</samp>, but used for the in-game clock.</p></td>
</tr>
<tr>
<td><p><samp>ClockDateFormat</samp></p></td>
<td><p>A string which describes the in-game date format as shown in the
in-game clock, with tokens replaced by in-game values. For example,
<code>[DAY_OF_WEEK]. [DAY_OF_MONTH]</code> would show
<code>Mon. 1</code>.</p>
<p>The valid tokens are:</p>
<ul>
<li><code>[DAY_OF_WEEK]</code>: the abbreviated day of week as returned
by <code>Game1.shortDayDisplayNameFromDayOfSeason</code> (like
<samp>Mon</samp> for Monday).</li>
<li><code>[DAY_OF_MONTH]</code>: the numerical day of the month.</li>
</ul></td>
</tr>
<tr>
<td><p><samp>FontApplyYOffset</samp></p></td>
<td><p><em>(optional)</em> Whether to shift the font up by four pixels
(multiplied by the <samp>FontPixelZoom</samp>), to better align
languages with larger characters like Chinese and Japanese. Default
false.</p></td>
</tr>
<tr>
<td><p><samp>NumberComma</samp></p></td>
<td><p><em>(optional)</em> The string to use as the thousands separator
(like <code>","</code> for <code>5,000,000</code>). Defaults to a
comma.</p></td>
</tr>
<tr>
<td><p><samp>SmallFontLineSpacing</samp></p></td>
<td><p><em>(optional)</em> The line spacing value used by
<samp>smallFont</samp>. Defaults to 26.</p></td>
</tr>
<tr>
<td><p><samp>UseGenderedCharacterTranslations</samp></p></td>
<td><p><em>(optional)</em> Whether the social tab and gift log will use
gender-specific translations (like the vanilla Portuguese language).
Defaults to false.</p>
<p>Specifically, this affects the
<samp>Strings\StringsFromCSFiles:SocialPage.cs.11635</samp> translation
("<em>(Single)</em>"). When enabled, it can contain male and female
translations separated by <code>/</code>, like the vanilla Portuguese
translation: "<em>(solteiro)/(solteira)</em>".</p></td>
</tr>
<tr>
<td><p><em>custom font fields</em></p></td>
<td><p>See <em><a href="#Add_a_custom_font" class="wikilink"
title="add a custom font">add a custom font</a></em> below.</p></td>
</tr>
</tbody>
</table>

### Example

This Content Patcher pack would add Esperanto to the game. ( is a token,
which will be replaced with your mod ID automatically.)

Once the language is defined, you can add translations to the game by
patching game assets like usual, and use the language code you specified
above. For example:

``` json
{
    "Action": "EditData",
    "Target": "Strings/StringsFromCSFiles",
    "Entries": {
        "Game1.cs.3043": "Lundo",
        "Game1.cs.3044": "Mardo",
        ...
    },
    "When": {
        "Language": "eo"
    }
}
```

## Add a custom font

You can provide your own Bitmap font for your custom language, which
maps arbitrary Unicode characters to sprites in your font texture. You
can
<a href="Modding_Editing_XNB_files#Unpack_game_files" class="wikilink"
title="unpack your game&#39;s Content folder">unpack your game's
<samp>Content</samp> folder</a> and look at the Chinese, Japanese,
Korean, and Russian fonts in the `Fonts` folder for examples of how this
looks in practice.

### Data format

To enable a custom font, add these three extra fields to
<a href="#Add_a_custom_language" class="wikilink"
title="your Data/AdditionalLanguages entry">your
<samp>Data/AdditionalLanguages</samp> entry</a>:

| field | description |
|----|----|
| `UseLatinFont` | Whether the language uses the game's default fonts. **Set to `false`** to enable a custom font. |
| `FontFile` | The asset name for your `.fnt` font data file (see <a href="#Font_files" class="wikilink" title="font files"><em>font
files</em></a> below). This must be the asset's name in the game's `Content` folder, not the file path in your content pack; see <a href="#Example_2" class="wikilink" title="the example below">the
example below</a>. |
| `FontPixelZoom` | A factor by which to multiply the font size. The recommended baseline is 1.5, but you can adjust it to make your text smaller or bigger in-game. |

### Font files

Note: if your language has a TrueType font available, you can use the
[Bitmap font generator](https://www.angelcode.com/products/bmfont/) to
generate these files from it.

Font data
Each font must have a text (XML) file with the `.fnt` extension which
describes the font.

<!-- -->


For example, here's the `Content/Fonts/Japanese.fnt` file (with most of
the characters stripped out for brevity):

:

``` xml
<?xml version="1.0"?>
<font>
  <info face="SetoFont-SP" size="24" bold="0" italic="0" charset="" unicode="1" stretchH="100" smooth="1" aa="1" padding="0,0,0,0" spacing="1,1" outline="0"/>
  <common lineHeight="24" base="21" scaleW="1024" scaleH="1024" pages="2" packed="0" alphaChnl="0" redChnl="4" greenChnl="4" blueChnl="4"/>
  <pages>
    <page id="0" file="Japanese_0" />
    <page id="1" file="Japanese_1" />
  </pages>
  <chars count="2514">
    ...
    <char id="37347" x="100" y="265" width="24" height="22" xoffset="0" yoffset="1" xadvance="24" page="0" chnl="15" />
    ...
  </chars>
</font>
```


See the [official format
documentation](https://www.angelcode.com/products/bmfont/doc/file_format.html)
to understand all the options, but at a high level:

<!-- -->


{\| class="wikitable"

\|- ! field ! description \|- \| `info` \| Describes the font itself:
the name, TrueType size, padding and spacing, etc. \|- \| `common` \|
Provides common info which applies to all of the characters, like the
line height. \|- \| `pages` \| Lists the sprite textures that are part
of the font. In the above example, the Japanese character sprites are
split into two images: `Japanese_0.png` and `Japanese_1.png`. Each
character in `chars` specifies which page it's on. \|- \| `chars` \|
Maps each Unicode character you'll use in-game to the sprite font. The
example above defines one character with these `char` fields:


{\| class="wikitable"

\|- ! char attribute ! explanation \|- \| `id` \| The decimal Unicode ID
for the character (*e.g.,* 37347 in the example above is 釣). You can
search characters in
[Unicodepedia](https://www.unicodepedia.com/unicode/cjk-unified-ideographs/91e3/cjk-unified-ideograph-91e3/)
to find their Unicode IDs. \|- \| `x`\
`y`\
`width`\
`height` \| The top-left position and size of the character sprite in
the page image, measured in pixels. \|- \| `xoffset`\
`yoffset` \| A pixel offset to apply to the character when it's drawn to
the screen. \|- \| `xadvance` \| When drawing multiple characters to the
screen, how many pixels drawing this character should advance the
cursor. \|- \| `page` \| The ID of the page image which contains the
sprite, as defined in the `pages` field. \|- \| `chnl` \| The color
channel for which the sprite has data. (This is always `15` for all
channels in Stardew Valley's current fonts.) \|} \|}

Font images
Each font also needs one or more images which contain the character
sprites (white on a transparent background). The file names and sprite
positions are defined in the above font data file.

<!-- -->


For example, here's the `Content/Fonts/Japanese_0` file (with a black
background so the sprites are visible):

<div style="display: inline-block; background:#000;">

<a href="File_Modding_-_example_font_texture.png" class="wikilink"
title="300px">300px</a>

</div>

### Example

If you're using <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a>, your content pack should
look something like this with the files described above:

    📁 Your Mod Name/
      🗎 content.json
      🗎 manifest.json
      📁 assets/
        🗎 YourLanguage.fnt
        🗎 YourLanguage_0.png

Now you just need to make them available through the game's
`Content/Fonts` folder. Make sure the target for the `.fnt` file matches
what you specified via `FontFile` in the
<a href="#Add_a_custom_language" class="wikilink"
title="language data">language data</a>, and the target for the image
matches what you specified via `pages` in the
<a href="#Font_files" class="wikilink" title="font data">font data</a>.

For example, here's the previous Esperanto example with a custom font
(note the `UseLatinFont` and `FontFile` fields in the language data, and
the two new patches at the bottom):

## Limitations

Custom languages must be available very early in the game startup, and
won't be handled correctly if they're added later. That means:

- For Content Patcher packs, they must be added without `When`
  conditions (or only using immutable conditions like config or
  `HasMod`).
- For C# mods, they should be added in
  <a href="Modding_Modder_Guide_APIs_Events#Game_loop" class="wikilink"
  title="GameLaunched"><samp>GameLaunched</samp></a> or earlier.

## See also

- <a href="Modding_Translations" class="wikilink"
  title="Modding:Translations">Modding:Translations</a>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Пользовательские_языки" class="wikilink"
title="ru:Модификации:Пользовательские языки">ru:Модификации:Пользовательские
языки</a> <a href="zh_模组_自定义语言" class="wikilink"
title="zh:模组:自定义语言">zh:模组:自定义语言</a>
