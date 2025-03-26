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
        f"{member.mention}, you make the world a better place! 🌍",
        f"{member.mention}, you're incredibly talented! 🎨",
        f"{member.mention}, your kindness is inspiring! ❤️",
        f"{member.mention}, if you were a vegetable, you'd be a cute-cumber! 🥒",
        f"{member.mention}, you have the best laugh! 😂",
        f"{member.mention}, you bring joy just by being you! 💕",
        f"{member.mention}, you're like a cloud—fluffy, wonderful, and full of good vibes! ☁️",
        f"{member.mention}, if awesomeness was a currency, you’d be a billionaire! 💰",
        f"{member.mention}, you have a heart of gold! 💛",
        f"{member.mention}, I’d agree with you even if you were wrong... because you’re just that cool! 😎",
        f"{member.mention}, the world would be 1000% better if more people were like you! 🌍💖",
        f"{member.mention}, if you were a Pokémon, you’d be Pikachu because you always brighten my day! ⚡",
        f"{member.mention}, you deserve all the cookies in the world! 🍪",
        f"{member.mention}, you have the perfect balance of cool and adorable! 🧊🐻",
        f"{member.mention}, NASA is still trying to figure out how you shine brighter than the sun! ☀️",
        f"{member.mention}, if they had a contest for being amazing, you'd take first place every time! 🏆",
        f"{member.mention}, your vibes are so good, even WiFi signals want to connect with you! 📶",
        f"{member.mention}, if kindness was a superpower, you'd be the strongest hero in the universe! 🦸",
        f"{member.mention}, you have more charm than a box of lucky charms! 🍀",
        f"{member.mention}, you’re like a limited edition—one of a kind and incredibly special! 💎",
        f"{member.mention}, even Google couldn’t find anyone cooler than you! 🌐",
        f"{member.mention}, you have a face that makes baby pandas jealous of your cuteness! 🐼",
        f"{member.mention}, you bring more smiles than a puppy playing in a pile of leaves! 🍂🐶",
        f"{member.mention}, I’d trade all my in-game loot just to make you smile! 🎮❤️",
        f"{member.mention}, even a broken clock is right twice a day, but you're amazing **all the time**! ⏰🔥",
        f"{member.mention}, the sun called… it said you outshine it! ☀️😎",
        f"{member.mention}, if happiness was an Olympic sport, you’d take gold! 🏅",
        f"{member.mention}, if life was a video game, you’d be the main character! 🎮👑",
        f"{member.mention}, you’re like WiFi… because I feel lost without you! 📡💕",
        f"{member.mention}, you radiate the kind of energy that even Monday mornings can’t ruin! 🌞☕",
        f"{member.mention}, even superheroes would be jealous of your awesomeness! 🦸‍♂️",
        f"{member.mention}, if good vibes were a currency, you’d be richer than Elon Musk! 💸"
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
        "I told my wife she should embrace her mistakes. She gave me a hug. 🤦‍♂️",
        "Parallel lines have so much in common. It’s a shame they’ll never meet. 📏",
        "Why don’t eggs tell jokes? Because they might crack up! 🥚😂",
        "I’m reading a book on anti-gravity. It’s impossible to put down! 📖🚀",
        "I told my suitcase that there will be no vacations this year. Now I’m dealing with emotional baggage. 🧳😢",
        "Why do cows have hooves instead of feet? Because they lactose. 🐄🥛",
        "How do you organize a space party? You planet! 🪐🎉",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾🏆",
        "Why couldn’t the bicycle stand up by itself? It was two-tired! 🚲",
        "I used to be addicted to soap, but I’m clean now. 🧼😂",
        "What do you call fake spaghetti? An impasta! 🍝",
        "Why was the math book sad? It had too many problems. 📖➕➗",
        "I would tell you a chemistry joke, but I know I wouldn’t get a reaction. 🧪",
        "What did one ocean say to the other ocean? Nothing, they just waved! 🌊👋",
        "I told my friend 10 jokes to make him laugh. Sadly, no pun in ten did. 🤷‍♂️",
        "What do you call a belt made out of watches? A waist of time! ⏳",
        "Why did the golfer bring an extra pair of pants? In case he got a hole in one! ⛳",
        "What do you get when you cross a snowman and a vampire? Frostbite! ⛄🧛",
        "Why don’t scientists trust atoms? Because they make up everything! ⚛️"
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
            "Water makes up about 60% of your body weight!"
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
        embed = Embed(
            title="🐱 **Random Cat**",
            color=Colour.purple()
        )
        embed.set_image(url=response[0]["url"])
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        """Sends a random dog picture."""
        response = requests.get("https://dog.ceo/api/breeds/image/random").json()
        embed = Embed(
            title="🐶 **Random Dog**",
            color=Colour.purple()
        )
        embed.set_image(url=response["message"])
        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        """Sends a random meme."""
        response = requests.get("https://meme-api.com/gimme").json()
        embed = Embed(
            title=f"🤣 **{response['title']}**",
            color=Colour.red()
        )
        embed.set_image(url=response["url"])
        await ctx.send(embed=embed)

@commands.command()
async def fact(self, ctx):
    """Shares a random fun fact."""
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible! 🍯",
        "Octopuses have three hearts and their blood is blue due to the presence of copper-based hemocyanin. 🐙💙",
        "Bananas are berries, but strawberries aren’t! 🍌🍓",
        "Water can boil and freeze at the same time under certain conditions called the triple point. ❄️🔥",
        "A day on Venus is longer than a year on Venus. 🌌",
        "The inventor of the Frisbee was turned into a Frisbee after he passed away. 🥏",
        "Sharks existed before trees! 🌲🦈",
        "A single cloud can weigh more than a million pounds. ☁️⚖️",
        "Cows have best friends and get stressed when separated. 🐄💖",
        "There's enough DNA in your body to stretch from the Sun to Pluto and back—17 times! 🧬",
        "Butterflies can taste with their feet. 🦋👣",
        "Sloths can hold their breath longer than dolphins—up to 40 minutes! 🦥🌊",
        "The Eiffel Tower can be 15 cm taller during the summer due to metal expansion. 🗼",
        "A group of flamingos is called a 'flamboyance.' 🦩🔥",
        "Wombat poop is cube-shaped so it doesn’t roll away. 🦛🔲",
        "Tigers have striped skin, not just striped fur. 🐅",
        "There’s an island in Japan full of bunnies called Okunoshima. 🏝️🐰",
        "Bananas glow blue under black light due to their natural ripening process. 🍌🔵",
        "Coconuts kill more people each year than sharks do. 🥥🦈",
        "Your brain generates enough electricity to power a small light bulb. 💡🧠"
    ]

    embed = Embed(
        title="📚 **Random Fact**",
        description=random.choice(facts),
        color=Colour.blue()
    )
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

# Registering the cog
async def setup(bot):
    bot.add_cog(FunCommands(bot))
