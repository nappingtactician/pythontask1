from flask import Flask, request, session, redirect, render_template, jsonify,make_response
import sqlite3
import json

app = Flask(__name__)
app.secret_key = "super_secret"


@app.route("/")
def hello():
    return redirect("http://127.0.0.1:5000/v1/sanitized")


@app.route("/v1/sanitized", methods=['GET', 'POST'])
def payload():
    result = [{"result": "sanitized"}, {"result": "unsanitized"}]
    if request.method == 'POST':
        data = request.get_json(force=True)
        username = data["username"]
        password = data["password"]
        con = sqlite3.connect('accounts.db')
        cur = con.cursor()
        sql = 'SELECT * FROM accounts WHERE username = ? AND password = ?'
        cur.execute(sql, (username, password))
        account = cur.fetchone()
        if account:
            session['logged'] = True
            return jsonify(result[0])
        else:
            return jsonify(result[1])

    con = sqlite3.connect('accounts.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM accounts WHERE username = 'pranal@gmail.com' AND password = 'pranal123'")

    return jsonify(result[0])


if __name__ == '__main__':
    app.debug = True
    app.config['TESTING'] = True
    app.run()
