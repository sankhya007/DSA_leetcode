class Solution(): 
    def decodeString(self, s): 
        stack = []
        current_string = ""
        current_number = 0 

        for c in s: 
            if c.isdigit(): 
                current_number = current_number * 10 + int(c)
            
            elif c == '[': 
                stack.append((current_string, current_number))
                current_string, current_number = "", 0

            elif c == "]": 
                prev_string, prev_number = stack.pop()
                current_string = prev_string + current_string * prev_number
            
            else: 
                current_string += c

        return current_string 