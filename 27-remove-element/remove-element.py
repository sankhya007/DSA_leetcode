class Solution:
    def removeElement(self, nums, val): 
        left = 0 
        for right in range(len(nums)): 
            if nums[right] != val: 
                nums[left] = nums[right]
                left += 1
        return left 

nums = [0,1,2,2,3,0,4,2]
val = 2
solution = Solution()
length = solution.removeElement(nums, val)
print(f"the new length of the array is : {length},                                                              the new list contains {nums[:length]} these elements")
# here we are ending just before the duplication of the elements starts