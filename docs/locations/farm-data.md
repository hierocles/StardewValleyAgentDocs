---
title: "Farm Data"
wiki_source: "Modding:Farm data"
permalink: /Modding:Farm_data/
category: locations
tags: [farm-data, assets, farm-type-data, farm-map, farm-map-properties, location-data, example]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the game stores and parses
<a href="Farm_Maps" class="wikilink" title="farm types">farm types</a>,
maps, and related data. This is an advanced guide for mod developers.

**Before reading this page**, see
<a href="Modding_Editing_XNB_files" class="wikilink"
title="Modding:Editing XNB files">Modding:Editing XNB files</a> for the
basic concepts.

## Assets

### Farm type data

You can define custom farm types by editing the `Data/AdditionalFarms`
asset.

This consists of a list of models, where each model has the fields
listed below.

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
class="wikilink" title="unique string ID">unique string ID</a> for the
farm type.</p></td>
</tr>
<tr>
<td><p><samp>TooltipStringPath</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Translation_key"
class="wikilink" title="translation key">translation key</a> containing
the translatable farm name and description. For example,
<samp>Strings/UI:Farm_Description</samp> will get it from the
<samp>Farm_Description</samp> entry in the <samp>Strings/UI</samp>
file.</p>
<p>The translated text must be in the form
"<samp>&lt;name&gt;_&lt;description&gt;</samp>", like "Pineapple Farm_A
farm shaped like a pineapple".</p></td>
</tr>
<tr>
<td><p><samp>MapName</samp></p></td>
<td><p>The <a href="Modding_Common_data_field_types#Asset_name"
class="wikilink" title="asset name">asset name</a> for the farm's <a
href="Modding_Maps" class="wikilink" title="map asset">map asset</a>,
relative to the <samp>Maps</samp> folder. For example,
<samp>Farm_Pineapple</samp> would load
<samp>Maps/Farm_Pineapple</samp>.</p></td>
</tr>
<tr>
<td><p><samp>IconTexture</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Asset_name" class="wikilink"
title="asset name">asset name</a> for a 22x20 pixel icon texture, shown
on the 'New Game' and co-op join screens.</p></td>
</tr>
<tr>
<td><p><samp>SpawnMonstersByDefault</samp></p></td>
<td><p><em>(Optional)</em> The default value of the 'spawn monsters at
night' <a href="Options#Advanced_Game_Options" class="wikilink"
title="advanced save option">advanced save option</a>.</p></td>
</tr>
<tr>
<td><p><samp>WorldMapTexture</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Asset_name" class="wikilink"
title="asset name">asset name</a> for a 131x61 pixel texture that's
drawn over the farm area in the in-game world map.</p></td>
</tr>
<tr>
<td><p><samp>ModData</samp></p></td>
<td><p><em>(Optional)</em> The <a
href="Modding_Common_data_field_types#Mod_data" class="wikilink"
title="mod data fields">mod data fields</a> for this farm type, which
can be accessed in C# code via
<samp>Game1.GetFarmTypeModData(key)</samp>.</p></td>
</tr>
</tbody>
</table>

### Farm map

The farm <a href="Modding_Maps" class="wikilink" title="map">map</a>
contains the general appearance and layout of your farm.
<a href="Modding_Maps" class="wikilink"
title="Modding:Maps">Modding:Maps</a> describes the basic process of
creating a map.

Copying and editing an existing farm map is recommended to avoid
problems with missing information. The map must be added to the game
files, and not replace an existing one.

### Farm map properties

You can customize the farm behavior by
<a href="Modding_Maps" class="wikilink"
title="setting map properties in the map asset">setting map properties
in the map asset</a>.

When testing map property changes, it's best to create a new save since
some of these are only applied when the save is created. These
properties are optional, and the game will use default values for any
properties that aren't specified.

Some notable map properties are:

- <a href="Modding_Maps#Warps_&amp;_map_positions" class="wikilink"
  title="Warp &amp; map positions">Warp &amp; map positions</a> set the
  player position when arriving on the farm (e.g. `BackwoodsEntry` when
  arriving from the
  <a href="backwoods" class="wikilink" title="backwoods">backwoods</a>,
  or `WarpTotemEntry` when using a
  <a href="Warp_Totem_Farm" class="wikilink" title="warp totem">warp
  totem</a> or
  <a href="Farm_Obelisk" class="wikilink" title="farm obelisk">farm
  obelisk</a>), and the default positions of some location contents
  (e.g. `MailboxLocation` for the default mailbox position).
