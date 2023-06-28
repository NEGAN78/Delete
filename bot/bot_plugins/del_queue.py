#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import asyncio

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from bot import Config, LOGGER
from bot.bot import Bot
from bot.database.configsdb import get_config

logger = LOGGER(__name__)


@Client.on_message(filters.chat(Config.CHATS), group=-1)
async def delll(bot: Client, update: Message):
    
    seconds = await get_config("DELETE_TIME", Config.DELETE_TIME)
    await asyncio.sleep(seconds)
    await update.delete()
    
