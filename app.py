from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Habit tracker - Home")


@app.route('/add', methods=["GET", "POST"])
def add_habit():
    return render_template("add_habit.html", title="Habit Tracker - Add Habit")


if __name__ == '__main__':
    app.run()
