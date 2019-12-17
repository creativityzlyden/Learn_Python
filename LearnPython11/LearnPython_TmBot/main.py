from telegram.ext import Updater
from config import TG_Token
updater = Updater(token=TG_Token, use_context=True)

def main():
    updater.start_polling()
    updater.idle()


main()
