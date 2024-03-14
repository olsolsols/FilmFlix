from connection import * 
import time

def deleteRecords():
    keyField=input("Enter ID of the record you'd like to delete: ")
    try:
        cursor.execute("DELETE FROM tblFilms WHERE filmID=" + keyField)
        conn.commit() # commit=apply
        print("\nRecord deleted")

        time.sleep(3)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except: 
        print("Record not deleted")


#deleteRecords()