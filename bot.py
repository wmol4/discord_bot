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
    if "back" in message.content.lower():
        if message.author.voice.voice_channel != None:
            voice_client = await client.join_voice_channel(message.author.voice_channel)
            random_length = randint(2, 10)
            time.sleep(random_length)
            msg = 'back'
            await client.send_message(message.channel, msg)
            time.sleep(5)
            await voice_client.disconnect()
            

client.run({token})
