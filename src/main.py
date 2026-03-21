from database import Database
from event import Event

def main():
    db = Database()

    # event = Event("2026-03-21 17:30:00", 1, 1, "live")
    # db.add_data(event)

    data = db.get_data()
    for event in data:
        print(event)

    db.sports_events_db.close()

if __name__ == "__main__":
    main()
