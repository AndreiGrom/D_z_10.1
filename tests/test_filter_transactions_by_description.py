from src.main import filter_transactions_by_description

import pytest


@pytest.mark.parametrize('transactions,search_string,expected', [
    (
            [
                {'description': 'Purchase at Store A'},
                {'description': 'Payment to Store B'},
                {'description': 'Purchase at Store A again'}
            ],
            'Store A',
            [
                {'description': 'Purchase at Store A'},
                {'description': 'Purchase at Store A again'}
            ]
    ),
    (
            [
                {'description': 'Payment received'},
                {'description': 'Deposit to bank'},
                {'description': 'Payment completed'}
            ],
            'Payment',
            [
                {'description': 'Payment received'},
                {'description': 'Payment completed'}
            ]
    ),
    (
            [
                {'description': 'Grocery shopping'},
                {'description': 'Dining out'},
                {'description': 'Grocery sale'}
            ],
            'sale',
            [
                {'description': 'Grocery sale'}
            ]
    ),
    (
            [],
            'Store A',
            []
    )
])
def test_filter_transactions_by_description(transactions, search_string, expected):
    assert filter_transactions_by_description(transactions, search_string) == expected