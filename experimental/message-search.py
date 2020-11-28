import discord
import re
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command 


class MessageSearch(Cog):
    def __init__(self, client):
        self.client = client

    @command(aliases=["srch"])
    async def search(self, ctx, amount: int, *, text: str):
        if amount > 999999:
            await ctx.send(f"<:disagree:767758599916486717> Amount {amount} reduced to 9999999 due to the message cap, continuing...")
            amount = 999999

        val = ""

        y = 0

        async for message in ctx.channel.history(limit=amount):
            if text.lower() in message.content.lower() and message != ctx.message:

                y += 1
                val += f"{y}. {message.author.name} - [Jump]({message.jump_url})\n"

        embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))
        def x():
            if val != "":
                return val

            else:
                return None
        embed.add_field(name="Matches for Text Provided", value=x())
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

        await ctx.send(embed=embed)

    @command(name="serversrch", aliases=["guildsearch", "gsrch"])
    async def attic_search(self, ctx, text: str):
        if ctx.guild.id == 366606284713230346:
            links = "Matches\n"

            for channel in ctx.guild.text_channels:
                try: 
                    async for message in channel.history(limit=2000):
                        if text in message.content.lower():
                            links += f"- {message.jump_url}\n"

                except:
                    pass

        await ctx.send(links)

                
                        


def setup(client):
	client.add_cog(MessageSearch(client))


def teardown(client):
	client.remove_cog(MessageSearch.__name__)

