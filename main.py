import re
import uuid
import socket
import platform
import os
import random
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from decorators import humanbytes
from config import *

#--------------------------------------------------Db-------------------------------------------------#

class Database:
    def __init__(self, url, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(url)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, user_id):
        return dict(id=user_id)

    async def add_user(self, user_id):
        user = self.new_user(user_id)
        await self.col.insert_one(user)

    async def is_user_exist(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        
#------------------------------Db End---------------------------------------------------------#       
        

Client = Client(
    "Memehub Bot",
    bot_token= BOT_TOKEN,
    api_id= API_ID,
    api_hash= API_HASH,
)

#--------------------------------------configs-------------------------------------------#
start_menu = ReplyKeyboardMarkup(
      [
            ["🤴 OWNER 🤴"],
            ["💻 Bot Devs 💻", "👮‍♂️ MemeHub Admins 👮‍♂️"],
            ["📊 Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )

next_1 = ReplyKeyboardMarkup(
      [
            ["📊 Statistics"],
            ["BACK 🔙"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )

back = ReplyKeyboardMarkup(
      [
            ["🤴 OWNER 🤴"],
            ["💻 Bot Devs 💻", "👮‍♂️ MemeHub Admins 👮‍♂️"],
            ["📊 Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )
      
password = "AgWKo1cHWmcfrkWt"
DATABASE_URL=MONGO_URI
db = Database(DATABASE_URL, "Memehub_bot")     
#-------------------------------start---------------------------------------#

@Client.on_message(filters.command("start"))
async def start(bot, message):
    if not await db.is_user_exist(message.from_user.id):
         await db.add_user(message.from_user.id)
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return    
    file_id = "CAADBQADVwYAAhCWAVRcksqpPVEWHAI"
    await bot.send_sticker(message.chat.id, file_id, reply_markup=start_menu)
    text = f"Hi {message.from_user.mention}, Welcome to  MemeHub Telegram 🇱🇰 Official Bot"
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
    if not await db.is_user_exist(message.from_user.id):
         USER = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('USER', user_id=f"tg://user?id={message.from_user.id}")
                 ]]
                  )
         info = await bot.get_users(user_ids=message.from_user.id)
         USER_DETAILS = f"#NEW_USER\n\n[{message.from_user.mention}](tg://user?id={message.from_user.id}) [`{message.from_user.id}`] Started Ur Bot.\n\n**First Name: `{info.first_name}`**\n**LastName: `{info.last_name}`**\n**Scam: `{info.is_scam}`**\n**Restricted: `{info.is_restricted}`**\n**Status:`{info.status}`**\n**Dc Id: `{info.dc_id}`**"
         await bot.send_message(-1001759991131, text=USER_DETAILS, reply_markup=USER)
    
           



#-------------------------------------------menu Regex-----------------------------------------#         
  
@Client.on_message(filters.regex(pattern="🤴 OWNER 🤴"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(OWNER_STICKER),reply_markup=OWNER_BTN)

@Client.on_message(filters.regex(pattern="📊 Statistics"))   
async def startprivate(bot, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(bot.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    countb = await db.total_users_count()
    countb = await db.total_users_count()
    count = await bot.get_chat_members_count(-1001210985373)
    counta = await bot.get_chat_members_count(-1001759991131)
    text=f"""**Bot Advanced Statistics 📊**
** 👥Members Counts in Our channel:**

◉──────────────────────────────────◉
 **MemeHub Telegram 🇱🇰  Users** : `{count}`
 **⚜️MemeHub Family⚜️ (Admins)**   : `{counta}`
 **ᴍᴇᴍᴇʜᴜʙ ᴏᴍғғɪᴄɪᴀʟ ʙᴏᴍᴛ 『🇱🇰』 Users** : `{countb}`
◉──────────────────────────────────◉
🖥 **System Information**

**PlatForm :** `{splatform}`
**PlatForm - Release :** `{platform_release}`
**PlatFork - Version :** `{platform_version}`
**Architecture :** `{architecture}`
**Hostname :** `{hostname}`
**IP :** `{ip_address}`
**Mac :** `{mac_address}`
**Processor :** `{processor}`
**Ram : ** `{ram}`
**CPU :** `{cpu_len}`
**CPU FREQ :** `{cpu_freq}`
**DISK :** `{disk}`
◉──────────────────────────────────◉
 """
 
    await bot.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await bot.send_message(message.chat.id, text=text)

@Client.on_message(filters.regex(pattern="💻 Bot Devs 💻"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(DEV_STICKER),reply_markup=DEV_BTN)

@Client.on_message(filters.regex(pattern="👮‍♂️ MemeHub Admins 👮‍♂️"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(ADMIN_STICKER),reply_markup=ADMIN_BTN)
    
@Client.on_message(filters.regex(pattern="NEXT 🔜"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='NEXT 🔜',reply_markup=next_1)
        
@Client.on_message(filters.regex(pattern="BACK 🔙"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='BACK 🔙',reply_markup=start_menu)

#-----------------------------------------update--------------------------------------------------#
@Client.on_message(filters.command("upd"))
async def on_off_antiarab(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    msg=message.reply_to_message
    f= message.text
    s=f.replace('/upd ' ,'')
    photo=s.replace('%20', ' ')
    caption=f"""
 #UPDATE 

**Update Available**
`
    ╔╦╗──╔╗──╔╗
    ║║╠═╦╝╠═╗║╚╦═╗
    ║║║╬║╬║╬╚╣╔╣╩╣
    ╚═╣╔╩═╩══╩═╩═╝
    ──╚╝`
    """
    await bot.send_photo(message.chat.id,photo=photo, caption=caption, reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('♻️ Updatate ♻️', callback_data="upd")
                 ]]
                  )
    ) 

@Client.on_message(filters.command("upd"))
async def on_off_antiarab(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    f= message.text
    s=f.replace('/upd ' ,'')
    UPDATE_N=s.replace('%20', ' ')
    text = f"""
#UPDATE

╭━╮╭━╮╱╱╱╱╱╭╮╱╱╱╱╭╮
┃┃╰╯┃┃╱╱╱╱╱┃┃╱╱╱╱┃┃
┃╭╮╭╮┣━━┳╮╭┫╰━┳╮╭┫╰━╮
┃┃┃┃┃┃┃━┫╰╯┃╭╮┃┃┃┃╭╮┃
┃┃┃┃┃┃┃━┫┃┃┃┃┃┃╰╯┃╰╯┃
╰╯╰╯╰┻━━┻┻┻┻╯╰┻━━┻━━╯

**Update Available**

◇─────Update Note─────◇
        
{UPDATE_N}
    """
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('♻️ Updatate ♻️', callback_data="upd")
                 ]]
                  )
    )

#----------------------------------------------main Cmds---------------------------------------------#

@Client.on_message(filters.private &filters.command("send"))
async def status(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    msg=message.reply_to_message
    f= message.text
    s=f.replace('/send ' ,'')
    fid=s.replace('%20', ' ')
    await send_msg(user_id=fid, message=msg)
    await message.delete()
    await bot.send_message(message.chat.id, text=f"Ur Msg Sent To [User](tg://user?id={fid})", reply_markup=CLOSE_BUTTON)

@Client.on_message(filters.private &filters.command("admincast"))
async def status(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    msg=message.reply_to_message
    await send_msg(user_id=1884885842, message=msg)
    await send_msg(user_id=5115331277, message=msg)
    await send_msg(user_id=5025877489, message=msg)
    await send_msg(user_id=1202064253, message=msg)
    await send_msg(user_id=1120271521, message=msg)
    
@Client.on_message(filters.command(["help", "help@MemeHubTgSl_Bot"]))
async def help(bot, message):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    await bot.send_sticker(message.chat.id, random.choice(HELP_STICKER), reply_markup=start_menu)
    await message.reply_text(
        text=HELP_STRING,
        reply_markup=CLOSE_BUTTON,
        disable_web_page_preview=True
         )

@Client.on_message(filters.private & filters.command("status"), group=5)
async def status(bot, update):
    if update.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    if not await db.is_user_exist(update.from_user.id):
         await db.add_user(update.from_user.id)
         
    await bot.send_sticker(update.chat.id, random.choice(STAT_STICKER))
    total_users = await db.total_users_count()
    text = "**Bot Advanced Statistics 📊**\n"
    text += f"\n**Total Users:** `{total_users}`"

    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )

@Client.on_message(
    filters.private &
    filters.command("broadcast") &
    filters.reply
)
async def broadcast(bot, update, broadcast_ids={}):
    if update.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    
    all_users = await db.get_all_users()
    broadcast_msg= update.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break

    out = await update.reply_text(text=f"Broadcast Started! You will be notified with log file when all the users are notified.")
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total = total_users, current = done, failed = failed, success = success)
        
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id = int(user['id']), message = broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(dict(current = done, failed = failed, success = success))
        
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    
    completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
    await asyncio.sleep(3)
    await out.delete()

    if failed == 0:
        await update.reply_text(text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.", quote=True)
    else:
        await update.reply_document(document='broadcast.txt', caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
        
    os.remove('broadcast.txt') 

                       
print("cmds.py Working....")  

#------------------------------------------------Pm----------------------------------------------------#

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == 1884885842:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=1884885842,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text)
    )
    

@Client.on_message(filters.private & filters.sticker)
async def pm_media(bot, message):
    if message.from_user.id == 1884885842:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=1884885842,
        from_chat_id=message.chat.id,
        message_id=message.id
    )
    await bot.send_message(1884885842, text=PM_TXT_ATTS.format(reference_id, info.first_name))
    
@Client.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == 1884885842:
        await replay_media(bot, message)
        return
    await message.reply_text(text="Ur Photo Sent To [MemeHub Telegram 🇱🇰 ](https://t.me/memehubTGSL) Admins", reply_markup=CLOSE_BUTTON)
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=1884885842,       
        from_chat_id=message.chat.id,
        message_id=message.id,
        caption=PM_MED_ATT.format(reference_id, message.from_user.mention)
    )
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=-1001759991131,
        from_chat_id=message.chat.id,
        message_id=message.id,
        caption=PM_MED_ATT.format(reference_id, message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton("✅ᴀᴄᴄᴇᴘᴛ", callback_data="acce"),
                 InlineKeyboardButton("❌ʀᴇᴊᴇᴄᴛ", callback_data="cloc")
                 ]]
                 )
   )


@Client.on_message(filters.text)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )


@Client.on_message(filters.media)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.id
        )
@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == 1884885842:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=1884885842,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text)
    )


