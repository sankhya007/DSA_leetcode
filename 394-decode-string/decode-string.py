class Solution: 
    def decodeString(self, s): 
        stack = []
        current_string = ""
        current_number = 0 
        for c in s: 
            if c.isdigit(): 
                current_number = current_number * 10 + int(c) # add space "0"
            elif c == '[': 
                stack.append((current_string, current_number)) # add in stack
                current_string, current_number = "", 0 # reset back 
            elif c == ']': 
                prev_string, num = stack.pop() # assign value
                current_string = prev_string + current_string * num # multiply with current
            else: 
                current_string += c # is two strings together
        return current_string 