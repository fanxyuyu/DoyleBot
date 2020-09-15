import discord
import random
from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #say as the bot
    @commands.command(aliases=['Say', 'SAY']) #use to set a list that can run a command
    async def say(self, ctx, *, textt): #you can't start a command with number
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'{textt}')
        return

    #Embed text
    @commands.command(aliases=['EMBED', 'Embed']) #use to set a list that can run a command
    async def embed(self, ctx, *, textts): #you can't start a command with number
        await ctx.channel.purge(limit = 1)
        embed = discord.Embed(description = f"{textts}", colour = discord.Colour.blue())
        await ctx.send(embed=embed)
        return

    #reverses the text
    @commands.command(aliases=['Reverse', 'REVERSE'])
    async def reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f":arrows_counterclockwise: {t_rev}")
        
    #See someones avatar
    @commands.command()
    @commands.cooldown(1, 4.0, commands.BucketType.user)
    async def avatar(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            embed = discord.Embed(colour = random.randint(0, 0xFFFFFF))
            embed.set_author(name = f"{ctx.author.name}'s profile picture", icon_url = ctx.author.avatar_url)
            embed.set_image(url = ctx.author.avatar_url)
            return await ctx.send(embed = embed)
        else:
            embed = discord.Embed(colour = random.randint(0, 0xFFFFFF))
            embed.set_author(name = f"{user.name}'s profile picture", icon_url = user.avatar_url)
            embed.set_image(url = user.avatar_url)
            return await ctx.send(embed = embed)
        

def setup(client):
    client.add_cog(fun(client))
