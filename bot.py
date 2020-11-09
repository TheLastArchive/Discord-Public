import discord
from discord.ext import commands, tasks
import re
from random import randint


client = commands.Bot(command_prefix = "//")

@client.event
async def on_ready():
    
    daily_video.start()
    print("The bot is doing stuff.")


@client.event
async def on_message(message):
    """Deletes Counting Wins YT link"""

    if message.author == client.user:
        return

    print("Counting wins check")
    if 'https://www.youtube.com/watch?v=QiDqntDy39U' in message.content: 
        await message.delete()
        print("Counting Wins deleted")
        return
    
    """Sends a peeposalute whenever someone says 'goodnight'"""        
    print("Goodnight check")
    gn = re.compile('goodnight|good night|gn')
    if gn.search(message.content.lower()): 
        await message.channel.send('<:peepoSalute:665687773407215637>')
        print('peepo has saluted')
        return
    
    """Checks the new-uploads channel, reacts to any new messages as well as grabbing the video URL"""
    print("Checking if channel is #new-uploads")
    if message.channel.id == 447206848030965760:
        with open('s0urvideos.txt', 'a') as f:
            f.write(message.content + '\n')
            print("New video added to list")
        with open('s0urvideos.txt', 'r') as f:
            videos = f.readlines()
            print(videos[-1])
        message.add_reaction('<:Wowee:592122719546638408>')
        return


@tasks.loop(hours=24)
async def daily_video():
    """Sends a random S0ur video in #general daily"""

    with open('s0urvideos.txt', 'r') as f:
        videos = f.readlines()

    target_general_id = 314631937899757579
    general_id = client.get_channel(target_general_id)
    await general_id.send(videos[randint(0, len(videos) - 1)])
    print("Daily S0ur video sent")
    print(videos[-1])


client.run()