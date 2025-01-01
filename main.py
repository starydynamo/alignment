import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from responses import AlignmentSystem

# Load bot token from .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Alignment System instance
alignment_system = AlignmentSystem()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="alignmentcreate")
async def alignment_create(ctx, character_name: str):
    response = alignment_system.create_character(character_name)
    await ctx.send(response)

@bot.command(name="characterassign")
async def character_assign(ctx, character_name: str, alignment: int):
    response = alignment_system.assign_alignment(character_name, alignment)
    await ctx.send(response)

@bot.command(name="characterrank")
async def character_rank(ctx, character_name: str, change: str):
    try:
        change_value = int(change)
        response = alignment_system.rank_character(character_name, change_value)
        await ctx.send(response)
    except ValueError:
        await ctx.send("Invalid rank change. Please provide a number.")

@bot.command(name="characteralignment")
async def character_alignment(ctx, character_name: str):
    response = alignment_system.track_alignment(character_name)
    await ctx.send(response)

@bot.command(name="characterlist")
async def character_list(ctx):
    response = alignment_system.list_characters()
    await ctx.send(response)

@bot.command(name="groupalignment")
async def group_alignment(ctx):
    response = alignment_system.group_alignment()
    await ctx.send(response)

@bot.command(name="me")
async def assign_user_to_character(ctx, character_name: str):
    discord_user = str(ctx.author)
    response = alignment_system.assign_user(discord_user, character_name)
    await ctx.send(response)

bot.run(TOKEN)
