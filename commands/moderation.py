import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}  # Dictionary to store warnings (Use a database for persistence)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unpanic(self, ctx):
        guild = ctx.guild
        everyone_role = guild.default_role

        for channel in guild.text_channels:
            await channel.set_permissions(everyone_role, send_messages=True)

        embed = discord.Embed(
            title="🔓 **Server Unlocked**",
            description="All text channels have been unlocked. Use `!panic` to lock them.",
            color=discord.Colour.green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def panic(self, ctx):
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

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="🔨 **Ban**",
            description=f"{member.mention} has been banned.",
            color=discord.Colour.red()
        )
        if reason:
            embed.add_field(name="Reason", value=reason, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="🔨 **Kick**",
            description=f"{member.mention} has been kicked.",
            color=discord.Colour.red()
        )
        if reason:
            embed.add_field(name="Reason", value=reason, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, send_messages=False)

        await member.add_roles(muted_role, reason=reason)
        embed = discord.Embed(
            title="🔇 **Mute**",
            description=f"{member.mention} has been muted.",
            color=discord.Colour.orange()
        )
        if reason:
            embed.add_field(name="Reason", value=reason, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            embed = discord.Embed(
                title="🔊 **Unmute**",
                description=f"{member.mention} has been unmuted.",
                color=discord.Colour.green()
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} is not muted.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(
            title="🧹 **Clear**",
            description=f"Cleared {amount} messages.",
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed, delete_after=5)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        if member.id not in self.warnings:
            self.warnings[member.id] = []
        self.warnings[member.id].append(reason)

        embed = discord.Embed(
            title="⚠️ **Warn**",
            description=f"{member.mention} has been warned.",
            color=discord.Colour.orange()
        )
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Total Warnings", value=len(self.warnings[member.id]), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def warnings(self, ctx, member: discord.Member):
        warns = self.warnings.get(member.id, [])
        if warns:
            description = "\n".join([f"🔹 {warn}" for warn in warns])
        else:
            description = "No warnings found."

        embed = discord.Embed(
            title="⚠️ **Warnings**",
            description=f"{member.mention} warnings:\n{description}",
            color=discord.Colour.orange()
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(
            title="🔒 **Lock**",
            description="This channel has been locked.",
            color=discord.Colour.red()
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(
            title="🔓 **Unlock**",
            description="This channel has been unlocked.",
            color=discord.Colour.green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def roleinfo(self, ctx, role: discord.Role):
        embed = discord.Embed(
            title="🎭 **Role Info**",
            description=f"Information about the role **{role.name}**.",
            color=role.color
        )
        embed.add_field(name="ID", value=role.id, inline=False)
        embed.add_field(name="Color", value=str(role.color), inline=False)
        embed.add_field(name="Created At", value=role.created_at.strftime("%Y-%m-%d"), inline=False)
        await ctx.send(embed=embed)


# Setup function for adding the cog to the bot
async def setup(bot):
    await bot.add_cog(Moderation(bot))
