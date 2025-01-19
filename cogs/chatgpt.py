import discord
from discord.ext import commands
import openai

with open("api_key.txt", "r") as api_key_file:
   openai.api_key = api_key_file.readline().strip()

class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;chatgpt
    @commands.command(brief="- Ask ChatGPT a question", description="- Interact with ChatGPT")
    async def chatgpt(self, ctx, *, prompt):
        try:
            # Send the prompt to OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            # Extract and send the response
            reply = response['choices'][0]['message']['content']
            await ctx.send(reply)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # ;whatami
    @commands.command(brief="- Discover your personality!", description="- Generates a fun personality based on your username")
    async def whatami(self, ctx):
        try:
            username = ctx.author.name
            prompt = f"Analyze the username '{username}' and generate a creative and fun personality description. Be playful and imaginative."
            
            # Send the prompt to OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative and fun assistant who describes personalities based on names."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extract and send the response
            reply = response['choices'][0]['message']['content']
            embed = discord.Embed(
                title="🌀 What Am I?",
                description=f"{ctx.author.mention}, here's your personality description:",
                color=discord.Color.blue()
            )
            embed.add_field(name="Personality", value=reply, inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # ;advice
    @commands.command(brief="- Receive a piece of advice", description="- Generates helpful or funny advice")
    async def advice(self, ctx):
        try:
            prompt = "Provide a helpful or funny piece of advice that anyone can use."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a wise assistant who provides advice."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            await ctx.send(f"🧠 **Advice:** {reply}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # ;story
    @commands.command(brief="- Tell me a story", description="- Generates a short, fun story")
    async def story(self, ctx, *, topic=None):
        try:
            user = ctx.author.name
            prompt = f"Write a short, fun, and creative story involving a character named {user}."
            if topic:
                prompt += f" The story should be about {topic}."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative storyteller."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            await ctx.send(f"📖 **Here's your story:**\n{reply}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # ;joke
    @commands.command(brief="- Hear a joke", description="- Generates a funny or silly joke")
    async def joke(self, ctx):
        try:
            prompt = "Tell me a funny and clean joke."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a funny assistant who tells jokes."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            await ctx.send(f"😂 **Joke:** {reply}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # ;define
    @commands.command(brief="- Define a word or concept", description="- Provides the definition of a word or concept")
    async def define(self, ctx, *, word):
        try:
            prompt = f"Provide a clear and concise definition for the word or concept: {word}."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a knowledgeable assistant who defines words and concepts."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            embed = discord.Embed(
                title=f"📚 Definition of {word}",
                description=reply,
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # ;funfact
    @commands.command(brief="- Learn a fun fact", description="- Shares an interesting or surprising fact")
    async def funfact(self, ctx):
        try:
            prompt = "Share a surprising or interesting fun fact."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a knowledgeable assistant who shares fun facts."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            await ctx.send(f"🤓 **Fun Fact:** {reply}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # ;quote
    @commands.command(brief="- Get a motivational quote", description="- Provides a motivational or inspirational quote")
    async def quote(self, ctx):
        try:
            prompt = "Provide an inspirational or motivational quote."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an inspiring assistant who provides motivational quotes."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            await ctx.send(f"🌟 **Quote:** {reply}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(ChatGPT(bot))
