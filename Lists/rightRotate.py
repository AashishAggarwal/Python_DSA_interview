# Implement a function right_rotate(lst, k) which will rotate the given list by k. 
# This means that the right-most elements will appear at the left-most position in the list and so on.

### 1st method - O(n)

def right_rotate(lst, k):
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], abs(3)))


### 2nd Method - O(n)

def right_rotate(lst, k): 
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        rotatedList.append(lst[item])
    return rotatedList


print(right_rotate([10, 20, 30, 40, 50], abs(3)))