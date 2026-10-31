class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        k = 0 

        for x in nums: 
            # k < 2 just so we include 2 items and then we can keep on comparing
            # if the item we have now is same as 2 previous spaces, skip. else add
            if k < 2 or x != nums[k - 2]: 
                nums[k] = x
                k += 1

        return k 
                

