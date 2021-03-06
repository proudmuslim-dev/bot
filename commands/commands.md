# Commands for Overseer

**Below is a list of commands and their usage in my bot, Overseer#4432. This list is hosted as a markdown file on github because I am too broke for proper VPS hosting.**

## Moderation Commands
| Command      | Usage                 | Function                          | Flags                                                           | Aliases    |
|--------------|-----------------------|-----------------------------------|-----------------------------------------------------------------|------------|
| Ban          | >ban {user} {reason}  | Bans User                         | None                                                            | Bean, bonk |
| Kick         | >kick {user} {reason} | Kicks user                        | None                                                            | Boot       |
| Purge        | >purge {amount}       | Purges channel                    | --silent (Removes the message that the bot sends after purging) | None       |
| Channelstats | >cs                   | Sends an embed with channel stats | None                                                            | None       |
| Prefix       | >{prefix}             | Changes server prefix             | None                                                            | None       |

## Guild Commands
| Command      | Usage           | Function                                                                                                                       | Flags | Aliases                       |
|--------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|-------|-------------------------------|
| Total        | >total          | Sends an embed showing the total number of users, channels, and roles in the guild. [Example](https://i.imgur.com/GabdfdE.png) | None  | None                          |
| Guild        | >guild          | Sends an embed displaying guild information. [Example](https://i.imgur.com/B6ENXTt.png)                                        | None  | Server, g, s                  |
| Members      | >members        | Sends an embed with the total number of users in the guild. [Example](https://i.imgur.com/VVJxac7.png)                         | None  | None                          |
| Guildid      | >guildid        | Sends an embed with the guild id. [Example](https://i.imgur.com/KF8OJZ5.png)                                                   | None  | Gid                           |

## User Commands
| Command      | Usage           | Function                                                                                                                       | Flags | Aliases                       |
|--------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|-------|-------------------------------|
| Avatar       | >av {user}      | Sends the given user's profile picture, defaults to message author.                                                             | None  | avatar                        |
| Whois        | >whois {user}   | Sends an embed containing information for the user, defaults to message author.                                                 | None  | user, info                    |
| Roles        | >roles {user}   | Sends an embed listing all of the user's roles and the total number of roles they have, defaults to message author.             | None  | None                          |
| CreationDate | >created {user} | Sends and embed containing the date and time (UTC) when the account was created, defaults to message author.                    | None  | creation, cdate, creationdate |
| JoinDate     | >joined {user}  | Sends and embed containing the date and time (UTC) when the account joined the guild, defaults to message author.               | None  | jd, joindate                  |