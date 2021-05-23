from cogs.audio import audio
import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Załadowano help')

    @commands.group(pass_context=True, invoke_without_command=True)
    async def help(self, ctx):

        helpem = discord.Embed(
            title='Help | Main Page',
            description=f'Hello! Thank you for using our bot.\nIf you\'re looking for information, check our site.\nI you aren\'t admin of this server, you can add this bot to your server. Just check our site.\nIf you\'re lookin for commands, just type `g!help` and name of category you want to inspect.',
            colour=discord.Colour.red()
        )

        helpem.add_field(
            name="Generate", value="Commands, which generates psc/nitro", inline=True)
        helpem.add_field(
            name="Load", value="Commands, which are really advanced", inline=True)
        helpem.add_field(
            name="Audio", value="Audio related commands", inline=True)
        helpem.add_field(
            name="Others", value="All other commands", inline=True)

        await ctx.send(embed=helpem)

    @help.group(pass_context=True, invoke_without_command=True, aliases=['Generate', 'gen', 'Gen'])
    async def generate(self, ctx):

        helpgen = discord.Embed(
            title='Help | Generate Page',
            description='Commands, which generates psc codes/nitro links, then sends them to user\'s DMs.\nFor more info type `g!help Generate` and command you want to inspect',
            colour=discord.Colour.red()
        )

        helpgen.add_field(name="psc", value="Generates psc code", inline=True)
        helpgen.add_field(
            name="nitro", value="Generates nitro link", inline=True)

        await ctx.send(embed=helpgen)

    @help.group(pass_context=True, invoke_without_command=True, aliases=['Load', 'reload', 'Reload'])
    async def load(self, ctx):

        helplo = discord.Embed(
            title='Help | Load Page',
            description=f'Commands, which you probably don\'t know how to use and when, so just do not.\nFor more info type `g!help Load` and command you want to inspect',
            colour=discord.Colour.red()
        )

        helplo.add_field(name="_load", value="Loads extention", inline=True)
        helplo.add_field(name="unload", value="Unloads extention", inline=True)
        helplo.add_field(name="reload", value="Reloads extention", inline=True)

        await ctx.send(embed=helplo)

    @help.group(pass_context=True, invoke_without_command=True, aliases=['Music', 'Audio', 'music'])
    async def audio(self, ctx):
        helpat = discord.Embed(
            title='Help | Others Page',
            description=f'Audio commands',
            colour=discord.Colour.red()
        )

        helpat.add_field(
            name="tts", value="Text to speech", inline=True)

        helpat.add_field(
            name="patus", value="...", inline=True)

        await ctx.send(embed=helpat)

    @help.group(pass_context=True, invoke_without_command=True, aliases=['Others', 'other', 'Other'])
    async def others(self, ctx):

        helpot = discord.Embed(
            title='Help | Others Page',
            description=f'All other commands\nFor more info type `g!help Others` and command you want to inspect',
            colour=discord.Colour.red()
        )

        helpot.add_field(
            name="ping", value="Displays bot\'s ping", inline=True)

        helpot.add_field(
            name="count", value="Counts to the given number", inline=True)

        await ctx.send(embed=helpot)

    @generate.command(pass_context=True)
    async def psc(self, ctx):
        await ctx.send("Sends psc code to user who used it, then sends mention of user to chat, after 20 sec deletes all the messages in channel `g!psc`")

    @generate.command(pass_context=True)
    async def nitro(self, ctx):
        await ctx.send("Sends nitro link to user who used it, then sends mention of user to chat, after 20 sec deletes all the messages in channel `g!nitro`")

    @load.command(pass_context=True)
    async def _load(self, ctx):
        await ctx.send("Loads an extention, which you've chosen `g!load <name of extention>`")

    @load.command(pass_context=True)
    async def unload(self, ctx):
        await ctx.send("Unloads an extention, which you've chosen `g!unload <name of extention>`")

    @load.command(pass_context=True)
    async def reload(self, ctx):
        await ctx.send("Reloads an extention, which you've chosen `g!reload <name of extention>`")

    @audio.command(pass_context=True)
    async def tts(self, ctx):
        await ctx.send("`g!tts [text you want to convert to speech]`")

    @audio.command(pass_context=True)
    async def patus(self, ctx):
        await ctx.send("`g!patus`")

    @others.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.send("Shows bot\'s ping `g!ping`")

    @others.command(pass_context=True)
    async def count(self, ctx):
        await ctx.send("`g!count [number you want to count to]`")


def setup(bot):
    bot.add_cog(help(bot))
