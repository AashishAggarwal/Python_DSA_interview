# Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.

def find_product(lst):
    # Write your code here
    product = []
    for i in range(len(lst)):
        prod = 1
        for j in range(len(lst)):
            if j == i:
                continue
            prod *= lst[j]
        product.append(prod)
    return product    
         
print(find_product([1, 2, 3, 4]))


### 2nd Method

def find_product(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result


print(find_product([1, 2, 3, 4]))


### 3rd Method

def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


print(find_product([1, 2, 3, 4]))
