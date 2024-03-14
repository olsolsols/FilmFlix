import mysql.connector

conn = mysql.connector.connect(host = "localhost", database="filmflixdb", user = "root", password="password") #this db was just created in workbench (its empty). Otehrwise I can re-insert the data manually

if conn.is_connected():
    print("Connected to MySQL")
else:
    print("connection failed")

cursor=conn.cursor(prepared=True)

cursor.execute("""CREATE TABLE `tblFilms`
    (
    `filmID` INT,
    `title` VARCHAR(45),
    `yearReleased` INT,
    `rating` VARCHAR(20),
    `duration` INT,
    `genre` VARCHAR(20),
    PRIMARY KEY (`filmID`),
    UNIQUE INDEX `filmID_UNIQUE` (`filmID` ASC) VISIBLE
    );""")