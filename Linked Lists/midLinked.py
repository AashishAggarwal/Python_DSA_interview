# Find the Middle Value in a Linked List challenge.

### Method 1 - O(n)

from LinkedList import LinkedList
from Node import Node
# Access HeadNode => list.getHead()
# Check length => list.length()
# Check if list is empty => list.isEmpty()
# Node class  { int data ; Node nextElement;}


def find_mid(lst):
    if lst.is_empty():
        return None

    node = lst.get_head()
    mid = 0
    if lst.length() % 2 == 0:
        mid = lst.length()//2
    else:
        mid = lst.length()//2 + 1

    for i in range(mid - 1):
        node = node.next_element

    return node.data


lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()
print(find_mid(lst))


### 2nd Method - O(n)
# faster because the calculation of the length and the 
# traversal till the middle are happening side-by-side.

from LinkedList import LinkedList
from Node import Node
def find_mid(lst):
  if lst.is_empty():
    return -1
  current_node = lst.get_head()
  if current_node.next_element == None:
		#Only 1 element exist in array so return its value.
    return current_node.data
  
  mid_node = current_node
  current_node = current_node.next_element.next_element
  #Move mid_node (Slower) one step at a time
  #Move current_node (Faster) two steps at a time
  #When current_node reaches at end, mid_node will be at the middle of List 
  while current_node:
    mid_node = mid_node.next_element
    current_node = current_node.next_element
    if current_node:
      current_node = current_node.next_element
  if mid_node:
    return mid_node.data
  return -1

lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()
print(find_mid(lst))