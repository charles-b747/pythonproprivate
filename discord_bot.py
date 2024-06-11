import discord
from discord.ext import commands
import bot_logic_password

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.event
async def on_member_join(member):
    channel_id = 1244726414356250634  # Replace with your desired channel ID
    channel = bot.get_channel(channel_id)
    await channel.send(f"{member.mention} Welcome to the server!")

@bot.command()
async def hello(ctx):
    await ctx.send('Cześć!')

@bot.command()
async def bye(ctx):
    await ctx.send('\\U0001f642')

@bot.command()
async def generate_password(ctx, lenght = 8):
    await ctx.send(bot_logic_password.gen_pass(lenght))

bot.run("MTI0NTA1OTgzNzg1OTk5MTY2Ng.GghkO9.ktI3hBbeAEwBdPUVRwk0wYYUsqmxzGzChYhNr0")
