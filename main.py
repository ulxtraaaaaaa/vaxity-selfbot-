import discord
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore, Style
import random
import datetime
import string
import asyncio
import json
import requests
import urllib

with open("config.json") as f:
  j = json.load(f)
token = j["token"]
prefix = j["prefix"]

intents = discord.Intents.all()

client = commands.Bot(command_prefix=prefix, self_bot = True, intents = intents)

client.remove_command("help")

@client.event
async def on_ready():
  print(Fore.BLUE + """ ██▒   █▓ ▄▄▄      ▒██   ██▒ ██▓▄▄▄█████▓▓██   ██▓
▓██░   █▒▒████▄    ▒▒ █ █ ▒░▓██▒▓  ██▒ ▓▒ ▒██  ██▒
 ▓██  █▒░▒██  ▀█▄  ░░  █   ░▒██▒▒ ▓██░ ▒░  ▒██ ██░
  ▒██ █░░░██▄▄▄▄██  ░ █ █ ▒ ░██░░ ▓██▓ ░   ░ ▐██▓░
   ▒▀█░   ▓█   ▓██▒▒██▒ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░
   ░ ▐░   ▒▒   ▓▒█░▒▒ ░ ░▓ ░░▓    ▒ ░░      ██▒▒▒ 
   ░ ░░    ▒   ▒▒ ░░░   ░▒ ░ ▒ ░    ░     ▓██ ░▒░ 
     ░░    ░   ▒    ░    ░   ▒ ░  ░       ▒ ▒ ░░  
      ░        ░  ░ ░    ░   ░            ░ ░     
     ░                                    ░ ░     """ + Fore.RESET)
  print(Fore.BLUE + f"Logged in as: {Fore.RESET}{Fore.RED}[{Fore.RESET}{Fore.BLUE}{client.user.name}#{client.user.discriminator}{Fore.RESET}{Fore.RED}]" + Fore.RESET)
  print(Fore.BLUE + f"Your Prefix Is: {Fore.RED}[{Fore.RESET}{Fore.BLUE}{prefix}{Fore.RESET}{Fore.RED}]" + Fore.RESET)
  print(Fore.BLUE + f"You Are In {len(client.guilds)} Servers!" + Fore.RESET)
  
  
  @client.command()
  async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
    embed.set_author(name="𝙑𝘼𝙓𝙄𝙏𝙔 𝙎𝙀𝙇𝙁𝘽𝙊𝙏",icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Vaxity SelfBot")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/798884296983183400/810658530062761984/image0.gif")
    embed.add_field(name="*🎸 𝙈𝙤𝙙𝙚𝙧𝙖𝙩𝙞𝙤𝙣*",value="`Shows The Moderation Commands`",inline=False)
    embed.add_field(name="*🎸 𝙈𝙞𝙨𝙘𝙚𝙡𝙡𝙖𝙣𝙚𝙤𝙪𝙨*",value="`Shows The Miscellaneous Commands`",inline=False)
    embed.add_field(name="*🎸 𝙐𝙩𝙞𝙡𝙞𝙩𝙮*",value="`Shows The Utility Commands`",inline=False)
    embed.add_field(name="*🎸 𝙎𝙩𝙖𝙩𝙪𝙨*",value="`Shows The Status Commands`",inline=False)
    embed.add_field(name="*🎸 𝙉𝙎𝙁𝙒*",value="`Shows The NSFW Commands`",inline=False)
    await ctx.send(embed=embed)
    
