# Implement a function findMinimum(lst) which finds the smallest number in the given list.

def find_minimum(arr):
    # Write your code here
    mini = arr[0]
    for num in arr:
        if num <= mini:
            mini = num
    return mini 

### 2nd Method - O(nlogn)

def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    lst.sort()  # sort list
    return lst[0]  # return first element


print(find_minimum([9, 2, 3, 6]))

### 3rd Method - O(nlogn)

def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              my_list[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                my_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k]=right[j]
            j += 1
            k += 1


def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    merge_sort(lst)  # sort list
    return lst[0]  # return first element


print(find_minimum([9, 2, 3, 6]))

### 4th method - O(n)

def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    minimum = lst[0]
    for ele in lst:
        # update if found a smaller element
        if ele < minimum:
            minimum = ele
    return minimum


print(find_minimum([9, 2, 3, 6]))
