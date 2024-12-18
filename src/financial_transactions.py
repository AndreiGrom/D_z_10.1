import pandas as pd
import csv


def read_transactions_from_csv(file_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла."""
    transactions = []
    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            transactions.append(row)
    return transactions


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """Считывает финансовые операции из Excel-файла."""
    transactions = pd.read_excel(file_path)
    return transactions.to_dict(orient="records")
