import discord

from discord.ext import commands
from datetime import datetime

from core import checks
from core.models import PermissionLevel


class Banno(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def andybanno(self, ctx, reporter: int, reporting: int, *, reason: str=None):
        await ctx.message.delete()
        ending_msg = f"""Reporter: {reporter}\nReporting: {reporting}\n\n{reason}"""
        chn_id = 390434979282157568
        banno_id = 672691818219044872
        embed = discord.Embed(description=ending_msg, timestamp=datetime.utcnow())
        embed.set_footer(text="brought to you by andy")
        chn = await self.bot.fetch_channel(chn_id)
        banno = await self.bot.fetch_channel(banno_id)
        await banno.send(ending_msg)
        await chn.send(f"<@!332196248993923073>\n```>>ban {reporting} // You may appeal here -> https://ays.gg/ban-appeal```")
  
  
def setup(bot):
    bot.add_cog(Banno(bot))
    
