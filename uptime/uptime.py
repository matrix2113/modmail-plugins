import discord
from discord.ext import commands
from datetime import datetime

class uptime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.utcnow()

     @commands.command()
     async def uptime(self, ctx):
        """
        Check the bot's uptime
        """
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(f'Uptime is {days}d, {hours}h, {minutes}m, {seconds}s')

def setup(bot):
    bot.add_cog(uptime(bot))
