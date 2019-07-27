import discord
from discord.ext import commands, Embed
from datetime import datetime
from core.models import PermissionLevel
from core.decorators import trigger_typing
from core import checks

class uptime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
#        bot = self.context.bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    @trigger_typing
    async def uptime(self, ctx):
        """Shows uptime for the bot."""
        embed = Embed(color=self.bot.main_color, timestamp=datetime.utcnow())
        embed.set_author(name="Modmail - Uptime", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        desc = "This is an plugin command used to see how long your bot has been"
        desc += "online since the last restart."
        embed.description = desc

        embed.add_field(name="Uptime", value=self.bot.uptime)
        embed.add_field(name="Plugin Creator", value="[`matrix2113`](https://github.com/matrix2113/modmail-plugins/)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(uptime(bot))
