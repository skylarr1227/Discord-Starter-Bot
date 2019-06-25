import discord
from discord.ext import commands


class General:
    def __init__(self,client):
        self.client = client
    @commands.command(pass_context=True)
    async def testpls(self, ctx):
        print("uwu reading")
        await ctx.channel.send("Ayy, reading you loud and clear captain")
        
def setup(client):
    client.add_cog(General(client))
