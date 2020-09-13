import discord
import random
from discord.ext import commands

class _8ball(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', '8']) #use to set a list that can run a command
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def ball(self, ctx, *, question): #you can't start a command with number
        responses = ['Com certeza!',
                    'Não sei, pergunta pro leo.',
                    'Que tipo de pergunta é essa?',
                    'Sim!',
                    'Não!',
                    'kkkkk ele não sabe xD',
                    'que soninho... me pergunte novamente mais tarde.',
                    'que pergunta merda, parabéns.',
                    'Não tenho certeza.',
                    'CLARO!! COM CERTEZA ABSOLUTA!',
                    'Dúvido muito.',
                    'Quem sabe :)',
                    'Essa é uma boa pergunta, eu não sei te responder.',
                    'Pra você a resposta é não.',
                    'Pra você a resposta é sim.',
                    'Esquece a pergunta te achei gatinha rsrs.',
                    'Não vou falar ^^',
                    'Pode confiar nisso.',
                    'Segundo meu horóscopo... não posso te responder.',
                    'CLARO QUE SIM!',
                    'CLARO QUE NAO!',
                    'Se fosse o baruel perguntando eu diria que sim.',
                    'sim... não... quem sabe...',
                    'sim e eu amo muito o leleo.',
                    'Obrigado por perguntar, SIM!',
                    'Obrigado por perguntar, NAO!',
                    'desculpa por ser um bot :(',
                    'pergunta pro cat, ele sabe a resposta certa',
                    'O importante é ser feliz e não perfeito']
        await ctx.send(f'Pergunta: {question}\nResposta: {random.choice(responses)}')

    @ball.error
    async def ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Correct use: !8ball <question>")

def setup(client):
    client.add_cog(_8ball(client))
