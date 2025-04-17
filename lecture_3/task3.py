from typing import List
import random as r


def define_list(limit: int, max: int = 100) -> List[int]:
    l: List = list()
    for i in range(limit):
        l.append(r.randint(1, max))
    return l


def merge_lists(limit: int, max: int = 100) -> List[int]:
    list_1: List[int] = define_list(5)
    print(f"{list_1 = }")
    list_2: List[int] = define_list(5)
    print(f"{list_2 = }")
    merged_list: List[int] = list_1 + list_2
    return merged_list


if __name__ == '__main__':
    merge_list: List[int] = merge_lists(5)
    print(sorted(merge_list))