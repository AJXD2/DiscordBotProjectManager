from disnake.ext import commands
import disnake


class Default(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Ping!")
    async def ping(self, inter: disnake.CommandInteraction):
        await inter.response.send_message("Pong!")


def setup(bot: commands.Bot):
    bot.add_cog(Default(bot))
