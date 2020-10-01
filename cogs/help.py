from discord.ext.commands import Cog
from discord.ext.commands import command
import discord

class Help(Cog):
    def __init__(self, client):
        self.client= client
        self.client.remove_command("help")

    @command(name="help")
    async def show_help(self, ctx):
        embed = discord.Embed(title="Help", color = discord.Color.from_rgb(255, 130, 53))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/717215043724509275/a82627ad58710534531cec935abd5e87.webp?size=1024")

        """Moderation commands"""
        modcmd = "Ban - Usage: >>ban <users> | Aliases: bean, bonk\n"
        modcmd += "\nKick - Usage: >>kick <users> | Aliases: boot\n"


        embed.add_field(name="**Moderation Commands**", value=modcmd, inline=False)

        """utility commands"""
        utilcmd = "Whois - Usage: >>whois <user> | Output: An embed with user information, defaults to the sender\n"
        utilcmd += "\nAvatar - Usage: >>avatar <user> | Output: The user's avatar, defaults to the sender\n"
        utilcmd += "\nRoles - Usage: >>roles <user> | Output: An embed with a list of all the user's roles\n"
        utilcmd += "\nUserid - Usage: >>uid <user> | Output: aAn embed with the given user's ID. Aliases:  \n"
        utilcmd += "\nChannelstats - Usage: >>cs | Displays channel stats for the current channel | **Currently working on implementing a way to use this on channels other than the one you are in**\n"

        embed.add_field(name="**Utility Commands**", value=utilcmd, inline=False)

        """Server Commands"""
        servcmd = "Server - Usage: >>server | Output: an embed with information on the server, includes information from all commands in this category | Aliases: guild, g, s\n"
        servcmd +="\nTotal - Usage: >>total | Output: an embed with the total roles, channels, and members of the server\n"
        servcmd += "\nMembers - Usage: >>members | Output: an embed displaying the total memebers of the guild\n"
        

        embed.add_field(name="**Server commands**", value=servcmd, inline=False)

        """Misc commands"""
        miscmd = "Ping - Usage: >>ping | Output: Pong\n"
        miscmd += "\nPong - Usage: >>ping | Output: Ping\n"
        miscmd += "\nKill - Usage: >>kill <user> | Output: Successfully killed <user>, defaults to no one | Why would you want to use this cmd\n"
        miscmd += "\nGruh - Usage: >>gruh | Output: Gruh moment\n"
        miscmd += "\nRepeat - Usage: >>repeat <message> | Output: <message>\n"
        miscmd += "\nHello - Usage: >>hello | Useless command\n"

        embed.add_field(name="**Miscellaneous Commands**", value = miscmd)

        """DM Commands"""
        dmcmd = "DM - Usage: >>dm <user> <message> | Sends a user a pm via the bot, requires administrator perms, probably going to remove this soon\n"

        embed.add_field(name="**DM Commands**", value =dmcmd, inline=False)

        """Credit commands"""
        credcmd = "Dev - Usage: >>dev | Sends a message crediting my two main developers\n"
        credcmd += "Source - Usage: >>source | Sends a message with a link the github page that contains my source code"

        embed.add_field(name="**Credits**", value=credcmd)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

        await ctx.send(embed=embed)

    @command(name="help util", aliases=["help utils", "help utility", "help utilities", "h utils", "h utilities", "h utility"])
    async def help_util(self, ctx):
        embed = discord.Embed(title= "**Help for Utility Commands**", color=discord.Colour.from_rgb(255, 150, 53))
 
        """utility commands"""
        utilcmd = "Whois - Usage: >>whois <user> | Output: An embed with user information, defaults to the sender\n"
        utilcmd += "\nAvatar - Usage: >>avatar <user> | Output: The user's avatar, defaults to the sender\n"
        utilcmd += "\nRoles - Usage: >>roles <user> | Output: An embed with a list of all the user's roles\n"
        utilcmd += "\nUserid - Usage: >>uid <user> | Output: aAn embed with the given user's ID. Aliases:  \n"
        utilcmd += "\nChannelstats - Usage: >>cs | Displays channel stats for the current channel | **Currently working on implementing a way to use this on channels other than the one you are in**\n"
        
        embed.add_field(name="Commands:", value=utilcmd)

        await ctx.send(embed=embed)

    @command(name="help guild", aliases=["help server", "h servcr", "h guild"])
    async def help_guild(self, ctx):
        embed = discord.Embed(title="**Help for Server Commands**")

        """Server Commands"""
        servcmd = "Server - Usage: >>server | Output: an embed with information on the server, includes information from all commands in this category | Aliases: guild, g, s\n"
        servcmd +="\nTotal - Usage: >>total | Output: an embed with the total roles, channels, and members of the server\n"
        servcmd += "\nMembers - Usage: >>members | Output: an embed displaying the total memebers of the guild\n"

        embed.add_field(name="Commands:", value=servcmd, inline=False)

    @command(name="help misc", aliases=["h misc", "help miscellaneous", "h miscellaneous"])
    async def help_misc(self, ctx):
        embed = discord.Embed(title="**Help for Miscellaneous Commands**")

        """Misc commands"""
        miscmd = "Ping - Usage: >>ping | Output: Pong\n"
        miscmd += "\nPong - Usage: >>ping | Output: Ping\n"
        miscmd += "\nKill - Usage: >>kill <user> | Output: Successfully killed <user>, defaults to no one | Why would you want to use this cmd\n"
        miscmd += "\nGruh - Usage: >>gruh | Output: Gruh moment\n"
        miscmd += "\nRepeat - Usage: >>repeat <message> | Output: <message>\n"
        miscmd += "\nHello - Usage: >>hello | Useless command\n"

        embed.add_field(name="Commands:", value = miscmd)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))

def teardown(client):
    client.remove_cog(Help.__name__)
