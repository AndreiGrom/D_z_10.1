date = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
    }
]


def tranzaction_summ(list):
    for i in list:
        if i["operationAmount"]["currency"]["code"] == "RUB":
            return float(i["operationAmount"]["amount"])


print(tranzaction_summ(date))
