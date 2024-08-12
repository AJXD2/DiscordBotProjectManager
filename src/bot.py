from disnake.ext import commands
import disnake
from src.settings import settings

bot = commands.InteractionBot(
    intents=disnake.Intents.all(),
    test_guilds=[int(settings.TEST_GUILD)],
    owner_id=int(settings.OWNER_ID),
    sync_commands_debug=True,
    application_id=int(settings.DISCORD_CLIENT_ID),
)

bot.load_extensions("src/cogs")
