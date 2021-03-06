# Write a function that takes a number testVariable and
# returns a string that is its equivalent binary number.

def decimalToBinary(testVariable):
    # Write your code here
    if testVariable <= 1:
        return str(testVariable)
    
    # Recursive case
    else:
        return decimalToBinary(testVariable // 2) + decimalToBinary(testVariable % 2)   # Floor division - 
        # division that results into whole number adjusted to the left in the number line

# Driver Code
testVariable = 11
print(decimalToBinary(testVariable))