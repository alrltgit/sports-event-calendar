from flask import Flask, render_template, jsonify, request
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

@app.route("/api/post_events", methods=['POST'])
def post_data():
    data = request.get_json()
    new_event = Event(db,
        date=data['date'],
        competition=data['competition'],
        venue=data['venue'],
        status=data['status'],
        sport=data['sport'],
        team=data['participants'],
        location=data['location']
    )

    new_event.insert_event()
    return jsonify({"message": "Event added successfully"}, 200)

if __name__ == "__main__":
    app.run()
