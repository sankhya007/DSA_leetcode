class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = [] # initializing both of the stacks 

    def push(self, x: int) -> None:
        self.in_stack.append(x) # only the  instack will append values 

    def pop(self) -> int:
        self.peek() # here to make the stacks act like queue 
        return self.out_stack.pop() # just pop the top most eleemnt after doing the peek 

    def peek(self) -> int:
        if not self.out_stack: 
            while self.in_stack: 
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1] # litrallry go through it in the opposite direction and pop out the exact opposite number of the stack you 1st had, coz you fkn reversed it

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack # if everything is empty return true 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()