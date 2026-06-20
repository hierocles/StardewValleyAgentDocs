---
title: "Content Api"
wiki_source: "Modding:Modder Guide/APIs/Content"
permalink: /Modding:Modder_Guide/APIs/Content/
category: smapi
tags: [content, intro, what-s-an-asset, what-s-an-asset-name, what-does-the-content-api-do, read-assets, read-mod-assets, get-actual-mod-asset-keys]
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

The content API lets you read custom assets, or read/edit/replace game
assets.

## Intro

### What's an 'asset'?

An *asset* is one image, map, or data structure provided to the game.
The game stores its default assets in its `Content` folder, though mods
can have custom assets too. For example, all of Abigail's portraits are
stored in one asset inside `Content\Portraits\Abigail.xnb`. If you
<a href="Modding_Editing_XNB_files" class="wikilink"
title="unpack that file">unpack that file</a>, you'll see it contains an
image file:

<a href="File_Modding_-_creating_an_XNB_mod_-_example_portraits.png"
class="wikilink"
title="File:Modding - creating an XNB mod - example portraits.png"><span>File:Modding</span>
- creating an XNB mod - example portraits.png</a>

See <a href="Modding_Editing_XNB_files" class="wikilink"
title="Editing XNB files">Editing XNB files</a> for more info about
asset files.

### What's an 'asset name'?

An *asset name* identifies an asset. For a game asset, this is the file
path relative to the game's `Content` folder *without* the `.xnb`
extension. For example:

| content file                    | asset name          |
|---------------------------------|---------------------|
| `Content\Portraits\Abigail.xnb` | `Portraits/Abigail` |
| `Content\Maps\Desert.ja-JA.xnb` | `Maps/Desert.ja-JA` |

Note that in <a href="Modding_Content_Patcher" class="wikilink"
title="Content Patcher packs">Content Patcher packs</a>, the asset name
*doesn't* include the language code. For example, the Content Patcher
asset name in the second row above is `Maps/Desert`.

### What does the content API do?

SMAPI handles content loading for the game. This lets you...

- read data, images, or maps from your mod folder (with support for
  `.json`, `.png`, `.tbin`, `.tmx`, and `.xnb` files);
- read assets from the game's `Content` folder;
- make changes to game assets (without changing the actual files);
- provide new assets to the game.

The rest of this page explains each one in more detail.

## Read assets

### Read mod assets

You can read custom assets from your mod folder by specifying its path
(relative to your mod folder) and type. For example:

``` c#
// read an image file
Texture2D texture = helper.ModContent.Load<Texture2D>("assets/texture.png");
// alternatively
IRawTextureData texture = helper.ModContent.Load<IRawTextureData>("assets/texture.png");

// read a map file
Map map = helper.ModContent.Load<Map>("assets/map.tmx");

// read a data file
IDictionary<string, string> data = helper.ModContent.Load<Dictionary<string, string>>("assets/data.json");
```

The supported file types are...

| file extension | in-game type | notes |
|----|----|----|
| `.xnb` | *any* | A packed file, like those in the game's `Content` folder. Not recommended since it's harder to edit and maintain. |
| `.json` | `''any''` | A data file, typically used to store `Dictionary<int, string>` or `Dictionary<string, string>` data. |
| `.png` | `[https://docs.monogame.net/api/Microsoft.Xna.Framework.Graphics.Texture2D.html Texture2D]` | An image file. You can use this to load textures, spritesheets, tilesheets, etc. |
| `.tbin` or `.tmx` | `xTile.Map` | A map file, which can be used to create or modify an in-game location. SMAPI will automatically match tilesheets to image files in the same folder as the map if they exist; otherwise the game will check the `Content` folders for them. |

Some usage notes:

- The normal convention is to have them in an `assets` subfolder, though
  that's not required.
- Don't worry about which path separators you use; SMAPI will normalize
  them automatically.
- To avoid performance issues, don't call `content.Load<T>` repeatedly
  in draw code. Instead, load your asset once and reuse it.

