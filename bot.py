import discord
import config
import requests
import riot
class Bot():
    def __init__(self) -> None:
        self.bot = []

    def run_bot(self):
        token = config.token
        client = discord.Client()

        @client.event
        async def on_ready():
            print(f'{client.user} is now running')
        
        client.run(token)