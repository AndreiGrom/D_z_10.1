import pytest
from collections import Counter


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


# Тесты для count_transactions_by_category
@pytest.mark.parametrize('transactions, categories, expected', [
    (
        [
            {"description": "Shopping - Clothes"},
            {"description": "Shopping - Groceries"},
            {"description": "Shopping - Clothes"},
            {"description": "Utilities - Internet"},
        ],
        ["Shopping", "Utilities"],
        {"Shopping": 3, "Utilities": 1},
    ),
    (
        [
            {"description": "Dining - Restaurant"},
            {"description": "Dining - Fast Food"},
            {"description": "Groceries - Supermarket"},
        ],
        ["Dining", "Groceries"],
        {"Dining": 2, "Groceries": 1},
    ),
    (
        [
            {"description": "Travel - Airfare"},
            {"description": "Travel - Hotel"},
            {"description": "Entertainment - Movies"},
        ],
        ["Travel"],
        {"Travel": 2},
    ),
    (
        [
            {"description": "Sports - Gym"},
            {"description": "Sports - Equipment"},
        ],
        ["Shopping"],
        {},
    ),
])
def test_count_transactions_by_category(transactions, categories, expected):
    assert count_transactions_by_category(transactions, categories) == expected