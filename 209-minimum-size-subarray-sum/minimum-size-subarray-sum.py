# minimum size sub-array sum

class Solution(): 
    def minSubArrayLen(self, target, nums): 

        left = 0 
        current_sum = 0 
        min_length = float("inf")

        for right in range(len(nums)): 
            current_sum += nums[right]

            # when sum s more than target
            while current_sum >= target: 
                # right - left + 1 is the length of the current window
                min_length = min(min_length, right - left + 1)

                # negate the number from the far left
                current_sum -= nums[left]
                # left index increase
                left += 1 

        # return 0 if not found, else the length
        return 0 if min_length == float("inf") else min_length