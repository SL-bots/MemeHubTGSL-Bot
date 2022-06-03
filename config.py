import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Vars
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1884885842 5115331277 5025877489 1202064253 1120271521").split())
MONGO_URI = os.getenv("MONGO_URI")
MAIN_CHANNEL = int(os.environ.get("MAIN_CHANNEL", "-1001618208549"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001618208549"))
PRIVATE_LOG = int(os.environ.get("PRIVATE_LOG", "-1001660993748"))
force_subchannel = os.getenv("FSUB", "memehubtgsl")
OWNER_ID = int(os.environ.get("OWNER_ID", "1884885842"))
#Strings 
WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>Type your query here..\nI'll respond to your query as earliest</code> 😉\n\nуσυ ωαииα тσ киσω αвσυт мє😌? яєα∂ вєℓσω\n\nαвσυт @Gishankrishka:-\n •му иαмє:- Gishan Krishka \n •му αgє:- υикиσωи🌝\n •¢σмρυтєя ℓαиgυαgє:- ωєв ∂єνєℓσρмєит(ℓєαяиιиg), ρутнσи мσяє ѕσσи😁\n•¢нє¢к [About ༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒](https://t.me/Gishankrishka_Info_bot) fσя мσяє\n\nPlz Don't Send Stickers 🥲\nReason :- [This](https://t.me/ultchat/19589)"
USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
USER_DETAILS = "<b>FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
FORCESUB_TEXT = "**❌ Access Denied ❌**\n\nMemehub eke nathuva Mokatada yako Botva Start Kare kkk😒😒\n♻️Join and Try Again.♻️"
HELP_STRING = "Meme Tiye nam dapam Mekata😒😂. Adminlata Msg Daanna One Nam ekat Mekata dapam 😒😂"
START_STRING ="""
Hi {}, Welcome to  MemeHub Telegram 🇱🇰 Official Bot.
 Bot By [◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/Imgishan)
"""


#Inline Btn
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here - MemeHub Telegram 🇱🇰', url=f"https://t.me/+78jdOfCNSdFhMDM1")
                 ],
                 [
                 InlineKeyboardButton('🐞 ʀᴘᴏʀᴛ ʙᴜɢs 🐞', user_id=f"@Imgishan")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )
                  
CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖒𝖘𝖊", callback_data="cloce")
                 ]]
                 )
                                                    
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="👻 ʙᴀᴍᴄᴋ 👻",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="hlp"),
                 InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍄", url="https://github.com/TeamAlphaTg/MemehubtgSl_Bot")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", switch_inline_query="share"),
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ᴄʜɴʟ ➕", switch_inline_query="cshare")
                 ]]
                  )

