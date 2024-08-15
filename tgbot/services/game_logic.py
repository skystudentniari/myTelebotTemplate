import uuid

outcomes = {
        ('камень', 'ножницы'): "Ты выиграл!",
        ('камень', 'бумага'): "Ты проиграл!",
        ('ножницы', 'камень'): "Ты проиграл!",
        ('ножницы', 'бумага'): "Ты выиграл!",
        ('бумага', 'камень'): "Ты выиграл!",
        ('бумага', 'ножницы'): "Ты проиграл!"
    }


def determine_winner(player1_info, player2_info):
    player1_move = player1_info["move"]
    player2_move = player2_info["move"]   
    
    if player1_move == player2_move:
        result = "Ничья!"
    else:
        result = outcomes.get((player1_move, player2_move),
                              "Неправильный ввод! Пожалуйста, напиши камень, ножницы или бумага.")

    return result

def create_game(message):
    player_id = messsage.from_user.id
    chat_id = message_from_user.chat.id
    game_id = uuid.uuid1()
    game = {"start": True,
            "move1": False,
            "move2": False, 
            "end": False,
            "game_id": game_id,
            "players": {"player1": {"user_id": player_id,
                                    "name": message.from_user.first_name,
                                    "move": None
                                    },
                        
                        "player2": {}}
            }
    return game
    
def update_game():
    ...
    
def delete_game():
    ...
        
def computer_move():
    ...
    
def player_move(player_choice, user_id):
    ...
