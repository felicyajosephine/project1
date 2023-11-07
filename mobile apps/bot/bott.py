import discord
import repond
# import respondses


async def send_message(message, user_message, is_private):
    try:
        respond = repond.handel_response(user_message)
        await message.author.send(respond) if is_private else await message.channel.send(respond)
    except Exception as e:
        print (e)

def run_disc_bot():
    TOKEN = "MTE3MTQyOTk2MzcxMTM4MTU4NA.Gggq22.SsigO7Ivtz9bLpLBJZrXasMJYzKUUYvaouZfho"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    # client = discord.Client()



    @client.event
    async def on_ready():
        print(f"{client.user}is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said : '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
    
