# valid parenthesis

class Solution(): 
    def isValid(self, s):

        stack = []
        # opening bracket as the value of the closing brackets
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s: 
            '''
            if not closing bracket - add in stack 
            if closing bracket, pop value from stack
            store in temp_element, compare 
            if match - true, else False
            true = return not stack meaning,the stack is empty
            '''
            if char in mapping:  
                if mapping[char] != stack.pop() if stack else "#":
                    return False
            else: 
                stack.append(char)

        return not stack