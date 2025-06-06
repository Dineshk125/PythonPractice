## Static Method

from datetime import datetime


class Calendar:

    def __init__(self) -> None:
        self.events = []

    def add_events(self, new_event):
        self.events.append(new_event)

    def display_event(self):
        print(f"Event Name: {self.events}")

    @staticmethod
    def is_weekend(date: datetime):
        if date.weekday() > 4:
            print("Weekend")
        else:
            print("Weekday")


c1 = Calendar()
c1.add_events("DSA")
c1.display_event()


current = datetime.now()
c1.is_weekend(current)
