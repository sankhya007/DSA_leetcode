# valid parentheses 

class Solution(): 
    def isValid(self, s): 

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s: 
            if char in mapping: 
                # if the value of the popped element does not match the element in array return False
                # pop if stack has element
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element: 
                    return False
                    
            # append if there is opening bracket        
            else: 
                stack.append(char)

        return not stack