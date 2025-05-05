import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")
    DB_URL = os.environ.get("DB_URL","")
 
    # other configs
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/eb80582fa42f9bd412085.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1087141176').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001778606534"))

    # free upload limit 
    FREE_UPLOAD_LIMIT = 10737418240  # 10 GB = 10 * 1024 * 1024 * 1024

    # premium mode feature ✅
    UPLOAD_LIMIT_MODE = True 
    PREMIUM_MODE = True 
    
    #force subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "Unlimited_Movie_Zone")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """<b>Hi, {}👋

This Is Advanced And Powerful File Renamer Bot 🤖
Using This Bot You Can Rename & Change Thumbnail Of Your File 📁
You Can Also Convert Video To File & File To Video 🎞️
This Bot Also Support Custom Caption & Metadata 📑

This Bot Was Created By : <a href=https://t.me/GwitcherG>Chamindu-Gayanuka💞</a></b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 My Name    : {}
├🖥️ Developers : {}
├👨‍💻 Programmer : {}
├📕 Library    : {}
├✏️ Language   : {}
├💾 Data Base  : {}
├📊 Version    : <a href=https://github.com/Chamindu-Gayanuka/Digital-Rename-Bot>{}</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> /Start The Bot.

✏️ <b><u>How to Rename a File</u></b>
<b>•></b> Send Any File And Type New File Name \nAnd Select The Format [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Unlimited_Movie_Zone>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

    UPGRADE_PREMIUM= """
•⪼ ★𝘗𝘭𝘢𝘯𝘴    -  ⏳𝘋𝘢𝘵𝘦 - 💸𝘗𝘳𝘪𝘤𝘦 
•⪼ 🥉𝘉𝘳𝘰𝘯𝘻𝘦  -   3𝘥𝘢𝘺𝘴 -   30
•⪼ 🥈𝘚𝘪𝘭𝘷𝘦𝘳   -   7𝘥𝘢𝘺𝘴 -   70
•⪼ 🥇𝘎𝘰𝘭𝘥    -  15𝘥𝘢𝘺𝘴 -  150
•⪼ 🏆𝘗𝘭𝘢𝘵𝘪𝘯𝘶𝘮 -  1𝘮𝘰𝘯𝘵𝘩 -  300
•⪼ 💎𝘋𝘪𝘢𝘮𝘰𝘯𝘥 -  2𝘮𝘰𝘯𝘵𝘩 -  600

- 𝘋𝘢𝘪𝘭𝘺 𝘜𝘱𝘭𝘰𝘢𝘥 𝘓𝘪𝘮𝘪𝘵 𝘜𝘯𝘭𝘪𝘮𝘪𝘵𝘦𝘥
- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 10%
    """
    
    UPGRADE_PLAN= """
𝘗𝘭𝘢𝘯: 𝘗𝘳𝘰
𝘋𝘢𝘵𝘦: 1 𝘮𝘰𝘯𝘵𝘩 
𝘗𝘳𝘪𝘤𝘦: 150
𝘓𝘪𝘮𝘪𝘵: 100 𝘎𝘉

𝘗𝘭𝘢𝘯: 𝘜𝘭𝘵𝘢 𝘗𝘳𝘰 
𝘋𝘢𝘵𝘦: 1 𝘮𝘰𝘯𝘵𝘩 
𝘗𝘳𝘪𝘤𝘦: 300
𝘓𝘪𝘮𝘪𝘵: 1000 𝘎𝘉

- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 10%
    """
    
    THUMBNAIL = """
🌌 <b><u>How to Set Thumbnail</u></b>

<b>•></b> Send Any Photo To Set As Thumbnail.
<b>•></b> /del_thumb Use This Command To Delete Your Current Thumbnail.
<b>•></b> /view_thumb Use This Command To View Your Current Thumbnail.
"""
    CAPTION= """
📑 <b><u>How to Set Custom Caption</u></b>

<b>•></b> /set_caption - Use This Command To Set Your Custom Caption.
<b>•></b> /see_caption - Use This Command To See Your Custom Caption.
<b>•></b> /del_caption - Use This Command To Delete Your Custom Caption.

Example:- `/set_caption 📕 FILE NAME: {filename}
💾 SIZE: {filesize}
⏰ DURATION: {duration}`
"""
    BOT_STATUS = """
⚡️ Bot Status ⚡️

⌚️ BOT UPTIME: `{}`
👭 TOTAL USERS: `{}`
💸 TOTAL PREMIUM USERS: `{}`
⏳ UPLOAD: `{}`
🚀 DOWNLOAD: `{}`
"""
    LIVE_STATUS = """
⚡ LIVE SERVER STATUS ⚡

UPTIME: `{}`
CPU: `{}%`
RAM: `{}%` 
TOTAL DISK: `{}`
USED SPACE: `{} {}%`
FREE SPACE: `{}`
UPLOAD: `{}`
DOWNLOAD: `{}`
V3.0.0 [STABLE]
"""
    DIGITAL_METADATA = """
❪ SET CUSTOM METADATA ❫

- /metadata - To Set & Change Your Custom Metadata.

☞ For Example:-

`--change-title @Unlimited_Movie_Zone
--change-video-title @Unlimited_Movie_Zone
--change-audio-title @Unlimited_Movie_Zone
--change-subtitle-title @Unlimited_Movie_Zone
--change-author @Unlimited_Movie_Zone`

📥 For Help Cont. @Unlimited_Movie_Zone
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /set_prefix - To add a prefix along with your filename.
➢ /see_prefix - To see your prefix.
➢ /del_prefix - To delete your prefix.
➢ /set_suffix - To add a suffix along with your filename.
➢ /see_suffix - To see your suffix.
➢ /del_suffix - To delete your suffix.

Example:- `/set_suffix @Unlimited_Movie_Zone`
Example:- `/set_prefix @Unlimited_Movie_Zone`
"""

    DEV_TXT = """<b><u>Special Thanks & Developers</b></u>
    
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/Chamindu-Gayanuka/Digital-Rename-Bot>Digital-Rename-Bot</a>

• ❣️ <a href=https://github.com/Chamindu-Gayanuka>Chamindu-Gayanuka</a>"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ For Example:-

`--change-title @Unlimited_Movie_Zone
--change-video-title @Unlimited_Movie_Zone
--change-audio-title @Unlimited_Movie_Zone
--change-subtitle-title @Unlimited_Movie_Zone
--change-author @Unlimited_Movie_Zone`

📥 For Help Cont. @Unlimited_Movie_Zone
"""
    
    RKN_PROGRESS = """<b>\n
╭━━━━❰RENAME PROCESSING...❱━➣
┣⪼ 🗃️ Size  : {1} | {2}
┣⪼ ⏳️ Done  : {0}%
┣⪼ 🚀 Speed : {3}/s
┣⪼ ⏰️ ETA   : {4}
╰━━━━━━━━━━━━━━━➣ </b>"""