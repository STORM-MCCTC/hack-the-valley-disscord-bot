import discord
from discord.ext import commands

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;ping
    @commands.command(brief="- Pings Client", description="- Pings Client")  # ;ping
    async def ping(self, ctx):
        await ctx.send("Pong :3")

    # ;Helloworld
    @commands.command(brief="- Hello world", description="- Hello world")  # ;ping
    async def Helloworld(self, ctx):
        await ctx.send("Hello world!")

async def setup(bot):
    await bot.add_cog(Debug(bot))
