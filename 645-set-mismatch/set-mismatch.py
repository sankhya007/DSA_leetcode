class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        res = [0, 1]
        nums.sort()

        for i in range(1, len(nums)): 
            if nums[i] == nums[i - 1]: 
                res[0] = nums[i]
            elif nums[i] - nums[i - 1] == 2: # should be 1
                res[1] = nums[i] - 1

        # if the last number is not same as the length meaning the last element is the duplicate so that is why we have to keep the len of the given array as the 2nd element if res
        if nums[-1] != len(nums): 
            res[1] = len(nums)

        return res