import notion_helper
import discord

class DiscordClient(discord.Client):
    def __init__(self, user, notion_client):
        self.notion_client = notion_client
        self.user = user

    async def on_ready(self):
        print(f'{self.client.user} has connected to Discord')

    async def on_message(self, message):
        if(message.content == "help"):
            await message.author.send("Enter your task in this format: name,catagory,priority,due date,details")
        else:    
            params = ','.split(message.content)
            if(len(params) > 0 and len(params) < 6):
                for i in range(len(params), 6):
                    params.append(None)
                self.notion_client.add(params[0], catagory=params[1], priority=params[2], due_date=params[3], text=params[4])
            else:
                message.author.send("Enter your task in this format: name,catagory,priority,due date(year-month-day),details")
    
