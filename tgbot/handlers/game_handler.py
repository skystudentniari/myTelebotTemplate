import random
from telebot import TeleBot
from telebot.types import Message


from ..services.game_logic import determine_winner, computer_move, player_move

MAY_CHOICE = ["камень", "ножницы", "бумага"]
 
def start_game_with_bot(message: Message, bot: TeleBot):
    user_id = messsage.from_user.id
    bot.send_message(user_id, f"Привет, выберите ход: (камень/ножницы/бумага)") #move
    bot.register_next_step_handler(message, process_bot_choice, bot)
    
    
def process_bot_choice(message: Message, bot: TeleBot):
    player_choice = message.text
    bot_choice = random.choice(MAY_CHOICE)
    player1_info = {"name": message.from_user.first_name, "move": player_choice}
    player2_info = {"name": "bot", "move": bot_choice}
    result = determine_winner(player1_info, player2_info)
    bot.send_message(user_id, result)