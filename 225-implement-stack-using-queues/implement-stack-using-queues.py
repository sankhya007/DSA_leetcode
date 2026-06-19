from collections import deque
class MyStack: 
    def __init__(self): 
        self.q = deque() #deque = double ended queue
    def push(self, x): 
        self.q.append(x) 
        for _ in range(len(self.q) - 1): # pop all values 
            self.q.append(self.q.popleft()) # from left and append in right 
    def pop(self): 
        return self.q.popleft()
    def top(self): 
        return self.q[0]
    def empty(self): 
        return len(self.q) == 0
