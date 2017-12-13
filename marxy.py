import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "c mamo?":
        await client.send_message(message.channel, "c mamo :cookie:") #responds with Cookie emoji when someone says "cookie"

client.run("MzkwNTM1MTAyOTM5MTM2MDEw.DRLh1w.du_k9B-x02PiaY4Nq_s0hOWtYO4") #Replace token with your bots token
