import discord, random
from discord.ext import commands

emojis = ["😎", "😍", "😂", "🥶", "😱", "😳", "🤢", "🥱", "🤐", "🤯", "🤠", "💀", "🤏", "👀", "🌵", "⚡️", "💦", "🎉",
          "🥳", "😈", "🤡","✅","❌","🤔","🙄","🥺","🤧","🆗","💰"]


# testing file lol

class Extra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('fun.py is online')

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'happy birthday' in message.content.lower():
            if not message.author.bot:
                await message.channel.send('Happy Birthday! 🥳')
        if 'i agree' in message.content.lower():
            if not message.author.bot:
                await message.add_reaction("🤡")
                await message.channel.send('LMAO SIMP!!')
        if not message.channel == self.bot.get_channel(697528022307176521):
            if random.randint(0, 100) > 97:
                await message.add_reaction(random.choice(emojis))
        await bot.process_commands(message)


def setup(bot):
    bot.add_cog(Extra(bot))