### Get actual mod asset keys

When you load an asset from your mod folder, SMAPI stores it with an
asset name that uniquely identifies it. If you need to pass the asset
name to game code, you can retrieve the actual asset name:

``` c#
tilesheet.ImageSource = helper.ModContent.GetActualAssetKey("assets/tilesheet.png");
```

### Read content assets

You can also read assets from the game folder:

``` c#
Texture2D portraits = helper.GameContent.Load<Texture2D>("Portraits/Abigail");
```

Note that this requires the
<a href="#What&#39;s_an_&#39;asset&#39;?" class="wikilink"
title="asset name">asset name</a>, *not* a filename.

## Replace a game asset

### Basics

You can replace an asset entirely by providing the asset through the
<a href="Modding_Modder_Guide_APIs_Events#Content.AssetRequested"
class="wikilink"
title="AssetRequested event"><samp>AssetRequested</samp> event</a> (see
<a href="Modding_Modder_Guide_APIs_Events#FAQs" class="wikilink"
title="how to use events">how to use events</a>). SMAPI will raise the
event every time an asset is loaded (which may happen multiple times per
asset), so you can replace the asset. If any mod provides the asset, the
original file won't be read at all and won't be changed.

There are two important concepts when replacing assets:

:; Load priority



Logically there's only one initial version of an asset. If multiple mods
want to load the same asset, SMAPI will use the load priority you
specify in the load methods to choose one (like
`AssetLoadPriority.Medium` in
`e.LoadFromModFile<Map>("assets/Farm.tmx", AssetLoadPriority.Medium)`).
If multiple mods have the same high priority, SMAPI will choose the one
that was registered first. You can use one of the preset levels like
`AssetLoadPriority.Medium`, or add arbitrary offsets like
`AssetLoadPriority.Medium + 1` (which is higher-priority than
`AssetLoadPriority.Medium` but lower than `AssetLoadPriority.High`.

<!-- -->



`AssetLoadPriority.Exclusive` is a special case. This declares that your
load operation is mandatory and shouldn't be skipped if another mod
loads it too. This is discouraged since it reduces mod compatibility. If
multiple mods specify `AssetLoadPriority.Exclusive`, SMAPI will log an
error and apply *none* of them.

:; Deferred loads



The load doesn't happen right away. When you call `e.LoadFrom` or
`e.LoadFromModFile`, you're telling SMAPI how to load the asset when
it's ready to do that. SMAPI will call every mod listening to the event
first, then use the information provided to check if the asset exists or
provide the asset (depending on which method the game called).

### Replace an image file

For example, here's a mod which replaces Abigail's portraits with a
custom version from its mod folder:

``` c#
internal sealed class ModEntry : Mod
{
    /// <inheritdoc/>
    public override void Entry(IModHelper helper)
    {
        helper.Events.Content.AssetRequested += this.OnAssetRequested;
    }

    /// <inheritdoc cref="IContentEvents.AssetRequested"/>
    /// <param name="sender">The event sender.</param>
    /// <param name="e">The event data.</param>
    private void OnAssetRequested(object sender, AssetRequestedEventArgs e)
    {
        if (e.Name.IsEquivalentTo("Portraits/Abigail"))
        {
            e.LoadFromModFile<Texture2D>("assets/abigail-portraits.png", AssetLoadPriority.Medium);
        }
    }
}
```

See IntelliSense on the `e` parameter for all the available options and
usage.

### Replace a map file

You can use the `AssetRequested` event to load custom maps too. When you
load a map file, and an unpacked tilesheet is present in the mod folder
(relative to the map file), SMAPI will automatically link the map to
that file and handle loading it too. If the tilesheet filename starts
with a season and underscore, the game will apply its normal seasonal
logic to it too.

For example, let's say you have a mod with this structure:

    📁 ExampleMod/
        🗎 ExampleMapMod.dll
        🗎 manifest.json
        📁 assets/
            🗎 Farm.tmx
            🗎 fall_customTilesheet.png
            🗎 spring_customTilesheet.png
            🗎 summer_customTilesheet.png
            🗎 winter_customTilesheet.png

You can load the custom map like this:

``` c#
internal sealed class ModEntry : Mod
{
    /// <inheritdoc/>
    public override void Entry(IModHelper helper)
    {
        helper.Events.Content.AssetRequested += this.OnAssetRequested;
    }

    /// <inheritdoc cref="IContentEvents.AssetRequested"/>
    /// <param name="sender">The event sender.</param>
    /// <param name="e">The event data.</param>
    private void OnAssetRequested(object sender, AssetRequestedEventArgs e)
    {
        if (e.Name.IsEquivalentTo("Maps/Farm"))
        {
            e.LoadFromModFile<Map>("assets/Farm.tmx", AssetLoadPriority.Medium);
        }
    }
}
```

That's it! SMAPI will detect a reference to
`spring_customTilesheet.png`, find the file relative to the map file,
and load it too. When the season changes in-game, SMAPI will
automatically switch it to `summer_customTilesheet.png`, etc. The other
tilesheet references will be left untouched (since there's no local
file), and use the game asset files.

### Add a new asset

Providing a new asset is exactly like replacing an existing one (see
previous sections). For example, this code adds a new dialogue file for
a custom NPC:

``` c#
internal sealed class ModEntry : Mod
{
    /// <inheritdoc/>
    public override void Entry(IModHelper helper)
    {
        helper.Events.Content.AssetRequested += this.OnAssetRequested;
    }

    /// <inheritdoc cref="IContentEvents.AssetRequested"/>
    /// <param name="sender">The event sender.</param>
    /// <param name="e">The event data.</param>
    private void OnAssetRequested(object sender, AssetRequestedEventArgs e)
    {
        if (e.Name.IsEquivalentTo("Characters/Dialogue/John"))
        {
            e.LoadFrom(
                () => {
                    return new Dictionary<string, string>
                    {
                        ["Introduction"] = "Hi there! My name is Jonathan."
                    };
                },
                AssetLoadPriority.Medium
            );
        }
    }
}
```

## Edit a game asset

### Basics

You can edit any game asset after it's loaded (but before it's provided
to the game), without changing the original files. You do this by adding
your edits in the
<a href="Modding_Modder_Guide_APIs_Events#Content.AssetRequested"
class="wikilink"
title="AssetRequested event"><samp>AssetRequested</samp> event</a> (see
<a href="Modding_Modder_Guide_APIs_Events#FAQs" class="wikilink"
title="how to use events">how to use events</a>). SMAPI will raise the
event every time an asset is loaded (which may happen multiple times per
asset), so you can edit the asset.

