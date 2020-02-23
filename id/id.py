import discord
from discord.ext import commands


class ThreadID(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
		
	@commands.command()
	async def id(self, ctx):
		"""Returns the Recipient's ID"""
		await ctx.send(ctx.thread.id)
		

def setup(bot):
	bot.add_cog(ThreadID(bot))
