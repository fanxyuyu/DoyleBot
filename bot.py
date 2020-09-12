import discord
import random
import time
import os
from discord.ext import commands, tasks #import the commands from discord extension
from itertools import cycle #import para criar um cycle usado nos stats do bot


client = commands.Bot(command_prefix = 'b.') #defines the command to client (if used BOT instead of client the declaration should be named bot)
status = cycle(['bot prefix: b.', 'bot by: Lust#4444'])


#back to normal
@client.event
async def on_ready():
    change_status.start()
    print('BRUBS IS ONLINE :)')

#list of commands: ping, 8ball, clear

#comando para deixar o status do jogo
@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#comando para testar o ping
@client.command()
async def ping(ctx): #parameter
    await ctx.send(f'`Ping: {round (client.latency * 1000)} ms`')

#comando para erro
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando inexistente')


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
                'desculpa por ser bot :(']
    await ctx.send(f'Pergunta: {question}\nResposta: {random.choice(responses)}')


#comando clear
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

#comandos de chat
@client.command()
async def hiter(ctx): #parameter
    await ctx.send('Lindo, maravilhoso e cheiroso!')

@client.command()
async def lust(ctx): #parameter
    await ctx.send('mto zika')

@client.command()
async def giovanna(ctx): #parameter
    await ctx.send('Rainha da programação, merece o mundo! princesa manda salve rsrs')

@client.command()
async def baruel(ctx): #parameter
    await ctx.send('por favor baruel, para de mandar gif merda')

@client.command()
async def cat(ctx): #parameter
    await ctx.send('Deboche, ironia e ódio gratuito')

@client.command()
async def felipe(ctx): #parameter
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
async def leo(ctx): #parameter
    await ctx.send('Ta tudo bem leo, o importante é ser feliz e não perfeito')

@client.command()
async def willy(ctx): #parameter
    await ctx.send('Se não fosse pelo leo seria a maior revelação otaka do discord\nps: perdão pela bagunça no among us')

#cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzU0MDQyNjgwNDEzMTI2ODA4.X1u--A.tyhgPrK7duNmyELhJZjImXXARJg')
