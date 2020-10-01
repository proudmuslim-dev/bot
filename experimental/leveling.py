import discord
from discord.ext import commands
import json 
import os

os.chdir(r'~/augh/test/experimental')
class Leveling(commands.Cog):
    """Overseer bullied me into this"""
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self, message):
        with open('users.json', 'r') as f:
            users = json.load(f)
            
        with open('users.json', 'w') as f:
            json.dump(users, f)
