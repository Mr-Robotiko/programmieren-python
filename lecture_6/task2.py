from typing import Dict


class Laenge:
    __meter: Dict[str, float] = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "yd": 0.9143}

    def __init__(self, value: float, unit: str):
        self.value: int = value
        self.unit: str = unit

    def getMeter(self):
        return self.value * Laenge.__meter[self.unit]

    def __add__(self, other):
        sum_in_meter: int = self.getMeter() + other.getMeter()
        sum: float = sum_in_meter / Laenge.__meter[self.unit]
        return Laenge(sum, self.unit)

    def __str__(self):
        return f"{self.value:.2f}[{self.unit}]"


if __name__ == '__main__':
    print(Laenge(34, "cm") + Laenge(12, "m"))
    a = Laenge(34, "cm") + Laenge(12, "m")
    print(a)
