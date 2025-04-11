from cheksum import checksum


def main():
    isbn: str = str(input("Wie lautet die ISBN?\t"))
    number: int = checksum(isbn)
    print(f"Die Prüfziffer lautet: {number}")


if __name__ == '__main__':
    main()