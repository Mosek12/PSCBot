import discord
from discord.ext import commands
import asyncio
import random
from gtts import gTTS


async def play_file(ctx, filename):
    voice_channel = ctx.author.voice.channel
    voice_channel = await voice_channel.connect()
    source = discord.FFmpegPCMAudio(filename)
    voice_channel.play(source, after=lambda: print("sus"))
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

    @commands.command()
    @commands.guild_only()
    async def tts(self, ctx, *, text):
        """TTS"""
        speech = gTTS(text=text, lang='pl', slow=False)

        speech.save('assets/tts.mp3')
        await asyncio.sleep(1)

        filename = "assets/tts.mp3"
        await play_file(ctx, filename)


def setup(bot):
    bot.add_cog(audio(bot))
