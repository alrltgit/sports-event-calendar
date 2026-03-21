from flask import Flask, render_template
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

@app.route("/competitions")
def competitions():
    return render_template(competitions.html)

@app.route("/teams")
def teams():
    return render_template("teams.html")

db.sports_events_db.close()

if __name__ == "__main__":
    app.run()
