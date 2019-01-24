import discord
import random


client = discord.Client()
TOKEN = "NTM3ODI4NDgwNTIwNTUyNDY4.Dyq7Xw.6DI8UyqMD5grouAX8MYFsyXIeuk"

@client.event
async def on_ready():
    print("Up and ready sire")
    await client.change_presence(game=discord.Game(name="In development"))

@client.event
async def on_message(message):
    #ignore itself
    if message.author == client.user:
        return
    
client.run(TOKEN)
