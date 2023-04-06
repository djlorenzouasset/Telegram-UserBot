import asyncio
import pyrogram

from utils.TelegramClient import TelegramClient


class Main:
    def __init__(self): 
        self.client = TelegramClient()


    async def start_client(self):
        """
        Start the client and run the userbot until you press Ctrl + C
        """
        
        await self.client.run()

        await pyrogram.idle()
        print('[-] Userbot stopped. Bye.')
        await self.client.stop()


try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Main().start_client())
except KeyboardInterrupt:
    pass