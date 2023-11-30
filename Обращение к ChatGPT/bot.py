from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
   update.message.reply_text('Привет, я твой бот!')

def main() -> None:
   updater = Updater("TOKEN", use_context=True)
   dispatcher = updater.dispatcher
   dispatcher.add_handler(CommandHandler("start", start))
   updater.start_polling()
   updater.idle()

if __name__ == '__main__':
   main()