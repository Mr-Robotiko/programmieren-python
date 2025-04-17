from typing import List
import random as r


def sum():
    l: List = list()
    sum: int = 0
    for i in range(5):
        l.append(r.randint(1, 500))
        print(f"{l[i]}")
        sum += l[i]
    print(f"{sum = }")


if __name__ == '__main__':
    sum()