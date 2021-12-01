# Implement a function rearrange(lst) which rearranges the elements such that all the 
# negative elements appear on the left and positive elements appear at the right of the list.

### 1st Method - O(n)

def rearrange(lst):
    neg = []
    pos = []
    # make a list of negative and positive numbers
    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
    # merge two lists and return
    return neg + pos


print(rearrange([10, -1, 20, 4, 5, -9, -6]))

### 2nd Method - O(n)

def rearrange(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if lst[curr] < 0:
            # if not the last negative number
            if curr != leftMostPosEle:
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst


print(rearrange([10, -1, 20, 4, 5, -9, -6]))

### 3rd Method - O(n)

def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


print(rearrange([10, -1, 20, 4, 5, -9, -6]))
