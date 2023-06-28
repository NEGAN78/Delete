#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import asyncio
from pyrogram import compose
from bot.bot import Bot
from bot.user import User

async def main():
    clients = [
        Bot(),
        User()
    ]
    
    await compose(clients)

asyncio.run(main())
