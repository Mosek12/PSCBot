import discord
from discord import colour
from discord.ext import commands
from discord.ext.commands.core import command


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

    @commands.command()
    # moderator, kierownik budowy, administrator, właściciel
    @commands.has_any_role(769266991219212309, 769264017482973234, 799616680107180052, 572786262193340423)
    async def vote(self, ctx, member: discord.Member, arg):

        if arg == 'degrad':
            string = 'zdegradowaniem'
        elif arg == 'intemute':
            string = 'natychmiastowym tymczasowym zmutowaniem'
        else:
            embed = discord.Embed(
                description='Aby poprawnie użyć tej komendy, musisz zrobić to według wzoru `vote @użytkownik degrad/intemute`',
                colour=discord.Colour.random()
            )
        embed = discord.Embed(
            description=f'Głosowanie użytkownika {ctx.author.mention} za {string} {member.mention}',
            colour=discord.Colour.random()
        )
        await ctx.send(embed=embed)
        await ctx.add_reaction(ctx, ':white_check_mark:')


def setup(bot):
    bot.add_cog(others(bot))
