class Solution(object):
    def removeElement(self, nums, val):
        count = 0 
        for num in nums: 
            if num != val: 
                nums[count] = num
                count += 1
        return count