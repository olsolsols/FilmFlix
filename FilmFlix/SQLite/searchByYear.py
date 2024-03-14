from sqlite3 import dbapi2
from connection import *
import time


def searchYear():
    yrRel = input("Enter the release year of the film you want to search for: ")
    yrRel = "'" + yrRel + "'"
    cursor.execute('SELECT * FROM tblFilms WHERE yearReleased='+yrRel)
    row = cursor.fetchall()
    for record in row:
        print(record)
        
#searchYear()