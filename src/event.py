class Event:
    def __init__(self, db, date=None, competition=None, venue=None, status=None, sport=None, team=None, location=None, team_description=None):
        self.date = date
        self.competition = competition
        self.venue = venue
        self.location = location
        self.status = status
        self.sport = sport
        self.team = team
        self.team_description = team_description
        self.db = db

    def get_events(self):
        query = """
            SELECT
                c.Name AS competition,
                e.Date_Time AS date, 
                s.Name AS sport,
                v.Name AS venue,
                v.Location AS location,
                e.Status AS status,
                GROUP_CONCAT(t.Name SEPARATOR ' vs ') AS participants
            FROM Events e
            JOIN Competitions c
                ON e.Competition_ID = c.ID
            JOIN Venues v
                ON e.Venue_ID = v.ID
            JOIN Event_Participants p
                ON e.ID = p.Event_ID
            JOIN Teams t
                ON t.ID = p.Team_ID
            JOIN Sports s
                ON t.Sport_ID = s.ID
            GROUP BY e.ID, c.Name, s.Name, v.Name, v.Location, e.Status;
            """

        return self.db.get_data(query)

    def insert_event(self):
        sport_query = "SELECT ID FROM Sports WHERE Name = :sport"
        competition_query = "INSERT INTO Competitions (Name, Sport_ID) VALUES (:competition, :sport_id)"
        venue_query = "INSERT INTO Venues (Name, Location) VALUES (:venue, :location)"
        event_query = """
            INSERT INTO Events (Date_Time, Competition_ID, Venue_ID, Status)
            VALUES (:date, :competition_id, :venue_id, :status)
        """
        teams_query = """
            INSERT INTO Teams (Name, Description, Sport_ID)
            VALUES (:team, :team_description, :sport_id)
        """
        participants_query = """
            INSERT INTO Event_Participants (Event_ID, Team_ID, Role)
            VALUES (:event_id, :team_id, :role)
        """

        sport_id = self.db.get_data(sport_query, {"sport": self.sport})

        if not sport_id:
            add_sport_query = "INSERT INTO Sports (Name) VALUES (:sport)"
            self.db.add_data(add_sport_query, {"sport": self.sport})

            sport_id = self.db.get_data(sport_query, {"sport": self.sport})

        competition_data = {"competition": self.competition, "sport_id": sport_id[0][0]}
        competition_id = self.db.add_data(competition_query, competition_data)

        venue_data = {"venue": self.venue, "location": self.location}
        venue_id = self.db.add_data(venue_query, venue_data)

        event_data = {
            "date": self.date,
            "competition_id": competition_id,
            "venue_id": venue_id,
            "status": self.status,
        }
        event_id = self.db.add_data(event_query, event_data)

        team_data = {
            "team": self.team,
            "team_description": self.team_description,
            "sport_id": sport_id[0][0],
        }
        team_id = self.db.add_data(teams_query, team_data)

        participants_data = {"event_id": event_id, "team_id": team_id, "role": "-"}
        self.db.add_data(participants_query, participants_data)


    def get_event(self, category, data):
        filters = {
            "date": "e.Date_Time",
            "competition": "c.Name",
            "venue": "v.Name",
            "status": "e.Status",
        }
        filter_column = filters.get(category)
        if not filter_column:
            raise ValueError("Invalid event category")

        query = f"""
            SELECT
                c.Name,
                e.Date_Time, 
                s.Name,
                v.Name,
                v.Location,
                e.Status,
                t.Name 
            FROM Events e
            JOIN Competitions c
                ON e.Competition_ID = c.ID
            JOIN Venues v
                ON e.Venue_ID = v.ID
            JOIN Event_Participants p
                ON e.ID = p.Event_ID
            JOIN Teams t
                ON t.ID = p.Team_ID
            JOIN Sports s
                ON t.Sport_ID = s.ID
            WHERE {filter_column} = :data
            LIMIT 1
            """

        return self.db.get_data(query, {"data": data})