There are two important concepts when replacing assets:

:; Edit order



When mods apply multiple edits to the same asset, they're applied
sequentially in the order they were registered. You can optionally
provide an edit priority when you call the `e.Edit` method, to apply
your edit before or after other edits. You can use one of the preset
levels like `AssetEditPriority.Default`, or add arbitrary offsets like
`AssetEditPriority.Default + 1` (which is higher-priority than
`AssetEditPriority.Default` but lower than `AssetEditPriority.Late`).

:; Deferred edits



The edit doesn't happen right away. When you call `e.Edit`, you're
telling SMAPI how to apply your edit when it's ready to do that. SMAPI
will call every mod listening to the event first, then use all the
information provided to edit the asset when it's loaded.

### Example data edit

For example, here's a mod which doubles the sale price of all items:

``` c#
internal sealed class ModEntry : Mod
{
    /// <inheritdoc/>
    public override void Entry(IModHelper helper)
    {
        helper.Events.Content.AssetRequested += this.OnAssetRequested;
    }

    /// <inheritdoc cref="IContentEvents.AssetRequested"/>
    /// <param name="sender">The event sender.</param>
    /// <param name="e">The event data.</param>
    private void OnAssetRequested(object sender, AssetRequestedEventArgs e)
    {
        if (e.NameWithoutLocale.IsEquivalentTo("Data/Objects"))
        {
            e.Edit(asset =>
            {
                var data = asset.AsDictionary<string, ObjectData>().Data;

                foreach ((string itemID, ObjectData itemData) in data)
                {
                    itemData.Price *= 2;
                }
            });
        }
    }
}
```

