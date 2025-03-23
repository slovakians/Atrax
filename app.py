#-------------------------------------------
#
# Fun fact when just editing this file it 
# Crashed my browser btw its 1039 lines
# of code btw 
#
#-------------------------------------------

import discord
from discord.ext import commands
from discord import Embed, Colour, SelectOption
from discord.ui import Select, View
import random
import yt_dlp as youtube_dl
import asyncio

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
            embed.add_field(name="`!credits`", value="Shows credits to the guys who made the bot.", inline=False)
            embed.add_field(name="`!ban <user>`", value="Ban a user from the server.", inline=False)
            embed.add_field(name="`!unpanic`", value="Unlocks all text channels in the server", inline=False)
            embed.add_field(name="`!panic`", value="Locks all text channels in the server.", inline=False)
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
@commands.has_permissions(administrator=True)
async def unpanic(ctx):
    guild = ctx.guild
    everyone_role = guild.default_role

    for channel in guild.text_channels:
        await channel.set_permissions(everyone_role, send_messages=True)

    embed = discord.embed(
        title="🔓 **Server Unlocked**",
        description="All text channels have been unlocked. Use `!panic` to lock them.",
        color=discord.Colour.green()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True) 
async def panic(ctx):
    guild = ctx.guild
    everyone_role = guild.default_role

    
    for channel in guild.text_channels:
        await channel.set_permissions(everyone_role, send_messages=False)

    embed = discord.Embed(
        title="🔒 **Server Locked**",
        description="All text channels have been locked. Use `!unpanic` to unlock them.",
        color=discord.Colour.red()
    )
    await ctx.send(embed=embed)

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
        f"{member.mention}, your secrets are safe with me. I never even listen when you tell them.",
        f"{member.mention}, your family tree must be a cactus because everybody on it is a prick.",
        f"{member.mention}, you bring everyone so much joy... when you leave the room.",
        f"{member.mention}, your birth certificate is an apology letter from the condom factory.",
        f"{member.mention}, if you were any slower, you’d be moving backward.",
        f"{member.mention}, your WiFi signal is stronger than your personality.",
        f"{member.mention}, you have something on your chin... no, the third one down.",
        f"{member.mention}, I’d agree with you, but then we’d both be wrong.",
        f"{member.mention}, you bring people together… to talk about how annoying you are.",
        f"{member.mention}, you have something on your face… oh wait, that’s just your face.",
        f"{member.mention}, you have something on your mind. I hope it’s a brain.",
        f"{member.mention}, I’d call you a tool, but even tools are useful.",
        f"{member.mention}, I was hoping for a battle of wits, but you appear to be unarmed.",
        f"{member.mention}, you make onions cry.",
        f"{member.mention}, I’d explain it to you, but I left my crayons at home.",
        f"{member.mention}, your voice is proof that sound can be annoying.",
        f"{member.mention}, I’d give you a nasty look, but you already have one.",
        f"{member.mention}, your parents must be so proud… of your siblings.",
        f"{member.mention}, you have something on your shoe… oh, it’s just your personality.",
        f"{member.mention}, you’re like a cloud—when you disappear, it’s a beautiful day.",
        f"{member.mention}, you should carry a plant around to replace the oxygen you waste.",
        f"{member.mention}, if brains were taxed, you’d get a refund.",
        f"{member.mention}, your handshake is weaker than your WiFi signal.",
        f"{member.mention}, your personality is like a Windows error—frustrating and unavoidable.",
        f"{member.mention}, your confidence is inspiring, considering how little reason you have for it.",
        f"{member.mention}, your ideas are like software bugs—annoying and hard to fix.",
        f"{member.mention}, even Wikipedia doesn’t want to cite you.",
        f"{member.mention}, your common sense is on the endangered species list.",
        f"{member.mention}, you were the kid in school who tried to high-five himself.",
        f"{member.mention}, your intelligence is like a soap bubble—there for a second and then gone.",
        f"{member.mention}, your brain is so small, it has its own gravitational pull.",
        f"{member.mention}, if sarcasm was a degree, you'd still fail.",
        f"{member.mention}, even a magic 8-ball gives better advice than you.",
        f"{member.mention}, your thoughts are like a loading screen—always buffering.",
        f"{member.mention}, if your personality was a TV show, it would be canceled after one episode.",
        f"{member.mention}, your insults are so weak, even autocorrect ignores them.",
        f"{member.mention}, your jokes are like Windows updates—nobody likes them, but we have to sit through them.",
        f"{member.mention}, your sense of humor is so bad, even dad jokes reject you.",
        f"{member.mention}, if dumb was a sport, you’d have a gold medal.",
        f"{member.mention}, if you had a dollar for every bad decision, you’d own a mansion.",
        f"{member.mention}, your brain runs on trial software.",
        f"{member.mention}, you’re proof that some people peak in elementary school.",
        f"{member.mention}, your thoughts are so slow, snails are taking notes.",
        f"{member.mention}, even your pet is embarrassed to be seen with you.",
        f"{member.mention}, your brain is like an abandoned theme park—empty and full of bad ideas.",
        f"{member.mention}, if patience was a currency, you'd be broke.",
        f"{member.mention}, you remind me of a cloud—when you go away, it’s a better day.",
        f"{member.mention}, I’d give you a piece of my mind, but I’m afraid you’d lose it.",
        f"{member.mention}, you should come with a warning label.",
        f"{member.mention}, your brain must be on airplane mode.",
        f"{member.mention}, if you were a fruit, you’d be a rotten banana.",
        f"{member.mention}, you’re like a penny—two-faced and not worth much.",
        f"{member.mention}, if intelligence was a currency, you'd be in eternal debt.",
        f"{member.mention}, you’re about as useful as a screen door on a submarine.",
        f"{member.mention}, your thoughts are like a Windows update—laggy and unnecessary.",
        f"{member.mention}, you bring people together… to collectively ignore you.",
        f"{member.mention}, your thoughts are so slow, even dial-up internet feels faster.",
        f"{member.mention}, even a broken clock is right twice a day—what's your excuse?",
        f"{member.mention}, if stupidity was a superpower, you’d be the main character.",
        f"{member.mention}, your intelligence is like a soap bubble—there for a second and then gone.",
        f"{member.mention}, if your common sense was money, you'd be bankrupt.",
        f"{member.mention}, your jokes are so bad they make fortune cookies cringe.",
        f"{member.mention}, if I had a dollar for every smart thing you said, I’d be broke.",
        f"{member.mention}, your logic is like a screen door on a submarine.",
        f"{member.mention}, if boredom had a mascot, it would be you.",
        f"{member.mention}, your social skills are like dial-up internet—painfully slow.",
        f"{member.mention}, if you had any less personality, you'd be a rock.",
        f"{member.mention}, you’re the reason why mute buttons exist.",
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
    embed = discord.Embed(
        title=f"👤 **User Info: {member.name}**",
        color=discord.Colour.blue()
    )
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=False)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
    
    # Handle avatar URL
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    embed.set_thumbnail(url=avatar_url)
    
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild

    # Server features
    features = "\n".join([f"✅ {feature}" for feature in guild.features]) if guild.features else "❌ No special features"

    # Channel counts
    text_channels = len(guild.text_channels)
    voice_channels = len(guild.voice_channels)

    # Verification level
    verification_level = str(guild.verification_level).capitalize()

    # Member counts
    total_members = guild.member_count
    bots = sum(member.bot for member in guild.members)
    humans = total_members - bots

    # Roles
    roles = len(guild.roles)

    # Server creation date
    created_at = guild.created_at.strftime("%m/%d/%Y, %I:%M %p")

    # Server icon URL
    icon_url = guild.icon.url if guild.icon else "https://discord.com/assets/1f0bfc0865d324c2587920a7d80c609b.png"

    # Embed
    embed = discord.Embed(
        title=f"🏰 **Server Info: {guild.name}**",
        color=discord.Colour.blue()
    )
    embed.add_field(name="Owner", value=guild.owner, inline=False)
    embed.add_field(name="Features", value=features, inline=False)
    embed.add_field(name="Channels", value=f"🎆 {text_channels}\n🔊 {voice_channels}", inline=False)
    embed.add_field(name="Info", value=f"Verification Level: {verification_level}", inline=False)
    embed.add_field(name="Icon Link", value=f"[Click Here]({icon_url})", inline=False)
    embed.add_field(name="Prefixes", value="`!`", inline=False)  # Customize prefixes as needed
    embed.add_field(name="Members", value=f"Total: {total_members}\nHumans: {humans}\nBots: {bots}", inline=False)
    embed.add_field(name="Roles", value=f"{roles} roles", inline=False)
    embed.add_field(name="Image", value=f"ID: {guild.id}, Created • {created_at}", inline=False)
    
    # Set thumbnail
    embed.set_thumbnail(url=icon_url)

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
        description="[Click here to invite the bot!](https://discord.com/oauth2/authorize?client_id=1350697653075185684&scope=bot&permissions=8)",
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

