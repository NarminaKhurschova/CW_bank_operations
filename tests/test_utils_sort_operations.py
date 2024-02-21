import pytest
from utils.sort_operations import get_executed_operations, few_last_operations, replace_num_to_symb


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


def test_replace_num_to_symb(num_acc, num_card):
    assert replace_num_to_symb(num_acc) == ["*", "*", "*", "*", "*", "*", "*", "*", "*",
                                            "*", "*", "*", "*", "*", "*", "*", "8", "7", "6", "5"]
    assert replace_num_to_symb(num_card) == ["4", "4", "5", "6", "7", "8", "*", "*", "*", "*"
                                                , "*", "*", "2", "3", "5", "4"]
