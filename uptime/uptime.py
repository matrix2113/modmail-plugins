import discord
from discord.ext import commands
from discord import Embed
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
        """Shows information about this bot."""
        embed = Embed(color=self.bot.main_color, timestamp=datetime.utcnow())
        embed.set_author(name="Modmail - About", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        desc = "This is an open source Discord bot that serves as a means for "
        desc += "members to easily communicate with server administrators in "
        desc += "an organised manner."
        embed.description = desc

        embed.add_field(name="Uptime", value=self.bot.uptime)
        embed.add_field(name="Latency", value=f"{self.bot.latency * 1000:.2f} ms")
        embed.add_field(name="Version", value=f"`{self.bot.version}`")
        embed.add_field(name="Author", value="[`kyb3r`](https://github.com/kyb3r)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(uptime(bot))
