import socket
import discord
import asyncio
import os
from discord.ui import Button, View

# Your bot token
TOKEN = os.environ['DISCORD_TOKEN']

# Create a client instance of the bot
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


# Check if port is open on server
def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            return True
    except (socket.timeout, socket.error):
        return False


# Function to periodically check server and update the bot's status
async def check_and_update_status():
    host = 'configure to your personal ip/domain (e.g minecraftserver.com)'
    port = 25565
    while True:
        # Check if server is online
        status = 'online' if check_port(host, port) else 'offline'

        # Update bot's presence based on server status
        if status == 'online':
            await bot.change_presence(activity=discord.Game(
                name="🟢SERVER ONLINE🟢"))
        else:
            await bot.change_presence(activity=discord.Game(
                name="🔴SERVER OFFLINE🔴"))

        # Wait for 30 seconds before checking again
        await asyncio.sleep(30)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    # Start the server status checking loop
    await check_and_update_status()


# Run the bot
bot.run(TOKEN)
