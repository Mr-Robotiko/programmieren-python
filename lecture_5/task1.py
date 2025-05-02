def konkat(*kwargs):
    string: str = ""
    for x in kwargs:
        string += x
    return string


if __name__ == '__main__':
    print(konkat("D", "H", "B", "W"))
    print(konkat("Sonnen", "schein"))

