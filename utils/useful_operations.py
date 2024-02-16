from utils import sort_operations
from modul.operation_main import Operation

checked_operations = sort_operations.sorted_operations
last_checked_operations = []

for operation in checked_operations:
    if operation.get('from'):
        single_operation = Operation(operation['id'], operation['date'], operation['state'],
                                     operation['operationAmount']['amount'],
                                     operation['operationAmount']['currency']['name'],
                                     operation['description'],
                                     operation['from'], operation['to'])
        set_operation = single_operation.get_this_operation()
        last_checked_operations.append(set_operation)
    else:
        continue


print(last_checked_operations)