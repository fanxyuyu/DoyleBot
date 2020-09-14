import discord
import os #to use cogs
import time #to use time.sleep
import asyncio #to delete message
from discord.ext import commands, tasks
from itertools import cycle #import to create a cycle on bot status

startup_extensions = ['cogs._8ball','cogs.anime','cogs.fun','cogs.help','cogs.names','cogs.time'] #starts defined cogs

client = commands.Bot(command_prefix = '!')
status = cycle(['use !help | v0.3'])
client.remove_command('help') #removes default help command

#Load message
@client.event
async def on_ready():
    change_status.start()
    print(f'bot: {client.user} is now online!')

#change bot game status
@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#ping tester
@client.command(aliases=['PING', 'Ping'])
async def ping(ctx): #parameter
    await ctx.send(f'`Ping: {round (client.latency * 1000)} ms`')

#command error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown): #if command is on cooldown
        times = round(error.retry_after, 1)
        message = await ctx.send(f"{ctx.author.mention} you can use this command in `{times}` Seconds(s)")
        time.sleep(2)
        await message.delete()
        return

#clear <qnt> command -> defined to role named a
@client.command(aliases=['CLEAR', 'Clear'])
@commands.has_role('a')
#@commands.cooldown(1, 3.0, commands.BucketType.user)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount + 1)
    message = await ctx.send(f'Total messages deleted: {amount}')
    time.sleep(3)
    await message.delete()
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Correct use: !clear <qntd>')
        
#load cogs
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.run('NzU0MDQyNjgwNDEzMTI2ODA4.X1u--A.tyhgPrK7duNmyELhJZjImXXARJg')
