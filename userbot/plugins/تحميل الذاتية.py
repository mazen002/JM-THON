#  قبل لا تفكر تخمط هذا الملف ترا الملف متعوب عليه لا تخمط واني حذرتك
# حسب قوانين موقع github https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
# تنص على انه اي شخص ياخذ الملف بدون ذكر حقوق طبع والنشر سيتم حذف حسابه من قبل صاحب الملف اقتضى التنوي
# Copyright ©️ 2021 RR9R7 . All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits -  (  @RR7PP  - @JMTHON  )

from userbot import *
from userbot import jmthon

@jmthon.on(admin_cmd(pattern="(جلب الصورة|احا)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    rr9r7 = await event.get_reply_message()
    pic = await rr9r7.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
-تـم جـلب الصـورة بنجـاح ✅
- CH: @Jmthon
- Dev: @RR9R7
  """,
    )
    await event.edit("تتحمل")
