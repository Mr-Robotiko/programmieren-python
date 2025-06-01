# aufgabe_04
# |__ aufgabe_04.py
# |__ lipsum.txt
import sys
from typing import Dict, List


def count_letters(filename) -> Dict[str, int]:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower() # Konvertierung zu Kleinbuchstaben
    except FileNotFoundError:
        print(f"Die Datei {filename} wurde nicht gefunden.")
        return {}
    letter_count: Dict[str, int] = {}
    for char in content:
        if char.isalpha(): # Prüfen, ob das Zeichen ein Buchstabe ist
            amount: int = 0
            for i in content:
                if i == char:
                    amount += 1
                else:
                    continue
                letter_count[char] = amount
        else:
            continue
    return letter_count


def display_graph(letter_counts: Dict[str, int]):
    chars = letter_counts.keys()
    sorted_chars = sorted(chars)
    for char in sorted_chars:
        amount = letter_counts[char]
        graph = amount * "#"
        print(f"{char}:\t{amount}\t{graph}")


def display_statics(letter_counts: Dict[str, int]):
    maximum: int = 0
    max_char: str = ""
    minimum: int = 10
    min_char = ""
    sum: float = 0
    length: int = 0
    for char, amount in letter_counts.items():
        if amount > maximum:
            maximum = amount
            max_char = char
        if amount < minimum:
            minimum = amount
            min_char = char
        sum += amount
        length += 1

    averge = sum/length

    print(f"Maximale Buchstabenhäufigkeit: {maximum}")
    print(f"Minimale Buchstabenhäufigkeit: {minimum}")
    print(f"Durchschnittliche Buchstabenhäufigkeit: {averge:.2f}")
    print(f"Buchstaben mit maximaler Häufigkeit: {max_char}")
    print(f"Buchstaben mit minimaler Häufigkeit: {min_char}")


def main():
    if len(sys.argv) != 2:
        print("Bitte geben Sie genau einen Dateipfad als Argument an.")
        return
    filename = "lipsum.txt"
    letter_count = count_letters(filename)
    display_graph(letter_count)
    display_statics(letter_count)


if __name__ == '__main__':
    main()
