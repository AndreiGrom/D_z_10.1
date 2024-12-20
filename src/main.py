import csv
import json
import re
from collections import Counter

import pandas as pd


def filter_transactions_by_description(transactions: list, search_string: str) -> list:
    """
    Фильтрует транзакции по заданной строке поиска в описании.
    """

    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [
        transaction
        for transaction in transactions
        if pattern.search(transaction["description"])
    ]


def count_transactions_by_category(transactions: list, categories: list) -> dict:
    """
    Подсчитывает количество транзакций для каждой заданной категории.

    Возвращает:
    dict: Словарь, где ключи - категории, а значения - количество транзакций в каждой категории.
    """
    category_count = Counter()

    for transaction in transactions:
        for category in categories:
            if category in transaction["description"]:
                category_count[category] += 1

    return dict(category_count)


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        file_path = input(
            "Программа: Для обработки выбран JSON-файл. Введите путь к файлу: "
        )
        with open(file_path, "r") as file:
            transactions = json.load(file)

    elif choice == "2":
        file_path = input(
            "Программа: Для обработки выбран CSV-файл. Введите путь к файлу: "
        )
        with open(file_path, "r") as file:
            transactions = list(csv.DictReader(file))

    elif choice == "3":
        file_path = input(
            "Программа: Для обработки выбран XLSX-файл. Введите путь к файлу: "
        )
        transactions = pd.read_excel(file_path).to_dict(orient="records")

    else:
        print("Программа: Неверный выбор. Пожалуйста, попробуйте снова.")
        return

    status = (
        input(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:"
            " EXECUTED, CANCELED, PENDING\nПользователь: "
        )
        .strip()
        .lower()
    )

    valid_statuses = {"executed", "canceled", "pending"}
    if status not in valid_statuses:
        print(f'Программа: Статус операции "{status}" недоступен.')
        return

    filtered_transactions = [
        transaction
        for transaction in transactions
        if transaction["status"].lower() == status
    ]

    print(f'Программа: Операции отфильтрованы по статусу "{status.upper()}"')

    if not filtered_transactions:
        print(
            "Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации."
        )
        return

    sort_by_date = (
        input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if sort_by_date == "да":
        order = (
            input(
                "Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: "
            )
            .strip()
            .lower()
        )
        if order == "по возрастанию":
            filtered_transactions.sort(key=lambda x: x["date"])
        elif order == "по убыванию":
            filtered_transactions.sort(key=lambda x: x["date"], reverse=True)

    only_rub_transactions = (
        input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if only_rub_transactions == "да":
        filtered_transactions = [
            transaction
            for transaction in filtered_transactions
            if transaction["currency"] == "RUB"
        ]

    filter_by_description = (
        input(
            "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
        )
        .strip()
        .lower()
    )
    if filter_by_description == "да":
        search_string = input("Введите слово для фильтрации: ")
        filtered_transactions = filter_transactions_by_description(
            filtered_transactions, search_string
        )

    print("Программа: Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in filtered_transactions:
        # Форматирование вывода
        print(
            f"{transaction['date']} {transaction['description']}\nСчет {transaction['account']}\nСумма:"
            f" {transaction['amount']} {transaction['currency']}\n"
        )


if __name__ == "__main__":
    main()
