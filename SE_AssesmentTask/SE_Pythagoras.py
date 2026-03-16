from SE_PythagShortSide import shortSideModule
from SE_PythagLongSide import longSideModule
from SE_Utils import clear_console

def pythagSideMenu():
    
    print("Welcome to the pythagorean theorem module.")

    # Display a menu for the user to select a shape for area calculation. The user can continue to
    # select shapes until they choose to return to the main menu.
    user_pythag_selection = "99"
    while user_pythag_selection != "0":
        clear_console()
        print("Which side of your triangle do you want to calculate?: ")
        print("1. Hypotenuse")
        print("2. Short side")
        print("0. Back to main menu")
        print ("")
        user_pythag_selection = input("Enter the number of your selection: ")
        if user_pythag_selection == "1":
            longSideModule()
        elif user_pythag_selection == "2":
            shortSideModule()
        elif user_pythag_selection == "0":
            return
        else:
            print("Invalid selection. Please try again.")