The `IAssetData asset` argument from the `Edit` method has some helpers
to make editing data easier, documented below. (See IntelliSense for
more info.)

### Edit any file

These fields/methods are available directly on the `asset` from the
`Edit` method for any asset type, and also available through the helpers
listed below.

:; Data



A reference to the loaded asset data.

:; ReplaceWith



Replace the entire asset with a new version. You shouldn't do that in
most cases though; see *<a href="#Replace_a_game_asset" class="wikilink"
title="replace a game asset">replace a game asset</a>* instead, or use
one of the helpers below.

### Edit a dictionary

A *dictionary* is a key/value data structure, represented like this in
JSON exports:

``` json
{
   "key A": "value A",
   "key B": "value B",
   ...
}
```

You can get a dictionary helper using
`asset.AsDictionary<TKey, string>()`, where `TKey` is replaced with the
key type (usually `int` or `string`).

:; Data



A reference to the loaded data. For example, here's how to add or
replace a specific entry to the above example:

`   /// <inheritdoc cref="IContentEvents.AssetRequested"/>`\
`   /// <param name="sender">The event sender.</param>`\
`   /// <param name="e">The event data.</param>`\
`   private void OnAssetRequested(object sender, AssetRequestedEventArgs e)`\
`   {`\
`       if (e.NameWithoutLocale.IsEquivalentTo("Location/Of/The/Asset"))`\
`       {`\
`           e.Edit(asset =>`\
`           {`\
`                var editor = asset.AsDictionary<string, string>();`\
`                editor.Data["Key C"] = "Value C";`\
`           });`\
`       }`\
`   }`

</syntaxhighlight>

### Edit an image

When editing an image file, you can get a helper using
`asset.AsImage()`.

:; Data



A reference to the loaded image. You can directly edit each pixel in the
image through this field, though that's rarely needed.

:; PatchImage



Edit or replace part of the image. This is basically a copy & paste
operation, so the source texture is applied over the loaded texture. For
example:

`   /// <inheritdoc cref="IContentEvents.AssetRequested"/>`\
`   /// <param name="sender">The event sender.</param>`\
`   /// <param name="e">The event data.</param>`\
`   private void OnAssetRequested(object sender, AssetRequestedEventArgs e)`\
`   {`\
`       if (e.NameWithoutLocale.IsEquivalentTo("Location/Of/The/Asset"))`\
`       {`\
`           e.Edit(asset =>`\
`           {`\
`                 var editor = asset.AsImage();`\
`                 IRawTextureData sourceImage = this.Helper.ModContent.Load<IRawTextureData>("custom-texture.png");`\
`                 editor.PatchImage(sourceImage, targetArea: new Rectangle(300, 100, 200, 200));`\
`           });`\
`       }`\
`   }`

</syntaxhighlight>



Available method arguments:

{\| class="wikitable"

\|- ! argument ! usage \|- \| `source` \| The source image to copy &
paste onto the loaded image. May be a `Texture2D` or a `IRawTextureData`
\|- \| `sourceArea` \| *(optional)* The pixel area within the source
image to copy (or omit to use the entire source image). This must fit
within the target image. \|- \| `targetArea` \| *(optional)* The pixel
area within the loaded image to replace (or omit to replace starting
from the top-left corner up to the full source size). \|- \| `patchMode`
\| *(optional)* How the image should be patched. The possible values...

- `PatchMode.Replace` (default): erase the original content within the
  area before pasting in the new content;
- `PatchMode.Overlay`: draw the new content over the original content,
  so the original content shows through transparent or semi-transparent
  pixels.
- `PatchMode.Mask`: apply a transparency mask to the original content.
  This subtracts the alpha value of each pixel in the mask from the
  corresponding pixel in the target content (ignoring colors in mask).
  For example, a fully opaque pixel in the mask will result in a fully
  transparent pixel in the final image.

\|}

