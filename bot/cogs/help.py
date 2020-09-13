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
        embed.set_footer(text='*The moon is friend for the lonesome to talk to.*')
        #embed.set_thumbnail(url='https://i.ibb.co/S7mKyfQ/123.jpg')
        embed.set_image(url='https://i.ibb.co/S7mKyfQ/123.jpg')
        embed.add_field(name='Admin/Fun', value='clear (A)\n8ball\nnames\nreverse')
        embed.add_field(name='Anime', value='anime\nsenpai\nhug\nkiss\nslap')
        embed.add_field(name='Basic', value='help\nping\nitaly')
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
        embed.add_field(name='Commands', value='**senpai:** *<@user>* notice me!\n**hug:** *<@user>* hugs someone\n**kiss:** *<@user>* kisses someone\n**slap:** *<@user>* slaps someone', inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))
