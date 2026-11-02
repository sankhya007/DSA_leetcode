class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        
        nums.sort()
        left = 0 
        actual_total = 0 # this will store the actual sum of the numbers that we have in the sliding window
        res = 0 # memory store element

        for right in range(len(nums)): 
            actual_total += nums[right] # one by one we are adding the right values in the total and making the sliding window bigger 
            while nums[right] * (right - left + 1) > actual_total + k: 
                '''
                k is actually our budget, meaning how much can we actually add 
                and by adding k to the actual sum we get how much we can actually increment the value that we have in the 1st place
                multiple of nums[right] and the length of the siding window(assuming the value in the right is bigger than any value in the left because we already have sorted the array) for the array to have the same elements the sum will be the value that we calculated
                '''
                # if the value is actually bigger then we have to make the window smaller, for that remove the value form left and left increment
                actual_total -= nums[left]
                left += 1

            # the max the window size we got in the array's lifetime
            res = max(res, right - left + 1)

        return res


nums = [1,2,4]
k = 5

sol = Solution()
print(sol.maxFrequency(nums, k))