class Solution(): 
	def majorityElement(self, nums): 
		n = len(nums)//2
		nums.sort()
		return nums[n]

# index:  0  1  2  3  4  5  6
#         ↓  ↓  ↓  ↓  ↓  ↓  ↓
# nums:  [1, 1, 1, 2, 2, 2, 2]
#                   ↑
#                 nums[3]

# this is why the nums n work 