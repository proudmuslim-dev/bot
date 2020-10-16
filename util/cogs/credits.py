import discord
from discord.ext import commands


class Credits(commands.Cog):
    """Informative commands"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dev(self, ctx):
        embed = discord.Embed(title="**My Development Team:**", color=discord.Colour.from_rgb(255, 150, 53))
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/717215043724509275/a82627ad58710534531cec935abd5e87.webp?size=1024")
        embed.add_field(name="Lead Developers", value="- **Proudmuslim#5818**\n- **SirNapkin1334#7960**")
        embed.add_field(name="Guy who did nothing", value="- **Cyclcrclicly#3420**")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

        await ctx.send(embed=embed)

    @commands.command()
    async def source(self, ctx):
        await ctx.send("You may view the bot's source code at https://github.com/proudmuslim-dev/bot")


def setup(client):
    client.add_cog(Credits(client))


def teardown(client):
    client.remove_cog(Credits.__name__)
