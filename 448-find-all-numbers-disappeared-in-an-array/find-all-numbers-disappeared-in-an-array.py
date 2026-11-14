class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        length = len(nums)
        array = []
        num_set = set(nums)

        for i in range(1, length+1): 
            if i not in num_set: 
                array.append(i)
            
        return array