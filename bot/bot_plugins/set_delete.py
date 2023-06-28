#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import Client, filters,enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from bot import Config
from bot.database.configsdb import update_config


@Client.on_message(filters.command("setdelete") & filters.user(Config.AUTH_USERS), group=-1)
async def setdelete(bot, update: Message):
    await update.reply_text(
        text="**Select the mode of delete button:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("1 hr", callback_data="setdelete_3600"),
                    InlineKeyboardButton("30 min", callback_data="setdelete_1800"),
                ],
                [
                    InlineKeyboardButton("25 min", callback_data="setdelete_1500"),
                    InlineKeyboardButton("20 min", callback_data="setdelete_1200"),
                ],
                [
                    InlineKeyboardButton("15 min", callback_data="setdelete_900"),
                    InlineKeyboardButton("12 min", callback_data="setdelete_720"),
                ],
                [
                    InlineKeyboardButton("10 min", callback_data="setdelete_600"),
                    InlineKeyboardButton("5 min", callback_data="setdelete_300"),
                ],
                [
                    InlineKeyboardButton("1 min", callback_data="setdelete_60"),
                    InlineKeyboardButton("20 sec", callback_data="setdelete_20"),
                ],
            ]
        ),
        quote=True,
        parse_mode=enums.ParseMode.MARKDOWN
    )


@Client.on_callback_query(filters.regex(r"^setdelete_\d+$") & filters.user(Config.AUTH_USERS), -2)
async def setdelete_callback(_, update: CallbackQuery):

    await update.answer()

    data = update.data.split("_")[1]
    await update.message.edit_text(
        text=f"**Delete button will be automatically deleted after {data} seconds.**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🗑 Close", callback_data="close_data")
                ]
            ]
        ),
        parse_mode=enums.ParseMode.MARKDOWN
    )
    # from info import DELETE_TIME
    # DELETE_TIME = int(data)

    await update_config({"_id": "DELETE_TIME", "value": int(data)})
    return



