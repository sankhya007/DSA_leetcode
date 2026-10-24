class Solution(): 
    def evalRPN(self, tokens): 
        
        stack = []
        operators = "+-*/"

        for token in tokens: 
            if token in operators:
                
                # 2nd element pops 1st so b will pop 1st
                b = stack.pop()
                a = stack.pop()

                if token == "+": 
                    stack.append(a + b)
                
                if token == "-": 
                    stack.append(a - b)

                if token == "*": 
                    stack.append(a * b)

                if token == "/": 
                    result = abs(a) // abs(b)
                    
                    if (a < 0) != (b < 0): 
                        result = -result

                    stack.append(result)

            else: 
                stack.append(int(token))

        return stack[0]