import utils.http_session
import utils.transport
import utils.session
import aiohttp, asyncio, warnings, pytz, datetime
import logging
import logging.config
import glob, sys, importlib.util, pyromod
from pathlib import Path

# pyrogram imports
import pyrogram.utils
from pyrogram import Client, __version__, errors
from pyrogram.raw.all import layer

# bots imports
from config import Config
from plugins.web_support import web_server
from plugins.file_rename import app


pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

# Get logging configurations
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler('BotLog.txt'),
             logging.StreamHandler()]
)
#logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class DigitalRenameBot(Client):
    def __init__(self):
        super().__init__(
            name="DigitalRenameBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15)
                
         
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME
        self.premium = Config.PREMIUM_MODE
        self.uploadlimit = Config.UPLOAD_LIMIT_MODE
       # self.log = logger
        
        app = aiohttp.web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await aiohttp.web.TCPSite(app, bind_address, Config.PORT).start()
        
        path = "plugins/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as a:
                patt = Path(a.name)
                plugin_name = patt.stem.replace(".py", "")
                plugins_path = Path(f"plugins/{plugin_name}.py")
                import_path = "plugins.{}".format(plugin_name)
                spec = importlib.util.spec_from_file_location(import_path, plugins_path)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["plugins" + plugin_name] = load
                print("Digital Botz Imported " + plugin_name)
                
        print(f"{me.first_name} Is Started.....✨️")
        
        for id in Config.ADMIN:
            if Config.STRING_SESSION:
                try: await self.send_message(id, f"2GB+ File Support Has Been Added To Your Bot.\n\nNote: 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐓𝐡𝐞𝐧 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐬 𝟐𝐆𝐁+ 𝐟𝐢𝐥𝐞𝐬.\n\n**__{me.first_name}  Is Started.....✨️__**")
                except: pass
            else:
                try: await self.send_message(id, f"2GB- File Support Has Been Added To Your Bot.\n\n**__{me.first_name}  Is Started.....✨️__**")
                except: pass
                    
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.datetime.now(pytz.timezone("Asia/Colombo"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL, f"**__{me.mention} Is Restarted !!**\n\n📅 Date : `{date}`\n⏰ Time : `{time}`\n🌐 TimeZone : `Asia/Colombo`\n\n🉐 Version : `v{__version__} (Layer {layer})`</b>")
            except:
                print("Please Make This Bot Admin in Your Log Channel")

    async def stop(self, *args):
        for id in Config.ADMIN:
            try: await self.send_message(id, f"**Bot Stopped....**")                                
            except: pass
        print("Bot Stopped 🙄")
        await super().stop()
        

bot_instance = DigitalRenameBot()

def main():
    async def start_services():
        if Config.STRING_SESSION:
            await asyncio.gather(
                app.start(),        # Start the Pyrogram Client
                bot_instance.start()  # Start the bot instance
            )
        else:
            await asyncio.gather(bot_instance.start()) # Start the bot instance

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())
    loop.run_forever()

if __name__ == "__main__":
    warnings.filterwarnings("ignore", message="There is no current event loop")
    try:
        main()
    except errors.FloodWait as ft:
        print(f"Flood Wait Occurred, Sleeping For {ft}")
        asyncio.sleep(ft.value)
        print("Now Ready For Deploying !")
        main()