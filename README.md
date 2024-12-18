# Домашка по уроку 10.1

## Описание:
В домашних условиях реализованы две функции:
функция `return_new_list`«принимает список и сортирует его 
по заданному результату», 
функция `get_sorted_list`«принимает список и сортирует его
по убыванию дат».В проект добавлен модуль generators, в нем 
реализованы функции: 

`filter_by_currency`"""Принимает список 
словарей с банковскими операциями, возвращает итератор,
    который выдает по очереди операции, в которых указана 
заданная валюта.
    """

Функция `transaction_descriptions`  "Принимает список 
словарей и возвращает описание каждой операции по очереди"

Фунция `card_number_generator` "Uтенерирует номера карт в 
формате 0000 0000 0000 0000, диапазоны передаются как 
параметры генератора"

Декоратор `log` логирует вызов функции
    и ее результат выводит в файл или в консоль


Функции покрыты  тестами с помощью 
фреймворка pytest.

## Установка:
1.Клонируйте репозитории:
```
git clone https://github.com/AndreiGrom/D_z_10.1.git
```

2.Устоновите в зависимости:
```
pip install requests
```
## Использование
1.Выберите функцию, которую хотите использовать. 

2.В аргументах функции передайте значения, 
которые хотите использовать в других странах.

## Использование pytest

1.В терменале ввести команду "pytest".

2.Чтобы запустить тесты с оценкой 
покрытия в терменале ввести команду "pytest --cov".


```markdown
# Финансовые операции

Этот проект содержит функции для считывания финансовых операций из CSV и Excel файлов.

## Установка

Для начала, убедитесь, что у вас установлены необходимые зависимости. Используйте следующую команду:

```bash
pip install pandas openpyxl
```

## Функции

Проект включает следующие функции для чтения финансовых операций:

### `read_transactions_from_csv(file_path: str) -> list[dict]`

Эта функция считывает финансовые операции из указанного CSV-файла.

- **Аргумент**:
  - `file_path` (str): Путь к CSV-файлу.
  
- **Возвращает**:
  - `list[dict]`: Список словарей с транзакциями.

#### Пример использования:

```python
transactions = read_transactions_from_csv('path/to/your/transactions.csv')
print(transactions)
```

### `read_transactions_from_excel(file_path: str) -> list[dict]`

Эта функция считывает финансовые операции из указанного Excel-файла.

- **Аргумент**:
  - `file_path` (str): Путь к Excel-файлу.
  
- **Возвращает**:
  - `list[dict]`: Список словарей с транзакциями.

#### Пример использования:

```python
transactions = read_transactions_from_excel('path/to/your/transactions.xlsx')
print(transactions)
```

## Примечания

- Убедитесь, что ваши CSV и Excel файлы содержат корректные данные и соответствуют ожидаемому формату.
- Для работы с Excel файлами необходима библиотека `openpyxl`.

```