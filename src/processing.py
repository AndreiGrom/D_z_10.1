from typing import Optional



def return_new_list(dictionary_list: list, state='CANCELED') -> Optional[list]:
    """принимает список и сортирует его по заданному значению"""
    return_list = []
    for i in dictionary_list:
        if i.get('state') == state:
            return_list.append(i)
    return return_list


def get_sorted_list(dictionary_list: list,ascending=True) -> Optional[list]:
    """Принимает список и сортирует его по по убыванию даты"""
    sort = sorted(dictionary_list, key=lambda i: i.get('date', 0), reverse=ascending)
    return sort
