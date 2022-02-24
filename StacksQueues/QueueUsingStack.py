# You have to implement the enqueue() and dequeue() functions using the MyStack class we created earlier. 
# enqueue( ) will insert a value into the queue and dequeue( ) will remove a value from the queue.

from unittest.main import MAIN_EXAMPLES
from Stack import MyStack

# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


# Two Stack working in enqueue()
class newQueue1:

    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()
    
    # Inserts element in the queue - O(n)
    def enqueue(self, value):
        # Push value in main stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
            print(str(value) + " init main enqueued")
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            # Inserting value in the queue
            self.main_stack.push(value)
            print(str(value) + " temp enqueued")
            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())

    # Removes element from queue - O(1)
    def dequeue(self):
        # If stack empty return none
        if self.main_stack.is_empty():
            return None
        value = self.main_stack.pop()
        print(str(value) + " main dequeued")
        return value


# Two Stack working in dequeue()
class newQueue2:

    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()
    
    # Inserts element in the queue - O(1)
    def enqueue(self, value):
        # Push value in main stack in O(1)
        self.main_stack.push(value)
        print(str(value) + " enqueued")

    # Removes element from queue - O(1)
    def dequeue(self):
        # If both stack empty return none
        if not self.temp_stack.is_empty():
            front = self.temp_stack.pop()
            print(str(front) + " dequeued")
            return front
        if self.temp_stack.is_empty() and self.main_stack.is_empty():
            return None
        # Transfer all elements to temp stack
        while not self.main_stack.is_empty():
            self.temp_stack.push(self.main_stack.pop())
        front = self.temp_stack.pop()
        print(str(front) + " dequeued")
        return front



if __name__ == "__main__" :
    queue = newQueue1()
    for i in range(5):
        queue.enqueue(i+1)
    print("----------")
    for i in range(5):
        queue.dequeue()
    print("----------")

    queue = newQueue2()
    for i in range(5):
        queue.enqueue(i+1)
    print("----------")
    for i in range(5):
        queue.dequeue()
