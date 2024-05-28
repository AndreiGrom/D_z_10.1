from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator:
    """Принимает список словарей с банковскими операциями, возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта.
    """

    transactions_by_currency = filter(
        lambda item: item["operationAmount"]["currency"]["code"] == currency,
        transactions_list,
    )
    for trans in transactions_by_currency:
        yield trans


def transaction_descriptions(list_inp: list[dict]) -> Generator:
    "Принимает список словарей и возвращает описание каждой операции по очереди"
    result = (v for i in list_inp for k, v in i.items() if k == "description")
    for i in result:
        yield i


def card_number_generator(start=1, stop=9999999999999999) -> Generator:
    "Uтенерирует номера карт в формате 0000 0000 0000 0000, диапазоны передаются как параметры генератора"
    while True:
        result = f"{start:016d}"
        yield result[:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:]
        start += 1
        if start == stop + 1:
            break