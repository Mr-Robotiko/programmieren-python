def voting_system():
    candidates = {
        "Miriam": 0,
        "Andreas": 0,
        "Tim": 0
    }

    has_voted = False
    while not has_voted:
        print("\nKandidaten:")
        for name in candidates:
            print(name)

        choice = input("Stimme für Kandidat(in): ")

        if choice in candidates:
            candidates[choice] += 1
            print(f"Danke für die Wahl von {choice}!")
            has_voted = True
        else:
            print("Kein gültiger Kandidat.")

    print("\nAktuelle Stimmen:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes}")

    print("\nVielen Dank für Ihre Teilnahme!")
    exit(0)


if __name__ == '__main__':
    voting_system()
