import discord
import redis
from server.config import REDIS_HOST, REDIS_PORT

TOKEN = "PUT_DISCORD_TOKEN_HERE"

r = redis.Redis(host=REDIS_HOST,port=REDIS_PORT,decode_responses=True)

bot = discord.Bot()

@bot.slash_command(description="Request a song")
async def request(ctx, path: str):

    r.rpush("song_requests",path)

    await ctx.respond(f"Added to queue: {path}")

@bot.slash_command(description="View queue")
async def queue(ctx):

    q = r.lrange("song_requests",0,-1)

    if not q:
        await ctx.respond("Queue empty")
    else:
        await ctx.respond("\n".join(q))

bot.run(TOKEN)