import discord
from discord.ext import commands

class names(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    @commands.command()
    async def jack(self, ctx):
        await ctx.send('Eu nunca vi alguém com tanta autoestima, parabéns pelo double ego! #OMaisHumildeDoDiscord')
    @commands.command()
    async def bruno(self, ctx):
        await ctx.send('Meu criador... ele que me fez assim :(')
    @commands.command()
    async def giovannasasa(self, ctx):
        await ctx.send('Sei lá giovanna... acho que é isso... Nunca mais vou me recuperar desse trauma. Rainha da programação nas horas vagas')
    @commands.command()
    async def baruel(self, ctx):
        await ctx.send('por favor baruel, para de mandar gif merda e de programar no celular 3 da manhã pelo celular na casa da namorada')
    @commands.command()
    async def cat(self, ctx):
        await ctx.send('Deboche, ironia e ódio gratuito... e pezinho fofinho :3')
    @commands.command()
    async def felipe(self, ctx):
        await ctx.send('Dançando kpop olhando pra baixo pra ver o leo')
    @commands.command()
    async def khtr(self, ctx):
        await ctx.send('Parabéns por aguentar o pv, nunca vamos esquecer do seu sacrificio')
    @commands.command()
    async def thx(self, ctx):
        await ctx.send('kkkkkkkkkk criptomoeda')
    @commands.command()
    async def udy(self, ctx):
        await ctx.send('Nao importa a cor da sua pele segue lá: https://www.tiktok.com/@udaocacarato')


    @commands.command()
    async def pv(self, ctx):
        embed = discord.Embed(
            title = 'paulin bacana',
            #description = 'foi mal daniel',
            colour = discord.Colour.blue()
        )
        embed.set_image(url='https://media1.tenor.com/images/ef12d730c3d3044f384fea8cb6d8a3a5/tenor.gif')
        await ctx.send(embed=embed)
        
    @commands.command()
    async def giovanna(self, ctx):
        embed = discord.Embed(
            title = 'JIGSAY',
            description = '#bike',
            colour = discord.Colour.blue()
        )
        embed.set_image(url='https://media1.tenor.com/images/05f7b997db2f06947a97cd7671370cc5/tenor.gif?itemid=15725648')
        await ctx.send(embed=embed)

    #@commands.command()
    #async def daniel(self, ctx):
        #embed = discord.Embed(
            #title = 'DanielMatiasz',
            #description = 'o terror do meier',
            #colour = discord.Colour.blue()
        #)
        #embed.set_image(url='https://i.ibb.co/GxjNr4H/aaaaa.png')
        #await ctx.send(embed=embed)

    @commands.command()
    async def saporra(self, ctx):
        embed = discord.Embed(
            title = 'saporra',
            description = 'kawaii moe ><',
            colour = discord.Colour.blue()
        )
        embed.set_image(url='https://i.ibb.co/kD52NHP/saporra.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def leo(self, ctx):
        await ctx.send('Ta tudo bem leo, o importante é ser feliz e não perfeito')

    @commands.command()
    async def willy(self, ctx):
        await ctx.send('Se não fosse pelo leo seria a maior revelação otaku do discord\nps: perdão pela bagunça no among us')



def setup(client):
    client.add_cog(names(client))
