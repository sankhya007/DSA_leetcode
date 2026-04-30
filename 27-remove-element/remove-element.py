class Solution:
    def removeElement(self, nums, val): 
        left = 0 
        for right in range(len(nums)): 
            if nums[right] != val: 
                nums[left] = nums[right]
                # this line is to change the value on the list this is doing nothing to the index
                left += 1
                # this line is to change the index, increment by +1
        return left 

nums = [0,1,2,2,3,0,4,2]
val = 2
solution = Solution()
length = solution.removeElement(nums, val)
print(f"the new length of the array is : {length},                                                              the new list contains {nums[:length]} these elements")
# here we are ending just before the duplication of the elements starts 
# because we are not actually changing the length of the array we are removing the elements that we do nto need and then just printing the changed poortion according to our needs 