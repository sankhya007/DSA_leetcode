# split array largest sum 

class Solution(): 
	def splitArray(self, nums, k): 

		# total is suppose to be higher than max number to fit in one array
		left = max(nums)
		right = sum(nums)

		while left <= right: 

			mid = (left + right) // 2

			# start with 1 sub array(co minimum)
			subarray = 1 
			current_sum = 0 

			# initial loop in numbers
			for num in nums: 

				# if more than mid, create a new sub-array
				if num + current_sum > mid: 
					subarray += 1 
					# current-sum refresh
					current_sum = num 

				# else just add to current sum
				else: 
					current_sum += num

			# try out with a bigger mid, so allow more number in array
			if subarray <= k: 
				right = mid - 1

			# try out with smaller mid so have less max number in array
			else: 
				left = mid + 1 

		return left


nums = [7,2,5,10,8]
k = 2

sol = Solution()
print(sol.splitArray(nums, k))