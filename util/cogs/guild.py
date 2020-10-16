import discord
from discord.ext import commands

class Server(commands.Cog):
	"""Server/Guild Commands"""
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=["t"])
	async def total(self, ctx):
		embed = discord.Embed(title=f"Totals for {ctx.guild.name}:", color=discord.Colour.from_rgb(255, 130, 53))
		embed.set_thumbnail(url=ctx.guild.icon_url)
		
		embed.add_field(name="Total Channels", value=len(ctx.guild.channels))
		embed.add_field(name="Total Members", value=len(ctx.guild.members))
		embed.add_field(name="Total Roles", value=len(ctx.guild.roles))

		embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

		await ctx.send(embed=embed)

	@commands.command(name="guild", aliases=["server", "g", "s",])
	async def server(self, ctx):
		embed = discord.Embed(title=f"Guild Stats for {ctx.guild.name}:", color=discord.Colour.from_rgb(255, 130, 53))
		embed.set_thumbnail(url=ctx.guild.icon_url)
		
		embed.add_field(name="Guild Name", value = " ".join([(x[0].upper() + x[1:]) for x in str(ctx.guild.region).split()]))
		embed.add_field(name="Guild ID", value=ctx.guild.id, inline=True)
		embed.add_field(name="Guild Region", value=ctx.guild.region, inline=True)
		embed.add_field(name="Guild Creation Date", value=ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
		embed.add_field(name="Total Channels", value=len(ctx.guild.channels))
		embed.add_field(name="Total Members", value=len(ctx.guild.members))
		embed.add_field(name="Total Roles", value=len(ctx.guild.roles))


		embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

		await ctx.send(embed=embed)

	@commands.command()
	async def members(self, ctx):
		embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0))
		embed.set_thumbnail(url=ctx.guild.icon_url)
		embed.add_field(name=f"**Total Members for {ctx.guild.name}:**", value=len(ctx.guild.members))

		await ctx.send(embed=embed)

	@commands.command(name="guildid", aliases=["gid"])
	async def guild_id(self, ctx):
		embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))
		embed.set_thumbnail(url=ctx.guild.icon_url)
		embed.add_field(name=f"Guild ID for {ctx.guild.name}", value=ctx.guild.id)
		embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

		await ctx.send(embed=embed)


def setup(client):
	client.add_cog(Server(client))


def teardown(client):
	client.remove_cog(Server.__name__)

