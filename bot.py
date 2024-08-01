# handlers
from tgbot.handlers.user import any_user

# telebot
from telebot import TeleBot

# config
from tgbot.config import load_config


def register_handlers(bot):
    bot.register_message_handler(any_user, commands=['start'], pass_bot=True)


def main():
    config = load_config(".env")

    bot = TeleBot(config.tg_bot.token)
    register_handlers(bot)

    bot.infinity_polling()



if __name__ == "__main__":
    main()