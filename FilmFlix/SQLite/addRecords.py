from connection import * 
import time

#code for opening database filmflixdb ---> this is only for replit?
# conn = sqlite3.connect('filmflix.db')
# cursor = conn.cursor()

#creating a subroutine to add a record
def addRecords():
    records = []

    filmID = cursor.lastrowid
    title = input("Enter the film title: ")
    yearReleased = int(input("Enter the release year: "))
    rating = input("Enter the film rating: ")
    duration = int(input("Enter the duration of the film in minutes: "))
    genre = input("Enter the film genre: ")

    records.append(filmID)
    records.append(title)
    records.append(yearReleased)
    records.append(rating)
    records.append(duration)
    records.append(genre)

    try: 
        cursor.execute('INSERT INTO tblFilms VALUES (?, ?, ?, ?, ?, ?)', records)
        conn.commit()
        print("The record has been added successfully.")

        time.sleep(3)
        cursor.execute('SELECT * FROM records')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Record not added")

#addRecords()