from blockchainDB import BlockchainDatabase
from transactionsDB import TransactionDatabase
from discord.ext import commands
from asyncio import sleep as async_sleep
from asyncio import create_task
from commandgroups import main_commands
import discord

# INIT
blockchain = BlockchainDatabase()
transactions = TransactionDatabase()
bot = discord.Bot(intents=discord.Intents.all(), help_command=None)


async def change_status():
    activities = [
        discord.Activity(type=discord.ActivityType.watching, name="IN BETA"),
        discord.Activity(type=discord.ActivityType.playing, name="Made by @sippingsizzurp")
    ]

    while True:
        for activity in activities:
            await bot.change_presence(activity=activity)
            await async_sleep(10)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")
    create_task(change_status())

bot.add_application_command(main_commands.main_commands)

bot.run("")