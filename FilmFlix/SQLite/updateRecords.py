from connection import * 
import time

def updateRecords():
    keyField = input("Enter ID of the record to be updated: ")
    field = input("Which field do you want to update? (title, yearReleased, rating, duration, genre): ")
    newFieldValue = input("Enter the new value for the field you are updating: ")
    print(newFieldValue)

    newFieldValue = "'" + newFieldValue + "'"
    print(newFieldValue)

    try:
        cursor.execute("UPDATE tblFilms SET " + field + "=" + newFieldValue + " WHERE filmID" + "=" + keyField)
        conn.commit()
        print("Record Updated")

        time.sleep(2)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Record not updated")

#updateRecords()