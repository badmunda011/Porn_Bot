import asyncio
import importlib
from pyrogram import idle
from Porn import Porn
from Porn.bad import ALL_MODULES

 

loop = asyncio.get_event_loop()


async def bad_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Porn.bad." + all_module)
    print("»»»» ʜᴇʀᴏᴋᴏ ʀᴏʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    loop.run_until_complete(bad_boot())
