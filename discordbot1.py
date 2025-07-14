import discord
import zarbot123123
import yaziturabot123123
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    global res
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$cock slayeh'):
        await message.channel.send("slayy gurlll :stuck_out_tongue:")
    elif message.content.startswith('$latenightproject'):
        await message.channel.send("MTM4OTMzMTcwMjY0MzU1NjYwNA.GqzZug.wke4OZY2XdnQ-5SZiWFLAaK4ASeRE6WWrN-e54")
    elif message.content.startswith('$zar'):
        await message.channel.send(zarbot123123.roll())
    elif message.content.startswith('$yazıtura'):
        await message.channel.send(yaziturabot123123.flip())
    else:
        await message.channel.send(message.content)


@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

client.run("MTM4OTMzMTcwMjY0MzU1NjYwNA.GqzZug.wke4OZY2XdnQ-5SZiWFLAaK4ASeRE6WWrN-e54")