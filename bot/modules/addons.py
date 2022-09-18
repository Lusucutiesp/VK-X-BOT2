from pyrogram import enums
from telegram.ext import CommandHandler

from bot import LOGGER, DB_URI, PRE_DICT, dispatcher
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.db_handler import DbManger

def prename_set(update, context):
    lm = sendMessage("Pʟᴇᴀsᴇ Wᴀɪᴛ,Pʀᴏᴄᴇssɪɴɢ..🌀", context.bot, update.message)
    user_id_ = update.message.from_user.id 
    pre_send = update.message.text.split(" ", maxsplit=1)
    reply_to = update.message.reply_to_message
    if len(pre_send) > 1:
        txt = pre_send[1]
    elif reply_to is not None:
        txt = reply_to.text
    else:
        txt = ""
    prefix_ = txt
    PRE_DICT[user_id_] = prefix_
    if DB_URI:
        DbManger().user_pre(user_id_, prefix_)
        LOGGER.info(f"User : {user_id_} Prename is Saved in DB")
    editMessage("Pʀᴇɴᴀᴍᴇ Fᴏʀ Tʜᴇ Fɪʟᴇ Is Dᴏɴᴇ..🎌", lm)
    
prename_set_handler = CommandHandler(BotCommands.PreNameCommand, prename_set,
                                       filters=(CustomFilters.authorized_chat | CustomFilters.authorized_user), run_async=True)
dispatcher.add_handler(prename_set_handler)
