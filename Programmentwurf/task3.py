class Animal:
    def __init__(self, name: str, race: str):
        self._name = name
        self._race = race

    def get_name(self) -> str:
        return self._name

    def get_race(self) -> str:
        return self._race

    def __str__(self) -> str:
        return f"{self._name} the {self._race}"

    def __repr__(self) -> str:
        return self.__str__()


class Shelter:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, name, race):
        new_animal = Animal(name, race)
        self.animals.append(new_animal)
        print(f"{new_animal.get_name()} added to the shelter.")

    def show_animals(self):
        print("Shelter Animals:")
        for animal in self.animals:
            print(animal)


class DogExt(Animal):
    def __init__(self, name: str, size: int):
        super().__init__(name, "Dog")
        self._size = size

    def get_size(self) -> int:
        return self._size

    def __str__(self) -> str:
        return f"{self.get_name()} the {self.get_race()}, Size: {self._size} cm"

    def __repr__(self) -> str:
        return self.__str__()


# Nutzung der Klassen
if __name__ == '__main__':
    shelter = Shelter()
    shelter.add_animal("Fritz","Frog")
    shelter.add_animal("Karla", "Cat")
    shelter.show_animals()

# Erstellen eines DogExt-Objekts
my_dog = DogExt("Buddy", 50)
# Ausgabe des Dog-Objekts
print(my_dog)