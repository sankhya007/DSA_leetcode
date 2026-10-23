# move zeros

class Solution: 
    def moveZeroes(self, nums): 

        index = 0
        # can not create a new array

        for num in nums: 
            if num != 0: 
                nums[index] = num 
                index += 1
            else: 
                continue
        # shift numbers till it is possible to do so

        # start from where the index left off and continue till end
        for i in range(index, len(nums)): 
            nums[i] = 0
        # the rest becomes zero

        return nums