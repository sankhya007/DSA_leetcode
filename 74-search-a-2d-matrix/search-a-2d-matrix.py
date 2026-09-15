# search in a 2d matrix 

class Solution(): 
	def searchMatrix(self, matrix, target): 

		# check if the matrix is empty
		if not matrix and not matrix[0]: 
			return False 

		# count rows and cols
		rows = len(matrix)
		cols = len(matrix[0])

		# pointers
		left = 0 
		right = rows * cols - 1 # last element rows*cols

		# initial loop 
		while left <= right: 

			# mid number
			mid = left + (right - left) // 2 
			# value col
			mid_value = matrix[mid // cols][mid % cols]

			# if same return
			if mid_value == target: 
				return True

			# if value bigger than mid, leave out left part 
			elif mid_value < target: 
				left = mid + 1 

			# if value smaller, leave out right part
			else: 
				right = mid - 1 

		return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

sol = Solution()
print(sol.searchMatrix(matrix, target))