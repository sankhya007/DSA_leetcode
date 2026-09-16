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
                    # use absolute values 
                    result = abs(a) // abs(b)

                    # trying to figure out of one value is negative or not, if so then turn result -ve and append. else, ignore and append 
                    if (a < 0) != (b < 0): 
                        result = -result 

                    stack.append(result)

            # if a value then add to the stack, make int so further calculation possible
            else: 
                stack.append(int(token))

        return stack[0]