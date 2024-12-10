import os
import json
from typing import Any
import logging

logging.basicConfig(
    filename='logs/utils.log',
    filemode='a+',
    format='%(levelname)s:%(name)s:Request time: %(asctime)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'  # Этот формат удаляет микросекунды
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_processing(path_file: str) -> Any:
    """Обработка транзакций. На вход функция принимает путь до файла с транзакциями в формате .json
    и возвращает в виде списка. Если файл пустой или не содержит список транзакций возвращает пустой список."""

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path_file = os.path.join(base_dir, "data", path_file)

    logger.info(f'Попытка открыть файл: {full_path_file}')

    try:
        with open(full_path_file, encoding="utf-8") as file_json:
            data = json.load(file_json)
            logger.info(f'Файл успешно загружен: {path_file}')
    except FileNotFoundError:
        logger.error(f'Файл не найден: {full_path_file}')
        return []
    except json.JSONDecodeError:
        logger.error(f'Ошибка декодирования JSON в файле: {full_path_file}')
        return []
    except Exception as e:
        logger.error(f'Неожиданная ошибка: {type(e).__name__} - {str(e)}')
        return []

    if isinstance(data, list):
        return data
    else:
        logger.warning(f'Данные в файле не являются списком: {full_path_file}')
        return []



path_file_operations = "operations.json"
path_file_empty = "empty.json"
path_file_test = "utils_test.json"

print(transaction_processing(path_file_test))

