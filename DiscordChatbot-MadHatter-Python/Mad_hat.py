#Name: Dustin Shaw
#Purpose: The purpose of this program is to create a discord chatbot that qoutes Alice in Wonderland's MadHatter when called

import discord
import random 
import time

#token for bot communication
TOKEN = ''


client = discord.Client()

#defined variables for qoute purposes

qouteList = []

#defining the qoutes and then appending them to qouteList
worldQoute = """If I had a world of my own, everything would be nonsense. \n Nothing would be what it is, because everything would be what it isn't. \n And contrary wise, what is, it wouldn't be. \n And what it wouldn't be, it would. You see?"""
peopleThink = "People who don't think shouldn't talk."
mmmm = "One to be a murderer. One to be a martyr. One to be a Monarch. One to go Mad."
madQuestion = "Have I gone mad?"
bonkers = "You're entirely bonkers. But I'll tell you a secret all the best people are."
sentences = "I'm going to give you a sentence, a full sentence with a noun \n a verb and a posible agitate. I don't like all these judges running \n around with their half baked sentences, \n thats how you get salmonella poisoning."
bloodSweatTea = "Blood, sweat and tea, sister! That's what it takes to achieve all great and terrible things."
notRight = "Just because I'm mad doesn't mean I'm not right."


qouteList.append(worldQoute)
qouteList.append(peopleThink)
qouteList.append(mmmm)
qouteList.append(madQuestion)
qouteList.append(bonkers)
qouteList.append(bloodSweatTea)
qouteList.append(notRight)



@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hatter'):
        await message.channel.send(qouteList[random.randint(0,6)])

client.run(TOKEN)