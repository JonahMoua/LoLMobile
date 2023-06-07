import discord

def run_bot():
    token = 'MTExNjA5MTAzMTA1ODkxNTQ1OQ.GQ0PWv.oGKGgQocdUvN4tOjHH0hV9gR2WCqnQYpsyAJ6Q'
    client = discord.Client()


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    client.run(token)