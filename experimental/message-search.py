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
        if amount > 200:
            await ctx.send(f"<:disagree:767758599916486717> Amount {amount} reduced to 200 due to the message cap, continuing...")
            amount = 200

        val = ""

        async for message in ctx.channel.history(limit=amount):
            if text.lower() in message.content.lower() and message != ctx.message:
                val += f"- {message.jump_url}\n"

        embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))
        def foo():
            if val != "":
                return val

            else:
                return None
        embed.add_field(name="Matches for Text Provided", value=foo())
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

        await ctx.send(embed=embed)

def setup(client):
	client.add_cog(MessageSearch(client))


def teardown(client):
	client.remove_cog(MessageSearch.__name__)

