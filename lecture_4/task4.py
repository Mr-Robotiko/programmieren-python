def kredit_tilgungsplan(kreditsumme, zinssatz, jahresrate, startjahr):
    restschuld = kreditsumme
    jahr = startjahr

    print("Berechnung des Tilgungsplans")
    print("-" * 30)
    while restschuld > 0:
        print(f"Jahr: {jahr}")
        zinsen = restschuld * (zinssatz / 100)

        if jahresrate <= zinsen:
            print("Warnung: Die Rückzahlung deckt nicht einmal die Zinsen. Schulden wachsen!")
            break

        tilgung = jahresrate - zinsen
        restschuld = round(restschuld - tilgung, 2)
        if restschuld < 0:
            tilgung += restschuld
            restschuld = 0.0

        print(f"Zinsen: {zinsen:.2f} EUR  Tilgung: {tilgung:.2f} EUR  Restschulden: {restschuld:.2f} EUR\n")
        jahr += 1

    print(f"Restforderung: {restschuld:.2f} EUR")


# Beispielwerte (kannst du durch Benutzereingaben ersetzen)
if __name__ == "__main__":
    startjahr = int(input("Startjahr: "))
    kreditsumme = float(input("Kreditsumme (EUR): "))
    zinssatz = float(input("Zinssatz (%): "))
    jahresrate = float(input("Jährliche Rückzahlung (EUR): "))

    kredit_tilgungsplan(kreditsumme, zinssatz, jahresrate, startjahr)
