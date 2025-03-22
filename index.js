import discord
from discord.ext import commands
from discord import Embed, Colour, SelectOption
from discord.ui import Select, View
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Custom Help Command with Dropdown
@bot.command()
async def help(ctx):
    # Create the embed
    embed = Embed(
        title="📜 **Help Menu**",
        description="Select a category from the dropdown below to view commands.",
        color=Colour.blue()
    )

    # Create the dropdown menu
    select_menu = Select(
        custom_id="help_menu",
        placeholder="Choose a category...",
        options=[
            SelectOption(label="Moderation", value="moderation", description="Commands for moderating the server."),
            SelectOption(label="Fun", value="fun", description="Fun commands to enjoy!"),
            SelectOption(label="Utility", value="utility", description="Useful commands for everyday use."),
            SelectOption(label="Games", value="games", description="Play games with the bot!"),
            SelectOption(label="Music", value="music", description="Commands for playing music."),
            SelectOption(label="Extra", value="extra", description="Additional fun commands.")
        ]
    )

    # Create a view and add the dropdown to it
    view = View()
    view.add_item(select_menu)

    # Send the embed and view
    await ctx.send(embed=embed, view=view)

# Handle dropdown selection
@bot.event
async def on_interaction(interaction):
    if interaction.data.get("custom_id") == "help_menu":
        category = interaction.data["values"][0]
        embed = Embed(title=f"📜 **{category.capitalize()} Commands**", color=Colour.blue())

        if category == "moderation":
            embed.description = "🔨 **Moderation Commands**"
            embed.add_field(name="`!ban <user>`", value="Ban a user from the server.", inline=False)
            embed.add_field(name="`!kick <user>`", value="Kick a user from the server.", inline=False)
            embed.add_field(name="`!mute <user>`", value="Mute a user.", inline=False)
            embed.add_field(name="`!unmute <user>`", value="Unmute a user.", inline=False)
            embed.add_field(name="`!clear <amount>`", value="Clear a number of messages.", inline=False)
            embed.add_field(name="`!warn <user> <reason>`", value="Warn a user.", inline=False)
            embed.add_field(name="`!warnings <user>`", value="Check a user's warnings.", inline=False)
            embed.add_field(name="`!lock`", value="Lock a channel.", inline=False)
            embed.add_field(name="`!unlock`", value="Unlock a channel.", inline=False)
            embed.add_field(name="`!roleinfo <role>`", value="Get information about a role.", inline=False)

        elif category == "fun":
            embed.description = "🎉 **Fun Commands**"
            embed.add_field(name="`!meme`", value="Get a random meme.", inline=False)
            embed.add_field(name="`!8ball <question>`", value="Ask the magic 8-ball a question.", inline=False)
            embed.add_field(name="`!hug <user>`", value="Hug a user.", inline=False)
            embed.add_field(name="`!kiss <user>`", value="Kiss a user.", inline=False)
            embed.add_field(name="`!roll`", value="Roll a dice.", inline=False)
            embed.add_field(name="`!flip`", value="Flip a coin.", inline=False)
            embed.add_field(name="`!say <message>`", value="Make the bot say something.", inline=False)
            embed.add_field(name="`!avatar <user>`", value="Get a user's avatar.", inline=False)
            embed.add_field(name="`!quote`", value="Get a random quote.", inline=False)
            embed.add_field(name="`!roast <user>`", value="Roast a user.", inline=False)

        elif category == "utility":
            embed.description = "🛠️ **Utility Commands**"
            embed.add_field(name="`!userinfo <user>`", value="Get information about a user.", inline=False)
            embed.add_field(name="`!serverinfo`", value="Get information about the server.", inline=False)
            embed.add_field(name="`!poll <question>`", value="Create a poll.", inline=False)
            embed.add_field(name="`!timer <seconds>`", value="Set a timer.", inline=False)
            embed.add_field(name="`!remind <time> <message>`", value="Set a reminder.", inline=False)
            embed.add_field(name="`!invite`", value="Get the bot's invite link.", inline=False)
            embed.add_field(name="`!ping`", value="Check the bot's latency.", inline=False)
            embed.add_field(name="`!calc <expression>`", value="Do a quick calculation.", inline=False)
            embed.add_field(name="`!weather <location>`", value="Get the weather for a location.", inline=False)
            embed.add_field(name="`!translate <text>`", value="Translate text.", inline=False)

        elif category == "games":
            embed.description = "🎮 **Game Commands**"
            embed.add_field(name="`!rps <choice>`", value="Play Rock-Paper-Scissors.", inline=False)
            embed.add_field(name="`!guess <number>`", value="Guess the number.", inline=False)
            embed.add_field(name="`!trivia`", value="Answer a trivia question.", inline=False)
            embed.add_field(name="`!hangman`", value="Play hangman.", inline=False)
            embed.add_field(name="`!tictactoe <user>`", value="Play Tic-Tac-Toe with a friend.", inline=False)
            embed.add_field(name="`!blackjack`", value="Play Blackjack.", inline=False)
            embed.add_field(name="`!roulette`", value="Play Roulette.", inline=False)
            embed.add_field(name="`!slot`", value="Play the slot machine.", inline=False)
            embed.add_field(name="`!quiz`", value="Start a quiz.", inline=False)
            embed.add_field(name="`!wordle`", value="Play Wordle.", inline=False)

        elif category == "music":
            embed.description = "🎵 **Music Commands**"
            embed.add_field(name="`!play <song>`", value="Play a song.", inline=False)
            embed.add_field(name="`!pause`", value="Pause the current song.", inline=False)
            embed.add_field(name="`!resume`", value="Resume the paused song.", inline=False)
            embed.add_field(name="`!skip`", value="Skip the current song.", inline=False)
            embed.add_field(name="`!stop`", value="Stop the music.", inline=False)
            embed.add_field(name="`!queue`", value="View the music queue.", inline=False)
            embed.add_field(name="`!volume <level>`", value="Set the volume.", inline=False)
            embed.add_field(name="`!nowplaying`", value="Show the currently playing song.", inline=False)
            embed.add_field(name="`!shuffle`", value="Shuffle the queue.", inline=False)
            embed.add_field(name="`!loop`", value="Loop the current song or queue.", inline=False)

        elif category == "extra":
            embed.description = "✨ **Extra Fun Commands**"
            embed.add_field(name="`!roast <user>`", value="Roast a user.", inline=False)
            embed.add_field(name="`!compliment <user>`", value="Compliment a user.", inline=False)
            embed.add_field(name="`!joke`", value="Tell a joke.", inline=False)
            embed.add_field(name="`!fact`", value="Share a random fact.", inline=False)
            embed.add_field(name="`!cat`", value="Get a random cat picture.", inline=False)
            embed.add_field(name="`!dog`", value="Get a random dog picture.", inline=False)
            embed.add_field(name="`!meme`", value="Get a random meme.", inline=False)
            embed.add_field(name="`!quote`", value="Get a random quote.", inline=False)
            embed.add_field(name="`!hack <user>`", value="Fake hack a user.", inline=False)
            embed.add_field(name="`!ascii <text>`", value="Convert text to ASCII art.", inline=False)

        await interaction.response.edit_message(embed=embed)

