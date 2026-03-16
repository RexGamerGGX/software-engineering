from SE_Validation import validatePositive, validateIntegerDataInput
from SE_Utils import clear_console

def getLongAndShort():

    isValid = False 

    clear_console()   
   
    #Get the long and short sides of the triangle from the user, and return them as integers, along with whether or not they are valid
    print("Enter the following sides of the triangle to calculate its unknown short side (positive integers only).")
    isValid, outputs = validateIntegerDataInput("Enter the long side of the triangle: ", "Enter the short side of the triangle: ")
    if isValid:
        int_long, int_short = outputs
        return int_long, int_short, isValid
    if [0] < [1]:
        print("The long side must be greater than the short side. Please try again.")
    
    return 0, 0, False

def findUnknownShortSide(long, short):
    short_side = (long**2 - short**2)**0.5
    print(f"The short side of the triangle is: {short_side:.2f}")
    print("")
    input("Press enter to continue...")

def shortSideModule():
    while True:

        long, short, isValid = getLongAndShort()

        # Validate the long and short sides. If they are valid, calculate the short side of the triangle.
        if isValid and validatePositive(long) and validatePositive(short):
            findUnknownShortSide(long, short)
        else:
            input("Press enter to continue...")

        print ("")
        print("What would you like to do next?")
        print("1. Calculate the short side of another triangle")
        print("0. Back to Pythagorean menu")
        choice = input("Enter the number of your selection: ")
        if choice == "1":
            continue
        elif choice == "0":
            return
        else:
            print("Invalid selection. Returning to Pythagorean menu.")
            input("Press enter to continue...")
            return

