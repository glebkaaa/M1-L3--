import discord
from discord.ext import commands
from credits import bot_token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send('he' * count_heh)


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

bot.run(bot_token)
