---
title: "Open Source"
wiki_source: "Modding:Open source"
permalink: /Modding:Open_source/
category: smapi
tags: [open-source, why-is-open-source-important, common-questions, make-your-code-open-source, if-your-code-is-already-on-github, if-your-code-isn-t-on-github, see-also]
---
←<a href="Modding_Index" class="wikilink" title="Index">Index</a>

A mod is **open-source** if its code is public and covered by [an
open-source license](https://choosealicense.com/). Modders are strongly
encouraged to make their mods and content packs open-source.

## Why is open source important?

Open source is important for the long-term health of the modding
community, and helps make the player experience smoother.

How it benefits others
Depending on the open-source license you choose, others can...

:\* see your code;

:\* make changes to a copy of the code;

:\* send you proposed updates, changes, and fixes;

:\* prepare unofficial updates;

:\* better help users with support questions by looking at the code.


The effect can be significant: only 1% of open-source mods broke when
SMAPI 3.0 released, compared to **51%** of closed-source mods (and that
doesn't count closed-source mods that were never updated for earlier
game/SMAPI releases).

<!-- -->

How it benefits you
Besides the above benefits, a license is very important if you'll accept
contributions from others.

<!-- -->


*Without* a license, contributors have a copyright for changes they make
to your mod (like code, translation, or content changes). By
contributing to your mod, they're implicitly giving you permission to
use the content/changes in the way they're currently used. But since you
no longer own the entire mod, you can't change how they're published
(e.g. splitting the mod into smaller components, copying code into
another mod, etc) without getting permission from each past contributor.
And if some of those contributors can't be reached, you're out of luck
unless you strip their contributions out of the mod entirely.

<!-- -->


*With* a license, any contributions are automatically covered by the
license too. That means you can do anything with the contributions that
the license allows.

## Common questions

What if I don't like a proposed change?
You still have full control of your original code and mod pages; nobody
can change those without your approval! You're free to reject a change
someone proposes to your mod.

<!-- -->

Does this apply for content packs?
Yep! Content packs aren't compiled, but other modders can't legally make
changes without a code license. Note that 'permissions' options on sites
like Nexus are legally iffy (*e.g.,* who has copyright on derivatives?
Can derivatives be relicensed?), so it's a good idea to have a code
license for content packs too. That also lets other modders contribute
pull requests and updates. When this page says 'code', it means
everything in your content pack including JSON files, images, maps, etc.

<!-- -->

Can I prevent commercial use?
A non-commercial license prevents others from profiting from or
reselling the content. It's certainly better than no license at all, but
it's *not* open-source. This can have unintended side-effects like
preventing streamers from showing your mods because their videos are
monetized. Avoiding non-commercial licenses is strongly recommended.

<!-- -->

I already released the mod without a license. Can I add a license now?
Yes. If you created the entire mod yourself, you can add or change the
license anytime. If others contributed to the mod (including code,
translations, or images), you'll need to either get permission from each
contributor to relicense their contributions, or strip their changes out
of the mod.

<!-- -->

What is a Git repository?
Git is software that helps track changes to your code, and a repository
is a folder containing your mod files with Git tracking. You can look up
Git tutorials if you want to know more, but don't worry: you don't need
to know how it works to use it!

## Make your code open-source

### If your code is already on GitHub

You're already almost done! You just need to [choose an open-source
license](https://choosealicense.com/) (MIT License is a good choice if
you're undecided), and [add a `LICENSE` file to the
repository](https://help.github.com/en/github/building-a-strong-community/adding-a-license-to-a-repository).

### If your code isn't on GitHub

This looks like a lot of steps, but don't worry: it's pretty
straightforward, and you only need to do it once. If you need help, come
ask in <a href="Modding_Community#Discord" class="wikilink"
title="#making-mods on the Stardew Valley Discord">#making-mods on the
Stardew Valley Discord</a>. :)

#### Via VisualStudio

Visual Studio has a pretty good git integration, documented here:
<https://learn.microsoft.com/en-us/visualstudio/version-control/git-create-repository?view=vs-2022>

#### Via SourceTree

<dl>

<dt>

Create a Git repository

</dt>

<dd>

First, let's create the public repository which will contain your code.

