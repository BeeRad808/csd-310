# Author:		Shayla Bradley
# Assignment:	Module 7.2
# Date:			11/27/22

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "H@ters88",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

db = mysql.connector.connect(user = 'root', password = 'H@ters88', host = '127.0.0.1', database = 'movies')
	
# Creates new cursor connection.
cursor = db.cursor()
	
# First query selects all fields in studio table.
query = "SELECT * from studio"
cursor.execute(query)
result = cursor.fetchall()
# Studio records.
print("--DISPLAYING Studio RECORDS--")
for row in result:
	print("Studio ID:", row[0])
	print("Studio Name:", row[1])
	print(" ")
	
# Second query selects all fields in genre table.	
query = "SELECT * from genre"
cursor.execute(query)
result = cursor.fetchall()
# Genre records.
print("--DISPLAYING Genre RECORDS--")
for row in result:
	print("Genre ID:", row[0])
	print("Genre Name:", row[1])
	print(" ")
	
# Third query selects movie names with runtime less than 2 hours.
query = "SELECT film_name, film_runtime from film where film_runtime < 120"
cursor.execute(query)
result = cursor.fetchall()

# Short Film records.
print("--DISPLAYING Short Film RECORDS--")
for row in result:
	print("Film Name:", row[0])
	print("Runtime:", row[1])
	print("")

# Fourth query gets list of film names and directors grouped by director.
query = "SELECT film_name, film_director from film order by film_director"
cursor.execute(query)
result = cursor.fetchall()
# Director records.
print("--DISPLAYING Director RECORDS in Order--")
for row in result:
	print("Film Name:", row[0])
	print("Director:", row[1])
	print(" ")
	
cursor.close()
db.close()
