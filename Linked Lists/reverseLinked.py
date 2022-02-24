# Implement a program which could reverse a linked list

from Node import Node
from LinkedList import LinkedList
#Access head_node => list.get_head()
#Check if list is empty => list.is_empty()
#Delete at head => list.delete_at_head()
#Delete by value => list.delete(value)
#Search for element => list.search()
#Length of the list => list.length()
#Node class  { int data ; Node next_element;}

def reverse(lst):
  # To reverse linked, we need to keep track of three things
  previous = None # Maintain track of the previous node
  current = lst.get_head() # The current node
  next = None # The next node in the list

  #Reversal
  while current:
    next = current.next_element
    current.next_element = previous
    previous = current
    current = next

    #Set the last element as the new head node
    lst.head_node = previous
    # lst.print_list()
  return lst

lst = LinkedList()
lst.insert_at_head(6)
lst.insert_at_head(4)
lst.insert_at_head(9)
lst.insert_at_head(10)
lst.print_list()

reverse(lst)
lst.print_list()