1.  Create a [GitHub](https://github.com/) account.
2.  Install [SourceTree](https://www.sourcetreeapp.com/) (Mac/Windows)
    or [GitKraken](https://www.gitkraken.com/) (Linux). When asked, link
    it to your GitHub account.
3.  [Create the repository on
    GitHub](https://help.github.com/articles/create-a-repo/).
    Suggested settings (see
    <a href="_File_Modding_-_create_GitHub_repo.png" class="wikilink"
    title="screenshot">screenshot</a>):

    1.  Repository name: consider *StardewMods* if you'll put all your
        mods in the same repository, otherwise use the name of your mod.
    2.  Description: consider *Mods for Stardew Valley.*
    3.  Initialize ... with a README: enable this option.
    4.  Add `.gitignore`: leave this blank; we'll add our own later.
    5.  Add a license: [choose a license](https://choosealicense.com/)
        (MIT License is a good choice if you're undecided), and select
        it here.
    6.  Click 'Create repository'.
4.  On the repository page that appears, click the green "Clone or
    download" button and copy the URL:\
    <a href="File_Modding_-_copy_GitHub_repo_URL.png" class="wikilink"
    title="File:Modding - copy GitHub repo URL.png"><span>File:Modding</span>
    - copy GitHub repo URL.png</a>
5.  In SourceTree, click *File \> Clone* and paste the URL. Choose a
    destination path that's easy to access (like
    `C:\source\StardewMods`), and click 'Clone'.
6.  After cloning, navigate to repo settings (gear icon, top right)
7.  Click "Remotes" section
8.  Highlight the git path
9.  Click "edit" button
10. Click on the globe icon to the right of the URL/path
11. Highlight the project name
12. Click "edit accounts" button
13. Double-click on the Github account. An auth window will pop up
14. The default auth method is set to OAuth. Change to "Personal Access
    Token."
15. Input username and token
16. If not already selected, make sure Protocol is set to "HTTPS" and
    Save.

That's the hard part done! Now you have a repository on GitHub that's
synced with the folder on your computer.

</dd>

<dt>

Add the mod files

</dt>

<dd>

Next, let's add your files to the repository.

1.  Open the repository folder (the destination path you entered in step
    5 above).
2.  Unzip [this zip
    file](https://github.com/StardewModders/Files/raw/master/template%20repo/gitattributes%20and%20gitignore.zip)
    into the folder. This will add two files to the root of your folder:
    `.gitattributes` (which normalises line endings between
    Linux/Mac/Windows) and `.gitignore` (which hides files which
    shouldn't be committed from Git). You just need to have them in your
    folder, you won't need to change them.
3.  Copy your mod files (including the `.sln` file) into the folder.
4.  Commit your changes in SourceTree:
    1.  Click Commit at the top.
    2.  Click Stage All to add the files to your commit.
    3.  Enter a human-readable description for you changes in the
        textbox. The format is up to you, but "add initial mod files" is
        fine for now.
    4.  Make sure "Push changes immediately" is ticked.
    5.  Click "Commit".

That's it: all your files will appear on GitHub. Your mod is now
open-source!

</dd>

<dt>

Make changes

</dt>

<dd>

The steps above are all first-time setup. When you want to make changes,
it's much easier:

1.  Edit your code in the repository folder.
2.  In SourceTree, commit and push your changes (see step 4 in the
    previous section).

</dd>

</dl>

## See also

- <a href="Modding_Mod_compatibility" class="wikilink"
  title="Modding:Mod compatibility">Modding:Mod compatibility</a> links
  to the source code for every SMAPI mod, where available.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="es_Modding_Código_abierto" class="wikilink"
title="es:Modding:Código abierto">es:Modding:Código abierto</a>
<a href="pt_Modificações_Open_Source" class="wikilink"
title="pt:Modificações:Open Source">pt:Modificações:Open Source</a>
<a href="ru_Модификации_Open_source" class="wikilink"
title="ru:Модификации:Open source">ru:Модификации:Open source</a>
<a href="tr_Modlama_Açık_Kaynak" class="wikilink"
title="tr:Modlama:Açık Kaynak">tr:Modlama:Açık Kaynak</a>
<a href="zh_模组_开源代码" class="wikilink"
title="zh:模组:开源代码">zh:模组:开源代码</a>
