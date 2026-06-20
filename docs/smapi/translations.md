---
title: "Translations"
wiki_source: "Modding:Translations"
permalink: /Modding:Translations/
category: smapi
tags: [translations, for-translators, how-translations-work, how-to-translate-a-mod, how-to-provide-mod-translations, for-modders, using-translations, translation-summary]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

SMAPI mods can be translated into any language the game supports.
They'll automatically use the same language as the game, and will
fallback to the default text if a translation is missing. This page
explains how to provide or request translations.

## For translators

### How translations work

Each mod has an `i18n` folder containing the translation files (if it
supports translation), which you can open in a normal text editor like
Notepad. The folder always has a `default.json` (which has the default
English text), plus any of these files:

| Language   | File name                                             |
|------------|-------------------------------------------------------|
| German     | `de.json`                                             |
| Spanish    | `es.json`                                             |
| French     | `fr.json`                                             |
| Italian    | `it.json`                                             |
| Japanese   | `ja.json`                                             |
| Korean     | `ko.json`                                             |
| Hungarian  | `hu.json`                                             |
| Portuguese | `pt.json`                                             |
| Russian    | `ru.json`                                             |
| Turkish    | `tr.json`                                             |
| Chinese    | `zh.json`                                             |
| *Custom*   | file name matches the language's `LanguageCode` field |

Each file contains text that looks like this:

``` javascript
{
   "translation-key": "simple translatable text",
   "translation-key-2": "translatable text with a  value"
}
```

The first part (before `:`) is the unique key for the translation. This
is how the mod identifies the translation, so you shouldn't change it.

The second part (after `:`) is the translation text, which you can
change. Sometimes this will contain a token, which looks like ; this
will be replaced with different text when the mod runs, so you shouldn't
change the text between . For example, if the text says
`"You have gold"`, the player would actually see something like
`You have 500 gold` in-game.

### How to translate a mod

1.  Install the mod normally.
2.  Open the file you want to edit in its `i18n` folder. (If the file
    doesn't exist for your language yet, just copy `default.json` and
    rename it.)
3.  Edit the translations as needed (see
    *<a href="#How_translations_work" class="wikilink"
    title="how translations work">how translations work</a>* above).
4.  Launch the game and choose your language. The mod should show the
    translation text you entered.
5.  Send the edited file to the mod author, so they can add it to the
    official release.

**Tips:**

- If you see broken symbols in-game, try saving the translation file
  with UTF-8 encoding.
- You can test translation changes in-game without restarting the game.
  Enter `reload_i18n` into the SMAPI console to reload translations. (If
  a mod internally cached a translation, it may not be updated.)
