# Implement a function that takes a number testVariable and returns 
# the row of the Pascal’s triangle corresponding with that number.

from pyparsing import line


def printPascal(testVariable) :
  # Write your code here
    # Base case
    if testVariable == 0:
        return [1]
    
    else:
        # recursive case
        line = [1]

        previousLine = printPascal(testVariable - 1)
        for i in range(len(previousLine) - 1):
            line.append(previousLine[i] + previousLine[i+1])
        line += [1]
    return line

# Driver Code
testVariable = 5
print(printPascal(testVariable))