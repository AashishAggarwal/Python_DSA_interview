# Implement a function called evaluatePostFix() that will 
# compute a postfix expression given to it as a string.

from Stack import MyStack

def evaluate_post_fix(exp):
    stack = MyStack()
    try:
        for char in exp:
            if char.isdigit():
                # Push Numbers in stack
                stack.push(char)
            else:
                right = stack.pop()
                left = stack.pop()
                '''Using Python eval () method that takes a str expression,
                    evaluates it and returns an integer.'''
                stack.push(str(eval(left + char + right)))
        # Final answer should be a number
        return int(float(stack.pop()))
    except TypeError:
        return "invalid Sequence"


if __name__ == "__main__" :
    print("Result of expression (921*-8-4+) : " + str(evaluate_post_fix("921*-8-4+")))
    print("Result of expression (921*-8--4+) : " + str(evaluate_post_fix("921*-8--4+")))