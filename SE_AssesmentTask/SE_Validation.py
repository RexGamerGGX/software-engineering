# This subroutine will validate if the dimensions entered by the user for area calculation are valid. 
# It will return whether or not the dimensions are valid. Valid dimensions are positive integers.
def validatePositive(value):

    valid = True
    # Check if the value is positive. If it is not, it is invalid.
    if value <= 0:
        print("Invalid dimensions. Please enter positive values.")
        valid = False 
    
    return valid

# This subroutine will validate if the data entered by the user for area calculation is valid.
# It will return whether or not the data is valid, and the data as integers if it is valid. Valid data are integers (no decimals).
def validateIntegerDataInput(*args):
    valid = True
    outputs = []
    for value in args:
        valid_input = False
        while valid_input == False:
            temp_input = input(value)
             # Attempt to convert the data to integers in a "try". If this fails it will be caught in the "except". 
             # If it is valid, it will be returned as integers.
            try:
                temp_input = int(temp_input)
                outputs.append(temp_input)
                valid_input = True
            except ValueError:
                print("Invalid input. Please enter valid integers (no decimals).")
                print("")
                # if the input is invalid, ask the user if they want to try again. If they do not, return that the data is invalid.
                choice = input("Press y to try again, or enter to quit: ")
                if choice != "y":
                    return False , []    

    return valid, outputs