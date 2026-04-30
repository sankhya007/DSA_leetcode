class Solution:
    def removeDuplicates(self, nums): 

        if not nums: 
            return "the list is empty"
            # this is done in case the list if elements is empty

        left = 0
        for right in range(1, len(nums)):
            # here we start from 1, or else the left and right will be the same number 
            if nums[left] != nums[right]: 
                left += 1
                # this is changing the index
                nums[left] = nums[right]
                # this is changing the value in the list

        return left + 1
        # we increment the value by 1 because we need the length of the list and the left is the 2nd last value of the list so if we return than we could not get the actual length and thats why we return the value incremented by 1

nums = [0,0,1,1,1,2,2,3,3,4]

solution = Solution()
new_length = solution.removeDuplicates(nums)
print(f"the new length of the new list is : {new_length},                                                       and {nums[:new_length]} is the new list, without duplicates.")