@Client.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == 1884885842:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=1884885842,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption=PM_MED_ATT.format(reference_id, info.first_name)
    )


@Client.on_message(filters.text)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )


@Client.on_message(filters.media)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.id
        )
print("Pm Working....")


#------------------------------------------------Callback-------------------------------------------#
@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="♻️Adding Soon.....",
        )
    elif update.data == "bak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʙᴀᴍᴄᴋ 👻",
         )
    elif update.data == "bak":
         await update.message.delete()
         await bot.delete_message(update.chat.id, update.message.id)
    elif update.data == "hlp":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʜᴇᴍʟᴘ 👻",
         )
    elif update.data == "cloce":
         await update.message.delete()
    elif update.data == "ref": 
        await update.answer(
             text="♻️Reloading.....♻️",
        ) 
    elif update.data == "cloc":
         await update.message.delete()
         rid=update.message.caption.split()[2]
         await bot.send_message(rid, text=f"☠️ **Ur Message Rejected By{update.from_user.mention}** ☠️")
    elif update.data == "upd":
        await update.message.edit_text("Updating....")
        await update.answer(
             text="♻️ Updatating Please Wait ♻️",
        )
        await update.message.edit("**♻️ Updatating ♻️ -**") 
        await update.message.edit("**♻️ Updatating ♻️ \**") 
        await update.message.edit("**♻️ Updatating ♻️ |**")
        await update.message.edit("**♻️ Updatating ♻️ /**")
        await update.message.edit("**♻️ Updatating ♻️ -**") 
        await update.message.edit("**♻️ Updatating ♻️ \**") 
        await update.message.edit("**♻️ Updatating ♻️ |**")
        await update.message.edit("**♻️ Updatating ♻️ /**")
        await update.message.edit("**♻️ Updatating ♻️ -**") 
        await update.message.edit("**♻️ Updatating ♻️ \**") 
        await update.message.edit("**♻️ Updatating ♻️ |**")
        await update.message.edit("**♻️ Updatating ♻️ /**")
        await update.message.edit("**♻️ Updatating ♻️ -**") 
        await update.message.edit("**♻️ Updatating ♻️ \**") 
        await update.message.edit("**♻️ Updatating ♻️ |**")
        await update.message.edit("**♻️ Updatating ♻️ /**")
        await update.message.edit("**♻️ Updatating ♻️ -**") 
        await update.message.edit("**♻️ Updatating ♻️ \**") 
        await update.message.edit("**♻️ Updatating ♻️ |**")
        await update.message.edit("**♻️ Updatating ♻️ /**")
        await update.message.edit("**♻️ Updatating ♻️ -**") 
        await update.message.edit("**♻️ Updatating ♻️ \**") 
        await update.answer(
             text="♻️ Updated ♻️",
        )
        await update.message.edit(text="**♻️----Updated----♻️**", reply_markup=CLOSE_BUTTON)
    elif update.data == "acce":
        info = await bot.get_users(user_ids=update.message.from_user.id)
        reference_id = int(update.message.chat.id)
        await bot.copy_message(
        chat_id=-1001210985373,
        from_chat_id=-1001759991131,
        message_id=update.message.id
    )   
        await update.answer(
             text="✅ᴍᴇssᴀɢᴇ ᴀᴄᴄᴇᴘᴛᴇᴅ",
        ) 
        await update.message.delete() 
    
