from SE_Validation import validateIntegerDataInput
from SE_Validation import validatePositive
from SE_Utils import clear_console
# This subroutine will get three sides from the user
# These will be returned in a list of strings
def getTriangleSides():
    
    clear_console()

    print("Enter the three triangle sides (positive integers only).")

    isvalid = False
    
    
    isValid, outputs = validateIntegerDataInput("Enter a side length: ", "Enter a side length: ", "Enter a side length: ")
    if isValid:
        side1, side2, side3 = outputs
        return [side1, side2, side3], True
    
    return [], False

  


# This subroutine will accept a valid list of three side lengths of type
#    integer in ascending order
# It will determine and display the classification of the triangle
# The following classifications will be determined:
#  - Isoscelles
#  - Equilateral
#  - Scalene
#  - Right Angled (isoscelles and scalene triangles will be checked for this)
#  - Impossible triangle
def classifyTriangle(sides):

    # Check for impossible triangle
    if sides[0] + sides[1] <= sides[2]:
        print("This is an impossible triangle")

    # Check for equilateral triangle
    elif sides[0] == sides[1] and sides[0] == sides[2]:
        print("This is an equilateral triangle")

    # It will be scalene or isoscelles, These can also be right-angled
    else:

        # Check for isoscelles
        if (sides[0] == sides[1] or
            sides[0] == sides[2] or
            sides[1] == sides[2]):

            print("This is an isoceles triangle")
        else:
            print("This is a scalene triangle")

        # Check for right angled
        if (sides[0] ** 2) + (sides[1] ** 2) == sides[2] ** 2:
            print("This is also a right-angled triangle")


# This is the controlling module for the identify triangles feature
def identifyTrianglesModule():

    while True:

        sides, isValid = getTriangleSides()

        if isValid and validatePositive(sides[0]) and validatePositive(sides[1]) and validatePositive(sides[2]):
            sides.sort()

            classifyTriangle(sides)
        else:
            input("Press enter to continue...")

        print ("")
        print("What would you like to do next?")
        print("1. Classify another triangle")
        print("0. Back to main menu")
        choice = input("Enter the number of your selection: ")
        if choice == "1":
            continue
        elif choice == "0":
            return
        else:
            print("Invalid selection. Returning to main menu.")
            input("Press enter to continue...")
            return


    