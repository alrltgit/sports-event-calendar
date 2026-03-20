DROP DATABASE IF EXISTS Sports_Events;
CREATE DATABASE Sports_Events;
USE Sports_Events;

CREATE TABLE Sports (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(45) NOT NULL
);

CREATE TABLE Venues (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(45) NOT NULL,
    Location VARCHAR(45) NOT NULL
);

CREATE TABLE Competitions (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Sport_ID INT NOT NULL,
    CONSTRAINT _fk_competitions_to_sport FOREIGN KEY (Sport_ID) REFERENCES Sports(ID)
);

CREATE TABLE Teams (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(45) NOT NULL,
    Description VARCHAR(100) NOT NULL,
    Sport_ID INT NOT NULL,
    CONSTRAINT _fk_teams_to_sport FOREIGN KEY (Sport_ID) REFERENCES Sports(ID)
);

CREATE TABLE Events (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Date_Time DATETIME NOT NULL,
    Competition_ID INT NOT NULL,
    Venue_ID INT NOT NULL,
    Status VARCHAR(20),
    CONSTRAINT _fk_events_to_competition FOREIGN KEY (Competition_ID) REFERENCES Competitions(ID),
    CONSTRAINT _fk_events_to_venue FOREIGN KEY (Venue_ID) REFERENCES Venues(ID),
    CONSTRAINT _chk_status CHECK (Status IN ("scheduled", "live", "finished"))
);

CREATE TABLE Event_Participants (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    Event_ID INT NOT NULL,
    Team_ID INT NOT NULL,
    Role VARCHAR(45),
    CONSTRAINT _fk_event_participants_to_event FOREIGN KEY (Event_ID) REFERENCES Events(ID),
    CONSTRAINT _fk_event_participants_to_team FOREIGN KEY (Team_ID) REFERENCES Teams(ID)
);