:; ExtendImage



Extend the image if needed to fit the given size. Note that **resizing
the image is an expensive operation**, creates a new texture instance,
and extending a spritesheet horizontally may cause game errors or bugs.
For example:

e.Edit(asset =\> {

`  var editor = asset.AsImage();`

`  // make sure the image is at least 1000px high`\
`  editor.ExtendImage(minWidth: editor.Data.Width, minHeight: 1000);`

});

</syntaxhighlight>



Available method arguments:

{\| class="wikitable"

\|- ! argument ! usage \|- \| `minWidth` \| The minimum desired width.
If the image width is less than this value, it'll be extended on the
right up to that size. \|- \| `minHeight` \| The minimum desired height.
If the image height is less than this value, it'll be extended from the
bottom up to that size. \|}

### Edit a map

When editing a map file, you can get a helper using `asset.AsMap()`.

:; Data



A reference to the loaded map. You can directly edit the map or tiles
through this field.

:; PatchMap



Edit or replace part of the map. This is basically a copy & paste
operation, so the source map is applied over the loaded map. For
example:

e.Edit(asset =\> {

`  var editor = asset.AsMap();`\
`  `\
`  Map sourceMap = this.Helper.ModContent.Load<Map>("custom-map.tmx");`\
`  editor.PatchMap(sourceMap, targetArea: new Rectangle(30, 10, 20, 20));`

});

</syntaxhighlight>



Available method arguments:

{\| class="wikitable"

\|- ! argument ! usage \|- \| `source` \| The source map to copy & paste
onto the loaded map. \|- \| `sourceArea` \| *(optional)* The tile area
within the source map to copy (or omit to use the entire source map).
This must fit within the target map. \|- \| `targetArea` \| *(optional)*
The tile area within the loaded map to replace (or omit to replace
starting from the top-left corner up to the full source size). \|- \|
`patchMode` \| *(optional)* How to merge tiles into the target map. The
default is `ReplaceByLayer`.

For example, assume a mostly empty source map with two layers: `Back`
(red) and `Buildings` (blue):\
<a href="File_SMAPI_content_API_-_map_patch_mode_-_source.png"
class="wikilink"
title="File:SMAPI content API - map patch mode - source.png"><span>File:SMAPI</span>
content API - map patch mode - source.png</a>

Here's how that would be merged with each patch mode (black areas are
the empty void under the map):

<File:SMAPI> content API - map patch mode - overlay.png\|`Overlay`: only
matching tiles are replaced. The red tile replaces the ground on the
`Back` layer, but the ground is visible under the blue `Buildings` tile.
<File:SMAPI> content API - map patch mode - replace by
layer.png\|`ReplaceByLayer` *(default)*: all tiles are replaced, but
only on layers that exist in the source map. <File:SMAPI> content API -
map patch mode - replace.png\|`Replace`: all tiles are replaced.

\|}

:; ExtendMap



Extend the map if needed to fit the given size. Note that **this is an
expensive operation** and resizes the map in-place. For example:

e.Edit(asset =\> {

`  var editor = asset.AsMap();`

`  // make sure the map is at least 256 tiles high`\
`  editor.ExtendMap(minHeight: 256);`

});

</syntaxhighlight>



Available method arguments:

{\| class="wikitable"

\|- ! argument ! usage \|- \| `minWidth` \| The minimum desired width in
tiles. If the map width is less than this value, it'll be extended on
the right up to that size. \|- \| `minHeight` \| The minimum desired
height in tiles. If the map height is less than this value, it'll be
extended from the bottom up to that size. \|}

## Advanced

### Use `IRawTextureData`

