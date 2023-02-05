from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from jepthon import jepthon

from ..core.managers import edit_delete, edit_or_reply

@jepiq.on(admin_cmd(pattern="تاك 200(?: |$)(.*)"))
async def iq(jepiq):
    mentions = jepiq.text[8:]
    chat = await jepiq.get_input_chat()
    async for x in jepiq.client.iter_participants(chat, 200):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉"
    await jepiq.client.send_message(jepiq.chat_id, mentions)
    await jepiq.delete()
@jepiq.on(admin_cmd(pattern="تاك 150(?: |$)(.*)"))
async def iq(jepiq):
    mentions = jepiq.text[8:]
    chat = await jepiq.get_input_chat()
    async for x in jepiq.client.iter_participants(chat, 150):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await jepiq.client.send_message(jepiq.chat_id, mentions)
    await jepiq.delete()
@jepiq.on(admin_cmd(pattern="تاك 100(?: |$)(.*)"))
async def iq(jepiq):
    mentions = jepiq.text[8:]
    chat = await jepiq.get_input_chat()
    async for x in jepiq.client.iter_participants(chat, 100):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await jepiq.client.send_message(jepiq.chat_id, mentions)
    await jepiq.delete()
@jepiq.on(admin_cmd(pattern="تاك 50(?: |$)(.*)"))
async def iq(jepiq):
    mentions = jepiq.text[8:]
    chat = await jepiq.get_input_chat()
    async for x in jepiq.client.iter_participants(chat, 50):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await jepiq.client.send_message(jepiq.chat_id, mentions)
    await jepiq.delete()
@jepiq.on(admin_cmd(pattern="تاك 10(?: |$)(.*)"))
async def iq(jepiq):
    mentions = jepiq.text[8:]
    chat = await jepiq.get_input_chat()
    async for x in jepiq.client.iter_participants(chat, 10):
        mentions += f" \n 🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await jepiq.client.send_message(jepiq.chat_id, mentions)
    await jepiq.delete()
