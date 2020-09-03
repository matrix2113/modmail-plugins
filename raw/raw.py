import discord
from discord.ext import commands


class EmbedRaw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def raw(self, ctx, message_id: int=None)
