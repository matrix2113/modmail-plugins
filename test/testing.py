import discord
from discord.ext import commands

class testing(commands.Cog):
    """
    Testing
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="testing", invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def dbug(self, ctx):
        """Testing Command"""

        await ctx.send_help(ctx.command)
        
    @testing.command(name="testing")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def test(self, ctx):
        """Test Command"""
        await ctx.send('Testing Works')

def setup(bot):
    bot.add_cog(testing(bot))
