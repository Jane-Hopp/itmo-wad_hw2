from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def root():
    return redirect(url_for("index"))

@app.route("/profile")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)