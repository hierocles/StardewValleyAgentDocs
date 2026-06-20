---
title: "Troubleshooting"
wiki_source: "Modding:Player Guide/Troubleshooting"
permalink: /Modding:Player_Guide/Troubleshooting/
category: player-guide
tags: [player-guide, troubleshooting, the-basics, common-fixes, span-id-reset-content-reset-your-content-files-span, span-id-dedicated-gpu-run-the-game-on-your-dedicated-graphics-card-windows-only-span, faqs-about-stardew-valley-1-6, game-doesn-t-launch]
---
}\|1}}}} }

` |}`\
`   |unofficial`\
`   |}`\
`     |broken`\
`     |ok`\
`   }}`\
` }}`

}}}} }}} }}} }}} }}} \|- class="mod" style="line-height: 1em;
\|ok\|optional=background: \#9F9; \|workaround\|unofficial=background:
\#CF9; \|broken=background: \#F99; \|obsolete\|abandoned=background:
\#999}}" id="" data-id="" data-name="" data-author=""
}\|data-cf-id="}"}} }\|data-curseforge-id="}"}}
}\|data-curseforge-key="}"}} }\|data-nexus-id="}"}}
}\|data-moddrop-id="}"}} }\|data-github="}"}}
}\|data-custom-source="}"}} data-url="}}}}}}}}}" data-status=""
}\|data-broke-in="}"}} }\|data-unofficial-version="}"}}
}\|data-unofficial-url="}"}} }\|data-pr="}"}}
}\|data-content-pack-for="}"}} }\|data-dev-note="}"}}
}\|data-map-local-versions="}"}} }\|data-map-remote-versions="}"}}
}\|data-change-update-keys="}"}} \| }\|\[}
\]\|}\|\|}\|\[<https://www.curseforge.com/stardewvalley/mods/>}
\]\|}\|\[<https://community.playstarbound.com/resources/>} \]\|}\|\[}
\]\|}}}}}}}}}} \| \| <span class="mod-summary">

`|ok         = ✓ }|}|use latest version.}}`\
`|optional   = ✓ }|}|use optional download.}}`\
`|unofficial = ⚠ broken}|, use [} unofficial update]}| (`<small>`}`</small>`)}}|}}}.`\
`|workaround = ⚠ broken, }`\
`|broken     = ↻ broken, }|}||not updated yet.|not open-source.}}}}`\
`|obsolete   = ✖ }|}|remove this mod (obsolete).}}`\
`|abandoned  = ✖ }|}|remove this mod (no longer maintained).}}`\
`|unknown    = ☐ }|}|not tested yet.}}`

}}</span>\|optional\|[^1]}} }\|\
⚠ }} \| <small>}</small> \| }\|\[<https://github.com/>} source\]\|}\|\[}
source\]\|<span style="color: red; font-size: 0.85em; opacity: 0.5;">closed
source</span>}}}} \| class="no-wrap"\|<small>
<a href="#" class="wikilink" title="#">#</a> }\| \[} PR\]}}
}\|<abbr title="}">\[dev note\]</abbr>}}
}\|1\|0}}\|}\|1\|0}}\|\|<abbr title="The mod data is invalid: can't specify CurseForge key or ID without the other.">\[⚠
invalid data\]</abbr>}}</small>

