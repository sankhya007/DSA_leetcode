# simplify path - leetcode

class Solution(): 
    def simplifyPath(self, path): 

        stack = []

        for part in path.split("/"): 
            if part == "..": 
                if stack: 
                    stack.pop()

            # check if part, because it can be empty in case if //
            # we already filter out ".."
            # so we need to think about letters and "."
            # if not "." means it only can be a letter
            # add that letter to the stack 
            # because "." means we in same directory

            elif part and part != ".": 
                stack.append(part)

            # there will be a "/" in the front 
            # anything else will be only letters 
            # have "/" space them in-between
            
        return "/" + "/".join(stack)