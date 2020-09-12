import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

#custom help command
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Commands list',
            colour = discord.Colour.blue()
            )
        embed.set_thumbnail(url='https://i.ibb.co/S7mKyfQ/123.jpg')
        embed.add_field(name='Admin', value='clear')
        embed.add_field(name='Basic', value='help\nping\nitaly')
        embed.add_field(name='Fun', value='8ball\nnames\nanime\nreverse', inline=False)
        await ctx.send(embed=embed)

#names commands
    @commands.command()
    async def names(self, ctx):
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.add_field(name='Names', value='baruel\nbruno\ncat\ndaniel\nfelipe\ngiovanna\nhiter\nleo\npv\nwilly', inline=False)
        await ctx.send(embed=embed)

#anime commands
    @commands.command()
    async def anime(self, ctx):
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.add_field(name='Commands', value='senpai\nhug', inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))
