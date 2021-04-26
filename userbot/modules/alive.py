import time
from platform import python_version

from telethon import version

from . import ALIVE_NAME, StartTime, catversion, get_readable_time, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "𝗝𝗠𝗧𝗛𝗢𝗡"
CAT_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/25a12a98abe5392b13bd9.jpg"
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "✘  𝙬𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝗝𝗠𝗧𝗛𝗢𝗡  ✘"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "✜"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ\n"
        cat_caption += f"**{EMOJI} حالة البوت 𝆹𝅥𝅮** `{check_sgnirts}`\n"
        cat_caption += f"**{EMOJI} اصدار التليثون  𝆹𝅥𝅮** `{version.__version__}\n`"
        cat_caption += f"**{EMOJI} اصدار البايثون 𝆹𝅥𝅮** `{python_version()}\n`"
        #        cat_caption += f"**{EMOJI} مدة التشغيل 𝆹𝅥𝅮** `{uptime}\n`"
        cat_caption += f"**{EMOJI} يوزرك 𝆹𝅥𝅮** {mention}\n"
        cat_caption += f"**{EMOJI} قناة السورس 𝆹𝅥𝅮** [اضغط هنا](t.me/JMTHON) .\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧᵗⵧⵧ𓍻\n"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} حالة البوت  𝆹𝅥𝅮**  `{check_sgnirts}`\n"
            f"**{EMOJI} اصدار التليثون  𝆹𝅥𝅮** `{version.__version__}\n`"
            f"**{EMOJI} اصدار البايثون  𝆹𝅥𝅮** `{python_version()}\n`"
            f"**{EMOJI} مدة الاستخدام 𝆹𝅥𝅮** `{uptime}\n`"
            f"**{EMOJI} يوزرك 𝆹𝅥𝅮** {mention}\n",
        )


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "لم يتم تعيين حالة البوت"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "شغال 💯♥"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n  •  **Syntax : **`.alive` \
      \n  •  **Function : **__status of bot will be showed__\
      \n\n  •  **Syntax : **`.ialive` \
      \n  •  **Function : **__inline status of bot will be shown.__\
      \nSet `ALIVE_PIC` var for media in alive message"
    }
)
