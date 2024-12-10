
from unittest.mock import patch
import requests
from src.external_api import convert_currency

def api_urel(uzername):
    response = requests.get(f"https://api.apilayer.com/exchangerates_data/latest?base={from_currency}&symbols={to_currency}")
    return response.json()

@patch('requests.get')


def test_api_url(mock_get):
    mock_get.return_value.json.return_value = {'login':'testuser', 'name': 'Test user'}
    assert test_api_url('testures') == {'login':'testuser', 'name': 'Test user'}
    mock_get.assert_called_one_with('ttps://api.apilayer.com/exchangerates_data/latest?base={from_currency}&symbols={'
                                    'to_currency}')

