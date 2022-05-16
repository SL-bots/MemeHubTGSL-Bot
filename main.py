import os

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel

#Client
Client = Client(
    "Memehub Bot",
    bot_token= "5347727010:AAFfGwumkROYWgwkgL1FYcfmjeiZG1M_KT4",
    api_id= 8838171,
    api_hash= "0587408d4f7d9301f5295840b0f3b494",
)


START_STRING ="""
Hi {}, Welcome to  MemeHub Telegram 🇱🇰 Official Bot.


 Bot By [◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/Imgishan)
"""
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="👻 ʙᴀᴍᴄᴋ 👻",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', url="https://t.me/N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="hlp")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", url="https://t.me/share/url?url=%F0%9D%99%B7%F0%9D%9A%92.%20%F0%9D%99%B1%F0%9D%9A%98%F0%9D%9A%A2%F0%9D%9A%9C%20%F0%9D%9A%8A%F0%9D%9A%97%F0%9D%9A%8D%20%F0%9D%9A%90%F0%9D%9A%92%F0%9D%9A%9B%F0%9D%9A%95%F0%9D%9A%9C%20%F0%9D%9A%A0%F0%9D%9A%8E%20%F0%9D%9A%8A%F0%9D%9A%9B%F0%9D%9A%8E%20%F0%9D%9A%9D%F0%9D%9A%91%F0%9D%9A%8E%20%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%91%F0%9D%9A%9E%F0%9D%9A%8B%20%F0%9D%9A%92%F0%9D%9A%8F%20%F0%9D%9A%A2%F0%9D%9A%98%F0%9D%9A%9E%20%F0%9D%9A%91%F0%9D%9A%8A%F0%9D%9A%9F%F0%9D%9A%8E%20%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%9C%20%F0%9D%9A%9C%F0%9D%9A%8E%F0%9D%9A%97%F0%9D%9A%8D%20%F0%9D%9A%A2%F0%9D%9A%98%F0%9D%9A%9E%F0%9D%9A%9B%20%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%9C%20%F0%9D%9A%9D%F0%9D%9A%98%20%F0%9D%9A%98%F0%9D%9A%9E%F0%9D%9A%9B%20%F0%9D%9A%8B%F0%9D%9A%98%F0%9D%9A%9D%20%F0%9D%9A%8A%F0%9D%9A%97%F0%9D%9A%8D%20%F0%9D%9A%91%F0%9D%9A%8E%F0%9D%9A%95%F0%9D%9A%99%20%F0%9D%9A%9E%F0%9D%9A%9C.%0A%0A%F0%9D%99%BC%F0%9D%9A%8E%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%91%F0%9D%9A%9E%F0%9D%9A%8B%20%E0%B6%91%E0%B6%9A%E0%B7%9A%20%E0%B6%87%E0%B6%A9%E0%B7%8A%E0%B6%B8%E0%B7%92%E0%B6%B1%E0%B7%8A%20%E0%B6%B1%E0%B7%90%20%E0%B6%9A%E0%B7%92%E0%B6%BA%E0%B6%BD%20%E0%B6%AF%E0%B7%94%E0%B6%9A%E0%B7%99%E0%B6%B8%E0%B7%8A%E0%B6%AF%20%E0%B6%89%E0%B6%B1%E0%B7%8A%E0%B6%B1%E0%B7%9A%20%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%9C%20%E0%B6%9C%E0%B7%9C%E0%B6%A9%E0%B6%9C%E0%B7%90%E0%B7%84%E0%B7%92%E0%B6%BD%E0%B7%8F%20%E0%B6%92%E0%B7%80%E0%B7%8F%E0%B6%A7%20%E0%B6%9A%E0%B6%BB%E0%B6%9C%E0%B6%B1%E0%B7%8A%E0%B6%B1%20%E0%B6%AF%E0%B7%99%E0%B6%BA%E0%B6%9A%E0%B7%8A%20%E0%B6%B1%E0%B7%9A%E0%B6%AF%3F%20%E0%B6%B8%E0%B7%99%E0%B6%B1%E0%B7%8A%E0%B6%B1%20%E0%B7%80%E0%B7%92%E0%B7%83%E0%B6%AF%E0%B7%94%E0%B6%B8%20%E0%B6%94%E0%B6%BA%E0%B7%8F%E0%B6%9C%E0%B7%9A%20%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%9C%2F%F0%9D%9A%8F%F0%9D%9A%9E%F0%9D%9A%97%F0%9D%9A%97%F0%9D%9A%A2%20%F0%9D%9A%9F%F0%9D%9A%92%F0%9D%9A%8D%F0%9D%9A%8E%F0%9D%9A%98%F0%9D%9A%9C%20%E0%B6%94%E0%B6%9A%E0%B7%8A%E0%B6%9A%E0%B7%9C%E0%B6%B8%20%E0%B6%91%E0%B7%80%E0%B6%B1%E0%B7%8A%E0%B6%B1%20%E0%B6%85%E0%B6%B4%E0%B7%92%E0%B6%A7%20%E0%B6%85%E0%B6%B4%E0%B7%92%20%E0%B6%92%E0%B7%80%E0%B7%8F%20%E0%B6%AF%E0%B7%8F%E0%B6%B1%E0%B7%80%E0%B7%8F%20%E0%B6%85%E0%B6%B4%E0%B7%9A%20%F0%9D%9A%8C%F0%9D%9A%91%F0%9D%9A%8A%F0%9D%9A%97%F0%9D%9A%97%F0%9D%9A%8E%F0%9D%9A%95%20%E0%B6%91%E0%B6%9A%E0%B7%9A%20%E0%B6%92%20%E0%B6%85%E0%B6%AD%E0%B6%BB%E0%B7%92%E0%B6%B1%E0%B7%8A%20%E0%B7%84%E0%B7%90%E0%B6%B8%E0%B6%AF%E0%B7%8F%E0%B6%B8%20%F0%9D%9A%96%F0%9D%9A%8E%F0%9D%9A%96%F0%9D%9A%9C%20%E0%B6%AF%E0%B7%8F%E0%B6%B1%20%E0%B6%85%E0%B6%BA%E0%B6%A7%20%E0%B6%85%E0%B6%B4%E0%B7%9A%20%F0%9D%9A%8C%F0%9D%9A%91%F0%9D%9A%8A%F0%9D%9A%97%F0%9D%9A%97%F0%9D%9A%8E%F0%9D%9A%95%20%E0%B6%91%E0%B6%9A%E0%B7%9A%20%E0%B6%87%E0%B6%A9%E0%B7%8A%E0%B6%B8%E0%B7%92%E0%B6%B1%E0%B7%8A%20%E0%B7%80%E0%B7%99%E0%B6%B1%E0%B7%8A%E0%B6%B1%E0%B6%AD%E0%B7%8A%20%E0%B6%B4%E0%B7%94%E0%B7%85%E0%B7%94%E0%B7%80%E0%B6%B1%E0%B7%8A%20%E0%B6%85%E0%B6%AF%E0%B6%B8%20%E0%B6%91%E0%B6%9A%E0%B7%8A%E0%B7%80%E0%B6%B1%E0%B7%8A%E0%B6%B1%20%E0%B6%85%E0%B6%B4%20%E0%B7%83%E0%B6%B8%E0%B6%9C%20%F0%9F%A4%9E%E2%9C%8C%EF%B8%8F%F0%9F%A4%9F%F0%9F%A4%98%F0%9F%91%8A%0A%0A%0A%F0%9D%99%B1%F0%9D%9A%98%F0%9D%9A%9D%20%3D%20%40MemehubTgSl_Bot")
                 ]]
                  )
                  
