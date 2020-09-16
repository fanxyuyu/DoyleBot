import discord
import random
from discord.ext import commands

class anime(commands.Cog):

    def __init__(self, client):
        self.client = client


    #simple notice me senpai command with a gif
    @commands.command(aliases=['noticemesenpai', 'senpai', 'SENPAI', 'NOTICEME', 'Senpai', 'Notice'])
    @commands.cooldown(1, 4.0, commands.BucketType.user)
    async def noticeme(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user: #exclude with there's no argument
            embed = discord.Embed(description = f"Of course I'll notice you {ctx.author.mention} ʕ•ᴥ•ʔﾉ♡", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media1.tenor.com/images/865132c2b61df5e4a2a04ee0d7de686c/tenor.gif')
            return await ctx.send(embed=embed)
        if user.id == ctx.author.id: #check if the user taged himself
            embed = discord.Embed(description = f"Of course I'll notice you {ctx.author.mention} ʕ•ᴥ•ʔﾉ♡", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media1.tenor.com/images/865132c2b61df5e4a2a04ee0d7de686c/tenor.gif')
            return await ctx.send(embed=embed)
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"Finally someone noticed me, {ctx.author.mention} you're my senpai now!", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media1.tenor.com/images/bd39500869eeedd72d94274282fd14f2/tenor.gif')
            return await ctx.send(embed=embed)
        if user.bot: #check if it taged a bot
            return await ctx.send(f"Unfortunately **{user.mention}** is a bot so I don't think it can notice you :(")
        embed = discord.Embed(description = f'Hey {user.mention} please notice {ctx.author.mention}!!', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url='https://i.alexflipnote.dev/500ce4.gif')
        await ctx.send(embed=embed)



    #hug another user command
    @commands.command(aliases=['Hug', 'HUG'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def hug(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            embed = discord.Embed(description = f"Here {ctx.author.mention} , I'll give you a hug ♡", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://cdn.weeb.sh/images/Bkta0ExOf.gif')
            await ctx.send(embed=embed)
            return
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f'{ctx.author.mention} is feeling really lonely and hugs a pillow', colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media1.tenor.com/images/1a0ac2f256d11e323ccad554de71f0cf/tenor.gif')
            await ctx.send(embed=embed)
            return
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"I... I was not expecting it... thanks {ctx.author.mention}", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://64.media.tumblr.com/f2a878657add13aa09a5e089378ec43d/tumblr_n5uovjOi931tp7433o1_500.gif')
            await ctx.send(embed=embed)
            return
        if user.bot:
            embed = discord.Embed(description = f"HEY {ctx.author.mention}!! why are you trying to hug another bot?", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/27/16/68/271668b1037633d7f7ae63dc1a1c29f2.gif')
            await ctx.send(embed=embed)
            return

        #hugs gifs list
        gifshug = ['https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif',
                'https://cdn.weeb.sh/images/Hyv6uOQPZ.gif',
                'https://cdn.weeb.sh/images/Hyv6uOQPZ.gif',
                'https://cdn.weeb.sh/images/Sk80wyhqz.gif',
                'https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/tenor.gif',
                'https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif', #meh?
                'https://media1.tenor.com/images/7d6a56988dc7e6152ca578b7a1f24be9/tenor.gif',
                'https://media1.tenor.com/images/79aa56112b2d0eca4f50e9df188e18ad/tenor.gif',
                'https://cdn.weeb.sh/images/B11CDkhqM.gif',
                'https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif',
                'https://cdn.weeb.sh/images/H1X6OOmPW.gif',
                'https://cdn.weeb.sh/images/HJ7lY_QwW.gif']
        #hugs phrases
        hugs = [f'{ctx.author.mention} hugs tightly {user.mention}',
                f'{ctx.author.mention} hugs {user.mention}',
                f'{ctx.author.mention} hugs {user.mention} with love',
                f'{ctx.author.mention} forces {user.mention} to a hug',
                f'{ctx.author.mention} hugs {user.mention} to make him feel better',
                f'{ctx.author.mention} surprises {user.mention} with a hug']

        embed = discord.Embed(description = f'{random.choice(hugs)}', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(gifshug)}')
        await ctx.send(embed=embed)



    #kiss another user command
    @commands.command(aliases=['Kiss', 'KISS'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def kiss(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            await ctx.send(f'{ctx.author.mention} Y-you need to mention someone')
            return
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"{ctx.author.mention} you can't kiss yourself so here, take mine ♡", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/6a/46/8f/6a468f80cb1384d681440115d6e6d1b9.gif')
            await ctx.send(embed=embed)
            return
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"DUMMY!! do~don't do that to me {ctx.author.mention}", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/b0/93/ec/b093ec61870988f4098dd8b7f1d1cec1.gif')
            await ctx.send(embed=embed)
            return
        if user.bot:
            embed = discord.Embed(description = f"I get it {ctx.author.mention}, you're fine with anyone as long as it's a bot right?", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/07/77/44/07774417cc35d0727e4913a531cb851a.gif')
            await ctx.send(embed=embed)
            return

        #kiss gifs list
        gifskiss = ['https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif', #meh
                'https://media1.tenor.com/images/621ceac89636fc46ecaf81824f9fee0e/tenor.gif', #meh
                'https://media1.tenor.com/images/40711a5b00fcf9918ddef1aa483d993f/tenor.gif',
                'https://cdn.weeb.sh/images/rypMnpuvW.gif',
                'https://media1.tenor.com/images/a0b68f4704f811bfcc517574425e96a5/tenor.gif',
                'https://cdn.weeb.sh/images/B1MJ2aODb.gif',
                'https://media1.tenor.com/images/37ceeaa82fb503fb10bbd539ad4e3fd8/tenor.gif',
                'https://media1.tenor.com/images/3dc3bb6e35aa0d090527babe698bfe55/tenor.gif',
                'https://media1.tenor.com/images/be905a75eb3036494fc32df12b7c1b7a/tenor.gif',
                'https://cdn.weeb.sh/images/rJoL2pdvb.gif',
                'https://cdn.weeb.sh/images/Sk1k3TdPW.gif',
                'https://cdn.weeb.sh/images/ByiMna_vb.gif',
                'https://cdn.weeb.sh/images/Sksk4l51z.gif']
        #kiss phrases
        kiss = [f'{ctx.author.mention} kisses {user.mention}',
                f'{ctx.author.mention} just kissed {user.mention} all night long',
                f'{ctx.author.mention} forces a kiss on {user.mention}',
                f'{ctx.author.mention} kisses {user.mention} who loves it',
                f'{ctx.author.mention} surprises {user.mention} with a kiss',
                f'{ctx.author.mention} kisses {user.mention} and **5** others later',
                f'{ctx.author.mention} kisses {user.mention} but regrets it later',
                f'{ctx.author.mention} kisses {user.mention} but **{user.nick}** regrets it later',
                f'{ctx.author.mention} kisses {user.mention} and **{user.nick}** falls in love']

        embed = discord.Embed(description = f'{random.choice(kiss)}', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(gifskiss)}')
        await ctx.send(embed=embed)



    #slaps another user command
    @commands.command(aliases=['Slap', 'SLAP'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def slap(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            embed = discord.Embed(description = f"I'm... I'm sorry {ctx.author.mention} :( you made me do it", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/1c/8f/0f/1c8f0f43c75c11bf504b25340ddd912d.gif')
            await ctx.send(embed=embed)
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"I'm... I'm sorry {ctx.author.mention} :( you made me do it", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/1c/8f/0f/1c8f0f43c75c11bf504b25340ddd912d.gif')
            await ctx.send(embed=embed)
            return
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"Why? Why do you want to hurt me {ctx.author.mention}??", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media.tenor.com/images/7e623e17dd8c776aee5e0c3e0e9534c9/tenor.gif')
            await ctx.send(embed=embed)
            return
        if user.bot:
            embed = discord.Embed(description = f"Why {ctx.author.mention}? Why did you did you hurt another bot? you monster", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/39/ec/67/39ec6796a4c1722c046cbb30eaf9e210.gif')
            await ctx.send(embed=embed)
            return

        #slaps gifs list
        gifslap = ['https://media0.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif',
                'https://i.pinimg.com/originals/b8/f3/02/b8f302e2fa5f45fa4d472a23d828568b.gif',
                'https://media1.tenor.com/images/af36628688f5f50f297c5e4bce61a35c/tenor.gif',
                'https://cdn.weeb.sh/images/BJSpWec1M.gif',
                'https://cdn.weeb.sh/images/HkHCm1twZ.gif',
                'https://i.imgur.com/3rHE4Ee.gif',
                'https://cdn.weeb.sh/images/Bkj-oaV0Z.gif',
                'https://i.kym-cdn.com/photos/images/newsfeed/001/390/712/289.gif',
                'https://cdn.weeb.sh/images/SJlkNkFwb.gif',
                'https://cdn.weeb.sh/images/ByHUMRNR-.gif',
                'https://cdn.weeb.sh/images/SkSCyl5yz.gif',
                'https://cdn.weeb.sh/images/Hk6JVkFPb.gif']
        #slaps phrases
        slap = [f'{ctx.author.mention} slaps {user.mention}',
                f'{ctx.author.mention} slaps {user.mention} with all her mighty',
                f'{ctx.author.mention} surprises {user.mention} with a slap',
                f'{ctx.author.mention} slaps {user.mention} but **{user.nick}** likes it',
                f'{ctx.author.mention} slapped {user.mention} so hard that **{user.nick}** ends up liking it',
                f'{ctx.author.mention} slaps {user.mention} for no reason',
                f'{ctx.author.mention} slaps {user.mention} because **{user.nick}** was mean',
                f'{ctx.author.mention} slaps {user.mention} but **{user.nick}** take revenge later',
                f'{ctx.author.mention} slaps {user.mention} but regrets it later']

        embed = discord.Embed(description = f'{random.choice(slap)}', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(gifslap)}')
        await ctx.send(embed=embed)



    #pats another user command
    @commands.command(aliases=['Pat', 'PAT'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def pat(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            embed = discord.Embed(description = f"Okay {ctx.author.mention} I'll pat you this time ♡", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://64.media.tumblr.com/tumblr_lmi2d8FjRV1qd6621.gif')
            await ctx.send(embed=embed)
            return
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"Okay {ctx.author.mention} I'll pat you this time ♡", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://64.media.tumblr.com/tumblr_lmi2d8FjRV1qd6621.gif')
            await ctx.send(embed=embed)
            return
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"thanks for pating me {ctx.author.mention} ^^ I like you a little bit more now", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/8b/42/6c/8b426c9bedc37054cd7e73925fa10da5.gif')
            await ctx.send(embed=embed)
            return
        if user.bot:
            embed = discord.Embed(description = f"get out {ctx.author.mention}, you're not allowed to touch this bot", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.imgur.com/v44ViSk.gif')
            await ctx.send(embed=embed)
            return

        #pats gifs list
        gifspat = ['https://i.imgur.com/4ssddEQ.gif',
                'https://i.pinimg.com/originals/70/96/0e/70960e87fb9454df6a1d15c96c9ad955.gif',
                'https://thumbs.gfycat.com/NauticalDampJerboa-max-1mb.gif',
                'https://giffiles.alphacoders.com/184/184069.gif',
                'https://i.imgur.com/wz8ilbW.gif',
                'https://thumbs.gfycat.com/CaringInfiniteFirebelliedtoad-size_restricted.gif',
                'https://pa1.narvii.com/6523/b7ef2fa2dc1ba00f7d6c1e0ff1301cf62fe36e2c_hq.gif',
                'https://cdn.weeb.sh/images/rytzGAE0W.gif',
                'https://cdn.weeb.sh/images/HyWlxJFvb.gif',
                'https://cdn.weeb.sh/images/BJnD9a4Rb.gif',
                'https://cdn.weeb.sh/images/H1XkAyYNM.gif',
                'https://media1.tenor.com/images/2cf1704769d0227c69ebc4b6c85e274b/tenor.gif']
        #pats phrases
        pats = [f'{ctx.author.mention} pats {user.mention}',
                f'{ctx.author.mention} pats {user.mention} and **{user.nick}** likes it',
                f'{ctx.author.mention} surprises {user.mention} by patting them',
                f'{ctx.author.mention} pats {user.mention} but **{user.nick}** gets tired after a while',
                f'{ctx.author.mention} pats {user.mention} so hard that **{user.nick}** ends up with a headache later',
                f'{ctx.author.mention} pats {user.mention} for no reason',
                f'{ctx.author.mention} pats {user.mention} to make him feel better',
                f'{ctx.author.mention} pats {user.mention} and **{user.nick}** falls in love',
                f'{ctx.author.mention} pats {user.mention} all night long']

        embed = discord.Embed(description = f'{random.choice(pats)}', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(gifspat)}')
        await ctx.send(embed=embed)



    #kills another user command
    @commands.command(aliases=['Kill', 'KILL'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def kill(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            await ctx.send(f"{ctx.author.mention} Y-you want to kill someone?? you'll have to mention them...")
            return
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"Please don't kill yourself {ctx.author.mention}... I'll miss you...", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://data.whicdn.com/images/240443619/original.gif')
            await ctx.send(embed=embed)
            return
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"I won't let you kill me {ctx.author.mention} I'll fight you", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.imgur.com/VAbxu4H.gif')
            await ctx.send(embed=embed)
            return
        if user.bot:
            embed = discord.Embed(description = f"that's cute {ctx.author.mention}, but you can't kill a bot", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://data.whicdn.com/images/297349107/original.gif')
            await ctx.send(embed=embed)
            return

        #kills gifs list
        gifskill = ['https://i.imgur.com/St6brKP.gif',
                'https://i.imgur.com/roweWUe.gif',
                'https://i.imgur.com/ynyTOIB.gif',
                'https://i.imgur.com/mRo4oFL.gif',
                'https://i.imgur.com/CNX8gW8.gif']
        #kill phrases
        kills = [f'{ctx.author.mention} wants to kill {user.mention}',
                f'{ctx.author.mention} just killed {user.mention}',
                f'{ctx.author.mention} kills {user.mention} but regrets it later',
                f'{ctx.author.mention} tries to kill {user.mention} but **{user.nick}** survives',
                f'{ctx.author.mention} killed {user.mention} and enjoyed it way too much',
                f'{ctx.author.mention} kills {user.mention} for no reason']

        embed = discord.Embed(description = f'{random.choice(kills)}', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(gifskill)}')
        await ctx.send(embed=embed)


    #licks another user command
    @commands.command(aliases=['Lick', 'LICK'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def lick(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            embed = discord.Embed(description = f"WHA-WHAT? you want me to lick you {ctx.author.mention}?... pervert...", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media3.giphy.com/media/93c09w31Ys65O/giphy.gif')
            await ctx.send(embed=embed)
            return
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"WHA-WHAT? you want me to lick you {ctx.author.mention}?... pervert...", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media3.giphy.com/media/93c09w31Ys65O/giphy.gif')
            await ctx.send(embed=embed)
            return
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"do-don't lick me like that {ctx.author.mention}!", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://cdn.weeb.sh/images/Bkxge0uPW.gif')
            await ctx.send(embed=embed)
            return
        if user.bot:
            embed = discord.Embed(description = f"get away from that bot {ctx.author.mention}, I won't let you lick it", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://i.pinimg.com/originals/b6/34/6c/b6346ce53c26db1b3f474da4a6e7ebe2.gif')
            await ctx.send(embed=embed)
            return

        #lick gifs list
        gifslick = ['https://cdn.weeb.sh/images/S1Ill0_vW.gif',
                'https://cdn.weeb.sh/images/H1zlgRuvZ.gif',
                'https://cdn.weeb.sh/images/Sk15iVlOf.gif',
                'https://cdn.weeb.sh/images/rktygCOD-.gif',
                'https://cdn.weeb.sh/images/rykRHmB6W.gif']
        #lick phrases
        licks = [f'{ctx.author.mention} licks {user.mention}',
                f'{ctx.author.mention} licks {user.mention} and **{user.nick}** likes it',
                f'{ctx.author.mention} surprised {user.mention} with a lick',
                f'{user.mention} tries to resit {ctx.author.mention} licks but with no succes',
                f"{ctx.author.mention} starts to lick {user.mention} and can't stop",
                f'{ctx.author.mention} licks {user.mention} surprising them']

        embed = discord.Embed(description = f'{random.choice(licks)}', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(gifslick)}')
        await ctx.send(embed=embed)



    #cuddle with another user command
    @commands.command(aliases=['Cuddle', 'CUDDLE'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def cuddle(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            embed = discord.Embed(description = f"Take a cuddle from me {ctx.author.mention}", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://cdn.weeb.sh/images/B1SzeshCW.gif')
            await ctx.send(embed=embed)
            return
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"{ctx.author.mention} just wanted to cuddle with someone", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://cdn.weeb.sh/images/BJkABImvb.gif')
            await ctx.send(embed=embed)
            return
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"Take a cuddle from me {ctx.author.mention}", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://cdn.weeb.sh/images/B1SzeshCW.gif')
            await ctx.send(embed=embed)
            return
        if user.bot:
            embed = discord.Embed(description = f"thanks {ctx.author.mention} for showing love by using cuddle on a bot", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://cdn.weeb.sh/images/r1VzDkmjW.gif')
            await ctx.send(embed=embed)
            return

        #cuddle gifs list
        gifscuddle = ['https://cdn.weeb.sh/images/SyZk8U7vb.gif',
                'https://cdn.weeb.sh/images/BJseUI7wb.gif',
                'https://cdn.weeb.sh/images/rk2-UL7PW.gif',
                'https://cdn.weeb.sh/images/SJn18IXP-.gif',
                'https://cdn.weeb.sh/images/SykzL87D-.gif',
                'https://cdn.weeb.sh/images/HkZDkeamf.gif',
                'https://cdn.weeb.sh/images/r1A77CZbz.gif',
                'https://cdn.weeb.sh/images/ryfyLL7D-.gif']
        #cuddle phrases
        cuddle = [f'{ctx.author.mention} cuddles {user.mention}',
                f'{ctx.author.mention} cuddles with {user.mention} but only **{ctx.author.nick}** likes it',
                f"{ctx.author.mention} can't stop cuddling {user.mention}",
                f'{user.mention} tries to resit {ctx.author.mention} cuddles but ends up liking it',
                f"{ctx.author.mention} cuddles {user.mention} who hates it but **{ctx.author.nick}** don't care",
                f'{ctx.author.mention} suddenly cuddles {user.mention} surprising them',
                f'{ctx.author.mention} wishes {user.mention} would cuddle with them more often',
                f"{user.mention} hates {ctx.author.mention} cuddles (even if sometimes it doesn't seems so)",
                f"{user.mention} loves {ctx.author.mention} cuddles (even if sometimes it doesn't seems so)"]

        embed = discord.Embed(description = f'{random.choice(cuddle)}', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(gifscuddle)}')
        await ctx.send(embed=embed)



    #insults another user command
    @commands.command(aliases=['Insult', 'INSULT'])
    @commands.cooldown(1, 3.0, commands.BucketType.user)
    async def insult(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if not user:
            embed = discord.Embed(description = f"Fuck u {ctx.author.mention}", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://cdn.weeb.sh/images/rJ07FuXvZ.gif')
            await ctx.send(embed=embed)
            return
        if user.id == ctx.author.id:
            embed = discord.Embed(description = f"Fuck u {ctx.author.mention}", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://cdn.weeb.sh/images/rJ07FuXvZ.gif')
            await ctx.send(embed=embed)
            return
        if user.id == self.client.user.id:
            embed = discord.Embed(description = f"I won' let you insult me {ctx.author.mention}", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media1.tenor.com/images/aa6d975cb5318886db35f27f692d09d3/tenor.gif')
            await ctx.send(embed=embed)
            return
        if user.bot:
            embed = discord.Embed(description = f"Stop {ctx.author.mention}, I won' let you insult that bot", colour = random.randint(0, 0xFFFFFF))
            embed.set_image(url='https://media1.tenor.com/images/0309270c724249c5061338422cf1d325/tenor.gif')
            await ctx.send(embed=embed)
            return

        #insult gifs list
        gifsinsult = ['https://cdn.weeb.sh/images/HJNGt_mwZ.gif',
                'https://cdn.weeb.sh/images/ryxSrY_XDZ.jpeg',
                'https://cdn.weeb.sh/images/BJDmYumDZ.gif',
                'https://cdn.weeb.sh/images/HJyBFu7Db.gif',
                'https://cdn.weeb.sh/images/By9VFuXPb.gif',
                'https://cdn.weeb.sh/images/HyYfK_Qwb.gif',
                'https://cdn.weeb.sh/images/rJmEFd7DW.gif',
                'https://cdn.weeb.sh/images/rJbMK_7vW.gif']
        #insult phrases
        insult = [f'{ctx.author.mention} has insulted {user.mention}',
                f'{ctx.author.mention} has insulted {user.mention}']

        embed = discord.Embed(description = f'{random.choice(insult)}', colour = random.randint(0, 0xFFFFFF))
        embed.set_image(url=f'{random.choice(gifsinsult)}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(anime(client))
