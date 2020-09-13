import discord
import random
from discord.ext import commands

class anime(commands.Cog):

    def __init__(self, client):
        self.client = client


    #simple notice me senpai command with a gif
    @commands.command(aliases=['noticemesenpai', 'senpai'])
    async def noticeme(self, ctx, user: discord.Member = None):
        if not user: #exclude with there's no argument
            return await ctx.send(f"Correct use: b.senpai <@user>")
        if user.id == ctx.author.id: #check if the user taged himself
            return await ctx.send(f"Are you that needy? you can't notice yourself!")
        if user.bot: #check if it taged a bot
            return await ctx.send(f"Unfortunately **{user.name}** is a bot so I don't think it can notice you :(")
        embed = discord.Embed(description = f'Hey **{user.name}**, **{ctx.author.name}** wants you to notice him!', colour = discord.Colour.blue())
        embed.set_image(url='https://i.alexflipnote.dev/500ce4.gif')
        await ctx.send(embed=embed)


    #hug another user command
    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):
        if not user:
            return await ctx.send(f"Correct use: b.hug <@user>")
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f'**{ctx.author.name}** is feeling really lonely and hugs a pillow', colour = discord.Colour.blue())
            embed.set_image(url='https://media1.tenor.com/images/1a0ac2f256d11e323ccad554de71f0cf/tenor.gif')
            await ctx.send(embed=embed)
            return #stops the command if self tag
        if user.bot:
            return await ctx.send(f"Unfortunately **{user.name}** is a bot but thanks for the hug :heart_exclamation:")
        #hugs gifs list
        gifshug = ['https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif',
                'https://media1.tenor.com/images/85dcef131af84b515106955e142df54e/tenor.gif',
                'https://media1.tenor.com/images/f5df55943b64922b6b16aa63d43243a6/tenor.gif',
                'https://media1.tenor.com/images/bb841fad2c0e549c38d8ae15f4ef1209/tenor.gif',
                'https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/tenor.gif',
                'https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif',
                'https://media1.tenor.com/images/7d6a56988dc7e6152ca578b7a1f24be9/tenor.gif',
                'https://media1.tenor.com/images/79aa56112b2d0eca4f50e9df188e18ad/tenor.gif',
                'https://media1.tenor.com/images/94c44a9898927f22dff399c2c248f433/tenor.gif',
                'https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif']
        #hugs phrases
        hugs = [f'**{ctx.author.name}** hugs tightly **{user.name}**',
                f'**{ctx.author.name}** hugs **{user.name}** with love',
                f'**{ctx.author.name}** forces **{user.name}** to a hug',
                f'**{ctx.author.name}** hugs **{user.name}** to make him feel better',
                f'**{ctx.author.name}** surprises **{user.name}** with a hug',
                f'**{ctx.author.name}** hugs **{user.name}**']

        embed = discord.Embed(description = f'{random.choice(hugs)}', colour = discord.Colour.blue())
        embed.set_image(url=f'{random.choice(gifshug)}')
        await ctx.send(embed=embed)


    #kiss another user command
    @commands.command()
    async def kiss(self, ctx, user: discord.Member = None):
        if not user:
            return await ctx.send(f"Correct use: b.kiss <@user>")
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"Hey **{ctx.author.name}** you can't kiss yourself so take mine ><", colour = discord.Colour.blue())
            embed.set_image(url='https://i.pinimg.com/originals/6a/46/8f/6a468f80cb1384d681440115d6e6d1b9.gif')
            await ctx.send(embed=embed)
            return #stops the command if self tag
        if user.bot:
            return await ctx.send(f"thanks... **{user.name}** :flushed:")
        #kiss gifs list
        gifskiss = ['https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif',
                'https://media1.tenor.com/images/621ceac89636fc46ecaf81824f9fee0e/tenor.gif',
                'https://media1.tenor.com/images/40711a5b00fcf9918ddef1aa483d993f/tenor.gif',
                'https://media1.tenor.com/images/db79d17d7a5e08bf64e55a63eea5976f/tenor.gif',
                'https://media1.tenor.com/images/a0b68f4704f811bfcc517574425e96a5/tenor.gif',
                'https://media1.tenor.com/images/0d70e1c91378712021717d2f6424fd07/tenor.gif',
                'https://media1.tenor.com/images/37ceeaa82fb503fb10bbd539ad4e3fd8/tenor.gif',
                'https://media1.tenor.com/images/3dc3bb6e35aa0d090527babe698bfe55/tenor.gif',
                'https://media1.tenor.com/images/be905a75eb3036494fc32df12b7c1b7a/tenor.gif',
                'https://media1.tenor.com/images/49811017ffb751e3c4228f68d55778e4/tenor.gif']
        #kiss phrases
        kiss = [f'**{ctx.author.name}** kisses **{user.name}**',
                f'**{ctx.author.name}** kisses **{user.name}** all night long',
                f'**{ctx.author.name}** forces a kiss on **{user.name}**',
                f'**{ctx.author.name}** kisses **{user.name}** who loves it',
                f'**{ctx.author.name}** surprises **{user.name}** with a kiss',
                f'**{ctx.author.name}** kisses **{user.name}** and *5* others later',
                f'**{ctx.author.name}** kisses **{user.name}** and regrets it later',
                f'**{ctx.author.name}** kisses **{user.name}** but **{user.name}** regrets it later',
                f'**{ctx.author.name}** kisses **{user.name}** and **{user.name}** fall in love']

        embed = discord.Embed(description = f'{random.choice(kiss)}', colour = discord.Colour.blue())
        embed.set_image(url=f'{random.choice(gifskiss)}')
        await ctx.send(embed=embed)


    #slaps another user command
    @commands.command()
    async def slap(self, ctx, user: discord.Member = None):
        if not user:
            return await ctx.send(f"Correct use: b.slap <@user>")
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"I'm... I'm sorry **{ctx.author.name}** :( you made me do it", colour = discord.Colour.blue())
            embed.set_image(url='https://i.pinimg.com/originals/1c/8f/0f/1c8f0f43c75c11bf504b25340ddd912d.gif')
            await ctx.send(embed=embed)
            return #stops the command if self tag
        if user.bot:
            embed = discord.Embed(description = f"Why? Why do you want to hurt me **{ctx.author.name}**", colour = discord.Colour.blue())
            embed.set_image(url='https://media.tenor.com/images/7e623e17dd8c776aee5e0c3e0e9534c9/tenor.gif')
            await ctx.send(embed=embed)
            return
        #slaps gifs list
        gifslap = ['https://media0.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif',
                'https://i.pinimg.com/originals/b8/f3/02/b8f302e2fa5f45fa4d472a23d828568b.gif',
                'https://media1.tenor.com/images/af36628688f5f50f297c5e4bce61a35c/tenor.gif',
                'https://pa1.narvii.com/6807/b3b719851bc98fa5387ecf7447ed9ef4b77f4f5d_hq.gif',
                'https://i.kym-cdn.com/photos/images/newsfeed/001/126/001/997.gif',
                'https://i.imgur.com/3rHE4Ee.gif',
                'https://i.pinimg.com/originals/46/b0/a2/46b0a213e3ea1a9c6fcc060af6843a0e.gif',
                'https://i.kym-cdn.com/photos/images/newsfeed/001/390/712/289.gif',
                'https://i.kym-cdn.com/photos/images/newsfeed/000/846/661/240.gif']
        #slaps phrases
        slap = [f'**{ctx.author.name}** slaps **{user.name}**',
                f'**{ctx.author.name}** slaps **{user.name}** with all her mighty',
                f'**{ctx.author.name}** surprises **{user.name}** by slapping him',
                f'**{ctx.author.name}** slaps **{user.name}** but **{user.name}** likes it',
                f'**{ctx.author.name}** slapped **{user.name}** so hard that **{user.name}** ends up liking it',
                f'**{ctx.author.name}** slaps **{user.name}** for no reason',
                f'**{ctx.author.name}** slaps **{user.name}** because **{user.name}** was mean',
                f'**{ctx.author.name}** slaps **{user.name}** but **{user.name}** take revenge later',
                f'**{ctx.author.name}** slaps **{user.name}** but regrets it later']

        embed = discord.Embed(description = f'{random.choice(slap)}', colour = discord.Colour.blue())
        embed.set_image(url=f'{random.choice(gifslap)}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(anime(client))
