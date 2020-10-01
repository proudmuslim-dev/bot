import discord
from discord.ext import commands


class Dev(commands.Cog):
	"""Dev command stuff"""

	

	@commands.command()
	async def rules(self, ctx):
		embed = discord.Embed(title="**Rules for Overseer Development Discord**", color=discord.Colour.from_rgb(255, 130, 53))
		embed.add_field(name="**General Rules**", value="1. [Discord TOS](https://discord.com/terms) \n2. [Discord Community Guidelines](https://discord.com/guidelines) \n3. Don't be an arse. \n4. Be respectful towards other members.")
		embed.add_field(name="**Rules Specific for #support**", value="1. Don't troll. If you see someone trolling, PM a staff member \n2.")

		await ctx.send(embed=embed)


def setup(client):
	client.add_cog(Dev(client))


def teardown(client):
	client.remove_cog(Dev.__name__)
