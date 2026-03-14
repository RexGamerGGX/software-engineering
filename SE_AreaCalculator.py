#This subroutine will get the lenght and width of the user's rectangle

def getRectangleSides():
    
    #Ask the user for the lenght and width of the rectangle
    width = input("Enter the width of the rectangle: ")
    length = input("Enter the length of the rectangle: ")

    dimensions = length , width
   
def validateDimensions(dimensions):

    valid = True

    try:
        for dimension in dimensions:
            intDimensions = int(dimensions)
            if intDimensions <= 0:
                valid = False
    except ValueError:
        valid = False
    return valid

# This function displays a menu for the user to select a shape for area calculation.

def areaModuleMenu():

    user_area_selection = "99"
    while user_area_selection != 0:

        print("Which shape's area do you wish to calculate?")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("0. Back to main menu")

        user_area_selection = input("Input the number of your selection: ")

        if user_area_selection == "1":
            pass
        if user_area_selection == "2":
            pass
        if user_area_selection == "3":
            pass
        if user_area_selection == "0":
            return

