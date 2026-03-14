# This is the mainline module
# It will control the main menu and call the other modules as requested
from SE_IdentifyingTriangles import identifyTrianglesModule

def main():

    print("Welcome the Maths Ed program")

    # This loop is for the main menu
    option = "99"
    while option != "0":

        print("\nSelect from the following options: ")
        print("  1: Identify Triangles")
        print("  2: Area Calculator")
        print("  3: Pythagoras' Theorem")
        print("  0: Quit")

        option = input("\nEnter your selection: ")

        # Call the user selected module
        if option == "1":
            identifyTrianglesModule()
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            pass
        elif option == "0":
            pass
        else:
            print("Please enter a valid option")


# This code is a Python convention to call the main subroutine
#   if this file is directly run
# If the file is imported instead, the main subroutine will not be called
if __name__ == '__main__':
    main()

