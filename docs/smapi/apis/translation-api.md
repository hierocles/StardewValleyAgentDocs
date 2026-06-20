---
title: "Translation Api"
wiki_source: "Modding:Modder Guide/APIs/Translation"
permalink: /Modding:Modder_Guide/APIs/Translation/
category: smapi
tags: [translation, overview, i18n-folder, file-structure, file-format, tips-for-translators, reading-translations, built-in-api]
---
<div style="float: right; border: 2px solid rgb(0, 116, 72); background: #A1DEE2; padding: 0.75em; padding-top: 0.5em; margin: 0 0 2em 2em;">

<span style="font-size: larger;">**Creating SMAPI mods**
<a href="File_SMAPI_mascot.png" class="wikilink" title="25px">25px</a></span>

------------------------------------------------------------------------

- <a href="Modding_Modder_Guide_Get_Started" class="wikilink"
  title="Get started">Get started</a>
- <a href="Modding_Modder_Guide_Game_Fundamentals" class="wikilink"
  title="Game fundamentals">Game fundamentals</a>
- <a href="Modding_Modder_Guide_Test_and_Troubleshoot" class="wikilink"
  title="Test &amp; troubleshoot">Test &amp; troubleshoot</a>
- <a href="Modding_Modder_Guide_Release" class="wikilink"
  title="Release">Release</a>
- <a href="Modding_Modder_Guide_APIs" class="wikilink"
  title="API reference">API reference</a>

  Basic SMAPI APIs:

  - <a href="Modding_Modder_Guide_APIs_Mod_structure" class="wikilink"
    title="Mod structure">Mod structure</a>
  - <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
    title="Manifest">Manifest</a>
  - <a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
    title="Events">Events</a>
  - <a href="Modding_Modder_Guide_APIs_Config" class="wikilink"
    title="Configuration">Configuration</a>
  - <a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
    title="Load &amp; edit content">Load &amp; edit content</a>
  - <a href="Modding_Modder_Guide_APIs_Data" class="wikilink"
    title="Data">Data</a>
  - <a href="Modding_Modder_Guide_APIs_Input" class="wikilink"
    title="Input">Input</a>
  - <a href="Modding_Modder_Guide_APIs_Logging" class="wikilink"
    title="Logging">Logging</a>
  - <a href="Modding_Modder_Guide_APIs_Reflection" class="wikilink"
    title="Reflection">Reflection</a>
  - <a href="Modding_Modder_Guide_APIs_Multiplayer" class="wikilink"
    title="Multiplayer">Multiplayer</a>
  - <a href="Modding_Modder_Guide_APIs_Translation" class="wikilink"
    title="Translation">Translation</a>
  - <a href="Modding_Modder_Guide_APIs_Update_checks" class="wikilink"
    title="Update checks">Update checks</a>
  - <a href="Modding_Modder_Guide_APIs_Utilities" class="wikilink"
    title="Utilities">Utilities</a>

  Advanced SMAPI APIs:

  - <a href="Modding_Modder_Guide_APIs_Content_Packs" class="wikilink"
    title="Content packs">Content packs</a>
  - <a href="Modding_Modder_Guide_APIs_Console" class="wikilink"
    title="Mod console commands">Mod console commands</a>
  - <a href="Modding_Modder_Guide_APIs_Integrations" class="wikilink"
    title="Mod integrations">Mod integrations</a>
  - <a href="Modding_Modder_Guide_APIs_Harmony" class="wikilink"
    title="Harmony patching">Harmony patching</a>
- <a href="Modding_Index#Advanced_topics" class="wikilink"
  title="Specific guides">Specific guides</a>

</div>

←
<span style="font-size: smaller;"><a href="Modding_Index" class="wikilink"
title="Modding:Index">Modding:Index</a></span>
<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

The translation API lets you translate your mod, and include all
languages in one release package for SMAPI to use automatically based on
the game language.

## Overview

SMAPI reads translations from files in your mod folder. When you request
a translation, it will automatically handle locale fallback (*e.g.,* if
a translation isn't available in `pt-BR.json`, SMAPI will check
`pt.json` and `default.json`). Translations can be a simple string, or
they can include tokens to inject values into the translation.

## i18n folder

### File structure

SMAPI reads translations from JSON files in an `i18n` subfolder in your
mod folder:

    YourMod/
       i18n/
          default.json
          es.json
          fr.json
       manifest.json
       YourMod.dll

