from flask import Flask, render_template, jsonify
from database import Database
from event import Event

app = Flask(
    __name__,
    template_folder = "../templates",
    static_folder = "../static"
)

db = Database()
events_table = Event(db)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/api/events")
def get_data():
    events = events_table.get_events()

    records = []
    for record in events:
        records.append({
            "competition": record[0],
            "date": record[1].isoformat(),
            "sports": record[2],
            "venue": record[3],
            "location": record[4],
            "status": record[5],
            "team": record[6]
        })
    return jsonify(records)

@app.route("/competitions")
def competitions():
    return render_template("competitions.html")

@app.route("/teams")
def teams():
    return render_template("teams.html")

# db.sports_events_db.close()

if __name__ == "__main__":
    app.run()
