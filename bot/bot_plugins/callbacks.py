#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from bot.config import Config
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, enums



@Client.on_callback_query()
async def callbacks(bot: Client, update: CallbackQuery):
    
    await update.answer("")
