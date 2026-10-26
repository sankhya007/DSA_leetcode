class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]

        for i in range(1, numRows): 
            prev = triangle[-1] # select the last element
            row = [1] # add the 1st 1in the row 
            for j in range(1, i): # loop at many times we need
                row.append(prev[j -1] + prev[j]) # add the existing two values and move forward by one increment
            row.append(1) # add the last 1 
            triangle.append(row) # append the row itself 

        return triangle