class Solution(): 
    def simplifyPath(self, path): 

        stack = []

        for part in path.split("/"): 
            
            if part == "..": 
                if stack: 
                    stack.pop()

            elif part and part != ".": 
                stack.append(part)

        return "/" + "/".join(stack)