# 1. Rock-Paper-Scissors
@bot.command()
async def rps(ctx, choice: str = None):
    choices = ["rock", "paper", "scissors"]
    if not choice or choice.lower() not in choices:
        await ctx.send("❌ Please choose either `rock`, `paper`, or `scissors`.")
        return

    bot_choice = random.choice(choices)
    choice = choice.lower()

    if choice == bot_choice:
        result = "It's a tie!"
    elif (choice == "rock" and bot_choice == "scissors") or \
         (choice == "paper" and bot_choice == "rock") or \
         (choice == "scissors" and bot_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    embed = discord.Embed(
        title="🎮 **Rock-Paper-Scissors**",
        description=f"You chose **{choice}**. I chose **{bot_choice}**. {result}",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

# 2. Guess the Number
@bot.command()
async def guess(ctx):
    target = random.randint(1, 10)
    attempts = 3

    embed = discord.Embed(
        title="🎯 **Guess the Number**",
        description="I'm thinking of a number between 1 and 10. You have 3 attempts!",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

    for attempt in range(attempts):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        try:
            msg = await bot.wait_for("message", timeout=30.0, check=check)
            guess = int(msg.content)

            if guess == target:
                embed = discord.Embed(
                    title="🎯 **Correct!**",
                    description=f"Congratulations! You guessed the number **{target}** in {attempt + 1} attempts!",
                    color=discord.Colour.green()
                )
                await ctx.send(embed=embed)
                return
            else:
                hint = "Too high!" if guess > target else "Too low!"
                await ctx.send(f"❌ {hint} You have {attempts - attempt - 1} attempts left.")
        except asyncio.TimeoutError:
            await ctx.send("⏰ Time's up! You took too long to respond.")
            return

    await ctx.send(f"😢 You're out of attempts! The number was **{target}**.")

# 3. Trivia
@bot.command()
async def trivia(ctx):
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the largest planet in the solar system?", "answer": "Jupiter"}
    ]
    q = random.choice(questions)
    correct_answer = q["answer"]

    embed = discord.Embed(
        title="❓ **Trivia**",
        description=q["question"],
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        if msg.content.lower() == correct_answer.lower():
            response_embed = discord.Embed(
                title="✅ **Correct!**",
                description=f"Great job! The correct answer is **{correct_answer}**.",
                color=discord.Colour.green()
            )
        else:
            response_embed = discord.Embed(
                title="❌ **Incorrect!**",
                description=f"Sorry, the correct answer is **{correct_answer}**.",
                color=discord.Colour.red()
            )
        await ctx.send(embed=response_embed)
    except asyncio.TimeoutError:
        await ctx.send("⏰ Time's up! You took too long to respond.")

# 4. Hangman
@bot.command()
async def hangman(ctx):
    words = ["python", "discord", "bot", "programming"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6

    embed = discord.Embed(
        title="🪓 **Hangman**",
        description=f"The word has {len(word)} letters. Guess a letter!\n`{' '.join(guessed)}`",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

    while attempts > 0 and "_" in guessed:
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and len(m.content) == 1

        try:
            msg = await bot.wait_for("message", timeout=30.0, check=check)
            letter = msg.content.lower()

            if letter in word:
                for i, char in enumerate(word):
                    if char == letter:
                        guessed[i] = letter
                await ctx.send(f"✅ Correct! `{' '.join(guessed)}`")
            else:
                attempts -= 1
                await ctx.send(f"❌ Incorrect! You have {attempts} attempts left.")
        except asyncio.TimeoutError:
            await ctx.send("⏰ Time's up! You took too long to respond.")
            return

    if "_" not in guessed:
        await ctx.send(f"🎉 You won! The word was **{word}**.")
    else:
        await ctx.send(f"😢 You lost! The word was **{word}**.")

# 5. Tic-Tac-Toe
@bot.command()
async def tictactoe(ctx, member: discord.Member):
    if member.bot:
        await ctx.send("❌ You can't play against a bot!")
        return

    embed = discord.Embed(
        title="⭕ **Tic-Tac-Toe**",
        description=f"{ctx.author.mention} vs {member.mention}. Game starting soon!",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

# 6. Blackjack
@bot.command()
async def blackjack(ctx):
    embed = discord.Embed(
        title="🃏 **Blackjack**",
        description="Blackjack game starting soon!",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

# 7. Roulette
@bot.command()
async def roulette(ctx):
    embed = discord.Embed(
        title="🎰 **Roulette**",
        description="Roulette game starting soon!",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

# 8. Slot Machine
@bot.command()
async def slot(ctx):
    embed = discord.Embed(
        title="🎰 **Slot Machine**",
        description="Slot machine game starting soon!",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

# 9. Quiz
@bot.command()
async def quiz(ctx):
    embed = discord.Embed(
        title="📚 **Quiz**",
        description="Quiz game starting soon!",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

# 10. Wordle
@bot.command()
async def wordle(ctx):
    embed = discord.Embed(
        title="🔠 **Wordle**",
        description="Wordle game starting soon!",
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)
# credits
@bot.command()
async def credits(ctx):
    embed = discord.Embed(
        title="🌟 **Atrax Credits**",
        description="Thank you for using **Atrax**! Here are the credits and some important links:",
        color=discord.Colour.green()
    )
    embed.add_field(
        name="👑 **Creator**",
        value="Made by **Purukees**",
        inline=False
    )
    embed.add_field(
        name="🏓 **Bot Ping**",
        value=f"{round(bot.latency * 1000)}ms",
        inline=False
    )
    embed.add_field(
        name="📂 **GitHub Repository**",
        value="[Atrax on GitHub](https://github.com/slovakians/Atrax)",
        inline=False
    )
    embed.add_field(
        name="📫 **YouTube**",
        value="[ShadBG on YouTube](https://www.youtube.com/@shadbg)",
        inline=False
    )
    embed.add_field(
        name="💡 **Did You Know?**",
        value="Atrax is an open-source Discord bot designed to make your server experience better! Feel free to contribute to the project on GitHub.",
        inline=False
    )
    embed.set_thumbnail(url="https://files.oaiusercontent.com/file-LzmTjU7M3x95dLMNpbDgev?se=2025-03-22T11%3A49%3A34Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Db4ecad7e-bee1-49e2-8007-3a752dbfe659.webp&sig=ntkZWKNSsizzB/ft2RmxWSzWVafGk2xgKpdPxNGTfHA%3D")
    embed.set_footer(text="Thanks for using Atrax! ❤️")

    await ctx.send(embed=embed)


# ------------------------------
# Music Commands (10)
# ------------------------------

# Music Queue
queue = []
loop = False

# YouTube DL Options
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # Bind to IPv4
    'cookiefile': 'cookies.txt'  # Add this line to use cookies
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

# Play Command
@bot.command()
async def play(ctx, *, url):
    if not ctx.author.voice:
        await ctx.send("You are not connected to a voice channel.")
        return

    channel = ctx.author.voice.channel

    if not ctx.voice_client:
        await channel.connect()
    elif ctx.voice_client.channel != channel:
        await ctx.send("I'm already in another voice channel.")
        return

    async with ctx.typing():
        try:
            player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
            queue.append(player)
            if not ctx.voice_client.is_playing():
                play_next(ctx)
            await ctx.send(f"Added to queue: **{player.title}**")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

# Pause Command
@bot.command()
async def pause(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("Music paused.")
    else:
        await ctx.send("No music is currently playing.")

# Resume Command
@bot.command()
async def resume(ctx):
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Music resumed.")
    else:
        await ctx.send("Music is not paused.")

# Skip Command
@bot.command()
async def skip(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Skipped the current song.")
    else:
        await ctx.send("No music is currently playing.")

# Stop Command
@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        await ctx.voice_client.disconnect()
        queue.clear()
        await ctx.send("Music stopped and disconnected.")
    else:
        await ctx.send("I'm not in a voice channel.")

# Queue Command
@bot.command()
async def queue_cmd(ctx):
    if not queue:
        await ctx.send("The queue is empty.")
    else:
        queue_list = "\n".join([f"{i + 1}. {song.title}" for i, song in enumerate(queue)])
        await ctx.send(f"**Queue:**\n{queue_list}")

# Now Playing Command
@bot.command()
async def nowplaying(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        await ctx.send(f"Now playing: **{ctx.voice_client.source.title}**")
    else:
        await ctx.send("No music is currently playing.")

# Volume Command
@bot.command()
async def volume(ctx, volume: int):
    if ctx.voice_client:
        if 0 <= volume <= 100:
            ctx.voice_client.source.volume = volume / 100
            await ctx.send(f"Volume set to **{volume}%**.")
        else:
            await ctx.send("Volume must be between 0 and 100.")
    else:
        await ctx.send("I'm not in a voice channel.")

# Shuffle Command
@bot.command()
async def shuffle(ctx):
    if queue:
        random.shuffle(queue)
        await ctx.send("Queue shuffled.")
    else:
        await ctx.send("The queue is empty.")

# Loop Command
@bot.command()
async def loop_cmd(ctx):
    global loop
    loop = not loop
    await ctx.send(f"Looping {'enabled' if loop else 'disabled'}.")

# Helper function to play the next song
def play_next(ctx):
    if queue:
        player = queue.pop(0)
        ctx.voice_client.play(player, after=lambda e: play_next(ctx) if loop or queue else None)
        asyncio.run_coroutine_threadsafe(ctx.send(f"Now playing: **{player.title}**"), bot.loop)
    elif ctx.voice_client:
        asyncio.run_coroutine_threadsafe(ctx.voice_client.disconnect(), bot.loop)


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




bot.run('TOKEN IN HERE BOI')
