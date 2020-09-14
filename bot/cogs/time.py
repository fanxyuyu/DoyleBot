import discord
import os
from datetime import datetime #for datetime
from pytz import timezone #for timezone
from discord.ext import commands, tasks

class time(commands.Cog):

    def __init__(self, client):
        self.client = client

    #time italy
    @commands.command(aliases=['Italy', 'ITALY'])
    async def italy(self, ctx): #formerly printCurrentTime
        fmt = "%H:%M:%S"
        # Current time in UTC
        now_utc = datetime.now(timezone('UTC'))
        # Convert to Europe/Berlin time zone
        now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
        await ctx.send(f'{now_berlin.strftime(fmt)} (Italy)')


def setup(client):
    client.add_cog(time(client))
