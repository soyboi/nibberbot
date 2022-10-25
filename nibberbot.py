import discord
from discord import app_commands

class Nibberbot(discord.Client):

    def __init__(self, *, intents:discord.Intents):

        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):

        await self.tree.fetch_commands()
        await self.tree.sync()