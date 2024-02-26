import utils.data_from_json
from modul.operation_main import Operation
from utils.data_from_json import *
from utils.sort_operations import *

# Получение массива json
operations_data = utils.data_from_json.operations_content
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
objects_sort_by_data = sort_by_date(objects_of_operations)

# последние 5 операций
last_operations = few_last_operations(objects_sort_by_data)
for operation in last_operations:
    date_of_operation = form_data_in_operation(operation)
    # получение названия счета или карты отправителя
    name_of_amount_sender = get_type_of_operations(operation['sender'])
    # получение названия счета или карты получателя
    name_of_amount_receiver = get_type_of_operations(operation['to'])
    # сокрытие цифр
    hide_it = hide_num_of_card(operation)
    # группировка по 4 цифры
    div_it = div_card_numer(operation)
    print(f'{date_of_operation} {operation["description"]}\n'
          f'{name_of_amount_sender }{operation["sender"]} -> {name_of_amount_receiver}{operation["to"]}\n'
          f'{operation["amount"]} {operation["name"]}')