@client.command(aliases=["mod"])
async def moderation(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description="*[] Is Required, <> Is Optional*",timestamp=ctx.message.created_at)
  embed.set_footer(text="Vaxity SelfBot")
  embed.set_author(name="𝙈𝙊𝘿𝙀𝙍𝘼𝙏𝙄𝙊𝙉",icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.add_field(name="*🎸 𝘽𝙖𝙣 [𝙢𝙚𝙢𝙗𝙚𝙧]*",value="`Bans The Specified Member`",inline=False)
  embed.add_field(name="*🎸 𝙆𝙞𝙘𝙠 [𝙢𝙚𝙢𝙗𝙚𝙧]*",value="`Kicks The Specified Member`",inline=False)
  embed.add_field(name="*🎸 𝘼𝙍 [𝙢𝙚𝙢𝙗𝙚𝙧] [𝙧𝙤𝙡𝙚]*",value="`Adds The Specified Role To The Specified Member`",inline=False)
  embed.add_field(name="*🎸 𝙏𝙍 [𝙢𝙚𝙢𝙗𝙚𝙧] [𝙧𝙤𝙡𝙚]*",value="`Takes The Specified Role From The Specified Member`",inline=False)
  embed.add_field(name="*🎸 𝙋𝙪𝙧𝙜𝙚 <𝙖𝙢𝙤𝙪𝙣𝙩>*",value="`Purges The Specified Amount Of Messages`",inline=False)
  embed.set_image(url="https://cdn.discordapp.com/attachments/798884296983183400/810672071193395230/image0.gif")
  await ctx.send(embed=embed)
  
@client.command()
async def status(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,description="*[] Is Required, <> Is Optional*")
  embed.set_footer(text="Vaxity SelfBot")
  embed.set_author(name="𝙎𝙏𝘼𝙏𝙐𝙎",icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.set_image(url="https://cdn.discordapp.com/attachments/798884296983183400/810673820230746112/image0.gif")
  embed.add_field(name="*🎸 𝙂𝙖𝙢𝙚 [𝙣𝙖𝙢𝙚]*",value="`Changes Your Status To A Game`",inline=False)
  embed.add_field(name="*🎸 𝙎𝙩𝙧𝙚𝙖𝙢 [𝙣𝙖𝙢𝙚]*",value="`Changes Your Status To A Stream`",inline=False)
  embed.add_field(name="*🎸 𝙒𝙖𝙩𝙘𝙝 [𝙣𝙖𝙢𝙚]*",value="`Changes Your Status To Watching`",inline=False)
  embed.add_field(name="*🎸 𝘾𝙤𝙢𝙥𝙚𝙩𝙞𝙣𝙜 [𝙣𝙖𝙢𝙚]*",value="`Changes Your Status To Competing In`",inline=False)
  embed.add_field(name="*🎸 𝘾𝙡𝙚𝙖𝙧*",value="`Clears Your Custom Status`",inline=False)
  await ctx.send(embed=embed)
  
@client.command()
async def utility(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,description="*[] Is Required, <> Is Optional*")
  embed.set_footer(text="Vaxity SelfBot")
  embed.set_author(name="𝙐𝙏𝙄𝙇𝙄𝙏𝙔",icon_url=ctx.author.avatar_url)
  embed.set_image(url=ctx.author.avatar_url)
  embed.set_image(url="https://cdn.discordapp.com/attachments/798758041885212685/810678549211906058/image0.gif")
  embed.add_field(name="*🎸 𝘼𝙑 <𝙢𝙚𝙢𝙗𝙚𝙧>*",value="`Shows The Mentioned Members Avatar`",inline=False)
  embed.add_field(name="*🎸 𝙎𝙚𝙧𝙫𝙚𝙧𝙄𝙣𝙛𝙤*",value="`Shows The Servers Info`",inline=False)
  embed.add_field(name="*🎸 𝘾𝙧𝙚𝙖𝙩𝙤𝙧*",value="`Shows This SelfBots Creator`",inline=False)
  embed.add_field(name="*🎸 𝙋𝙞𝙣𝙜*",value="`Shows The Clients Latency`",inline=False)
  embed.add_field(name="*🎸 𝙄𝙣𝙛𝙤*",value="`Shows Some Info About Yourself`",inline=False)
  await ctx.send(embed=embed)
  
@client.command(aliases=["misc"])
async def miscellaneous(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,description="*[] Is Required, <> Is Optional*")
  embed.set_footer(text="Vaxity SelfBot")
  embed.set_author(name="𝙈𝙄𝙎𝘾𝙀𝙇𝙇𝘼𝙉𝙀𝙇𝙊𝙐𝙎,",icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.set_image(url="https://cdn.discordapp.com/attachments/798938425033228339/810960396520652861/image0.gif")
  embed.add_field(name="*🎸 𝙃𝙪𝙜 [𝙢𝙚𝙢𝙗𝙚𝙧] <𝙢𝙚𝙢𝙗𝙚𝙧>*",value="`Sends a gif of hugging the mentioned members/member`",inline=False)
  embed.add_field(name="*🎸 𝙆𝙞𝙨𝙨 [𝙢𝙚𝙢𝙗𝙚𝙧] <𝙢𝙚𝙢𝙗𝙚𝙧>*",value="`Sends a gif of kissing the mentioned members/member`",inline=False)
  embed.add_field(name="*🎸 𝙎𝙥𝙖𝙢 [𝙩𝙚𝙭𝙩]*",value="`Spams The Specified Text`",inline=False)
  embed.add_field(name="*🎸 𝘼𝙨𝙘𝙞𝙞 [𝙩𝙚𝙭𝙩]*",value="`Sends The Specified Text In Ascii`",inline=False)
  embed.add_field(name="*🎸 𝙒𝙞𝙯𝙯*",value="`Fake Wizzes The Server, Only Meant To Scare Friends`",inline=False)
  await ctx.send(embed=embed)
  
@client.command()
async def nsfw(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
  embed.set_footer(text="Vaxity SelfBot")
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.set_image(url="https://cdn.discordapp.com/attachments/799074981769248819/811409095231668245/image0.gif")
  embed.set_author(name="𝙉𝙎𝙁𝙒",icon_url=ctx.author.avatar_url)
  embed.add_field(name="*🎸 𝙃𝙚𝙣𝙩𝙖𝙞*",value="`Sends A Hentai Image`",inline=False)
  embed.add_field(name="*🎸 𝙎𝙚𝙭*",value="`Sends A Sex Image`",inline=False)
  embed.add_field(name="*🎸 𝙏𝙞𝙩𝙨*",value="`Sends A Tit Image`",inline=False)
  embed.add_field(name="*🎸 𝙋𝙪𝙨𝙨𝙮*",value="`Sends A Pussy Image`",inline=False)
  embed.add_field(name="*🎸 𝘿𝙞𝙘𝙠*",value="`Sends A Dick Image`",inline=False)
  await ctx.send(embed=embed)
  
@client.command()
async def ban(ctx, member: discord.Member, *, reason):
  await ctx.message.delete()
  await member.ban(reason=reason)
  
@client.command()
async def kick(ctx, member: discord.Member, *, reason):
  await ctx.message.delete()
  await member.kick(reason=reason)
  
@client.command()
async def ar(ctx, member: discord.Member, role: discord.Role):
  await ctx.message.delete()
  await member.add_roles(role)
  
@client.command()
async def tr(ctx, member: discord.Member, role: discord.Role):
  await ctx.message.delete()
  await member.remove_roles(role)
  
@client.command()
async def mute(ctx, member: discord.Member):
  await ctx.message.delete()
  if isinstance(error, commands.RoleNotFound):
    await ctx.send("Muted Role Not Found!")
  else:
    role = client.get_role("Muted")
    await member.add_roles(role)
  
@client.command()
async def game(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Game(name=x))
  
@client.command()
async def stream(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Streaming(name=x, url="https://twitch.tv/ulxywulxy"))
  
@client.command()
async def watch(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=x))
  
@client.command()
async def competing(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=x))
  
@client.command()
async def av(ctx, member: discord.Member=None):
  member = ctx.author if not member else member
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0))
  embed.set_image(url=member.avatar_url)
  await ctx.send(embed=embed)

