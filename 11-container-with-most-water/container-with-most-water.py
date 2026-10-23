# container with most water

class Solution(): 
    def maxArea(self, height): 

        left = 0 
        right = len(height) - 1

        max_area = 0 

        while left < right: 

            # width
            container_width = right - left
            # area
            valiable_area = min(height[left], height[right]) * container_width
            # max_area(just in case)
            max_area = max(max_area, valiable_area)

            # two pointer movement towards middle
            # we need to get the max height else 
            # which ever side is smaller we go towards the middle from that side to else accounting the larger height the water will spill
            if height[left] < height[right]: 
                left += 1

            else: 
                right -= 1 

        return max_area