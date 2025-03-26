import discord
from discord.ext import commands
from discord import Embed, Colour
import random
import requests
import pyfiglet  # Required for ASCII art generation

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

    @commands.command()
    async def compliment(self, ctx, member: discord.Member = None):
        """Sends a nice compliment to the mentioned user."""
        if not member:
            await ctx.send("💖 **You need to mention someone to compliment!**")
            return

        compliments = [
            f"{member.mention}, you light up the room! ✨",
            f"{member.mention}, you're an amazing person! 🌟",
            f"{member.mention}, if awesomeness was a currency, you’d be a billionaire! 💰",
            f"{member.mention}, the sun called… it said you outshine it! ☀️😎",
        ]

        embed = Embed(
            title="💖 **Compliment**",
            description=random.choice(compliments),
            color=Colour.green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def joke(self, ctx):
        """Tells a random joke."""
        jokes = [
            "Why don’t skeletons fight each other? Because they don’t have the guts! 💀",
            "Why don’t eggs tell jokes? Because they might crack up! 🥚😂",
        ]

        embed = Embed(
            title="😂 **Random Joke**",
            description=random.choice(jokes),
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def fact(self, ctx):
        """Shares a random fact."""
        facts = [
            "Honey never spoils. You could eat 3000-year-old honey!",
            "Octopuses have three hearts!",
            "Bananas are berries, but strawberries aren’t!",
        ]

        embed = Embed(
            title="🤓 **Random Fact**",
            description=random.choice(facts),
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        """Sends a random cat picture."""
        response = requests.get("https://api.thecatapi.com/v1/images/search").json()
        embed = Embed(title="🐱 **Random Cat**", color=Colour.purple())
        embed.set_image(url=response[0]["url"])
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        """Sends a random dog picture."""
        response = requests.get("https://dog.ceo/api/breeds/image/random").json()
        embed = Embed(title="🐶 **Random Dog**", color=Colour.purple())
        embed.set_image(url=response["message"])
        await ctx.send(embed=embed)

    @commands.command()
    async def hack(self, ctx, member: discord.Member = None):
        """Fake hacks a user for fun."""
        if not member:
            await ctx.send("💻 **You need to mention someone to hack!**")
            return
        
        messages = [
            f"🔍 Hacking {member.mention}'s account...",
            "🔑 Stealing password...",
            "💳 Accessing bank details...",
            "📂 Downloading private files...",
            "✅ Hack complete! Just kidding! 😆"
        ]

        embed = Embed(
            title="💻 **Fake Hack**",
            description="\n".join(messages),
            color=Colour.dark_red()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def ascii(self, ctx, *, text=None):
        """Converts text into ASCII art."""
        if not text:
            await ctx.send("🔠 **You need to provide text to convert!**")
            return

        ascii_text = pyfiglet.figlet_format(text)
        if len(ascii_text) > 2000:
            await ctx.send("⚠️ **ASCII text is too long! Try a shorter phrase.**")
            return
        
        await ctx.send(f"```\n{ascii_text}\n```")

async def setup(bot):
    """Loads the FunCommands cog properly."""
    await bot.add_cog(FunCommands(bot))
