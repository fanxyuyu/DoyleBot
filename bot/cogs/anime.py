import discord
import random
from discord.ext import commands

class anime(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['noticemesenpai', 'senpai'])
    async def noticeme(self, ctx, user: discord.Member = None):
        if not user:
            return await ctx.send(f"Correct use: b.senpai <@user>")
        if user.id == ctx.author.id:
            return await ctx.send(f"Are you that needy? you can't notice yourself!")
        if user.bot:
            return await ctx.send(f"Unfortunately **{user.name}** is a bot so I don't think it can notice you :(")
        embed = discord.Embed(description = f'Hey **{user.name}**, **{ctx.author.name}** wants you to notice him!', colour = discord.Colour.blue())
        embed.set_image(url='https://i.alexflipnote.dev/500ce4.gif')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(anime(client))
