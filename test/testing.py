import discord
from discord.ext import commands

class testing(commands.Cog):
    """
    Testing
    """
    def __init__(self, bot):
        
        self.bot = bot

    @commands.group(name="testing", invoke_without_command=True)
    async def testing(self, ctx):
        """Testing Command"""

        await ctx.send_help(ctx.command)
        
    @testing.command(name="testing")
    async def test(self, ctx):
        """Test Command"""
        await ctx.send('Testing Works')

def setup(bot):
    bot.add_cog(testing(bot))
