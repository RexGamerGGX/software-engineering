# This is the mainline module
# It will control the main menu and call the other modules as requested
from SE_IdentifyingTriangles import identifyTrianglesModule
from SE_AreaCalculator import areaModuleMenu
from SE_Pythagoras import pythagSideMenu
from SE_Utils import clear_console

def main():

    print("Welcome the Maths Ed program")

    # This loop is for the main menu
    option = "99"
    while option != "0":

        clear_console()
        print("\nSelect from the following options: ")
        print("  1: Identify Triangles")
        print("  2: Area Calculator")
        print("  3: Pythagoras' Theorem")
        print("  4: Area Quiz")
        print("  0: Quit")

        option = input("\nEnter your selection: ")

        # Call the user selected module
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

