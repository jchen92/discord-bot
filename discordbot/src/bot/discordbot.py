import discord
from discord.ext import commands
from opus_loader import load_opus_lib
import logging


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


load_opus_lib()


description = '''Example bot!'''

bot = commands.Bot(command_prefix='!', description=description)
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command()
async def add(left : int, right : int):
    """ Adds two numbers together.""" 
    await bot.say(left + right)
    
@bot.command()
async def joinvoice():
    """ Commands the bot to join the General channel """
    channel = discord.Object(id='168807126389620738')
    await bot.join_voice_channel(channel)
    
@bot.command(pass_context = True)
async def exitvoice(ctx):
    """ Commands the bot to leave the all channels """
    for x in bot.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
    
    return await bot.say("I am not connected to any voice channel on this server!")

    
bot.run('MzM1Mjg0MzE0MzA2NjQxOTIy.DEnlPA.xd1-kcQ5LqMdiEJOP3Fl6ReopoE')