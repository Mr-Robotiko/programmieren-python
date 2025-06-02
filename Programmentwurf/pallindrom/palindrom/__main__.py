# Datei: palindrom/__init__.py

def is_palindrome(word: str) -> bool:
    word = word.lower()
    return word == word[::-1]


def main():
    while True:
        word = input("Wort eingeben (oder 'exit' zum Beenden): ").strip()
        if word.lower() == "exit":
            print("Programm beendet.")
            break

        if is_palindrome(word):
            print(f"{word} ist ein Palindrom.")
        else:
            print(f"{word} ist kein Palindrom.")


if __name__ == "__main__":
    main()
