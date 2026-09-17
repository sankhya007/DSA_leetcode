class Solution(): 
    def generateParenthesis(self, n): 

        result = []

        def backtrack(current, open, close): 

            if len(current) == n * 2: # goal reached
                result.append(current)
                return result 

            if open < n: # haven't placed enough opening brackets
                backtrack(current + "(", open + 1, close)

            if close < open: # haven't placed enough closing brackets
                backtrack(current + ")", open, close + 1) 

        backtrack("", 0, 0)
        return result