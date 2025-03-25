import discord
from discord.ext import commands
from discord import Embed, Colour
import random

class gun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

    @commands.command()
    async def eightball(self, ctx, *, question=None):
        if not question:
            await ctx.send("🎱 **You need to ask a question!**")
            return

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

    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("🤗 **You need to mention someone to hug!**")
            return

        embed = Embed(
            title="🤗 **Hug**",
            description=f"{ctx.author.mention} hugged {member.mention}!",
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("😘 **You need to mention someone to kiss!**")
            return

        embed = Embed(
            title="😘 **Kiss**",
            description=f"{ctx.author.mention} kissed {member.mention}!",
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def roll(self, ctx):
        embed = Embed(
            title="🎲 **Roll**",
            description=f"You rolled a {random.randint(1, 6)}!",
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def flip(self, ctx):
        result = random.choice(["Heads", "Tails"])
        embed = Embed(
            title="🪙 **Flip**",
            description=f"It's **{result}**!",
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, message=None):
        if not message:
            await ctx.send("📢 **You need to provide a message to say!**")
            return

        embed = Embed(
            description=message,
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = Embed(
            title=f"🖼️ **{member.name}'s Avatar**",
            color=Colour.blue()
        )
        embed.set_image(url=member.display_avatar.url)  # Fixed avatar URL
        await ctx.send(embed=embed)

    @commands.command()
    async def quote(self, ctx):
        quotes = [
            "The best way to predict the future is to create it.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "Do what you can, with what you have, where you are.",
            "Believe you can and you're halfway there.",
            "The only limit to our realization of tomorrow is our doubts of today.",
            "Opportunities don't happen, you create them.",
            "You don’t have to be great to start, but you have to start to be great.",
            "It always seems impossible until it’s done.",
            "Courage is resistance to fear, mastery of fear, not absence of fear.",
            "Dream big and dare to fail.",
            "Life is 10% what happens to us and 90% how we react to it.",
            "Happiness is not something ready-made. It comes from your own actions.",
            "Life isn’t about finding yourself. Life is about creating yourself.",
            "In the middle of every difficulty lies opportunity.",
            "Every moment is a fresh beginning.",
            "Don’t wait for the perfect moment. Take the moment and make it perfect.",
            "Difficulties in life are intended to make us better, not bitter.",
            "Life is what happens when you’re busy making other plans.",
            "Enjoy the little things, for one day you may look back and realize they were the big things.",
            "The best things in life aren’t things."
        ]
        
        embed = Embed(
            title="📜 **Quote**",
            description=random.choice(quotes),
            color=Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def roast(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("🔥 **You need to mention someone to roast!**")
            return

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

    @commands.command()
    async def meme(self, ctx):
        embed = Embed(
            title="🖼️ ERROR",
            description="🚧 The meme command is currently disabled.",
            color=Colour.red()
        )
        await ctx.send(embed=embed)

# Properly registering the cog
async def setup(bot):
    await bot.add_cog(gun(bot))
