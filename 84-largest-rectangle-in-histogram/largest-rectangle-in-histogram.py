class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0 
        heights.append(0)
        for i, h in enumerate(heights): 
            while stack and heights[stack[-1]] > h: # the one we are looking at is smaller than the last one 
                height = heights[stack.pop()] 
                width = i if not stack else i - stack[-1] - 1 #right - left - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area