Did something go wrong with your game? This is the page for you. (This
page isn't only for players who use mods!)

# The basics

## Common fixes

1.  Restart your computer.
2.  Make sure you have Stardew Valley or later.
    1.  Click the "?" button on the title screen, and the version will
        appear in the bottom-left.
    2.  Right-click on the game's name in Steam and go to Properties.
        Check the betas tab, and make sure you are <strong>not opted
        into the 32-bit beta</strong> if you are trying to use SMAPI.
        For more information, see <a
        href="Modding_Player_Guide_Troubleshooting#SMAPI_doesn.27t_work_with_the_compatibility_branch"
        class="wikilink"
        title="Modding:Player_Guide/Troubleshooting#SMAPI_doesn.27t_work_with_the_compatibility_branch">Modding:Player_Guide/Troubleshooting#SMAPI_doesn.27t_work_with_the_compatibility_branch</a>.
3.  <a href="#reset-content" class="wikilink"
    title="Reset your content files">Reset your content files</a>.
4.  If you use SMAPI:
    1.  Make sure you have the [latest version of
        that](https://smapi.io/).\
        <small>The SMAPI version is shown at the top of the SMAPI
        console window.</small>
    2.  Upload a log to [the log parser](https://smapi.io/log),
        following the instructions on that page to find where your log
        is stored. It can help you diagnose common errors. Take a look
        at this [annotated
        log](https://stardewmodding.wiki.gg/wiki/Tutorial:_How_to_read_your_SMAPI_log)
        for more information on how to read and understand your log.
        1.  If the parser website says the log is too big, or it takes
            too long to parse, you can open it up in any text editor
            (Notepad or Notepad++ work; on Mac TextEditor works), then
            copy from the very top of the log to the bottom of the first
            couple errors, and parse that.
    3.  The very top of your log will show a list of all your mods that
        need to be updated. You can also use to keep track of your
        updates from the in-game menu. **The first thing to try when
        you're having issues with mods is to update everything shown
        there, even if some of the mods seem to be working fine right
        now.**
    4.  If you've narrowed down the issue to a specific mod or group of
        mods, try performing a clean reinstall.
        1.  Remove all folders for the mod that's causing the issue,
            making sure to check the mod page for a list of every folder
            that's included. (If you're downloading mods from Nexus, you
            can look under "Preview File Contents." On ModDrop, you can
            find that information under "Files" on the sidebar.)
        2.  Redownload the mod and follow the installation instructions
            on the mod page. If you normally use a mod manager,
            reinstall the mod manually to make sure your issue wasn't
            caused by the mod manager placing files in the wrong
            locations.
5.  If you still get the error, look through the common issues on this
    page or <a href="Modding_Help#Using_mods" class="wikilink"
    title="ask for help">ask for help</a>!

## <span id="reset-content">Reset your content files</span>

Many problems are caused by broken game files (especially if you
<a href="Modding_Using_XNB_mods" class="wikilink"
title="use XNB mods">use XNB mods</a>). You can reset your game files to
fix that. SMAPI mods won't be affected.

1.  See the instructions for your platform:
    - [for
      Steam](https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335);
    - [for GOG
      Galaxy](https://support.gog.com/hc/en-us/articles/360003930017);
    - [for Xbox App for PC / PC Game
      Pass](https://support.xbox.com/en-US/help/games-apps/troubleshooting/troubleshoot-games-windows-10)
      (under *Problems launching a game from the Xbox app* and then
      *Repair the game*).
2.  If you use SMAPI on Linux or macOS, reinstall SMAPI to fix the
    launcher.

<div class="modding-error-box">

**Caution:** XNB mods (which replace your game files directly) are
<a href="Modding_Using_XNB_mods" class="wikilink"
title="no longer recommended">no longer recommended</a> and can cause
issues. Resetting your content files will remove XNB mods you installed.
After doing so, consider
<a href="Modding_Using_XNB_mods#Alternatives_using_Content_Patcher"
class="wikilink" title="using content packs instead">using content packs
instead</a>.'''

</div>

## <span id="dedicated-gpu">Run the game on your dedicated graphics card (Windows only)</span>

<a href="File_SMAPI_dedicated_GPU_on_Windows.png" class="wikilink"
title="thumbnail">thumbnail</a>

Many computers have two options for running games: *integrated graphics*
(part of the processor) and *dedicated graphics* (a separate graphics
card by NVIDIA or AMD). Stardew Valley should be run on the dedicated
graphics, but that's not always the default (especially on laptops). If
you're not sure if this applies to your computer, it's safe to just try
the instructions below anyway — they just won't do anything if it
doesn't apply.

To fix this:

1.  From the start menu, search for *Graphics Settings* and open it.
2.  In the window that opens, click "Browse" near the top and choose in
    <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
    class="wikilink" title="your game folder">your game folder</a> (or
    if you play without mods).
3.  In the app list, click "Options" under `StardewModdingAPI` (or
    `Stardew Valley` if you play without mods).
4.  Change the Graphics preference to "High performance".
5.  Save.
6.  Check whether your issues still happen.

## FAQs about Stardew Valley 1.6

Are mods updated for 1.6?
Stardew Valley 1.6 is a major update, so many mods will need to be
updated for it.

:\* The latest [SMAPI](https://smapi.io/) and [Content
Patcher](https://www.nexusmods.com/stardewvalley/mods/1915) add full
support for Stardew Valley 1.6. Make sure you update SMAPI and all your
mods to the latest versions.

:\* 44% of SMAPI mods were ready on day one, and that number should
steadily rise as they get updated. You can check the [mod compatibility
list](https://smapi.io/mods/) to see if your mods are updated, or look
for purple update alerts in your SMAPI console window.

:\* Most content packs should work fine once the SMAPI mod which loads
them is updated.

:\*
<a href="Modding_Using_XNB_mods" class="wikilink" title="XNB mods">XNB
mods</a> are mostly broken in 1.6. These have been deprecated for years
and may cause issues like broken textures, missing or broken game
content, and crashes. You can
<a href="#Reset_your_content_files" class="wikilink"
title="reset your game files">reset your game files</a> to remove any
you have.

What does 1.6 change for mods?
Stardew Valley 1.6 has
<a href="Modding_Migrate_to_Stardew_Valley_1.6" class="wikilink"
title="a huge number of changes to help mod authors">a huge number of
changes to help mod authors</a>. For players, it has and will also let
mods do much more in the future.

<!-- -->

Can I go back to Stardew Valley 1.5.6 until my mods update?
Yep. If you use Steam:

1.  Click *Stardew Valley* in the Steam client.
2.  Hit the cog button in the top-right corner and click the
    *Properties* option.
3.  Go to the *Betas* tab.
4.  Select "legacy_1.5.6" in the Beta Participation dropdown.

<!-- -->


If you use GOG:

1.  Launch GOG Galaxy.
2.  Click Stardew Valley.
3.  From the menu at the top, click *Extras* to see downloads for
    previous versions.

# Game doesn't launch

When you try to launch the game, nothing seems to happen or the window
closes instantly. (If you use Steam, it might show 'running' for a few
seconds.)

<dl>

<dt>

1\. Try common fixes:

</dt>

<dd>

1.  Restart your computer.
2.  <a href="#Reset_your_content_files" class="wikilink"
    title="Reset your content files">Reset your content files</a> or
    reinstall the game.
3.
4.  Delete your `startup_preferences` file. (To find it:
    <a href="Saves#Find_your_save_files" class="wikilink"
    title="open your saves folder">open your saves folder</a>, and it'll
    be in the folder that contains it.)
5.  Install the software for your graphics card (i.e. [NVIDIA
    App](https://www.nvidia.com/en-us/software/nvidia-app/) or [AMD
    Software](https://www.amd.com/en/technologies/software)), then use
    that software to update to your latest graphics drivers. (See [how
    to check which graphics card you
    have](https://www.tomsguide.com/how-to/what-graphics-card-do-i-have-heres-how-to-tell).)
6.  Disable any programs that intercept the game (like MSI AfterBurner
    or RivaTuner).
7.  If you use...
    <table>
    <thead>
    <tr>
    <th><p>system</p></th>
    <th><p>common fixes</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>SMAPI on Windows</p></td>
    <td><p>If you use Steam, double-check that your Steam launch options
    match the <a href="Modding_Installing_SMAPI_on_Windows#Steam"
    class="wikilink" title="instructions in the install guide">instructions
    in the install guide</a>.</p></td>
    </tr>
    <tr>
    <td><p>SMAPI on Linux</p></td>
    <td><p>If you use Steam, make sure your Steam launch options are
    empty.</p>
    <p>Your default terminal might not be compatible. Try installing the
    xterm terminal.</p></td>
    </tr>
    <tr>
    <td><p>SMAPI on macOS</p></td>
    <td><p>If you use Steam, make sure your Steam launch options are
    empty.</p></td>
    </tr>
    </tbody>
    </table>
8.

</dd>

<dt>

2\. (*Windows only*) Run the game on your dedicated graphics card:

</dt>

<dd>

See <a href="#dedicated-gpu" class="wikilink"
title="Run the game on your dedicated graphics card (Windows only)"><em>Run
the game on your dedicated graphics card (Windows only)</em></a> above.
Don't skip this step! It very often fixes the issue.

</dd>

<dt>

3\. Check if there's an error message:

</dt>

<dd>

1.  <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
    class="wikilink" title="Open your game folder">Open your game folder</a>.
2.  Right-click the folder background. On Windows, also hold
3.  Click the option that says *Open in Command Prompt*, *Open in
    PowerShell*, *Open in Windows Terminal* or *Open In Terminal*
    (depending on your system settings/OS).
4.  Type this command:
    | if you play...            | command                   |
    |---------------------------|---------------------------|
    | with mods on Windows      | `.\StardewModdingAPI.exe` |
    | without mods on Windows   | `.\"Stardew Valley.exe"`  |
    | with mods on Mac/Linux    | `./StardewModdingAPI`     |
    | without mods on Mac/Linux | `./"StardewValley"`       |
5.  Press enter to run the command.
6.  If it shows an error message, check for a section under
    <a href="#Specific_error_messages" class="wikilink"
    title="Specific error messages"><em>Specific error messages</em></a>
    below.

</dd>

(note: any command prompt works, including WSL's, if you don't like
powershell/command prompt.)

<dt>

4\. Ask for help:

</dt>

<dd>

If you still haven't solved it, come
<a href="#Ask_for_help" class="wikilink" title="Ask for help">Ask for
help</a>!

</dd>

</dl>

# Specific errors when launching game

## "Could not load 'Stardew Valley' or one of its dependencies"

SMAPI wasn't able to load the game's executable. There's a number of
possible reasons for this:

1.  <a href="#Reset_your_content_files" class="wikilink"
    title="Reset your content files">Reset your content files</a>.
2.  Make sure you have Stardew Valley or later. (If you're not sure:
    launch without mods per step 4 below, click the "?" button on the
    title screen, and check the bottom-left corner of the screen.)
3.  Make sure you have the [latest version of SMAPI](https://smapi.io/).
4.  Make sure you can launch the game without SMAPI:
    1.  Open
        <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
        class="wikilink" title="your game folder">your game folder</a>.
    2.  Double-click (on Windows) or `StardewValley-original` (on
        Linux/macOS).
    3.  If the game doesn't work either, see
        <a href="#Game_doesn&#39;t_launch" class="wikilink"
        title="game doesn&#39;t launch"><em>game doesn't launch</em></a>.
5.  Make sure you didn't enable the "compatibility branch" in Steam or
    GOG Galaxy (<a href="#Known_issues" class="wikilink"
    title="mods don&#39;t work on the compatibility branch">mods don't work
    on the compatibility branch</a>).
6.  Make sure you're running from your game folder (see the
    <a href="Modding_Player_Guide_Getting_Started#Getting_started"
    class="wikilink" title="install instructions">install instructions</a>).
7.  Did you install SMAPI manually (not
    <a href="Modding_Player_Guide_Getting_Started#Install_SMAPI"
    class="wikilink" title="using the installer">using the installer</a>)?
    Make sure you followed all the steps in the installer's `README.txt`
    file.
8.  In rare cases, completely uninstalling then reinstalling the game
    may be needed.

## "The game failed to launch: `Microsoft.Xna.Framework.Graphics.NoSuitableGraphicsDeviceException`: Failed to create graphics device"<span id="no-suitable-gpu"> </span>

That means your graphics drivers aren't supported by the underlying game
framework.

Common fixes are listed below (in the recommended order to try).

### (*Windows only*) Run the game on your dedicated graphics card

See <a href="#dedicated-gpu" class="wikilink"
title="Run the game on your dedicated graphics card (Windows only)"><em>Run
the game on your dedicated graphics card (Windows only)</em></a> above.
Don't skip this step! It very often fixes the issue.

### (*Windows only*) Revert the SDL update

If the error message contains this exact text:

    NullReferenceException: Object reference not set to an instance of an object.
       at MonoGame.OpenGL.GL.LoadExtensions()

Then you're affected by a bug in the game's `SDL2.dll` file, which can
be fixed by reverting to the previous version.

To fix it:

1.  Switch to Stardew Valley 1.6.8.
    To do that if you use Steam:

    1.  Open the Steam client.
    2.  Right-click Stardew Valley and choose *Properties* \> *Betas*.
    3.  Set the "Beta Participation" dropdown to `legacy_1.6.8`.
    4.  Wait until the game finishes updating.

    Or if you use GOG:

    1.  Open the GOG Galaxy client.
    2.  Right-click Stardew Valley and choose *Manage Installation* \>
        *Configure*.
    3.  Set the "Beta channels" dropdown to `compatibility`.
    4.  Wait until the game finishes updating.
2.  Launch the game (without SMAPI) and make sure it works. If it still
    fails, these steps won't fix it.
3.  Revert the SDL update. To do that:
    1.  Open
        <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
        class="wikilink" title="your game folder">your game folder</a>.
    2.  Copy the file to your desktop.
    3.  Switch back to the current version of Stardew Valley by
        repeating the first step, but setting the beta to "None" (Steam)
        or "Disabled" (GOG).
    4.  Copy the from your desktop back into the game folder. It will
        ask if you want to replace the file; say yes.

### Update your graphics drivers

1.  Install the app for your graphics card ([GeForce
    Experience](https://www.nvidia.com/en-us/geforce/geforce-experience/)
    for NVIDIA or [AMD
    Software](https://www.amd.com/en/technologies/software) for AMD). If
    you're not sure, see [how to check which graphics card you
    have](https://www.tomsguide.com/how-to/what-graphics-card-do-i-have-heres-how-to-tell).
2.  Open the app.
3.  Find the section that shows graphics driver info. Make sure it says
    you have the latest version, and install any updates if not.

### (*Linux only*) Don't force Wayland driver for SDL

You may have `SDL_VIDEODRIVER=wayland` set, which will force SDL
applications like Stardew Valley to start under Wayland. Removing this
override might help. It may be in your `.bashrc`, `.bash_profile` or
similar location.

If you want/have to use Wayland (and it's not working out of the box),
you can try to use your system's SDL2 library instead of the one bundled
with Stardew Valley. This is of course unsupported. Navigate into the
game's `game` subfolder and rename `libSDL2-2.0.0.dylib` and
`libSDL2-2.0.so.0`, for example to `libSDL2-2.0.0.dylib.disabled` and
`libSDL2-2.0.so.0.disabled`. If this works, perhaps make a note of it
(for example in a textfile inside your Stardew Valley folder) to avoid
forgetting this change in case you at some point run into issues and
need to undo it.

### Use the compatibility branch or an older version of Stardew Valley

As an absolute last resort, you can...

- Use the [Stardew Valley compatibility
  branch](https://www.stardewvalley.net/compatibility/) (note that that
  <a href="#Known_issues" class="wikilink"
  title="mods don&#39;t work with that version">mods don't work with that
  version</a> currently);
- *or* <a href="#SMAPI_doesn&#39;t_work_with_compatibility_branch"
  class="wikilink"
  title="downgrade to Stardew Valley 1.5.4 or earlier">downgrade to
  Stardew Valley 1.5.4 or earlier</a> (note that you'll need to use
  older versions of SMAPI and many mods).

## "missing executable" (Steam only)

Steam can't find the game launcher, usually because your Steam launch
options are incorrect. Common fixes:

- If you want to use SMAPI:\
  make sure it's installed and your launch options are correct (see
  <a href="Modding_Player_Guide_Getting_Started#Getting_started"
  class="wikilink" title="install guide">install guide</a>).
- If you're uninstalling SMAPI:\
  \# In Steam, right-click *Stardew Valley* and choose *Properties*.
  1.  Click the *Set Launch Options* button.
  2.  Make sure the textbox is completely empty.

## "Could not load file or assembly"

If the 'file or assembly' starts with `Microsoft` or `System` (like
"*FileNotFoundException: Could not load file or assembly
'System.\[...\]' or one of its dependencies*") OR you get something like
"The library '\[...\].dll' required to execute the application is not
found in 'C:\Program Files\dotnet\`" (often this is `hostpolicy.dll`),
something is wrong with the core frameworks used by the game.

Common fixes:

- <a href="Modding_Player_Guide_Troubleshooting#Reset_your_content_files"
  class="wikilink" title="Reset the content files">Reset the content
  files</a>.
- If that doesn't work, uninstall Stardew Valley (and fully delete your
  game folder) and then reinstall it.
- Check to make sure you don't <a
  href="Modding_Player_Guide_Troubleshooting#After_updating_to_the_latest_versions.2C_launching_the_game_still_shows_an_old_SMAPI_or_game_version"
  class="wikilink"
  title="accidentally have two copies of the game">accidentally have two
  copies of the game</a>.

(Stardew now comes packaged with the dependencies needed to run, so you
shouldn't need to install them yourself.)

You may also see an error like this if you installed SMAPI manually (by
renaming the .bat to a .zip and moving files yourself). Try reinstalling
SMAPI using the installer if that is the case.

## `OutOfMemoryException` errors

Your log shows `OutOfMemoryException` errors in the console, and the
game may severely lag or crash. That means your game ran out of
available memory mid-session.

This might also show up as `Unable to allocate pixels for the bitmap`.

Some common fixes:

- Make sure you have the latest Stardew Valley , which is 64-bit and
  doesn't have the 32-bit limitations of older versions.
- If you still get the error, you might need to remove content mods you
  don't need (particularly content packs for Custom Music, SAAT or TMXL
  Map Toolkit, which can use a lot of memory).

## NoAudioHardwareException: Audio has failed to initialize

This exception means that for whatever reason, either the game or SMAPI
cannot use your computer's audio. A possible fix (for Windows) is
installing [OpenAl](https://www.openal.org/downloads/). You can also try
plugging in some headphones or connecting a bluetooth headset.

## Mac: Contents/MacOS/StardewValley Already Exists

This error looks something like: "An error occurred in the base update
loop: IOException: The file '/Users/USERNAME/Library/Application
Support/Steam/steamapps/common/Stardew
Valley/Contents/MacOS/StardewValley' already exists."

If this happens, verify the following:

- Show hidden files in Finder with `Command+Shift+.`, then go to your
  home directory (named after your username, likely has a little home
  icon next to it on the left side of Finder). There should be a bunch
  of hidden folders that show up.
- The folder `~/.config/StardewValley/ErrorLogs` exists. If it doesn't
  exist, make it exist.
- Your screenshots button works. If it doesn't work, make sure the
  folder `~/.local/share/StardewValley/Screenshots` exists. If it
  doesn't exist, make it exist.

If neither of those fixes works, it's not clear what to do.

# Specific errors when loading a mod

## "Skipped '...' because it doesn't have a manifest.json"

SMAPI couldn't find the `manifest.json` file for the mod in that folder.

Common causes:

- It's not a SMAPI mod, so it won't work in the `Mods` folder. See the
  mod's page or documentation for install instructions.
- The mod isn't installed correctly. Try deleting and reinstalling the
  mod to fix that. If you're using a mod manager like Vortex, try
  <a href="Modding_Player_Guide_Getting_Started#Install_mods"
  class="wikilink" title="reinstalling the mod yourself">reinstalling the
  mod yourself</a> instead.

## "Skipped '...' because it was blocked by Windows Smart App Control"<span id="smart-app-control"></span>

When you see this error:

<table>
<thead>
<tr>
<th><p>SMAPI version</p></th>
<th><p>error shown</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>≤ 4.5.2</p></td>
<td><p>"<em>Skipped … because its DLL couldn't be loaded.</em>"</p>
<p>When SMAPI developer mode is enabled via , the technical details
show:<br />
<em>FileLoadException: Could not load file or assembly '…'. An
Application Control policy has blocked this file.
(0x800711C7)</em></p></td>
</tr>
<tr>
<td><p>≥ 4.5.3</p></td>
<td><p>"<em>Skipped … because it was blocked by Windows Smart App
Control</em>"</p></td>
</tr>
</tbody>
</table>

The mod was blocked by the optional "Smart App Control" feature in
Windows 11, which tries to guess whether an app is safe. It tends to be
inaccurate and often changes its mind from one moment to the next.
Unfortunately, you [can't bypass it for a known valid
app](https://support.microsoft.com/en-us/windows/smart-app-control-frequently-asked-questions-285ea03d-fa88-4d56-882e-6698afdb7003).

Smart App Control is only enabled if you accepted to send "optional
diagnostic data" to Microsoft during Windows installation. You can
safely disable (and re-enable) it anytime.

If you want to disable Smart App Control:

1.  Open the *Settings* app.
2.  Go to *Privacy & Security \> Windows Security \> App & Browser
    Control \> Smart App Control settings*.
3.  Set it to off.

If you didn't realize you're sending information about your computer
usage to Microsoft, you can optionally disable that too:

1.  Open the *Settings* app.
2.  Go to *Privacy & Security \> Diagnostics & Feedback*.
3.  Set "*Send optional diagnostic data*" to off.

# Other issues launching the game

## SMAPI takes forever to load

There's a few common causes:

- For players on Windows:
  - <a href="#dedicated-gpu" class="wikilink"
    title="Run the game on your dedicated graphics card"><strong>Run the
    game on your dedicated graphics card</strong></a>. Don't skip this
    step!
  - **Make sure the SMAPI window doesn't show 'Select' in the title
    bar**:<a href="File_Screenshot_2022-01-08_140059.png" class="wikilink"
    title="600px">600pxThis</a> pauses loading so you can see what the
    console says, enabled when you select any text on the console
    window. To fix it, just click the console and press the 'enter' key
    a few times.
- **An antivirus is slowing SMAPI.** Often this results in long delays
  while loading (e.g. several seconds to do a very basic task). You can
  try disabling your antivirus to check if this is the cause; if that
  fixes it, re-enable the antivirus and then whitelist SMAPI, Stardew
  Valley, and the game folder in your antivirus settings. (Tip: Windows
  has a default antivirus named Windows Defender, even if you didn't
  install one yourself.)
- **If you have many mods, a loading time measured in minutes is not
  unusual.** The exact loading time depends heavily on which mods you
  have and what your computer is like. If you have a few very large mods
  (e.g. expansion-type mods), you should probably wait a few minutes
  before deciding something is wrong. If you have PyTK installed but are
  no longer using it, try removing it to see if this helps the load
  times.

## SMAPI or mod files disappear, or they're blocked by your antivirus or browser<span id="antivirus"></span><span id="SMAPI_files_disappear_or_antivirus_complains"></span>

Your antivirus or browser might delete, block, or report SMAPI or mod
files. This is almost always a false positive, meaning the files don't
contain a trojan.

:; **How can I know if it's actually safe?**



Nothing on the Internet is guaranteed, but it's most likely safe — you
can check by reading the code (e.g. see ), [decompiling the
download](https://www.jetbrains.com/decompiler/), or [uploading it to
VirusTotal](https://www.virustotal.com/). VirusTotal scans the file with
sixty or so antiviruses; if only one or two detect an issue, it's most
likely a false positive. Note that all files on Nexus Mods are scanned
by VirusTotal automatically before they're available to download.

:; **Why does this happen?**



Antiviruses and browsers are usually concerned because...

- The download is still new. In this case it didn't really detect
  anything, it's just worried because it's an unknown file. Antiviruses
  often show a fake trojan name like `Trojan:Win32/Emali.A!cl` for this.
  Antiviruses learn to allow it after enough users download it, but that
  resets for each release.
- Antiviruses may check for certain patterns like accessing files or
  rewriting code, which are both things SMAPI mods do as part of their
  normal functionality (since changing the game is the whole point).

:; **How can I download a file which my browser blocks as
'suspicious'?**



There are two approaches:

- You can wait a few days before downloading a new update (or a few
  weeks for a less popular mod). Once enough users have downloaded it,
  your browser won't considers it an unknown file anymore.
- *Or* the browser UI which says the file is supicious should have a
  'more info' link, or a symbol like **⋮** or **▼** which indicates
  options. Click that to show the option to download it anyway.

:; **How can I install SMAPI or a mod if my antivirus flags it?**



There are two approaches:

- You can wait few days before downloading a new update (or a few weeks
  for a less popular mod). By then enough users should have downloaded
  it to reduce antivirus alerts.
- *Or* if you've checked that it's safe above, another option is to...
  1.  Temporarily disable your antivirus.
  2.  Redownload and
      <a href="Modding_Player_Guide_Getting_Started#Getting_started"
      class="wikilink" title="install SMAPI">install SMAPI</a> or the
      mod.
  3.  Add an exception to your antivirus for the
      <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
      class="wikilink" title="Stardew Valley folder">Stardew Valley folder</a>
      (search online for your antivirus name with the words *add folder
      exception* for instructions).

## After updating to the latest versions, launching the game still shows an old SMAPI or game version

That usually means you have two copies of the game: one copy you
updated, and another you're actually playing.

To check if that's the issue:

1.  Launch the SMAPI installer again, and note the "Game path" shown on
    the first screen:\
    <a href="File_SMAPI_installer_path.png" class="wikilink"
    title="500px">500px</a>
2.  Launch the game with SMAPI, and note the "Mods go here" path shown
    at the top of the output:\
    <a href="File_SMAPI_mods_path.png" class="wikilink"
    title="500px">500px</a>
3.  Open the game folder through Steam, GOG Galaxy, or Xbox. To do that:
    go to
    <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
    class="wikilink" title="Find your game folder"><em>Find your game
    folder</em></a>, click 'more options' under the table, and see
    options 3–5.
4.  All three paths should be identical (except for the `/Mods` part).

If you have multiple game folders, the best solution is to only have
one. To do that:

1.  Make a copy of your `Mods` folder somewhere else.
2.  Uninstall the game.
3.  Delete any folders you found above.
4.  Reinstall the game through Steam or GOG Galaxy.
5.  Reinstall SMAPI, which should now detect your single game path.
6.  Copy your mods back into the new game folder.

## Game screen is frozen when launched via SteamLink or other Steam RemotePlay

solution - from PC

1.  Launch SDV via SMAPI's StardewModdingAPI
2.  The cmd will open and show logging information about loading... and
    then it will launch SDV
3.  Once SDV is launched you need to \[alt\]+\[tab\] out of it. It
    should go to cmd once you do, but if it doesn't immediately select
    cmd, simple select that window
4.  Click the minimize button \[-\] on cmd to minimize it
5.  With cmd now minimized, you can refocus SDV by clicking the window
    and it should now be unfrozen!

solution - from controller connected to SteamLink

1.  Launch SDV via SMAPI's StardewModdingAPI
2.  The cmd will open and show logging information about loading... and
    then it will launch SDV
3.  Once SDV is launched, the screen will appear frozen. Hold down the
    left "options-like" button on your controller to open the SteamLink
    quick menu.
    - On an Xbox controller, this is the "Back" button
    - On a PlayStation controller, this is the "Share" button
    - On a Steam controller, this is the "Left Arrow" button
4.  In this menu, select the "Virtual Keyboard" option to reveal an
    onscreen keyboard
5.  Select the \`\[alt\]\` key and then the \`\[tab\]\` key. This will
    Alt-Tab you out of the frozen SDV screen and auto-focus the cmd
    window.
6.  With the cmd now revealed and focused, on the still visible "Virtual
    Keyboard" select the "Windows" key and then the "down arrow" key.
    This should minimize the cmd window
    - The "Windows" key is in the bottom-left side of the keyboard and
      looks like it has 4 arrows/triangle icons on it.
7.  When cmd minimizes SDV should automatically be refocused and should
    now be unfrozen!

# Other issues playing the game

## Game lags or stutters in-game

There's a few things you can try.

1.  If you use mods:
    1.  Update SMAPI and your mods to their latest versions.
    2.  Make sure there's no repeating errors in the SMAPI console
        window (if there are, see
        <a href="#Get_help" class="wikilink" title="get help"><em>get
        help</em></a>).
    3.  Temporarily remove all mods except SMAPI and Error Handler. If
        that fixes it, one of your mods might be causing lag. (You can
        still try the other fixes below to see if they help.)
2.  For Windows players only:
    1.  <a href="#dedicated-gpu" class="wikilink"
        title="Run the game on your dedicated graphics card">Run the game on
        your dedicated graphics card</a>.
    2.  Install the software for your graphics card ([GeForce
        Experience](https://www.nvidia.com/en-us/geforce/geforce-experience/)
        for NVIDIA or [AMD
        Software](https://www.amd.com/en/technologies/software) for
        AMD), then use that software to update to your latest graphics
        drivers. (See [how to check which graphics card you
        have](https://www.tomsguide.com/how-to/what-graphics-card-do-i-have-heres-how-to-tell).)
    3.  If using NVIDIA GeForce Experience, make sure WhisperMode is
        disabled.
3.  For Linux/SteamDeck players:
    1.  From <a href="Modding_Game_folder" class="wikilink"
        title="your game folder">your game folder</a>, open
        `smapi-internal/config.json` and set `ListenForConsoleInput` to
        false. (Note the instructions at the top of that file about
        creating a `config.user.json` file.)
    2.  From
        <a href="#(Linux_only)_Don&#39;t_force_Wayland_driver_for_SDL"
        class="wikilink"
        title="#(Linux only) Don&#39;t force Wayland driver for SDL">#(Linux
        only) Don't force Wayland driver for SDL</a>, you can patch the
        bundled SDL binaries to use the system binaries for SDL, and
        this could fix your performance entirely, especially if running
        in fullscreen lags a lot compared to running in 1/4 screen,
        which is an old issue from old versions of SDL2.
4.  Add an exception in your antivirus software for the
    <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
    class="wikilink" title="Stardew Valley folder">Stardew Valley folder</a>.
    You can search online for your antivirus name with the words *add
    folder exception* for instructions.\
    **Note for Windows players:** if didn't install an antivirus, you
    have Windows Defender by default and it *can* cause lag. Try
    [excluding the game
    folder](https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26)
    in that case.
5.  [Set the processor
    affinity](https://www.thewindowsclub.com/processor-affinity-windows)
    for (if using mods) or (without mods) to 2 or higher.
6.  [Set the process
    priority](https://winaero.com/change-process-priority-windows-10/)
    for (if using mods) or (without mods) to *High*.
7.  If you own the Steam version of the game, try launching the game
    through the Steam client.

If you're still having issues after that, see
<a href="#Get_help" class="wikilink" title="get help"><em>get
help</em></a>.

## Game audio doesn't play or audio is distorted (Windows only)

Audio plays fine in your browser or other apps, but the game is silent.
Here are some common fixes:

1.  Restart your computer.
2.  [Make sure the Windows mixer isn't muting the
    game](https://community.playstarbound.com/threads/no-sound.151798/#post-3325874).
3.  Make sure the in-game sound slider options aren't muted.
4.  <a href="#Game_doesn&#39;t_launch" class="wikilink"
    title="Check the debugging options under &quot;Game doesn&#39;t launch&quot;">Check
    the debugging options under "Game doesn't launch"</a>.
5.  <a href="#NoAudioHardwareException_Audio_has_failed_to_initialize"
    class="wikilink"
    title="Check for a NoAudioHardwareException and follow instructions there">Check
    for a NoAudioHardwareException and follow instructions there</a>

## Save disappeared or doesn't load

See <a href="Saves#Troubleshooting" class="wikilink"
title="Saves#Troubleshooting">Saves#Troubleshooting</a>.

## (Linux only) Multiplayer menu doesn't load

The issue is down to a faulty execstack call (See [Steam
discussion](https://steamcommunity.com/app/413150/discussions/0/695372304943764421))
in the call-stack within these bundled libraries that are causing the
multiplayer library to crash and thus the menu to never load. To fix
this:

1.  Obtain a version of patchelf for your distribution, or from
    [upstream](https://nixos.org/patchelf.html) (the NixOS/patchelf
    GitHub repository).
2.  Then, open a terminal, and navigate to your Stardew Valley root
    folder.
3.  Run `patchelf --clear-execstack libGalaxy64.so`.
4.  Then run `patchelf --clear-execstack libGalaxyCSharpGlue.so`.

The issue should be fixed now.

## Can't connect to another player in multiplayer

1.  Check your game setup:
    1.  Make sure you have the latest Stardew Valley version ( on PC).
    2.  Make sure the host (main player) is in co-op mode. They need to
        click the *Co-op* button on the title screen, and launch the
        save by clicking "Host (farmname) Farm". Loading a save through
        the regular load game menu, even if cabins have been built, will
        launch it in single-player mode.
    3.  Make sure you have enough cabins built for the number of
        players.
    4.  Make sure the server is set to online in the game options.
    5.  <a href="#Reset_your_content_files" class="wikilink"
        title="Reset the content files for all players">Reset the content files
        for all players</a>.
    6.  Delete your `startup_preferences` (found in
        `%appdata%/StardewValley` on Windows or
        `~/.config/StardewValley` on Linux/Mac).
2.  Make sure everyone launches the game through Steam or GOG Galaxy
    (not a separate shortcut). For SMAPI on Windows, see
    <a href="Modding_Installing_SMAPI_on_Windows#Configure_your_game_client"
    class="wikilink"
    title="Configure your game client in the Windows install guide"><em>Configure
    your game client</em> in the Windows install guide</a>.
3.  Turn off firewalls and antiviruses for all players. If you have more
    than one antivirus, that's very likely the cause. Never use more
    than one antivirus at a time.
4.  Restart all players' PCs.
5.  Restart all players' routers, and check for any [updates for your
    router](https://www.wikihow.com/Update-Router-Firmware).
6.  If you don't see the 'enter invite code' option, your Steam name may
    have been flagged as inappropriate. Try changing it and re-launching
    the game.
7.  (Windows only) <a href="#Game_doesn&#39;t_launch" class="wikilink"
    title="Check the debugging steps under Game doesn&#39;t launch">Check
    the debugging steps under <em>Game doesn't launch</em></a>.
8.  If you use mods and are getting a "version mismatch" error, check
    your log files for a line like
    `[19:49:26 TRACE game] Starting server. Protocol version:` and check
    whether the protocol version matches.

For console players, please try all of the steps that apply
(particularly the first four under 'check your game setup') and try
[power
cycling](https://edu.gcfglobal.org/en/basic-computer-skills/how-to-power-cycle-a-device/1/)
your console. Please note that all consoles require their paid online
service to play over the internet.

## SMAPI doesn't recognize controller (Steam only)

Common fixes:

1.  Launch the game through Steam.
2.  Windows only: make sure you set the launch options (see
    <a href="Modding_Installing_SMAPI_on_Windows#Configure_your_game_client"
    class="wikilink"
    title="Configure your game client in the Windows install guide"><em>Configure
    your game client</em> in the Windows install guide</a>).
3.  If all else fails, you can use third-party software to add
    controller support. Suggested software:
    - Linux: .
    - Mac: . When using a non-Xbox controller, you should [enable
      'pretend to be an Xbox 360
      controller'](https://community.playstarbound.com/threads/guide-best-working-controllers-how-to-set-up-on-mac-osx.148008/).
      (In some cases, you may need to enable it even for an Xbox
      controller.)
    - Windows: [reWASD](https://www.rewasd.com/) (not free after trial
      period) or [InputMapper](https://inputmapper.download/) (free but
      more complicated) to remap your controller as an Xbox controller.

## Cursor gets stuck on museum or build screen

When placing items in the museum or placing buildings on the farm, the
cursor gets stuck in one spot and snaps back whenever you try to move
it.

That happens when the game doesn't detect the gamepad mode correctly. To
fix it:

1.  Load your save.
2.  Open the in-game menu and go to the options.
3.  Set the *Gamepad Mode* option to either *Force On* (if you use a
    controller) or *Force Off* (if you use a keyboard and mouse).

## Pet event repeating over and over

You probably have a pet named the same thing as an NPC in the game, most
likely a modded NPC (both reported instances have been Stardew Valley
Expanded NPC names). Save editing to remove your pet may help, but is
tricky and difficult. Narrowing down the cause of this issue has been
somewhat difficult. You can try naming the pet something other than the
name of an NPC, or rejecting the pet, and see if that helps, but you may
end up with multiple pets.

# Other issues with the SMAPI installer

## SMAPI installer opens, then immediately closes

Q: The installer opens for a second, then immediately closes.

A: Make sure you’re installing SMAPI 3.13.1 or later, which fixed an
issue with path names. If you are, try whitelisting the SMAPI installer
with your antivirus, and redownload, as your SMAPI installer may have
been mangled by your antivirus. If that still doesn’t work try these
steps:

1.  Open the installer folder.
2.  Hold shift and right-click on the folder background.
3.  Click the option that says Open in command prompt / PowerShell /
    Windows Terminal (depending on your Windows settings).
4.  Run `"install on Windows.bat"` (if Command Prompt) or
    `./"install on Windows.bat"` (if PowerShell or Windows Terminal).
5.  Now if it crashes, the window should stay open so you can see the
    error.
6.  Post a screenshot of the full window when it shows the error in the
    \#using-mods discord channel for debugging help.

# Known issues

## SMAPI doesn't work with the compatibility branch

What is the compatibility branch?
There's two versions of Stardew Valley : the newer 64-bit *main branch*
which is installed by default, and a legacy 32-bit [*compatibility
branch* for older systems](https://www.stardewvalley.net/compatibility).
These have identical content for players, but <a
href="Modding_Migrate_to_Stardew_Valley_1.5.5#Game_compatibility_branch"
class="wikilink" title="use different frameworks">use different
frameworks</a>.

<!-- -->

Why don't mods work with it?
Unfortunately SMAPI only supports the main branch of the game currently.
There are formidable difficulties across all mods in supporting all
three variations, 32-bit imposes significant restrictions on what mods
can do, and the [Steam hardware
stats](https://store.steampowered.com/hwsurvey) show that ≈99.69% of
players have 64-bit.

<!-- -->


Having multiple versions of SMAPI (like we do for Linux/macOS/Windows
compatibility) wouldn't be enough in this case. Every C# mod author
would need to manually port two versions of every update of every mod
forever, which is prohibitively unfeasible. It's possible that in the
future we'll either figure out how SMAPI can automatically rewrite mods
for the compatibility branch, or some modders may port SMAPI and
individual mods to the compatibility branch.

<!-- -->

How can I play if I can't update to the latest versions?
You have a few options.

1.  First, make sure you really can't update. Over 99% of systems should
    be compatible with the main branch; it's only very old system that
    are 32-bit-only or use unsupported graphics cards that might not
    work.
2.  *Or* you can switch to the game's compatibility branch without mods.
    Mods don't work with it currently, but it'll continue receiving the
    same content updates backported to the older frameworks for players
    with older systems.
3.  *Or* you can rollback to the previous Stardew Valley 1.5.4, so you
    can continue playing like before. The newest mod updates won't work
    for you, but you'll be able to install any mod updates up to 29
    November 2021. If (or when) we figure out how to make mods work with
    the compatibility branch in the future, then you'd be able to switch
    to the compatibility branch instead.
    If you want to rollback to Stardew Valley 1.5.4, here's how:


    Please note this only works on the **Steam** version of the game!

    1.  Install [.NET 5 or
        later](https://dotnet.microsoft.com/download/dotnet).
    2.  Download the latest \[ DepotDownloader\] release.
    3.  Open a command prompt in the DepotDownloader folder.
    4.  Run this command (replace `<username>` and `<password>` with
        your Steam login):
            dotnet DepotDownloader.dll -app 413150 -depot 413151 -manifest 7802000804251603756 -username <username> -password <password>
    5.  Install SMAPI in the downloaded folder and move your mods over.
    6.  Launch `StardewModdingAPI.exe` in the downloaded folder.
4.  *Or* use a tool called DepotDLGUI designed to download 1.5.4 more
    easily using \[ DepotDownloader\].

    Please note this only works on the **Steam** version of the game!

    1.  Install [.NET
        5](https://dotnet.microsoft.com/en-us/download/dotnet/5.0).
    2.  Download the latest release of \[ DepotDLGui\]. (Green Price Tag
        on the right side of the screen, under the word Releases)
    3.  Unzip the file you just downloaded.
    4.  Run `DepotDLGUI_cs.exe`
    5.  Install SMAPI in the downloaded folder
        (`depots\413151\8043676`)and move your mods over.
    6.  Launch `StardewModdingAPI.exe` in the downloaded folder.

# Get help

## Report a bug

If you play *without* mods
See [this guide to fixing your
game](https://steamcommunity.com/app/413150/discussions/0/142261352650065356/).
If you still need help,
<a href="#Ask_for_help" class="wikilink" title="ask for help">ask for
help</a>.

<!-- -->

If you play *with* mods
First, check whether it happens without mods too:

1.  Open
    <a href="Modding_Player_Guide_Getting_Started#Find_your_game_folder"
    class="wikilink" title="your game folder">your game folder</a>.
2.  Double-click (on Windows) or `StardewValley-original` (on
    Linux/macOS) to launch the game.

<!-- -->


If it only happens *with* mods installed,
<a href="#Ask_for_help" class="wikilink" title="ask for help">ask for
help</a>. Otherwise see **If you play without mods** above.

## Ask for help

See <a href="Modding_Help" class="wikilink"
title="Modding:Help">Modding:Help</a> for how to get help!

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="de_Modding_Spieleranleitung_Problembehebung" class="wikilink"
title="de:Modding:Spieleranleitung/Problembehebung">de:Modding:Spieleranleitung/Problembehebung</a>
<a href="es_Modding_Guía_del_jugador_Solución_de_problemas"
class="wikilink"
title="es:Modding:Guía del jugador/Solución de problemas">es:Modding:Guía
del jugador/Solución de problemas</a> <a
href="ru_Модификации_Руководство_по_использованию_модификаций_Устранение_неполадок"
class="wikilink"
title="ru:Модификации:Руководство по использованию модификаций/Устранение неполадок">ru:Модификации:Руководство
по использованию модификаций/Устранение неполадок</a>
<a href="tr_Modlama_Oyuncu_Rehberi_Sorun_Giderme" class="wikilink"
title="tr:Modlama:Oyuncu Rehberi/Sorun Giderme">tr:Modlama:Oyuncu
Rehberi/Sorun Giderme</a>
<a href="zh_模组_使用指南_疑难解答" class="wikilink"
title="zh:模组:使用指南/疑难解答">zh:模组:使用指南/疑难解答</a>

[^1]:
