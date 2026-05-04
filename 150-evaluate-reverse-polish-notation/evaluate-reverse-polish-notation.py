class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"

        for token in tokens: 
            if token in operators: 
                b = stack.pop()
                a = stack.pop()

                if token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(int(a / b)) # trunkate towards zero 
                # you can not use "//" / round down function because 5 // 2 = 3 but int(5/2) = 2 closer to zero

            else: 
                stack.append(int(token))

        return stack[0]
        # after doing all that the stack is going to contain only one value but of we use return stack we are going to get a list in return like "[9]" and that is not what we want, we want a value like 9 that's why we are calling an index 