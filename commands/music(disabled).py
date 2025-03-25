import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, song=None):
        embed = discord.Embed(
            title="🎵 **Music System Disabled**",
            description="Oops! The **music commands** are currently **disabled** due to a technical issue. 🚧",
            color=discord.Colour.red()
        )
        embed.add_field(name="🔧 **We're Working on It!**", value="Im Finding A Way To Fix This Issue! 🎶", inline=False)
        embed.set_footer(text="Thank you for your patience! ❤️")
        await ctx.send(embed=embed)

    @commands.command()
    async def pause(self, ctx):
        await self.play(ctx)

    @commands.command()
    async def resume(self, ctx):
        await self.play(ctx)

    @commands.command()
    async def skip(self, ctx):
        await self.play(ctx)

    @commands.command()
    async def stop(self, ctx):
        await self.play(ctx)

    @commands.command()
    async def queue(self, ctx):
        await self.play(ctx)

    @commands.command()
    async def volume(self, ctx, level=None):
        await self.play(ctx)

    @commands.command()
    async def nowplaying(self, ctx):
        await self.play(ctx)

    @commands.command()
    async def shuffle(self, ctx):
        await self.play(ctx)

    @commands.command()
    async def loop(self, ctx):
        await self.play(ctx)

async def setup(bot):
    await bot.add_cog(Music(bot))  # ✅ Load cog properly
