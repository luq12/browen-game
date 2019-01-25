import discord
import random


client = discord.Client()
TOKEN = "NTM3ODI4NDgwNTIwNTUyNDY4.Dyq7Xw.6DI8UyqMD5grouAX8MYFsyXIeuk"

@client.event
async def on_ready():
    print("Up and ready sire")
    await client.change_presence(game=discord.Game(name="In development"))

class Item:
    def __init__(self, itemID):
        self.itemID = itemID

    def set_name(self, name):
        self.name = name

    def set_weight(self, weight):
        self.weight = weight
        
    def set_value(self, value):
        self.value = value

    def get_info(self):
        print("Item: " + self.name)
        print("Weight: " + self.weight)
        print("Value: " + self.value + "gp")
        
class Player:
    def __init__(self, playerID):
        self.playerID = playerID

    def generate_character(self):
        self.name = "Mysterious Stranger"
        self.hp = 100
        self.athletics = 10
        self.personality = 10
        self.dexterity = 10
        self.acuity = 10

    def set_name(self, name):
        self.name = name

    def set_athletics(self, athletics):
        self.athletics = athletics
        
    def set_personality(self, personality):
        self.personality = personality
        
    def set_dexterity(self, dexterity):
        self.dexterity = dexterity
        
    def set_acuity(self, acuity):
        self.acuity = acuity

    def set_hp(self,hp):
        self.hp = hp
        
@client.event
async def on_message(message):
    #ignore itself
    if message.author == client.user:
        return


client.run(TOKEN)
