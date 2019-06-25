import discord, asyncio
from datetime import datetime
from discord.ext.commands import Bot
from discord.ext import commands
from settings import *
command_sets = ["general.test"]


class DiscordBot(commands.Bot):
   def __init__(self):
      super().__init__(command_prefix=config.COMMANDPREFIX, case_insensitive=True)
      self.uptime = datetime.utcnow()
      self.remove_command('help')
      ##self.modules = ['general','moderation']
      for extension in command_sets:
         try:
            self.load_extension('modules.'+extension)
         except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
         else:
            print("Loaded: {}".format(extension))

            
   async def on_ready(self):
       print(login_string)
       print('Username: ' + str(self.user.name))
       print('Client ID: ' + str(self.user.id))
       print('Invite URL: ' + 'https://discordapp.com/oauth2/authorize?&client_id=' + str(self.user.id) + '&scope=bot&permissions=0')
       if not hasattr(self, 'uptime'):
           self.uptime = datetime.utcnow()
   
   def isOwner(self,message):
       return (message.author.id == config.OWNERID)
   @commands.command()
   async def reload(self):
      for extension in command_sets:
         try:
            self.load_extension('modules.'+extension)
         except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
         else:
            print("Loaded: {}".format(extension))
client = DiscordBot()


client.run(config.TOKEN)

