
class Operation:
    """
    Класс для одной банковской операции
    """
    def __init__(self, id, date, state, operationAmount, name_of_currency, description, sender, to):
        self.id = id
        self.date = date
        self.state = state
        self.operationAmount = operationAmount
        self.name_of_currency = name_of_currency
        self.description = description
        self.sender = sender
        self.to = to

    def get_id(self):
        if self.id >= 0:
            return id
        else:
            print("Поле 'id' не заполнено")

    def get_format_date(self):
        if self.date is None:
            print("Поле 'date' не заполнено")
        else:
            return self.date

    def get_state(self):
        if self.state is None:
            print("Поле 'state' не заполнено")
        else:
            return self.state

    def get_operationAmount(self):
        if self.operationAmount is None:
            print("Поле 'operationAmount' не заполнено")
        else:
            return self.operationAmount

    def get_description(self):
        if self.description is None:
            print("Поле 'description' не заполнено")
        else:
            return self.description

    def get_sender(self):
        if self.sender is None:
            print("Поле 'sender' не заполнено")
        else:
            return self.sender

    def get_to(self):
        if self.to is None:
            print("Поле 'to' не заполнено")
        else:
            return self.to

    def get_this_operation(self):
        operation_content = {
            'date': self.get_format_date(),
            'description': self.get_description(),
            'sender': self.get_sender(),
            'to': self.get_to(),
            'amount': self.get_operationAmount(),
            'name': self.name_of_currency
        }
        return operation_content

