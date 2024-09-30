from discord.ext import commands
import transactionsDB
import discord

from transactionsDB import TransactionDatabase

main_commands = discord.SlashCommandGroup("main commands", "A set of commands that serve the primary functionality of the bot.")

TDB = TransactionDatabase()

@main_commands.command(name="create", description="Creates a new escrow transaction.")
async def create_escrow(ctx: discord.ApplicationContext, amt: int):
    TDB.create_transaction(userid=ctx.author.id, amt=amt)
