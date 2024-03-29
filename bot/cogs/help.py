import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    #custom help command
    @commands.command(aliases=['HELP', 'Help'])
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Commands list',
            colour = discord.Colour.blue()
            )
        embed.set_footer(text='*The moon is friend for the lonesome to talk to.*')
        #embed.set_thumbnail(url='https://i.ibb.co/S7mKyfQ/123.jpg')
        embed.set_image(url='https://i.ibb.co/S7mKyfQ/123.jpg')
        embed.add_field(name='Admin/Fun', value='clear (A)\n8ball\nnames\nreverse\navatar\nsaporra\nfact')
        embed.add_field(name='Basic', value='help\nping\nitaly\nanime')
        embed.add_field(name='Text', value='say\nembed')
        await ctx.send(embed=embed)

    #names commands
    @commands.command(aliases=['NAMES', 'Names'])
    async def names(self, ctx):
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.add_field(name='Names', value='baruel\nbruno\ncat\nfelipe\ngiovanna\njack\nleo\npv\nwilly\nkhtr\nudy\nthx', inline=False)
        await ctx.send(embed=embed)

    #anime commands
    @commands.command(aliases=['Anime', 'ANIME'])
    async def anime(self, ctx):
        embed = discord.Embed(title = 'Anime commands', description = '**interaction use:** *!command <@user>*', colour = discord.Colour.blue())
        embed.set_thumbnail(url='https://i.ibb.co/S7mKyfQ/123.jpg')
        embed.add_field(name='Reaction', value='blush\ncry\ndance\npout\nsmug')
        embed.add_field(name='Interaction', value='senpai\nhug\nkiss\nslap\npat\nkill\nlick\ncuddle\ninsult')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))
