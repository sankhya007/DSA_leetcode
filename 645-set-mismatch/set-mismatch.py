from collections import Counter

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        res = [0, 0] #duplicate, not found

        for i in range(1, len(nums)+1): 
            if count[i] == 0: # means not found
                res[1] = i 
            if count[i] == 2: # means seen twice in the array
                res[0] = i
        # 1 will not give us anything because that is the optimal number of how many times a number should be visible

        return res
