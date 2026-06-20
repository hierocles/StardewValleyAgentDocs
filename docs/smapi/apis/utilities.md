---
title: "Utilities"
wiki_source: "Modding:Modder Guide/APIs/Utilities"
permalink: /Modding:Modder_Guide/APIs/Utilities/
category: smapi
tags: [utilities, metadata, mod-path, constants, context, helpers, dates, file-paths]
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

SMAPI provides some C# objects you can use to simplify your code.

## Metadata

### Mod path

Before handling mod folder paths, be aware that:

- The **mod's folder path is not consistent**. The game is installed to
  different folders, Nexus mods are often unzipped into a folder like
  `Mods/Your Mod Name 1.27.5-541-1-27-5-1598664794/YourModFolder` by
  default, and players can organize their mod folders like
  `Mods/For single-player/YourModFolder`.
- Paths are formatted differently on Linux/Mac/Android vs Windows.

You don't need to worry about that when using SMAPI APIs, which take
relative paths and automatically fix the format if needed:

``` c#
var data = this.Helper.Data.ReadJsonFile<SomeDataModel>("assets/data.json");
```

If you really need a full path, you should use
`this.Helper.DirectoryPath` and `Path.Combine` to get it:

``` c#
string path = Path.Combine(this.Helper.DirectoryPath, "assets", "data.json"); // "assets/data.json" in the current mod's folder
var file = new FileInfo(path);
```

See
*<a href="#Constants" class="wikilink" title="Constants">Constants</a>*
for other paths like the game folder.

### Constants

The `Constants` class provides metadata about SMAPI and the game.

<table>
<thead>
<tr>
<th><p>value</p></th>
<th><p>meaning</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Constants.ApiVersion</samp></p></td>
<td><p>The version of the running SMAPI instance.</p></td>
</tr>
<tr>
<td><p><samp>Constants.MinimumGameVersion</samp><br />
<samp>Constants.MaximumGameVersion</samp></p></td>
<td><p>The game versions supported by the running SMAPI
instance.</p></td>
</tr>
<tr>
<td><p><samp>Constants.TargetPlatform</samp></p></td>
<td><p>The current operating system (one of <samp>Android</samp>,
<samp>Linux</samp>, <samp>Mac</samp>, or <samp>Windows</samp>).</p></td>
</tr>
<tr>
<td><p><samp>Constants.GameFramework</samp></p></td>
<td><p>The game framework running the game (one of <samp>Xna</samp> or
<samp>MonoGame</samp>).</p></td>
</tr>
<tr>
<td><p><samp>Constants.GamePath</samp></p></td>
<td><p>The absolute path to the <samp>Stardew Valley</samp>
folder.</p></td>
</tr>
<tr>
<td><p><samp>Constants.ContentPath</samp></p></td>
<td><p>The absolute path to the game's <samp>Content</samp>
folder.</p></td>
</tr>
<tr>
<td><p><samp>Constants.DataPath</samp></p></td>
<td><p>The absolute path to the game's data folder (which contains the
<a href="Saves" class="wikilink" title="save folder">save
folder</a>).</p></td>
</tr>
<tr>
<td><p><samp>Constants.LogDir</samp></p></td>
<td><p>The absolute path to the folder containing the game and SMAPI
logs.</p></td>
</tr>
<tr>
<td><p><samp>Constants.SavesPath</samp></p></td>
<td><p>The absolute path to the <a href="Saves" class="wikilink"
title="save folder">save folder</a>.</p></td>
</tr>
<tr>
<td><p><samp>Constants.CurrentSavePath</samp></p></td>
<td><p>The absolute path to the current save folder, if a save is
loaded.</p></td>
</tr>
<tr>
<td><p><samp>Constants.SaveFolderName</samp></p></td>
<td><p>The name of the current save folder (like
<samp>Name_012345789</samp>), if a save is loaded.</p></td>
</tr>
</tbody>
</table>

### Context

The `Context` class provides information about the game state and player
control.

Game/player state
{\| class="wikitable"

\|- ! value ! meaning \|- \| `Context.IsGameLaunched` \| Whether the
game has been launched and initialised. This becomes true immediately
before the first update tick. \|- \| `Context.IsWorldReady` \| Whether
the player has loaded a save and the world has finished initialising.
Useful for ignoring events before the save is loaded. \|- \|
`Context.IsPlayerFree` \| Whether `Context.IsWorldReady` and the player
is free to act on the world (no menu is displayed, no cutscene is in
progress, etc). \|- \| `Context.CanPlayerMove` \| Whether
`Context.IsPlayerFree` and the player is free to move (*e.g.,* not using
a tool). \|- \| `Context.IsInDrawLoop` \| Whether the game is currently
running the draw loop. This isn't relevant to most mods, since you
should use <a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="display events">display events</a> to draw to the screen. \|}

<a href="Multiplayer" class="wikilink"
title="Multiplayer">Multiplayer</a>
{\| class="wikitable"

\|- ! value ! meaning \|- \| `Context.IsMultiplayer` \| Whether
`Context.IsWorldReady`, and the world was loaded in multiplayer mode
(regardless of whether any other players are connected) or is currently
in split-screen mode. \|- \| `Context.IsSplitScreen` \| Whether
`Context.IsMultiplayer` and the *current player* is in split-screen
mode. This doesn't apply for remote players. \|- \|
`Context.HasRemotePlayers` \| Whether `Context.IsMultiplayer` and any
players are connected over the network. \|- \| `Context.IsMainPlayer` \|
Whether `Context.IsWorldReady`, and the player is the main player. This
is always true in single-player, and true when hosting in multiplayer.
\|- \| `Context.IsOnHostComputer` \| Whether the current player is on
the host computer. This is true when `Context.IsMainPlayer`, or for
farmhands in split-screen mode. \|- \| `Context.ScreenId` \| The unique
ID of the current screen in split-screen mode. The main player always
has ID 0. A screen is always assigned a new ID when it's opened (so a
player who quits and rejoins will get a new screen ID). \|}

