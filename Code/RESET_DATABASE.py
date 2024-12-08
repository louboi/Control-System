# Import the SQLite function
import sqlite3

# Connect to the database and get it ready to be used
con = sqlite3.connect("Code/Secrets.db")
cur = con.cursor()

#------------------------------------------------------------------------------------------------

# Initiallise the users table
try:
    cur.execute("DROP TABLE users")
except:
    print("That table doesn't exist yet.")

cur.execute("CREATE TABLE users(Username, Password, UUID)")
print("User table created")

# Output that it is done
print("Reset the database")