---
title: "Integrations"
wiki_source: "Modding:Modder Guide/APIs/Integrations"
permalink: /Modding:Modder_Guide/APIs/Integrations/
category: smapi
tags: [integrations, dependencies, mod-registry, mod-provided-apis, providing-an-api, using-an-api, known-limitations, message-sending]
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

A *mod integration* refers to two mods communicating or cooperating in
some way. SMAPI provides a few features to support this.

## Dependencies

You can define dependencies in your `manifest.json` file, which are
other mods that must be loaded before yours. If the dependency is
required and missing, SMAPI will show a friendly error to the player.
See <a href="Modding_Modder_Guide_APIs_Manifest" class="wikilink"
title="the manifest page">the manifest page</a> for more info.

## Mod registry

Your mod can get information about loaded mods, or check if a particular
mod is loaded. (All mods are loaded by the time your mod's `Entry(…)`
method is called.)

``` c#
// check if a mod is loaded
bool isLoaded = this.Helper.ModRegistry.IsLoaded("UniqueModID");

// get info for a mod
IModInfo mod = this.Helper.ModRegistry.Get("UniqueModID");
bool isContentPack = mod.IsContentPack;
IManifest manifest = mod.Manifest; // name, description, version, etc

// get info for all loaded mods
foreach(IModInfo mod in this.Helper.ModRegistry.GetAll()) { … }
```

## Mod-provided APIs

Mods can provide their own APIs to other mods, even without a dependency
or assembly reference. This can be used to integrate mods, provide
custom information, or provide new framework APIs beyond those offered
by SMAPI itself.

### Providing an API

To provide an API for other mods to use:

1.  Add a normal class to your mod project with the methods and
    properties you want to expose.
    ``` c#
    public class YourModApi
    {
        public string ExampleProperty { get; set; } = "Example value";

        public bool GetThing(string example)
        {
           return true;
        }
    }
    ```

    (You can use a
    [constructor](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/constructors)
    to initialise the API if desired.)
2.  Override `GetApi` in your mod's entry class and return an instance
    of your API. You can choose between two versions of this method:
    - Override `GetApi()` to provide one instance of the API to all
      mods. This will only be called once, and SMAPI will cache the mod
      instance.
      ``` c#
         public override object GetApi()
         {
            return new YourModApi();
         }
      ```
    - *Or* Override `GetApi(IModInfo mod)` to provide one instance per
      mod. This will be called once for each mod that requests an API.
      Note that this info is provided for informational purposes only
      (e.g. to log errors). Denying API access to specific mods is
      strongly discouraged and may be considered abusive.

      ``` c#
         public override object GetApi(IModInfo mod)
         {
            return new YourModApi(mod.Manifest);
         }
      ```

That's it! SMAPI will get one instance of your API and cache it.

Notes:

- `GetApi` is always called after `Entry`, so it's safe to pass in your
  mod's initialised fields.
- Be careful when changing your API! If you make a breaking change,
  other mods may need an update before they can access your API again.
- You can optionally add a public
  [interface](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/interface)
  to your API. If a mod directly references your mod DLL, they'll be
  able to use your interface instead of creating their own.

### Using an API

You can use a mod-provided API by mapping it to an
[interface](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/interface):

1.  Create an interface with only the properties and methods you want to
    access. This interface must be public and cannot be an inner
    interface. (If you directly reference the mod DLL and it provides a
    public API interface, you can use that instead.)
    ``` C#
    public interface ISomeModApi
    {
       bool GetThing(string example);
    }
    ```
2.  In your mod code (after `Entry`), you can get the API by specifying
    the interface you created in step 1, and the
    <a href="Modding_Modder_Guide_APIs_Manifest#Basic_fields"
    class="wikilink" title="mod&#39;s unique ID">mod's unique ID</a>:
    ``` c#
    ISomeModApi api = helper.ModRegistry.GetApi<ISomeModApi>("other-mod-ID");
    if (api != null)
       bool result = api.GetThing("boop");
    ```

For a quick integration, you can also use reflection instead of creating
an interface:

``` c#
object api = helper.ModRegistry.GetApi("other-mod-id");
if (api != null)
   bool result = helper.Reflection.GetMethod(api, "GetThing").Invoke<bool>("boop");
```

Notes:

- You can't call `GetApi` until all mods are initialised and their
  `Entry` methods called. You can use the `GameLoop.GameLaunched`
  <a href="#Events" class="wikilink" title="event">event</a> if you need
  to access mod APIs early; this is guaranteed to happen after all mods
  are initialised.
- You should always null-check APIs you consume. `GetApi` will return
  `null` if the API isn't available (*e.g.,* because the mod isn't
  already installed or doesn't have one). If <samp>GetAPi\</smap\>
  cannot map an API, it will throw an exception.
- Keep in mind that mods may change their API interfaces over time; it
  may be useful to check the version of the other mod before trying to
  map the interface.

### Known limitations

- When providing an API, the interface and implementation must be
  public.

## Message sending

You can send messages using
<a href="Modding_Modder_Guide_APIs_Multiplayer" class="wikilink"
title="the multiplayer API">the multiplayer API</a>, with a destination
ranging from very narrow (*e.g.,* one mod on one connected computer) to
very broad (all mods on all computers). Messages can also be sent to the
current computer, *e.g.,* to communicate between two mods. This can be
used for a variety of integrations.

For example:

- Request something from a host mod. (Tractor Mod uses this to summon a
  tractor to the current player in multiplayer, even if the tractor
  isn't in a location synced to that player.)
- Notify another mod about something. (Chests Anywhere uses this to
  notify Automate when a chest's automation options are edited.)

## Shared assembly reference

*NOTE*: This is not a SMAPI feature, but this is documented here since
it is also a common pattern for providing mod integration.

You can add a reference to a mod's assembly in your `csproj` and
directly import its namespaces and functions into your mod code. Note
that this should only be attempted if what you want isn't available
through the mod's public API, or if this is the target mod's intended
method of exposing its own. This would also make said mod a hard
dependency for your own mod.

For example, this snippet adds an assembly reference to Content
Patcher's assembly in your mod code under the `ContentPatcher`
namespace, without also including `ContentPatcher.dll` in your mod
build:

``` xml
<ItemGroup>
    <Reference Include="ContentPatcher" HintPath="$(GamePath)\Mods\ContentPatcher\ContentPatcher.dll" Private="false" />
</ItemGroup>
```

Make sure the path to `ContentPatcher.dll` is correct on your own
installation.

<a href="ru_Модификации_Руководство_мододела_API_Интеграции"
class="wikilink"
title="ru:Модификации:Руководство мододела/API/Интеграции">ru:Модификации:Руководство
мододела/API/Интеграции</a>
<a href="zh_模组_制作指南_APIs_Integrations" class="wikilink"
title="zh:模组:制作指南/APIs/Integrations">zh:模组:制作指南/APIs/Integrations</a>
