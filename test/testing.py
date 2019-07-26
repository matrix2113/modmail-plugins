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
    
    @commands.command()
    async def testing(self, ctx):
        await ctx.send('Testing works')

def setup(bot):
    bot.add_cog(testing(bot))
