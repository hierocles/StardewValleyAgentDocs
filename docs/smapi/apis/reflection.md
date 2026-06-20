---
title: "Reflection"
wiki_source: "Modding:Modder Guide/APIs/Reflection"
permalink: /Modding:Modder_Guide/APIs/Reflection/
category: smapi
tags: [reflection, intro, basic-reflection, overview, fields-and-properties, methods, advanced-reflection]
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

The reflection API lets you access fields, properties, or methods you
otherwise couldn't access. You can use it from `helper.Reflection` in
your entry method, or `this.Helper.Reflection` elsewhere in your entry
class.

## Intro

[*Reflection*](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection)
is a powerful C# feature which lets code analyse and interact with code.
SMAPI provides a simplified reflection API focused on accessing private
game fields, properties, and methods. SMAPI will automatically handle
validation, caching, and performance optimisation.

## Basic reflection

### Overview

SMAPI provides three overloaded methods to access code: `GetField`,
`GetProperty`, and `GetMethod`. Each one takes three arguments:

| argument | purpose |
|----|----|
| `obj` or `type` | The instance (or type if static) which has the private field/property/method you want to access. |
| `name` | The name of the private field/property/method. |
| `required` | Whether to throw a descriptive exception if the field/property/method isn't found. Default true. If set to false, it will return `null` instead and you should validate it yourself. |

Each method returns an object you can use to interact further with it —
like getting or setting the field/property value, or invoking the
method.

### Fields and properties

`GetField` and `GetProperty` are used the same way. Both return an
object with two methods: `GetValue` returns the current field/property
value, and `SetValue` overrides their value.

You can get the value directly:

``` c#
// get value of instance field
bool wasPet = this.Helper.Reflection.GetField<bool>(pet, "wasPetToday").GetValue();
```

Or you can keep a reference to the reflection data, and change the value
separately:

``` c#
// set value of static field
IReflectedField<int> soundTimer = this.Helper.Reflection.GetField<int>(typeof(Junimo), "soundTimer");
soundTimer.SetValue(100);
```

If you need to access the field/property repeatedly, keeping the
reflection object will improve performance.

### Methods

`GetMethod` returns an object with one overloaded method. The `Invoke`
comes in two forms:

- `Invoke()` calls a method with no return value.
- `Invoke<T>()` calls a method which returns a value, where `T` is the
  expected return type.

For example, this calls the private `TV.getFortuneForecast` method and
stores the value it returns:

``` c#
string forecast = this.Helper.Reflection
   .GetMethod(new TV(), "getFortuneForecast")
   .Invoke<string>();
```

If the method expects arguments, you can just add those to the `Invoke`
method:

``` c#
Vector2 spawnTile = new Vector2(25, 25);
this.helper.Reflection
   .GetMethod(Game1.getFarm(), "doSpawnCrow")
   .Invoke(spawnTile);
```

## Advanced reflection

If you need to do more, you can access the underlying C# reflection
types:

``` c#
FieldInfo field = this.Helper.Reflection.GetField<string>(…).FieldInfo;
MethodInfo method = this.Helper.Reflection.GetMethod(…).MethodInfo;
```

Or even use [C#
reflection](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection)
directly. Note that SMAPI adds caching and optimisations which you'll
need to handle yourself if you do this.

<a href="ru_Модификации_Руководство_мододела_API_Рефлексия"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Рефлексия">ru:Модификации:Руководство
мододела/API/Рефлексия</a>
<a href="zh_模组_制作指南_APIs_Reflection" class="wikilink"
title="zh:模组:制作指南/APIs/Reflection">zh:模组:制作指南/APIs/Reflection</a>
