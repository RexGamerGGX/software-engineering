from SE_Utils import clear_console
from SE_Validation import validatePositive
#This subroutine will get the length and width of the user's rectangle
def getRectangleSides():
    isValid = False    
    while isValid == False: 
        clear_console()
        #Ask the user for the length and width of the rectangle
        width = input("Enter the width of the rectangle. Whole numbers and decimals are allowed: ")
        length = input("Enter the length of the rectangle. Whole numbers and decimals are allowed: ")
        #Return the width and length as floats
        try:
            f_width = float(width)
            f_length = float(length)
            isValid = True
        except  ValueError:
            print("Invalid input. Please enter valid numbers using (.) for decimals.")
            quit = input("To quit the area calculator menu, press q. To try again, press enter: ")
            if (quit == "q"):
                return 0, 0, False

    return f_width, f_length, isValid

# This subroutine will calculate the area of a rectangle given its width and length
# and display the result to the user. The area will be displayed to two decimal places.
def rectangleArea(width, length):

    area = width * length
    print(f"The area of the rectangle is: {float(area):.2f}")
    print("")
    input("Press enter to continue...")

# This is the main function for the area calculator module. It will call the other subroutines 
# to get the dimensions of the rectangle, validate them, and calculate the area if they are valid.
def rectangleAreaModule():
    

    width, length, isValid = getRectangleSides()
# 
    if isValid and validatePositive(width) and validatePositive(length):
        rectangleArea(width, length)
    else:
        input("Press enter to continue...")