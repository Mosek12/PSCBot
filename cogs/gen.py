import discord
from discord.ext import commands
import asyncio
import random


class gen(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Załadowano gen')

    @commands.command()
    async def psc(self, ctx, arg):

        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        embed1 = discord.Embed(
            title='Your PaySafeCard code is down here',
            description=f'||0{random.choice(digit)}{random.choice(digit)}{random.choice(digit)}-{random.choice(digit)}{random.choice(digit)}{random.choice(digit)}{random.choice(digit)}-{random.choice(digit)}{random.choice(digit)}{random.choice(digit)}{random.choice(digit)}-{random.choice(digit)}{random.choice(digit)}{random.choice(digit)}{random.choice(digit)}||',
            colour=discord.Colour.blue()
        )

        embed1.set_footer(
            text='Generated via complicated algorithm by paysafecardgeneratorAPI.org')
        embed1.set_thumbnail(
            url='https://avatars.githubusercontent.com/u/22189864?s=280&amp;v=4')

        embed2 = discord.Embed(
            description=f'{ctx.author.mention} **Check your DMs!**',
            colour=discord.Colour.random()
        )

        await ctx.author.send(embed=embed1)
        await ctx.send(embed=embed2)
        await asyncio.sleep(20)
        await ctx.channel.purge(limit=3)

    @commands.command()
    async def nitro(self, ctx, arg):
        letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        embed1 = discord.Embed(
            title='Your NITRO link is down here',
            description=f'||https://discord.gift/{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}||',
            colour=discord.Colour.orange()
        )

        embed1.set_thumbnail(url='https://i.redd.it/mvoen8wq3w831.png')

        embed2 = discord.Embed(
            description=f'{ctx.author.mention} **Check your DMs!**',
            colour=discord.Colour.random()
        )

        await ctx.author.send(embed=embed1)
        await ctx.send(embed=embed2)
        await asyncio.sleep(20)
        await ctx.channel.purge(limit=3)


def setup(bot):
    bot.add_cog(gen(bot))
