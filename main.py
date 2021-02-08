import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!help For Commands'))
    print('Bot Loaded.')

@client.command()    
async def ping(ctx):
   await ctx.send(f'pong {round(client.latency * 1000)}ms')
   
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=5):
   await ctx.channel.purge(limit=amount)   
   await ctx.send('``Succesfully Purged.``')
   
@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No Reason Provided"):
   await member.send("``You have been kicked from a server that uses Insanity, You was kicked for: +reason``")
   await member.kick(reason=reason)


@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)  

@client.command(aliases=['user','info'])
async def information(ctx, member : discord.Member):
      embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.red())
      embed.add_field(name = "ID", value = member.id , inline = True)
      await ctx.send(embed=embed) 


@client.command()
async def unban(ctx, *, member):
   banned_users = await ctx.guild.bans()
   member_name, member_discriminator = member.split('#')
   for ban_entry in banned_users:
       user = ban_entry.user
       
       if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user) 
          await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
          return
          
client.run('ODA4MzMwNjkxMTQ1MjM2NDkx.YCE-ng.1w54Pq0PeGOIjpPlw4-IvqxoZj0')  
   

