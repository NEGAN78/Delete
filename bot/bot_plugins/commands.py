#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import asyncio
import time
import sys
import psutil

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from bot import LOGGER, Config


logger = LOGGER(__name__)


@Client.on_message(filters.command(["start"]) & filters.user(Config.AUTH_USERS))
async def start (bot, update):
    
    await update.reply_text("Bot Started..! And its Up and Running..!")


@Client.on_message(filters.private & filters.command(["stats"]) & filters.user(Config.AUTH_USERS))
async def stats(bot, update):


    msg = await bot.send_message(
        chat_id=update.chat.id,
        text="__Processing...__",
        parse_mode=enums.ParseMode.MARKDOWN
    )

    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(
        time.time() - Config.BOT_START_TIME))
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent

    ms_g = f"<b><u>Bot Status</b></u>\n" \
        f"<code>Uptime: {currentTime}</code>\n"\
        f"<code>CPU Usage: {cpu_usage}%</code>\n"\
        f"<code>RAM Usage: {ram_usage}%</code>\n\n" 
    await msg.edit_text(
        text=ms_g,
        parse_mode=enums.ParseMode.HTML
    )


@Client.on_message(filters.private & filters.command(["restart"]) & filters.user(Config.AUTH_USERS))
async def restart(bot, update):

    b = await bot.send_message(
        chat_id=update.chat.id,
        text="__Restarting.....__",
        parse_mode=enums.ParseMode.MARKDOWN
    )
    await asyncio.sleep(3)
    await b.delete()
    os.system("git pull")
    os.remove("logs.txt")
    os.execl(sys.executable, sys.executable, "-m", "bot")


@Client.on_message(filters.command(['logs']) & filters.user(Config.AUTH_USERS))
async def send_logs(_, m):
    await m.reply_document(
        "logs.txt",
        caption='Logs'
    )

