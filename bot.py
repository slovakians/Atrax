import discord
from discord.ext import commands
import asyncio
import os
import random
import time
import socket
import psutil
import aiohttp
import asyncpraw



# Use an environment variable for security
TOKEN = "TOKEN"

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} ({bot.user.id})")
    await load_commands()
    asyncio.create_task(change_status())  # Use asyncio.create_task instead of loop.create_task

async def load_commands():
    """Automatically loads all .py files in the 'commands' folder"""
    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await bot.load_extension(f"commands.{filename[:-3]}")  # Load cog properly
                print(f"✅ Loaded {filename}")
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")

async def change_status():
    """Rotates bot status messages"""
    while True:
        servers_count = len(bot.guilds)
        statuses = [
            f"🌍 In {servers_count} servers!",
            "⚡ Use !help for commands!",
            f"🚀 Serving {servers_count} communities!"
        ]

        for status in statuses:
            await bot.change_presence(activity=discord.Game(name=status))
            await asyncio.sleep(10)  # Change status every 10 seconds

bot.run(TOKEN)