HELP_STRING = "Meme Tiye nam dapam Mekata😒😂. Adminlata Msg Daanna One Nam ekat Mekata dapam 😒😂"

CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖒𝖘𝖊", callback_data="cloc")
                 ]]
                 )

                  
WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>Type your query here..\nI'll respond to your query as earliest</code> 😉\n\nуσυ ωαииα тσ киσω αвσυт мє😌? яєα∂ вєℓσω\n\nαвσυт @Gishankrishka:-\n •му иαмє:- Gishan Krishka \n •му αgє:- υикиσωи🌝\n •¢σмρυтєя ℓαиgυαgє:- ωєв ∂єνєℓσρмєит(ℓєαяиιиg), ρутнσи мσяє ѕσσи😁\n•¢нє¢к [About ༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒](https://t.me/Gishankrishka_Info_bot) fσя мσяє\n\nPlz Don't Send Stickers 🥲\nReason :- [This](https://t.me/ultchat/19589)"
USER_DETAILS = "<b>FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_MED_ATT = "<b>Photo from:</b> {} \n<b>Name:</b> {}"


@Client.on_message(filters.command(["start", "start@MemeHubTgSl_Bot"]))
async def startprivate(bot, message):
    USER = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('USER', url=f"https://t.me/{message.from_user.username}")
                 ]]
                  )
    info = await bot.get_users(user_ids=message.from_user.id)
    USER_DETAILS = f"[{message.from_user.mention}](tg://user?id={message.from_user.id}) [`{message.from_user.id}`] Started Ur Bot.\n\n**First Name: `{info.first_name}`**\n**LastName: `{info.last_name}`**\n**Scam: `{info.is_scam}`**\n**Restricted: `{info.is_restricted}`**\n**Status:`{info.status}`**\n**Dc Id: `{info.dc_id}`**"
    await bot.send_message(-1001759991131, text=USER_DETAILS, reply_markup=USER)
    file_id = "CAADBQADVwYAAhCWAVRcksqpPVEWHAI"
    await bot.send_sticker(message.chat.id, file_id)
    text = f"Hi {message.from_user.mention}, Welcome to  MemeHub Telegram 🇱🇰 Official Bot\n\nDevs\n\n[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/Imgishan)\n[unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™](t.me/UnknownB_o_y)"
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

