from SE_Validation import validatePositive, validateIntegerDataInput 
from SE_Utils import clear_console
# This subroutine will get the radius of the user's circle
def getCircleRadius():


    isValid = False 

    clear_console()   
   
    #Get the radius of the circle from the user, and return it as an integer, along with whether or not it is valid
    print("Enter the radius of the circle to calculate its area (positive integers only).")
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
# Return string "Main" if the user wants to return to the main menu, and return None if they want to return to the area calculator menu.
def circleAreaModule():
    while True:
        radius, isValid = getCircleRadius()

        # Validate the radius. If it is valid, calculate the area of the circle.
        if isValid and validatePositive(radius):
            circleArea(radius)
        else:
            input("Press enter to continue...")

        # After calculating the area, ask the user if they want to calculate the area of another circle
        # or return to the area calculator menu.
        print ("")
        print("What would you like to do next?")
        print("1. Calculate the area of another circle")
        print("2. Back to area calculator menu")
        print("0. Back to main menu.")

        # If they want to calculate the area of another circle, repeat the process.
        # If they want to return to the area calculator menu, return from the function.
        # If they enter an invalid option, return to the area calculator menu.
        choice = input("Enter the number of your selection: ")
        
        if choice == "1":
            continue
        elif choice == "2":
            return
        elif choice == "0":
            return "Main"
        else:
            print("Invalid selection. Returning to area calculator menu.")
            input("Press enter to continue...")
            return