## Helpers

### Dates

Use `SDate` for calculating in-game dates. You start by creating a date:

``` c#
var date = SDate.Now(); // current date
var date = new SDate(28, "spring"); // date in the current year
var date = new SDate(28, "spring", 2); // date in the given year
var date = SDate.From(Game1.Date); // from a game date
```

Then you can calculate offsets from any date:

``` c#
// add days
new SDate(28, "spring", 1).AddDays(370); // 06 fall in year 4

// subtract days
new SDate(01, "spring", 2).AddDays(-1); // 28 winter in year 1
```

...and compare dates:

``` c#
var a = new SDate(01, "spring");
var b = new SDate(02, "spring");
if (a < b) // true
  ...
```

...and get a translated date string:

``` c#
var date = new SDate(15, "summer");
string message = $"See you on {date.ToLocaleString(withYear: false)}!"; // See you on Summer 15!
```

Note that `SDate` won't let you create invalid dates:

``` C#
// ArgumentException: Invalid day '30', must be a value from 1 to 28.
new SDate(30, "spring");

// ArithmeticException: Adding -1 days to 01 spring Y1 would result in invalid date 28 winter Y0.
new SDate(01, "spring", 1).AddDays(-1);
```

Once created, dates have a few properties you can use:

| property | meaning |
|----|----|
| `Day` | The day of month. |
| `Season` | The normalised season name. |
| `SeasonIndex` | The zero-based season index recognised by game methods like `Utility.getSeasonNameFromNumber`. |
| `Year` | The year number. |
| `DayOfWeek` | The day of week (like `Monday`). |
| `DaysSinceStart` | The number of days since the first day, inclusively (*i.e.,* 01 spring Y1 = 1). |

### File paths

`PathUtilities` provides utility methods for working with file paths and
<a href="Modding_Modder_Guide_APIs_Content" class="wikilink"
title="asset names">asset names</a>, complementing the `Path` class
provided by .NET:

<table>
<thead>
<tr>
<th><p>method</p></th>
<th><p>usage</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>GetSegments</code></p></td>
<td><p>Split a path into its delimited segments, like
<code>/usr/bin/example</code> → <code>usr</code>, <code>bin</code>, and
<code>example</code>. For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="dt">string</span><span class="op">[]</span> segments <span class="op">=</span> PathUtilities<span class="op">.</span><span class="fu">GetSegments</span><span class="op">(</span>Constants<span class="op">.</span><span class="fu">ExecutionPath</span><span class="op">);</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><code>IsSafeRelativePath</code></p></td>
<td><p>Get whether a path is relative and doesn't contain directory
climbing (<code>../</code>), so it's guaranteed to be within the parent
folder.</p></td>
</tr>
<tr>
<td><p><code>IsSlug</code></p></td>
<td><p>Get whether a string can be used as a 'slug', containing only
basic characters that are safe in all contexts (<em>e.g.,</em>
filenames, URLs, SMAPI IDs, etc).</p></td>
</tr>
<tr>
<td><p><code>NormalizePath</code></p></td>
<td><p>Normalize file paths or asset names to match the format used by
the current OS. For example:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode c#"><code class="sourceCode cs"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="dt">string</span> path <span class="op">=</span> PathUtilities<span class="op">.</span><span class="fu">NormalizePathSeparators</span><span class="op">(</span>@<span class="st">&quot;Characters\Dialogue//Abigail&quot;</span><span class="op">);</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="co">// Linux/Mac: &quot;Characters/Dialogue/Abigail&quot;</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="co">// Windows: &quot;Characters\Dialogue\Abigail&quot;</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

### Per-screen data

SMAPI's `PerScreen<T>` utility manages a separate value for each local
screen in split-screen mode. See
<a href="Modding_Modder_Guide_APIs_Multiplayer#Per-screen_data"
class="wikilink"
title="PerScreen&lt;T&gt; in the multiplayer API"><samp>PerScreen&lt;T&gt;</samp>
in the multiplayer API</a> for details.

### Semantic versions

Use `SemanticVersion` to manipulate and compare versions per the
[Semantic Versioning 2.0 standard](http://semver.org/). Example usage:

``` c#
// build version from parts
ISemanticVersion version = new SemanticVersion(5, 1, 0, "beta");

// build version from string
ISemanticVersion version = new SemanticVersion("5.1.0-beta");

// compare versions (also works with SemanticVersion instances instead of strings)
new SemanticVersion("5.2").IsOlderThan("5.10"); // true
new SemanticVersion("5.10").IsNewerThan("5.10-beta"); // true
new SemanticVersion("5.1").IsBetween("5.0", "5.2"); // true
```

Note that game versions before 1.2.0 and some mod versions are
non-standard (*e.g.,* Stardew Valley 1.11 comes *before* 1.2). All SMAPI
versions are standard.

## Input

SMAPI's `SButton` constants uniquely represent controller, keyboard, and
mouse button presses or clicks. See the
<a href="Modding_Modder_Guide_APIs_Input" class="wikilink"
title="Input">Input</a> page for more info.

<a href="ru_Модификации_Руководство_мододела_API_Утилиты"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Утилиты">ru:Модификации:Руководство
мододела/API/Утилиты</a>
<a href="zh_模组_制作指南_APIs_Utilities" class="wikilink"
title="zh:模组:制作指南/APIs/Utilities">zh:模组:制作指南/APIs/Utilities</a>
