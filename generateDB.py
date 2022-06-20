import sqlite3

queries = ["""CREATE TABLE IF NOT EXISTS "items" (
	"itemID"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"description"	TEXT,
	"categoryID"	INTEGER,
	"date"	TEXT,
	"image"	TEXT,
	PRIMARY KEY("itemID" AUTOINCREMENT)
);""",

"""CREATE TABLE IF NOT EXISTS "categories" (
	"categoryID"	INTEGER NOT NULL UNIQUE,
	"category"	TEXT,
	PRIMARY KEY("categoryID" AUTOINCREMENT)
);""",

"""CREATE TABLE IF NOT EXISTS "claims" (
	"claimID"	INTEGER NOT NULL UNIQUE,
	"itemID"	INTEGER,
	"claimDate"	TEXT,
	"claimedBy"	TEXT,
	PRIMARY KEY("claimID" AUTOINCREMENT)
);""",

"""CREATE TABLE IF NOT EXISTS "users" (
	"userID"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT UNIQUE,
	"firstname"	TEXT,
	"lastname"	TEXT,
	"email"	TEXT UNIQUE,
	"password"	TEXT,
	PRIMARY KEY("userID" AUTOINCREMENT)
);""",

"""CREATE TABLE IF NOT EXISTS "roleAssignment" (
	"assignmentID"	INTEGER NOT NULL UNIQUE,
	"userID"	INTEGER,
	"roleID"	INTEGER,
	PRIMARY KEY("assignmentID" AUTOINCREMENT)
);""",

"""CREATE TABLE IF NOT EXISTS "roles" (
	"roleID"	INTEGER NOT NULL UNIQUE,
	"role"	TEXT,
	PRIMARY KEY("roleID" AUTOINCREMENT)
)""",

"""INSERT INTO "main"."roleAssignment"("assignmentID","userID","roleID") VALUES (2,1,2);""",

"""INSERT INTO users ('username','firstname','lastname','password','email') VALUES ('admin','Admin','User','admin','admin@bcc.net.au');"""]


db = sqlite3.connect('lostProperty.db')
try:
    cursor = db.cursor()
    for query in queries:
        cursor.execute(query)
    db.commit() # Commit all changes at once.
    print("Tables created and records inserted successfully")
except Exception as error:
    db.rollback()
    print("Oops: " + str(error))
finally:
    db.close()