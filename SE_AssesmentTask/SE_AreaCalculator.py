from SE_RectangleArea import rectangleAreaModule
from SE_TriangleArea import triangleAreaModule
from SE_CircleArea import circleAreaModule
from SE_Utils import clear_console

# This is the area main menu function that displays a menu for the user to select a shape for area calculation.
# It will call the appropriate subroutine based on the user's selection. 
# The user can continue to select shapes until they choose to return to the main menu.
# uses return_to_main variable to determine whether to return to the main menu or
# the area calculator menu after a shape's area has been calculated.
def areaModuleMenu():

    user_area_selection = "99"

    while user_area_selection != 0:
        # Display a menu for the user to select a shape for area calculation. The user can select a shape
        # for area calculation, or return to the main menu. 
        # If they select a shape, the appropriate subroutine will be called to calculate the area of that shape.
        clear_console()
        print("Welcome to the area calculator module.")
        print("\nSelect a shape to calculate its area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("0. Back to main menu")
        print ("") 

        # Get the user's selection and call the appropriate subroutine based on their choice.
        user_area_selection = input("Enter your selection: ")
        return_to_main = None
        if user_area_selection == "1":
            return_to_main =  rectangleAreaModule()
        elif user_area_selection == "2":
            return_to_main = triangleAreaModule()
        elif user_area_selection == "3":
           return_to_main = circleAreaModule()
        elif user_area_selection == "0":
            return
        else:
            print("Invalid selection. Please try again.")

        if return_to_main == "Main":
            return

