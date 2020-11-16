import discord
import random
from discord.ext import commands

class anime2(commands.Cog):

    def __init__(self, client):
        self.client = client


    #REACTIONS: Blush!
    @commands.command(aliases=['BLUSH', 'Blush'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def blush(self, ctx, user: discord.Member = None):
        await ctx.message.delete()

        blushgifs = ['https://cdn.weeb.sh/images/rJa-zUmv-.gif',
                    'https://cdn.weeb.sh/images/HklJGIXPW.gif',
                    'https://cdn.weeb.sh/images/BJH4f8mP-.gif',
                    'https://cdn.weeb.sh/images/r1U7G87vZ.gif',
                    'https://cdn.weeb.sh/images/Sy1-ML7vW.gif',
                    'https://cdn.weeb.sh/images/S1X7GIXw-.gif',
                    'https://i.imgur.com/yBdeWN7.gif',
                    'https://i.imgur.com/PsH7bRr.gif',
                    'https://i.imgur.com/myWNMeq.gif',
                    'https://i.imgur.com/hgvdfSI.gif']

        if not user:
            embed = discord.Embed(description = f"{ctx.author.mention}**'s blushing**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(blushgifs)}')
            return await ctx.send(embed=embed)
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"{ctx.author.mention}**'s blushing**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(blushgifs)}')
            return await ctx.send(embed=embed)
        if user.bot:
            embed = discord.Embed(description = f"{ctx.author.mention}**'s blushing**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(blushgifs)}')
            return await ctx.send(embed=embed)
        embed = discord.Embed(description = f"{ctx.author.mention}**'s blushes at {user.mention}**", colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(blushgifs)}')
        await ctx.send(embed=embed)



    #REACTIONS: Cry!
    @commands.command(aliases=['CRY', 'Cry'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def cry(self, ctx, user: discord.Member = None):
        await ctx.message.delete()

        crygifs = ['https://cdn.weeb.sh/images/ByF7REgdf.gif',
                    'https://cdn.weeb.sh/images/ByuM1x5Jz.gif',
                    'https://cdn.weeb.sh/images/Sy1EUa-Zz.gif',
                    'https://cdn.weeb.sh/images/HyiGQUmPb.gif',
                    'https://cdn.weeb.sh/images/ByPGQIQwb.gif',
                    'https://cdn.weeb.sh/images/HyO7mIXvW.gif',
                    'https://cdn.weeb.sh/images/rJUbkgqyf.gif',
                    'https://cdn.weeb.sh/images/BJJkFTN0b.gif',
                    'https://i.imgur.com/wHW3NNW.gif',
                    'https://i.imgur.com/VSGPi6X.gif']

        if not user:
            embed = discord.Embed(description = f"{ctx.author.mention}**'s crying**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(crygifs)}')
            return await ctx.send(embed=embed)
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"{ctx.author.mention}**'s crying**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(crygifs)}')
            return await ctx.send(embed=embed)
        if user.bot:
            embed = discord.Embed(description = f"{ctx.author.mention}**'s crying**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(crygifs)}')
            return await ctx.send(embed=embed)
        embed = discord.Embed(description = f"{user.mention}** made **{ctx.author.mention} **cry**", colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(crygifs)}')
        await ctx.send(embed=embed)



    #REACTIONS: DANCE!
    @commands.command(aliases=['DANCE', 'Dance'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def dance(self, ctx, user: discord.Member = None):
        await ctx.message.delete()

        dancegifs = ['https://media1.giphy.com/media/EW3CTnkH6uy3K/giphy.gif',
                    'https://media3.giphy.com/media/b7l5cvG94cqo8/giphy.gif',
                    'https://cdn.weeb.sh/images/SJWuu8mwW.gif',
                    'https://cdn.weeb.sh/images/H1ha_L7DW.gif',
                    'https://i.imgur.com/Fs51fKV.gif',
                    'https://cdn.weeb.sh/images/Hk0duIXPb.gif',
                    'https://media4.giphy.com/media/w5MSivCJcmHEQ/giphy.gif',
                    'https://media0.giphy.com/media/N4AIdLd0D2A9y/giphy.gif',
                    'https://media1.tenor.com/images/c5bf0c167048f0baf563e42611a1eaa2/tenor.gif?itemid=14872583']

        if not user:
            embed = discord.Embed(description = f"{ctx.author.mention}** has started to dance**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(dancegifs)}')
            return await ctx.send(embed=embed)
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"{ctx.author.mention}** has started to dance**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(dancegifs)}')
            return await ctx.send(embed=embed)
        if user.bot:
            embed = discord.Embed(description = f"{ctx.author.mention}** has started to dance**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(dancegifs)}')
            return await ctx.send(embed=embed)
        embed = discord.Embed(description = f"{ctx.author.mention}** started to dance with** {user.mention}", colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(dancegifs)}')
        await ctx.send(embed=embed)



    #REACTIONS: POUT!
    @commands.command(aliases=['POUT', 'Pout'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def pout(self, ctx, user: discord.Member = None):
        await ctx.message.delete()

        poutgifs = ['https://i.imgur.com/fgHYCPu.gif',
                    'https://i.imgur.com/BvJMkcL.gif',
                    'https://i.imgur.com/4QIb6DK.gif',
                    'https://i.imgur.com/7cBmyR9.gif',
                    'https://i.imgur.com/Ti9mlBj.gif',
                    'https://pa1.narvii.com/6680/aadd8ceb77b1deded865ff3755b83230a929a96a_hq.gif',
                    'https://media.tenor.com/images/0f5d12aa3dfa6d8fd9e8a41bc51ec421/tenor.gif']

        if not user:
            embed = discord.Embed(description = f"{ctx.author.mention}** started to pout**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(poutgifs)}')
            return await ctx.send(embed=embed)
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"{ctx.author.mention}** started to pout**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(poutgifs)}')
            return await ctx.send(embed=embed)
        if user.bot:
            embed = discord.Embed(description = f"{ctx.author.mention}** started to pout**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(poutgifs)}')
            return await ctx.send(embed=embed)
        embed = discord.Embed(description = f"{ctx.author.mention}** pouts looking at** {user.mention}", colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(poutgifs)}')
        await ctx.send(embed=embed)



    #REACTIONS: Smug!
    @commands.command(aliases=['SMUG', 'Smug'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def smug(self, ctx, user: discord.Member = None):
        await ctx.message.delete()

        smuggifs = ['https://i.imgur.com/uYhZvlV.gif',
                    'https://media.tenor.com/images/a6db0f3c43c515305a01157ef3606536/tenor.gif',
                    'https://media1.tenor.com/images/ea2e6ec351e238d8e8bd624b3738a9b3/tenor.gif?itemid=14210719',
                    'https://i.kym-cdn.com/photos/images/newsfeed/001/161/167/eda.gif',
                    'https://64.media.tumblr.com/254c921a2e7138bb20d3c28a0ec27102/tumblr_omo6hwUkUJ1shmkc9o1_r2_540.gif',
                    'https://memestatic1.fjcdn.com/thumbnails/comments/+_4e1dbf75401e7c414c06328ec8a5b0e6.gif',
                    'https://cdn.weeb.sh/images/rJUbkgqyf.gif',
                    'https://cdn.weeb.sh/images/BJJkFTN0b.gif',
                    'https://64.media.tumblr.com/8e8164ba096f8bbcfd10233ad4d4a632/99c0165c2e40671f-92/s400x600/96deb4b2ff460e2990ca231f6db968ecfa3643db.gifv']

        if not user:
            embed = discord.Embed(description = f"{ctx.author.mention}** smugs**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(smuggifs)}')
            return await ctx.send(embed=embed)
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"{ctx.author.mention}** smugs**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(smuggifs)}')
            return await ctx.send(embed=embed)
        if user.bot:
            embed = discord.Embed(description = f"{ctx.author.mention}** smugs**", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url=f'{random.choice(smuggifs)}')
            return await ctx.send(embed=embed)
        embed = discord.Embed(description = f"{ctx.author.mention}** smugs at **{user.mention}", colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(smuggifs)}')
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(anime2(client))
