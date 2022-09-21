from typing import final
import discord
import os
import random
import time
from trashtalk import get, save
from compliments import getCompliment, saveCompliment
from reminder import getReminder, saveReminder

from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

def substring_after(s, delim):
    return s.partition(delim)[2]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author)
    if message.content.casefold().startswith('hello') or message.content.casefold().startswith('hi'):
        if message.author.id == 487170655725551616:
            await message.channel.send(f"Hello {getCompliment()} <@{message.author.id}>.")
        else:
            trashtalk = get()
            print(f"Hello {trashtalk} <@{message.author}>!")
            await message.channel.send(f"Hello {trashtalk} <@{message.author.id}>!")
    elif message.content.startswith('+tt '):
        msg = message.content
        finalms = substring_after(msg, "+tt ").strip()
        await message.delete()
        if not finalms:
            await message.channel.send(f"WAY SULOD OY USABA!")
            return
        await message.channel.send(f"Uploading {finalms}...", delete_after=1)
        print("Added: "+ finalms)
        save(finalms)
    elif message.content.startswith('+c '):
        msg = message.content
        finalms = substring_after(msg, "+c ").strip()
        await message.delete()
        if not finalms:
            await message.channel.send(f"WAY SULOD OY USABA!")
            return
        await message.channel.send(f"Uploading {finalms}...", delete_after=1)
        print("Added: "+ finalms)
        saveCompliment(finalms)
    elif message.content.startswith('+remind '):
        msg = message.content
        finalms = substring_after(msg, "+remind ").strip()
        if not finalms:
            await message.channel.send(f"WAY SULOD OY USABA!")
            return
        saveReminder(message.author.id, finalms)
client.run(os.getenv('TOKEN'))