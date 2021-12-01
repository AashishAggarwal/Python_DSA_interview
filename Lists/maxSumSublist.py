# Given an integer list, return the maximum sublist sum. The list 
# may contain both positive and negative integers and is unsorted.

### 1st Method - O(n^2)

def find_max_sum_sublist(lst): 
  # Write your code here!
  if min(lst) >= 0:
    return sum(lst)
  max_sum = 0
  for i in range(len(lst)):
    for j in range(i, len(lst)):
      if max_sum < sum(lst[i:j]):
        max_sum = sum(lst[i:j])
  return max_sum

find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1])


### 2nd Method - Kadane's Algorithm - O(n)


def find_max_sum_sublist(lst): 
  if (len(lst) < 1): 
    return 0

  curr_max = lst[0]
  global_max = lst[0]
  length_array = len(lst)
  for i in range(1, length_array):
    if curr_max < 0: 
      curr_max = lst[i]
    else:
      curr_max += lst[i]
    if global_max < curr_max:
      global_max = curr_max

  return global_max


lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print("Sum of largest subarray: ", find_max_sum_sublist(lst))