from flask import *
import os, sys # for file operations
import datetime # for datetime
from imageUtils import *
from dbUtils import *

app = Flask(__name__)

app.secret_key = "L:slkjweijsdhJAS"
folderLocation = os.path.dirname(os.path.realpath(sys.argv[0]))
app.config["uploadsFolder"] = folderLocation + "/static/images/"

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html",
                           user=session["name"] if "username" in session else None,
                           lostProperty=selectQuery(getItems,(50,0))) # update to add pagination

@app.route('/claimed')
def claimed():
    if "username" in session:
        return render_template("claimed.html", user=session["name"], lostProperty=selectQuery(getItems,(50,0)))
    else:
        flash('You must be logged in to view this page.')
        return render_template("login.html")

@app.route('/item/<itemID>')
def item(itemID):
    return render_template("item.html",
                           user=session["name"] if "username" in session else None,
                           item=selectQuery(getOneItem, (itemID,))[0])


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
            thumb = thumbnail(Image.open(files))
            thumb.save(os.path.join(app.config["uploadsFolder"], 'thumb_'+fileName), quality=95)
        else:
            image = "noImage.png"

        commitQuery(addItem, (request.form["title"],
                              request.form["description"],
                              request.form["categoryID"],
                              currentDT.strftime("%Y-%m-%d"),
                              image))
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
    user = selectQuery(getOneUser,(username,))
    if len(user)>0 and password == user[0][5]: # Check entered username and password match the known ones
        session["username"] = username
        session["name"] = user[0][2]
        return redirect("/")
    else:
        flash('Please check your login details and try again.')
        return render_template("login.html")

@app.route('/signup')
def signup():
    if "username" in session:
        return redirect("/") # Send to home page if logged in already.
    else:
        return render_template("signup.html")


@app.route('/signup', methods = ["POST"])
def signupPost():
    username = request.form["username"]
    users = selectQuery(getAllUsers)
    if username in str(users):
        flash('Username not available. Please try again.')
        return render_template("signup.html")
    else:
        commitQuery(addUser, (username,
                              request.form["firstname"],
                              request.form["lastname"],
                              request.form["email"],
                              request.form["password"]))
        session["username"] = username
        session["name"] = request.form["firstname"]
        return redirect("/")


@app.route('/logout')
def logout():
    session.pop("username")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True) # Debugging on when doing html changes.