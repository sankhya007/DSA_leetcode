class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        current_string = ""
        current_number = 0

        for c in s: 
            if c.isdigit(): 
                current_number = current_number * 10 + int(c)
            elif c == '[': 
                stack.append((current_string, current_number))
                current_string, current_number = "", 0 
            elif c == ']': 
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else: 
                current_string += c

        return current_string