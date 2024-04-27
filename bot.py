import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
import os

TOKEN = os.getenv('TOKEN')

# bot = commands.Bot(command_prefix='=')
# scheduler = AsyncIOScheduler()

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @bot.command()
# async def schedule_message(ctx, time, *, message):
#     # Schedule the message
#     scheduler.add_job(send_scheduled_message, CronTrigger.from_crontab(time), args=(ctx.channel, message))

#     await ctx.send(f'Message scheduled for {time}: {message}')

# async def send_scheduled_message(channel, message):
#     await channel.send(message)

if __name__ == "__main__":
    # scheduler.start()
    # bot.run(TOKEN)
    print(f'token: {TOKEN}')