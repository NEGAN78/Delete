#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import Client, __version__, enums

from bot import Config, LOGGER

class User(Client):
    def __init__(self):
        super().__init__(
            "UserBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            plugins={
                "root": "bot/user_plugins",
            },
            workers=1500,
            session_string=Config.SESSION_STRING,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        self.me = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"User @{self.me.username}  started! "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("User stopped. Bye.")

