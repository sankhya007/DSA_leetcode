class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {")" : "(", "}" : "{", "]" : "["}

        for ch in s: 
            if ch in mapping: 
                top_element = stack.pop() if stack else "#"
                if mapping[ch] != top_element: 
                    return False
            else: 
                stack.append(ch)

        # the stack has to be empty to make sure that input like this "((" are not in the stack
        return not stack
