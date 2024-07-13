# Generate Session In Your Telegram premium @Opleech
# Copyright (c) 2023 WOODcraft
from pyrogram import filters
from pyrogram.types import Message

from SessionGenerator import Opleech
from SessionGenerator.utils import add_served_user, keyboard


@Opleech.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"😚 𝗛𝗘𝗬 𝗕𝗔𝗕𝗬 {message.from_user.first_name},\n\n🥀 𝗧𝗵𝗶𝘀 𝗜𝘀 {Opleech.mention},\n𝗔𝗻 𝗢𝗽𝗲𝗻 𝗦𝗼𝘂𝗿𝗰𝗲 𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 𝗕𝗼𝘁, 𝗪𝗿𝗶𝘁𝘁𝗲𝗻 𝗜𝗻 𝗣𝘆𝘁𝗵𝗼𝗻 ❤].",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
