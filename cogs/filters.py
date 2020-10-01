import discord
from discord.ext import commands
import re

class Chat(commands.Cog):
    """Chat filters"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        pattern = "(?:https?:\/\/)?((?:dis\.gd|discord\.(?:gg|io|me)|invite\.gg)\/([a-zA-Z0-9\-]+))"
        if message.guild.id in [743073728853835828]:
            if message.author.id not in [252104964753719296, 196271012717789184,
            234322190714011648,
            475263799511875584, 689590579935707241, 
            172309577134505985]:
                if(re.search(pattern, message.content.lower())):
                    await message.delete()
                else:
                    pass




def setup(client):
	client.add_cog(Chat(client))


def teardown(client):
	client.remove_cog(Chat.__name__)

