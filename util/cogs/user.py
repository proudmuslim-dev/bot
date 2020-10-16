import discord
from discord.ext import commands

class User(commands.Cog):
    """User commands"""
    def __init__(self, client):
        self.client = client

    @commands.command(name="user id", aliases=["myid", "my id", "uid", "userid"])
    async def user_id(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        embed = discord.Embed(color=discord.Colour.from_rgb(255, 130, 53))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=f"User ID for {member.name}:", value=member.id)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

        await ctx.send(embed=embed)

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member:discord.Member = None):
        if not member:
            await ctx.send(ctx.author.avatar_url)
        else:
            await ctx.send(member.avatar_url)

    @commands.command(aliases=["user", "info"])
    async def whois(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        if member.name == member.display_name:
            nick = "None"

        else:
            nick = member.display_name

        roles = [role for role in member.roles]

        def check_role_count(list):
            if len(list) > 3:
                return False
            else:
                return True

        embed = discord.Embed(title=f"Info for user {member.name}", description=member.mention, color = discord.Colour.from_rgb(255, 130, 53))

        embed.add_field(name="ID", value=member.id, inline=False, )
        embed.set_thumbnail(url=member.avatar_url)

        embed.add_field(name="Total Roles", value = (len(member.roles) - 1))
        embed.add_field(name="Nickname", value=nick, inline=True)

        embed.add_field(name="Account Created on", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
        embed.add_field(name="Joined Server on", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)

        embed.add_field(name="Bot?", value = member.bot, inline=True)
        embed.add_field(name=f"Roles ({len(roles)})", value = " ".join([role.mention for role in roles]), inline=check_role_count(member.roles))

        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

        await ctx.send(embed=embed)

    @commands.command()
    async def roles(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author

        roles = [role for role in member.roles]

        embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=f"Roles for {member.name}:", value = " ".join([role.mention for role in roles]))
        embed.add_field(name="Total", value=len(member.roles), inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")

        await ctx.send(embed=embed)

    @commands.command(aliases=["creation", "cdate", "created"])
    async def creationdate(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author

        embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=f"Account creation date for {member.name}", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")
        
        await ctx.send(embed=embed)

    @commands.command(aliases=["jd", "jdate", "joined"])
    async def joindate(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author

        embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=f"Server join date for {member.name}", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")
        
        await ctx.send(embed=embed)
        
    @commands.command(aliases=["d"])
    async def dates(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 150, 53))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=f"Server join date for {member.name}", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"Account creation date for {member.name}", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by: {ctx.author.name}")
        
        await ctx.send(embed=embed)
        
        


def setup(client):
	client.add_cog(User(client))


def teardown(client):
	client.remove_cog(User.__name__)
