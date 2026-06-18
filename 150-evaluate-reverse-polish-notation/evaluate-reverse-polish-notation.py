class Solution: 
    def evalRPN(self, tokens): 
        stack = []
        operators = "+-*/"
        for token in tokens: 
            if token in operators: 
                b = stack.pop() # right
                a = stack.pop() # left (position of the right and left matters)
                if token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(int(a / b))
            else: 
                stack.append(int(token)) # if an value - add in stack as int
        return stack[0]
