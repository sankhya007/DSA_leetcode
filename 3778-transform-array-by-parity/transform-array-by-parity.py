class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        
        count_even = 0
        n = len(nums)
        array = [1]*n 

        for num in nums: 
            if num % 2 == 0: 
                count_even += 1

        for i in range(0, count_even, 1): 
            array[i] = 0 

        return array
