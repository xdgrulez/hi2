# This example requires the "message_content" intent.

import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return

    if message.content.startswith("$hi"):
        await message.channel.send("Hi!")

token_str = os.environ["HI_TOKEN"]
client.run(token_str)
