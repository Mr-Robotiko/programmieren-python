from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = list()

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def get_books(self):
        return self.books

    def print(self):
        for i in self.books:
            print(f"Title: {i.title}\tAuthor: {i.title}")


if __name__ == '__main__':
    book1 = Book("Illuminati", "Dan Brown")
    book2 = Book("Das Symbol", "Dan Brown")

    lib = Library()
    lib.add_book(book1)
    lib.add_book(book2)

    lib.print()
