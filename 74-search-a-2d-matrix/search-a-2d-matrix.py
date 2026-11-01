class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        # solution woll not work due to time complexity restrictions
        # for array in matrix:
        #     left = 0 
        #     right = len(array) - 1
        #     while left < right: 
        #         mid = left + (right - left) // 2
        #         if array[mid] == target: 
        #             return True
        #         if array[mid] < target: 
        #             left = mid + 1
        #         else: 
        #             right = mid
        #     return False

        if not matrix and not matrix[0]: 
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

            if mid_value < target: 
                left = mid + 1

            else: 
                right = mid - 1

        return False
