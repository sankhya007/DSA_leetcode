class Solution:
    def threeSum(self, nums): 
        nums.sort() # sorting in a non descending order
        triplets = [] # storage to add the triplets

        for i in range(len(nums) - 2): # here -2 because there are 3 elements and we need to stop at the 2nd last to get 3 elements to calculate with 
            if i > 0 and nums[i] == nums[i - 1]: # here the i > 0 is important because if the list only have 0's  then it the whole calculation underneath is not going to work 
                continue # skip the duplicate 

            left = i + 1 # point to the 2nd val in the triplets
            right = len(nums) - 1 # point to the 3rd val in the triplets

            while left < right: 
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0: 
                    triplets.append([nums[i] ,nums[left] ,nums[right]]) # here the append is done in a 2d array because there could be multiple emenets  that are adding upto zero, and to do that we need to add more than one triplets in the stoorage we made that's why 2d array is used 
                    left += 1
                    right -= 1
                    # above is the basic calculation, and now we need to worry about the duplicates in the left or the right 

                    while left < right and nums[left] == nums[left - 1]: # duplicate in the left index
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]: # duplicate in the right index
                        right -= 1 
                
                elif current_sum < 0: # coz it is non descending if we have value in negative then we can just shift the left index by 1 and the total will increase
                    left += 1

                else: # current_sum > 0
                    right -= 1

        return triplets

nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))
    