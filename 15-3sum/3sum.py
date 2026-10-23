# 3sum - leetcode 

class Solution(): 
    def threeSum(self, nums): 

        nums.sort()
        triplets = []

        for i in range(len(nums) - 2): 

            # if number same, skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # because the nums[i] is the 1st number
            left = i + 1
            right = len(nums) - 1

            # left is the number right next to the num 
            # right is the last element from the array
            while left < right: 
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0: 
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1 
                    right -= 1 

                    # after the left and the right have been incremented towards the middle then check if the number matches or nah
                    # if match increment another
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # coz already sorted
                elif current_sum < 0: 
                    left += 1 

                else: 
                    right -= 1 


        return triplets