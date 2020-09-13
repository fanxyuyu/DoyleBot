import discord
import random
from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #say as the bot
    @commands.command() #use to set a list that can run a command
    async def say(self, ctx, *, textt): #you can't start a command with number
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'{textt}')
        return

    #Embed text
    @commands.command() #use to set a list that can run a command
    async def embed(self, ctx, *, textts): #you can't start a command with number
        await ctx.channel.purge(limit = 1)
        embed = discord.Embed(description = f"{textts}", colour = discord.Colour.blue())
        await ctx.send(embed=embed)
        return

    #reverses the text
    @commands.command()
    async def reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f":arrows_counterclockwise: {t_rev}")

def setup(client):
    client.add_cog(fun(client))
