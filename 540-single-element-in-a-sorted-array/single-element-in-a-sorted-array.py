# single element in a sorted array 

class Solution(object):
    def singleNonDuplicate(self, nums):
    	for i in range(len(nums)): 

    		# pointers 
    		left = 0 
    		right = len(nums) - 1

    		while left < right: 
    			mid = (left + right) // 2 

    			# turn the mid into a even number
    			if mid % 2 == 1: 
    				mid -= 1 

    			# if the numbers are same that means numbers on the left are sorted, we move to the right section
    			if nums[mid] == nums[mid + 1]: 
    				left = mid + 2 

    			# if not then the fucker is in the left, hunt him down
    			else: 
    				right = mid

    		return nums[left]


nums = [1,1,2,3,3,4,4,8,8]

sol = Solution()
print(sol.singleNonDuplicate(nums))