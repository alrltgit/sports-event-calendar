from database import Database
from event import Event

def main():
    db = Database()

    event = Event(db, "2026-03-21 17:30:00", "World Cup", "Stadium", "live", "Football", "Poland")

    # event.insert_event()

    # records = event.get_events()
    # for record in records:
    #     print(record)

    # records = event.get_event("competition", "FIBA Europe Cup 2025-26")
    # records = event.get_event("date", "2026-04-14 17:30:00")
    # records = event.get_event("venue", "Prince Philip Hall")
    records = event.get_event("status", "finished")
    print(records)

    db.sports_events_db.close()

if __name__ == "__main__":
    main()
