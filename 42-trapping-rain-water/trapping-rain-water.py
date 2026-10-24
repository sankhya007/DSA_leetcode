class Solution(): 
    def trap(self, heights): 
        
        if not heights: 
            return 0

        trapped_water = 0 

        left = 0 
        right = len(heights) - 1

        max_left = 0 
        max_right = 0 

        while left <= right: 

            # meaning left have to move forward
            if heights[left] < heights[right]: 
                # if height[left] greater ir equal = will not hold water
                if heights[left] >= max_left: 
                    # max_height change
                    max_left = heights[left]
                # if the height small = will store water
                else: 
                    # incremental increase
                    trapped_water += max_left - heights[left]
                # move to the next piller
                left += 1

            else: # height[right] < height[left]: 
                if heights[right] >= max_right: 
                    max_right = heights[right]
                else: 
                    trapped_water += max_right - heights[right]
                right -= 1

        return trapped_water