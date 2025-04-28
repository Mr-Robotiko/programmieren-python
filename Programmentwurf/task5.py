def create_report(**kwarg) -> None:
        print("================")
        for key, value in kwarg.items():
            print(f"{key}:\t{value}")


if __name__ == '__main__':
    create_report(Name="Thomas Müller", Alter=28, Hobbies="Radfahren, Lesen")
    create_report(Student="Max Mustermann", GPA=1.0, Ausbildungsfirma="ABC")
    create_report(Tier="Hund", Alter=5, Geräusch="Bellen")
    create_report(Farbe="rot", Alter=40, Ort="Hamburg", Art="selten")