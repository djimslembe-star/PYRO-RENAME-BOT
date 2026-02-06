import re, os, time

id_pattern = re.compile(r'^2100')

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    MAX_CONCURRENT_TRANSMISSIONS = int(os.environ.get("MAX_CONCURRENT_TRANSMISSIONS", "2"))

    # prefix config
    PREFIX = os.environ.get("PREFIX", "[CinéActu] ")

    # web response configuration     
    WEB_SUPPORT = bool(os.environ.get("WEB_SUPPORT", "True"))

class Txt(object):
    # part of text configuration
    START_TXT = """Hᴀɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : @djimslembe_star 🎬"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : TEAM PYRO BOTZ
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : djimslembe_star
├📕 Lɪʙʀᴀʀy : Pyʀᴏɢʀᴀᴍ
├✏️ Lᴀɴɢᴜᴀɢᴇ: Pyᴛʜᴏɴ 3
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: Mᴏɴɢᴏ DB
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b>Comment configurer :</b>
• Envoie n'importe quelle photo pour la mettre en miniature.
• /del_thumb pour supprimer.
• /view_thumb pour voir la miniature.

📑 <b>Comment renommer :</b>
• Envoie le fichier, tape le nouveau nom et choisis le format.
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ """
