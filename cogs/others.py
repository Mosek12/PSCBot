import discord
from discord.ext import commands


class others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Załadowano others')

    @commands.command()
    async def count(self, ctx, arg: int):
        if arg <= 2137:
            a = 0
            while a != arg:
                a += 1
                await ctx.send(a)
        else:
            await ctx.send('Your argument must be less than 2137')


def setup(bot):
    bot.add_cog(others(bot))
