class Solution: 
    def spiralOrder(self, matrix): 
        if not matrix: 
            return []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        storage = []
        while left <= right and top <= bottom: 
            for j in range(left, right + 1): 
                storage.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1): 
                storage.append(matrix[i][right])
            right -= 1
            if top <= bottom: 
                for j in range(right, left - 1, -1):
                    storage.append(matrix[bottom][j])
                bottom -= 1
            if left <= right: 
                for i in range(bottom, top - 1, -1): 
                    storage.append(matrix[i][left])
                left += 1
        return storage
