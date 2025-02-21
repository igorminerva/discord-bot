import discord
import random 
import requests
import os
 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
insults = [
    "Sei così lento che i piccioni ti superano in volo!",
    "Sei così intelligente che hai inventato l'acqua asciutta!",
    "Sei così forte che vinci a braccio di ferro contro un fantasma!",
    "Sei così bello che i mirror ti chiedono l'autografo!",
    "Sei così veloce che arrivi in ritardo prima di partire!",
    "Sei così simpatico che i clown ti chiedono consigli!",
    "Sei così brillante che i diamanti ti invidiano!"
]


@client.event
async def on_ready():
    print(f'Logged in as {client.user}! Bot is ready.')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content == '!ping':
        n = random.randrange(insults.__len__())
        await message.channel.send(f'{message.author.mention}, {insults[n]}!')

    if message.content == '!dog':
        try:
            # Fetch random dog image URL from the API
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            response.raise_for_status()  # Ensure the request was successful
            data = response.json()
            image_url = data['message']  # Get the image URL from the API response

            # Send the image to the Discord channel
            await message.channel.send(image_url)

        except Exception as e:
            await message.channel.send("Sorry, I couldn't fetch a dog image. 🐶")
            print(f"Error fetching dog image: {e}")

    if message.content == '!alessio' or message.content == '!simo':
        try:
            response = requests.get('https://animals.maxz.dev/api/monkey/random')
            response.raise_for_status()  # Ensure the request was successful
            data = response.json()
            image_url = data['image']  # Get the image URL from the API response

            # Send the image to the Discord channel
            await message.channel.send(image_url)

        except Exception as e:
            await message.channel.send("Sorry, I couldn't fetch an Alessio image.")
            print(f"Error fetching alessio image: {e}")
    

        

client.run(os.getenv('DISCORD_TOKEN'))
