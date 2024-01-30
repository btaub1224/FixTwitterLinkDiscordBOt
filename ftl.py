"""
Discord bot to fix Twitter/Tiktok links so media displays appropiately
"""
import os
import discord
from dotenv import load_dotenv
intents = discord.Intents.all()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """
    Show bot is logged in 
    """
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    """
    Check every message (not sent by the bot) and check for valid urls to change
    """
    if message.author == client.user:
        return

    valid_urls = ["https://twitter.com", "https://x.com"]
    tiktok_url = "https://www.tiktok.com"

    if any(valid_url in message.content for valid_url in valid_urls):
        new_message = "https://fxtwitter.com" + \
            str(message.content.split(".com", 1)[1].split(" ", 1)[0])
        await message.channel.send("Fixed twitter link, originally posted by posted by " + \
            str(message.author) + ": " + new_message)

    elif tiktok_url in message.content:
        new_message = "https://vxtiktok.com" + \
            str(message.content.split(".com", 1)[1].split(" ", 1)[0])
        await message.channel.send("Fixed tiktok link, originally posted by posted by " + \
            str(message.author) + ": " + new_message)

load_dotenv()
client.run(os.getenv('TOKEN'))
