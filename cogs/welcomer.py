import discord
from discord.ext import commands


class Welcome(commands.Cog):
    """Welcomer stuff"""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        send = False
        if member.guild.id in [743073728853835828, 754012537296781483]:
            channel = discord.utils.get(member.guild.channels, name="welcome-logs")
            send = True

        elif member.guild.id in [763493055771705385]:
            channel = discord.utils.get(member.guild.channels, name="joins")
            send = True

        elif member.guild.id in [778714948779114516]:
            channel = discord.utils.get(member.guild.channels, name="welcome")
            send = True

        elif member.guild.id == 786802402887729254:
            channel = discord.utils.get(member.guild.channels, id = 786826679896244245)
            send = True

        if send:
            embed = discord.Embed(title=f"User info for {member.name}", color=discord.Colour.from_rgb(255, 150, 53))
            embed.add_field(name="User ID", value=member.id, inline=False)
            embed.add_field(name="Account Creation Date",
                            value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            embed.add_field(name="Joined Server on", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                            inline=True)
            embed.set_thumbnail(url=member.avatar_url)

            await channel.send(f"Please welcome {member.mention} to {member.guild.name}")
            await channel.send(embed=embed)

        
        if member.guild.id == 754012537296781483 and member.id == 196683878935560192:
            await member.kick()




def setup(client):
    client.add_cog(Welcome(client))


def teardown(client):
    client.remove_cog(Welcome.__name__)
