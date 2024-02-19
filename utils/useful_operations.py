from utils import sort_operations
from modul.operation_main import Operation
from utils.sort_operations import *


checked_operations = sort_operations.sorted_operations
all_checked_operations = []

for operation in checked_operations:
    if operation.get('from'):
        single_operation = Operation(operation['id'], operation['date'], operation['state'],
                                     operation['operationAmount']['amount'],
                                     operation['operationAmount']['currency']['name'],
                                     operation['description'],
                                     operation['from'], operation['to'])
        set_operation = single_operation.get_this_operation()
        all_checked_operations.append(set_operation)
    else:
        continue

not_all = sorted_by_date(all_checked_operations)
last_operations = few_last_operations(not_all)
for operation in last_operations:
    hide_it = hide_num_of_card(operation)
    print (hide_it)



