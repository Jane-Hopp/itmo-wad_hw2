from flask import Flask, render_template, redirect, url_for, request, session
import redis

app = Flask(__name__)
app.secret_key = 'da2c629492e7d5a31cd029fa4b95b6'

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('username', 'alice')
r.set('password', 'P@ssw0rd')

@app.route("/")
def root():
    return render_template("login.html")

@app.route("/profile")
def index():
    if ('username' in session) and (r.get('username').decode() in session['username']): 
        return render_template("index.html")
    return 'You need to log in'

@app.route("/login", methods=['POST'])
def login():
    if (request.form['username'] == r.get('username').decode()) and (request.form['pwd'] == r.get('password').decode()):
        session['username'] = request.form['username']
        return redirect(url_for("index"))
    return render_template("login.html", error='Wrong username or password. Try again')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)