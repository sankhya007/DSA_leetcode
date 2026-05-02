class Solution:
    def maxArea(self, height): 
        left = 0 
        right = len(height) - 1
        max_area = 0 
        while left < right: 
            width = right - left
            current_area = min(height[right], height[left]) * width 
            max_area = max(max_area, current_area)
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        return max_area
height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))