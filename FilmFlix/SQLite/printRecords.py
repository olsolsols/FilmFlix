from connection import *

def printRecords():
    cursor.execute('SELECT * FROM tblFilms')
    row = cursor.fetchall()
    for record in row:
        print(record)
#printRecords()