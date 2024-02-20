from modul.operation_main import Operation
from utils.sort_operations import *

# Получение массива json
operations_data = utils.operations_content
# получение отсортированного списка библиотек
checked_operations = get_executed_operations(operations_data)
# список операций как объектов класса Operation
objects_of_operations = []

for operation in checked_operations:
    if operation.get('from'):
        single_operation = Operation(operation['id'], operation['date'], operation['state'],
                                     operation['operationAmount']['amount'],
                                     operation['operationAmount']['currency']['name'],
                                     operation['description'],
                                     operation['from'], operation['to'])
        set_operation = single_operation.get_this_operation()
        objects_of_operations.append(set_operation)
    else:
        continue

# операции с форматированным параметром date
objects_with_form_data = form_data_in_operation(objects_of_operations)
# последние 5 операций
last_operations = few_last_operations(objects_with_form_data)
for operation in last_operations:
    # получение названия счета или карты отправителя
    name_of_amount_sender = get_type_of_operations(operation['sender'])
    # получение названия счета или карты получателя
    name_of_amount_receiver = get_type_of_operations(operation['to'])
    # сокрытие цифр
    hide_it = hide_num_of_card(operation)
    # группировка по 4 цифры
    div_it = div_card_numer(operation)
    print(f'{operation["date"]} {operation["description"]}\n'
          f'{name_of_amount_sender }{operation["sender"]} -> {name_of_amount_receiver}{operation["to"]}\n'
          f'{operation["amount"]} {operation["name"]}')



