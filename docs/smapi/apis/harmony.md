---
title: "Harmony"
wiki_source: "Modding:Modder Guide/APIs/Harmony"
permalink: /Modding:Modder_Guide/APIs/Harmony/
category: smapi
tags: [harmony, when-to-use-harmony, how-to-use-it, best-practices, faqs, which-version-of-harmony-should-i-use, why-should-i-avoid-harmony-annotations-and-patchall, what-is-inlining-and-why-does-it-matter]
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

`lets you patch or replace methods, effectively rewriting the game code. SMAPI includes a copy of Harmony for mods to use.`

## When to use Harmony

**Harmony should be a last resort.** It's a powerful tool that lets you
do things that may be harder otherwise, but it comes with significant
disadvantages:

- It's very easy to cause crashes, errors, or subtle bugs, including
  difficult-to-diagnose memory corruption errors.
- SMAPI often can't detect incompatible Harmony code.
- SMAPI often can't rewrite Harmony patches for compatibility, so the
  mod may break on other platforms (e.g. Android) or in future game
  updates.
- Patches may conflict with other Harmony mods, sometimes in ways that
  are difficult to troubleshoot.
- Patches may have unpredictable effects on other mods that aren't using
  Harmony. That may also irritate other modders, if players often report
  bugs to other mods due to your patches.
- Patches may prevent you from attaching a debugger when testing (even
  when you're testing unrelated code).
- If someone else's mod calls code you patched and that code crashes,
  the error will be logged under their mod's name (unless you handle
  errors). This can cause players to report bugs to other authors, which
  can be irritating if they know it's due to your mod.
- SMAPI will show a warning when your mod is loaded saying it may affect
  game stability.

You should only use Harmony if you're sure what you want isn't feasible
without it. For example: instead of patching logic that handles player
interaction, you can detect and suppress the interaction using
<a href="Modding_Modder_Guide_APIs_Input" class="wikilink"
title="SMAPI&#39;s input API">SMAPI's input API</a>, and run your own
code to handle it.

## How to use it

**Harmony should be a last resort** (see the previous section).

1.  Edit your mod's `.csproj` project file, and add this to the first
    `<PropertyGroup>` section:
    ``` xml
    <EnableHarmony>true</EnableHarmony>
    ```
2.  In your mod's `Entry` method, use Harmony's code API to register
    patches:
    ``` c#
    var harmony = new Harmony(this.ModManifest.UniqueID);

    // example patch, you'll need to edit this for your patch
    harmony.Patch(
       original: AccessTools.Method(typeof(StardewValley.Object), nameof(StardewValley.Object.canBePlacedHere)),
       prefix: new HarmonyMethod(typeof(ObjectPatches), nameof(ObjectPatches.CanBePlacedHere_Prefix))
    );
    ```
3.  See the [Harmony tutorials and
    documentation](https://harmony.pardeike.net/). Additionally, you can
    check out some Stardew-specific examples on the [Modding
    wiki](https://stardewmodding.wiki.gg/wiki/Tutorial:_Harmony_Patching).

## Best practices

1.  See <a href="#When_to_use_Harmony" class="wikilink"
    title="when to use Harmony">when to use Harmony</a>.
2.  Unhandled errors in a patch can be hard to troubleshoot, which often
    leads to players asking for help on the page for SMAPI or someone
    else's mod. **Please** handle errors, log them, and default to the
    original code. For example:
    ``` C#
    internal class ObjectPatches
    {
        private static IMonitor Monitor;

        // call this method from your Entry class
        internal static void Initialize(IMonitor monitor)
        {
            Monitor = monitor;
        }

        // patches need to be static!
        internal static bool CanBePlacedHere_Prefix(StardewValley.Object __instance, GameLocation location, Vector2 tile, ref bool __result)
        {
            try
            {
                ...; // your patch logic here
                return false; // don't run original logic
            }
            catch (Exception ex)
            {
                Monitor.Log($"Failed in {nameof(CanBePlacedHere_Prefix)}:\n{ex}", LogLevel.Error);
                return true; // run original logic
            }
        }
    }
    ```
3.  Use postfixes when possible for best compatibility and stability.
4.  Don't use transpile patches unless you have no choice and you know
    what you're doing. This has a much higher chance of causing issues,
    is more fragile and likely to break in game updates, and makes it
    much less likely that other modders can help if you need it.
5.  <a href="#How_to_use_it" class="wikilink" title="Use the code API">Use
    the code API</a> instead of annotations like `[HarmonyPatch]` (see
    *<a href="#Why_should_I_avoid_Harmony_annotations_and_PatchAll?"
    class="wikilink"
    title="Why should I avoid Harmony annotations and PatchAll?">Why should
    I avoid Harmony annotations and <samp>PatchAll</samp>?</a>*).

## FAQs

### Which version of Harmony should I use?

The Harmony version is managed by SMAPI (currently 2.2.*x*). If you
<a href="#How_to_use_it" class="wikilink"
title="use the EnableHarmony option">use the <samp>EnableHarmony</samp>
option</a>, you'll use the version bundled with SMAPI automatically.

### Why should I avoid Harmony annotations and `PatchAll`?

There are two ways to add patches:

- <a href="#How_to_use_it" class="wikilink" title="Use the code API">Use
  the code API</a> (recommended).
- Use annotations like `[HarmonyPatch]` on static classes, then call
  Harmony's `PatchAll` to dynamically scan the assembly for those
  annotations. This is fragile and discouraged.

For context, SMAPI automatically rewrites mods when needed for
compatibility. That's used to keep mods working when there are breaking
changes in the game/SMAPI/Harmony, or to handle crossplatform
differences (e.g. using PC mods on Android). For example, the Stardew
Valley 1.5.5 update broke most C# mods, but nearly all of them were
fixed automatically by SMAPI's rewriting.

However annotations work differently in the compiled code, so SMAPI
can't rewrite them. That means mods which use annotations are more
fragile; they may break without warning in future game/SMAPI/Harmony
updates, and may not work on some platforms.

### What is inlining and why does it matter?

[Inlining](https://en.wikipedia.org/wiki/Inline_expansion) is when the
JIT takes a method call and sticks the body of the method called instead
of emitting an actual call. If this happens, a harmony patch applied to
the callee will not take effect.

The heuristics the JIT uses to decide whether or not to inline a method
are not documented and are subject to change, but [small, simple methods
that do not throw
exceptions](https://stackoverflow.com/a/31467000/19366602) are the most
likely to be inlined. Additionally, the heuristic seems to change
between platform and platform, with mac being more aggressive than
Windows.

<a href="ru_Модификации_Руководство_мододела_API_Harmony"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Harmony">ru:Модификации:Руководство
мододела/API/Harmony</a>
<a href="zh_模组_制作指南_APIs_Harmony" class="wikilink"
title="zh:模组:制作指南/APIs/Harmony">zh:模组:制作指南/APIs/Harmony</a>
