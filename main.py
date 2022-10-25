import discord
from nibberbot import Nibberbot
import configparser

intents = discord.Intents.all()
client = Nibberbot(intents=intents)
config = configparser.ConfigParser()
config.read('config.ini')

@client.event
async def on_ready():

    print(f'Logged in as {client.user} ID: {client.user.id}')
    print('--------')

    #TODO: make it make a list of user addable roles here (for each role if role is below limiter role add to list)


@client.tree.command()
async def hello(interaction: discord.Interaction):

    await interaction.response.send_message(f'wassup ni🅱🅱a, {interaction.user.mention}')

@client.tree.command()
async def gibrole(interaction: discord.Interaction):

    roles = []

    for role in interaction.user.guild.roles:
        roles.append(str(role).lstrip('@'))

    print(f'{roles}')
    await interaction.channel.send(roles)

    await interaction.response.send_message(f'role giben to {interaction.user.mention}')


client.run(config['AUTH']['token'])
