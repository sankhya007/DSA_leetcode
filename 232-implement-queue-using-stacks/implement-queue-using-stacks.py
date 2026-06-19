class MyQueue: 
    def __init__(self): 
        self.in_stack = []
        self.out_stack = [] # initialize
    def push(self, x): 
        self.in_stack.append(x) 
    def pop(self): 
        self.peek()
        return self.out_stack.pop()
    def peek(self): 
        if not self.out_stack: # is no value in out 
            while self.in_stack: # and value in "in"
                self.out_stack.append(self.in_stack.pop()) # reverse add from in to out 
        return self.out_stack[-1] # return last element - actually 1st 
    def empty(self): 
        return not self.in_stack and not self.out_stack