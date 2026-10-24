# container with most water

class Solution(): 
    def maxArea(self, height):

        left = 0 
        right = len(height) - 1

        max_area = 0 

        while left < right: 
            
            container_width = right - left

            variable_area = min(height[left], height[right]) * container_width
            max_area = max(max_area, variable_area)

            if height[left] < height[right]: 
                left += 1

            else: 
                right -= 1

        return max_area