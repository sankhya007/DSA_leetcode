class MinStack:

    def __init__(self):
        self.stack =[]
        self.min_stack = [] # here we are initializinf the both stacks of both of the storages all together 

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(val if not self.min_stack else min(val, self.min_stack[-1]))
        # here we are appending the val to the min_stack if the min_stack is empty and if it is not empty then we are going to compare the val with the topmost elemnt of the min stack and then append the smallest one 

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop() # here we are jut popping the topmost element in each of the stacks

    def top(self) -> int:
        return self.stack[-1] # to get the top element we just have to return the top elemnt of the normal stack and that is what we are meant to do as per the instruction 

    def getMin(self) -> int:
        return self.min_stack[-1] # to get the minimum number we would have the topmost element in the min_stack because min stack is apppendingg the smallest elements in the array and that's why it is meant to have the smallest element so to get the min we would have to return that  


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()