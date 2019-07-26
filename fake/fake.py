import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self,bot):
      self.bot = bot
      
    @commands.command()
    async def purge(self,ctx):
        """
        Purge Command
        """
        await ctx.send('Purge Testing')
        
def setup(bot):
    bot.add_cog(Moderation(bot))
