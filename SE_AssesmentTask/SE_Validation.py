# This subroutine will validate if the dimensions of the rectangle
   # are valid. Valid dimensions are positive integers.
def validatePositive(value):

    valid = True

    if value <= 0:
        print("Invalid dimensions. Please enter a positive value.")
        valid = False 
    
    return valid