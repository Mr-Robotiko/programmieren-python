class DivisibleBySeven:

    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.num <= 100:
            current = self.num
            self.num += 1
            if current % 7 == 0:
                return current
        raise StopIteration


if __name__ == '__main__':
    test = DivisibleBySeven()
    for i in test:
        print(i)