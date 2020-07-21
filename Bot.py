import discord
import asyncio
from discord.ext import commands
client=commands.Bot(command_prefix='.')
@client.event
async def on_ready():
	print('bot is ready')
client.run('NzM1MTA0MDM3ODI0NzU3ODcw.XxbZew.-RPQCuvVc2RYNHlNKQ-os2Dbf7E')
