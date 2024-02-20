import json

# получение массива из json
with open('../data_json/operations.json') as file:
    file_content = file.read()
    operations_content = json.loads(file_content)

