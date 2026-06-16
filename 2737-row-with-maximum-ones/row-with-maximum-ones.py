class Solution: 
    def rowAndMaximumOnes(self, mat): 
        max_ones = 0 
        one_index = 0
        for i in range(len(mat)): 
            current_sum = sum(mat[i])
            if current_sum > max_ones: 
                max_ones = current_sum
                one_index = i
        return [one_index, max_ones]