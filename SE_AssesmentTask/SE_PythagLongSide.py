from SE_Validation import validatePositive, validateIntegerDataInput
from SE_Utils import clear_console

def getShortSides():

    isValid = False

    clear_console()
    #Get both short sides of the triangle from the user, and return them as integers, along with whether or not they are valid
    print("Enter the following sides of the triangle to calculate its unknown long side (positive integers only).")
    isValid, outputs = validateIntegerDataInput("Enter the first short side of the triangle: ", "Enter the second short side of the triangle: ")
    if isValid:
        int_short1, int_short2 = outputs
        return int_short1, int_short2, isValid

    return 0, 0, False

def findUnknownLongSide(short1, short2):
    long_side = (short1**2 + short2**2)**0.5
    print(f"The hypotenuse of the triangle is: {long_side:.2f}")
    print("")
    input("Press enter to continue...")

def longSideModule():
    while True:
        short1, short2, isValid = getShortSides()
        # Validate the short sides. If they are valid, calculate the long side of the triangle.
        if isValid and validatePositive(short1) and validatePositive(short2):
            findUnknownLongSide(short1, short2)
        else:
            input("Press enter to continue...")
        print ("")
        print("What would you like to do next?")
        print("1. Calculate the hypotenuse of another triangle")
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

