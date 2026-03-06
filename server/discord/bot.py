import discord

TOKEN = "PUT_DISCORD_TOKEN_HERE"

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.slash_command(description="Request a song")
async def request(ctx, song: str):
    await ctx.respond(f"Song request received: {song}")

@bot.slash_command(description="Now playing")
async def nowplaying(ctx):
    await ctx.respond("AutoDJ is currently playing music.")

bot.run(TOKEN)