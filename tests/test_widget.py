from src.widget import account_details, format_date
import pytest


def test_account_details():
    user_inp = 'Счет 73654108430135874305'
    result = 'Счет **4305'
    assert account_details(user_inp) == result


@pytest.mark.parametrize('value, expected',[
    ('2018-07-11T02:26:18.671407', '11.07.2018'),
    ('2018-07-12T02:45:18.671407', '12.07.2018'),
    ('2024-11-11T02:45:18.671407', '11.11.2024')

])


def test_format_date(value,expected):
    assert format_date(value) == expected

