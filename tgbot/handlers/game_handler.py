import random
from telebot import TeleBot
from telebot.types import Message, InlineKeyboardMarkup
import logging


from ..services.game_logic import determine_winner, computer_move, player_move, create_game

MAY_CHOICE = ["камень", "ножницы", "бумага"]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

games = {}

def start_game_with_bot(message: Message, bot: TeleBot):
    user_id = message.from_user.id
    bot.send_message(user_id, f"Привет, выберите ход: (камень/ножницы/бумага)")  # move
    bot.register_next_step_handler(message, process_bot_choice, bot)
    
def start_game_with_player(message: Message, bot: TeleBot):
    user_id = message.from_user.id
    game = create_game(message)
    game_id = game.get("game_id")
    games[game_id] = game
    bot.send_message(user_id, f"Привет! Создалась игра под id {game_id}."
                    "Вы игрок 1")
    logging.info(f"Была создана игра - {game}")

def process_bot_choice(message: Message, bot: TeleBot):
    user_id = message.from_user.id
    player_choice = message.text
    bot_choice = random.choice(MAY_CHOICE)
    player1_info = {"name": message.from_user.first_name, "move": player_choice}
    player2_info = {"name": "bot", "move": bot_choice}
    result = determine_winner(player1_info, player2_info)
    bot.send_message(user_id, result)

def get_inline_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for choice in MAY_CHOICE:
        markup.add(InlineKeyboardButton(choice, callback_data=choice))
    return markup
