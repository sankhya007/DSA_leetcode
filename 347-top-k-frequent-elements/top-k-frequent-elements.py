class Solution: 
	def topKFrequent(self, nums, k): 

		# storage
		count = {}

		# counting the frequency
		for num in nums: 
			count[num] = count.get(num, 0) + 1

		# sorting them in descending order (by frequency)
		sorted_nums = sorted(count, key=count.get, reverse=True)

		# return until k 
		return sorted_nums[:k]