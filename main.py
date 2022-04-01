from flask import *

app = Flask(__name__)

app.secret_key = "L:slkjweijsdhJAS"

adminUsername = "admin"
adminPassword = "admin"


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", user=session["username"] if "username" in session else None)


@app.route('/login')
def login():
    if "username" in session:
        return redirect("/") # Send to home page if logged in already.
    else:
        return render_template("login.html")


@app.route('/login', methods = ["POST"])
def loginPost():
    username = request.form["username"]
    password = request.form["password"]
    if username == adminUsername and password == adminPassword: # Check entered username and password match the known ones
        session["username"] = username
        return redirect("/")
    else:
        flash('Please check your login details and try again.')
        return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop("username")
    return redirect("/")

if __name__ == "__main__":
    app.run()