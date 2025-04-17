from typing import Tuple


def main():
    t: Tuple = (1,2,3,4)
    for i in t:
        print(t[i-1])


if __name__ == '__main__':
    main()