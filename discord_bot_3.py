import discord
from discord.ext import commands
import random
import requests
import os
import bot_logic_password

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_fox_image_url():
    response = requests.get('https://randomfox.ca/floof/')
    data = response.json()
    return data['image']

@bot.command(name='fox')
async def fox(ctx):
    '''Po wywołaniu polecenia fox program wywołuje funkcję get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"{member.mention} Welcome to the server!")

@bot.command()
async def hello(ctx):
    await ctx.send('Cześć!')

@bot.command()
async def bye(ctx):
    await ctx.send('\U0001f642')

@bot.command()
async def generate_password(ctx, length=8):
    await ctx.send(bot_logic_password.gen_pass(length))

@bot.command()
async def photos_show(ctx):
    nazwy = os.listdir('memes')
    randomowy = random.choice(nazwy)
    with open('memes/' + randomowy, 'rb') as f:
        image = discord.File(f, filename=randomowy)
        await ctx.send(file=image)

bot.run("YOUR TOKEN")
