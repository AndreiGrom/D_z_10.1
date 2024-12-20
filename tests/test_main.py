from src.main import main
import json
import pandas as pd
from unittest.mock import patch, mock_open


@patch('builtins.input', side_effect=[
    '1',  # Выбор JSON
    'path/to/transactions.json',  # Путь к файлу
    'executed',  # Статус
    'да',  # Сортировка по дате
    'по возрастанию',  # Порядок сортировки
    'да',  # Выводить только рублевые транзакции
    'да',  # Фильтрация по описанию
    'тест'  # Слово для фильтрации
])
@patch('builtins.print')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps([
    {"date": "2023-01-01", "description": "Тестовая транзакция", "account": "Счет 1", "amount": 1000, "currency": "RUB", "status": "executed"},
    {"date": "2023-01-02", "description": "Тестовая транзакция 2", "account": "Счет 2", "amount": 2000, "currency": "USD", "status": "executed"},
    {"date": "2023-01-03", "description": "Тестовая транзакция 3", "account": "Счет 3", "amount": 1500, "currency": "RUB", "status": "canceled"},
]))
def test_main_json(mock_open, mock_print, mock_input):
    main()
    mock_print.assert_any_call('Программа: Операции отфильтрованы по статусу "EXECUTED"')
    mock_print.assert_any_call('Программа: Распечатываю итоговый список транзакций...')
    assert mock_print.call_count > 0  # Проверяем, что что-то было напечатано

@patch('builtins.input', side_effect=[
    '2',  # Выбор CSV
    'path/to/transactions.csv',  # Путь к файлу
    'canceled',  # Статус
    'нет',  # Сортировка по дате
    'нет',  # Выводить только рублевые транзакции
    'нет'  # Фильтрация по описанию
])
@patch('builtins.print')
@patch('builtins.open', new_callable=mock_open, read_data='date,description,account,amount,currency,status\n2023-01-01,Тестовая транзакция,Счет 1,1000,RUB,executed\n2023-01-02,Тестовая транзакция 2,Счет 2,2000,USD,canceled\n')
def test_main_csv(mock_open, mock_print, mock_input):
    main()
    mock_print.assert_any_call('Программа: Операции отфильтрованы по статусу "CANCELED"')
    mock_print.assert_any_call('Программа: Распечатываю итоговый список транзакций...')
    assert mock_print.call_count > 0  # Проверяем, что что-то было напечатано

@patch('builtins.input', side_effect=[
    '3',  # Выбор XLSX
    'path/to/transactions.xlsx',  # Путь к файлу
    'executed',  # Статус
    'да',  # Сортировка по дате
    'по убыванию',  # Порядок сортировки
    'нет',  # Выводить только рублевые транзакции
    'нет'  # Фильтрация по описанию
])
@patch('builtins.print')
@patch('pandas.read_excel', return_value=pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02'],
    'description': ['Тестовая транзакция', 'Тестовая транзакция 2'],
    'account': ['Счет 1', 'Счет 2'],
    'amount': [1000, 2000],
    'currency': ['RUB', 'USD'],
    'status': ['executed', 'executed']
}))
def test_main_xlsx(mock_read_excel, mock_print, mock_input):
    main()
    mock_print.assert_any_call('Программа: Операции отфильтрованы по статусу "EXECUTED"')
    mock_print.assert_any_call('Программа: Распечатываю итоговый список транзакций...')
    assert mock_print.call_count > 0