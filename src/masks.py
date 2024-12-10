from typing import Union
import logging


logging.basicConfig(
    filename='logs/masks.log',
    filemode='a+',
    format='%(levelname)s:%(name)s:Request time: %(asctime)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_hidden_card(card_number: Union[str]) -> Union[str]:
    """Принимает номер карты и выводит маску карты"""
    try:
        if len(card_number) != 16 or not card_number.isdigit():
            logger.error(f'Некорректный номер карты: {card_number}')
            return "Ошибка: некорректный номер карты"

        result = card_number[0:6] + 6 * "*" + card_number[-4:]
        result_split = (
            result[0:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:]
        )
        logger.info(f'Сгенерирована маска карты: {result_split}')  # Логирование успешного случая
        return result_split
    except Exception as e:
        logger.error(f'Ошибка в get_hidden_card: {str(e)}')  # Логирование ошибки
        return "Ошибка: произошла ошибка в обработке номера карты"

def returns_the_account_mask(account_number: Union[str]) -> Union[str]:
    """Принимает номер счета и возвращает маску счета"""
    try:
        if len(account_number) < 4 or not account_number.isdigit():
            logger.error(f'Некорректный номер счета: {account_number}')
            return "Ошибка: некорректный номер счета"

        masked_account = 2 * "*" + account_number[-4:]
        logger.info(f'Сгенерирована маска счета: {masked_account}')  # Логирование успешного случая
        return masked_account
    except Exception as e:
        logger.error(f'Ошибка в returns_the_account_mask: {str(e)}')  # Логирование ошибки
        return "Ошибка: произошла ошибка в обработке номера счета"

def main():
    # Пример использования функций
    card = "1234567812345678"
    account = "1234567890"
    print(get_hidden_card(card))
    print(returns_the_account_mask(account))

if __name__ == '__main__':
    main()