# ------------------------------------------------------------
#       Commands Count : IDK
#  Credits to @slovakians
#  For making the commands
#  Helped by @Mr_Unknown
#
#  Tooked Time to Build
#  1 week , 2 days , idk how many hours
#
#  Line OF Codes
#  825 lines of Codes
#
#  YT: @SHADBG
# ------------------------------------------------------------

# ------------------------------
# Moderation Commands (10)
# ------------------------------

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = Embed(
        title="🔨 **Ban**",
        description=f"{member.mention} has been banned.",
        color=Colour.red()
    )
    if reason:
        embed.add_field(name="Reason", value=reason, inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = Embed(
        title="🔨 **Kick**",
        description=f"{member.mention} has been kicked.",
        color=Colour.red()
    )
    if reason:
        embed.add_field(name="Reason", value=reason, inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, speak=False, send_messages=False)
    await member.add_roles(muted_role, reason=reason)
    embed = Embed(
        title="🔇 **Mute**",
        description=f"{member.mention} has been muted.",
        color=Colour.orange()
    )
    if reason:
        embed.add_field(name="Reason", value=reason, inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(muted_role)
    embed = Embed(
        title="🔊 **Unmute**",
        description=f"{member.mention} has been unmuted.",
        color=Colour.green()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    embed = Embed(
        title="🧹 **Clear**",
        description=f"Cleared {amount} messages.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed, delete_after=5)

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason):
    embed = Embed(
        title="⚠️ **Warn**",
        description=f"{member.mention} has been warned.",
        color=Colour.orange()
    )
    embed.add_field(name="Reason", value=reason, inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def warnings(ctx, member: discord.Member):
    embed = Embed(
        title="⚠️ **Warnings**",
        description=f"{member.mention} has no warnings.",
        color=Colour.orange()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = Embed(
        title="🔒 **Lock**",
        description="This channel has been locked.",
        color=Colour.red()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed = Embed(
        title="🔓 **Unlock**",
        description="This channel has been unlocked.",
        color=Colour.green()
    )
    await ctx.send(embed=embed)

@bot.command()
async def roleinfo(ctx, role: discord.Role):
    embed = Embed(
        title="🎭 **Role Info**",
        description=f"Information about the role **{role.name}**.",
        color=role.color
    )
    embed.add_field(name="ID", value=role.id, inline=False)
    embed.add_field(name="Color", value=str(role.color), inline=False)
    embed.add_field(name="Created At", value=role.created_at.strftime("%Y-%m-%d"), inline=False)
    await ctx.send(embed=embed)

# ------------------------------
# Fun Commands (9)
# ------------------------------



@bot.command()
async def eightball(ctx, *, question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.", "Yes – definitely.",
        "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
        "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    embed = Embed(
        title="🎱 **8Ball**",
        description=f"**Question:** {question}\n**Answer:** {random.choice(responses)}",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def hug(ctx, member: discord.Member):
    embed = Embed(
        title="🤗 **Hug**",
        description=f"{ctx.author.mention} hugged {member.mention}!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx, member: discord.Member):
    embed = Embed(
        title="😘 **Kiss**",
        description=f"{ctx.author.mention} kissed {member.mention}!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def roll(ctx):
    embed = Embed(
        title="🎲 **Roll**",
        description=f"You rolled a {random.randint(1, 6)}!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def flip(ctx):
    result = random.choice(["Heads", "Tails"])
    embed = Embed(
        title="🪙 **Flip**",
        description=f"It's **{result}**!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, message):
    embed = Embed(
        description=message,
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = Embed(
        title=f"🖼️ **{member.name}'s Avatar**",
        color=Colour.blue()
    )
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def quote(ctx):
    quotes = [
        "The best way to predict the future is to create it.",
        "Life is 10% what happens to us and 90% how we react to it.",
        "Do what you can, with what you have, where you are."
    ]
    embed = Embed(
        title="📜 **Quote**",
        description=random.choice(quotes),
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def roast(ctx, member: discord.Member):
    roasts = [
        f"{member.mention}, you're the reason we can't have nice things.",
        f"{member.mention}, you're proof that evolution can go in reverse.",
        f"{member.mention}, you're like a cloud. When you disappear, it's a beautiful day."
    ]
    embed = Embed(
        title="🔥 **Roast**",
        description=random.choice(roasts),
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

# ------------------------------
# Utility Commands (10)
# ------------------------------

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = Embed(
        title=f"👤 **User Info: {member.name}**",
        color=Colour.blue()
    )
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=False)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = Embed(
        title=f"🏰 **Server Info: {guild.name}**",
        color=Colour.blue()
    )
    embed.add_field(name="Members", value=guild.member_count, inline=False)
    embed.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d"), inline=False)
    embed.set_thumbnail(url=guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
async def poll(ctx, *, question):
    embed = Embed(
        title="📊 **Poll**",
        description=question,
        color=Colour.blue()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction("👍")
    await message.add_reaction("👎")

@bot.command()
async def timer(ctx, seconds: int):
    await ctx.send(f"Timer set for {seconds} seconds.")
    await asyncio.sleep(seconds)
    await ctx.send(f"{ctx.author.mention}, your timer is up!")

@bot.command()
async def remind(ctx, time: int, *, reminder):
    await ctx.send(f"Reminder set for {time} minutes.")
    await asyncio.sleep(time * 60)
    await ctx.send(f"{ctx.author.mention}, reminder: {reminder}")

@bot.command()
async def invite(ctx):
    embed = Embed(
        title="📨 **Invite**",
        description="[Click here to invite the bot!](https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot&permissions=8)",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    embed = Embed(
        title="🏓 **Pong!**",
        description=f"Latency: {round(bot.latency * 1000)}ms",
        color=Colour.green()
    )
    await ctx.send(embed=embed)

@bot.command()
async def calc(ctx, *, expression):
    try:
        result = eval(expression)
        embed = Embed(
            title="🧮 **Calculator**",
            description=f"**Result:** {result}",
            color=Colour.blue()
        )
    except:
        embed = Embed(
            title="🧮 **Calculator**",
            description="Invalid expression.",
            color=Colour.red()
        )
    await ctx.send(embed=embed)

@bot.command()
async def weather(ctx, *, location):
    embed = Embed(
        title="☀️ **Weather**",
        description=f"Weather for {location} not implemented yet.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def translate(ctx, *, text):
    embed = Embed(
        title="🌍 **Translate**",
        description="Translation feature not implemented yet.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

# ------------------------------
# Games Commands (10)
# ------------------------------

@bot.command()
async def rps(ctx, choice: str):
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)
    result = ""
    if choice.lower() == bot_choice:
        result = "It's a tie!"
    elif (choice.lower() == "rock" and bot_choice == "scissors") or \
         (choice.lower() == "paper" and bot_choice == "rock") or \
         (choice.lower() == "scissors" and bot_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"
    embed = Embed(
        title="🎮 **Rock-Paper-Scissors**",
        description=f"You chose **{choice}**. I chose **{bot_choice}**. {result}",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def guess(ctx, number: int):
    target = random.randint(1, 10)
    if number == target:
        embed = Embed(
            title="🎯 **Guess the Number**",
            description=f"Congratulations! You guessed the number **{target}**!",
            color=Colour.green()
        )
    else:
        embed = Embed(
            title="🎯 **Guess the Number**",
            description=f"Sorry, the number was **{target}**. Try again!",
            color=Colour.red()
        )
    await ctx.send(embed=embed)

@bot.command()
async def trivia(ctx):
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the largest planet in the solar system?", "answer": "Jupiter"}
    ]
    q = random.choice(questions)
    embed = Embed(
        title="❓ **Trivia**",
        description=q["question"],
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def hangman(ctx):
    words = ["python", "discord", "bot", "programming"]
    word = random.choice(words)
    embed = Embed(
        title="🪓 **Hangman**",
        description=f"The word has {len(word)} letters. Guess a letter!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def tictactoe(ctx, member: discord.Member):
    embed = Embed(
        title="⭕ **Tic-Tac-Toe**",
        description=f"{ctx.author.mention} vs {member.mention}. Game starting soon!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def blackjack(ctx):
    embed = Embed(
        title="🃏 **Blackjack**",
        description="Blackjack game starting soon!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def roulette(ctx):
    embed = Embed(
        title="🎰 **Roulette**",
        description="Roulette game starting soon!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def slot(ctx):
    embed = Embed(
        title="🎰 **Slot Machine**",
        description="Slot machine game starting soon!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def quiz(ctx):
    embed = Embed(
        title="📚 **Quiz**",
        description="Quiz game starting soon!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def wordle(ctx):
    embed = Embed(
        title="🔠 **Wordle**",
        description="Wordle game starting soon!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

# ------------------------------
# Music Commands (10)
# ------------------------------

@bot.command()
async def play(ctx, *, song):
    embed = Embed(
        title="🎵 **Play**",
        description=f"Now playing: **{song}**",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def pause(ctx):
    embed = Embed(
        title="🎵 **Pause**",
        description="Music paused.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def resume(ctx):
    embed = Embed(
        title="🎵 **Resume**",
        description="Music resumed.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def skip(ctx):
    embed = Embed(
        title="🎵 **Skip**",
        description="Skipped the current song.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def stop(ctx):
    embed = Embed(
        title="🎵 **Stop**",
        description="Music stopped.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def queue(ctx):
    embed = Embed(
        title="🎵 **Queue**",
        description="Here's the current queue:",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def volume(ctx, level: int):
    embed = Embed(
        title="🎵 **Volume**",
        description=f"Volume set to **{level}%**.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def nowplaying(ctx):
    embed = Embed(
        title="🎵 **Now Playing**",
        description="Currently playing: **Song Name**",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def shuffle(ctx):
    embed = Embed(
        title="🎵 **Shuffle**",
        description="Queue shuffled.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def loop(ctx):
    embed = Embed(
        title="🎵 **Loop**",
        description="Looping the current song.",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

# ------------------------------
# Extra Fun Commands (8)
# ------------------------------

@bot.command()
async def compliment(ctx, member: discord.Member):
    compliments = [
        f"{member.mention}, you're amazing!",
        f"{member.mention}, you're the best!",
        f"{member.mention}, you're a star!"
    ]
    embed = Embed(
        title="✨ **Compliment**",
        description=random.choice(compliments),
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def joke(ctx):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]
    embed = Embed(
        title="😂 **Joke**",
        description=random.choice(jokes),
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def fact(ctx):
    facts = [
        "Honey never spoils.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries aren't."
    ]
    embed = Embed(
        title="📚 **Fact**",
        description=random.choice(facts),
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
    embed = Embed(
        title="🐱 **Cat**",
        description="Here's a random cat picture!",
        color=Colour.blue()
    )
    embed.set_image(url="https://cataas.com/cat")
    await ctx.send(embed=embed)

@bot.command()
async def dog(ctx):
    embed = Embed(
        title="🐶 **Dog**",
        description="Here's a random dog picture!",
        color=Colour.blue()
    )
    embed.set_image(url="https://dog.ceo/api/breeds/image/random")
    await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
    memes = ["https://example.com/meme1.jpg", "https://example.com/meme2.jpg"]
    embed = Embed(
        title="😂 **Meme**",
        color=Colour.blue()
    )
    embed.set_image(url=random.choice(memes))
    await ctx.send(embed=embed)


@bot.command()
async def hack(ctx, member: discord.Member):
    embed = Embed(
        title="💻 **Hack**",
        description=f"Hacking {member.mention}... Just kidding!",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def ascii(ctx, *, text):
    embed = Embed(
        title="🔠 **ASCII Art**",
        description=f"```\n{text}\n```",
        color=Colour.blue()
    )
    await ctx.send(embed=embed)




bot.run('TOKEN IN HERE')
