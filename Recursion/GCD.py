# Implement a function that takes two numbers, testVariable1 
# and testVariable2 and returns their greatest common divisor.

def gcd(testVariable1, testVariable2) :
  # Base Case
    if testVariable1 == testVariable2:
        return testVariable1

    # Recursive Case
    if testVariable1 > testVariable2:
        return gcd(testVariable1 - testVariable2, testVariable2)
    else:
        return gcd(testVariable1, testVariable2 - testVariable1)

# Driver Code
number1 = 42
number2 = 56
print(gcd(number1, number2))