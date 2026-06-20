---
title: "Gift Tastes"
wiki_source: "Modding:Gift taste data"
permalink: /Modding:Gift_taste_data/
category: npcs
tags: [gift-taste-data, data, raw-data, format, multilining, how-a-gift-taste-is-determined]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game calculates NPC gift tastes. This is an
advanced guide for mod developers.

## Data

### Raw data

NPC gift tastes are stored in `Content\Data\NPCGiftTastes.xnb`, which
can be <a href="Modding_Editing_XNB_files#unpacking" class="wikilink"
title="unpacked to edit">unpacked to edit</a>. Here's the raw data as of
for reference:

### Format

The file contains two types of data:

- *Universal tastes* apply to all villagers. Their key is
  `Universal_<Taste>` (Love, Like, Neutral, Dislike, or Hate), and their
  value is a space-delimited array of reference IDs (object unqualified
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="item ID">item ID</a> if ≥0,
  <a href="Modding_Items#Categories" class="wikilink"
  title="category ID">category ID</a> if \<0, or
  <a href="Modding_Context_tags" class="wikilink"
  title="context tag">context tag</a>). For example, consider this
  entry:
  ``` json
    "Universal_Dislike": "-4 -8 -12 -15 -16 -19 -22 -24 -25 -28 -74 78 169 246 247 305 309 310 311 403 419 423 535 536 537 725 726 749 271 Book_PriceCatalogue category_trinket",
  ```

  This data means villagers should have a universal dislike for category
  -4,
  <a href="Modding_Objects" class="wikilink" title="object 78">object
  78</a>, anything with the context tag
  <a href="Modding_Context_tags#Added_automatically" class="wikilink"
  title="category_trinket">category_trinket</a> etc.
- *Personal tastes* apply to a specific villager. Their key is the
  villager's internal name (like `Abigail`), and their value alternates
  dialogue text with a list of reference IDs in this order: love, like,
  dislike, hate, and neutral. For example, consider Abigail's gift
  tastes:
  ``` json
    "Abigail": "I seriously love this! You're the best, @!/66 128 220 226 276 611 904 Book_Void/Hey, how'd you know I was hungry? This looks delicious!/119 109 SkillBook_4 BasiliskPaw/What am I supposed to do with this?/-5 -75 -79 16 245 246/What were you thinking? This is awful!/330/You brought me a present? Thanks.//"
  ```

  By splitting the string with `/` as the delimiter, we can extract this
  data:

  | field index | taste | reaction dialogue | reference IDs |
  |----|----|----|----|
  | 0, 1 | love | I seriously love this! You're the best, @! | 66 128 220 226 276 611 904 Book_Void |
  | 2, 3 | like | Hey, how'd you know I was hungry? This looks delicious! | 119 109 SkillBook_4 BasiliskPaw |
  | 4, 5 | dislike | What am I supposed to do with this? | -5 -75 -79 16 245 246 |
  | 6, 7 | hate | What were you thinking? This is awful! | 330 |
  | 8, 9 | neutral | You brought me a present? Thanks. | *none* |

  This data means she should personally love item 66 (Amethyst), dislike
  category -5 (eggs), etc. Even though she has no items in her neutral
  list, she will still have items that she's neutral to if they're in
  the `Universal_Neutral` list. See below for an explanation of how gift
  tastes are determined overall.

### Multilining

NPC Gift tastes can be multilined for readability. Line breaks must be
before or after the `/` delimiter. For example:

``` json
  "Abigail": "
I seriously love this! You're the best, @!/66 128 220 226 276 611 904 Book_Void/
Hey, how'd you know I was hungry? This looks delicious!/119 109 SkillBook_4 BasiliskPaw/
What am I supposed to do with this?/-5 -75 -79 16 245 246/
What were you thinking? This is awful!/330/
You brought me a present? Thanks.//
"
```

## How a gift taste is determined

The data format allows tastes to conflict in multiple ways:

- between an
  <a href="Modding_Common_data_field_types#Item_ID" class="wikilink"
  title="item ID">item ID</a> and category ID;
- between a universal taste and personal taste;
- between conflicting values (*e.g.,* Jodi both loves and hates
  Daffodils (item ID 18) specifically);
- and any combination of the above (*e.g.,* between a universal item ID
  and personal category ID).

(TODO: Add information about where context tags fit within the
algorithm.)

The game uses a rather complicated algorithm to determine how much an
NPC likes an gift (see `NPC::getGiftTasteForThisItem`). Here's a cleaned
up version of the algorithm in pseudocode:

    var TASTE = neutral
    bool HAS_UNIVERSAL_ID = false
    bool HAS_UNIVERSAL_NEUTRAL_ID = false

    // part I: universal taste by category
    if category is universally loved:
       TASTE = love
    else if category is universally hated:
       TASTE = hate
    else if category is universally liked:
       TASTE = like
    else if category is universally disliked:
       TASTE = dislike

    // part II: universal taste by item ID
    if itemID is universally loved:
       TASTE = love
       HAS_UNIVERSAL_ID = true
    else if itemID is universally hated:
       TASTE = hate
       HAS_UNIVERSAL_ID = true
    else if itemID is universally liked:
       TASTE = like
       HAS_UNIVERSAL_ID = true
    else if itemID is universally disliked:
       TASTE = dislike
       HAS_UNIVERSAL_ID = true
    else if itemID is universally neutral:
       TASTE = neutral
       HAS_UNIVERSAL_ID = true
       HAS_UNIVERSAL_NEUTRAL_ID = true

    // part III: override neutral if it's from universal category
    if TASTE is neutral and not HAS_UNIVERSAL_NEUTRAL_ID:
       if item is edible but tastes bad (-300 > edibility < 0):
          TASTE = hate
       else if item has a price < 20g:
          TASTE = dislike

    // part IV: sometimes override with personal tastes
    if ((npc loves itemID OR (item has a category AND npc loves category)) AND (item has no category OR npc doesn't personally love category OR no universal taste for itemID)
       return love
    if ((npc hates itemID OR (item has a category AND npc hates category)) AND (item has no category OR npc doesn't personally hate category OR no universal taste for itemID)
       return hate
    if ((npc like itemID OR (item has a category AND npc likes category)) AND (item has no category OR npc doesn't personally like category OR no universal taste for itemID)
       return like
    if ((npc dislikes itemID OR (item has a category AND npc dislikes category)) AND (item has no category OR npc doesn't personally dislike category OR no universal taste for itemID)
       return dislike
    if ((npc neutrals itemID OR (item has a category AND npc neutrals category)) AND (item has no category OR npc doesn't personally neutral category OR no universal taste for itemID)
       return neutral

    // part V: return taste if not overridden
    return TASTE

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Datos_de_gustos_por_regalos" class="wikilink"
title="es:Modding:Datos de gustos por regalos">es:Modding:Datos de
gustos por regalos</a>
<a href="pt_Modificações_Dados_dos_gostos_do_presente" class="wikilink"
title="pt:Modificações:Dados dos gostos do presente">pt:Modificações:Dados
dos gostos do presente</a>
<a href="ru_Модификации_Подарки" class="wikilink"
title="ru:Модификации:Подарки">ru:Модификации:Подарки</a>
<a href="zh_模组_礼物喜好数据" class="wikilink"
title="zh:模组:礼物喜好数据">zh:模组:礼物喜好数据</a>
