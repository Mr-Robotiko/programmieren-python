from datetime import time


def test_year(year: int):
    if (year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0)):
        print(f"{year} ist ein Schaltjahr")
    else:
        print(f"{year} ist kein Schaltjahr")


if __name__ == '__main__':
    year: int = int(input("Welches Jahr soll geprüft werden?\t"))
    test_year(year)