When loading image data, creating a `Texture2D` instance or calling its
`GetData`/`SetData` methods is very expensive and involves GPU calls.
You can avoid that by loading images as SMAPI's `IRawTextureData`
instead, which returns the data directly with no GPU calls. You can then
pass it directly to other SMAPI APIs like
<a href="Modding_Modder_Guide_APIs_Content#Edit_an_image"
class="wikilink" title="PatchImage"><samp>PatchImage</samp></a>.

For example, this mod applies an image overlay to Abigail's portrait
without loading the overlay as a `Texture2D` instance:

``` c#
public class ModEntry : Mod
{
    public override void Entry(IModHelper helper)
    {
        helper.Events.Content.AssetRequested += this.OnAssetRequested;
    }

    private void OnAssetRequested(object sender, AssetRequestedEventArgs e)
    {
        if (e.NameWithoutLocale.IsEquivalentTo("Portraits/Abigail"))
        {
            e.Edit(asset =>
            {
                var editor = asset.AsImage();

                IRawTextureData overlay = this.Helper.ModContent.Load<IRawTextureData>("assets/overlay.png");
                editor.PatchImage(overlay);
            });
        }
    }
}
```

You can also edit the `IRawTextureData` data directly before passing it
to other methods. For example, this converts the texture to grayscale:

``` c#
IRawTextureData image = this.Helper.ModContent.Load<IRawTextureData>("assets/image.png");

int pixelCount = image.Width * image.Height;
for (int i = 0; i < pixelCount; i++)
{
    Color color = image.Data[i];
    if (color.A == 0)
        continue; // ignore transparent color

    int grayscale = (int)((color.R * 0.3) + (color.G * 0.59) + (color.B * 0.11)); // https://stackoverflow.com/a/596282/262123
    image.Data[i] = new Color(grayscale, grayscale, grayscale, color.A);
}
```

(Note: while SMAPI's implementation of IRawTextureData is exactly as
long as it needs to be, this may not be the case for implementations of
IRawTextureData from mods.)

### Compare asset names

You can't use normal string comparison with asset names. For example,
`Characters/Abigail` and `CHARACTERS\ABIGAIL` are the same asset name,
but comparing them with C#'s `==` operator will return false.

You can use SMAPI's `IAssetName` type to compare asset names instead.
For example, `assetName.IsEquivalentTo("Characters/Abigail")` will
return true for both of the above names. There are two ways to get an
`IAssetName` value:

- In content events like `AssetRequested`, use the `e.Name` or
  `e.NameWithoutLocale` property.
- You can parse a custom asset name string into an `IAssetName`:
  ``` c#
  IAssetName assetName = this.Helper.GameContent.ParseAssetName("CHARACTERS/Abigail");
  if (assetName.StartsWith("Characters/")) { ... }
  if (assetName.IsEquivalentTo("Characters/Abigail")) { ... }
  ```

If you *really* need to compare strings manually, you should normalize
the asset names using
<a href="Modding_Modder_Guide_APIs_Utilities#File_paths"
class="wikilink" title="PathUtilities"><samp>PathUtilities</samp></a>
and compare case-insensitively. For example:

``` c#
string assetName = "Characters/Dialogue/Abigail";
string dialoguePrefix = PathUtilities.NormalizeAssetName("Characters/Dialogue/");
bool isDialogue = assetName.StartsWith(dialoguePrefix, StringComparison.OrdinalIgnoreCase);
```

### Cache invalidation

You can reload an asset by invalidating it from the cache. It will be
reloaded next time the game requests it (and mods will have another
chance to intercept it), and SMAPI will automatically update references
to the asset in many cases. For example, this lets you change what
clothes an NPC is wearing (by invalidating their cached sprites or
portraits).

Please be aware that in some cases a localized version of the asset will
be cached and simply invalidating the default asset will not work for
any language other than english.

Reloading assets is fairly expensive, so use this API judiciously to
avoid impacting game performance. Definitely don't do this every update
tick.

Typically you'll invalidate a specific asset key:

``` c#
helper.GameContent.InvalidateCache("Data/ObjectInformation");
```

You can also invalidate assets matching a lambda:

