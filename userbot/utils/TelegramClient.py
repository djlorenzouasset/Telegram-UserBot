import aiofiles
import json
import os 

from pyrogram import Client
from dotenv import load_dotenv

from utils.settings import Settings


class TelegramClient(Client):
    def __init__(self):
        """
        custom telegram client

        """
        load_dotenv() # load .env file

        self.session: str = "session"
        self.api_id: int = os.getenv("API_ID")
        self.api_hash: str = os.getenv("API_HASH")

        self.settings: Settings = Settings

        super().__init__(
            name=self.session,
            api_id=self.api_id,
            api_hash=self.api_hash,
            plugins=dict(root="plugins")
        )

    
    async def run(self):
        """
        Run client and initialize settings

        """
        if not os.path.isfile("utils/settings.json"):
            print('[ERROR] settings.json not found.')
            exit(2)

        else:
            async with aiofiles.open(file="utils/settings.json", mode="r") as f:
                self.settings = Settings(json.loads(await f.read()))

            await self.start()        
            print(f'[+] Userbot started as {self.me.first_name} ({self.me.id})')