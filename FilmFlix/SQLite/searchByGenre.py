from sqlite3 import dbapi2
from connection import *
import time



#this will be executed if input is in double quotes
def searchGenre():
    genre = input("Enter the film genre you want to search for: ")
    genre = "'" + genre + "'"
    cursor.execute('SELECT * FROM tblFilms WHERE genre='+genre)

    # cursor.execute('SELECT * FROM members WHERE Firstname = "Em"')
    row = cursor.fetchall()
    for record in row:
        print(record)
        
#searchGenre()


#newFieldValue = "'" + newFieldValue + "'" ----> not sure how this works
# def searchByFilmID():
#     searchID = input("Enter filmID of record to search for: ")
#     print("No quotes",searchID)
#     # adding single quote to your textsring is 
#     #abdul    =    "!" +  abdul + "!"
#     searchID = "!" + searchID + "!"
#     print("With quotes",searchID)
 
#     cursor.execute('SELECT * FROM tblFilms WHERE title='+ "'" + searchID + "'")
#     row = cursor.fetchall()
#     for record in row:
#         print(record)
    
# searchByFilmID()