import discord
import os #to use cogs
import time #to use time.sleep
import asyncio #to delete message
import randfacts #for random facts
from discord.ext import commands, tasks
from itertools import cycle #import to create a cycle on bot status

startup_extensions = ['cogs._8ball','cogs.anime','cogs.anime2','cogs.fun','cogs.help','cogs.names','cogs.time'] #starts defined cogs

client = commands.Bot(command_prefix = '!')
status = cycle(['ITX'])
client.remove_command('help') #removes default help command

#Load message
@client.event
async def on_ready():
    RecompensaRealm.start()
    change_status.start()
    print(f'bot: {client.user} is now online!')

#change bot game status
@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#log for deleted messages
@client.event
async def on_message_delete(message):
    msg = str(message.author)+ 'deleted message in '+str(message.channel)+': '+str(message.content)
    channels = client.get_channel(756270352346382367)
    if(message.author.bot):
        return
    else:
        embed = discord.Embed(color = 12370112)
        embed.set_author(name = f"{message.author}", icon_url = message.author.avatar_url)
        embed.add_field(name=f'Canal:', value=F'{message.channel}', inline = False)
        embed.add_field(name=f'Mensagem deletada:', value=F'{message.content}')
        return await channels.send(embed = embed)

#log for edited messages:
@client.event
async def on_message_edit(message_before, message_after):
    #msg = str(message.author)+ 'deleted message in '+str(message.channel)+': '+str(message.content)' +'
    channels = client.get_channel(756270352346382367)
    if(message_before.author.bot):
        return
    else:
        embed = discord.Embed(color = 12370112)
        embed.set_author(name = f"{message_before.author}", icon_url = message_before.author.avatar_url)
        embed.add_field(name=f'Canal:', value=F'{message_before.channel}', inline = False)
        embed.add_field(name=f'Mensagem antes:', value=F'{message_before.content}')
        embed.add_field(name=f'Mensagem depois:', value=F'{message_after.content}', inline = False)
        return await channels.send(embed = embed)

#ping tester
@client.command(aliases=['PING', 'Ping'])
async def ping(ctx): #parameter
    await ctx.send(f'`Ping: {round (client.latency * 1000)} ms`')

#command error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown): #if command is on cooldown
        times = round(error.retry_after, 2)
        times = times % (24 * 3600)
        hours = int(times // 3600)
        times %= 3600
        minutes = int(times // 60)
        times %= 60
        seconds = int(times)
        if (hours>=1):
            message = await ctx.send(f"{ctx.author.mention} -> you can use this command in `{hours} hour(s), {minutes} minute(s) and {seconds} seconds(s)`")
            time.sleep(3)
            return await message.delete()
        if ((hours < 1) & (minutes >= 1)):
            message = await ctx.send(f"{ctx.author.mention} -> you can use this command in `{minutes} minute(s) and {seconds} seconds(s)`")
            time.sleep(3)
            return await message.delete()
        elif (minutes < 1):
            message = await ctx.send(f"{ctx.author.mention} -> you can use this command in `{seconds} seconds(s)`")
            time.sleep(3)
            return await message.delete()

#clear <qnt> command -> defined to role named a
@client.command(aliases=['CLEAR', 'Clear'])
@commands.has_role('a')
#@commands.cooldown(1, 90, commands.BucketType.user)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount + 1)
    message = await ctx.send(f'Total messages deleted: {amount}')
    time.sleep(3)
    await message.delete()
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Correct use: !clear <qntd>')
        
#random fact   
@client.command()
@commands.cooldown(1, 10.0, commands.BucketType.user)
async def fact(ctx):
    x = randfacts.getFact()
    return await ctx.send(x)


#mensagem de recompensa do realm
@tasks.loop(hours=24)
async def RecompensaRealm():
    channels = client.get_channel(755530735376531557)
    try:
        d = 'https://i.imgur.com/SyW1gzN.png'
        embed = discord.Embed(title = 'recompensa do realm', description = f"não se esqueçam de pegar a recompensa de hoje!", color = 12370112)
        embed.set_thumbnail(url = d)
        await channels.send("@everyone")
        await channels.send(embed = embed)
        print("Mensagem de recompensa enviada")
    except Exception as e:
        print(f"Mensagem de recompensa error: {e}")

        
#load cogs
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.run('NzU0MDQyNjgwNDEzMTI2ODA4.X1u--A.tyhgPrK7duNmyELhJZjImXXARJg')
