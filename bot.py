import discord
import responses
from discord.ext import commands
from keep_alive import keep_alive
async def send_message(message,user_message,is_private):
    try:
        response= responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
def run_discord_bot():
    TOKEN = 'MTA0ODczNjYxNTYzMzI3MjkzMw.G7wX8R.lJItemMBbnHWitmMQZHORn4aQvkQkPALrCvXBU'
    intents = discord.Intents.default()
    intents.members = True

    intents.message_content = True 


    client= discord.Client(intents=intents)
    bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')
    @bot.command
    async def rps(message):
      if message.author == client.user:
            return
      await message.channel.send(f'Pong! {round(client.latency * 1000)} ms')
    
  
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        await client.change_presence(activity=discord.Game(name="with Mudae >.<"))
    @client.event
    async def on_member_join(member):
        try:
            channel = member.guild.system_channel
            embedVar = discord.Embed(title="Welcome to Akio!! <:02_hello:862771386501824592>", description=f"{member.mention} just joined! \n Feel free to explore and have fun in our server <:02_love:865566023435550730> ", color=0x9208ea)
            embedVar.set_thumbnail(url="https://media.discordapp.net/stickers/892387220269461554.webp?size=128")
            await channel.send(embed=embedVar)
        except:
            channel = member.guild.get_channel(921975028608802836)
            embedVar = discord.Embed(title="Welcome to Akio!! <:02_hello:862771386501824592>", description=f"{member.mention} just joined! \n Feel free to explore and have fun in our server <:02_love:865566023435550730> ", color=0x9208ea)
            embedVar.set_thumbnail(url="https://media.discordapp.net/stickers/892387220269461554.webp?size=128")
            await channel.send(embed=embedVar)

    @client.event
    async def on_member_remove(member):
        try:
            channel = member.guild.system_channel
            
            embedVar = discord.Embed(title="Bye-Bye <:KannaHello:1029145517906739302>", description=f"Hope {member.mention} had fun in our server <:IrizchuPat:1029146890580803635>\n See you again!!", color=0x9208ea)
            embedVar.set_thumbnail(url="https://media.discordapp.net/stickers/892387220269461554.webp?size=128")
            await channel.send(embed=embedVar)
        except:
            channel = member.guild.get_channel(921975028608802836)
            embedVar = discord.Embed(title="Bye-Bye <:KannaHello:1029145517906739302>", description=f"Hope {member.mention} had fun in our server <:IrizchuPat:1029146890580803635>\n See you again!!", color=0x9208ea)
            embedVar.set_thumbnail(url="https://media.discordapp.net/stickers/892387220269461554.webp?size=128")
            await channel.send(embed=embedVar)
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith("!akio"):
            response="nani"
            await message.channel.send(response)


        
        username=str(message.author)
        user_message=str(message.content)
        channel = str(message.channel)
        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0]=='?':
            user_message= user_message[1:]
            await send_message(message,user_message,is_private=True)
        else:
            await send_message(message,user_message,is_private=False)
    keep_alive()
    client.run(TOKEN)



