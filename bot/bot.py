import discord
import random
import time
import os
from datetime import datetime #for datetime
from pytz import timezone #for timezone
from discord.ext import commands, tasks #import the commands from discord extension
from itertools import cycle #import to create a cycle on bot status

client = commands.Bot(command_prefix = 'b.') #defines the command to client (if used BOT instead of client the declaration should be named bot)
status = cycle(['type b.help', 'bot by: Lust#4444', 'type b.help', 'bot by: Lust#4444', 'I see you'])
client.remove_command('help') #removes default help command


#Load message
@client.event
async def on_ready():
    change_status.start()
    print(f'bot: {client.user} is now online!')

#list of all commands: help, ping, 8ball <question>, clear <qnt>, italy, other names

#change bot game status
@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#ping tester
@client.command()
async def ping(ctx): #parameter
    await ctx.send(f'`Ping: {round (client.latency * 1000)} ms`')

#command error (does not exist)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command.')

#custom help command
@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Commands list',
        colour = discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://i.ibb.co/S7mKyfQ/123.jpg')
    embed.add_field(name='Admin', value='clear')
    embed.add_field(name='Basic', value='help\nping\nitaly')
    embed.add_field(name='Fun', value='8 ball\nnames')
    embed.set_footer(text='bot by Lust#4444')
    await ctx.send(embed=embed)

#names commands
@client.command()
async def names(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='Names', value='baruel\nbruno\ncat\ndaniel\nfelipe\ngiovanna\nhiter\nleo\npv\nwilly', inline=False)
    await ctx.send(embed=embed)

#8ball command
@client.command(aliases=['8ball']) #use to set a list that can run a command
async def _8ball(ctx, *, question): #you can't start a command with number
    responses = ['Com certeza!',
                'Não sei, pergunta pro leo.',
                'Que tipo de pergunta é essa?',
                'Sim!',
                'Não!',
                'kkkkk ele não sabe xD',
                'que soninho... me pergunte novamente mais tarde.',
                'que pergunta merda, parabéns.',
                'Não tenho certeza.',
                'Talvez sim, talvez não.',
                'Dúvido muito.',
                'Quem sabe :)',
                'Essa é uma boa pergunta, eu não sei te responder.',
                'Pra você a resposta é não.',
                'Pra você a resposta é não.',
                'Esquece a pergunta te achei gatinha rsrs.',
                'Não vou falar ^^',
                'Pode confiar nisso.',
                'Segundo meu horóscopo... não posso te responder.',
                'CLARO QUE SIM!',
                'Se fosse o baruel perguntando eu diria que sim.',
                'sim... não... quem sabe...',
                'sim e eu amo muito o leleo.',
                'Obrigado por perguntar, SIM!',
                'Obrigado por perguntar, NAO!',
                'desculpa por ser bot :('
                'pergunta pro cat, ele sabe a resposta certa']
    await ctx.send(f'Pergunta: {question}\nResposta: {random.choice(responses)}')

#join command
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    print(channel.id)
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

#clear <qnt> command -> defined to role named a
@client.command()
@commands.has_role('a')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount + 1)
    await ctx.send(f'Total messages deleted: {amount}')
    time.sleep(3)
    await ctx.channel.purge(limit = 1)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Correct use: b.clear <qntd>')

#names commands
@client.command()
async def hiter(ctx):
    await ctx.send('Lindo, maravilhoso e cheiroso!')

@client.command()
async def bruno(ctx):
    await ctx.send('mto zika')

@client.command()
async def giovanna(ctx):
    await ctx.send('Rainha da programação, merece o mundo! princesa manda salve rsrs')

@client.command()
async def baruel(ctx):
    await ctx.send('por favor baruel, para de mandar gif merda')

@client.command()
async def cat(ctx):
    await ctx.send('Deboche, ironia e ódio gratuito')

@client.command()
async def felipe(ctx):
    await ctx.send('Dançando kpop olhando pra baixo pra ver o leo')

@client.command()
async def pv(ctx):
    embed = discord.Embed(
        title = 'pvtdo <3 khitara',
        description = 'foi mal daniel',
        colour = discord.Colour.blue()
    )
    embed.set_image(url='https://i.makeagif.com/media/10-09-2015/-vktJk.gif')
    await ctx.send(embed=embed)

@client.command()
async def daniel(ctx):
    embed = discord.Embed(
        title = 'Daniel com seus amigos',
        description = 'foi mal sub',
        colour = discord.Colour.blue()
    )
    embed.set_image(url='https://media.tenor.com/images/8f50bd23019d8d303e5a12911c259b61/tenor.gif')
    await ctx.send(embed=embed)

@client.command()
async def leo(ctx):
    await ctx.send('Ta tudo bem leo, o importante é ser feliz e não perfeito')

@client.command()
async def willy(ctx):
    await ctx.send('Se não fosse pelo leo seria a maior revelação otaka do discord\nps: perdão pela bagunça no among us')


#time italy
@client.command()
async def italy(ctx): #formerly printCurrentTime
    fmt = "%H:%M:%S"
    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    # Convert to Europe/Berlin time zone
    now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
    await ctx.send(f'{now_berlin.strftime(fmt)} (Italy)')

client.run('NzU0MDQyNjgwNDEzMTI2ODA4.X1u--A.tyhgPrK7duNmyELhJZjImXXARJg')
