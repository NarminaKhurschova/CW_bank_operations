import utils
from datetime import datetime
import re


def get_executed_operations(all_operations):
    """
    Функция вычисляющая только одобренные операции:
    :param all_operations: список библиотек операций,
    :return: список библиотек операций, которые одобрены (EXECUTED)
    """
    executed_operations = []
    for operation in all_operations:
        if operation.get('state'):
            if operation['state'] == 'EXECUTED':
                executed_operations.append(operation)
                continue
        else:
            continue
    return executed_operations


def form_data_in_operation(all_operations):
    """
    Функция, приведения элемента массива ['date'] в формат даты
    :param all_operations: операция dict,
    :return: операция с форматированной датой
    """
    all_operations = sorted(all_operations, key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'),
                            reverse=True)
    return all_operations


def few_last_operations(array, start=1, end=6):
    """
    Функция выдающая первые несколько элементов из списка
    :param array: список
    :param start: начало среза,
    :param end: конец среза,
    :return: возвращение списка с учетом среза
    """
    if array:
        return array[start:end]
    else:
        print("Нет списка")


def get_type_of_operations(user_of_operation):
    """
    Функция отображающая счет или карту,
    :param user_of_operation: название банковской операции [sendler] или [to],
    :return: возвращает измененную строку с буквенной частью название карты или Счет
    """
    pattern = r'\d'
    type_of_operation = re.sub(pattern, '', user_of_operation)
    return type_of_operation


def replace_num_to_symb(num_of_sender):
    """
    Функция, сокрытия номера счета или карты
    :param num_of_sender: номер счета или карты
    :return: номер счета с заменой цифр с 1 по 16,
    номер карты с заменой цифр с 6 по 12
    """
    pattern = r'\D+'
    card_sender_num_raw = re.sub(pattern, '', num_of_sender)
    num_of_sender_secured = []
    if 'Счет' not in num_of_sender:
        for digit in card_sender_num_raw:
            if len(num_of_sender_secured) in range(6, 12):
                pattern = r'\d'
                num_of_sender_secured.append(re.sub(pattern, '*', digit))
            else:
                num_of_sender_secured.append(digit)
    else:
        for digit in card_sender_num_raw:
            if len(num_of_sender_secured) in range(0, 16):
                pattern = r'\d'
                num_of_sender_secured.append(re.sub(pattern, '*', digit))
            else:
                num_of_sender_secured.append(digit)
    return num_of_sender_secured


def div_card_numer(operation_to_div_card):
    """
    Функция приведения номера счета или карты
    в отображение по 4 цифры
    :param operation_to_div_card: цифровая часть названия карты или счета,
    :return: цифровая часть карты или счета, поделенная по 4 цифры
    """
    card_to_div = operation_to_div_card
    card_number_formatted = []
    for i, sym in enumerate(card_to_div):
        card_number_formatted.append(sym)
        if (i + 1) % 4 == 0:
            card_number_formatted.append(' ')
    return card_number_formatted


def hide_num_of_card(operation):
    """
    Функция приведения цифровой части счета
    с помощью функций div_card_numer, replace_num_to_symb,
    :param operation: одна операция dict
    :return: операция dict с измененным номером карты или счета
    """
    num_of_sender = operation['sender']
    num_of_sender_format = div_card_numer(replace_num_to_symb(num_of_sender))
    num_of_receiving = operation['to']
    num_of_receiving_format = div_card_numer(replace_num_to_symb(num_of_receiving))
    operation['sender'] = ''.join(num_of_sender_format)
    operation['to'] = ''.join(num_of_receiving_format)
    return operation
