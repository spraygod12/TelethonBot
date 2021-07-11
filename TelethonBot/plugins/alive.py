from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/alive"))
async def alibe(event):
  BANG_PIC = "https://telegra.ph/file/14bf5a328b02eff37ed26.jpg"
  but = [[Button.url("Mʏ ᴍᴀsᴛᴇʀ »»", "t.me/PR4TIK_XD")]]
  pm_caption = "•**I'M ALIVE AND READY TO BANG**\n\n"
  pm_caption += "•**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
  pm_caption += "• Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
  pm_caption += "• 𝙎𝙈𝙀𝙓 𝙓 𝙑𝙀𝙍𝙎𝙄𝙊𝙉: 1.1\n"
  pm_caption += "• 𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉 ☞ {version.__version__}\n"
  pm_caption += (
        "• 𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔 ☞ [「sᴘʀᴀʏɢᴏᴅ • ᴏᴘ」❤️🥀](t.me/PR4TIK_XD)\n\n"
    )
  pm_caption += f"• 𝘾𝙍𝙀𝘼𝙏𝙊𝙍 ☞ [「sᴘʀᴀʏɢᴏᴅ • ᴏᴘ」❤️🥀](t.me/PR4TIK_XD)\n"
  await BotzHub.send_file(event. chat_id, file=BANG_PIC, captions=pm_caption, buttons=but, link_preview=False)
