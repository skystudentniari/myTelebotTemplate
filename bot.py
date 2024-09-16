import logging

# handlers
from tgbot.handlers.user import any_user
from tgbot.handlers.game_handler import (start_game_with_bot,
                                         start_game_with_player, handle_game_callback)

# telebot
from telebot import TeleBot

# config
from tgbot.config import load_config

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


def register_handlers(bot):
    bot.register_message_handler(any_user, commands=["start"], pass_bot=True)
    bot.register_message_handler(start_game_with_bot, commands=["game_bot"], pass_bot=True)
    bot.register_message_handler(start_game_with_player, commands=["game"], pass_bot=True)
    bot.register_callback_query_handler(handle_game_callback, func=lambda call: call.data.startswith('quiz_'),  pass_bot=True)



def main():
    setup_logging()

    config = load_config(".env")

    bot = TeleBot(config.tg_bot.token)
    register_handlers(bot)

    bot.infinity_polling()


if __name__ == "__main__":
    main()
