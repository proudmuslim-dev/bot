import discord
from discord.ext import commands
from datetime import datetime


class Logging(commands.Cog):
    """Logging Commands"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def logging(self, ctx):
        await ctx.send(":warning: Logging commands are currently under development.")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        send = False
        if message.guild.id in [743073728853835828, 763493055771705385, 732525308661727243, 754012537296781483]:
            channel = discord.utils.get(message.guild.channels, name="logs")
            send = True

        elif message.guild.id == 786802402887729254:
            channel = discord.utils.get(message.guild.channels, id = 789143875842211890)
            send = True

        if send:
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))
            embed.add_field(name=f"Message by {message.author} deleted in #{message.channel.name}",
                            value=message.content)
            embed.set_footer(
                icon_url="https://cdn.discordapp.com/avatars/573986854366347274/ddff32c78e30ee32f7771eb562dfdba3.webp?size=1024",
                text="Developed by 𝓟𝓻𝓸𝓾𝓭𝓶𝓾𝓼𝓵𝓲𝓶#5818")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        send = False
        if before.guild.id in [743073728853835828, 763493055771705385, 732525308661727243, 754012537296781483] and before.content != after.content:
            channel = discord.utils.get(before.guild.channels, name="logs")
            send = True

        elif before.guild.id == 786802402887729254:
            channel = discord.utils.get(before.guild.channels, id = 789143875842211890)
            send = True

        if send:
            embed = discord.Embed(title=f"Message edited in #{before.channel.name} by {before.author}",
                                  timestamp=datetime.utcnow(), color=discord.Colour.from_rgb(255, 150, 53))

            embed.add_field(name="Original Message", value=before.content)
            embed.add_field(name="Edited Message", value=after.content)
            embed.set_footer(
                icon_url="https://cdn.discordapp.com/avatars/573986854366347274/76b36e11e0757464a6477f480bf5f543.webp?size=1024",
                text="Developed by 𝓟𝓻𝓸𝓾𝓭𝓶𝓾𝓼𝓵𝓲𝓶#5818")

            await channel.send(embed=embed)



def setup(client):
    client.add_cog(Logging(client))


def teardown(client):
    client.remove_cog(Logging.__name__)
