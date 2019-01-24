import discord
import random


client = discord.Client()
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


#when the bot starts
@client.event
async def on_ready():
    #set playing status to Brad is great
    await client.change_presence(game=discord.Game(name="game the bot is playing"))

#when a message is sent in chat
@client.event
async def on_message(message):
    #ignore the message if it originates from the bot
    if message.author == client.user:
        return

    #general channel response
    #if someone types "random user's message" respond with "bot response message"
    if message.content.lower() == "random user's message":
        await client.send_message(message.channel, "bot response message")

    #specific channel response
    #if someone types "k" into chat, respond with "hello other bots" in the channel 513765387943411737, aka bots
    if message.content == "k":
        await client.send_message(discord.Object(id='513765387943411737'), 'hello other bots')

    #react to a specific user
    #if the message author is ABCD#0123, react to the message with a thumbs up
    if str(message.author) == 'ABCD#0123':
        await client.add_reaction(message,'\N{THUMBS UP SIGN}')

    #if "w.claim" or "p!catch" are in a message, send a signal to that channel that the bot is typing
    if "w.claim" in message.content.lower() or "p!catch" in message.content.lower():
        await client.send_typing(message.channel)

client.run(TOKEN)
