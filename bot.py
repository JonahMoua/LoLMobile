import discord
import config

def run_bot():
    token = config.token
    client = discord.Client()


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    client.run(token)