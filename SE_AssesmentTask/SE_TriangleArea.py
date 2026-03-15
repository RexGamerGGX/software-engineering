from SE_Validation import validatePositive
from SE_Utils import clear_console
# This subroutine will get the base and height of the user's triangle
def getTriangleDimensions():

    clear_console()
    #ask the user for the base and height of the triangle
    base = input("Enter the base of the triangle. Whole numbers and decimals are allowed: ")
    height = input("Enter the height of the triangle. Whole numbers and decimals are allowed: ")
    #return the base and height as floats
    return float(base), float(height)

# This subroutine will calculate the area of a triangle given its base and height
# and display the result to the user. The area will be displayed to two decimal places.
def triangleArea(base, height):

    area = 0.5 * base * height
    print(f"The area of the triangle is: {float(area):.2f}")

# This is the main function for the triangle area calculator module. It will call the other subroutines
# to get the dimensions of the triangle, validate them, and calculate the area if they are valid.
def triangleAreaModule():

    base, height = getTriangleDimensions()

    # Validate the base and height. If they are valid, calculate the area of the triangle.
    if validatePositive(base) and validatePositive(height):
        triangleArea(base, height)
