from flask import Flask, request, session, render_template, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret"


@app.route("/")
def hello():
    return redirect("http://127.0.0.1:5000/v1/sanitized")


@app.route("/v1/sanitized", methods=['GET', 'POST'])
def login():
    result = [{"result": "sanitized"}, {"result": "unsanitized"}]
    if request.method == 'POST':
        userdata = request.form
        username = userdata['username']
        password = userdata['password']
        con = sqlite3.connect('accounts.db')
        cur = con.cursor()
        sql = 'SELECT * FROM accounts WHERE username = ? AND password = ?'
        cur.execute(sql, (username, password))
        account = cur.fetchone()
        # if account is None:
        #     return False
        if account:
            session['logged'] = True
            return result[0]
        else:
            return result[1]
    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
