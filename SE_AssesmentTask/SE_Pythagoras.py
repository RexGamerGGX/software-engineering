from SE_Utils import clear_console
from SE_PythagLongSide import longSideModule
from SE_PythagShortSide import shortSideModule

# This is the controlling module for the pythagorean theorem feature. 
# It will call the other subroutines to get the sides of the triangle, validate them, and calculate the unknown side if they are valid.
# uses return_to_main variable to determine whether to return to the main menu or
# the area calculator menu after a shape's area has been calculated.
def pythagSideMenu():
    
    user_pythag_selection = "99"

    while user_pythag_selection != "0":
         # Display a menu for the user to select a shape for area calculation. The user can 
         # select a shape for area calculation, or return to the main menu.
         # If they select a shape, the appropriate subroutine will be called to calculate the area of that shape.
        clear_console()
        print("Welcome to the pythagorean theorem module.")
        print("Which side of your triangle do you want to calculate?: ")
        print("1. Hypotenuse")
        print("2. Short side")
        print("0. Back to main menu")
        print ("")
        
        # Get the user's selection and call the appropriate subroutine based on their choice. 
        # The user can continue to select options until they choose to return to the main menu.
        user_pythag_selection = input("Enter the number of your selection: ")
        return_to_main = None
        if user_pythag_selection == "1":
            return_to_main = longSideModule()
        elif user_pythag_selection == "2":
            return_to_main = shortSideModule()
        elif user_pythag_selection == "0":
            return
        else:
            print("Invalid selection. Please try again.")

        if return_to_main == "Main":
            return 
        



