__authors__ = 'Intron014'

import discord
from discord.ext import commands
import traceback
import sys
import os
import json

def gettoken():
    token_file = open("token.txt", "r")
    token_string = token_file.read()
    token_token = token_string.split("\n")
    bot_token = str(token_token[0])
    return bot_token

bot_token = gettoken()

description = "Da simple bot for da simple life"
bot = commands.Bot(command_prefix=["."], description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_ready():
    activity = discord.Game(name="Netflix", type=3)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a test"))
    #await bot.change_presence(activity=discord.Game(name="a game"))
    #await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    print("Bot is ready!")

bot.run(bot_token)