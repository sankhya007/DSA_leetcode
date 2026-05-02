class Solution:
    def subarraySum(self, nums, k): 
        count = 0 
        current_sum = 0
        sub_array = {0:1}
        for num in nums: 
            current_sum += num
            if current_sum - k in sub_array: 
                count += sub_array[current_sum - k]
            sub_array[current_sum] = sub_array.get(current_sum , 0) + 1
        return count
nums = [1,1,1]
k = 2
solution = Solution()
print(solution.subarraySum(nums, k))