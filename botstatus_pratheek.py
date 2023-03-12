from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

api_id = '21886784'
api_hash = '82fd1b4d334c4b813572cb0b1fcc299d'
session_string = ''

app = Client(
    "iacuptime"
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string
)

TIME_ZONE = 'Asia/Kolkata'
BOT_LIST = '@Lena_MilizeBot, @roronoa_zoro_robot'
CHANNEL_OR_GROUP_ID = '-1001557054615'
MESSAGE_ID = 35
BOT_ADMIN_IDS = [837914403, 1189238402]


async def main_pratheek():
    async with app:
        while True:
            print("Checking...")
            xxx_pratheek = f"📊 | 𝗟𝗜𝗩𝗘 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦"
            for bot in BOT_LIST:
                try:
                    yyy_pratheek = await app.send_message(bot, "/start")
                    aaa = yyy_pratheek.id
                    await asyncio.sleep(10)
                    zzz_pratheek = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_pratheek:
                        bbb = ccc.id
                    if aaa == bbb:
                        xxx_pratheek += f"\n\n🤖  @{bot}\n        └ **Down** ❌"
                        for bot_admin_id in BOT_ADMIN_IDS:
                            try:
                                await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                            except Exception:
                                pass
                        await app.read_chat_history(bot)
                    else:
                        xxx_pratheek += f"\n\n🤖  @{bot}\n        └ **Alive** ✅"
                        await app.read_chat_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"%d %b %Y at %I:%M %p")
            xxx_pratheek += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n**♻️ Refreshes automatically - Powered By Pratheek**"
            await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_pratheek)
            print(f"Last checked on: {last_update}")
            await asyncio.sleep(6300)


app.run(main_pratheek())
