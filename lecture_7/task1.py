from dataclasses import dataclass

@dataclass
class Person:
    __slots__ = ["name", "age"]
    name: str
    age: int


if __name__ == '__main__':
    person1 = Person("Toboguko Gehrkomoto", 32)
    print(person1)