@Client.on_message(filters.command(["help", "help@MemeHubTgSl_Bot"]))
async def startprivate(bot, message):
    await message.reply_text(
        text=HELP_STRING,
        reply_markup=CLOSE_BUTTON,
        disable_web_page_preview=True
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
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> {info.first_name}\n\n{message.text}**"
    )
    await bot.send_message(
        chat_id=-1001759991131,
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> {message.from_user.mention}\n\n{message.text}**"
    )


@Client.on_message(filters.sticker & filters.private) 
async def pm_media(bot, message):
    file_id = "CAADBQADEwUAAmjn4Vez7jrL1Cu2AAEC"
    await bot.send_sticker(message.chat.id, file_id) 

@Client.on_message(filters.media & filters.private)
async def pm_media(bot, message):
    if message.from_user.id == 1884885842:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await message.forward(1884885842)
    
    await bot.send_message(1884885842 ,f"Photo from:</b> {reference_id} **\n**Name:</b> {info.first_name}")
    await message.forward(-1001210985373)
    await message.forward(-1001759991131)
    await bot.send_message(
        chat_id=-1001759991131,
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> {message.from_user.mention}\n\n{message.text}**\n\n@admin"
    )
    reply_markup = BACK_BUTTONS
    text = "Ur Photo Sent To [MemeHub Telegram 🇱🇰](https://t.me/memehubTGSL)"
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
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
    elif update.data == "cloc":
         await update.message.delete()
         
@Client.on_message(filters.user(1884885842) & filters.sticker)
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
            message_id=message.message_id
        )          
         
           

print(f"""
Im Alive
""")
Client.run()