``` c#
helper.GameContent.InvalidateCache(asset => asset.DataType == typeof(Texture2D) && asset.Name.IsEquivalentTo("Data/ObjectInformation"));
```

### Patch helper for custom assets

A patch helper provides utility methods for editing a given asset
(*e.g.,* to merge maps or resize an image).

You can get a patch helper for arbitrary data. For example, this loads
two map files and merges them:

``` c#
Map farm = this.Helper.ModContent.Load<Map>("assets/farm.tmx");
Map islands = this.Helper.ModContent.Load<Map>("assets/islands.tmx");

this.Helper.ModContent
   .GetPatchHelper(farm)
   .AsMap()
   .PatchMap(source: islands, targetArea: new Rectangle(0, 26, 56, 49));
```

See <a href="#Edit_a_game_asset" class="wikilink"
title="edit a game asset"><em>edit a game asset</em></a> for a
description of the available patch helpers.

### Let other mods edit your internal assets

Other mods can't edit your internal mod files (including data or texture
files), but they *can* edit custom assets you provide through the
content pipeline. This technique consists of three steps:

1.  Define a custom asset based on the internal file using the
    <a href="Modding_Modder_Guide_APIs_Events#Content.AssetRequested"
    class="wikilink"
    title="AssetRequested event"><samp>AssetRequested</samp> event</a>.
2.  Detect when it's loaded/changed using the
    <a href="Modding_Modder_Guide_APIs_Events#Content.AssetReady"
    class="wikilink" title="AssetReady event"><samp>AssetReady</samp>
    event</a>.
3.  Load it through the content pipeline when you need it.

For example, this mod just loads a data asset (a dictionary of model
entries):

``` c#
public class ModEntry : Mod
{
    /// <summary>The loaded data.</summary>
    private Dictionary<string, ExampleModel> Data;

    /// <inheritdoc/>
    public override void Entry(IModHelper helper)
    {
        helper.Events.Content.AssetRequested += this.OnAssetRequested;
        helper.Events.Content.AssetReady += this.OnAssetReady;
        helper.Events.GameLoop.GameLaunched += this.OnGameLaunched;
    }

    private void OnAssetRequested(object sender, AssetRequestedEventArgs e)
    {
        //
        // 1. define the custom asset based on the internal file
        //
        if (e.Name.IsEquivalentTo("Mods/Your.ModId/Data"))
        {
            e.LoadFromModFile<Dictionary<string, ExampleModel>>("assets/default-data.json", AssetLoadPriority.Medium);
        }
    }

    private void OnAssetReady(object sender, AssetReadyEventArgs e)
    {
        //
        // 2. update the data when it's reloaded
        //
        if (e.Name.IsEquivalentTo("Mods/Your.ModId/Data"))
        {
            this.Data = Game1.content.Load<Dictionary<string, ExampleModel>>("Mods/Your.ModId/Data");
        }
    }

    private void OnGameLaunched(object sender, GameLaunchedEventArgs e)
    {
        //
        // 3. load the data
        //    (This doesn't need to be in OnGameLaunched, you can load it later depending on your mod logic.)
        //
        this.Data = Game1.content.Load<Dictionary<string, ExampleModel>>("Mods/Your.ModId/Data");
    }
}
```

This works for any asset type (e.g. maps or textures), and you can do
this even without an internal file (e.g. using
`e.LoadFrom(() => new Dictionary<string, ExampleModel>(), AssetLoadPriority.Medium)`).

## See also

- [Tutorial: Making Framework
  Mods](https://stardewmodding.wiki.gg/wiki/Tutorial:_Making_Framework_Mods)
  for an external tutorial on making new framework mods that utilize the
  content pipeline, including loading, reading and invalidating new
  assets.

<a href="ru_Модификации_Руководство_мододела_API_Контент"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Контент">ru:Модификации:Руководство
мододела/API/Контент</a>
<a href="zh_模组_制作指南_APIs_Content" class="wikilink"
title="zh:模组:制作指南/APIs/Content">zh:模组:制作指南/APIs/Content</a>
