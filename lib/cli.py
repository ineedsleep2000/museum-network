from helpers import (
    exit_program,
    museum_menu,
    exhibit_menu,
    menu
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

################################################################
# Command Line Interface
################################################################
if __name__ == "__main__":
    main()
