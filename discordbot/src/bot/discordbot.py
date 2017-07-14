import discord
from discord.ext import commands
import logging


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


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
async def joinchannel():
    """ Commands the bot to join the current channel """
    channel = client.get_channel('id')
    await bot.join_voice_channel(channel)
    
@bot.command()
async def exitchannel():
    """ Commands the bot to leave the current channel """
    await bot.disconnect()
    
bot.run('MzM1Mjg0MzE0MzA2NjQxOTIy.DEnlPA.xd1-kcQ5LqMdiEJOP3Fl6ReopoE')