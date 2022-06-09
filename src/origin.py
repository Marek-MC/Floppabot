import discord
import discord.ext.commands
import json

# Literally just imports the Token from Json.
with open('TOKEN.json', 'r') as f:
    data=json.load(f);token=data['TOKEN'];f.close()
    
# Create the main client function.
class MyClient(discord.Client):
    async def on_ready(self): 
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message): # When client recieves a message
        print('{0.author}: {0.content}'.format(message))




# Startup
MyClient().run(token)

