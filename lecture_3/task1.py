from typing import List, Any


def main():
    l: List = list()
    for i in range(3):
        l.append(input("Was ist der zu initialisierende Wert:\t"))
    print(l)


if __name__ == '__main__':
    main()