from typing import Union


def get_hidden_card(card_number: Union[str]) -> Union[str]:
    """Принимает номер карты и выводита маску карты"""
    result = card_number[0:6] + 6 * "*" + card_number[-4:]
    result_split = (
        result[0:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:]
    )
    return result_split


def returns_the_account_mask(account_number: Union[str]) -> Union[str]:
    """Принимает номер счета и возвращающей маску счета"""
    return 2 * "*" + account_number[-4:]