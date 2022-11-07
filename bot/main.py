import os

import telegram
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def main():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.send_message(TELEGRAM_CHAT_ID, 'Привет!')


if __name__ == '__main__':
    main()
