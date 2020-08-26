import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import gettable as gt

load_dotenv()
TK=os.getenv('BOT_TOKEN')

client=commands.Bot(command_prefix='o')
@client.event
async def on_ready():
	print('bot is ready')

@client.command()
async def quest(ctx):
	a="bye"
	l=['hi','bye']
	await ctx.send(f"{random.choice(l)} to you {ctx.author.mention}")

@client.command()
async def standings(ctx):
	st=gt.getStandings()
	await ctx.send("```\n"+str(st)+"```")

@client.command()
async def standings_east(ctx):
	st=gt.getStandingsEast()
	await ctx.send("```\n"+str(st)+"```")

@client.command()
async def standings_west(ctx):
	st=gt.getStandingsWest()
	await ctx.send("```\n"+str(st)+"```")

@client.command()
async def teams(ctx):
	st=gt.getTeams()
	await ctx.send("```\n"+str(st)+"```")

@client.command()
async def schedule(ctx):
	st=gt.getSchedule()
	await ctx.send("```\n"+str(st)+"```")

client.run(TK)
