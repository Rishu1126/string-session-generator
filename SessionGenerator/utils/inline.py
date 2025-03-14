# YT : @ultroidofficial
# Copyright (c) 2023 WOODcraft
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="💓 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 💓", callback_data="gensession")],
        [
            InlineKeyboardButton(text="💘 𝗢𝗪𝗡𝗘𝗥 💘", url="https://t.me/Niksonfire"),
            InlineKeyboardButton(
                text="🥀𝗨𝗣𝗗𝗔𝗧𝗘🥀", url="https://t.me/dil_ke_alfaaaz"
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
