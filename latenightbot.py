import discord
from discord.ext import commands
import zarbot123123
import yaziturabot123123

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx):
    await ctx.send("heh")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # saniye --> milisaniye
    await ctx.send(f"{latency}ms")

@bot.command()
async def zar(ctx):
    await ctx.send(zarbot123123.roll())

@bot.command()
async def yazıtura(ctx):
    await ctx.send(yaziturabot123123.flip())

@bot.command()
async def yardım(ctx):
    mesaj = (
        "**Kullanılabilir Komutlar:**\n"
        "?hello: Bot kendini tanıtır ve merhaba der.\n"
        "?heh: bot heh mesajı gönderir.\n"
        "?sil (sayı): Verilen sayı kadar mesajı siler.\n"
        "?ping: Botun gecikmesini (ping) milisaniye olarak gösterir.\n" \
        "?zar: Bot 6 taraflı bir zar çevirip sonuçları yazar. \n"
        "?yazıtura: Bot bot yazı tura çevirip sonuçları yazar. \n"
    )
    await ctx.send(mesaj)

bot.run(TOKEN BURAYA)