from flask import *



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/table")
def table():
    return render_template("tables-general.html")

@app.route("/chart")
def chart():
    return render_template("charts.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")



if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)