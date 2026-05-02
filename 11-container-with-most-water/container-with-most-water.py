class Solution:
    def maxArea(self, height): 
        left = 0 
        right = len(height) - 1
        max_area = 0 # container to store the max_area because that function is not getthing called inside the loop 

        while left < right: 
            width = right - left # width is just a value we created just to do the multiplicaiton and that is dependent on the index because there is no other factor there is to multiply with the height
            current_area = min(height[right], height[left]) * width 
            max_area = max(max_area, current_area)

            if height[left] < height[right]: # here we need to use the values in the height because if not then we would be using the index and that's not right
                left += 1
            else: 
                right -= 1

        return max_area

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))