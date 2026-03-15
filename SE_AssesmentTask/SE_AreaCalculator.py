from SE_RectangleArea import rectangleAreaModule
from SE_TriangleArea import triangleAreaModule
from SE_Utils import clear_console

# This is the area main menu function that displays a menu for the user to select a shape for area calculation.
# It will call the appropriate subroutine based on the user's selection. 
# The user can continue to select shapes until they choose to return to the main menu.
def areaModuleMenu():

    print("Welcome to the area calculator module.")

    # Display a menu for the user to select a shape for area calculation. The user can continue to
    # select shapes until they choose to return to the main menu.
    user_area_selection = "99"
    while user_area_selection != 0:
        clear_console()
        print("\nSelect a shape to calculate its area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("0. Back to main menu")

        # Get the user's selection and call the appropriate subroutine based on their choice.
        user_area_selection = input("Input the number of your selection: ")

        if user_area_selection == "1":
            rectangleAreaModule()
        elif user_area_selection == "2":
            triangleAreaModule()
        elif user_area_selection == "3":
            pass
        elif user_area_selection == "0":
            return
        else:
            print("Invalid selection. Please try again.")

        

