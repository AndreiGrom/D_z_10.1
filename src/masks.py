
from typing import Union
import logging


logging.basicConfig(
    filename='mask.log',
    filemode='a+',
    format='%(levelname)s:%(name)s:Request time: %(asctime)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'  # этот формат удаляет микросекунды
)

logger = logging.getLogger('mask')  # Логгер с именем 'mask'
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_hidden_card(card_number: Union[str]) -> Union[str]:
    """Принимает номер карты и выводит маску карты"""
    result = card_number[0:6] + 6 * "*" + card_number[-4:]
    result_split = (
        result[0:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:]
    )
    logger.info(f'Сгенерирована маска карты: {result_split}')  # Логирование
    return result_split

def returns_the_account_mask(account_number: Union[str]) -> Union[str]:
    """Принимает номер счета и возвращает маску счета"""
    masked_account = 2 * "*" + account_number[-4:]
    logger.info(f'Сгенерирована маска счета: {masked_account}')
    return masked_account

def main():
    # Пример использования функций
    card = "1234567812345678"
    account = "1234567890"
    print(get_hidden_card(card))
    print(returns_the_account_mask(account))

if __name__ == '__main__':
    main()