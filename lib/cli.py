from seed import (
    seed_database
)
from helpers import (
    exit_program,
    list_of_all_museums,
    list_of_all_exhibits,
    museum_menu,
    exhibit_menu
)

################################################################
# Interface Operations
################################################################

def main():
    while True:
        menu()
        choice = input("Input Command Here: ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            museum_menu()
        elif choice == "2":
            exhibit_menu()
        else:
            print("Invalid choice")



def menu():
    print("""
          
          |-------------------------------------------|
          |******|WELCOME TO THE MUSEUM NETWORK|******|
          |-------------------------------------------|

          """)
    print("*********** Main Menu ***********")
    print("Please select an option below")
    print("1. View Museums Menu")
    print("2. View Exhibits Menu")
    print("0. Exit Program")
    print("*********************************")


################################################################
# Comman Line Interface
################################################################
if __name__ == "__main__":
    seed_database()
    main()
