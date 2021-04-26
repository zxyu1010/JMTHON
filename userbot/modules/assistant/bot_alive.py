from telethon import events

from userbot import ALIVE_NAME, bot

currentversion = "4.9"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "JMTHON"
pm_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
pm_caption += f"ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ\n"
pm_caption += f"**{EMOJI} حالة البوت 𝆹𝅥𝅮** `{check_sgnirts}`\n"
pm_caption += f"**{EMOJI} اصدار التليثون  𝆹𝅥𝅮** `{version.__version__}\n`"
pm_caption += f"**{EMOJI} اصدار البايثون 𝆹𝅥𝅮** `{python_version()}\n`"
pm_caption += f"**{EMOJI} مدة التشغيل 𝆹𝅥𝅮** `{uptime}\n`
pm_caption += f"**{EMOJI} يوزرك 𝆹𝅥𝅮** {mention}\n"
pm_caption += f"**{EMOJI} المطور 𝆹𝅥𝅮** [اضغط هنا](t.me/JMTHON) .\n"
pm_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧᵗⵧⵧ𓍻\n"

@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
