from SE_IdentifyingTriangles import identifyTrianglesModule
from SE_AreaCalculator import areaModuleMenu
from SE_Pythagoras import pythagSideMenu
from SE_Utils import clear_console

# This is the mainline module
# It will control the main menu and call the other modules as requested by the user. 
# The user can continue to select options until they choose to quit the program.
def main():

    # This loop is for the main menu and will continue to run until the user selects the option to quit the program.
    option = "99"
    while option != "0":
        
        # Display the main menu and get the user's selection.
        clear_console()
        print("Welcome the Maths Ed program")
        print("\nSelect from the following options: ")
        print("  1: Identify Triangles")
        print("  2: Area Calculator")
        print("  3: Pythagoras' Theorem")
        print("  4: Area Quiz")
        print("  0: Quit")

        option = input("\nEnter your selection: ")

        # Call the user selected module and pass control to it. 
        # When the user returns from the module, the main menu will be displayed again.
        if option == "1":
            identifyTrianglesModule()
        elif option == "2":
            areaModuleMenu()
        elif option == "3":
            pythagSideMenu()
        elif option == "4":
            pass
        elif option == "0":
            print ("Thank you for using the Maths Ed program. Goodbye!")
            pass
        else:
            print ("")
            print("Please enter one of the available options.")
            input("Press enter to try again...")


# This code is a Python convention to call the main subroutine
#   if this file is directly run
# If the file is imported instead, the main subroutine will not be called
if __name__ == '__main__':
    main()

