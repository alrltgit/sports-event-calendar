INSERT INTO Events (ID, Date_Time, Competition_ID, Venue_ID, Status) VALUES
(1, "2026-04-14 17:30:00", 1, 1, "scheduled"),
(2, "2026-04-1", 2, 2, "scheduled"),
(3, "2026-04-1 18:15:00", 2, 3, "scheduled"),
(4, "2026-04-8", 2, 4, "scheduled"),
(5, "2025-11-23 08:50:00", 3, 5, "finished"),
(6, "2025-11-30 09:30:00", 3, 6, "finished"),
(7, "2026-03-20 14:00:00", 4, 7, "live"),
(8, "2026-06-11 08:00:00", 5, 8, "live");

INSERT INTO Teams (ID, Name, Description, Sport_ID) VALUES
(1, "Spar Girona", "-", 1),
(2, "Umana Reyer Venezia", "-", 1),
(3, "Falco Vulcano Energia KC Szombathely", "-", 1),
(4, "Surne Bilbao Basket", "-", 1),
(5, "PAOK BC", "-", 1),
(6, "UCAM Murcia", "-", 1),
(7, "PEZZO ROSOLA Patrik", "-", 2),
(8, "GRIGOLINI Filippo", "-", 2),
(9, "CINGOLANI Tommaso", "-", 2),
(10, "BOSIO Giovanni", "-", 2),
(11, "DELL'OLIO Francesco ", "-", 2),
(12, "DEVOS Victor ", "-", 2),
(13, "Nigeria", "-", 3),
(14, "Zimbabwe Under-19", "-", 3);

INSERT INTO Event_Participants (ID, Event_ID, Team_ID, Role) VALUES
(1, 1, 1, "-"),
(2, 1, 2, "-"),
(3, 2, 3, "-"),
(4, 2, 4, "-"),
(5, 3, 5, "-"),
(6, 3, 6, "-"),
(7, 4, 6, "-"),
(8, 4, 5, "-"),
(9, 5, 7, "-"),
(10, 5, 8, "-"),
(11, 5, 9, "-"),
(12, 5, 10, "-"),
(13, 5, 11, "-"),
(14, 6, 7, "-"),
(15, 6, 8, "-"),
(16, 6, 11, "-"),
(17, 6, 12, "-"),
(18, 7, 13, "-"),
(19, 7, 14, "-");

INSERT INTO Competitions (ID, Name, Sport_ID) VALUES
(1, "EuroLeague Women 2025-26", 1),
(2, "FIBA Europe Cup 2025-26", 1),
(3, "2025/26 Cyclo-Cross World Cup", 2),
(4, "Nigeria Invitational Women's T20I Tournament", 3),
(5, "FIFA World Cup 2026", 4);

INSERT INTO Sports (ID, Name) VALUES
(1, "Basketball"),
(2, "Cycling"),
(3, "Cricket"),
(4, "Football"),
(5, "MMA"),
(6, "Tennis");

INSERT INTO Venues (ID, Name, Location) VALUES
(1, "Prince Philip Hall", "Zaragoza, Spain"),
(2, "Schaeffler Arena Savaria", "Szombathely, Hungary"),
(3, "PAOK Sports Arena", "Thessaloniki, Greece"),
(4, "Palacio de los Deportes", "Murcia, Spain"),
(5, "-", "Tabor,  Czech Republic"),
(6, "-", "Flamanville,  France"),
(7, "Tafawa Balewa Square Cricket Oval", "Lagos, Nigeria"),
(8, "Guadalajara Stadium", "Zapopan, Mexico");
