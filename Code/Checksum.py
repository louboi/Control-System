# Import the required functions
import sqlite3 # Import the SQLite Function used to manage the database
import math

# Connect to the database
con = sqlite3.connect("Code/Secrets.db")
cur = con.cursor()

# Required Subroutines
def check(username):
    cur.execute("SELECT UUID FROM users WHERE Username = ?", (username,))
    z = cur.fetchall()
    return int(z[0][0])

UUID = 0
username = ""

while True:
    username = str(input("What is your username? "))
    UUID = check(username)
    checksum = 0
    if UUID // 2 == 0:
        checksum = UUID ** 16
    elif UUID // 2 != 0:
        checksum = UUID ** 15
    else:
        print("Error code 003")
    print(UUID)
    print(checksum)