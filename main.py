from flask import *
import os, sys # for file operations
import datetime # for datetime

app = Flask(__name__)

app.secret_key = "L:slkjweijsdhJAS"
folderLocation = os.path.dirname(os.path.realpath(sys.argv[0]))
app.config["uploadsFolder"] = folderLocation + "/static/images/"

users = {"admin":{
            "password": "admin",
            "name": "Admin User"},
         "pleb":{
            "password": "password",
            "name": "Pleb User"}
         }

lostProperty = {0:{"title":"Water Bottle",
                   "description":"Blue Camelbak 1L",
                   "date":"2022-04-22",
                   "claimed":False,
                   "claimedBy":"",
                   "image":"picture1.jpg"},
                1:{"title":"Hat",
                   "description":"Blue Sports Hat",
                   "date":"2022-04-20",
                   "claimed":False,
                   "claimedBy":"",
                   "image":"noImage.png"},
                2:{"title":"Headphones",
                   "description":"Black, Fancy, Wireless",
                   "date":"2022-04-18",
                   "claimed":True,
                   "claimedBy":"John Johnson",
                   "image":"picture2.jpg"}
        }

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html",
                           user=session["name"] if "username" in session else None,
                           lostProperty=lostProperty)

@app.route('/claimed')
def claimed():
    if "username" in session:
        return render_template("claimed.html", user=session["name"], lostProperty=lostProperty)
    else:
        flash('You must be logged in to view this page.')
        return render_template("login.html")

@app.route('/item/<key>')
def item(key):
    return render_template("item.html",
                           user=session["name"] if "username" in session else None,
                           data=lostProperty[int(key)])


@app.route('/add')
def add():
    if "username" in session:
        return render_template("add.html",
                               user=session["name"])
    else:
        flash('You must be logged in to view this page.')
        return render_template("login.html")

@app.route('/add', methods = ["POST"])
def addPost():
    if "username" in session:
        currentDT = datetime.datetime.now()
        files = request.files["image"]
        if files:
            fileName = currentDT.strftime("%Y-%m-%d %H-%M-%S") + "-" + files.filename
            files.save(os.path.join(app.config["uploadsFolder"], fileName))
            image = fileName
        else:
            image = "noImage.png"
        lostProperty[len(lostProperty)] = {"title":request.form["title"],
                                           "description":request.form["description"],
                                           "date":currentDT.strftime("%Y-%m-%d"),
                                           "claimed":False,
                                           "claimedBy":"",
                                           "image":image}
        print(lostProperty)
        return redirect("/")
    else:
        flash('You must be logged in to view this page.')
        return render_template("login.html")


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
    if username in users and password == users[username]["password"]: # Check entered username and password match the known ones
        session["username"] = username
        session["name"] = users[username]["name"]
        return redirect("/")
    else:
        flash('Please check your login details and try again.')
        return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop("username")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True) # Debugging on when doing html changes.