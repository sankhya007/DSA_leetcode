class Solution:
    def minimumDeletions(self, nums): 
        n = len(nums)
        if n <= 2: 
            return n
        min_index = 0
        max_index = 0
        for i in range(1, n): 
            if nums[i] > nums[min_index]: 
                min_index = i
            elif nums[i] < nums[max_index]: 
                max_index = i
        left = min(min_index, max_index)
        right = max(min_index, max_index)
        opt1 = right + 1
        opt2 = n - left 
        opt3 = (left + 1) + (n - right)
        return min(opt1, opt2, opt3)