- <a href="Modding_Maps#Farmhouse_interior" class="wikilink"
  title="Farmhouse interior properties">Farmhouse interior properties</a>
  set the appearance and contents of the
  <a href="farmhouse" class="wikilink" title="farmhouse">farmhouse</a>
  (e.g. `FarmHouseFlooring` for the default flooring, or
  `FarmHouseStarterGift` for what's in the starter giftbox).
- <a href="Modding_Maps#Fishing" class="wikilink"
  title="Fishing properties">Fishing properties</a> override fishing and
  crab pot behavior.
- <a href="Modding_Maps#Plants,_forage,_&amp;_item_spawning"
  class="wikilink"
  title="Plants, forage, &amp; item spawning properties">Plants, forage,
  &amp; item spawning properties</a> override how crops, forage,
  artifact spots, etc work on the farm.

### Location data

**Optionally**, you can override additional farm location behavior by
<a href="Modding_Location_data" class="wikilink"
title="editing Data/Locations">editing <samp>Data/Locations</samp></a>.
Each farm type can have its own entry, with a key in the form
`Farm_<farm type ID>`. If omitted, it defaults to the location data for
the standard farm layout.

This can be used to override forage, fish, crab pot catches, artifact
spots, etc.

For custom farms, some fields should have specific values to preserve
expected behavior:

| field | description |
|----|----|
| `DisplayName` | A <a href="Modding_Common_data_field_types#Tokenizable_string"
class="wikilink" title="tokenizable string">tokenizable string</a> for the farm name. It should contain at least the `FarmName` token to be sure the farm name is shown. The standard value is `[LocalizedText Strings\\StringsFromCSFiles:MapPage.cs.11064 [EscapedText [FarmName]]]`. |
| `CreateOnLoad` | Must be `null` or omitted. Any other value will create duplicate locations. |
| `CanPlantHere` | Should be `true` or omitted. If `false`, crops can't be grown on your farm. |

## Example

For example, this <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher">Content Patcher</a> pack adds a farm type with
custom location data.

``` json
{
    "Changes": [
        // add farm type
        {
            "Action": "EditData",
            "Target": "Data/AdditionalFarms",
            "Entries": {
                "_PineappleFarm": { // for technical reasons, you need to specify the ID here *and* in the 'ID' field
                    "ID": "_PineappleFarm",
                    "TooltipStringPath": "Strings/UI:",
                    "MapName": "",
                    "IconTexture": "Mods//Icon",
                    "WorldMapTexture": "Mods//WorldMap"
                }
            }
        },

        // add farm name + description
        {
            "Action": "EditData",
            "Target": "Strings/UI",
            "Entries": {
                "": "Pineapple Farm_A farm shaped like a pineapple!" // tip: use  to translate it
            }
        },

        // load map
        {
            "Action": "Load",
            "Target": "Maps/",
            "FromFile": "assets/map.tmx"
        },

        // load icon
        {
            "Action": "Load",
            "Target": "Mods//Icon, Mods//WorldMap",
            "FromFile": "assets/.png"
        },

        // custom location data
        {
            "Action": "EditData",
            "Target": "Data/Locations",
            "Entries": {
                "Farm__PineappleFarm": {
                    "DisplayName": "[LocalizedText Strings\\StringsFromCSFiles:MapPage.cs.11064 [EscapedText [FarmName]]]",
                    "CanPlantHere": true,
                    "DefaultArrivalTile": {"X": 64, "Y": 15},
                    "MinDailyWeeds": 5,
                    "MaxDailyWeeds": 11,
                    "ArtifactSpots": [
                        // default artifact data
                        {
                            "Id": "Coal",
                            "ItemId": "(O)382",
                            "Chance": 0.5,
                            "MaxStack": 3
                        },
                        {
                            "Id": "MixedSeeds",
                            "ItemId": "(O)770",
                            "Chance": 0.1,
                            "MaxStack": 3
                        },
                        {
                            "Id": "Stone",
                            "ItemId": "(O)390",
                            "Chance": 0.25,
                            "MaxStack": 3
                        },
                        // custom artifacts
                        {
                            "Id": "SpringSeeds",
                            "ItemId": "(O)495",
                            "Chance": 0.2,
                            "MaxStack": 4,
                            "Condition": "SEASON Spring",
                            "Precedence": 1
                        },
                        {
                            "Id": "SummerSeeds",
                            "ItemId": "(O)496",
                            "Chance": 0.2,
                            "MaxStack": 4,
                            "Condition": "SEASON Summer",
                            "Precedence": 1
                        },
                        {
                            "Id": "FallSeeds",
                            "ItemId": "(O)497",
                            "Chance": 0.2,
                            "MaxStack": 4,
                            "Condition": "SEASON Fall",
                            "Precedence": 1
                        },
                        {
                            "Id": "WinterSeeds",
                            "ItemId": "(O)498",
                            "Chance": 0.2,
                            "MaxStack": 4,
                            "Condition": "SEASON Winter",
                            "Precedence": 1
                        }
                    ]
                }
            }
        }
    ]
}
```

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Ферма" class="wikilink"
title="ru:Модификации:Ферма">ru:Модификации:Ферма</a>
<a href="zh_模组_农场数据" class="wikilink"
title="zh:模组:农场数据">zh:模组:农场数据</a>
