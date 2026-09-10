# two sum, input array sorted - leetcode 

class Solution(): 
	def twoSum(self, numbers, target): 

		# pointers 
		left = 0 
		right = len(numbers) - 1

		# initial condition
		while left < right: 

			# current_sum calculation 
			current_sum = numbers[left] + numbers[right]

			# if sum same as target, return position
			if current_sum == target: 
				return [left + 1, right + 1] 

			# when sum smaller, move further up in array
			elif current_sum < target: 
				left += 1 

			# when sum larger, move further down in array
			elif current_sum > target: 
				right -= 1

		return None


numbers = [2,7,11,15]
target = 9 

sol = Solution() 
print(sol.twoSum(numbers, target))