#import CRUD files
import addRecords
import deleteRecords
import updateRecords
import printRecords
import searchByGenre
import searchByYear
import searchByRating

#creating a function for menu options
def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("\nMenu Options")
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Update a record")
        print("4. Print all records")
        print("5. Filter all records by certain genre: ")
        print("6. Filter all records by certain year: ")
        print("7. Filter all records by certain rating: ")
        print("8. Exit")
        options = input("\n Enter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Not in the list of options")
    return options

mainProgram = True

while mainProgram == True:
    mainMenu = menuOptions()

    if mainMenu == "1":
        addRecords.addRecords()
    elif mainMenu == "2":
        deleteRecords.deleteRecords()
    elif mainMenu == "3":
        updateRecords.updateRecords()
    elif mainMenu == "4":
        printRecords.printRecords()
    elif mainMenu == "5":
        searchByGenre.searchGenre()
    elif mainMenu == "6":
        searchByYear.searchYear()
    elif mainMenu == "7":
        searchByRating.searchRating()
    else:
        mainProgram = False
input("Press enter to exit")




menuOptions()

