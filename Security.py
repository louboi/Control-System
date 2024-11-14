# Import the required functions
import sqlite3 # Import the SQLite Function used to manage the database

# Connect to the database
con = sqlite3.connect("Secrets.db")
cur = con.cursor()

# Initiallise global variables
UUID = []
result = 0
Checksum = 0

# Check the Username and Password are valid
def check_validity(username, password):
    if len(username) > 10:
        print("Username invalid (001)")
    elif len(username) == 0:
        print("Username invalid (002)")
    if len(password) > 10:
        print("Username invalid (001)")
    elif len(password) == 0:
        print("Username invalid (002)")
    quit()

# Generate the UUID by converting to ascii decimal values and appending to a list.
def UUID_gen(password, username, UUID, result):
    u = username
    p = password
    UUID = [ord(c) for c in u] + [ord(c) for c in p]
    result = ''.join([str(s) for s in UUID])
    data = [(username, password, result)]
    cur.executemany("INSERT INTO users VALUES(?, ?, ?)", data)
    con.commit()
    print(UUID)
    print(result)

# Generate a checksum for validating users for entry
def checksum_gen(UUID, Checksum):
    if result // 2 != 0:
        print("The number is odd.")
    elif result // 2 == 0:
        print("The number is even.")
    else:
        print("Error code 001")

# Get the user to make a Username and Password
username = str(input("Please make a Username (less than 10 characters): "))
password = str(input("Please make a Password (less than 10 characters): "))

#----------Main Program begins here----------#
check_validity(username, password) # Validate the Username and Password
UUID_gen(password, username, UUID, result) # Generate the UUID