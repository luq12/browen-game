import discord
import random

client = discord.Client()
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

@client.event
async def on_ready():
    #Game status
    await client.change_presence(game=discord.Game(name="Rolling some dice"))

@client.event
async def on_message(message):
    #ignore itself
    if message.author == client.user:
        return
    
@client.event
async def on_message(message):
    if message.content[:6] == "%roll ":
        roll = message.content #variable to hold user input
        rolls = [] #array to hold dice output
        if roll.count('d') == 1:
            dice = roll.find('d')
            number_of_dice = roll[6:dice]
            number_of_dice = int(number_of_dice)
            die_to_roll = roll[dice+1:]
            die_to_roll = int(die_to_roll)
            for x in range(number_of_dice):
                 rolls.append(random.randint(1,die_to_roll))
            await client.send_message(message.channel, rolls)
            await client.send_message(message.channel, "Sum: " + str(sum(rolls)))
            await client.send_message(message.channel, "Average: " + str(((die_to_roll+1)/2)*(number_of_dice)))
        if roll.count('d') == 2:
            dice = roll.find('d')
            dice_dropped = roll.find('d', dice+1) #finds the second 'd', where the number of dropped dice is listed
            number_dice_dropped = roll[dice_dropped+1:]
            number_dice_dropped = int(number_dice_dropped)
            number_of_dice = roll[6:dice]
            number_of_dice = int(number_of_dice)
            die_to_roll = roll[dice+1:dice_dropped]
            die_to_roll = int(die_to_roll)
            for x in range(number_of_dice):
                 rolls.append(random.randint(1,die_to_roll))
            for x in range(number_dice_dropped):
                rolls.remove(min(rolls))
            await client.send_message(message.channel, rolls)
            await client.send_message(message.channel, "Sum: " + str(sum(rolls)))
            await client.send_message(message.channel, "Average: " + str(((die_to_roll+1)/2)*(number_of_dice-number_dice_dropped)))

client.run(TOKEN)
