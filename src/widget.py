from datetime import datetime
from typing import Optional


def account_details(user_input: str) -> Optional[str]:
    """Принимает информацию о счете или карте и возвращает его маску"""
    if user_input[-20:].isdigit():
        return user_input[:5] + "**" + user_input[-4:]
    else:
        mask = (
            user_input.replace(user_input[-10:], len(user_input[-10:-4]) * "*")
            + user_input[-4:]
        )
        result = (
            mask[:-16]
            + mask[-16:-12]
            + " "
            + mask[-12:-8]
            + " "
            + mask[-8:-4]
            + " "
            + mask[-4:]
        )
        return result


def format_date(date_time_str: str) -> str:
    """Принемает строку с датой и возвращает его в виде 11.07.2018"""
    short_date = date_time_str.split("T")[0]

    return str(datetime.strptime(short_date, "%Y-%m-%d").strftime("%d.%m.%Y"))


print(account_details("Visa Platinum 7000792289606361"))
