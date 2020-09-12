import discord
import os #to use cogs
from discord.ext import commands, tasks
from itertools import cycle #import to create a cycle on bot status

client = commands.Bot(command_prefix = 'b.')
status = cycle(['type b.help', 'bot by: Lust#4444', 'type b.help', 'bot by: Lust#4444', 'I see you'])
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
@client.command()
async def ping(ctx): #parameter
    await ctx.send(f'`Ping: {round (client.latency * 1000)} ms`')

#command error (if command does not exist)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command.')

#clear <qnt> command -> defined to role named a
@client.command()
@commands.has_role('a')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount + 1)
    await ctx.send(f'Total messages deleted: {amount}')
    time.sleep(3)
    await ctx.channel.purge(limit = 1)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Correct use: b.clear <qntd>')

#load cogs
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') #removes .py from files

client.run('NzU0MTIwNzg2MDU0MzQ4ODAx.X1wHtg.mlPtL0-5FkUaFFUUo4kNtrjzk94')
