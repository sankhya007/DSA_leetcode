class Solution:
    def calPoints(self, operations: list[str]) -> int:
        
        stack = []
        # new array 

        for opr in operations: 
            if opr == "+": 
                stack.append(stack[-1] + stack[-2])
            elif opr == "D": 
                stack.append(stack[-1]*2)
            elif opr == "C": 
                stack.pop()
            else: 
                stack.append(int(opr))

        return sum(stack)