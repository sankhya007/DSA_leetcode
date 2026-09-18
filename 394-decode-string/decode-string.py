class Solution(): 
    def decodeString(self, s): 
        stack = []
        current_string = ""
        current_number = 0 

        for c in s: 

            if c.isdigit(): 
                # multiply by 10 step added to then if the number is in double digits like "32, 41" we can have a int form of that, and for single digits it is getting multiplied with 0 so don't cause a difference
                current_number = current_number * 10 + int(c)

            elif c == '[': 
                # stack append and variable reset
                stack.append((current_string, current_number))
                current_string, current_number = "", 0

            elif c == ']': 
                # assign values
                prev_string, num = stack.pop()

                # the number will be in front so that's why we are multiplying the current_string with the previous number
                current_string = prev_string + current_string * num

            # if we have more than one string alongside of each other
            else: 
                current_string += c 

        return current_string





