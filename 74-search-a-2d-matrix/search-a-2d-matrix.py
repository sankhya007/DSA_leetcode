class Solution:
    def searchMatrix(self, matrix, target): 
        if not matrix: 
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0 
        right = rows * cols - 1
    
        while left <= right: 
            mid = left + (right - left) // 2
            mid_value = matrix[mid // cols][mid % cols]

            if mid_value == target: 
                return True
            elif mid_value < target: 
                left = mid + 1
            else: 
                right = mid - 1
        
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))