import discord

from discord.ext import commands, tasks

lgs = 797985158191775754

class LatencyTest(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
    @commands.command()
    async def pingstest(self, ctx):
      print("i work")
      
    @tasks.loop(hours=1.0)
    async def latency_return(self):
      chn = self.bot.fetch_channel(lgs)
      embed = discord.Embed(
          title="WS Latency",
          description=f"{self.bot.ws.latency * 1000:.4f} ms",
          color=self.bot.main_color,
        )
      return await ctx.send(embed=embed)
      print("latency returned successfully")
      
      
def setup(bot):
  bot.add_cog(LatencyTest())
