class Solution():
    def rowAndMaximumOnes(self, mat): 
        max_ones = 0 
        row_index = 0 # this does not have to be -1 

        for i in range(len(mat)):
            current_ones = sum(mat[i]) # just gonna add all the values and because it is 1s and 0s ony the 1s are gonna add up and then the sum will be the total number of 1s 
            if current_ones > max_ones: 
                max_ones = current_ones 
                row_index = i # return the index of that specific row 

        return [row_index, max_ones]

mat = [[0,0],[1,1],[0,0]]
solution = Solution()
print(solution.rowAndMaximumOnes(mat))

            