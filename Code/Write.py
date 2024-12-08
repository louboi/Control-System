# Import the required functions
import RPi.GPIO as GPIO                 # Import the GPIO Library
from mfrc522 import SimpleMFRC522       # Import the RFID reader library
import sqlite3                          # Import the SQLite Function used to manage the database
import math                             # Import math abilities
import time                             # Import time for sleep function

# Connect to the database
con = sqlite3.connect("Code/Secrets.db")
cur = con.cursor()

# Get the reading function ready
reader = SimpleMFRC522()

# Initialise variables
text = ""
user = ""
done = False

def write(text, user):
    cur.execute("SELECT UUID FROM users WHERE Username = ?", (user,))
    z = cur.fetchall()
    text = str(z[0][0])
    try:
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
    finally:
        GPIO.cleanup()

# Main program
while done == False:
    user = str(input("Input the user you would like to add: "))
    write(text, user)
    user = str(input("Do you want to continue? (Y/y or N/n): "))
    match user:
        case "y":
            done = False
            print("false")
        case "Y":
            done = False
            print("false")
        case "n":
            done = True
            print("true")
        case "N":
            done = True
            print("true")
