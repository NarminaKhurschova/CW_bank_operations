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


def sort_by_date(all_operations):
    """
    Функция сортировки операций по дате
    :param all_operations: все операции list
    :return: упорядоченные по дате операции list
    """
    all_operations = sorted(all_operations, key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'),
                            reverse=True)

    return all_operations


def form_data_in_operation(operation):
    """
    Функция, приведения элемента массива ['date'] в формат даты
    :param operation: операции list,
    :return: операция с форматированной датой
    """
    date_time = datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f")
    date = date_time.strftime("%d.%m.%Y")
    return date


def few_last_operations(array, start=0, end=5):
    """
    Функция выдающая первые несколько элементов из списка
    :param array: список
    :param start: начало среза,
    :param end: конец среза,
    :return: возвращение списка с учетом среза
    """
    if array:
        return array[start:end]
    elif array is None:
        return "Нет списка"


def get_type_of_operations(user_of_operation):
    """
    Функция отображающая счет или карту,
    :param user_of_operation: название банковской операции [sendler] или [to],
    :return: возвращает измененную строку с буквенной частью название карты или Счет
    """
    pattern = r'\d'
    type_of_operation = re.sub(pattern, '', user_of_operation)
    return type_of_operation


def del_letters(bank_prod):
    """
    Функция удаления букв из банковского продукта
    :param bank_prod: название и номер банковского продукта
    :return: номер банковского продукта
    """
    pattern = r'\D+'
    bank_prod = re.sub(pattern, '', bank_prod)
    return bank_prod


def replace_num_to_symb(num_of_card):
    """
    Функция, сокрытия номера счета или карты
    :param num_of_card: номер счета или карты
    :return: номер счета с заменой цифр с 1 по 16,
    номер карты с заменой цифр с 6 по 12
    """
    num_of_card = del_letters(num_of_card)
    num_of_sender_secured = []
    for digit in num_of_card:
        if len(num_of_sender_secured) in range(6, 12):
            pattern = r'\d'
            num_of_sender_secured.append(re.sub(pattern, '*', digit))
        else:
            num_of_sender_secured.append(digit)
    return num_of_sender_secured


def bank_acc_num(num_bank_acc):
    """
    Функция распознавания банковского счета и вывода его последних 6 цифр,
    :param num_bank_acc: Наименование и номер банковского счета list,
    :return: последние 6 цифр list
    """
    digit_in_num = del_letters(num_bank_acc)
    num_of_sender_secured = []
    for digit in digit_in_num:
        if len(num_of_sender_secured) in range(0, 16):
            pattern = r'\d'
            num_of_sender_secured.append(re.sub(pattern, '*', digit))
        else:
            num_of_sender_secured.append(digit)
    return num_of_sender_secured[14:20]


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


def sort_by_bank_prod(bank_prod):
    """
    Функция распознования продукта банка
    :param bank_prod: Наименование и номер продукта банка str
    :return: Номер счета или банковской карты str
    """
    if "Счет" in bank_prod:
        acc_num = bank_acc_num(bank_prod)
        return acc_num
    else:
        card_num = replace_num_to_symb(bank_prod)
        card_num_div = div_card_numer(card_num)
        return card_num_div


def hide_num_of_card(operation):
    """
    Функция приведения цифровой части счета
    :param operation: одна операция dict
    :return: операция dict с измененным номером карты или счета
    """
    num_of_sender = operation['sender']
    num_of_sender_format = sort_by_bank_prod(num_of_sender)
    num_of_receiving = operation['to']
    num_of_receiving_format = sort_by_bank_prod(num_of_receiving)
    operation['sender'] = ''.join(num_of_sender_format)
    operation['to'] = ''.join(num_of_receiving_format)
    return operation





