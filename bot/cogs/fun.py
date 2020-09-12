import discord
import random
from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f":arrows_counterclockwise: {t_rev}")

def setup(client):
    client.add_cog(fun(client))
