from discord.ext.commands import Cog
from discord.ext.commands import command
import discord

class Help(Cog):
    def __init__(self, client):
        self.client= client
        self.client.remove_command("help")

    @command(name="help")
    async def show_help(self, ctx):
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))

        helpmsg = "[Commands (WIP)](https://github.com/proudmuslim-dev/bot/blob/master/commands/commands.md)\n"
        helpmsg += "[Source Code](https://github.com/proudmuslim-dev/bot)\n"
        helpmsg += "[Support Server](https://discord.gg/8KSuJSY)\n"
        helpmsg += "[Invite](https://discord.com/oauth2/authorize?client_id=717215043724509275&scope=bot&permissions=8)"

        embed.add_field(name="Help", value=helpmsg)
      
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

        await ctx.send(embed=embed)

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
