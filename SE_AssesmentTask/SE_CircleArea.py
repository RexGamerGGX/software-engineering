from SE_Validation import validatePositive, validateIntegerDataInput 
from SE_Utils import clear_console
# This subroutine will get the radius of the user's circle
def getCircleSides():


    isValid = False 

    clear_console()   
   
    #Get the radius of the circle from the user, and return it as an integer, along with whether or not it is valid
    isValid, outputs = validateIntegerDataInput("Enter the radius of the circle: ")
    if isValid:
        int_radius = outputs[0]
        return int_radius, isValid
    
    return 0, False

# This subroutine will calculate the area of a circle given its radius
# and display the result to the user. The area will be displayed to two decimal places.
def circleArea(radius):

    area = 3.14159 * radius * radius
    print(f"The area of the circle is: {area:.2f}")
    print("")
    input("Press enter to continue...")

# This is the main function for the circle area calculator module. It will call the other subroutines
# to get the dimensions of the circle, validate them, and calculate the area if they are valid.
def circleAreaModule():

    radius, isValid = getCircleSides()

    # Validate the radius. If it is valid, calculate the area of the circle.
    if isValid and validatePositive(radius):
        circleArea(radius)
    else:
        input("Press enter to continue...")
