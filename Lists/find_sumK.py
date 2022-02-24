### Brute Force

def find_sum(lst, k):
    # iterate lst with i
    for i in range(len(lst)):
        # iterate lst with j
        for j in range(len(lst)):
            # if sum of two iterators is k
            # and i is not equal to j
            # then we have our answer
            if(lst[i]+lst[j] is k and i is not j):
                return [lst[i], lst[j]]


print(find_sum([1, 2, 3, 4], 5))

### 2nd Method

def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


def find_sum(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k -lst[j])
        if index is not -1 and index is not j:
            return [lst[j], k -lst[j]]
    


print(find_sum([1, 5, 3], 2))
print(find_sum([1, 2, 3, 4], 5))


### 3rd Method

def find_sum(lst, k):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False


print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))