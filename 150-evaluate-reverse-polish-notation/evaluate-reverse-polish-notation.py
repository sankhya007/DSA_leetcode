# evaluate reverse polish Notation 

class Solution(): 
    def evalRPN(self, tokens): 

        stack = []
        operators = "+-*/"

        for token in tokens: 
            if token in operators: 

                # assign elements
                b = stack.pop() # right element
                a = stack.pop() # left element 

                # get the values form the stack and add the operator function mentioned 
                if token == '+': 
                    stack.append(a + b)

                elif token == '-': 
                    stack.append(a - b)

                elif token == "*": 
                    stack.append(a * b)

                # no float value
                elif token == "/": 
                    stack.append(int(a / b))

            # if a value then add to the stack, make int so further calculation possible
            else: 
                stack.append(int(token))

        return stack[0]