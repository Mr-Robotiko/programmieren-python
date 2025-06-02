from typing import Dict


def voting_system():
    candidates: Dict[str, int] = dict()
    print("Wählen sie, indem sie die Namen eingeben")
    has_voted = False
    while not has_voted:
        candidate: str = input("Kandidat: \tPress ENT to continue\t")
        amount: int = 1
        if candidate == "":
            has_voted = True
        if candidate in candidates:
            candidates[candidate] += amount
        else:
            candidates[candidate] = amount


    while True:
        print("\nKandidaten:")
        print(candidates.keys())
        print("\nAktuelle Stimmen:")
        for candidate, votes in candidates.items():
            print(f"{candidate}: {votes}")
        break


if __name__ == '__main__':
    voting_system()

