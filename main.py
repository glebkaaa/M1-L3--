import discord
from random import choice
from credits import bot_token
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hi!')
    elif message.content.startswith('$bye'):
        await message.channel.send('\\U0001f642')
    # мой код доработки
    elif message.content.startswith('$smile'):
        smile_list = ['🐍', '🐲', '🐕']
        await message.channel.send(choice(smile_list))
    elif message.content.startswith('$play'):
        play_list = ['🦅', '🪙']
        await message.channel.send(choice(play_list))
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    if message.author != client.user:
        await message.channel.send(message.content)
    else:
        await message.channel.send(message.content)

client.run(bot_token)
