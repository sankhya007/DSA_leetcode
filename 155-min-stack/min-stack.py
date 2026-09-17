class MinStack: 

    def __init__(self): 

        # initialize storage
        self.stack = []
        self.min_stack = []

    def push(self, val): 

        # if empty add-on, else compare top most add the smallest
        self.stack.append(val)
        self.min_stack.append(val if not self.min_stack else min(val, self.min_stack[-1]))

    def pop(self): 

        # pop the last element
        self.stack.pop()
        self.min_stack.pop()

    def top(self): 

        # view the top element
        return self.stack[-1]

    def getMin(self): 

        # minimum number is the top most element of the min_ stack
        return self.min_stack[-1]