@client.command()
async def creator(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),title="Creators!",description="Ulxtra, <@798757277090709544>")
  await ctx.send(embed=embed)
  
@client.command()
async def ping(ctx):
  await ctx.message.delete()
  msg = await ctx.send("Pinging...")
  await asyncio.sleep(5)
  await msg.edit(content=f"Pong! {round(client.latency * 1000)}")
  
@client.command()
async def info(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0))
  embed.set_author(name=f"{ctx.author}'s Info!",icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.add_field(name="**Username:**",value=client.user.name,inline=False)
  embed.add_field(name="**ID:**",value=client.user.id,inline=False)
  embed.add_field(name="**Servers:**",value=f"{len(client.guilds)}",inline=False)
  await ctx.send(embed=embed)
  
@client.command()
async def spam(ctx, *, x):
  await ctx.message.delete()
  for i in range(100):
    await ctx.send(x)
    
@client.command()
async def clear(ctx):
  await ctx.message.delete()
  await client.change_presence(status=discord.Status.dnd)
  
@client.command()
async def purge(ctx, amount=1):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)
  
@client.command()
async def image(ctx, link):
  links = ["ulxtra.is-hot","ulxtra.runs-you","ak.shitted-on.me-wtf","child.porn"]
  await ctx.message.delete()
  embed = discord.Embed(color=discord.Colour.dark_theme(),title="**czar ratted me wtf**",description="whatever is in this image is gay")
  embed.set_image(url=link)
  await ctx.send(f"https://{random.choice(links)}", embed=embed)
    
