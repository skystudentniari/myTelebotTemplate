import random
from telebot import TeleBot
from telebot.types import Message,CallbackQuery
import logging
from inline_keyboards import create_game_keyboard


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
    bot.send_message(message.chat.id, f"Выберите ходы: камень/ножницы/бумага", reply_markup=get_inline_keyboard())
    

def process_bot_choice(message: Message, bot: TeleBot):
    user_id = message.from_user.id
    player_choice = message.text
    bot_choice = random.choice(MAY_CHOICE)
    player1_info = {"name": message.from_user.first_name, "move": player_choice}
    player2_info = {"name": "bot", "move": bot_choice}
    result = determine_winner(player1_info, player2_info)
    print(result)
    if result["is_correct"]:
        bot.send_message(user_id, result["game_result"])
    else:
        bot.send_message(user_id, result["game_result"])
        bot.register_next_step_handler(message, process_bot_choice, bot)



def handler_player_move(message:Message,  bot: TeleBot):
    question = "Сделайте ваш выбор:"
    may_choice = MAY_CHOICE
    bot_answer = "Ваш ход был принят"
    
    # Отправляем вопрос с вариантами ответов
    answer = bot.send_message(message.chat.id, question, reply_markup=create_game_keyboard(may_choice, bot_answer))
    # print(answer) 



def handle_game_callback(call: CallbackQuery,  bot: TeleBot):
    # Извлекаем правильность ответа из callback_data
    print(call)

    # Редактируем сообщение, чтобы убрать клавиатуру после ответа
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)