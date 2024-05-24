def filter_by_currency(transactions, valut="USD"):
    usd = []
    for k in transactions:
        for i, v in k.items():
            if i["currency"] == valut:
                usd.append(i)


def transaction_descriptions(list_inp):
    result = (v for i in list_inp for k, v in i.items() if k == "description")
    return result


def card_number_generator(start=1, stop=9999999999999999):
    while True:
        result = f"{start:016d}"
        yield result[:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:]
        start += 1
        if start == stop + 1:
            break
