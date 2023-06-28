#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG
import logging

from pyrogram import Client, enums, __version__
from pyropatch import listen, flood_handler

from bot import LOGGER, Config

logging.getLogger("pyrogram").setLevel(logging.ERROR)
# logging.getLogger("apscheduler").setLevel(logging.ERROR)
# logging.getLogger("apscheduler.executors").setLevel(logging.CRITICAL)


class Bot(Client):

    def __init__(self):
        super().__init__(
            "bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            plugins={
                "root": "bot/bot_plugins"
            },
            workers=600,
            bot_token=Config.BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"Bot @{usr_bot_me.username}  started! "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

