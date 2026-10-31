class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspace(n):
            stack = []
            for ch in n: 
                if ch.isalpha(): 
                    stack.append(ch)
                if stack and ch == "#": 
                    stack.pop()
            return stack

        result1 = backspace(s)
        result2 = backspace(t)

        return result1 == result2
            