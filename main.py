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

@client.tree.command()
async def hello(interaction: discord.Interaction):

    await interaction.response.send_message(f'wassup ni🅱🅱a, {interaction.user.mention}')

@client.tree.command()
async def gibrole(interaction: discord.Interaction, arg: str):

    roles = []
    addable_roles = []

    role_to_add = None

    flag = False

    for role in interaction.user.guild.roles:

        roles.append(role)

        if flag is not True and role.name == 'limiter':
            flag = True

        if flag is False and role.name != '@everyone':
            addable_roles.append(role.name.lower())

            if arg.lower() == role.name.lower():
                role_to_add = role

    if arg.lower() in addable_roles:
        await interaction.guild.get_member(interaction.user.id).add_roles(role_to_add)
        await interaction.response.send_message(f'role {role_to_add.name} giben to {interaction.user.mention}')
    else:
        await interaction.response.send_message('no such role niba')

@client.tree.command()
async def ungibrole(interaction: discord.Interaction, arg: str):

    roles = []
    addable_roles = []

    role_to_remove = None

    flag = False

    for role in interaction.user.guild.roles:

        roles.append(role)

        if flag is not True and role.name == 'limiter':
            flag = True

        if flag is False and role.name != '@everyone':
            addable_roles.append(role.name.lower())

            if arg.lower() == role.name.lower():
                role_to_remove = role

    if arg.lower() in addable_roles:
        await interaction.guild.get_member(interaction.user.id).remove_roles(role_to_remove)
        await interaction.response.send_message(f'role {role_to_remove.name} ungiben to {interaction.user.mention}')
    else:
        await interaction.response.send_message('no such role niba')


client.run(config['AUTH']['token'])
