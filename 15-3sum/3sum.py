# 3 sum - leetcode 

class Solution(): 
	def threeSum(self, nums): 

		nums.sort()
		triplets = []

		for i in range(len(nums) - 2): 

			# condition: if the number same - skip 
			if i > 0 and nums[i] == nums[i - 1]: 
				continue 

			# sliding window(working with "i")
			left = i + 1
			right = len(nums) - 1

			while left < right: 
				# calculation of current_sum
				current_sum = nums[i] + nums[left] + nums[right]

				if current_sum == 0: 
					# when 0, append and move to next
					triplets.append([nums[i], nums[left], nums[right]])
					left += 1
					right -= 1

					# condition: if same, move onto next
					while left < right and nums[left] == nums[left - 1]: 
						left += 1 
					while left < right and nums[right] == nums[right + 1]:
						right -= 1

				# works because the array is sorted
				elif current_sum < 0: 
					left += 1
				# current_sum > 0
				else: 
					right -= 1

		return triplets



