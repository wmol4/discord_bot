import discord
import asyncio
import time
from discord.ext import commands
import random
from random import randint

client = discord.Client()

@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return
        if "back" in message.content.lower():
            if message.author.voice.voice_channel != None:
                random_length = randint(10, 30)
                time.sleep(random_length)
                voice_client = await client.join_voice_channel(message.author.voice_channel)
                msg = 'back'
                await client.send_message(message.channel, msg)
                time.sleep(10)
                await voice_client.disconnect()
        if "loot" in message.content.lower():
            random_length = randint(100, 300)
            time.sleep(random_length)
            msg = '~loot'
            await client.send_message(message.channel, msg)
    except:
        True
            

client.run({token})
