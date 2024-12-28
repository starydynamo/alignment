import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Alignment descriptions
alignment_map = {
    100: "Lawful Good",
    90: "Neutral Good",
    80: "Chaotic Good",
    70: "Lawful Neutral",
    60: "True Neutral",
    50: "Unaligned",
    40: "Chaotic Neutral",
    30: "Lawful Evil",
    20: "Neutral Evil",
    10: "Chaotic Evil",
    0: "Hellish"
}

# Character library
characters = {}

# Load and save character data
def load_characters():
    try:
        with open("characters.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_characters():
    with open("characters.json", "w") as file:
        json.dump(characters, file, indent=4)

characters = load_characters()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Command: Create character
@bot.command(name="alignmentcreate")
async def create_character(ctx, name: str):
    if name in characters:
        await ctx.send(f"Character {name} already exists!")
    else:
        characters[name] = 50  # Default alignment
        save_characters()
        await ctx.send(f"Character {name} created with alignment: {alignment_map[50]}")

# Command: Assign alignment
@bot.command(name="characterassign")
async def assign_alignment(ctx, name: str, value: int):
    if name not in characters:
        await ctx.send(f"Character {name} does not exist!")
    elif value not in alignment_map:
        await ctx.send("Invalid alignment value! Use one of the predefined values.")
    else:
        characters[name] = value
        save_characters()
        await ctx.send(f"Character {name}'s alignment updated to: {alignment_map[value]}")

# Command: Rank adjustment
@bot.command(name="characterrank")
async def adjust_alignment(ctx, name: str, adjustment: int):
    if name not in characters:
        await ctx.send(f"Character {name} does not exist!")
    else:
        new_value = characters[name] + adjustment
        new_value = max(0, min(100, new_value))  # Clamp between 0 and 100
        characters[name] = new_value
        save_characters()
        await ctx.send(f"Character {name}'s alignment adjusted to: {alignment_map[new_value]}")

# Command: Show alignment
@bot.command(name="characteralignment")
async def show_alignment(ctx, name: str):
    if name not in characters:
        await ctx.send(f"Character {name} does not exist!")
    else:
        value = characters[name]
        await ctx.send(f"Character {name}'s alignment is: {value} ({alignment_map[value]})")

# Run the bot
bot.run("MTMyMjQ4NzYxNTAzMDgyNTAyMQ.Gq7G_x.KBf2t7Ql4xtDzlayrYybo4yABjG_qAfZ-QLkXA")

