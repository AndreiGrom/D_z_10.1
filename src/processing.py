from typing import Optional
from datetime import datetime


def return_new_list(dictionary_list: list, state='CANCELED') -> Optional[list]:
    """принимает список и сортирует его по заданному значению"""
    return_list = []
    for i in dictionary_list:
        if i.get('state') == state:
            return_list.append(i)
    return return_list