The `default.json` file has the default text shown if a more specific
translation isn't available, and you create a separate file for each
language. Each translation file should have one of these file names:

| Language   | File name |
|------------|-----------|
| Chinese    | `zh.json` |
| French     | `fr.json` |
| German     | `de.json` |
| Hungarian  | `hu.json` |
| Italian    | `it.json` |
| Japanese   | `ja.json` |
| Korean     | `ko.json` |
| Portuguese | `pt.json` |
| Russian    | `ru.json` |
| Spanish    | `es.json` |
| Turkish    | `tr.json` |

For large mods, you can optionally have a folder for each language
containing any number of `.json` files. This isn't recommended for most
mods though, since it's harder to keep in sync between languages and is
less supported by translation tools. For example:

    YourMod/
       i18n/
          default/
             dialogue.json
             events.json
          fr/
             dialogue.json
             events.json
       manifest.json
       YourMod.dll

You can't have both top-level files (like `fr.json`) and folders (like
`fr/dialogue.json`), so you'll need to use one pattern consistently.

For a <a href="Modding_Custom_languages" class="wikilink"
title="custom language">custom language</a>, use its `LanguageCode`
value in the filename.

### File format

Each `.json` file should contain a flat key→value lookup with your
default text. Each key is case-insensitive, and can contain
alphanumeric, underscore, hyphen, and dot characters. Feel free to add
JavaScript comments to organise or document your translations. For
example:

``` javascript
{
    // example translations
    "item-type.label": "Item type",
    "item-type.fruit-tree": " tree",
}
```

The in the above example is a token. You can add any tokens you want
(each having only letters in the name), and replace them with a
different value in code (see
<a href="#Reading_translations" class="wikilink"
title="reading translations"><em>reading translations</em></a> below).

### Tips for translators

- Save i18n files with UTF-8 encoding to avoid broken symbols in-game.
- Type `reload_i18n` into the SMAPI console and hit enter to reload
  translations without exiting the game. (If a mod internally cached a
  translation, it may not be updated.)

## Reading translations

### Built-in API

Once your i18n files are set up, you can read translations for the
current locale:

``` c#
// read a simple translation
string label = helper.Translation.Get("item-type.label");

// read a translation which uses tokens (accepts an anonymous object, dictionary, or model)
string text = helper.Translation.Get("item-type.fruit-tree", new { fruitName = "apple" });
```

The `helper.Translate(…)` method returns a fluent interface — you can
keep calling methods on its return value to customise the translation.
(See IntelliSense for a description of the available methods.) To get
the text, just assign it to a string:

``` c#
// use fluent chain
string text = helper.Translation.Get(key).Tokens(tokens).Tokens(moreTokens).Default("missing translation?");
```

All translations can use
<a href="Modding_Dialogue#Gender_switch" class="wikilink"
title="gender switch blocks">gender switch blocks</a>. They'll be
formatted based on the player's gender each time you fetch the
translation.

### Strongly-typed API

The built-in API doesn't have build-time validation. For example, if you
set a `fruitName` argument but the translation actually uses , you won't
know until you test each translation in-game and see the broken message.
That's fine for most mods, but can be an issue with larger mods that
have hundreds of translations across many different UI flows.

The optional [SMAPI mod translation class
builder](https://github.com/Pathoschild/SMAPI-ModTranslationClassBuilder#readme)
package lets you generate a strongly-typed class to read translations
like this instead:

``` c#
string label = I18n.ItemType_Label();
string text = I18n.ItemType_FruitTree(fruitName: "apple");
```

If a translation breaks, you'll know immediately since it won't compile.

## See also

[LINQ
script](https://gist.github.com/Pathoschild/4e0af42158583983a4206d4d734bfc0b)
to format an event for translations

<a href="ru_Модификации_Руководство_мододела_API_Перевод"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Перевод">ru:Модификации:Руководство
мододела/API/Перевод</a>
<a href="tr_Modlama_Mod_Rehberi_API&#39;ler_Çeviri" class="wikilink"
title="tr:Modlama:Mod Rehberi/API&#39;ler/Çeviri">tr:Modlama:Mod
Rehberi/API'ler/Çeviri</a>
<a href="zh_模组_制作指南_APIs_Translation" class="wikilink"
title="zh:模组:制作指南/APIs/Translation">zh:模组:制作指南/APIs/Translation</a>
