from SE_Validation import validatePositive, validateIntegerDataInput
from SE_Utils import clear_console

def getLongAndShort():

    isValid = False 

    clear_console()   
   
    #Get the long and short sides of the triangle from the user, and return them as integers, along with whether or not they are valid
    print("Enter the dimensions of the triangle to calculate its area (positive integers only).")
    isValid, outputs = validateIntegerDataInput("Enter the long side of the triangle: ", "Enter the short side of the triangle: ")
    if isValid:
        int_long, int_short = outputs
        return int_long, int_short, isValid
    
    return 0, 0, False

def findShortSide(long, short):
    short_side = (long**2 - short**2)**0.5
    print(f"The short side of the triangle is: {short_side:.2f}")
    print("")
    input("Press enter to continue...")

