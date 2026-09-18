# implement queue using stack

# __init__
# push 
# pop
# top 
# empty 

from collections import deque 

class MyStack: 
    
    # initialize double sided queue
    def __init__(self): 
        self.q = deque()

    # add new number in right, loop through the old numbers pull them back from left and add them from the right
    def push(self, x): 
        self.q.append(x)

        for _ in range(len(self.q) - 1): 
            self.q.append(self.q.popleft())

    # pop the leftmost or the topmost item
    def pop(self): 
        return self.q.popleft()

    # return the 1st element form left
    def top(self): 
        return self.q[0]

    # check if has element or no
    def empty(self): 
        return len(self.q) == 0