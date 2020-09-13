import discord
from discord.ext import commands

class names(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    @commands.command()
    async def hiter(self, ctx):
        await ctx.send('Lindo, maravilhoso e cheiroso!')
    @commands.command()
    async def bruno(self, ctx):
        await ctx.send('mto zika')

    @commands.command()
    async def giovanna(self, ctx):
        await ctx.send('Rainha da programação, merece o mundo! princesa manda salve rsrs')

    @commands.command()
    async def baruel(self, ctx):
        await ctx.send('por favor baruel, para de mandar gif merda')

    @commands.command()
    async def cat(self, ctx):
        await ctx.send('Deboche, ironia e ódio gratuito')

    @commands.command()
    async def felipe(self, ctx):
        await ctx.send('Dançando kpop olhando pra baixo pra ver o leo')



    @commands.command()
    async def pv(self, ctx):
        embed = discord.Embed(
            title = 'pvtdo <3 khitara',
            description = 'foi mal daniel',
            colour = discord.Colour.blue()
        )
        embed.set_image(url='https://i.makeagif.com/media/10-09-2015/-vktJk.gif')
        await ctx.send(embed=embed)

    @commands.command()
    async def daniel(self, ctx):
        embed = discord.Embed(
            title = 'Daniel com seus amigos',
            description = 'foi mal sub',
            colour = discord.Colour.blue()
        )
        embed.set_image(url='https://media.tenor.com/images/8f50bd23019d8d303e5a12911c259b61/tenor.gif')
        await ctx.send(embed=embed)

    @commands.command()
    async def leo(self, ctx):
        await ctx.send('Ta tudo bem leo, o importante é ser feliz e não perfeito')

    @commands.command() 
    async def willy(self, ctx):
        await ctx.send('Se não fosse pelo leo seria a maior revelação otaka do discord\nps: perdão pela bagunça no among us')



def setup(client):
    client.add_cog(names(client))
