import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("api_key")


def convert_currency(amount, from_currency, to_currency, api_key):
    # Убедитесь, что валюта поддерживается
    supported_currencies = ["USD", "EUR"]
    if (
        from_currency not in supported_currencies
        or to_currency not in supported_currencies
    ):
        raise ValueError("Поддерживаемые  валюты USD и EUR.")

    # Формируем URL для запроса
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={from_currency}&symbols={to_currency}"

    headers = {
        "apikey": api_key,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на наличие ошибок
        data = response.json()

        # Получаем курс
        exchange_rate = data["rates"].get(to_currency)
        if exchange_rate is None:
            raise ValueError(f"Не удалось найти обменный курс для {to_currency}")

        # Конвертируем
        converted_amount = amount * exchange_rate
        return converted_amount

    except requests.exceptions.RequestException as e:
        print(f"Не удалось выполнить HTTP-запрос : {e}")
        return None
    except ValueError as e:
        print(e)
        return None


# Пример использования функции
api_key = os.getenv("api_key")
amount_to_convert = 100  # сумма в USD
from_curr = "USD"
to_curr = "EUR"

converted_value = convert_currency(amount_to_convert, from_curr, to_curr, api_key)
if converted_value is not None:
    print(f"{amount_to_convert} {from_curr} is {converted_value:.2f} {to_curr}")