#--------------------------------------------------Inline------------------------------------------------#

@Client.on_inline_query()
async def answer(client, inline_query):
   if inline_query.query=='share':
        await inline_query.answer(
            results=[
                InlineQueryResultVideo(
                    title="Share Karapam",
                    video_url="https://telegra.ph/file/d58df8b002dfba939c9a8.mp4",
                    thumb_url="https://telegra.ph/file/7c8846dcae3767b15e3c0.jpg",
                    caption="""
𝙷𝚒. 𝙱𝚘𝚢𝚜 𝚊𝚗𝚍 𝚐𝚒𝚛𝚕𝚜 𝚠𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚖𝚎𝚖𝚎𝚑𝚞𝚋 𝚒𝚏 𝚢𝚘𝚞 𝚑𝚊𝚟𝚎 𝚖𝚎𝚖𝚎𝚜 𝚜𝚎𝚗𝚍 𝚢𝚘𝚞𝚛 𝚖𝚎𝚖𝚎𝚜 𝚝𝚘 𝚘𝚞𝚛 𝚋𝚘𝚝 𝚊𝚗𝚍 𝚑𝚎𝚕𝚙 𝚞𝚜.
𝙼𝚎𝚖𝚎𝚑𝚞𝚋 එකේ ඇඩ්මින් නැ කියල දුකෙම්ද ඉන්නේ 𝚖𝚎𝚖𝚎𝚜 ගොඩගැහිලා ඒවාට කරගන්න දෙයක් නේද? මෙන්න විසදුම ඔයාගේ 𝚖𝚎𝚖𝚎𝚜/𝚏𝚞𝚗𝚗𝚢 𝚟𝚒𝚍𝚎𝚘𝚜 ඔක්කොම එවන්න අපිට අපි ඒවා දානවා අපේ 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 එකේ ඒ අතරින් හැමදාම 𝚖𝚎𝚖𝚜 දාන අයට අපේ 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 එකේ ඇඩ්මින් වෙන්නත් පුළුවන් අදම එක්වන්න අප සමග 🤞✌️🤟🤘👊
𝙱𝚘𝚝 = @MemehubTgSl_Bot
""",
                    reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton('🐞 Report Bugs 🐞', user_id="1884885842")
                 ],
                 [
                 InlineKeyboardButton('ᴍᴇᴍᴇʜᴜʙ ᴏᴍғғɪᴄɪᴀʟ ʙᴏᴍᴛ 『🇱🇰』', user_id="@MemeHubTgSl_Bot")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", switch_inline_query="share")
                 ]])
                    
                        
                     
            ),
            ],
            cache_time=1
        ) 
        

print(" Deployed Successfully !")        
Client.run()
