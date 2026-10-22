# maximum sub-array 

class Solution(): 
    def maxSubArray(self, nums): 

        max_local = max_global = nums[0] # the 1st element

        for i in range(1, len(nums)): # remove the 1st element and count

            # compare with current number(because one number can also be the max sub-array) and addition
            max_local = max(nums[i], max_local + nums[i])

            # compare
            if max_local > max_global: 
                max_global = max_local

        return max_global