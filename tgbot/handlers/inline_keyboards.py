from telebot import types

def create_inline_keyboard(buttons: list, row_width: int = 2) -> types.InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру с заданными кнопками и шириной строки.
    
    :param buttons: Список кнопок, каждая из которых представлена как кортеж (текст кнопки, callback_data).
    :param row_width: Количество кнопок в одной строке (по умолчанию 2).
    :return: Инстанс инлайн-клавиатуры.
    """
    markup = types.InlineKeyboardMarkup(row_width=row_width)
    for text, callback_data in buttons:
        button = types.InlineKeyboardButton(text, callback_data=callback_data)
        markup.add(button)
    return markup

def create_confirm_cancel_keyboard(confirm_text: str = "Подтвердить", cancel_text: str = "Отмена") -> types.InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру с кнопками подтверждения и отмены.
    
    :param confirm_text: Текст на кнопке подтверждения (по умолчанию 'Подтвердить').
    :param cancel_text: Текст на кнопке отмены (по умолчанию 'Отмена').
    :return: Инстанс инлайн-клавиатуры с двумя кнопками.
    """
    buttons = [
        (confirm_text, "confirm"),
        (cancel_text, "cancel")
    ]
    return create_inline_keyboard(buttons, row_width=2)

def create_choice_keyboard(choices: list, callback_prefix: str = "choice") -> types.InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру на основе списка вариантов выбора.
    
    :param choices: Список вариантов (строк), которые будут отображаться на кнопках.
    :param callback_prefix: Префикс для callback_data каждой кнопки (по умолчанию 'choice').
    :return: Инстанс инлайн-клавиатуры с кнопками для каждого варианта.
    """
    buttons = [(choice, f"{callback_prefix}_{choice}") for choice in choices]
    return create_inline_keyboard(buttons, row_width=3)

def create_dynamic_keyboard(options: list, callback_data_list: list) -> types.InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру с динамически заданными текстами и callback_data.
    
    :param options: Список строк с текстами для кнопок.
    :param callback_data_list: Список callback_data, соответствующий каждой кнопке.
    :return: Инстанс инлайн-клавиатуры с динамическими кнопками.
    :raises ValueError: Если длины списков options и callback_data_list не совпадают.
    """
    if len(options) != len(callback_data_list):
        raise ValueError("Количество опций и callback_data должно совпадать")
    
    buttons = [(text, callback_data) for text, callback_data in zip(options, callback_data_list)]
    return create_inline_keyboard(buttons, row_width=2)




def create_game_keyboard(may_choice: list, choice: str) -> types.InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для викторины с несколькими вариантами ответов.
    
    :param answers: Список строк, представляющих варианты ответов.
    :param correct_answer: Строка с правильным ответом.
    :return: Инстанс инлайн-клавиатуры с кнопками для викторины.
    """
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    # Создаем кнопки с вариантами ответов
    
    for choice in may_choice:
        markup.add(types.InlineKeyboardButton(choice, callback_data=choice))
    
    return markup