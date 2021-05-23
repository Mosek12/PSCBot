import discord
from discord.ext import commands
import asyncio
import random


# defining function to handle playing sounds in Voice Channel
async def play_file(ctx, filename):

    voice_channel = ctx.author.voice.channel
    voice_channel = await voice_channel.connect()
    source = discord.FFmpegPCMAudio(filename)
    voice_channel.play(source, after=lambda: print("played doot"))
    while voice_channel.is_playing():
        await asyncio.sleep(1)
    voice_channel.stop()
    await voice_channel.disconnect()


class audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Załadowano audio')

    @commands.command()
    @commands.guild_only()
    async def patus(self, ctx):
        """Patus"""
        chance = random.randint(1, 2)
        if chance == 1:
            filename = "assets/patus.mp3"
        else:
            filename = "assets/patus2.mp3"
        await play_file(ctx, filename)


def setup(bot):
    bot.add_cog(audio(bot))
