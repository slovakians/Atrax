import discord
import random
import asyncio
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

    @commands.command()
    async def rps(self, ctx, choice: str = None):
        """Play Rock-Paper-Scissors with the bot."""
        choices = ["rock", "paper", "scissors"]
        choice = choice.lower() if choice else None

        if choice not in choices:
            return await ctx.send("❌ Please choose either `rock`, `paper`, or `scissors`.")

        bot_choice = random.choice(choices)
        
        results = {
            ("rock", "scissors"): "You win! 🏆",
            ("paper", "rock"): "You win! 🏆",
            ("scissors", "paper"): "You win! 🏆",
            ("scissors", "rock"): "You lose! 😢",
            ("rock", "paper"): "You lose! 😢",
            ("paper", "scissors"): "You lose! 😢"
        }
        
        result = "It's a tie! 🤝" if choice == bot_choice else results.get((choice, bot_choice))

        embed = discord.Embed(
            title="🎮 **Rock-Paper-Scissors**",
            description=f"You chose **{choice}**. I chose **{bot_choice}**.\n{result}",
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def guess(self, ctx):
        """Guess a number between 1 and 10 with 3 attempts."""
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
                msg = await self.bot.wait_for("message", timeout=30.0, check=check)
                guess = int(msg.content)

                if guess == target:
                    return await ctx.reply(f"🎉 **Correct!** The number was **{target}** in {attempt + 1} attempts!")

                hint = "📉 Too low!" if guess < target else "📈 Too high!"
                await ctx.reply(f"{hint} You have {attempts - attempt - 1} attempts left.")
            except asyncio.TimeoutError:
                return await ctx.reply("⏰ **Time's up!** You took too long to respond.")

        await ctx.reply(f"😢 You're out of attempts! The number was **{target}**.")

    @commands.command()
    async def hangman(self, ctx):
        """Play a game of Hangman with the bot."""
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
                msg = await self.bot.wait_for("message", timeout=30.0, check=check)
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
                return await ctx.send("⏰ **Time's up!** You took too long to respond.")

        if "_" not in guessed:
            await ctx.send(f"🎉 **You won!** The word was **{word}**.")
        else:
            await ctx.send(f"😢 **You lost!** The word was **{word}**.")

    @commands.command()
    async def trivia(self, ctx):
        """Ask a trivia question."""
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
            msg = await self.bot.wait_for("message", timeout=30.0, check=check)
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
            await ctx.send("⏰ **Time's up!** You took too long to respond.")

    @commands.command()
    async def tictactoe(self, ctx, member: discord.Member):
        """Start a game of Tic-Tac-Toe."""
        if member.bot:
            await ctx.send("❌ You can't play against a bot!")
            return

        embed = discord.Embed(
            title="⭕ **Tic-Tac-Toe**",
            description=f"{ctx.author.mention} vs {member.mention}. Game starting soon!",
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def credits(self, ctx):
        """Show bot credits and important links."""
        embed = discord.Embed(
            title="🌟 **Atrax Credits**",
            description="Thank you for using **Atrax**! Here are the credits and some important links:",
            color=discord.Colour.green()
        )
        embed.add_field(name="👑 **Creator**", value="Made by **Purukees**", inline=False)
        embed.add_field(name="🏓 **Bot Ping**", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
        embed.add_field(name="📂 **GitHub Repository**", value="[Atrax on GitHub](https://github.com/slovakians/Atrax)", inline=False)
        embed.add_field(name="📫 **YouTube**", value="[ShadBG on YouTube](https://www.youtube.com/@shadbg)", inline=False)
        embed.add_field(
            name="💡 **Did You Know?**",
            value="Atrax is an open-source Discord bot designed to improve your server experience! Feel free to contribute on GitHub.",
            inline=False
        )
        
        embed.set_thumbnail(url="https://github.com/slovakians/Atrax/blob/main/logo.png?raw=true")
        embed.set_footer(text="Thanks for using Atrax! ❤️")

        await ctx.send(embed=embed)
    
    @commands.command()
    async def guess(self, ctx):
        """Guess a number between 1 and 10 with 3 attempts."""
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
                msg = await self.bot.wait_for("message", timeout=30.0, check=check)
                guess = int(msg.content)

                if guess == target:
                    return await ctx.send(f"🎉 **Correct!** The number was **{target}** in {attempt + 1} attempts!")

                hint = "📉 Too low!" if guess < target else "📈 Too high!"
                await ctx.send(f"{hint} You have {attempts - attempt - 1} attempts left.")
            except asyncio.TimeoutError:
                return await ctx.send("⏰ **Time's up!** You took too long to respond.")

        await ctx.send(f"😢 You're out of attempts! The number was **{target}**.")

    @commands.command()
    async def roulette(self, ctx, bet: str = None):
        if bet not in ["red", "black", "green"]:
            await ctx.send("🎡 **Usage:** `!roulette red/black/green`")
            return

        outcome = random.choices(["red", "black", "green"], weights=[18, 18, 2])[0]  # Green is rarer
        embed = discord.Embed(
            title="🎡 Roulette",
            description=f"**{ctx.author.mention} bet on `{bet}`!**\nThe wheel landed on **{outcome}**!",
            color=discord.Colour.red() if outcome == "red" else discord.Colour.dark_grey() if outcome == "black" else discord.Colour.green()
        )

        if bet == outcome:
            embed.add_field(name="🎉 Winner!", value="You guessed correctly!", inline=False)
        else:
            embed.add_field(name="😢 You lost!", value="Try again!", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def blackjack(self, ctx):
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10s for J, Q, K; 11 for Ace
        user_hand = [random.choice(cards), random.choice(cards)]
        bot_hand = [random.choice(cards), random.choice(cards)]
        
        user_total = sum(user_hand)
        bot_total = sum(bot_hand)
        
        embed = discord.Embed(
            title="🃏 Blackjack",
            description=f"**{ctx.author.mention} plays Blackjack!**\n\n"
                        f"Your Hand: {user_hand} (Total: {user_total})\n"
                        f"Dealer’s Hand: {bot_hand} (Total: {bot_total})",
            color=discord.Colour.green()
        )
        
        if user_total > 21:
            embed.add_field(name="💀 Bust!", value="You went over 21 and lost!", inline=False)
        elif bot_total > 21 or user_total > bot_total:
            embed.add_field(name="🎉 You Win!", value="Congrats!", inline=False)
        elif user_total < bot_total:
            embed.add_field(name="😢 You Lose!", value="Better luck next time!", inline=False)
        else:
            embed.add_field(name="🤝 It's a Tie!", value="Try again!", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def wordle(self, ctx):
        words = ["apple", "grape", "table", "chair", "house"]
        word_to_guess = random.choice(words)
        attempts = 6
        guessed = False
        
        embed = discord.Embed(
            title="🔤 Wordle Game",
            description=f"**{ctx.author.mention}, guess the 5-letter word!**\nYou have **6 attempts**.",
            color=discord.Colour.purple()
        )
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and len(m.content) == 5

        while attempts > 0 and not guessed:
            try:
                msg = await ctx.bot.wait_for("message", check=check, timeout=20)
                guess = msg.content.lower()

                if guess == word_to_guess:
                    guessed = True
                    await ctx.send(f"🎉 **You got it!** The word was `{word_to_guess}`!")
                else:
                    attempts -= 1
                    await ctx.send(f"❌ Wrong guess! You have **{attempts} attempts** left.")
            except:
                await ctx.send(f"⏳ Time's up! The correct word was `{word_to_guess}`.")
                break
        
        if not guessed:
            await ctx.send(f"💀 You ran out of attempts! The correct word was `{word_to_guess}`.")

        # 🎰 SLOT MACHINE
    @commands.command()
    async def slot(self, ctx):
        """Spin a slot machine and see if you win!"""
        slots = ["🍒", "🍋", "🍊", "🍉", "🔔", "⭐", "💎"]
        result = [random.choice(slots) for _ in range(3)]

        embed = discord.Embed(
            title="🎰 Slot Machine",
            description=f"**{ctx.author.mention} spun the slots!**\n`{result[0]} | {result[1]} | {result[2]}`",
            color=discord.Colour.gold()
        )

        if result[0] == result[1] == result[2]:
            embed.add_field(name="🎉 Jackpot!", value="You won big!", inline=False)
        else:
            embed.add_field(name="💀 Better luck next time!", value="Try again!", inline=False)

        await ctx.send(embed=embed)

    # 🎡 ROULETTE
    @commands.command()
    async def roulette(self, ctx, bet: str = None):
        """Play roulette by betting on 'red', 'black', or 'green'."""
        if bet not in ["red", "black", "green"]:
            await ctx.send("🎡 **Usage:** `!roulette red/black/green`")
            return

        outcome = random.choices(["red", "black", "green"], weights=[18, 18, 2])[0]  # Green is rarer
        embed = discord.Embed(
            title="🎡 Roulette",
            description=f"**{ctx.author.mention} bet on `{bet}`!**\nThe wheel landed on **{outcome}**!",
            color=discord.Colour.red() if outcome == "red" else discord.Colour.dark_grey() if outcome == "black" else discord.Colour.green()
        )

        if bet == outcome:
            embed.add_field(name="🎉 Winner!", value="You guessed correctly!", inline=False)
        else:
            embed.add_field(name="😢 You lost!", value="Try again!", inline=False)

        await ctx.send(embed=embed)

    # ❓ QUIZ GAME
    @commands.command()
    async def quiz(self, ctx):
        """Start a fun quiz game!"""
        questions = {
            # 🌍 General Knowledge
            "What is the capital of France?": "paris",
            "Which continent is the largest by area?": "asia",
            "How many colors are in a rainbow?": "7",
            "What is the official language of Brazil?": "portuguese",
            "Which ocean is the largest?": "pacific ocean",
            
            # 🎬 Movies & TV
            "Who played Iron Man in the Marvel movies?": "robert downey jr",
            "What is the name of the wizarding school in Harry Potter?": "hogwarts",
            "Which animated movie features a snowman named Olaf?": "frozen",
            "What is the highest-grossing movie of all time?": "avatar",
            "Which TV show features characters Ross, Rachel, and Chandler?": "friends",

            # 🏆 Sports
            "Which sport is played at Wimbledon?": "tennis",
            "How many players are on a standard soccer team?": "11",
            "Who is known as 'The King' of basketball?": "lebron james",
            "Which country won the FIFA World Cup in 2018?": "france",
            "What is the national sport of Japan?": "sumo wrestling",

            # 🖥️ Science & Tech
            "What does 'CPU' stand for?": "central processing unit",
            "Who invented the telephone?": "alexander graham bell",
            "What planet is known as the Red Planet?": "mars",
            "What is the chemical symbol for gold?": "au",
            "Which element is needed for breathing?": "oxygen",

            # 🎶 Music
            "Who is known as the King of Pop?": "michael jackson",
            "Which British band sang 'Bohemian Rhapsody'?": "queen",
            "What is the name of Billie Eilish’s brother and music collaborator?": "finneas",
            "Which instrument has 88 keys?": "piano",
            "Who sang 'Shape of You'?": "ed sheeran",
            "Who Made The bot? (not capatilize)": "purukees"
        }
        
        question, answer = random.choice(list(questions.items()))
        
        embed = discord.Embed(
            title="❓ Quiz Time!",
            description=f"**{ctx.author.mention}, answer this:**\n\n{question}",
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=20)
            if msg.content.lower() == answer:
                await ctx.send(f"✅ Correct! {ctx.author.mention} got it right! 🎉")
            else:
                await ctx.send(f"❌ Wrong! The correct answer was `{answer}`.")
        except asyncio.TimeoutError:
            await ctx.send(f"⏳ Time's up! The correct answer was `{answer}`.")

async def setup(bot):
    await bot.add_cog(Fun(bot))  # ✅ Load cog properly