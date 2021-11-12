from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__, template_folder='templates')
'''
con = sqlite3.connect("visitors.db")
print("Database opened successfully")

con.execute("CREATE TABLE Visitors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, appointment TEXT NOT NULL)")

print("Table connected successfully")
'''

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/savedetails", methods = ["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form['email']
            appointment = request.form['appointment']
            with sqlite3.connect("visitors.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Visitors (name, email, appointment) values (?, ?, ?)", (name, email, appointment))
                con.commit()
                msg = "Visitor successfully Added"
        except:
            con.rollback()
            msg = "We can not add the employees to the list"
        finally:
            return render_template("success.html", msg = msg)
            con.close()

@app.route('/adminneeleshgandhi123456789')
def view():
    con = sqlite3.connect("visitors.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Visitors")
    rows = cur.fetchall()
    return render_template("view.html", rows = rows)


if __name__=="__main__":
    app.run(debug=True)