# Search in a Singly Linked List

### Iterative method -O(n)

from LinkedList import LinkedList
from Node import Node


def search(lst, value):

    # Start from first element
    current_node = lst.get_head()

    # Traverse the list till you reach end
    while current_node:
        if current_node.data == value:
            return True  # value found
        current_node = current_node.next_element

    return False  # value not found


lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(40)
lst.insert_at_head(5)
lst.print_list()
print(search(lst, 4))


## Recursive method - O(n)

def search(node, value):

    # Base case
    if(not node):
        return False  # value not found

    # check if the node's data matches our value
    if(node.data is value):
        return True  # value found

    # Recursive call to next node in the list
    return search(node.next_element, value)


lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(40)
lst.insert_at_head(5)
lst.print_list()
print(search(lst.get_head(), 4))
