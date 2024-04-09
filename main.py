import discord
import json
from discord import Intents, Status, Activity, ActivityType
from service_providers.migration_provider import run_migrations
from service_providers.seeding_provider import run_seeders

from config.vault import token
from config.app import Settings
from utilities.database import mysql_login, selector, modifyData
from datetime import datetime

is_seeding_enabled = Settings().get_setting("seeding")

intents = Intents(guilds=True)
bot = discord.Bot(intents=intents, status=Status.online,
                  activity=Activity(type=ActivityType.watching, name="chat"))

bot.load_extensions("cogs")  # Loads all cogs in the cogs folder


@bot.listen()
async def on_connect():
    await run_migrations()
    if is_seeding_enabled:
        await run_seeders()
    print('-' * 50)
    print('✓ Migrations finished successfully.')
    print(f'✓ {bot.user} is connected to Discord.')
    # await bot.sync_commands(guild_ids=[0]) #You might need to uncomment this if the slash commands aren't appearing


@bot.listen()
async def on_ready():
    print('-' * 50)
    print(f'✓ Logged in as {bot.user} successfully.')


@bot.check
async def guild_only(ctx):
    return ctx.guild is not None


bot.run(token)
