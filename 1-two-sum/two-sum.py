class Solution(): 
	def twoSum(self, nums, target): 
		storage = {}

		for i, num in enumerate(nums): 
			complement = target - num 

			if complement in storage: 
				return [storage[complement], i]

			# if the complement not in storage
			storage[num] = i 

solution = Solution()
nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums, target))