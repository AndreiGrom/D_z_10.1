from src.masks import get_hidden_card,returns_the_account_mask
import pytest


def test_get_hidden_card():
    result = '7000 79** **** 6361'
    spl = '7000792289606361'
    assert get_hidden_card(spl) == result

@pytest.mark.parametrize('value,expected',[
    ('7000792289606361', '7000 79** **** 6361'),
    ('1234567890123456', '1234 56** **** 3456'),
    ('asdfghjklqwertyu', 'asdf gh** **** rtyu'),
    ])

def test_get_hidden_card_(value, expected):
    assert get_hidden_card(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('73654108430135874305', '**4305'),
])

def test_returns_the_account_mask(value, expected):
    assert returns_the_account_mask(value) == expected
