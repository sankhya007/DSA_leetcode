class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # so we have to keep this in the sub array and everything else that will make x will be outside of the calculation
        target = sum(nums) - x
        left = 0 
        current_sum = 0 
        window_max = -1 # because if we do not find a way to match the target itself then we return -1

        for right in range(len(nums)): 
            current_sum += nums[right]

            while left <= right and current_sum > target: 
                current_sum -= nums[left]
                left += 1

            if current_sum == target: 
                # by saying window max i mean what ever the number of characters that the sliding window actually contains when it matches all the given statements
                # because if the given statements are matched then that is the number of elements that we have to remove
                window_max = max(window_max, right - left + 1)

        # we are returning len - max_window because the target that we have fulfilled is actually the opposite of the given target, the one that we have to keep on the given array, and not the one that we have to remove. That's why the negation
        return -1 if window_max == -1 else len(nums) - window_max

nums = [1,1,4,2,3]
x = 5

sol = Solution()
print(sol.minOperations(nums, x))