


"""CREATE TABLE "items" (
	"itemID"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"description"	TEXT,
	"categoryID"	INTEGER,
	"date"	TEXT,
	"image"	TEXT,
	PRIMARY KEY("itemID" AUTOINCREMENT)
);"""

"""CREATE TABLE "categories" (
	"categoryID"	INTEGER NOT NULL UNIQUE,
	"category"	TEXT,
	PRIMARY KEY("categoryID" AUTOINCREMENT)
);"""

"""CREATE TABLE "claims" (
	"claimID"	INTEGER NOT NULL UNIQUE,
	"itemID"	INTEGER,
	"claimDate"	TEXT,
	"claimedBy"	TEXT,
	PRIMARY KEY("claimID" AUTOINCREMENT)
);"""


"""CREATE TABLE "users" (
	"userID"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT UNIQUE,
	"firstname"	TEXT,
	"lastname"	TEXT,
	"email"	TEXT UNIQUE,
	"password"	TEXT,
	PRIMARY KEY("userID" AUTOINCREMENT)
);"""

"""CREATE TABLE "roleAssignment" (
	"assignmentID"	INTEGER NOT NULL UNIQUE,
	"userID"	INTEGER,
	"roleID"	INTEGER,
	PRIMARY KEY("assignmentID" AUTOINCREMENT)
);"""

"""CREATE TABLE "roles" (
	"roleID"	INTEGER NOT NULL UNIQUE,
	"role"	TEXT,
	PRIMARY KEY("roleID" AUTOINCREMENT)
)"""



"""INSERT INTO "main"."roleAssignment"("assignmentID","userID","roleID") VALUES (2,NULL,NULL);
UPDATE "main"."roleAssignment" SET "userID"=1 WHERE "_rowid_"='2'
UPDATE "main"."roleAssignment" SET "roleID"=2 WHERE "_rowid_"='2'"""


"""INSERT INTO "main"."roleAssignment"("assignmentID","userID","roleID") VALUES (2,1,2);"""