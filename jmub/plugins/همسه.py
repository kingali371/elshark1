from telethon import events
import random, re
from jmthon.utils import admin_cmd
import asyncio 

# Wespr File by  @lMl10l
# Copyright (C) 2021 jmthon TEAM
@jmub.on(
    admin_cmd(pattern="همسة ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    jepiqb = event.pattern_match.group(1)
    rrrd7 = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(rrrd7, jepiqb) 
    await tap[0].click(event.chat_id)
    await event.delete()
    
@jmub.on(admin_cmd("م23"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("᯽︙ اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n᯽︙ الامر • `.الهمسة`\n᯽︙ استخدامه • لعرض كيفية كتابة همسة سرية\n\n᯽︙ الامر • `.اكس او `\n ᯽︙ استخدامه • ففط ارسل الامر لبدء لعبة اكس او\n\n᯽︙ CH  - @L_H_V")
        
@jmub.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**᯽︙ شـرح كيـفية كـتابة همـسة سـرية**\n᯽︙ اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n᯽︙ مـثال  :   `.همسة ههلا @T_3_A`")
        
@jmub.on(
    admin_cmd(
       pattern="اكس او$"
    )
)
# كتابة وتعديل فريق الجوكر  #@lMl10l
async def gamez(event):
    if event.fwd_from:
        return
    jmusername = "@xoBot"
    uunzz = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(jmusername, uunzz)
    await tap[0].click(event.chat_id)
    await event.delete()
