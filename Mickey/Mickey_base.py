import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

global money
money = 250

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print("ID")
    print(client.user.id)
    print("Ready to use!")
    
    await client.change_presence(game=discord.Game(name='Been serving Ahmed since day 1'))
    
# PING AND 8BALL COMMAND
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!ping"):
        emb = (discord.Embed(title=":ping_pong: **Ping**",description="PONG!...Did that take long? :smiley:",colour = 0x3df270))
        await client.send_message(message.channel, embed=emb)
    elif message.content.startswith("!8ball"):
        emb = (discord.Embed(title=':8ball: **8ball**',description=random.choice(["It is certain :8ball:",
                                                                        "It is decidedly so :8ball:",
                                                                        "Yes, definitely :8ball:",
                                                                        "You may rely on it :8ball:",
                                                                        "As i see it, yes :8ball:",
                                                                        "Most likely :8ball:",
                                                                        "Outlook good :8ball:",
                                                                        "Yes :8ball:",
                                                                        "Signs point to yes :8ball:",
                                                                        "Reply hazy try again :8ball:",
                                                                        "Ask again later :8ball:",
                                                                        "Better not tell you now :8ball:",
                                                                        "Cannot predict now :8ball:",
                                                                        "Concentrate and ask again :8ball:",
                                                                        "Don't count on it :8ball:",
                                                                        "My reply is no :8ball:",
                                                                        "My sources say no :8ball:",
                                                                        "Outlook not so good :8ball:",
                                                                        "Very doubtful :8ball:"]),colour = 0x3df270))
        await client.send_message(message.channel, embed=emb)
    elif message.content.startswith("!rps"):
        
        await client.send_message(message.channel, user)
# JOIN AND LEAVE MESSAGE
@client.event
async def on_member_join(member):
    channel = member.server.get_channel("519241179142029324")
    emb =  (discord.Embed(title=":wave: **Welcome**",description="Welcome to {1.name}, {0.mention}, enjoy your stay mate".format(member, member.server),colour = 0x3df270))
    await client.send_message(channel, embed=emb)
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("519241179142029324")
    emb =  (discord.Embed(title=":middle_finger: **Bye**",description="I never liked you {0.mention}... sleep with you left eye opened...".format(member, member.server),colour = 0x3df270))
    await client.send_message(channel, embed=emb)
# BALANCE MESSAGE
@client.event
async def on_message(message):
    if message.author == client.user:
        return   
    elif message.content.startswith("!bal"):        
        emb = (discord.Embed(title =":moneybag: **Balance**",description="Your balance is currently : $",colour = 0x3df270))
        await client.send_message(message.channel, embed = emb)
        

        
client.run("NTE5MjM5ODYyNzkzMjczMzk2.DuccDQ.4w1WuS2XAfjtjodNWcjX7I17VvY")