ADMIN_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Nirmal Abeysinghe', user_id="N_Abeysinghe_2001")
                 ],
                 [                 
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒ ', user_id="ImGishan")
                 ],
                 [                 
                 InlineKeyboardButton('unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="UnknownB_o_y")
                 ],
                 [                 
                 InlineKeyboardButton('Navidu Nimsara', user_id="Navidu_Nimsara")
                 ],
                 [                 
                 InlineKeyboardButton('DarkLucifer 么 ™', user_id="Dark_Iucifer")
                 ],
                 [                 
                 InlineKeyboardButton('🌀*✩.𝗛𝗜𝗥𝗨.✩*🌀', user_id="hiru_malsh_2002")
                 ],
                 [
                 InlineKeyboardButton('𝙃𝙊𝙍𝘼 𝙋𝙐𝙎𝘼 ᖇḁͦj̥ͦḁͦṗȧƙకꫝꪖ', user_id="hora_pusa")
                 ],
                 [                 
                 InlineKeyboardButton('║♔ Ꭲ ᕼ ᗩ ᖇ ᑌ ᑎ_ _ᗰ Ꮖ Ꭲ ᕼ ᔑ ᗩ ᖇ ᗩ ❥⃟♔║', user_id="XXXTENTACION_LOVER")
                 ],
                 [                 
                 InlineKeyboardButton('Sahiru Keshan', user_id="Sahiru_2007")
                 ],
                 [                 
                 InlineKeyboardButton('𝙈𝙧.𝙎𝙖𝙩𝙝𝙖𝙣', user_id="Sathan_OP")
                 ],
                 [
                 InlineKeyboardButton('⚜️ K.Malith Punsara ⚜️', user_id="kmp32913291")
                 ],
                 [                 
                 InlineKeyboardButton('ගින්නෙ ඉන්න චීස් කෑල්ල', url="tg://user?id=1344811260")
                 ],
                 [                 
                 InlineKeyboardButton('ŦħȺɍᵾꝁ ɌɇnᵾɉȺ', user_id="ImTharuk")
                 ],
                 [                 
                 InlineKeyboardButton('𝐖ᏋᏒᏋ🆆🅾️🅻🅵', user_id="w_wolflk2")
                 ],
                 [
                 InlineKeyboardButton('𝙏𝙝𝙚𝙣𝙪𝙡𝙖⁹⁹⁹ ', user_id="Th4nula999")
                 ],
                 [                 
                 InlineKeyboardButton('☠️𝘋𝘳.𝘚𝘵𝘳𝘰𝘮𝘦☠️', user_id="Dr_Strome")
                 ],
                 [                 
                 InlineKeyboardButton('Pasindu Maleesha', user_id="PASINDU_M_WICK")
                 ],
                 [                 
                 InlineKeyboardButton('ixAAr Modderϟ➊ ', user_id="Mr_ixAAr")
                 ],
                 [
                 InlineKeyboardButton('𝙕𝙚𝙩𝙖', user_id="sthisara")
                 ],
                 [
                 InlineKeyboardButton('Inush Deeptha', user_id="SL10Inush")
                 ],
                 [                 
                 InlineKeyboardButton('🅳🅰️🆁🅺 丂卂爪ㄩ尺卂|', user_id="IamDarkSam2")
                 ],
                 [                 
                 InlineKeyboardButton('ᴄʜᴀᴍᴏᴅ ɪᴍᴀɴᴛʜᴀ ֍🇱🇰', user_id="G_c_c_123")
                 ],
                 [                 
                 InlineKeyboardButton('🇲 🇷✪ ™✓DaRkᗰᗴᎩᕼᗴᗰ', user_id="Brotherz90")
                 ],
                 [
                 InlineKeyboardButton('#𝙇𝙚𝙥𝙩_𝙏𝙂 Kaveesha Nethmal', user_id="jason_spqr_roman_Kr")
                 ],
                 [                 
                 InlineKeyboardButton('අකිල', user_id="akiyush")
                 ],
                 [                 
                 InlineKeyboardButton('☬෴𝐃𝐀𝐑𝐊 ✠ 𝐋𝐎𝐑𝐃෴☬', url="tg://user?id=1390045267")
                 ],
                 [                 
                 InlineKeyboardButton(' 𝗩𝗶𝗻𝗶𝘁𝗵 𝗕𝗮𝘄𝗮𝗻𝘁𝗵𝗮', url="tg://user?id=1100376280")
                 ],
                 [
                 InlineKeyboardButton('💫𝗢𝘁𝗿𝗶𝘅𝘅💫', user_id="animepissa")
                 ],
                 [                 
                 InlineKeyboardButton('🔥🌏♠️𝐌𝐫 𝙊𝙍𝙂𝘼♠️🌏🔥', user_id="ORGA0302")
                 ],
                 [                 
                 InlineKeyboardButton('Mr.ᴅᴇᴠɪʟʟ😈', user_id="lucifer_the_devill")
                 ],
                 [                 
                 InlineKeyboardButton('« Alok Weerasinghe »', user_id="Alokweerasinghe")
                 ],
                 [
                 InlineKeyboardButton('Sathish Kalhara', user_id="Sathish_Kalhara")
                 ],
                 [
                 InlineKeyboardButton('ᴱᴹᴾ ƇƠƲƝƬ ƊƦƛƇƲԼƛ', user_id="LordVladtheImpalerTransylvania")
                 ], 
                 [                 
                 InlineKeyboardButton('Гейзенберг 🇱🇰', user_id="der_heisenberge")
                 ],
                 [
                 InlineKeyboardButton('𝕵𝕬𝖄 𝕬𝕲𝕽𝕰', user_id="AgreeAgree")
                 ],
                 [                 
                 InlineKeyboardButton('', user_id="Dr_Strome")
                 ],
                 [                 
                 InlineKeyboardButton('B_.x._.sh._.n._.x._ ⁪⁬⁮⁮⁮⁮ ‌‌‌‌', user_id="Revolution_will_not_be_Televised")
                 ],
                 [                 
                 InlineKeyboardButton('🔥ADMC⚡️⚡️THOR🔥', user_id="madushanka_Thor")
                 ]]
                  )

OWNER_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('Nirmal Abeysinghe', user_id="N_Abeysinghe_2001")
                 ]]
                  )               

DEV_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒ ', user_id="ImGishan")
                 ],
                 [
                 InlineKeyboardButton('unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="UnknownB_o_y")
                 ],
                 [
                 InlineKeyboardButton('ŦħȺɍᵾꝁ ɌɇnᵾɉȺ', user_id="ImTharuk")
                 ],
                 [
                 InlineKeyboardButton('𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™', user_id="SL_BOTS_TM")
                 ],
                 [
                 InlineKeyboardButton('𝘿𝙚𝙣𝙪𝙬𝙖𝙣 🇱🇰', user_id="ImDenuwan")
                 ]]
                  )


#Rndm Stkr

OWNER_STICKER = ["CAADAgADtA8AAhUWiEuTU2os6PSW-AI",
                "CAADAgADCwMAAm2wQgN_tBzazKZEJQI",
                "CAADAgADtwEAAladvQr3FVtdLiA1jgI", 
                "CAADBQADSwQAAnxrOFaYSIaXhBE_YAI"              
         ]

STAT_STICKER = ["CAADAQAD7gMAAv5DwUe0nbeQnSoavAI",
                "CAADAgAD8QEAAladvQohKm5i6iYv7gI"              
         ]  

ADMIN_STICKER = ["CAADAgADzhMAAhDzcElTIbO4ZQ8stAI",
                "CAADBQADxwQAAgcbUFea8nhgWIiuGwI",
                "CAADBQADPAUAAtzIoFWtMe3LazkiKQI", 
                "CAADBQADDgQAAkKxWVZAvhW5fKSifwI"              
         ]
         
DEV_STICKER = ["CAADAgADaRsAAsOUWUpHrmf5mZp3EgI",
                "CAADAgADbAIAAladvQoqGV6cxNDenwI",
                "CAADAgADgQEAAiteUwteCmw-bAABeLQC", 
                "CAADBQADZgMAAvIEcFVMnMXcAqRX7gI",
                "CAADAgADFwADlp-MDlZMBDUhRlElAg"                
         ] 

HELP_STICKER = ["CAADAgADYgADWbv8JXMOJcSM3-2OAg",
                "CAADAgADzwEAAhZCawpc3d8UgDDcaQI",
                "CAADAgAD9AIAAvPjvgtVDXi3hHimOQI", 
                "CAADAgADiQEAAiteUwt812TG6sLw9AI"               
         ]


#Menu Btn

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





print("Config Working....")
