import discord
from discord.ext import commands
from discord import Embed, Colour
import asyncio
import random
import time
import socket
import psutil
import aiohttp
import re

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        """Get user information."""
        member = member or ctx.author
        embed = discord.Embed(
            title=f"👤 **User Info: {member.name}**",
            color=discord.Colour.blue()
        )
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=False)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
        
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        embed.set_thumbnail(url=avatar_url)
        
        await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        """Show server information."""
        guild = ctx.guild
        features = "\n".join([f"✅ {feature}" for feature in guild.features]) if guild.features else "❌ No special features"

        embed = discord.Embed(
            title=f"🏰 **Server Info: {guild.name}**",
            color=discord.Colour.blue()
        )
        embed.add_field(name="Owner", value=guild.owner, inline=False)
        embed.add_field(name="Features", value=features, inline=False)
        embed.add_field(name="Members", value=f"👥 {guild.member_count}", inline=False)
        embed.add_field(name="Created On", value=guild.created_at.strftime("%m/%d/%Y, %I:%M %p"), inline=False)
        
        icon_url = guild.icon.url if guild.icon else "https://discord.com/assets/1f0bfc0865d324c2587920a7d80c609b.png"
        embed.set_thumbnail(url=icon_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def poll(self, ctx, *, question=None):
        """Create a simple poll."""
        if not question:
            await ctx.send("📊 **You need to provide a question for the poll!**")
            return

        embed = Embed(
            title="📊 **Poll**",
            description=question,
            color=Colour.blue()
        )
        message = await ctx.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

    @commands.command()
    async def timer(self, ctx, seconds: int):
        """Set a timer."""
        if seconds <= 0:
            await ctx.send("⏳ **Time must be greater than zero!**")
            return
        
        await ctx.send(f"⏳ **Timer set for {seconds} seconds!**")
        await asyncio.sleep(seconds)
        await ctx.send(f"⏰ {ctx.author.mention}, your timer is up!")

    @commands.command()
    async def remind(self, ctx, time: int, *, reminder=None):
        """Set a reminder."""
        if time <= 0:
            await ctx.send("⏳ **Time must be greater than zero!**")
            return
        if not reminder:
            await ctx.send("🔔 **You need to specify what to remind you about!**")
            return

        await ctx.send(f"🔔 **Reminder set for {time} minutes!**")
        await asyncio.sleep(time * 60)
        await ctx.send(f"🔔 {ctx.author.mention}, reminder: {reminder}")

    @commands.command()
    async def invite(self, ctx):
        """Get the bot's invite link."""
        embed = Embed(
            title="📨 **Invite**",
            description="[Click here to invite the bot!](https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot&permissions=8)",
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    start_time = time.time()

    @commands.command()
    async def ping(self, ctx):
        """Show bot latency, system info, and uptime."""
        node = socket.gethostname()
        uptime = time.time() - self.start_time
        uptime_str = f"{int(uptime // 3600)}h {int((uptime % 3600) // 60)}m {int(uptime % 60)}s"
        cpu_usage = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        ram_usage = ram.percent
        total_ram = round(ram.total / (1024**3), 2)
        used_ram = round(ram.used / (1024**3), 2)

        embed = Embed(
            title="🏓 **Pong!**",
            description=f"**Latency:** `{round(self.bot.latency * 1000)}ms`\n"
                        f"📍 **Node:** `{node}`\n"
                        f"🕒 **Uptime:** `{uptime_str}`\n"
                        f"⚙️ **CPU Usage:** `{cpu_usage}%`\n"
                        f"💾 **RAM Usage:** `{ram_usage}%` ({used_ram}GB / {total_ram}GB)",
            color=Colour.green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def calc(self, ctx, *, expression):
        """Simple calculator."""
        try:
            if re.search(r"[a-zA-Z]", expression):
                raise ValueError("Invalid input")

            result = eval(expression)
            embed = Embed(
                title="🧮 **Calculator**",
                description=f"**Result:** `{result}`",
                color=Colour.blue()
            )
        except:
            embed = Embed(
                title="🧮 **Calculator**",
                description="⚠️ **Invalid expression!**",
                color=Colour.red()
            )
        await ctx.send(embed=embed)

    @commands.command()
    async def weather(self, ctx, *, location):
        """Fetch weather information."""
        from web import search
        try:
            response = search(f"current weather in {location}")
            embed = Embed(
                title=f"🌤️ **Weather in {location}**",
                description=f"**Response:** {response}",
                color=Colour.blue()
            )
            await ctx.send(embed=embed)
        except:
            await ctx.send("⚠️ **Could not fetch weather data. Try again later.**")

    @commands.command()
    async def translate(self, ctx, lang: str = None, *, text: str = None):
        """Translate text to another language."""
        from web import search
        if not lang or not text:
            await ctx.send("🌍 **Usage: !translate [language] [text]**")
            return

        try:
            response = search(f"translate '{text}' to {lang}")
            embed = Embed(
                title="🌍 **Translation**",
                description=f"**Original:** {text}\n**Translated:** {response}",
                color=Colour.blue()
            )
            await ctx.send(embed=embed)
        except:
            await ctx.send("⚠️ **Could not translate. Try again later.**")

async def setup(bot):
    await bot.add_cog(Utility(bot))  # ✅ Properly load the cog
