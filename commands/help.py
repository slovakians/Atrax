from discord.ext import commands
import discord

class HelpView(discord.ui.View):
    """A custom view for the help dropdown menu."""
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(HelpDropdown())

class HelpDropdown(discord.ui.Select):
    """Dropdown menu to select help categories."""
    def __init__(self):
        options = [
            discord.SelectOption(label="Moderation", value="moderation", description="Commands for moderating the server."),
            discord.SelectOption(label="Fun", value="fun", description="Fun commands to enjoy!"),
            discord.SelectOption(label="Utility", value="utility", description="Useful commands for everyday use."),
            discord.SelectOption(label="Games", value="games", description="Play games with the bot!"),
            discord.SelectOption(label="Music", value="music", description="Commands for playing music."),
            discord.SelectOption(label="Extra", value="extra", description="Additional fun commands.")
        ]
        super().__init__(placeholder="Choose a category...", options=options, custom_id="help_menu")

    async def callback(self, interaction: discord.Interaction):
        category = self.values[0]
        embed = discord.Embed(title=f"📜 **{category.capitalize()} Commands**", color=discord.Colour.blue())

        command_categories = {
            "moderation": [
                ("`!credits`", "Shows credits to the bot creators."),
                ("`!ban <user>`", "Ban a user from the server."),
                ("`!unpanic`", "Unlocks all text channels."),
                ("`!panic`", "Locks all text channels."),
                ("`!kick <user>`", "Kick a user from the server."),
                ("`!mute <user>`", "Mute a user."),
                ("`!unmute <user>`", "Unmute a user."),
                ("`!clear <amount>`", "Clear a number of messages."),
                ("`!warn <user> <reason>`", "Warn a user."),
                ("`!warnings <user>`", "Check a user's warnings."),
                ("`!lock`", "Lock a channel."),
                ("`!unlock`", "Unlock a channel."),
                ("`!roleinfo <role>`", "Get information about a role."),
            ],
            "fun": [
                ("`!meme`", "Get a random meme."),
                ("`!8ball <question>`", "Ask the magic 8-ball a question."),
                ("`!hug <user>`", "Hug a user."),
                ("`!kiss <user>`", "Kiss a user."),
                ("`!roll`", "Roll a dice."),
                ("`!flip`", "Flip a coin."),
                ("`!say <message>`", "Make the bot say something."),
                ("`!avatar <user>`", "Get a user's avatar."),
                ("`!quote`", "Get a random quote."),
                ("`!roast <user>`", "Roast a user."),
            ],
            "utility": [
                ("`!userinfo <user>`", "Get information about a user."),
                ("`!serverinfo`", "Get information about the server."),
                ("`!poll <question>`", "Create a poll."),
                ("`!timer <seconds>`", "Set a timer."),
                ("`!remind <time> <message>`", "Set a reminder."),
                ("`!invite`", "Get the bot's invite link."),
                ("`!ping`", "Check the bot's latency."),
                ("`!calc <expression>`", "Do a quick calculation."),
                ("`!weather <location>`", "Get the weather for a location."),
                ("`!translate <text>`", "Translate text."),
            ],
            "games": [
                ("`!rps <choice>`", "Play Rock-Paper-Scissors."),
                ("`!guess <number>`", "Guess the number."),
                ("`!trivia`", "Answer a trivia question."),
                ("`!hangman`", "Play hangman."),
                ("`!tictactoe <user>`", "Play Tic-Tac-Toe."),
                ("`!blackjack`", "Play Blackjack."),
                ("`!roulette`", "Play Roulette."),
                ("`!slot`", "Play the slot machine."),
                ("`!quiz`", "Start a quiz."),
                ("`!wordle`", "Play Wordle."),
            ],
            "music": [
                ("`!play <song>`", "Play a song."),
                ("`!pause`", "Pause the current song."),
                ("`!resume`", "Resume the paused song."),
                ("`!skip`", "Skip the current song."),
                ("`!stop`", "Stop the music."),
                ("`!queue`", "View the music queue."),
                ("`!volume <level>`", "Set the volume."),
                ("`!nowplaying`", "Show the currently playing song."),
                ("`!shuffle`", "Shuffle the queue."),
                ("`!loop`", "Loop the current song or queue."),
            ],
            "extra": [
                ("`!roast <user>`", "Roast a user."),
                ("`!compliment <user>`", "Compliment a user."),
                ("`!joke`", "Tell a joke."),
                ("`!fact`", "Share a random fact."),
                ("`!cat`", "Get a random cat picture."),
                ("`!dog`", "Get a random dog picture."),
                ("`!meme`", "Get a random meme."),
                ("`!quote`", "Get a random quote."),
                ("`!hack <user>`", "Fake hack a user."),
                ("`!ascii <text>`", "Convert text to ASCII art."),
            ]
        }

        for name, description in command_categories.get(category, []):
            embed.add_field(name=name, value=description, inline=False)

        await interaction.response.edit_message(embed=embed)

class Help(commands.Cog):
    """Help command with a dropdown menu"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        """Sends the help menu with a dropdown selector"""
        embed = discord.Embed(
            title="📜 **Help Menu**",
            description="Select a category from the dropdown below to view commands.",
            color=discord.Colour.blue()
        )
        view = HelpView()
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Help(bot))
