class Solution:
    def trap(self, height):
        if not height:
            return 0
        # this is so if the list if empty the return is 0(no water trapped)

        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        trapped_water = 0 # all the variable containters

        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left] # to get the max height of the left wall we draw this equation
                else:
                    trapped_water += max_left - height[left] # this is done in one block so thats why it looks like thuis its collects both of the side of a single piller and then does the calculation
                left += 1

            else: # height[right] < height[left]
                if height[right] >= max_right:
                    max_right = height[right] # to get the max right wall height
                else:
                    trapped_water += max_right - height[right] # also calculating one block similler to the previous block's calculation
                right -= 1

        return trapped_water

        
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
solution = Solution()
print(solution.trap(height))