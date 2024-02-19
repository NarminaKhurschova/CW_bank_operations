import utils
from datetime import datetime
import re

operations_data = utils.operations_content


def get_executed_operations(all_operations):
    executed_operations = []

    for operation in all_operations:
        if operation.get('state'):
            if operation['state'] == 'EXECUTED':
                executed_operations.append(operation)
                continue
        else:
            continue
    return executed_operations


sorted_operations = get_executed_operations(operations_data)


def sorted_by_date(all_operations):
    all_operations = sorted(all_operations, key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'),
                            reverse=True)

    return all_operations


def few_last_operations(sorted_by_date, start=1, end=6):
    if sorted_by_date:
        return sorted_by_date[start:end]
    else:
        print("Нет списка")


def hide_num_of_card(operation):
    num_of_card = operation['sender']
    pattern = r'\D+'
    card_number_raw = re.sub(pattern, '', num_of_card)
    card_number_secured = []

    if 'Счет' not in num_of_card:
        for digit in card_number_raw:
            if len(card_number_secured) in range(6, 12):
                pattern = r'\d'
                card_number_secured.append(re.sub(pattern, '*', digit))
            else:
                card_number_secured.append(digit)
    else:
        for digit in card_number_raw:
            if len(card_number_secured) in range(0, 16):
                pattern = r'\d'
                card_number_secured.append(re.sub(pattern, '*', digit))
            else:
                card_number_secured.append(digit)

    card_number_formatted = []
    for i, sym in enumerate(card_number_secured):
        card_number_formatted.append(sym)
        if (i+1) % 4 == 0:
            card_number_formatted.append(' ')

    operation['sender'] = ''.join(card_number_formatted)




    return operation





