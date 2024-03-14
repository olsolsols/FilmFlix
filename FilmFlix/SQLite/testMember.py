from myConnection import *
import time


#   id  fname   lname       email
# (4, 'Tommy', 'Hill', 'tf@ford.com')
# (5, 'Em', 'Jay', 'em@jay.com')

def searchFname():
    fname = input("Enter member's first name to search for: ")
    fname = "'" + fname + "'"

    cursor.execute('SELECT * FROM members WHERE Firstname=' + fname)
    row = cursor.fetchall()
    # print("A row", row)
    strData = str(row)
    if fname in strData:
        for record in row:
            print(record)
    else:
        print("No record exists of:", fname)

searchFname()