# 	  Author: Shayla Bradley
# Assignment: Module 8.2
# 		Date: 11/27/22
#
#

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "H@ters88",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

# Creates new connection with cursor.
cursor = db.cursor()
print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
input("\n\n Press any key to continue. . .")

# Create ref function.
def show_films(cursor, title):
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, " + \
			       "studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id = genre.genre_id " + \
			       "INNER JOIN studio ON film.studio_id = studio.studio_id")
    films = cursor.fetchall()

    # Formats output when show_films function is called.
    print("\n -- {} --".format(title))
    # Iterates through print format.
    for film in films:
        print("Film Name: ", film[0])
        print("Director: ", film[1])
        print("Genre Name ID: ", film[2])
        print("Studio Name: ", film[3])
        print("  ")

# Displays films.
title_one = "DISPLAYING FILMS"
# Passing cursor and title to show_films.
show_films(cursor, title_one)

# Runs insert query and displays results.
title_two = "DISPLAYING FILMS AFTER INSERT"
query_insert = "INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)" + \
        "VALUES ('Black Adam', 'Jaume Collet-Serra', 2, 3, 2022, 125) "
cursor.execute(query_insert)
db.commit()
# Passing cursor and title to show_films.
show_films(cursor, title_two)

# Runs update query and displays results.
title_three = "DISPLAYING FILMS AFTER UPDATE"
query_update = "UPDATE film SET genre_id = 1 WHERE film_id = 2"
cursor.execute(query_update)
db.commit()
# Passing cursor and title to show_films.
show_films(cursor, title_three)

# Runs delete query and displays results.
title_four = "DISPLAYING FILMS AFTER DELETE"
query_delete = "DELETE FROM film WHERE film_id = 1"
cursor.execute(query_delete)
db.commit()
# Passing cursor and title to show_films.
show_films(cursor, title_four)

db.close()
    
