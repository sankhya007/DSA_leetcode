class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0) # this is just a dummy element that we are adding

        for i, h in enumerate(heights): # turn them into two sets 
            while stack and heights[stack[-1]] > h: # if the stack has some elements compare the top element of the stack with thewith the recent height with the loop element 
                height = heights[stack.pop()] # pop the top element of the stack as height 
                width = i if not stack else i - stack[-1] - 1 # i if the stack is empty and if there is a value in the stack then so the following 
                max_area = max(max_area, height * width) # get the max 
            stack.append(i) # append every element 

        return max_area 