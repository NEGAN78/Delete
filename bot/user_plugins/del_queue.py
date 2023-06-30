#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import asyncio
import time

from datetime import datetime, timedelta

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from bot import Config, LOGGER
from bot.user import User
from bot.database.configsdb import get_config

logger = LOGGER(__name__)

TIME = {}

@Client.on_message(filters.chat(Config.CHATS), group=-1)
async def schedule_deleteion(bot: Client, update: Message):

    global TIME
  
    seconds = await get_config("DELETE_TIME", Config.DELETE_TIME)
    await asyncio.sleep(seconds)
    await update.delete()

    if Config.AUTO_PURGE:
        stored_time = TIME.get(update.chat.id, False)
        if not time:
            TIME[update.chat.id] = time.time()
            stored_time = time.time()

        if round(time.time() - stored_time) >= 15*60:
            TIME[update.chat.id] = time.time()
            async for msg in bot.get_chat_history(update.chat.id, limit=50):
                await bot_delete_msg(bot, msg)


@Client.on_message(filters.command(["purge"]) & filters.reply & filters.user(Config.AUTH_USERS))
async def purge_messages(bot: Client, update: Message):

    if bot.me.is_bot:
        return
    
    first_msg = update.reply_to_message_id
    last_msg = update.id
    
    async for msg in bot.get_chat_history(update.chat.id):
        if msg.id <= first_msg:
            break
        await bot_delete_msg(bot, msg)

    await update.reply(
        "Purged Successfully",
        True
    )


async def bot_delete_msg(bot: Client, update: Message):
    try:
        await update.delete()
    except Exception as e:
        logger.error(e)

