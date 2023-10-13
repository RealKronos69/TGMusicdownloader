# © KronoS
# https://fakekronos

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Song.database.access_db import db
import shutil
import psutil

#-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*#
def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

#-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*#

async def start(bot, update):
        await update.reply_text(
            text=f"Jᴀɪ Sʜʀᴇᴇ Rᴀᴍ, {update.from_user.mention}\n\n➻ ᴛʜɪs ɪs,<b>TGᴍᴜꜱɪᴄ Dᴏᴡɴʟᴏᴀᴅᴇʀ</b>\n\n๏ ꜰᴀꜱᴛᴇꜱᴛ ᴍᴜsɪᴄ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ  ʙᴏᴛ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ...\n๏ ꜱᴇɴᴅ ᴍᴇ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ꜱᴇᴇ ᴍᴀɢɪᴄ...ᴏʀ ʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜꜱɪᴄ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ꜱᴇᴀʀᴄʜ ꜱᴏɴɢ ʙᴜᴛᴛᴏɴ.\n──────────────────\n<b>Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs</b> : ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ᴍɪxᴄʟᴏᴜᴅ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                            [[
                                InlineKeyboardButton(
                                    "˹ꜱᴜᴘᴘᴏʀᴛ˼", url="https://t.me/Spartans_Mainchat"),
                                InlineKeyboardButton(
                                    "˹ᴅᴇᴠᴇʟᴏᴘᴇʀ˼", url="https://t.me/fakekronos")
                                ]]
                            ),
            disable_web_page_preview=True,
            parse_mode="html")



async def helper(bot, update):
        await update.reply_text(
            text=f"Send Me The Song Link\n\nDownload The Music\n\nSend as Music File Back to You\n\nNot all Music Files Can be Downloaded, So Please be Patient\n\nFeel Free to Conatct me If you Spot any Bugs @FakeKronoS",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                            [[
                                InlineKeyboardButton(
                                    "˹ꜱᴜᴘᴘᴏʀᴛ˼", url="https://t.me/Spartans_mainchat"),
                                InlineKeyboardButton(
                                    "˹ᴅᴇᴠᴇʟᴏᴘᴇʀ˼", url="https://t.me/fakekronos")
                                ]]
                            ),
            disable_web_page_preview=True,
            parse_mode="html")


async def status(bot, update):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await update.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )

