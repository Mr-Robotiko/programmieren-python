from dataclasses import dataclass

@dataclass(frozen = True)
class Car:
    brand: str
    model: str