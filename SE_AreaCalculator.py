#This subroutine will get the length and width of the user's rectangle

def getRectangleSides():
    
    #Ask the user for the length and width of the rectangle
    width = input("Enter the width of the rectangle: ")
    length = input("Enter the length of the rectangle: ")
    #Return the width and length as floats
    return float(width), float(length)


   # This subroutine will validate if the dimensions of the rectangle
   # are valid. Valid dimensions are positive integers.
def validateRectangleDimensions(width, length):

    valid = True

    if width <= 0 or length <= 0:
        print("Invalid dimensions. Please enter positive values.")
        valid = False 
    
    return valid

# This subroutine will calculate the area of a rectangle given its width and length
# and display the result to the user. The area will be displayed to two decimal places.
def rectangleArea(width, length):

    area = width * length
    print(f"The area of the rectangle is: {float(area):.2f}")

# This is the main function for the area calculator module. It will call the other subroutines 
# to get the dimensions of the rectangle, validate them, and calculate the area if they are valid.
def rectangleAreaModule():
    
    width, length = getRectangleSides()
    validateRectangleDimensions(width, length)
    if validateRectangleDimensions(width, length):
        rectangleArea(width, length)
    else:
        print("Please enter valid dimensions for the rectangle.")

# This is the main function that displays a menu for the user to select a shape for area calculation.
# It will call the appropriate subroutine based on the user's selection. 
# The user can continue to select shapes until they choose to return to the main menu.
def areaModuleMenu():
    
    print("Welcome to the area calculator module.")

    user_area_selection = "99"
    while user_area_selection != 0:

        print("\nSelect a shape to calculate its area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("0. Back to main menu")

        # Get the user's selection and call the appropriate subroutine based on their choice.
        user_area_selection = input("Input the number of your selection: ")

        if user_area_selection == "1":
            rectangleAreaModule()
        elif user_area_selection == "2":
            pass
        elif user_area_selection == "3":
            pass
        elif user_area_selection == "0":
            return
        else:
            print("Invalid selection. Please try again.")

        # After the area calculation is done, ask the user if they want to continue with the area module or return to the main menu.
        print("")
        area_cont = input("To continue with the area module, press y. To return to the main menu, press any other key: ")
        if area_cont !="y":
            break
       
        

