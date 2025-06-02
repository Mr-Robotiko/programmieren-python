from typing import List


def is_palindrome(word):
    reversed_word = ""
    len_word = len(word) * -1
    while len_word < 0:
        reversed_word += word[len_word]
        len_word += 1
    return word == reversed_word



def main():
    while True:
        word = "regallager" #input()
        if is_palindrome(word):
            print(f"{word} ist ein Palindrom.")
        else:
            print(f"{word} ist kein Palindrom.")


if __name__ == "__main__":
    main()