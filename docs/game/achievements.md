---
title: "Achievements"
wiki_source: "Modding:Achievement data"
permalink: /Modding:Achievement_data/
category: game
tags: [achievement-data, raw-data, format, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses achievement data. This
is an advanced guide for mod developers.

## Raw data

Achievement data is stored in `Content\Data\Achievements.xnb`, which can
be <a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked for editing">unpacked for editing</a>. Here's the raw
data as of for reference:

## Format

| Index | Field | Example Value |
|----|----|----|
| 0 | name | *Moving Up* |
| 1 | description | *Upgrade your house.* |
| 2 | display achievement on collections tab before it's earned | *true* |
| 3 | prerequisite achievement | *-1* |
| 4 | hat earned (index from `hats.xnb`) | *13* |
|  |  |  |

If index 2 is "true" and index 3 is "-1" then the achievement star will
be displayed on the collections tab (greyed out if not yet achieved).
Otherwise, index 3 shows the number of the achievement that must be
earned before the achievement will be displayed on the Collections tab.
(Example: you must earn achievement 28 "Treasure Trove" before
achievement 5 "A Complete Collection" will be displayed.)

The only achievement with a value of "false" in index 2 is the secret
achievement that doesn't display until it's earned.

For a list of hats, see
<a href="Modding_Hats" class="wikilink" title="hat data">hat data</a>.

## See also

- <a href="Achievements" class="wikilink"
  title="Achievements">Achievements</a>

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Datos_de_logros" class="wikilink"
title="es:Modding:Datos de logros">es:Modding:Datos de logros</a>
<a href="ru_Модификации_Достижения" class="wikilink"
title="ru:Модификации:Достижения">ru:Модификации:Достижения</a>
<a href="tr_Modlama_Başarım_Verisi" class="wikilink"
title="tr:Modlama:Başarım Verisi">tr:Modlama:Başarım Verisi</a>
