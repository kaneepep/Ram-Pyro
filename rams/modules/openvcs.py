from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as gez 
from geezlibs.geez.helper.cmd import *
from pyrogram.errors import MessageNotModified
from geezlibs.geez.helper.what import *
from geezlibs.geez.helper.basic import *
from geezlibs.ram.helpers.adminHelpers import DEVS, 
from config import BLACKLIST_GCAST
from geezlibs.geez.utils.misc import *
from geezlibs.geez.utils.tools import *

import requests
import os
import json
import random

@gez.on_message(filters.command("cask", cmd) & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ask", cmd) & filters.me)
async def openai(c, m):
    if len(m.command) == 1:
        return await m.reply(f"Ketik <code>.{m.command[0]} [question]</code> Pertanya untuk menggunakan OpenAI")
    question = m.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await m.reply("`Processing..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("**Kalo nanya yang bener dikit kek...**")
