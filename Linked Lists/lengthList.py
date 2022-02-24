# write a function which can tell us the length of a linked list. - O(n)

from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Node class attributes: {data, next_element}


def length(lst):
    # Write - Your - Code
    length = 0
    if lst.is_empty():
        return length
    
    curr_node = lst.get_head()
    while curr_node:
        length += 1
        curr_node = curr_node.next_element
    
    return length
