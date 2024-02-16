import utils

operations_data = utils.operations_content

print(operations_data)


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


print(get_executed_operations(operations_data))
