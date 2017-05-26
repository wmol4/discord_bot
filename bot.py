import discord
import asyncio
import time
from discord.ext import commands
import random
from random import randint

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('back'):
        random_length = randint(2, 10)
        time.sleep(random_length)
        msg = 'back'
        await client.send_message(message.channel, msg)

client.run({token})
