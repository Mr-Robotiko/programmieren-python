from typing import List


def even_numbers(n):
    num : int = 0
    even_numbers: List[int] = list()
    while len(even_numbers) < n:
        if num % 2 == 0:
            yield num
            even_numbers.append(num)
        num +=1


if __name__ == '__main__':
    for even in even_numbers(5):
        print(even)