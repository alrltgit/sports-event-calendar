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
        sport_query = f"SELECT ID FROM Sports WHERE Name = \"{self.sport}\""
        competition_query = "INSERT INTO Competitions (Name, Sport_ID) VALUES (%s, %s)"
        venue_query = "INSERT INTO Venues (Name, Location) VALUES (%s, %s)"
        event_query = "INSERT INTO Events (Date_Time, Competition_ID, Venue_ID, Status) VALUES (%s, %s, %s, %s)"
        teams_query = "INSERT INTO Teams (Name, Description, Sport_ID) VALUES (%s, %s, %s)"
        participants_query = "INSERT INTO Event_Participants (Event_ID, Team_ID, Role) VALUES (%s, %s, %s)"

        sport_id = self.db.get_data(sport_query)

        competition_data = (self.competition, sport_id[0][0])
        self.db.add_data(competition_query, competition_data)
        competition_id = self.db.cursor.lastrowid

        venue_data =  (self.venue, "-")
        self.db.add_data(venue_query, venue_data)
        venue_id = self.db.cursor.lastrowid

        event_data = (self.date, competition_id, venue_id, self.status)
        self.db.add_data(event_query, event_data)
        event_id = self.db.cursor.lastrowid

        team_data = (self.team, self.team_description, sport_id[0][0])
        self.db.add_data(teams_query, team_data)
        team_id = self.db.cursor.lastrowid

        participants_data = (event_id, team_id, "-")
        self.db.add_data(participants_query, participants_data)


    def get_event(self, category, data):
        query = ""

        match category:
            case "date":
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
                    WHERE e.Date_Time = \"{data}\"
                    LIMIT 1
                    """
            case "competition":
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
                    WHERE c.Name = \"{data}\"
                    LIMIT 1
                    """
            case "venue":
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
                    WHERE v.Name = \"{data}\"
                    LIMIT 1
                    """
            case "status":
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
                    WHERE e.Status = \"{data}\"
                    LIMIT 1
                    """
            case _:
                print("Wrong category!")

        return self.db.get_data(query)
