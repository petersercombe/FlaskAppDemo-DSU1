import sqlite3

def commitQuery(query, data=None):
    db = sqlite3.connect('lostProperty.db')
    try:
        cursor = db.cursor()
        if data == None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        db.commit() # Commit all changes at once.
    except Exception as error:
        db.rollback()
        print("Oops: " + str(error))
    finally:
        db.close()

def selectQuery(query, data=None):
    db = sqlite3.connect('lostProperty.db')
    try:
        cursor = db.cursor()
        if data == None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        return cursor.fetchall()
    except Exception as error:
        db.rollback()
        print("Oops: " + str(error))
    finally:
        db.close()

getAllUsers = "SELECT * FROM users"

getOneUser = "SELECT * FROM users WHERE username == ?"

addUser = "INSERT INTO users ('username','firstname','lastname','email','password') VALUES (?,?,?,?,?)"

print(selectQuery(getAllUsers))

print(selectQuery(getOneUser, ['staff',]))

# commitQuery(addUser, ('staff', 'Staff', 'User', 'staff@bcc.net.au', 'staff'))