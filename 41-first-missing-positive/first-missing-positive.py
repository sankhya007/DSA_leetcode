class Solution(object):
    def firstMissingPositive(self, nums):
        num_set = set(nums)
        # if i is a positive number it can not turn into negitive in the following code
        # so we start with i being a positive number, if the positive number in set we increment 
        # if the positive number not in set, return the incremented number
        # no matter where we are in the array we will get the 1st positive number 
        i = 1
        while i in num_set: 
            i += 1 
        return i 