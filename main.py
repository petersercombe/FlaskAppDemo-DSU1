from flask import *

app = Flask(__name__)

app.secret_key = "L:slkjweijsdhJAS"

adminUsername = "admin"
adminPassword = "admin"


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html") #, user=session["username"])


@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "GET":
        if "username" in session:
            return redirect("/") # Send to home page if logged in already.
        else:
            return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if username == adminUsername and password == adminPassword:
            session["username"] = username
            return redirect("/")
        else:
            return redirect("/login")


if __name__ == "__main__":
    app.run()