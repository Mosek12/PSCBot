import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import datetime

load_dotenv()

bot = commands.Bot(command_prefix='g!', help_command=None)


@bot.event
async def on_ready():
    print('Załadowano plik ładujący')
    await bot.change_presence(activity=discord.Streaming(name='Our site/Information', url='https://www.youtube.com/watch?v=7GrlTxyijEY'))


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(os.getenv('TOKEN'))
