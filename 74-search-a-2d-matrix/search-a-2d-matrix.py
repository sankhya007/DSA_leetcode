class Solution:
    def searchMatrix(self, matrix, target): 
        if not matrix: # if matrix empty
            return False
        
        rows = len(matrix)
        cols = len(matrix[0]) #initialize vals
        left = 0 
        right = rows * cols - 1 # the last element in 2d array 
    
        while left <= right: 
            mid = left + (right - left) // 2 # this is how it is 
            mid_value = matrix[mid // cols][mid % cols] # this is also how it is 

            if mid_value == target: # fkn easy asf logic
                return True
            elif mid_value < target: 
                left = mid + 1
            else: # mid_value > target
                right = mid - 1
        
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))