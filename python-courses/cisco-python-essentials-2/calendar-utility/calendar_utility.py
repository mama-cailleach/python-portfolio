import calendar
import datetime
import os

class Event:
    def __init__(self, date, description):
        self.date = date  # datetime.date
        self.description = description

    def __str__(self):
        return f"{self.date} - {self.description}"

class CalendarManager:
    def __init__(self, events_file="events.txt"):
        self.events_file = events_file
        self.events = []
        self.load_events()

    def add_event(self, date_str, description):
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return
        event = Event(date, description)
        self.events.append(event)
        print(f"Added event: {event}")

    def list_events(self, date_str=None):
        if date_str:
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
            filtered = [e for e in self.events if e.date == date]
            if not filtered:
                print("No events found for that date.")
            for event in filtered:
                print(event)
        else:
            if not self.events:
                print("No events.")
            for event in sorted(self.events, key=lambda e: e.date):
                print(event)

    def save_events(self):
        with open(self.events_file, "w") as f:
            for event in self.events:
                f.write(f"{event.date},{event.description}\n")
        print("Events saved.")

    def load_events(self):
        self.events.clear()
        if not os.path.exists(self.events_file):
            return
        with open(self.events_file) as f:
            for line in f:
                try:
                    date_str, description = line.strip().split(",", 1)
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                    self.events.append(Event(date, description))
                except Exception:
                    continue

    def print_month(self, year, month):
        print("\n" + calendar.month(year, month))
        # Show events for this month
        events_month = [e for e in self.events if e.date.year == year and e.date.month == month]
        if events_month:
            print("Events this month:")
            for event in sorted(events_month, key=lambda e: e.date):
                print(f"  {event.date}: {event.description}")

    def print_year(self, year):
        print("\n" + calendar.calendar(year))
        # Show events for the year
        events_year = [e for e in self.events if e.date.year == year]
        if events_year:
            print("Events this year:")
            for event in sorted(events_year, key=lambda e: e.date):
                print(f"  {event.date}: {event.description}")

def main():
    cm = CalendarManager()
    while True:
        print("\n--- Calendar Utility CLI ---")
        print("1. Show month calendar")
        print("2. Show year calendar")
        print("3. Add event/reminder")
        print("4. List all events")
        print("5. List events for a date")
        print("6. Save events")
        print("7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            y = int(input("Year (e.g. 2025): "))
            m = int(input("Month (1-12): "))
            cm.print_month(y, m)
        elif choice == "2":
            y = int(input("Year (e.g. 2025): "))
            cm.print_year(y)
        elif choice == "3":
            date_str = input("Event date (YYYY-MM-DD): ").strip()
            desc = input("Event description: ").strip()
            cm.add_event(date_str, desc)
        elif choice == "4":
            cm.list_events()
        elif choice == "5":
            date_str = input("Date to list (YYYY-MM-DD): ").strip()
            cm.list_events(date_str)
        elif choice == "6":
            cm.save_events()
        elif choice == "7":
            cm.save_events()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
