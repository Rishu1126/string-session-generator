# YT : @ultroidofficial
# Copyright (c) 2023 WOODcraft
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="💓 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 💓", callback_data="gensession")],
        [
            InlineKeyboardButton(text="💘 𝗢𝗪𝗡𝗘𝗥 💘", url="https://t.me/Abhi_rss"),
            InlineKeyboardButton(
                text="🥀𝗕𝗢𝗧𝗛𝗨𝗕 𝗡𝗘𝗧𝗪𝗢𝗥𝗞🥀", url="https://t.me/bot_hub_network"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="💥 𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗩𝟭 💥", callback_data="pyrogram1"),
            InlineKeyboardButton(text="🍁 𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗩𝟮 🍁", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="⚡ 𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 ⚡", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="🌜 𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻 🌛", callback_data="gensession")]]
)
