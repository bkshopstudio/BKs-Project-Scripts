import discord
from discord.ext import commands

intents = discord.Intents.default() 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot Online: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")


bot.run("MTMyNjYyOTk0NzMzODY1NzgzNA.G63EvH.sEQVzg1O7gs2YtcRLXL80IsB-Xt6VP4kw1dkkc") 
