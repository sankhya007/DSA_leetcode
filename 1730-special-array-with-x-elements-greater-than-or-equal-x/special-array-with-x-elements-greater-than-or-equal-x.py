class Solution:
    def specialArray(self, nums: list[int]) -> int:

        for x in range(1, len(nums) + 1):
            count = 0 
            for num in nums: 
                if num >= x:
                    count += 1
            # if count and the assumed length matches return x
            if count == x: 
                return x 
        
        return -1 
