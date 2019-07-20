import discord
import random
import os

token = os.environ["M8B_DISCORD_TOKEN"]
client = discord.Client()

response_list = ["As I see it, yes", "Yes", "No", "Very likely", "Not even close", "Maybe", "Very unlikely", "Gino's mom told me yes", "Gino's mom told me no", "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", " It is certain", "My sources say no", "Outlook good", "You may rely on it", "Very Doubtful", "Without a doubt"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!m8b"):
        lucky_num = random.randint(0,len(response_list) - 1)
        await message.channel.send(response_list[lucky_num])

client.run("{}".format(token))