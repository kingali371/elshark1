
import asyncio
import random
import re
import time
from random import choice, randint
from collections import deque
from telethon import events
import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName


from jmthon import CMD_HELP
from jmthon.utils import admin_cmd


# ================= CONSTANT =================


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# ===========================================

@jmub.on(admin_cmd(pattern=r"هف$"))
async def facepalm(e):
    """ Facepalm  🤦‍♂ """
    await e.edit("🤦‍♂")

@jmub.on(admin_cmd(pattern=r"كوفيد$"))
async def iqless(e):
    await e.edit("Antivirus scan was completed \n⚠️ Warning! This  donkey has Corona Virus")


@jmub.on(admin_cmd(pattern=r"ggl (.*)"))
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Tap this blue, help yourself.\
    \n[{query}]({r.json()['shorturl']})")


@jmub.on(admin_cmd(outgoing=True, pattern="فاشل$"))
async def fail(e):
        await e.edit("`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `" 
                     "`\n████▌▄▌▄▐▐▌█████ `"    
                     "`\n████▌▄▌▄▐▐▌▀████ `"       
                     "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `")    


@jmub.on(admin_cmd(outgoing=True, pattern="لول$"))
async def lol(e):
        await e.edit("`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `" 
                     "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"       
                     "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `" 
                     "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `") 
 
 
                                                                                   
@jmub.on(admin_cmd(outgoing=True, pattern="لوول$"))
async def lool(e):
        await e.edit("`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
                     "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
                     "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `")
                     



@jmub.on(admin_cmd(outgoing=True, pattern="ورده$"))
async def nih(e):
        await e.edit("`\n(\_/)`"
                     "`\n(•_•)`"
                     "`\n >🌹 *`"
                     "`\n                    `"
                     "`\n(\_/)`"
                     "`\n(•_•)`"
                     "`\n🌹<\ *`")


@jmub.on(admin_cmd(outgoing=True, pattern="هلو$"))  
async def gtfo(e):
        await e.edit("`\n█████████`" 
                     "`\n█▄█████▄█`"    
                     "`\n█▼▼▼▼▼`"       
                     "`\n█  منور يحب `"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                    "`\n ██   ██`")               


@jmub.on(admin_cmd(outgoing=True, pattern="ml(?: |$)(.*)"))
async def gtfo(e):
        message = e.pattern_match.group(1)
        await e.edit("`\n█████████`" 
                     "`\n█▄█████▄█`"    
                     "`\n█▼▼▼▼▼`"       
                     f"`\n█  {message}`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                    "`\n ██   ██`")               


@jmub.on(admin_cmd(outgoing=True, pattern="اكل$")) 
async def taco(e):
        await e.edit("\n{\__/}"
                     "\n(●_●)"
                     "\n( >🌮 اتفضل معايا?")


@jmub.on(admin_cmd(outgoing=True, pattern="باو$"))  
async def paw(e):
        await e.edit("`(=ↀωↀ=)")


@jmub.on(admin_cmd(outgoing=True, pattern="tf$")) 
async def tf(e):
        await e.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")  
      

@jmub.on(admin_cmd(outgoing=True, pattern="واحد$"))           
async def gey(e):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈U GAY`"
                    "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")    


@jmub.on(admin_cmd(outgoing=True, pattern="بوت$"))
async def bot(e):
        await e.edit("` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
                     "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `")


@jmub.on(admin_cmd(outgoing=True, pattern="جيت$"))
async def hey(e):
        await e.edit("\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃اناجيت!┊😀`"
                     "`\n┈┈▕▔▇▔▔┳▔▏╰┳┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
                     "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`")


@jmub.on(admin_cmd(outgoing=True, pattern="تف$"))
async def nou(e):
        await e.edit("`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
                     "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
                     "`\n┫┈┈  تف علي وشك\n┃┈╰╰━━━━╯`"
                     "`\n┗━━┻━┛`")



@jmub.on(admin_cmd(outgoing=True, pattern="خد$"))
async def gtfo(e):
        await e.edit(
"\n......................................../´¯/) "
"\n......................................,/¯../ "
"\n...................................../..../ "
"\n..................................../´.¯/"
"\n..................................../´¯/"
"\n..................................,/¯../ "
"\n................................../..../ "
"\n................................./´¯./"
"\n................................/´¯./"
"\n..............................,/¯../ "
"\n............................./..../ "
"\n............................/´¯/"
"\n........................../´¯./"
"\n........................,/¯../ "
"\n......................./..../ "
"\n....................../´¯/"
"\n....................,/¯../ "
"\n.................../..../ "
"\n............./´¯/'...'/´¯¯`·¸ "
"\n........../'/.../..../......./¨¯\ "
"\n........('(...´...´.... ¯~/'...') "
"\n.........\.................'...../ "
"\n..........''...\.......... _.·´ "
"\n............\..............( "
"\n..............\.............\...")



@jmub.on(admin_cmd(outgoing=True, pattern="قول هلا$"))
async def shalom(e):
    await e.edit(
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛🔷🔷🔷🔷️🔷🔷🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷💛💛️💛💛💛🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷️🔷💛"
        "\n💛🔷💛💛💛💛️💛🔷💛"
        "\n💛💛💛💛💛💛💛💛💛")

@jmub.on(admin_cmd(outgoing=True, pattern=r"(?:penis|dick)\s?(.)?"))
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace('🍆', emoji)
    await e.edit(titid)


