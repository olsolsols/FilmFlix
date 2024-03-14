from sqlite3 import dbapi2
from connection import *
import time


def searchRating():
    rating = input("Enter the rating of the film you want to search for: ")
    rating = "'" + rating + "'"
    cursor.execute('SELECT * FROM tblFilms WHERE rating='+rating)
    row = cursor.fetchall()
    for record in row:
        print(record)
        
#searchRating()