
def print_bakterien(d: int = 2):
    amount: int = 100
    min: int = d * 24 * 60
    h: int = 0
    print("================ Vermehrung von Bakterien ================")
    while min >= 0:
        print(f"Stunde: {h}\t Bakterien: {amount}")
        min -= 60
        h += 1
        amount = 4 * amount


if __name__ == '__main__':
    print_bakterien()


