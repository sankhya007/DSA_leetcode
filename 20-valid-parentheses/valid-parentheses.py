class Solution: 
    def isValid(self, s): 
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s: 
            if char in mapping: 
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element: # check if closing bracket
                    return False
            else: 
                stack.append(char) # append if opening bracket
        return not stack 