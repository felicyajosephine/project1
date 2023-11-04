from typing import Final
from telegram import update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6897699155:AAGmRfX9QK97nKL83v2j0lVyvItryYoGBHs'
BOT_USERNAME: Final = '@brownpuppy_bot'

async def start_command(update :update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("HAIII, I am puppyyy")

async def help_command(update : update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("HAIII, I am puppyyy, text me, and i will repond")

async def custom_command(update : update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this is custom comand")

#responses

def handle_response(text: str): #str:
    processed: str = text.lower()
    if "hai" in processed:
        return "hellooo"

    if "how are u" in processed:
        return "i feel amazing"

    if "please entertain me" in processed:
        return "watch puppy video, it will help u"
    
    return "i can not respond to ur text"