- There's an
  [Internationalization](https://www.nexusmods.com/stardewvalley/mods/21317)
  mod in development that aims to simplify the translation process. In
  particular updating existing translations. It replaces steps 2-4
  above. If you install that and run the game, you can open a page in
  your web browser to update translations of your installed mods live.
  It takes care of the json & utf-8 encoding so you don't have to. It's
  very new, so it might still have bugs.

### How to provide mod translations

You can provide translations anytime. There's no commitment needed —
your help is appreciated whether you only help once or keep coming back!

Here's the standard process:

1.  [Create an account on GitHub](https://github.com/).
2.  [View the open translation
    requests](https://github.com/StardewModders/mod-translations/issues).
    To only see requests for your language, click the 'Labels' dropdown
    and choose the `needs:` label for it.
3.  Click a request to see the details (including what the mod does,
    where to download it, and what translations are needed).
4.  Install the mod and edit the translations on your computer (see the
    previous section).
5.  Copy your translation text, and paste it into a comment on the
    GitHub request. <small>(If you're comfortable with GitHub, feel free
    to submit a pull request to the author instead.)</small>

That's it! The mod author will add your translations to the mod, so
it'll be available in your language in the next release.

**Tips:**

- If a mod has a *lot* of translations, feel free to only translate some
  of them. Someone else can finish the translations if needed.

## For modders

### Using translations

For help using translations, see
<a href="Modding_Modder_Guide_APIs_Translation" class="wikilink"
title="Modding:Modder Guide/APIs/Translation">Modding:Modder
Guide/APIs/Translation</a>.

### Translation summary

If your mod is <a href="Modding_Open_source" class="wikilink"
title="open-source">open-source</a>, you can add a translation summary
to your repository's `README.md` file ([see an
example](https://github.com/Pathoschild/StardewMods/#translating-the-mods)).
This makes it much more likely that translators will contribute
translations for your mod since it...

- indicates that contributions are welcome;
- explains how to provide translations;
- and provides a summary of each mod's translation status and links.

You can [auto-generate the translation summary using a
script](https://gist.github.com/Pathoschild/040ff6c8dc863ed2a7a828aa04447033).

### Request translations

1.  Before you start:
    1.  Your mod **must** be
        <a href="Modding_Open_source" class="wikilink"
        title="open-source">open-source</a> on a public site like
        [GitHub](https://github.com/).\
        *This is important for the modders curating the request list,
        since it lets them (a) check the current status of your mod
        translations to keep requests up-to-date, (b) answer questions
        from translators if needed, and (c) submit a pull request with
        any translations received when the ticket is closed if you stop
        responding.*
    2.  If you have partial translations, copy any missing translations
        into all translation files and mark them with `// TODO`. (That
        way translators only need to look at their language's file, they
        don't need to compare it with `default.json`.)
    3.  Make sure you watch the request and you have time to reply to
        questions! Your request will be closed if you don't respond to a
        question on the ticket within 72 hours.
    4.  The `default.json` must be complete and in English. If your main
        language isn't English and you need help preparing it, we can
        help! Just create a request the same way below, but choose
        `needs: English copyediting` as the label instead.
2.  [Create a request
    ticket](https://github.com/StardewModders/mod-translations/issues)
    with this info:
    <table>
    <thead>
    <tr>
    <th><p>field</p></th>
    <th><p>what to enter</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>title</p></td>
    <td><p>The mod name and version to translate.</p></td>
    </tr>
    <tr>
    <td><p>labels</p></td>
    <td><p>Choose the 'needs:' labels for the translations you need. (Don't
    add 'done:' labels, that's only for completed requests.)</p></td>
    </tr>
    <tr>
    <td><p>Description</p></td>
    <td><p>Provide the following information:</p>
    <ul>
    <li>A brief summary of what your mod does, including a link to the mod
    page.</li>
    <li>A link to the open-source code.</li>
    <li>A download link if you're requesting translations for an unreleased
    version. (You can attach it directly to the request ticket.)</li>
    <li>If needed, an explanation of where the text appears, screenshots,
    etc.</li>
    </ul>
    <p>Here's <a
    href="https://github.com/StardewModders/mod-translations/issues/1">an
    example request</a> which provides that info.</p></td>
    </tr>
    </tbody>
    </table>
3.  Watch your notifications so you know when someone contributes
    translations or answers a question!

## See also

- <a href="Modding_Custom_languages" class="wikilink"
  title="Modding:Custom languages">Modding:Custom languages</a>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Traducciones" class="wikilink"
title="es:Modding:Traducciones">es:Modding:Traducciones</a>
<a href="pt_Modificações_Traduções" class="wikilink"
title="pt:Modificações:Traduções">pt:Modificações:Traduções</a>
<a href="ru_Модификации_Перевод" class="wikilink"
title="ru:Модификации:Перевод">ru:Модификации:Перевод</a>
<a href="tr_Modlama_Çeviriler" class="wikilink"
title="tr:Modlama:Çeviriler">tr:Modlama:Çeviriler</a>
<a href="zh_模组_翻译模组" class="wikilink"
title="zh:模组:翻译模组">zh:模组:翻译模组</a>
