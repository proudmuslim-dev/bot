import discord
from discord.ext import commands

class MultiUser(commands.Cog):
    """Attempting rewrite of Moderation Cog"""
    def __init__(self, client):
        self.client = client

    # @commands.command()
    # async def multiban(self, ctx, *args):
    #     banned = []
    #     failed = []
    #     for member in args:
    #         if member.id in utils.devs:
    #             await ctx.send("Failed to ban {member.name}: Forbidden")
    #         else:
    #             try:
    #                 await member.ban()
    #                 banned.append(str(member.name))

    #             except:
    #                 failed.append(str(member.name))

    #     embed = discord.Embed(name="Output", color=discord.colour.from_rgb(255, 150 53))
    #     embed.add_field

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def dban(self, ctx, member1: discord.Member = None, member2: discord.Member = None, reason = None):
        members = []; members.append(member1); members.append(member2)
        if member1 and member2 != None or member2 != None:
            for member in members:
                if reason == None:
                    await member.dm(f"You were banned in {ctx.guild.name}")
                    await member.ban()
                else:
                    await member.dm(f"You were banned in {ctx.guild.name} for {reason}")
                    await member.ban()
        else:
            await ctx.send(":x: Missing one or more members.")



def setup(client):
	client.add_cog(MultiUser(client))


def teardown(client):
	client.remove_cog(MultiUser.__name__)


