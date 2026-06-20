---
title: "Chat Commands"
wiki_source: "Modding:Chat Commands"
permalink: /Modding:Chat_Commands/
category: game
tags: [chat-commands, registering-custom-commands, see-also]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents how custom
<a href="Multiplayer#Chat" class="wikilink" title="chat commands">chat
commands</a> are handled by the game. This is an advanced guide for mod
developers.

## Registering custom commands

Chat commands are modular and extensible, with a `ChatCommands` API to
manage them.

For example, you can add a custom chat command like this:

``` c#
string modId = this.ModManifest.UniqueId;
ChatCommands.Register($"{modId}_echo", this.Echo, name => $"{name} [message]: show the given message in the chat box.");

...

/// <inheritdoc cref="ChatCommandHandlerDelegate" />
private void Echo(string[] command, ChatBox chat)
{
    string message = ArgUtility.GetRemainder(command, 1);

    chat.addInfoMessage(message);
}
```

## See also

- <a href="Modding_Console_commands" class="wikilink"
  title="Modding:Console commands">Modding:Console commands</a> for
  commands that can be typed in the SMAPI console.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Чат-команды" class="wikilink"
title="ru:Модификации:Чат-команды">ru:Модификации:Чат-команды</a>
<a href="zh_模组_聊天命令" class="wikilink"
title="zh:模组:聊天命令">zh:模组:聊天命令</a>
