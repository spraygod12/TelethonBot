from .. import BotzHub
from telethon import events, Button

SMEX_USER = [1817754337]

@BotzHub.on(events.NewMessage(pattern="^/repo ?(.*)"))
async def _(event):
  if event.sender_id in SMEX_USER:
    await BotzHub.send_message(event.chat_id, "**HEY MASTER HERE IS YOUR REPO**\n\nhttps://github.com/spraygod12/TelethonBot")
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
