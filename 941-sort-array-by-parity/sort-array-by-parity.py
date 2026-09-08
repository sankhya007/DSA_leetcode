class Solution(object):
    def sortArrayByParity(self, nums):
        even = []
        odd = []

        # do i even need to explain 
        for num in nums: 
            if num % 2 == 0: 
                even.append(num)
            else: 
                odd.append(num)

        return even + odd 