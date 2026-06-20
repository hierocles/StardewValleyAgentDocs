---
title: "Migrate Harmony 2"
wiki_source: "Modding:Migrate to Harmony 2.0"
permalink: /Modding:Migrate_to_Harmony_2.0/
category: smapi
tags: [migrate-to-harmony-2-0, overview, what-s-changing, is-this-the-modapocalypse, how-to-update-your-mod, breaking-changes, api-changes, stricter-validation]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

SMAPI 3.12 updates from Harmony 1.2.0.1 to Harmony 2.1. That only
affects mods which use Harmony directly; that's
<a href="Modding_Modder_Guide_APIs_Harmony" class="wikilink"
title="discouraged in most cases">discouraged in most cases</a>, isn't
officially part of SMAPI's public API, and isn't subject to SMAPI's
normal versioning policy. If you use Harmony in your mods, this page
explains how the update affects them.

## Overview

### What's changing?

[Harmony 2.0](https://github.com/pardeike/Harmony/releases/tag/v2.0.0)
and [2.1](https://github.com/pardeike/Harmony/releases/tag/v2.1.0.0)
have many changes that benefit SMAPI and mods. Some notable changes:

- Added
  [finalizers](https://harmony.pardeike.net/articles/patching-finalizer.html)
  and [reverse
  patches](https://harmony.pardeike.net/articles/reverse-patching.html).
- Added [pass-through
  postfixes](https://harmony.pardeike.net/articles/patching-postfix.html).
- Added
  [`Manipulator`](https://harmony.pardeike.net/api/HarmonyLib.Transpilers.html)
  utility, `CodeInstruction` extensions, and other improvements for
  transpilers.
- Added more `AccessTools.Is*` methods.
- Added support for .NET 5.
- Transpilers can now default to the original input by returning `null`.
- Improved compatibility with Android modding.
- Improved exception messages.
- Improved validation for invalid patches.
- Fixed cases where methods were inlined and unpatchable on Linux/Mac.
- Fixed methods with struct return types being unpatchable.
- Various other improvements and fixes; see the [Harmony 2.0 release
  notes](https://github.com/pardeike/Harmony/releases/tag/v2.0.0),
  [Harmony 2.1 release
  notes](https://github.com/pardeike/Harmony/releases/tag/v2.1.0.0), and
  [new Harmony documentation](https://harmony.pardeike.net) for more
  info.

After waiting over a year to make sure the release is stable, SMAPI is
transitioning to Harmony 2.1.

### Is this the modapocalypse?

Nope. Although this is a major change, significant efforts were
undertaken to minimise the impact:

- mods which don't use Harmony directly aren't affected;
- most mods are rewritten automatically for compatibility, so they'll
  work without an update;
- pull requests were submitted to update affected open-source mods;
- unofficial updates were created as needed for mods which hadn't
  updated officially;
- the changes were actively communicated and documented to modders.

In addition, the target was *at least* 90% compatibility for open-source
mods before SMAPI migrates. All of this means that the release should
have minimal impact on mod compatibility, despite the scope of the
changes.

### How to update your mod

1.  Make sure you follow best practices outlined in the
    <a href="Modding_Modder_Guide_APIs_Harmony" class="wikilink"
    title="Harmony guide">Harmony guide</a>. In particular, use the
    `EnableHarmony` option (don't reference the Harmony DLL directly).
2.  Change `using Harmony;` to `using HarmonyLib;`.
3.  Change
    `HarmonyInstance harmony = HarmonyInstance.Create("your mod id");`
    to `Harmony harmony = new Harmony("your mod id");`.
4.  Check if any <a href="#Breaking_changes" class="wikilink"
    title="breaking changes">breaking changes</a> listed below apply to
    your mod.
5.  Recompile the mod.

## Breaking changes

### API changes

See *<a href="#How_to_update_your_mod" class="wikilink"
title="how to update your mod">how to update your mod</a>*.

### Stricter validation

Harmony 2.x has stricter validation in general, so invalid patches that
would previously somewhat work (*e.g.,* setting `__result` to the wrong
type) will now cause errors. See the exception messages for help fixing
these.

### Patching static constructors

The `AccessTools` methods for constructors (`Constructor`,
`DeclaredConstructor`, and `GetDeclaredConstructors`) no longer match
static constructors by default. Use the new `searchForStatic` argument
if you need to match them:

``` c#
// match static constructors only
var method = AccessTools.Constructor(typeof(ExampleType), searchForStatic: true);

// match static *or* instance constructors
var method =
   AccessTools.Constructor(typeof(ExampleType), searchForStatic: true)
   ?? AccessTools.Constructor(typeof(ExampleType));
```

Note that Harmony no longer matches static constructors for a good
reason — they're only called once for the type, so often static
constructor patches won't work correctly.

### Patching virtual methods

When patching a virtual method, you must now patch the specific type
which implements it. Patching the wrong type now results in the error
"*You can only patch implemented methods/constructors*".

For example, consider this code:

``` c#
public class GameLocation
{
   public virtual void cleanupBeforePlayerExit() {}
}

public class Farm : GameLocation {}
```

`Farm.cleanupBeforePlayerExit` doesn't exist, so it's inherited from
`GameLocation`. Harmony 1.x would let you patch
`Farm.cleanupBeforePlayerExit`, but in Harmony 2.x you must target the
actual method (`GameLocation.cleanupBeforePlayerExit` in this example).

### `HarmonyMethod` no longer allows null

Harmony 1.x allowed `new HarmonyMethod(null)`, so you could safely use
it with methods that might not exist. Harmony 2.x now throws an
exception in that case, so you should check if you're not sure it
exists:

``` c#
MethodInfo prefix = AccessTools.Method(this.GetType(), "Prefix");
if (prefix != null)
   harmony.Patch(original, new HarmonyMethod(prefix));
```

### Transpiler changes

Harmony 2.x uses a new engine () under the hood, so there may be
unexpected changes in the way transpiler patches work. For example,
short-form branches may become long-form. If your mod uses transpilers,
you should test each one to make sure it's working as you expect.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="zh_模组_迁移至Harmony_2.0" class="wikilink"
title="zh:模组:迁移至Harmony 2.0">zh:模组:迁移至Harmony 2.0</a>
