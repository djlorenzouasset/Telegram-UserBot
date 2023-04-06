import aiofiles
import json

from typing import Optional
from datetime import datetime

from .utils import str_to_date, date_to_str


class Settings:
    def __init__(self, settings: dict):
        """
        Settings class for a better usage
        """
        
        self.afk: Afk = Afk(settings.get('afk'))


    @property
    def to_dict(self) -> dict:
        """
        Return the class as dict

        :return dict: Settings

        """

        return {
            'afk': self.afk.__dict__
        }
    

    async def set_afk(self, reason: str = None) -> None:
        """
        Set afk mode

        :return:

        """

        self.afk.enabled = True
        self.afk.start = date_to_str(datetime.now())

        if reason:
            self.afk.message = reason
        else:
            reason = 'No reason.'

        print('[+] AFK mode enabled')
        await self.save_settings()


    async def remove_afk(self) -> None:
        """
        Remove afk mode

        :return:

        """

        self.afk.enabled = False
        self.afk.message = None
        self.afk.start = None

        print('[+] AFK mode disabled')
        await self.save_settings()


    async def save_settings(self) -> None:
        """
        Save current settings 

        :return:

        """

        async with aiofiles.open(file="utils/settings.json", mode="w") as file:
            await file.write(json.dumps(self.to_dict, indent=4))


class Afk:
    def __init__(self, data: dict):
        self.enabled: bool = data.get('enabled')
        self.message: Optional[str] = data.get('message')
        self.start: str = data.get('start')

        self.answer: str = data.get('afk_answer_message', 'Im afk right now, I will answer you later.')

        if self.start:
            self.start: datetime = str_to_date(self.start)