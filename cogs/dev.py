import discord
from discord.ext import commands


class Dev(commands.Cog):
	"""Dev command stuff"""
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def rules(self, ctx):
		embed = discord.Embed(title=f"Rules for {ctx.guild.name} Discord", 
								color = discord.Colour.from_rgb(255, 150, 53))

		rules = "1. **Treat others with respect.** This includes their opinions/beliefs.\n"
		rules += "\n2. **Know your limits**, do not overstep people's boundaries.\n"
		rules += "\n3. **Take your arguments to PMs**, don't verbally attack someone in public channels\n"
		rules += "\n4. **Leaking someone else's personal info or threatening to is forbidden.**\n"
		rules += "\n5. Political discussion is allowed in the off-topic channel **as long as it does not result in heated discussion.**\n\n"

		embed.add_field(name="**Section I. Common Sense**", value = rules)

		rules = "1. **Follow [Discord Community Guidelines](https://discordapp.com/guidelines) and [ToS](https://discordapp.com/terms)**\n"
		rules += "\n2. **Don't tag staff unless necessary.**\n"
		rules += "\n3. **Report any kind of predatory activity to the staff team immediately.** \n"
		rules += "\n4. **Keep bot commands to the proper channel and don't spam them.** \n"
		rules += "\n5. **No NSFW images** \n\n"

		embed.add_field(name="**Section II. General Rules**", value = rules, inline=False)

		rules = "1. **Do not troll or make obscenely loud noises** in the VCs.\n"
		rules +="\n2. **Try to reduce background noise.** If that isn't possible, use push to talk or the vc-text channel\n"

		embed.add_field(name="**Section III. Voice Channels**", value = rules, inline=False)


		await ctx.send(embed=embed)


def setup(client):
	client.add_cog(Dev(client))


def teardown(client):
	client.remove_cog(Dev.__name__)
