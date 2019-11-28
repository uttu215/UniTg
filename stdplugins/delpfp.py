Delete N numbers of profile pictures
Command: `.delpfp <number of profile pictures to be deleted>`
credit-Satwik(noob)
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil

@borg.on(admin_cmd("delpfp ?(.*)"))
async def delpfpcmd(self, message):
        

        args = utils.get_args(message)
        if not args:
            return await utils.answer(message, _("<b>Please specify number of profile pics to remove.</b>"))
        if args[0].lower() == "unlimited":
            pfps_count = None
        else:
            try:
                pfps_count = int(args[0])
            except ValueError:
                return await utils.answer(message, _("<b>Wrong amount of pfps.</b>"))
            if pfps_count <= 0:
                return await utils.answer(message, _("<b>Please provide positive number of"
                                                     + " profile pictures to remove.</b>"))

        await self.client(functions.photos.DeletePhotosRequest(await self.client.get_profile_photos("me",
                                                                                                    limit=pfps_count)))

        if pfps_count is None:
            pfps_count = _("all")
        await self.allmodules.log("delpfp")
        await utils.answer(message, _("<b>Removed </b><code>{}</code><b> profile pic(s).</b>".format(str(pfps_count))))
