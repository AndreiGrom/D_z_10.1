from src.processing import return_new_list,get_sorted_list
import pytest

def test_return_new_list(input_dickt,state):
    new_dickt = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert return_new_list(input_dickt,state) == new_dickt


def test_return_new_list_value_error(input_dickt, state):
    new_dickt = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert return_new_list(input_dickt, state) == new_dickt

    with pytest.raises(TypeError):
        return_new_list(0, '')


def test_get_sorted_list(input_dickt, ascending):

    sort_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert get_sorted_list(input_dickt,ascending) == sort_list

def test_get_sorted_list_type_error(input_dickt, ascending):
    sort_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert get_sorted_list(input_dickt, ascending) == sort_list

    with pytest.raises(TypeError):
         get_sorted_list(0,'True')


@pytest.mark.parametrize('value, state, expected',[
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
     'EXECUTED',[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
     )])


def test_return_new_list(value,state,expected):
    assert return_new_list(value,state) == expected