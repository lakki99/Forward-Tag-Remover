import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from config import BOT_TOKEN, API_ID, API_HASH, OWNER
from translation import TEXT, INLINE

app = Client("cleaner_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)


@app.on_message(filters.command("start"))
async def start(client: Client, msg: Message):
    await msg.reply_text(
        TEXT.START.format(msg.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=INLINE.START_BTN
    )

    # Send owner alert
    try:
        await client.send_message(
            OWNER.ID,
            f"🚀 Bot started by [{msg.from_user.first_name}](tg://user?id={msg.from_user.id})"
        )
    except Exception as e:
        print("Owner alert failed:", e)


@app.on_message(
    (filters.channel & filters.forwarded)
    | (filters.private & filters.incoming)
    | (filters.group & filters.forwarded)
)
async def remove(client: Client, msg: Message):
    try:
        if msg.media and not msg.video_note and not msg.sticker:
            await msg.copy(msg.chat.id, caption=msg.caption or None)
        else:
            await msg.copy(msg.chat.id)
        await msg.delete()
    except FloodWait as e:
        await asyncio.sleep(e.value)


if __name__ == "__main__":
    print("Bot is running...")
    app.run()