@client.command()
async def wizz(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"`WIZZING {ctx.guild.name}`")
  await asyncio.sleep(1)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.text_channels)} Text Channels**")
  await asyncio.sleep(3)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.voice_channels)} Voice Channels**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.categories)} Categories**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.roles)} Roles**")
  await asyncio.sleep(5)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Text Channels**")
  await asyncio.sleep(5)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Webhooks**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Roles**")
  await asyncio.sleep(3)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Categories**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Sending Pings**")
  await asyncio.sleep(10)
  await msg.edit(content=f"`WIZZED {ctx.guild.name}`")
  
@client.command()
async def ascii(ctx,*,message):
  await ctx.message.delete()
  ascii = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}").text
  if len("```"+ascii+"```") > 2000:
    return
  await ctx.send(f"```{ascii}```")

@client.command()
async def hug(ctx, member: discord.Member, user: discord.Member=None):
  await ctx.message.delete()
  user = ctx.author if not user else user
  hugg = requests.get("https://nekos.life/api/v2/img/hug")
  res = hugg.json()
  embed=discord.Embed(description=f"{user.mention} Hugs {member.mention}",color=discord.Colour.from_rgb(255,0,0))
  embed.set_image(url=res["url"])
  await ctx.send(embed=embed)
  
@client.command()
async def kiss(ctx,member: discord.Member, user: discord.Member=None): 
  await ctx.message.delete()
  user = ctx.author if not user else user
  kisss = requests.get("https://nekos.life/api/v2/img/kiss")
  res = kisss.json()
  embed=discord.Embed(description=f"{user.mention} Kisses {member.mention}",color=discord.Colour.from_rgb(255,0,0))
  embed.set_image(url=res["url"])
  await ctx.send(embed=embed)
  
@client.command()
async def hentai(ctx): 
  await ctx.message.delete()
  hentai = requests.get("https://nekos.life/api/v2/img/hentai")
  res = hentai.json()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
  embed.set_author(name="𝙃𝙀𝙉𝙏𝘼𝙄",icon_url=ctx.author.avatar_url)
  embed.set_image(url=res["url"])
  await ctx.send(embed=embed)
  
@client.command()
async def pussy(ctx):
  await ctx.message.delete()
  pussy = requests.get("https://nekos.life/api/v2/img/pussy")
  res = pussy.json()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
  embed.set_author(name="𝙋𝙐𝙎𝙎𝙔",icon_url=ctx.author.avatar_url)
  embed.set_image(url=res["url"])
  await ctx.send(embed=embed)
  
@client.command()
async def dick(ctx):
  await ctx.message.delete()
  dick = requests.get("https://nekos.life/api/v2/img/blowjob")
  res = dick.json()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
  embed.set_author(name="𝘿𝙄𝘾𝙆",icon_url=ctx.author.avatar_url)
  embed.set_image(url=res["url"])
  await ctx.send(embed=embed)
  
@client.command()
async def tits(ctx):
  await ctx.message.delete()
  boobs = requests.get("https://nekos.life/api/v2/img/boobs")
  res = boobs.json()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
  embed.set_author(name="𝙏𝙄𝙏𝙎",icon_url=ctx.author.avatar_url)
  embed.set_image(url=res["url"])
  await ctx.send(embed=embed)

@client.command()
async def sex(ctx):
  await ctx.message.delete()
  anal = requests.get("https://nekos.life/api/v2/img/anal")
  res = anal.json()
  embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
  embed.set_author(name="𝙎𝙀𝙓",icon_url=ctx.author.avatar_url)
  embed.set_image(url=res["url"])
  await ctx.send(embed=embed)
  
client.run(token,bot=False)
