import os
from dotenv import load_dotenv
from interactions import Client, Intents, listen, slash_command, SlashContext, check, is_owner

load_dotenv()

bot = Client(intents=Intents.DEFAULT)
# intents are what events we want to receive from discord, `DEFAULT` is usually fine

@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@slash_command(name="my_command", description="My first command :)")
async def my_command_function(ctx: SlashContext):
    await ctx.send("Hello World")


@slash_command(name="poop", description="poop command")
async def poop_function(ctx: SlashContext):
    await ctx.send("butt")


@slash_command(name="log", description="Log Anki for Today")
async def log_function(ctx: SlashContext):
    await ctx.send("log")
    # await ctx.member.add_roles(ctx.guild.get_role(1484234112590938153))


@slash_command(name="check", description="Check if someone did Anki")
async def check_function(ctx: SlashContext):
    await ctx.send("check")


token = os.getenv('TOKEN')
bot.start(token)