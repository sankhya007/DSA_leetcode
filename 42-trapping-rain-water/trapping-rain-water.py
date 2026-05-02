class Solution:
    def trap(self, height):
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        trapped_water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    trapped_water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    trapped_water += max_right - height[right]
                right -= 1
        return trapped_water
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
solution = Solution()
print(solution.trap(height))