from flask import Flask, render_template, request, redirect
from model_sqlite3 import SQLiteModel

app = Flask(__name__)
db = SQLiteModel("charities.db")  # Using SQLite3 database

@app.route("/")
def index():
    entries = db.get_all()
    return render_template("index.html", entries=entries)

@app.route("/add", methods=["POST"])
def add_entry():
    name = request.form["name"]
    description = request.form["description"]
    address = request.form["address"]
    service_type = request.form["service_type"]
    phone = request.form["phone"]
    hours = request.form["hours"]
    reviews = request.form["reviews"]

    db.insert(name, description, address, service_type, phone, hours, reviews)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
