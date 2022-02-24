# You are required to implement the next_greater_element() function. 
# For each element i in a list, # the function finds the first element 
# to its right which is greater than element i. If for any element 
# such a value does not exist, the answer is -1.

from Stack import MyStack

# Brute Force - O(n^2)
def next_greater_element1(lst):
    # stack = MyStack()
    res = []
    for i in range(len(lst)):
        # initialize nextGreatest to -1
        nextGreatest = -1
        for j in range(i+1, len(lst)):
            # update nextGreatest when greater value found
            if lst[j] > lst[i]:
                nextGreatest = lst[j]
                break
        # append next greatest
        res.append(nextGreatest)
        print(str(lst[i]) + " -- " + str(nextGreatest))
    return res

# Using Stack integration
def next_greater_element2(lst):
    stack = MyStack()
    res = [-1] * len(lst)
    for i in range(len(lst)):
        # initialize nextGreatest to -1
        nextGreatest = -1
        for j in range(i+1, len(lst)):
            # update nextGreatest when greater value found
            if lst[j] > lst[i]:
                nextGreatest = lst[j]
                break
        # append next greatest
        res.append(nextGreatest)
        print(str(lst[i]) + " -- " + str(nextGreatest))
    return res


if __name__ == "__main__" :
    next_greater_element1([4, 6, 3, 2, 8, 1, 9, 9, 9])
    next_greater_element2([4, 6, 3, 2, 8, 1, 9, 9, 9])