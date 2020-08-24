import discord
import random
from discord.ext import commands
client=commands.Bot(command_prefix='o')
@client.event
async def on_ready():
	print('bot is ready')
@client.command()
async def quest(ctx):
	a="bye"
	l=['hi','bye']
	await ctx.send(f"{random.choice(l)} to you {ctx.author.mention}")
client.run('NzM1MTA0MDM3ODI0NzU3ODcw.XxbZew.-RPQCuvVc2RYNHlNKQ-os2Dbf7E')
