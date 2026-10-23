# trapping rain water

class Solution(): 
    def trap(self, height): 

        # if nothing in array return 0
        if not height: 
            return 0 

        # two pointer
        left = 0 
        right = len(height) - 1

        # max_pointers
        max_left = 0 
        max_right = 0 

        # water storage
        trapped_water = 0 

        # two pointer loop
        while left < right: 

            # if left small then left move towards middle
            if height[left] < height[right]: 
                # if left is smaller than max left means the bar has depth, so we add however much depth the bar is adding
                if height[left] >= max_left: 
                    max_left = height[left]

                else: 
                    # trapped water getting added one by one in increments
                    trapped_water += max_left - height[left]

                # increment
                left += 1

            # if right small then right move towards middle
            else: 
                # if the max_right is smaller than the right then we add the depth that it has in the trapped water
                if height[right] >= max_right: 
                    max_right = height[right]

                else: 
                    trapped_water += max_right - height[right]

                # increment
                right -= 1 

        return trapped_water