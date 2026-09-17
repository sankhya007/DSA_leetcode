# generate parenthesis 

class Solution(): 
    def generateParenthesis(self, n): 

        result = []

        def backtrack(current, open, close): 

            # current - the string bulit so far
            # open - how many ( used so far(we can have n number of opening brackets)
            # close - how many ) used so far(same as open)

            # of length double then - reached goal
            # append in stack and return
            if len(current) == 2 * n: 
                result.append(current)
                return

            # meaning we have more opening brackets left, place another opening bracket and recurse with open + 1
            if open < n: 
                backtrack(current + "(", open + 1, close) 

            # meaning close == open, add another ")" to the current and recurse with close + 1 
            if close < open: 
                backtrack(current + ")", open, close + 1)

        # is to start the recursion with an empty space
        backtrack("", 0, 0)

        return result







