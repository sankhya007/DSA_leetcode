class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []

        for c in s: 

            # if something in stack that matches the current element, pop that element from stack
            # if it does not match add that element in stack 
            if stack and stack[-1] == c: 
                stack.pop()
            else: 
                stack.append(c)

        return "".join(stack)