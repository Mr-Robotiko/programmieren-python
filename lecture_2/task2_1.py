
def plan_holiday() -> float:
    print("Kostenplan für eine Reise")
    print("=========================")
    persons: int = int(input("Wie viele Personen gibt es?\t"))
    costs_hostel: float = float(input("Wie hoch sind die Hostelkosten pro Person?\t"))
    costs_bus: float = float(input("Wie hoch sind die Buskosten?\t"))
    costs_events: float = float(input("Wie hoch sind die Eventkosten?\t"))
    total_cost: float = (persons * costs_hostel) + costs_bus + costs_events
    print(f"Die Gesamtkosten betragen: {total_cost} EUR")


if __name__ == '__main__':
    plan_holiday()