from SE_Validation import validatePositive, validateIntegerDataInput
from SE_Utils import clear_console
# This subroutine will get the base and height of the user's triangle
def getTriangleDimensions():

    isValid = False

    clear_console()  

    #Get the base and height of the triangle from the user, and return them as integers, along with whether or not they are valid
    print("Enter the dimensions of the triangle to calculate its area (positive integers only).")
    isValid, outputs = validateIntegerDataInput("Enter the base of the triangle: ", "Enter the height of the triangle: ")
    if isValid:
        int_base, int_height = outputs
        return int_base, int_height, isValid
    
    return 0, 0, False
        
# This subroutine will calculate the area of a triangle given its base and height
# and display the result to the user. The area will be displayed to two decimal places.
def triangleArea(base, height):

    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
    print("")
    input("Press enter to continue...")

# This is the main function for the triangle area calculator module. It will call the other subroutines
# to get the dimensions of the triangle, validate them, and calculate the area if they are valid.
def triangleAreaModule():
    while True:
        base, height, isValid = getTriangleDimensions()

        # Validate the base and height. If they are valid, calculate the area of the triangle.
        if isValid and validatePositive(base) and validatePositive(height):
            triangleArea(base, height)
        else:
            input("Press enter to continue...")
        print ("")
        print("What would you like to do next?")
        print("1. Calculate the area of another triangle")
        print("0. Back to area calculator menu")
        choice = input("Enter the number of your selection: ")
        if choice == "1":
            continue
        elif choice == "0":
            return
        else:
            print("Invalid selection. Returning to area calculator menu.")
            input("Press enter to continue...")
            return
