from telebot import TeleBot
from telebot.types import Message

def any_user(message: Message, bot: TeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}!")