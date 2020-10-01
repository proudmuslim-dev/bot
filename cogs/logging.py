import discord
from discord.ext import commands

class Logging(commands.Cog):
    """Logging Commands"""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def logging(self, ctx):
        await ctx.send(":warning: Logging commands are currently under development.")

def setup(client):
	client.add_cog(Logging(client))


def teardown(client):
	client.remove_cog(Logging.__name__)

