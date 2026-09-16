# valid parentheses 

class Solution(): 
    def isValid(self, s): 

        stack = []

        mapping = {")": "(", "}": "{", "]": "["} 

        # suppose s = "({[]})"

        for char in s: 

            # check if it is a closing bracket
            if char in mapping: 

                # top element of stack matches the value of the closing bracket
                top_element = stack.pop() if stack else "#"

                # value under mapping(opening bracket) is not equal to top element return false
                if mapping[char] != top_element :
                    return False

            # all the opening brackets will be appended in the stack
            else: 
                stack.append(char)

        # if stack empty
        return not stack