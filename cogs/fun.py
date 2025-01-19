import discord
from discord.ext import commands
import random as ran

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;roll
    @commands.command(brief="- Roll Dice", description="- Rolls a dice with any number of sides")  # ;roll
    async def roll(self, ctx, sides: int):
        if sides <= 0:
            await ctx.send(f"{ctx.author.mention}, dice must have a positive number of sides.")
            return
        roll_result = ran.randint(1, sides)
        await ctx.send(f"{ctx.author.mention} rolled {roll_result} on a D{sides}")

    # ;magic8ball
    @commands.command()
    async def magic8ball(self, ctx, question: str):
        ran_list = ["Most definitely", "Yes", "Perchance", "maybe", "Probably Not", "No", "Most Definitely Not"]
        ran_result = ran.choice(ran_list)
        await ctx.send(f"{ctx.author.mention}, {ran_result}.")

    # ;coinflip
    @commands.command()
    async def coinflip(self, ctx):
        flip = ran.choice(["heads", "Tails"])
        await ctx.send(f"fliped {flip}")

    # ;hug
    @commands.command(brief="- Send a virtual hug", description="- Hugs the mentioned user")
    async def hug(self, ctx, member: discord.Member):
        hug_gifs = [
            "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
            "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
        ]
        gif = ran.choice(hug_gifs)
        embed = discord.Embed(
            title="🤗 Virtual Hug!",
            description=f"{ctx.author.mention} gives {member.mention} a big hug!",
            color=discord.Color.purple()
        )
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    # ;slap
    @commands.command(brief="- Slap a user", description="- Sends a virtual slap to the mentioned user")
    async def slap(self, ctx, member: discord.Member):
        slap_gifs = [
            "https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif",
            "https://media.giphy.com/media/l3YSimA8CV1k41b1u/giphy.gif",
            "https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif"
        ]
        gif = ran.choice(slap_gifs)
        embed = discord.Embed(
            title="👋 Virtual Slap!",
            description=f"{ctx.author.mention} slaps {member.mention}! Ouch!",
            color=discord.Color.red()
        )
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

        # ;ship
    @commands.command(brief="- Ship two users", description="- Calculates compatibility between two users")
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member):
        compatibility = ran.randint(0, 100)
        if compatibility > 80:
            description = "💖 A match made in heaven!"
        elif compatibility > 50:
            description = "💘 There's some real potential here!"
        elif compatibility > 20:
            description = "💔 It's complicated..."
        else:
            description = "💀 This ship is sinking fast!"

        embed = discord.Embed(
            title="💞 Ship Compatibility",
            description=f"{user1.mention} 💕 {user2.mention}",
            color=discord.Color.random()
        )
        embed.add_field(name="Compatibility Score", value=f"{compatibility}%", inline=False)
        embed.add_field(name="Analysis", value=description, inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))