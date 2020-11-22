import discord
from discord.ext import commands


class Direct(commands.Cog):
	"""DM Commands"""

	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def dm(self, ctx, member: discord.Member, *, args):
		try:
			target = await self.client.fetch_user(member.id)
			await target.send(args)
		except:
			await ctx.send("Couldn't dm the given user.")
		else:
			await ctx.send(f"'{args}' sent to: {target.name}")


	

def setup(client):
	client.add_cog(Direct(client))


def teardown(client):
	client.remove_cog(Direct.__name__)
