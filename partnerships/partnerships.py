import discord

from datetime import datetime
from discord.ext import commands


class Partnerships(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
    
    @commands.group()
    @commands.has_any_role(364843179888869376, 472812430544863235)
    async def partnership(self, ctx):
      if ctx.invoked_subcommand is None:
        return
        
    @partnership.command()
    @commands.has_any_role(364843179888869376, 472812430544863235)
    async def small(self, ctx, user: discord.Member=None):
      await ctx.send("test")
      

def setup(bot):
  bot.add_cog(Partnerships(bot))
