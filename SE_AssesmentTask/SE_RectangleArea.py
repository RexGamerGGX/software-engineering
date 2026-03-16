from SE_Utils import clear_console
from SE_Validation import validatePositive, validateIntegerDataInput
#This subroutine will get the length and width of the user's rectangle
def getRectangleSides():

    isValid = False 

    clear_console()   
    
    #Get the width and length of the rectangle from the user, and return them as integers, along with whether or not they are valid
    print("Enter the dimensions of the rectangle to calculate its area (positive integers only).")
    isValid, outputs = validateIntegerDataInput("Enter the width of the rectangle: ", "Enter the length of the rectangle: ")
    if isValid:
        int_width, int_length = outputs
        return int_width, int_length, isValid
    
    return 0, 0, False

# This subroutine will calculate the area of a rectangle given its width and length
# and display the result to the user. The area will be displayed to two decimal places.
def rectangleArea(width, length):

    area = width * length
    print(f"The area of the rectangle is: {area}")
    print("")
    input("Press enter to continue...")

# This is the main function for the area calculator module. It will call the other subroutines 
# to get the dimensions of the rectangle, validate them, and calculate the area if they are valid.
def rectangleAreaModule():
    
    while True:
        width, length, isValid = getRectangleSides()

        if isValid and validatePositive(width) and validatePositive(length):
            rectangleArea(width, length)
        else:
            input("Press enter to continue...")
        print ("")
        print("What would you like to do next?")
        print("1. Calculate the area of another rectangle")
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
