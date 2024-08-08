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
    
def computer_move():
    ...
    
def player_move(player_choice, user_id):
    ...

