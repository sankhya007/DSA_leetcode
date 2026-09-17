class Solution:
    def largestRectangleArea(self, heights):

        # storage
        stack = []

        max_area = 0 
        # so everything process
        heights.append(0)

        for i, h in enumerate(heights): 

            # till increasing we keep going 
            # when hit a smaller one we stop
            while stack and heights[stack[-1]] > h: 

                # assign the height
                height = heights[stack.pop()]

                # when stack has no value
                # else, current - last height - left boundary
                # not heights[stack] coz we are counting the index and stack only have the indexs and heights have the values
                width = i if not stack else i - stack[-1] -1 

                max_area = max(max_area, height * width)

            # only append the index when in increasing order
            stack.append(i)

        return max_area