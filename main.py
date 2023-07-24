import discord
from discord.ext import commands
import dc_bot_token


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send("Ben supra mk4 bot! Stutututututututuutututututututu")

@bot.command()
async def supra(ctx):
    supra_mk4 = open("supra.txt","r",encoding="utf-8")
    await ctx.send(supra_mk4.read())
    supra_mk4.close()

@bot.command()
async def photo(ctx):
    with open("supra.jpg","rb") as f:
        supra_photo = discord.File(f)
    await ctx.send(file=supra_photo)

@bot.command()
async def sound(ctx):
    with open("stututu.mp3","rb") as f:
        supra_sound = discord.File(f)
    await ctx.send(file=supra_sound)


bot.run(dc_bot_token.token)
