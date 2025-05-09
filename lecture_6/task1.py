from typing import List


class ListExt(list):
    def __init__(self, items: List[int]):
        super().__init__(items)

    def range(self):
        return self[-1] - self[0]


if __name__ == '__main__':
    test = ListExt([1])
    test.append(8)
    test.append(11)
    print(test)
    print(test.range())

