import pytest
from utils.sort_operations import *


@pytest.fixture
def operations_fi():
    return [{"id": 1,
             "name": "Счет",
             "state": "EXECUTED"},
            {"id": 2,
             "name": "Счет",
             "date": "2019-08-26T10:50:58.294041",
             "state": "EXECUTED"},
            {"id": 3,
             "name": "Счет",
             "state": "CANCELED"}
            ]


@pytest.fixture
def operation_cancel():
    return [{"id": 3,
             "name": "Счет",
             "func": "CANCELED"},
            {"id": 5,
             "name": "MasterCard",
             "func": "CANCELED"}
            ]


@pytest.fixture
def num_acc():
    return "Счет 44567890996523548765"


@pytest.fixture
def num_card():
    return "4456789099652354"


@pytest.fixture
def one_operation():
    return {"id": 2,
            "name": "Счет",
            "date": "2019-08-26T10:50:58.294041",
            "sender": "Счет 44567890996523548765",
            "to": "MasterCard 4456789099652354",
            "state": "EXECUTED"}


def test_get_executed_operations(operations_fi, operation_cancel):
    assert get_executed_operations(operations_fi) == [{"id": 1, "name": "Счет",
                                                       "state": "EXECUTED"},
                                                      {"id": 2,
                                                       "name": "Счет",
                                                       "state": "EXECUTED",
                                                       "date": "2019-08-26T10:50:58.294041"}]
    assert get_executed_operations(operation_cancel) == []


def test_few_last_operations(operations_fi):
    assert few_last_operations(None, 2, 3) == "Нет списка"
    assert few_last_operations(operations_fi, 2, 3) == [{"id": 3,
                                                         "name": "Счет",
                                                         "state": "CANCELED"}]


def test_replace_num_to_symb(num_card):
    assert replace_num_to_symb(num_card) == ["4", "4", "5", "6", "7", "8", "*", "*", "*", "*"
        , "*", "*", "2", "3", "5", "4"]


def test_bank_acc_num(num_acc):
    assert bank_acc_num(num_acc) == ["*", "*", "8", "7", "6", "5"]


def test_hide_num_of_card(one_operation):
    assert hide_num_of_card(one_operation) == {"id": 2,
                                               "name": "Счет",
                                               "date": "2019-08-26T10:50:58.294041",
                                               "sender": "**8765",
                                               "to": "4456 78** **** 2354 ",
                                               "state": "EXECUTED"}
