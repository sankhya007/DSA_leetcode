# implement a stack using queue

from collections import deque

class MyStack: 
    def __init__(self):
        # double ended queue 
        self.q = deque()

    # left = top (gives out)
    # right = bottom (gets in)
    def push(self, x): 
        self.q.append(x)

        # for each off the values we pop and append it in left/back
        for _ in range(len(self.q) - 1): 
            self.q.append(self.q.popleft())

    # pop top/left item
    def pop(self): 
        return self.q.popleft()

    # return top most/left most value
    def top(self): 
        return self.q[0]

    # check if queue empty
    def empty(self): 
        return len(self.q) == 0 
