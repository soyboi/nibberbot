import discord
from discord import app_commands
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class Nibberbot(discord.Client):

    def __init__(self, *, intents:discord.Intents):

        super().__init__(intents=intents)

        self.guild = discord.Object(id=config['VARS']['guildid'])
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):

        self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)