from typing import List


def main():
    colors: List[str] = ["Rot", "Grün", "Blau"]
    colors.remove("Grün")
    colors.insert(1, "Gelb")
    print(colors)


if __name__ == '__main__':
    main()
